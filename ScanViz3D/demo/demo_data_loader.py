import os
import sys

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_loader import DataLoader
from src.utils_data_loader import inspect_data_structure, print_sample_data

# 使用现有的数据库文件
db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'scan_data.db')

print(f"=== 数据加载演示 ===")
print(f"使用数据库: {db_path}")
print("=" * 80)

try:
    # 加载数据
    loader = DataLoader(db_path)
    
    # 测试不同类型的坐标数据加载
    coordinate_types = ['average', 'max', 'min']
    
    for coord_type in coordinate_types:
        print(f"\n=== 加载 {coord_type} 坐标 ===")
        point_cloud = loader.load_point_cloud(coordinate_type=coord_type)
        
        print(f"数据加载成功！")
        print(f"点云数据形状: {point_cloud.shape}")
        print(f"数据点数量: {point_cloud.shape[0]}")
        
        # 查看数据结构
        print("\n=== 数据结构查看 ===")
        structure = inspect_data_structure(point_cloud)
        print(f"形状: {structure['shape']}")
        print(f"数据类型: {structure['dtype']}")
        print(f"最小值: {structure['min']}")
        print(f"最大值: {structure['max']}")
        print(f"均值: {structure['mean']}")
        print(f"标准差: {structure['std']}")
        
        # 打印样例数据
        print("\n=== 样例数据打印 ===")
        print_sample_data(point_cloud, sample_size=5)
        print("-" * 80)
        
finally:
    print("\n演示完成！")
