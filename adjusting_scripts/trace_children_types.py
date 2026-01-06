import argparse
import ast
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


@dataclass
class ClassInfo:
    name: str
    module: str
    bases: List[str]
    node: ast.ClassDef
    match_returns: List[List[Set[str]]]
    init_params: List[str]
    init_vararg: Optional[str]
    items_assigns: List[ast.AST]
    content_assigns: List[ast.AST]


def _base_name(expr: ast.expr) -> Optional[str]:
    if isinstance(expr, ast.Name):
        return expr.id
    if isinstance(expr, ast.Attribute):
        return expr.attr
    return None


def _infer_types(expr: ast.AST, known_classes: Set[str]) -> Set[str]:
    if isinstance(expr, ast.Name):
        if expr.id in known_classes:
            return {expr.id}
        return {f"var:{expr.id}"}
    if isinstance(expr, ast.Attribute):
        if expr.attr in known_classes:
            return {expr.attr}
        return {f"attr:{expr.attr}"}
    if isinstance(expr, ast.Call):
        func_name = _base_name(expr.func)
        if func_name in known_classes:
            return {func_name}
        if func_name in {"str", "int", "float", "bool", "list", "tuple"}:
            return {func_name}
        return {f"call:{func_name}" if func_name else "call:unknown"}
    if isinstance(expr, ast.Constant):
        if expr.value is None:
            return {"None"}
        if isinstance(expr.value, bool):
            return {"bool"}
        if isinstance(expr.value, int):
            return {"int"}
        if isinstance(expr.value, float):
            return {"float"}
        if isinstance(expr.value, str):
            return {"str"}
        return {type(expr.value).__name__}
    if isinstance(expr, (ast.List, ast.Tuple)):
        types: Set[str] = set()
        for element in expr.elts:
            types.update(_infer_types(element, known_classes))
        return types or {"empty"}
    if isinstance(expr, ast.IfExp):
        types = _infer_types(expr.body, known_classes)
        types.update(_infer_types(expr.orelse, known_classes))
        return types
    if isinstance(expr, ast.JoinedStr):
        return {"str"}
    return {"unknown"}


def _collect_match_returns(
    node: ast.ClassDef, known_classes: Set[str]
) -> List[List[Set[str]]]:
    returns: List[List[Set[str]]] = []
    for item in node.body:
        if isinstance(item, ast.FunctionDef) and item.name == "match":
            for child in ast.walk(item):
                if isinstance(child, ast.Return) and child.value is not None:
                    value = child.value
                    if isinstance(value, (ast.Tuple, ast.List)):
                        return_types: List[Set[str]] = []
                        for element in value.elts:
                            return_types.append(_infer_types(element, known_classes))
                        returns.append(return_types)
    return returns


def _collect_init_info(
    node: ast.ClassDef,
) -> Tuple[List[str], Optional[str], List[ast.AST], List[ast.AST]]:
    params: List[str] = []
    vararg: Optional[str] = None
    items_assigns: List[ast.AST] = []
    content_assigns: List[ast.AST] = []

    for item in node.body:
        if isinstance(item, ast.FunctionDef) and item.name in {"init", "__init__"}:
            args = item.args
            params = [arg.arg for arg in args.args if arg.arg != "self"]
            vararg = args.vararg.arg if args.vararg else None
            for child in ast.walk(item):
                if isinstance(child, (ast.Assign, ast.AnnAssign)):
                    targets = []
                    if isinstance(child, ast.Assign):
                        targets = child.targets
                        value = child.value
                    else:
                        targets = [child.target]
                        value = child.value
                    for target in targets:
                        if (
                            isinstance(target, ast.Attribute)
                            and isinstance(target.value, ast.Name)
                            and target.value.id == "self"
                        ):
                            if target.attr == "items":
                                if value is not None:
                                    items_assigns.append(value)
                            if target.attr == "content":
                                if value is not None:
                                    content_assigns.append(value)
    return params, vararg, items_assigns, content_assigns


def _merge_match_types(
    match_returns: List[List[Set[str]]],
) -> List[Set[str]]:
    merged: List[Set[str]] = []
    for return_tuple in match_returns:
        for index, types in enumerate(return_tuple):
            while len(merged) <= index:
                merged.append(set())
            merged[index].update(types)
    return merged


def _format_union(types: Iterable[str]) -> str:
    types_list = sorted(t for t in types if t)
    if not types_list:
        return "unknown"
    if len(types_list) == 1:
        return types_list[0]
    return " | ".join(types_list)


def _build_children_patterns(
    match_returns: List[List[Set[str]]],
    items_types: Set[str],
    content_types: Set[str],
) -> List[str]:
    patterns: Set[str] = set()
    for return_tuple in match_returns:
        union_parts = [_format_union(types) for types in return_tuple]
        if union_parts:
            patterns.add(f"Tuple[{', '.join(union_parts)}]")
    if not patterns:
        union_types = items_types | content_types
        if union_types:
            patterns.add(f"List[{_format_union(union_types)}]")
    return sorted(patterns)


def _types_for_param(
    param: str,
    param_index: int,
    vararg: Optional[str],
    match_types: List[Set[str]],
) -> Set[str]:
    if param == vararg:
        types: Set[str] = set()
        for entry in match_types:
            types.update(entry)
        return types or {"unknown"}
    if param_index < len(match_types):
        return match_types[param_index] or {"unknown"}
    return {"unknown"}


def _extract_children_types(
    info: ClassInfo, known_classes: Set[str]
) -> Tuple[Set[str], Set[str], Set[str]]:
    items_types: Set[str] = set()
    content_types: Set[str] = set()
    unknown_types: Set[str] = set()
    match_types = _merge_match_types(info.match_returns)
    param_to_index = {name: index for index, name in enumerate(info.init_params)}

    for expr in info.items_assigns:
        if isinstance(expr, ast.Name) and expr.id in param_to_index:
            types = _types_for_param(
                expr.id, param_to_index[expr.id], info.init_vararg, match_types
            )
        elif isinstance(expr, ast.Name) and expr.id == info.init_vararg:
            types = _types_for_param(expr.id, -1, info.init_vararg, match_types)
        else:
            types = _infer_types(expr, known_classes)
        if "unknown" in types:
            unknown_types.update(types)
        items_types.update(types)

    for expr in info.content_assigns:
        if isinstance(expr, ast.Name) and expr.id in param_to_index:
            types = _types_for_param(
                expr.id, param_to_index[expr.id], info.init_vararg, match_types
            )
        elif isinstance(expr, ast.Name) and expr.id == info.init_vararg:
            types = _types_for_param(expr.id, -1, info.init_vararg, match_types)
        else:
            types = _infer_types(expr, known_classes)
        if "unknown" in types:
            unknown_types.update(types)
        content_types.update(types)

    if not items_types and not content_types and match_types:
        for match_entry in match_types:
            items_types.update(match_entry)

    return items_types, content_types, unknown_types


def _iter_python_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.py"):
        if path.is_file():
            yield path


def analyze_tree(root: Path) -> Dict[str, Dict[str, object]]:
    class_infos: Dict[str, ClassInfo] = {}
    class_name_to_keys: Dict[str, List[str]] = defaultdict(list)
    all_class_names: Set[str] = set()

    for path in _iter_python_files(root):
        module = str(path.relative_to(root))
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                base_names = [
                    name
                    for base in node.bases
                    for name in [_base_name(base)]
                    if name
                ]
                key = f"{module}:{node.name}"
                info = ClassInfo(
                    name=node.name,
                    module=module,
                    bases=base_names,
                    node=node,
                    match_returns=[],
                    init_params=[],
                    init_vararg=None,
                    items_assigns=[],
                    content_assigns=[],
                )
                class_infos[key] = info
                class_name_to_keys[node.name].append(key)
                all_class_names.add(node.name)

    known_base_names: Set[str] = {"Base"}
    subclass_keys: Set[str] = set()
    updated = True
    while updated:
        updated = False
        for key, info in class_infos.items():
            if key in subclass_keys:
                continue
            if any(base in known_base_names for base in info.bases):
                subclass_keys.add(key)
                if info.name not in known_base_names:
                    known_base_names.add(info.name)
                    updated = True

    for info in class_infos.values():
        info.match_returns = _collect_match_returns(info.node, all_class_names)
        (
            info.init_params,
            info.init_vararg,
            info.items_assigns,
            info.content_assigns,
        ) = _collect_init_info(info.node)

    results: Dict[str, Dict[str, object]] = {}
    for key in sorted(subclass_keys):
        info = class_infos[key]
        items_types, content_types, unknown_types = _extract_children_types(
            info, all_class_names
        )
        children_types = sorted(items_types | content_types)
        children_patterns = _build_children_patterns(
            info.match_returns, items_types, content_types
        )
        results[key] = {
            "module": info.module,
            "class_name": info.name,
            "children_types": children_types,
            "children_patterns": children_patterns,
            "items_types": sorted(items_types),
            "content_types": sorted(content_types),
            "unknown_types": sorted(unknown_types),
        }

    return results


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze Base subclasses and infer .children return types."
    )
    parser.add_argument(
        "--root",
        default="src/fparser/two/Fortran2003/nodes",
        help="Root directory to scan for Python files.",
    )
    parser.add_argument(
        "--output",
        default="children_types.json",
        help="Output JSON file path.",
    )
    args = parser.parse_args()

    root = Path(args.root)
    results = analyze_tree(root)
    output_path = Path(args.output)
    output_path.write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {len(results)} classes to {output_path}")


if __name__ == "__main__":
    main()