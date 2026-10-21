---
source_file: "docker/setup-secrets.sh"
type: "code"
community: "AgentShroud v0.7.0 Enforcement Audit Results"
location: "L430-L496"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AgentShroud_v070_Enforcement_Audit_Results
---

# cmd_extract

## Connections
- [[1Password bootstrap credentials never auto-resolved]] - `implements` [EXTRACTED]
- [[SECRET_DEFS]] - `references` [EXTRACTED]
- [[Static assertions SS1-SS12 on setup-secrets.sh]] - `references` [EXTRACTED]
- [[get_secret]] - `calls` [EXTRACTED]
- [[normalize_secret]] - `calls` [EXTRACTED]
- [[secret_matches_bot_filter]] - `calls` [EXTRACTED]
- [[setup-secrets.sh]] - `defines` [EXTRACTED]
- [[setup-secrets.sh script]] - `calls` [EXTRACTED]
- [[write_secret_file]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AgentShroud_v070_Enforcement_Audit_Results
