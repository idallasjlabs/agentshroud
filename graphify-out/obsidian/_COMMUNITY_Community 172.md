---
type: community
cohesion: 0.06
members: 39
---

# Community 172

**Cohesion:** 0.06 - loosely connected
**Members:** 39 nodes

## Members
- [[dot-constructor()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[dot-createConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[AGENTSHROUD_GATEWAY_CONTAINER Override (renamed container breaks CVE scan)]] - rationale - docker/docker-compose.agentshroud-bot.marvin.yml
- [[AgentShroud Daily Check-in (disabled — bot-identity-locked to dev)]] - rationale - docker/config/openclaw/cron/JOBS-REFERENCE.md
- [[AgentShroud Falco Detection Rules]] - document - docker/falco/rules.yaml
- [[Capability Dropping Layer (cap_drop ALL, add back minimum)]] - rationale - docs/archive/SECURITY.md
- [[ConnectProxyAgent]] - code - docker/config/openclaw/setup-https-proxy.js
- [[Docker Hardening Measures (no-new-privileges, cap_drop ALL, non-root)]] - rationale - docs/archive/SECURITY-ANALYSIS.md
- [[Falco Configuration]] - document - docker/falco/falco.yaml
- [[Falco Rule Unexpected Outbound Connection from AgentShroud]] - concept - docker/falco/rules.yaml
- [[Gateway Service_1]] - code - docker/docker-compose.yml
- [[Intrusion Detection & Honeypot Files]] - concept - docs/archive/FUTURE-FEATURES.md
- [[Marvin Dev Overlay (port and subnet offsets from prod)]] - code - docker/docker-compose.agentshroud-bot.marvin.yml
- [[NO_PROXY_HOSTS]] - code - docker/config/openclaw/setup-https-proxy.js
- [[PatchedWebSocket]] - code - docker/config/openclaw/setup-https-proxy.js
- [[Rule Container Shell Spawned]] - code - docker/falco/rules.yaml
- [[Rule Crypto Mining Detection]] - code - docker/falco/rules.yaml
- [[Rule File Access Outside Workspace]] - code - docker/falco/rules.yaml
- [[Rule Privilege Escalation Attempt]] - code - docker/falco/rules.yaml
- [[Rule Secret File Access]] - code - docker/falco/rules.yaml
- [[Rule Unexpected Outbound Connection from AgentShroud]] - code - docker/falco/rules.yaml
- [[Wazuh Agent Service]] - code - docker/docker-compose.yml
- [[bot-access-audit.sh]] - code - docker/scripts/bot-access-audit.sh
- [[bot-access-audit.sh script]] - code - docker/scripts/bot-access-audit.sh
- [[container macro (always-true placeholder inside the gateway)]] - rationale - docker/falco/rules.yaml
- [[gateway-start.sh entrypoint]] - code - docker/scripts/gateway-start.sh
- [[http]] - code - docker/config/openclaw/setup-https-proxy.js
- [[https]] - code - docker/config/openclaw/setup-https-proxy.js
- [[macOS Bridge (localhost-only BlueBubbles webhook relay)]] - concept - docs/archive/SECURITY.md
- [[net]] - code - docker/config/openclaw/setup-https-proxy.js
- [[proxyCreateConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[run_op()]] - code - docker/scripts/bot-access-audit.sh
- [[security-entrypoint.sh boot scan flow]] - code - docker/scripts/security-entrypoint.sh
- [[setup-https-proxy patchWsForProxy()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy proxyCreateConnection()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy shouldBypass()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[setup-https-proxy.js]] - code - docker/config/openclaw/setup-https-proxy.js
- [[shouldBypass()]] - code - docker/config/openclaw/setup-https-proxy.js
- [[tls]] - code - docker/config/openclaw/setup-https-proxy.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_172
SORT file.name ASC
```
