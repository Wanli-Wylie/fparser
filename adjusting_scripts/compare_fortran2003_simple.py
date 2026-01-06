#!/usr/bin/env python3
"""
系统性对比 Fortran2003 模块的旧版本（.bak文件）和新版本（重构后的目录结构）

这个版本通过解析源代码文件来对比，而不是导入模块，避免循环导入问题。

对比内容包括：
1. 导出的类和函数
2. 类的定义（签名、方法、属性等）
3. 类的继承关系
4. 模块级别的变量和常量
5. 导入的依赖
6. 类的数量统计
7. 类的差异（新增、删除、修改）
"""

import sys
import re
import ast
from pathlib import Path
from typing import Dict, Set, List, Tuple, Any, Optional
from collections import defaultdict


class SourceCodeAnalyzer:
    """分析源代码文件，提取类、函数等信息"""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = ""
        self.tree = None
        self.classes = {}
        self.functions = {}
        self.imports = set()
        self.constants = {}
        
    def parse(self):
        """解析源代码文件"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            
            # 解析AST
            try:
                self.tree = ast.parse(self.content)
            except SyntaxError as e:
                print(f"  警告: 解析AST失败: {e}")
                # 如果AST解析失败，使用正则表达式作为后备
                self._parse_with_regex()
                return
            
            # 提取信息
            self._extract_classes()
            self._extract_functions()
            self._extract_imports()
            self._extract_constants()
            
        except Exception as e:
            print(f"  错误: 无法读取文件 {self.file_path}: {e}")
    
    def _parse_with_regex(self):
        """使用正则表达式解析（当AST解析失败时）"""
        # 提取类定义
        class_pattern = r'^class\s+(\w+)\s*\([^)]*\):'
        for match in re.finditer(class_pattern, self.content, re.MULTILINE):
            class_name = match.group(1)
            self.classes[class_name] = {'name': class_name, 'line': self._get_line_number(match.start())}
        
        # 提取函数定义
        func_pattern = r'^def\s+(\w+)\s*\([^)]*\):'
        for match in re.finditer(func_pattern, self.content, re.MULTILINE):
            func_name = match.group(1)
            self.functions[func_name] = {'name': func_name, 'line': self._get_line_number(match.start())}
        
        # 提取导入
        import_pattern = r'^(?:from\s+([\w.]+)\s+)?import\s+([^\n]+)'
        for match in re.finditer(import_pattern, self.content, re.MULTILINE):
            module = match.group(1) or match.group(2).split('.')[0]
            imports = match.group(2).split(',')
            for imp in imports:
                name = imp.strip().split(' as ')[0].split('.')[0]
                self.imports.add(name)
    
    def _get_line_number(self, pos):
        """获取字符位置对应的行号"""
        return self.content[:pos].count('\n') + 1
    
    def _extract_classes(self):
        """从AST提取类定义"""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                bases = [self._get_name(base) for base in node.bases]
                methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
                attrs = [n.targets[0].id for n in node.body 
                        if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)]
                
                self.classes[node.name] = {
                    'name': node.name,
                    'bases': bases,
                    'methods': set(methods),
                    'attrs': set(attrs),
                    'line': node.lineno,
                }
    
    def _extract_functions(self):
        """从AST提取函数定义"""
        # 使用访问者模式来提取模块级别的函数
        class FunctionVisitor(ast.NodeVisitor):
            def __init__(self, functions_dict):
                self.functions = functions_dict
                self.in_class = False
            
            def visit_ClassDef(self, node):
                old_in_class = self.in_class
                self.in_class = True
                self.generic_visit(node)
                self.in_class = old_in_class
            
            def visit_FunctionDef(self, node):
                if not self.in_class:  # 只提取模块级别的函数
                    self.functions[node.name] = {
                        'name': node.name,
                        'line': node.lineno,
                    }
                self.generic_visit(node)
        
        visitor = FunctionVisitor(self.functions)
        visitor.visit(self.tree)
    
    def _extract_imports(self):
        """从AST提取导入语句"""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    self.imports.add(node.module.split('.')[0])
    
    def _extract_constants(self):
        """从AST提取常量（大写变量）"""
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.isupper():
                        try:
                            value = ast.literal_eval(node.value)
                            self.constants[target.id] = value
                        except:
                            pass
    
    def _get_name(self, node):
        """获取AST节点的名称"""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        else:
            return str(node)


class DirectoryAnalyzer:
    """分析目录中的所有Python文件"""
    
    def __init__(self, dir_path: Path):
        self.dir_path = dir_path
        self.analyzers = {}
        self.classes = {}
        self.functions = {}
        self.imports = set()
        self.constants = {}
        
    def analyze(self):
        """分析目录中的所有Python文件"""
        py_files = list(self.dir_path.rglob("*.py"))
        
        for py_file in py_files:
            analyzer = SourceCodeAnalyzer(py_file)
            analyzer.parse()
            self.analyzers[str(py_file)] = analyzer
            
            # 合并结果
            self.classes.update(analyzer.classes)
            self.functions.update(analyzer.functions)
            self.imports.update(analyzer.imports)
            self.constants.update(analyzer.constants)


class ModuleComparator:
    """对比两个版本的 Fortran2003 模块"""
    
    def __init__(self, old_module_path: str, new_module_path: str):
        self.old_module_path = Path(old_module_path)
        self.new_module_path = Path(new_module_path)
        self.old_analyzer = None
        self.new_analyzer = None
        
    def analyze(self):
        """分析两个版本"""
        print("=" * 80)
        print("分析源代码文件...")
        print("=" * 80)
        
        # 分析旧版本（单文件）
        print(f"\n分析旧版本: {self.old_module_path}")
        self.old_analyzer = SourceCodeAnalyzer(self.old_module_path)
        self.old_analyzer.parse()
        print(f"  类数量: {len(self.old_analyzer.classes)}")
        print(f"  函数数量: {len(self.old_analyzer.functions)}")
        print(f"  导入数量: {len(self.old_analyzer.imports)}")
        print(f"  常量数量: {len(self.old_analyzer.constants)}")
        
        # 分析新版本（目录）
        print(f"\n分析新版本: {self.new_module_path}")
        self.new_analyzer = DirectoryAnalyzer(self.new_module_path)
        self.new_analyzer.analyze()
        print(f"  文件数量: {len(self.new_analyzer.analyzers)}")
        print(f"  类数量: {len(self.new_analyzer.classes)}")
        print(f"  函数数量: {len(self.new_analyzer.functions)}")
        print(f"  导入数量: {len(self.new_analyzer.imports)}")
        print(f"  常量数量: {len(self.new_analyzer.constants)}")
    
    def compare_classes(self):
        """对比类"""
        print("\n" + "=" * 80)
        print("对比类定义")
        print("=" * 80)
        
        old_class_names = set(self.old_analyzer.classes.keys())
        new_class_names = set(self.new_analyzer.classes.keys())
        
        added_classes = new_class_names - old_class_names
        removed_classes = old_class_names - new_class_names
        common_classes = old_class_names & new_class_names
        
        print(f"\n类统计:")
        print(f"  旧版本类数量: {len(old_class_names)}")
        print(f"  新版本类数量: {len(new_class_names)}")
        print(f"  共同类数量: {len(common_classes)}")
        print(f"  新增类数量: {len(added_classes)}")
        print(f"  删除类数量: {len(removed_classes)}")
        
        # 详细对比共同类
        modified_classes = []
        
        print(f"\n对比共同类 ({len(common_classes)} 个)...")
        for class_name in sorted(common_classes):
            old_cls = self.old_analyzer.classes[class_name]
            new_cls = self.new_analyzer.classes[class_name]
            
            # 对比继承关系
            old_bases = set(old_cls.get('bases', []))
            new_bases = set(new_cls.get('bases', []))
            
            # 对比方法
            old_methods = old_cls.get('methods', set())
            new_methods = new_cls.get('methods', set())
            
            # 对比属性
            old_attrs = old_cls.get('attrs', set())
            new_attrs = new_cls.get('attrs', set())
            
            # 检查是否有变化
            bases_changed = old_bases != new_bases
            methods_changed = old_methods != new_methods
            attrs_changed = old_attrs != new_attrs
            
            if bases_changed or methods_changed or attrs_changed:
                modified_classes.append({
                    'name': class_name,
                    'bases_changed': bases_changed,
                    'old_bases': old_bases,
                    'new_bases': new_bases,
                    'methods_changed': methods_changed,
                    'old_methods': old_methods,
                    'new_methods': new_methods,
                    'attrs_changed': attrs_changed,
                    'old_attrs': old_attrs,
                    'new_attrs': new_attrs,
                })
        
        # 输出结果
        if added_classes:
            print(f"\n新增类 ({len(added_classes)} 个):")
            for name in sorted(list(added_classes))[:20]:
                print(f"  + {name}")
            if len(added_classes) > 20:
                print(f"  ... 还有 {len(added_classes) - 20} 个")
        
        if removed_classes:
            print(f"\n删除类 ({len(removed_classes)} 个):")
            for name in sorted(list(removed_classes))[:20]:
                print(f"  - {name}")
            if len(removed_classes) > 20:
                print(f"  ... 还有 {len(removed_classes) - 20} 个")
        
        if modified_classes:
            print(f"\n修改的类 ({len(modified_classes)} 个):")
            for info in modified_classes[:10]:
                print(f"\n  {info['name']}:")
                if info['bases_changed']:
                    print(f"    继承关系变化:")
                    print(f"      旧: {sorted(info['old_bases'])}")
                    print(f"      新: {sorted(info['new_bases'])}")
                if info['methods_changed']:
                    added_methods = info['new_methods'] - info['old_methods']
                    removed_methods = info['old_methods'] - info['new_methods']
                    if added_methods:
                        print(f"    新增方法: {sorted(list(added_methods))[:5]}")
                        if len(added_methods) > 5:
                            print(f"      ... 还有 {len(added_methods) - 5} 个")
                    if removed_methods:
                        print(f"    删除方法: {sorted(list(removed_methods))[:5]}")
                        if len(removed_methods) > 5:
                            print(f"      ... 还有 {len(removed_methods) - 5} 个")
            if len(modified_classes) > 10:
                print(f"  ... 还有 {len(modified_classes) - 10} 个修改的类未显示")
        
        unchanged_count = len(common_classes) - len(modified_classes)
        print(f"\n未变化的类: {unchanged_count} 个")
        
        return {
            'added': added_classes,
            'removed': removed_classes,
            'modified': modified_classes,
            'unchanged': unchanged_count,
        }
    
    def compare_functions(self):
        """对比函数"""
        print("\n" + "=" * 80)
        print("对比函数定义")
        print("=" * 80)
        
        old_func_names = set(self.old_analyzer.functions.keys())
        new_func_names = set(self.new_analyzer.functions.keys())
        
        added_funcs = new_func_names - old_func_names
        removed_funcs = old_func_names - new_func_names
        common_funcs = old_func_names & new_func_names
        
        print(f"\n函数统计:")
        print(f"  旧版本函数数量: {len(old_func_names)}")
        print(f"  新版本函数数量: {len(new_func_names)}")
        print(f"  共同函数数量: {len(common_funcs)}")
        print(f"  新增函数数量: {len(added_funcs)}")
        print(f"  删除函数数量: {len(removed_funcs)}")
        
        if added_funcs:
            print(f"\n新增函数 (前20个):")
            for name in sorted(list(added_funcs))[:20]:
                print(f"  + {name}")
            if len(added_funcs) > 20:
                print(f"  ... 还有 {len(added_funcs) - 20} 个")
        
        if removed_funcs:
            print(f"\n删除函数 (前20个):")
            for name in sorted(list(removed_funcs))[:20]:
                print(f"  - {name}")
            if len(removed_funcs) > 20:
                print(f"  ... 还有 {len(removed_funcs) - 20} 个")
        
        return {
            'added': added_funcs,
            'removed': removed_funcs,
            'common': common_funcs,
        }
    
    def compare_imports(self):
        """对比导入"""
        print("\n" + "=" * 80)
        print("对比导入依赖")
        print("=" * 80)
        
        added_imports = self.new_analyzer.imports - self.old_analyzer.imports
        removed_imports = self.old_analyzer.imports - self.new_analyzer.imports
        common_imports = self.old_analyzer.imports & self.new_analyzer.imports
        
        print(f"\n导入统计:")
        print(f"  旧版本导入数量: {len(self.old_analyzer.imports)}")
        print(f"  新版本导入数量: {len(self.new_analyzer.imports)}")
        print(f"  共同导入数量: {len(common_imports)}")
        print(f"  新增导入数量: {len(added_imports)}")
        print(f"  删除导入数量: {len(removed_imports)}")
        
        if added_imports:
            print(f"\n新增导入 (前20个):")
            for name in sorted(list(added_imports))[:20]:
                print(f"  + {name}")
            if len(added_imports) > 20:
                print(f"  ... 还有 {len(added_imports) - 20} 个")
        
        if removed_imports:
            print(f"\n删除导入 (前20个):")
            for name in sorted(list(removed_imports))[:20]:
                print(f"  - {name}")
            if len(removed_imports) > 20:
                print(f"  ... 还有 {len(removed_imports) - 20} 个")
        
        return {
            'added': added_imports,
            'removed': removed_imports,
            'common': common_imports,
        }
    
    def compare_structure(self):
        """对比文件结构"""
        print("\n" + "=" * 80)
        print("对比文件结构")
        print("=" * 80)
        
        print(f"\n旧版本:")
        print(f"  文件: {self.old_module_path}")
        if self.old_module_path.exists():
            size = self.old_module_path.stat().st_size
            print(f"  大小: {size:,} 字节")
            with open(self.old_module_path, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
            print(f"  行数: {lines:,}")
        
        print(f"\n新版本:")
        print(f"  目录: {self.new_module_path}")
        if self.new_module_path.exists():
            py_files = list(self.new_module_path.rglob("*.py"))
            total_size = sum(f.stat().st_size for f in py_files)
            total_lines = 0
            for f in py_files:
                try:
                    with open(f, 'r', encoding='utf-8') as file:
                        total_lines += len(file.readlines())
                except:
                    pass
            
            print(f"  Python文件数量: {len(py_files)}")
            print(f"  总大小: {total_size:,} 字节")
            print(f"  总行数: {total_lines:,}")
    
    def generate_report(self, output_file: str = "fortran2003_comparison_report.txt"):
        """生成完整的对比报告"""
        print("\n" + "=" * 80)
        print("生成对比报告")
        print("=" * 80)
        
        class_result = self.compare_classes()
        func_result = self.compare_functions()
        import_result = self.compare_imports()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("Fortran2003 模块对比报告\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"旧版本: {self.old_module_path}\n")
            f.write(f"新版本: {self.new_module_path}\n\n")
            
            # 类对比
            f.write("\n" + "=" * 80 + "\n")
            f.write("类对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本类数量: {len(self.old_analyzer.classes)}\n")
            f.write(f"新版本类数量: {len(self.new_analyzer.classes)}\n")
            f.write(f"新增类: {len(class_result['added'])}\n")
            f.write(f"删除类: {len(class_result['removed'])}\n")
            f.write(f"修改类: {len(class_result['modified'])}\n")
            f.write(f"未变化类: {class_result['unchanged']}\n\n")
            
            if class_result['added']:
                f.write("新增类列表:\n")
                for name in sorted(class_result['added']):
                    f.write(f"  + {name}\n")
                f.write("\n")
            
            if class_result['removed']:
                f.write("删除类列表:\n")
                for name in sorted(class_result['removed']):
                    f.write(f"  - {name}\n")
                f.write("\n")
            
            # 函数对比
            f.write("\n" + "=" * 80 + "\n")
            f.write("函数对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本函数数量: {len(self.old_analyzer.functions)}\n")
            f.write(f"新版本函数数量: {len(self.new_analyzer.functions)}\n")
            f.write(f"新增函数: {len(func_result['added'])}\n")
            f.write(f"删除函数: {len(func_result['removed'])}\n\n")
            
            # 导入对比
            f.write("\n" + "=" * 80 + "\n")
            f.write("导入对比结果\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"旧版本导入数量: {len(self.old_analyzer.imports)}\n")
            f.write(f"新版本导入数量: {len(self.new_analyzer.imports)}\n")
            f.write(f"新增导入: {len(import_result['added'])}\n")
            f.write(f"删除导入: {len(import_result['removed'])}\n\n")
        
        print(f"✓ 报告已保存到: {output_file}")
    
    def run_comparison(self):
        """运行完整的对比流程"""
        print("=" * 80)
        print("Fortran2003 模块对比工具")
        print("=" * 80)
        
        # 分析源代码
        self.analyze()
        
        # 对比
        self.compare_structure()
        class_result = self.compare_classes()
        func_result = self.compare_functions()
        import_result = self.compare_imports()
        
        # 生成报告
        self.generate_report()
        
        print("\n" + "=" * 80)
        print("对比完成！")
        print("=" * 80)
        
        return True


def main():
    """主函数"""
    script_dir = Path(__file__).parent
    old_module_path = script_dir / "src" / "fparser" / "two" / "Fortran2003.py.bak"
    new_module_path = script_dir / "src" / "fparser" / "two" / "Fortran2003"
    
    if not old_module_path.exists():
        print(f"错误: 找不到旧版本文件: {old_module_path}")
        return 1
    
    if not new_module_path.exists():
        print(f"错误: 找不到新版本目录: {new_module_path}")
        return 1
    
    # 创建对比器并运行
    comparator = ModuleComparator(old_module_path, new_module_path)
    success = comparator.run_comparison()
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

