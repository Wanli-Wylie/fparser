import json
import networkx as nx
import sys

def check_circular_dependencies(json_file):
    print(f"正在加载依赖关系: {json_file} ...")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建有向图
    G = nx.DiGraph()

    # 构建图：节点是类名，边代表依赖关系 (A -> B 表示 A 依赖 B)
    for class_name, dependencies in data.items():
        G.add_node(class_name)
        for dep in dependencies:
            G.add_edge(class_name, dep)

    print(f"图构建完成: {G.number_of_nodes()} 个节点, {G.number_of_edges()} 条边。")

    # 检测循环
    # simple_cycles 寻找所有的初级回路
    try:
        cycles = list(nx.simple_cycles(G))
    except Exception as e:
        print(f"图分析出错: {e}")
        return

    if not cycles:
        print("\n✅ 完美！未检测到循环依赖。可以直接批量注入 import。")
    else:
        print(f"\n⚠️ 警告！检测到 {len(cycles)} 组循环依赖。")
        print("直接添加 import 可能会导致运行时错误。建议手动检查以下类：\n")
        
        # 按涉及的类数量排序，先看短的循环
        cycles.sort(key=len)
        
        for idx, cycle in enumerate(cycles, 1):
            cycle_str = " -> ".join(cycle) + " -> " + cycle[0]
            print(f"Cycle {idx}: {cycle_str}")

def main():
    JSON_PATH = "class_dependencies.json"  # 上一步生成的json
    check_circular_dependencies(JSON_PATH)

if __name__ == "__main__":
    main()