---
source_file: "docker/setup-secrets.sh"
type: "code"
community: "setup-secrets.sh"
location: "L430-L496"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# cmd_extract

## Connections
- [[1Password bootstrap credentials never auto-resolved]] - `implements` [EXTRACTED]
- [[Prod secrets clobbered by a killed extract]] - `references` [EXTRACTED]
- [[SECRET_DEFS]] - `references` [EXTRACTED]
- [[Static assertions SS1-SS12 on setup-secrets.sh]] - `references` [EXTRACTED]
- [[get_secret]] - `calls` [EXTRACTED]
- [[normalize_secret]] - `calls` [EXTRACTED]
- [[secret_matches_bot_filter]] - `calls` [EXTRACTED]
- [[setup-secrets.sh]] - `defines` [EXTRACTED]
- [[setup-secrets.sh script]] - `calls` [EXTRACTED]
- [[setup_ephemeral_secrets]] - `calls` [EXTRACTED]
- [[write_secret_file]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/setup-secretssh
