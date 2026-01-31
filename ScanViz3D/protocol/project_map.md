# Project Map
Last Updated: 2026-01-31 14:06:00

```text
MVP-TestDrivenDevelopment/
├── ScanViz3D/
    ├── .gitignore              # [配置] 忽略 venv, dist, build, __pycache__ 等
    ├── requirements.txt        # [依赖] open3d, pytest, pyinstaller 等
    ├── main.py                 # [入口] 程序启动入口
    │
    ├── build_tools/            # [构建] 专门存放打包相关的脚本
    │   └── build_exe.py        # [脚本] 自动化打包脚本 (先测试 -> 后打包)
    │
    ├── data/                   # [资源] 存放测试用的 .db 扇扫数据
    │   └── scan_data.db
    │
    ├── protocol/               # [协议] AI 协作的核心约束
    │   └── ai_context.md       # [核心] AI 维护的项目记忆 (项目树、API签名、决策记录)
    │
    ├── src/                    # [源码] 业务逻辑
    │   ├── __init__.py
    │   ├── data_loader.py      # 业务层：数据库读取主逻辑
    │   ├── visualizer.py       # 业务层：可视化主逻辑
    │   ├── utils_data_loader.py # 工具层：纯函数，如 SQL 语句生成、二进制解析
    │   └── utils_visualizer.py  # 工具层：纯函数，如 坐标转换、颜色映射计算
    │
    └── tests/                  # [测试] TDD 核心区
        ├── __init__.py
        ├── test_loader.py      # 针对 data_loader 的测试
        ├── test_visualizer.py  # 针对 visualizer 的测试
        ├── test_utils_data.py  # [新增] 针对 utils_data_loader 的细粒度测试
        └── test_utils_viz.py   # [新增] 针对 utils_visualizer 的细粒度测试
    └── demo/                   # [演示] 存放演示脚本和结果
        ├── demo_data_loader.py # 数据加载演示脚本
        └── demo_data_loader.md # 演示结果记录
└─── README.md               # [文档] 项目说明 & AI 协议
```