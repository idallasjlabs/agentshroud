---
type: community
cohesion: 0.07
members: 39
---

# test_collaborator_tracker.py (4)

**Cohesion:** 0.07 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-constructor()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[dot-createConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[120s freshclam timeout rationale (bounded failure over outage)]] - rationale - docker/scripts/security-entrypoint.sh
- [[AgentShroud Falco Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[ConnectProxyAgent]] - code - docker/config/openclaw/setup-https-proxy.js
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection]] - concept - docker/falco/rules.yaml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[NO_PROXY_HOSTS]] - code - docker/config/openclaw/setup-https-proxy.js
- [[PatchedWebSocket]] - code - docker/config/openclaw/setup-https-proxy.js
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[alert_critical()]] - code - docker/scripts/security-entrypoint.sh
- [[bot-access-audit.sh]] - code - docker/scripts/bot-access-audit.sh
- [[bot-access-audit.sh script]] - code - docker/scripts/bot-access-audit.sh
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[gateway-start.sh]] - code - docker/scripts/gateway-start.sh
- [[gateway-start.sh script]] - code - docker/scripts/gateway-start.sh
- [[http]] - code - docker/config/openclaw/setup-https-proxy.js
- [[https]] - code - docker/config/openclaw/setup-https-proxy.js
- [[log()_5]] - code - docker/scripts/security-entrypoint.sh
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md
- [[net]] - code - docker/config/openclaw/setup-https-proxy.js
- [[proxyCreateConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[run_op()]] - code - docker/scripts/bot-access-audit.sh
- [[security-entrypoint.sh]] - code - docker/scripts/security-entrypoint.sh
- [[security-entrypoint.sh script]] - code - docker/scripts/security-entrypoint.sh
- [[setup-https-proxy patchWsForProxy()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy proxyCreateConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy shouldBypass()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy.js]] - code - docker/config/openclaw/setup-https-proxy.js
- [[shouldBypass()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[tls]] - code - docker/config/openclaw/setup-https-proxy.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_trackerpy_4
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)]]
- 1 edge to [[_COMMUNITY_run-standalone.sh]]

## Top bridge nodes
- [[container macro (always-true placeholder inside the gateway)]] - degree 7, connects to 1 community
- [[Rule Container Shell Spawned]] - degree 4, connects to 1 community
- [[gateway-start.sh]] - degree 3, connects to 1 community
