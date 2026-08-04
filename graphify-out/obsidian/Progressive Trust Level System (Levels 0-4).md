---
source_file: "docs/architecture/adr/ADR-008-progressive-trust-levels.md"
type: "concept"
community: "Module Group 261"
location: "line 12"
tags:
  - graphify/concept
  - graphify/INFERRED
  - community/Module_Group_261
---

# Progressive Trust Level System (Levels 0-4)

## Connections
- [[7-Layer Security Pipeline (76 modules L1 Core, L2 Middleware, L3 Output, L4 Tool, L5 Network, L6 File, L7 Infra)]] - `implements` [INFERRED]
- [[ADR-008 Progressive Trust Levels for Agents]] - `defines` [EXTRACTED]
- [[Trust Boundary Diagram (Zone 0 Owner, Zone 1 Gateway, Zone 2 Bot, Zone 3 External Services, Zone 4 SSH-gated nodes)]] - `visualizes` [INFERRED]
- [[Trust Promotion Rules (L0→L1 immediate; L1→L2 100 actions, 0 violations, 7 days; L2→L3 1000 actions, 5% violations; L3→L4 manual only)]] - `implements` [INFERRED]
- [[agentshroud.yaml Main Configuration Schema (gateway, security, audit, approval, rate_limiting, proxy, monitoring)]] - `configures` [INFERRED]

#graphify/concept #graphify/INFERRED #community/Module_Group_261
