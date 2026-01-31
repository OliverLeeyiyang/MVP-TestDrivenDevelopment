# Protocol Manifest
- **project_map.md**: Current directory structure. Update on file creation/deletion. Always call `ScanViz3D\demo\generate_project_tree.py` to fetch the current directory structure and use the generated `ScanViz3D\demo\project_tree.txt` as the current project map. Always add updation time at the top of the file.
- **api_spec.md**: Public methods and logic flow. Update when changing code signatures.
- **decision_log.md**: Persistent log of WHY decisions were made. **APPEND ONLY.**
- **other_info.md**: Other information about the project(like database structure).

**Strict Rule**: Never overwrite the entire `decision_log.md`. Only append new entries at the top.