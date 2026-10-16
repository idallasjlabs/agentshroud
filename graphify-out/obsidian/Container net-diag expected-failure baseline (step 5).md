---
source_file: "docker/scripts/colima-health-check.sh"
type: "rationale"
community: "AgentTarget"
location: "docker/scripts/colima-health-check.sh:470"
tags:
  - graphify/rationale
  - graphify/INFERRED
  - community/AgentTarget
---

# Container net-diag expected-failure baseline (step 5)

## Connections
- [[check()_4]] - `references` [EXTRACTED]
- [[openclaw service (dev override)]] - `shares_data_with` [INFERRED]
- [[sunday-upgrade-apply.sh no-op gate fixes (CLAUDE.md 0.0)]] - `semantically_similar_to` [INFERRED]

#graphify/rationale #graphify/INFERRED #community/AgentTarget
