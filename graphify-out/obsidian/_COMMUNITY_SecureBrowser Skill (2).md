---
type: community
members: 18
---

# SecureBrowser Skill (2)

**Members:** 18 nodes

## Members
- [[Conduit root-relative ws-ticket fetch - bare 404]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Dev Hermes polling prod's Telegram bot]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Funnel hermes via gateway (Hermes isolation boundary)]] - rationale - scripts/tailscale-serve.sh
- [[Funnel root path  - gateway hermes-dashboard]] - rationale - scripts/tailscale-serve.sh
- [[Hermes egress approval cards posted to OpenClaw bot (_token_for fallback)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes pinned 0.21.5 silent Sunday no-op]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Incident ConduitHermes instability 2026-10-16]] - document - INCIDENT_2026-10-16_conduit-outage.md
- [[Nemotron + Qwen-only no_think suffix root cause]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Prod Colima VM outbound traffic loss (0245Z root cause)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Prod Colima sizing is 8 CPU  12 GiB (610 withdrawn)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Temporary Funnel stopgap for ESP32 voice terminal]] - rationale - scripts/tailscale-serve.sh
- [[cmd_persist]] - code - scripts/tailscale-serve.sh
- [[cmd_start]] - code - scripts/tailscale-serve.sh
- [[cmd_status]] - code - scripts/tailscale-serve.sh
- [[cmd_stop]] - code - scripts/tailscale-serve.sh
- [[lazydocker socket leak]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[tailscale-serve.sh]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh script]] - code - scripts/tailscale-serve.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecureBrowser_Skill_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)]]

## Top bridge nodes
- [[cmd_start]] - degree 9, connects to 2 communities
- [[Incident ConduitHermes instability 2026-10-16]] - degree 10, connects to 1 community
- [[tailscale-serve.sh]] - degree 6, connects to 1 community
- [[Nemotron + Qwen-only no_think suffix root cause]] - degree 2, connects to 1 community
