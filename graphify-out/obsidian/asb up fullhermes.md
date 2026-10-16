---
source_file: "scripts/asb"
type: "code"
community: "setup-secrets.sh"
location: "L593-L609"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# asb up [full|hermes]

## Connections
- [[_PROFILE_FLAG]] - `shares_data_with` [EXTRACTED]
- [[_ensure_sandbox_image()]] - `calls` [EXTRACTED]
- [[_hermes_up()]] - `calls` [EXTRACTED]
- [[_prune_docker()]] - `calls` [EXTRACTED]
- [[phase_apply()]] - `references` [EXTRACTED]
- [[phase_baseline()]] - `references` [EXTRACTED]
- [[setup_ephemeral_secrets()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/setup-secretssh
