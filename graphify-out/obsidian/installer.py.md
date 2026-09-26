---
source_file: "gateway/web/installer.py"
type: "code"
community: "get_trivy_summary()"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/get_trivy_summary
---

# installer.py

## Connections
- [[InstallConfig]] - `contains` [EXTRACTED]
- [[PrerequisiteCheck]] - `contains` [EXTRACTED]
- [[api.py]] - `references` [EXTRACTED]
- [[check_prerequisites()]] - `contains` [EXTRACTED]
- [[detect_runtime()]] - `imports` [EXTRACTED]
- [[get_runtimes()]] - `contains` [EXTRACTED]
- [[get_security_comparison()]] - `imports` [EXTRACTED]
- [[installer_page()]] - `contains` [EXTRACTED]
- [[security.py]] - `imports_from` [EXTRACTED]
- [[start_install()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/get_trivy_summary