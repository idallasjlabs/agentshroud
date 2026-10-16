---
source_file: "scripts/asb"
type: "rationale"
community: "setup-secrets.sh"
location: "L625-L630"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# Compose profile gating (voice/hermes/full)

## Connections
- [[COMPOSE_CMD]] - `rationale_for` [EXTRACTED]
- [[_PROFILE_FLAG]] - `rationale_for` [EXTRACTED]
- [[asb clean-rebuild fullhermes]] - `rationale_for` [EXTRACTED]
- [[asb rebuild fullhermes]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/setup-secretssh
