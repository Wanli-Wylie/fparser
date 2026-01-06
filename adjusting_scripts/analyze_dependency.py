import ast
import json
import os
import glob
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Set, Dict, List, Tuple
import multiprocessing

# --- Worker Functions (必须定义在模块顶层以支持序列化) ---

def worker_find_classes(file_path: str) -> Set[str]:
    """
    Worker 1: 解析单个文件，返回其中定义的类名集合。
    """
    local_classes = set()
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    local_classes.add(node.name)
    except Exception as e:
        # 实际生产中建议记录日志，这里简单打印
        print(f"[Parse Error] {os.path.basename(file_path)}: {e}")
    return local_classes

def worker_analyze_deps(args: Tuple[str, Set[str]]) -> Tuple[str, List[str]]:
    """
    Worker 2: 解析单个文件，找出它依赖了哪些已知类。
    args 是一个元组 (file_path, known_classes_set)
    """
    file_path, known_classes = args
    class_deps_map = {} # 当前文件可能包含多个类（虽然你拆分了，但逻辑上兼容）
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
            
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                current_deps = set()
                
                # 遍历该类内部所有节点
                for child in ast.walk(node):
                    if isinstance(child, ast.Name):
                        # 核心判断：是已知类，且不是自己
                        if child.id in known_classes and child.id != class_name:
                            current_deps.add(child.id)
                
                # 我们只返回该文件里这个类的依赖信息
                # 格式化为: "ClassName": ["Dep1", "Dep2"]
                # 这里为了简单，假设一个文件对应一个主类，或者将所有结果平铺返回
                return (class_name, sorted(list(current_deps)))
                
    except Exception:
        pass
    
    return (None, [])

# --- Main Controller ---

def main():
    INPUT_DIR = "./src/fparser/two/Fortran2003/nodes"  # 请修改为你的目录
    OUTPUT_JSON = "class_dependencies.json"
    
    # 根据 CPU 核心数自动决定并行数量
    max_workers = multiprocessing.cpu_count() -8
    print(f"检测到 {max_workers} 个 CPU 核心，开始并行处理...")

    files = glob.glob(os.path.join(INPUT_DIR, "*.py"))
    if not files:
        print("未找到 Python 文件。")
        return

    # --- 第一阶段：并行扫描所有类定义 ---
    print(f"Step 1: 正在扫描 {len(files)} 个文件中的类定义...")
    all_known_classes = set()
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有任务
        futures = [executor.submit(worker_find_classes, f) for f in files]
        
        # 收集结果
        for future in as_completed(futures):
            all_known_classes.update(future.result())
            
    print(f"-> 发现全集: 共 {len(all_known_classes)} 个类。")

    # --- 第二阶段：并行分析依赖 ---
    print(f"Step 2: 正在并行分析 AST 依赖树...")
    full_dependency_map = {}
    
    # 准备参数：每个任务都需要文件路径和全量的类名集合
    # 注意：将 set 传给子进程会有序列化开销，但在 426 个类名这个量级下可以忽略不计
    task_args = [(f, all_known_classes) for f in files]
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker_analyze_deps, arg) for arg in task_args]
        
        for future in as_completed(futures):
            cls_name, deps = future.result()
            if cls_name:
                full_dependency_map[cls_name] = deps

    # --- 输出 ---
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(full_dependency_map, f, indent=4, ensure_ascii=False)

    print(f"完成！已生成 {OUTPUT_JSON}")
    print(f"平均每个类有 {sum(len(d) for d in full_dependency_map.values()) / len(full_dependency_map):.2f} 个依赖。")

if __name__ == "__main__":
    # Windows 下必须在 if __name__ == "__main__": 之下运行多进程
    main()