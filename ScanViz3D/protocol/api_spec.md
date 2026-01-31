## Function Signatures

### DataLoader
- `__init__(self, db_path)`: 初始化数据加载器，接收数据库文件路径
- `load_point_cloud(self, coordinate_type='average')`: 从数据库加载点云数据，返回numpy数组
  - `coordinate_type`: 坐标类型，可选值：'average', 'max', 'min'

### Visualizer
- `show(self, point_cloud)`: 显示点云数据，接收numpy数组格式的点云数据

### Utils Data Loader
- `generate_sql_query(table_name, columns)`: 生成SQL查询语句，返回字符串
- `parse_binary_data(binary_data)`: 解析二进制数据，返回解析后的数据
- `inspect_data_structure(points)`: 查看数据结构，返回数据结构信息字典
- `print_sample_data(points, sample_size=5)`: 打印样例数据

### Utils Visualizer
- `transform_coordinates(points, translation, rotation)`: 坐标变换，返回变换后的点云数据
- `calculate_color_map(intensity_values)`: 计算颜色映射，返回颜色列表

### Build Tools
- `run_tests()`: 运行测试，返回测试是否通过
- `build_exe()`: 构建可执行文件，返回构建是否成功
- `main()`: 构建工具主函数

### Main Entry
- `main()`: 程序主入口函数