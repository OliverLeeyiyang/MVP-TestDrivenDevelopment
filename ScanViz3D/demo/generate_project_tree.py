import os
import sys

def generate_project_tree(root_dir, max_depth=5, current_depth=0):
    """
    生成项目目录树结构
    :param root_dir: 根目录路径
    :param max_depth: 最大遍历深度
    :param current_depth: 当前深度
    :return: 项目树结构字符串
    """
    if current_depth >= max_depth:
        return ""
    
    tree_str = ""
    indent = "    " * current_depth
    
    # 获取目录内容并排序
    try:
        items = sorted(os.listdir(root_dir))
    except PermissionError:
        return f"{indent}[Permission Denied]\n"
    
    for i, item in enumerate(items):
        item_path = os.path.join(root_dir, item)
        is_last = i == len(items) - 1
        
        # 跳过忽略的目录和文件
        if item in ['.git', 'venv', 'dist', 'build', '__pycache__', '.pytest_cache']:
            continue
        if item.endswith('.pyc'):
            continue
        
        # 添加当前项到树中
        if is_last:
            tree_str += f"{indent}└── {item}\n"
        else:
            tree_str += f"{indent}├── {item}\n"
        
        # 如果是目录，递归遍历
        if os.path.isdir(item_path):
            tree_str += generate_project_tree(item_path, max_depth, current_depth + 1)
    
    return tree_str

def main():
    """
    主函数
    """
    # 获取项目根目录
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    print(f"=== ScanViz3D 项目树结构 ===")
    print(f"根目录: {project_root}")
    print("=" * 60)
    
    # 生成项目树
    tree_structure = generate_project_tree(project_root)
    print(tree_structure)
    
    # 将结果保存到文件
    output_file = os.path.join(os.path.dirname(__file__), 'project_tree.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# ScanViz3D 项目树结构\n\n")
        f.write(f"根目录: {project_root}\n\n")
        f.write(tree_structure)
    
    print(f"\n=== 结果保存 ===")
    print(f"项目树结构已保存到: {output_file}")

if __name__ == "__main__":
    main()
