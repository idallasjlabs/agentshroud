---
source_file: "docs/planning/redteam/05-credential-isolation.md"
type: "document"
community: "Community 580"
location: "L19"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Community_580
---

# Remediation

## Connections
- [[Remove secret mounts from agent container and implement transparent credential injection]] - `contains` [EXTRACTED]
- [[Step 1 Audit current secret mounts]] - `contains` [EXTRACTED]
- [[Step 2 Move all secrets to gateway-only Docker Secrets]] - `contains` [EXTRACTED]
- [[Step 3 Remove credential environment variables from agent container]] - `contains` [EXTRACTED]
- [[Step 4 Implement transparent credential injection in the gateway]] - `contains` [EXTRACTED]
- [[Step 5 Route all outbound requests through the gateway egress proxy]] - `contains` [EXTRACTED]
- [[Step 6 Handle 1Password specifically]] - `contains` [EXTRACTED]
- [[Step 7 Add credential leak detection to egress filtering]] - `contains` [EXTRACTED]
- [[Step 8 Verify no credentials remain in agent container]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Community_580