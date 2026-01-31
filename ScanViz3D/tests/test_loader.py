import pytest
import sqlite3
import os
import numpy as np
from src.data_loader import DataLoader

class TestDataLoader:
    def setup_method(self):
        # 使用现有的数据库文件
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'scan_data.db')
        # 验证数据库文件存在
        assert os.path.exists(self.db_path), f"Database file not found: {self.db_path}"
    
    def test_load_point_cloud_default(self):
        """测试默认加载平均值坐标"""
        loader = DataLoader(self.db_path)
        point_cloud = loader.load_point_cloud()
        assert len(point_cloud) > 0
        assert point_cloud.shape[1] == 3
        assert point_cloud.dtype == np.float64
    
    def test_load_point_cloud_average(self):
        """测试加载平均值坐标"""
        loader = DataLoader(self.db_path)
        point_cloud = loader.load_point_cloud(coordinate_type='average')
        assert len(point_cloud) > 0
        assert point_cloud.shape[1] == 3
    
    def test_load_point_cloud_max(self):
        """测试加载最大值坐标"""
        loader = DataLoader(self.db_path)
        point_cloud = loader.load_point_cloud(coordinate_type='max')
        assert len(point_cloud) > 0
        assert point_cloud.shape[1] == 3
    
    def test_load_point_cloud_min(self):
        """测试加载最小值坐标"""
        loader = DataLoader(self.db_path)
        point_cloud = loader.load_point_cloud(coordinate_type='min')
        assert len(point_cloud) > 0
        assert point_cloud.shape[1] == 3
    
    def test_load_point_cloud_invalid_type(self):
        """测试无效的坐标类型"""
        loader = DataLoader(self.db_path)
        with pytest.raises(ValueError):
            loader.load_point_cloud(coordinate_type='invalid')
    
    def test_load_point_cloud_invalid_db(self):
        """测试无效数据库路径"""
        invalid_db_path = "non_existent.db"
        loader = DataLoader(invalid_db_path)
        with pytest.raises(Exception):
            loader.load_point_cloud()
