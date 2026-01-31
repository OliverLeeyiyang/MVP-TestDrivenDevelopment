# AI Context & Memory Bank

## 1. Project Overview & Rules
- **Project**: ScanViz3D
- **Goal**: Visualize .db scan data using Open3D.
- **Rule 1 (TDD)**: Test BEFORE Code. No method implementation without a test case.
- **Rule 2 (Regression)**: Never break existing tests.
- **Rule 3 (File Structure)**: 
  - `ScanViz3D/src/utils_*.py` for pure helper functions (easy to test).
  - `ScanViz3D/src/` for main logic classes.

## 2. Project Tree (Updated Manually by AI)
AI should update this section when structure changes：
```text
MVP-TestDrivenDevelopment/
└── ScanViz3D/
    ├── .gitignore              # [配置] 忽略 venv, dist, build, __pycache__ 等
    ├── requirements.txt        # [依赖] open3d, pytest, pyinstaller 等
    ├── main.py                 # [入口] 程序启动入口
    │
    ├── build_tools/            # [构建] 专门存放打包相关的脚本
    │   └── build_exe.py        # [脚本] 自动化打包脚本 (先测试 -> 后打包)
    │
    ├── data/                   # [资源] 存放测试用的 .db 扇扫数据
    │   └── sample_scan.db
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
└──  README.md               # [文档] 项目说明 & AI 协议
```

## 3. API Signature Registry (AI Updates This)
*Record public methods here to avoid hallucination.*

### `src/utils_data_loader.py`
- `parse_blob_to_points(blob_data: bytes) -> list[tuple]`
  - *Status*: Pending
  - *Desc*: Converts binary blob from SQLite to list of (x,y,z).

### `src/data_loader.py`
- `class ScanReader`
  - `__init__(db_path: str)`
  - `get_scan_data(scan_id: int) -> RunResult`

## 4. Decision Log (Why did we do this?)
- [202X-XX-XX]: Decided to split `utils` files to isolate logic for easier unit testing.
- [202X-XX-XX]: Using `build_tools/build_exe.py` to enforce tests before building.