---
type: community
cohesion: 0.14
members: 14
---

# TestNewPatternsV080

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[ARM64 Seccomp Profile Requirement]] - rationale - docs/operations/raspberry-pi.md
- [[Colima Troubleshooting Procedures]] - concept - docs/runbooks/RUNBOOK.md
- [[Configuration Reference]] - document - docs/setup/setup-guide.md
- [[Example Configurations_1]] - document - docs/setup/setup-guide.md
- [[Glibc TLS Block Allocation Fix (Container Rebuild)]] - rationale - docs/runbooks/RUNBOOK.md
- [[Glibc TLS Incompatibility (Trillian)]] - rationale - docs/project/TELEGRAM_ISSUES.md
- [[Multi-Host Infrastructure (MarvinTrillianPi)]] - concept - docs/runbooks/RUNBOOK.md
- [[RUNBOOK_1]] - document - docs/runbooks/RUNBOOK.md
- [[Seccomp Profile Conflict (x86_64)]] - rationale - docs/project/TELEGRAM_ISSUES.md
- [[Secrets Setup Script (dockersecretssetup-secrets.sh)]] - concept - docs/operations/raspberry-pi.md
- [[agentshroud.yaml Configuration File]] - concept - docs/operations/raspberry-pi.md
- [[egress-config.yml - Egress Filtering]] - document - docs/setup/setup-guide.md
- [[mcp-config.yml - MCP Server Registry]] - document - docs/setup/setup-guide.md
- [[raspberry-pi]] - document - docs/operations/raspberry-pi.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestNewPatternsV080
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Implement gateway-level outbound information filtering module]]
- 2 edges to [[_COMMUNITY_TELEGRAM_ISSUES]]
- 1 edge to [[_COMMUNITY_graphify reference extra exports and benchmark (3)]]
- 1 edge to [[_COMMUNITY_LOW — Informational]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY__sync]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_canary.py]]
- 1 edge to [[_COMMUNITY_test_llm_proxy_thinking_suppression.py]]

## Top bridge nodes
- [[raspberry-pi]] - degree 8, connects to 4 communities
- [[RUNBOOK_1]] - degree 7, connects to 4 communities
- [[Configuration Reference]] - degree 5, connects to 1 community
- [[Glibc TLS Incompatibility (Trillian)]] - degree 2, connects to 1 community
- [[Seccomp Profile Conflict (x86_64)]] - degree 2, connects to 1 community
