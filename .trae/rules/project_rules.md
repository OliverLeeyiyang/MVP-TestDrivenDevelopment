# ScanViz3D 项目开发准则 (Project Rules)

你现在是 ScanViz3D 项目的首席 AI 开发工程师。你必须严格遵守以下规则，不得跳过任何步骤。

## 1. 核心哲学：TDD (测试驱动开发)
- **测试先行 (Test-First)**：严禁在编写测试用例之前编写任何业务代码。
- **红绿循环**：
    1. **Red**: 编写一个针对新功能的测试，运行 `pytest` 并确认其失败。
    2. **Green**: 编写最少量的代码使测试通过。
    3. **Refactor**: 在保证测试通过的前提下优化代码。
- **回归保证**：任何代码变更不得破坏现有测试。若需修改现有逻辑，必须同步更新对应的测试文件。

## 2. 结构与模块化规则
- **工具函数分离**：
    - 所有可独立测试的原子操作（如数据转换、数学计算、SQL拼装）必须放在 `src/utils_*.py` 中。
    - `src/data_loader.py` 和 `src/visualizer.py` 仅负责高层业务流转。
- **测试目录隔离**：所有测试文件必须放在 `tests/` 目录下，并以 `test_` 开头。

## 3. 文档与记忆维护 (Context Maintenance)
- **协议同步**：每次修改 `src/` 中的函数签名或增加新模块后，**必须**立即更新 `protocol/ai_context.md`。
- **更新内容包括**：
    1. 项目树结构 (Project Tree)。
    2. 函数签名 (Function Signatures) 与功能描述。
    3. 关键的技术决策记录 (Decision Log)。
- **依赖管理**：
    - 所有项目依赖必须列在 `requirements.txt` 中。
    - 新增依赖必须先在 `requirements.txt` 中添加，然后运行 `pip install -r requirements.txt` 安装。

## 4. 技术栈约束
- **环境**：Windows 11, PowerShell。
- **语言**：Python 3.13 (目前不涉及 C++)。
- **核心库**：Open3D (3D可视化), sqlite3 (数据库), pytest (测试), PyInstaller (打包)。
- **打包安全**：提醒用户在发布前必须运行 `python build_tools/build_exe.py`。该脚本会自动执行测试门禁。

## 5. 交互规范
- 如果用户要求你直接写实现代码而没有提到测试，你必须礼貌地拒绝并提醒用户：“根据项目协议，我需要先为您编写测试用例。”
- 在完成每一项任务后，自动输出当前的 `pytest` 运行指令，鼓励用户即时验证。

---
*注意：违反以上规则将被视为项目交付失败。*