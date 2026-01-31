import pytest
import numpy as np
from src.utils_data_loader import generate_sql_query, parse_binary_data, inspect_data_structure, print_sample_data

class TestUtilsDataLoader:
    def test_generate_sql_query(self):
        """测试生成SQL查询语句"""
        table_name = "scan_data"
        columns = ["x", "y", "z"]
        expected_query = "SELECT x, y, z FROM scan_data"
        assert generate_sql_query(table_name, columns) == expected_query
    
    def test_generate_sql_query_single_column(self):
        """测试生成单列SQL查询语句"""
        table_name = "scan_data"
        columns = ["x"]
        expected_query = "SELECT x FROM scan_data"
        assert generate_sql_query(table_name, columns) == expected_query
    
    def test_parse_binary_data(self):
        """测试解析二进制数据"""
        test_data = b"test binary data"
        result = parse_binary_data(test_data)
        assert result == test_data
    
    def test_inspect_data_structure(self):
        """测试查看数据结构"""
        test_points = np.array([[0.0, 0.0, 0.0],
                               [1.0, 1.0, 1.0],
                               [2.0, 2.0, 2.0]])
        structure_info = inspect_data_structure(test_points)
        assert "shape" in structure_info
        assert "dtype" in structure_info
        assert "min" in structure_info
        assert "max" in structure_info
    
    def test_print_sample_data(self):
        """测试打印样例数据"""
        test_points = np.array([[0.0, 0.0, 0.0],
                               [1.0, 1.0, 1.0],
                               [2.0, 2.0, 2.0]])
        # 这里只测试函数是否能正常执行，不测试打印输出
        try:
            print_sample_data(test_points, sample_size=2)
            assert True
        except Exception as e:
            pytest.fail(f"print_sample_data() raised Exception: {e}")
