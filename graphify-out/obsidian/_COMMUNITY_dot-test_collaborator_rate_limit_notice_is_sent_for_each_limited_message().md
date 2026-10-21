---
type: community
members: 9
---

# .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()

**Members:** 9 nodes

## Members
- [[1Password (trusted for secrets, gateway-only access)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[AgentShroud Bot (no direct credentialinternet access)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[AgentShroud Gateway (holds 1Password service account)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Isaiah Jefferson (full control)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 0 — Owner (Highest Trust)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 1 — Gateway (Trusted Enforcer)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 2 — Bot (Supervised Agent)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 3 — External Services (Conditional)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg
- [[Trust Zone 4 — Infrastructure Nodes (SSH-gated)]] - concept - docs/diagrams/images/diagram-11-trust-boundary.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
SORT file.name ASC
```
