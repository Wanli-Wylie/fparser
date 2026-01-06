import json
import os
import glob
import ast

def get_class_to_file_map(directory):
    """
    扫描目录下所有文件，建立 {ClassName: FileName} 的映射。
    用于确定 import 语句中的 'from module' 部分。
    """
    mapping = {}
    print("正在建立 [类名 -> 文件名] 映射...")
    
    files = glob.glob(os.path.join(directory, "*.py"))
    for file_path in files:
        # 获取不带后缀的文件名作为 module 名
        # 假设所有文件在同一层级
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        mapping[node.name] = {
                            "path": file_path,
                            "module": module_name
                        }
        except Exception as e:
            print(f"Skipping {file_path}: {e}")
            
    return mapping

def inject_imports(json_file, directory):
    # 1. 读取依赖数据
    with open(json_file, 'r', encoding='utf-8') as f:
        deps_data = json.load(f)

    # 2. 建立映射表
    class_map = get_class_to_file_map(directory)

    # 3. 开始注入
    print("开始批量注入 import...")
    modified_count = 0

    # 我们遍历 JSON，Key是“需要添加import的类”，Value是“它需要的类”
    for target_class, dependencies in deps_data.items():
        if not dependencies:
            continue
            
        if target_class not in class_map:
            print(f"警告: 找不到类 {target_class} 的定义文件，跳过。")
            continue

        target_info = class_map[target_class]
        file_path = target_info["path"]
        
        # 生成 import 语句列表
        import_lines = []
        for dep_class in dependencies:
            if dep_class in class_map:
                source_module = class_map[dep_class]["module"]
                # 避免自引用 (虽然之前的脚本过滤过，但安全起见)
                if source_module != target_info["module"]:
                    line = f"from {source_module} import {dep_class}\n"
                    import_lines.append(line)
            else:
                print(f"警告: 类 {target_class} 依赖 {dep_class}，但找不到 {dep_class} 的文件。")

        if not import_lines:
            continue

        # 去重并排序，保持美观
        import_lines = sorted(list(set(import_lines)))

        # 4. 写入文件
        # 读取原内容 -> 在顶部插入 -> 写回
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.readlines()
            
            # 检查是否已经存在这些 import (避免重复运行脚本导致堆叠)
            # 这是一个简单的字符串检查
            new_content = []
            existing_imports = set(line for line in original_content if line.startswith("from ") or line.startswith("import "))
            
            imports_to_add = []
            for line in import_lines:
                if line not in existing_imports:
                    imports_to_add.append(line)
            
            if not imports_to_add:
                continue

            # 将新的 import 插在最前面
            # 也可以优化逻辑插在 docstring 后面，或者 __future__ 后面，这里简单粗暴插在最前
            new_content = imports_to_add + ["\n"] + original_content
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_content)
                
            modified_count += 1
            
        except Exception as e:
            print(f"写入文件 {file_path} 失败: {e}")

    print(f"\n操作完成！共修改了 {modified_count} 个文件。")

def main():
    # 配置
    JSON_PATH = "class_dependencies.json"
    SPLIT_DIR = "./src/fparser/two/Fortran2003/nodes" # 你的代码目录
    
    if not os.path.exists(SPLIT_DIR):
        print("目录不存在")
        return

    inject_imports(JSON_PATH, SPLIT_DIR)

if __name__ == "__main__":
    main()