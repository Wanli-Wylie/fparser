import os
import glob

def remove_leading_emptylines(directory):
    print(f"正在处理目录: {directory} ...")
    
    # 获取目录下所有 py 文件
    files = glob.glob(os.path.join(directory, "*.py"))
    
    modified_count = 0
    
    for file_path in files:
        try:
            # 1. 读取文件
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            if not lines:
                continue

            # 2. 找到第一个非空行的索引
            first_content_index = 0
            has_content = False
            
            for i, line in enumerate(lines):
                # strip() 去除首尾空白字符，如果为空说明这一行全是空白
                if line.strip(): 
                    first_content_index = i
                    has_content = True
                    break
            
            # 特殊情况：如果整个文件全是空行，清空文件
            if not has_content:
                if len(lines) > 0: # 只有当原文件不是真“空”时才操作
                    print(f"[清空] {os.path.basename(file_path)} (全是空行)")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("")
                    modified_count += 1
                continue

            # 3. 如果开头没有空行，直接跳过
            if first_content_index == 0:
                continue

            # 4. 写入新内容 (从第一个有内容的行开始)
            print(f"[修改] {os.path.basename(file_path)} (移除了 {first_content_index} 行)")
            new_content = lines[first_content_index:]
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(new_content)
                
            modified_count += 1

        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")

    print(f"\n完成！共清理了 {modified_count} 个文件。")

if __name__ == "__main__":
    # --- 配置 ---
    TARGET_DIR = "./src/fparser/two/Fortran2003/nodes" # 你的代码目录
    # -----------
    
    if os.path.exists(TARGET_DIR):
        remove_leading_emptylines(TARGET_DIR)
    else:
        print(f"错误: 目录 {TARGET_DIR} 不存在。")