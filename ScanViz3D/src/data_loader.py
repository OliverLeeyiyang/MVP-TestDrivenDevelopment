import sqlite3
import numpy as np

class DataLoader:
    def __init__(self, db_path):
        """
        初始化数据加载器
        :param db_path: 数据库文件路径
        """
        self.db_path = db_path
    
    def load_point_cloud(self, coordinate_type='average'):
        """
        从数据库加载点云数据
        :param coordinate_type: 坐标类型，可选值：'average', 'max', 'min'
        :return: 点云数据，格式为numpy数组
        """
        # 先验证坐标类型，直接抛出ValueError
        if coordinate_type not in ['average', 'max', 'min']:
            raise ValueError("Invalid coordinate_type. Must be 'average', 'max', or 'min'")
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 根据坐标类型选择对应的列
            if coordinate_type == 'average':
                columns = 'ave_point_x, ave_point_y, ave_point_z'
            elif coordinate_type == 'max':
                columns = 'max_point_x, max_point_y, max_point_z'
            elif coordinate_type == 'min':
                columns = 'min_point_x, min_point_y, min_point_z'
            
            # 使用现有的fan_sweep_data表
            query = f"SELECT {columns} FROM fan_sweep_data"
            cursor.execute(query)
            points = cursor.fetchall()
            
            conn.close()
            
            if not points:
                return np.array([])
            
            return np.array(points, dtype=np.float64)
            
        except Exception as e:
            raise Exception(f"Failed to load point cloud: {e}")
