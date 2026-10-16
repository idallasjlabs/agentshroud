---
source_file: "scripts/asb"
type: "code"
community: "setup-secrets.sh"
location: "L637-L666"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# asb clean-rebuild [full|hermes]

## Connections
- [[Compose profile gating (voicehermesfull)]] - `rationale_for` [EXTRACTED]
- [[PROJECT (compose project name)]] - `shares_data_with` [EXTRACTED]
- [[S16 asb rebuildclean-rebuild build with $_PROFILE_FLAG]] - `references` [EXTRACTED]
- [[_PROFILE_FLAG]] - `shares_data_with` [EXTRACTED]
- [[_ensure_sandbox_image()]] - `calls` [EXTRACTED]
- [[_hermes_down()]] - `calls` [EXTRACTED]
- [[_hermes_up()]] - `calls` [EXTRACTED]
- [[_prune_docker()]] - `calls` [EXTRACTED]
- [[_reset_device_store()]] - `calls` [EXTRACTED]
- [[setup_ephemeral_secrets()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/setup-secretssh
