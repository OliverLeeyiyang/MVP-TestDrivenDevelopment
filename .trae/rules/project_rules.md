# ScanViz3D Rules (TDD & Protocol)

## 1. TDD First
- **Strict TDD**: Write tests BEFORE code. Red -> Green -> Refactor.
- **No Regressions**: Never break existing tests. Update tests if logic changes.
- **Pytest**: Always run `pytest` to verify. Use `tests/test_*.py`.
- Never modify ScanViz3D\data\scan_data.db

## 2. Structure & Demo
- **Utils**: Atomic functions -> `src/utils_*.py`.
- **Logic**: Flow control -> `src/*.py`.
- **Demo Mode**: For exploration, create paired `/demo/X.py` and `/demo/X.md`. The `.md` must record execution output/results.

## 3. Memory & Context
- **Sync Protocol**: Always read `protocol/manifest.md` for incrementally update.
- **Requirements**: Update `requirements.txt` before installing new libs.

## 4. Stack & Env
- Windows 11 (PowerShell), Python 3.13.

## 5. Interaction
- **Refuse**: If asked for code without tests, say: "According to protocol, I must write tests first."
- **Feedback**: End every task with the exact `pytest` command to run.