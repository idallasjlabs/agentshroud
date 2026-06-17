---
type: community
cohesion: 0.06
members: 40
---

# Module Group 112

**Cohesion:** 0.06 - loosely connected
**Members:** 40 nodes

## Members
- [[1Password Cloud]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[1Password — Trusted for secrets, Gateway-only access]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[AgentShroud Bot — No direct credential access, all via op-proxy, HTTP CONNECT proxy, MCP Inspector]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Allowlisted Domains (api.openai.com, api.anthropic.com, api.telegram.org, oauth2.googleapis.com, www.googleapis.com, github.com, githubusercontent.com, imap.mail.me.com, smtp.mail.me.com)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Anthropic API — Trusted for inference, Allowlisted domain]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Blocked (403 Forbidden) — All other domains, All RFC1918 addresses (10.x, 172.16.x, 192.168.x)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Blocked  Untrusted Zone]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Bot Container (no service account)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Bot Environment (secrets as env vars, never written to disk)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Bot Makes Outbound Request (any HTTPS connection)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Connection Logged (timestamp, target domain, allowedblocked, connection count)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Diagram 11 Trust Boundary (PNG)]] - image - docs/diagrams/images/diagram-11-trust-boundary.png
- [[Diagram 11 Trust Boundary (SVG)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Diagram 12 Credential Flow (PNG)]] - image - docs/diagrams/images/diagram-12-credential-flow.png
- [[Diagram 12 Credential Flow (SVG)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Diagram 13 Network Security Egress (PNG)]] - image - docs/diagrams/images/diagram-13-network-security-egress.png
- [[Diagram 13 Network Security Egress (SVG)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Direct Connection (would bypass all controls) — NOT CONFIGURED]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Domain Allowlisted (agentshroud.yaml proxy.allowed_domains)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Exported Secrets (ANTHROPIC_OAUTH_TOKEN, BRAVE_API_KEY, ICLOUD_APP_PASSWORD, ICLOUD_USERNAME, ICLOUD_EMAIL)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Gateway Container (has service account)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[GitHub — Trusted for code ops, Allowlisted domain]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[HTTP CONNECT Tunnel — request to gateway8181]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[HTTP_PROXY set (httpgateway8181)]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[OP_SERVICE_ACCOUNT_TOKEN (loaded from Docker secret runsecrets1password_service_account)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[OpenAI API — Trusted for inference, Allowlisted domain]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[POST credentialsop-proxy (credential proxy endpoint)]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[TCP Tunnel Established — Gateway Relays Traffic]] - image - docs/diagrams/images/diagram-13-network-security-egress.svg
- [[Telegram API — Trusted for messaging, Allowlisted domain]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 0 — Owner (Highest Trust)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 1 — Gateway (Trusted Enforcer)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 2 — Bot (Supervised Agent)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 3 — External Services (Conditional)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 4 — Infrastructure Nodes (SSH-gated)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Unlisted Domains Blocked by default-deny HTTP CONNECT proxy]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Validates GATEWAY_AUTH_TOKEN, checks allowed_op_paths pattern]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[marvin SSH Host (approved)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[op_proxy_read_with_retry() — Cascading retries 5s,10s,15s,30s,60s]] - image - docs/diagrams/images/diagram-12-credential-flow.svg
- [[raspberrypi SSH Host (approved, agentshroud-bot user, id_ed25519)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[trillian SSH Host (approved)]] - image - docs/diagrams/images/diagram-11-trust-boundary.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_112
SORT file.name ASC
```
