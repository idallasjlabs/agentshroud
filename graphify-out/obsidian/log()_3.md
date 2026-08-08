---
source_file: "docker/scripts/security-scan.sh"
type: "code"
community: "Docker Deploy Scripts"
location: "L18"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Docker_Deploy_Scripts
---

# log()

## Connections
- [[alert_if_critical()]] - `calls` [EXTRACTED]
- [[run_clamav()]] - `calls` [EXTRACTED]
- [[run_oscap()]] - `calls` [EXTRACTED]
- [[run_sbom()]] - `calls` [EXTRACTED]
- [[run_trivy()]] - `calls` [EXTRACTED]
- [[security-scan.sh]] - `defines` [EXTRACTED]
- [[security-scan.sh script]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Docker_Deploy_Scripts