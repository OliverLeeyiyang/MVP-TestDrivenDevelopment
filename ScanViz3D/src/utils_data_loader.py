import numpy as np

def generate_sql_query(table_name, columns):
    """
    生成SQL查询语句
    :param table_name: 表名
    :param columns: 列名列表
    :return: SQL查询语句
    """
    columns_str = ", ".join(columns)
    return f"SELECT {columns_str} FROM {table_name}"

def parse_binary_data(binary_data):
    """
    解析二进制数据
    :param binary_data: 二进制数据
    :return: 解析后的数据
    """
    # 这里可以根据实际的二进制数据格式进行解析
    return binary_data

def inspect_data_structure(points):
    """
    查看数据结构
    :param points: 点云数据，格式为numpy数组
    :return: 数据结构信息字典
    """
    if not isinstance(points, np.ndarray):
        raise ValueError("Input must be a numpy array")
    
    structure_info = {
        "shape": points.shape,
        "dtype": str(points.dtype),
        "min": points.min(axis=0).tolist(),
        "max": points.max(axis=0).tolist(),
        "mean": points.mean(axis=0).tolist(),
        "std": points.std(axis=0).tolist()
    }
    
    return structure_info

def print_sample_data(points, sample_size=5):
    """
    打印样例数据
    :param points: 点云数据，格式为numpy数组
    :param sample_size: 样例大小
    """
    if not isinstance(points, np.ndarray):
        raise ValueError("Input must be a numpy array")
    
    print(f"Total points: {len(points)}")
    print(f"Sample size: {min(sample_size, len(points))}")
    print("Sample data:")
    
    # 随机选择样例点
    if len(points) > sample_size:
        indices = np.random.choice(len(points), sample_size, replace=False)
        sample_points = points[indices]
    else:
        sample_points = points
    
    for i, point in enumerate(sample_points):
        print(f"  [{i}]: ({point[0]:.4f}, {point[1]:.4f}, {point[2]:.4f})")
