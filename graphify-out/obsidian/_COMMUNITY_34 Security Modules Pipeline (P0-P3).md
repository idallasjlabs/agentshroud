---
type: community
cohesion: 0.22
members: 10
---

# 34 Security Modules Pipeline (P0-P3)

**Cohesion:** 0.22 - loosely connected
**Members:** 10 nodes

## Members
- [[Approval Request Workflow (user-facing)]] - concept - docs/user-guide.md
- [[Command Injection Threat — regex + no-shell exec mitigation]] - rationale - docs/ssh-security-review.md
- [[Host SpoofingMITM Threat — TOFU model residual risk]] - rationale - docs/ssh-security-review.md
- [[Open Findings (C3-C5, H4-H7, M1-M5)]] - concept - docs/claude-security-audit-prompt.md
- [[Option 1 Direct SSH (current approach)]] - concept - docs/architecture/DISTRIBUTED_OPENCLAW_NODE_ARCHITECTURE.md
- [[Production Deployment Recommendations]] - concept - docs/ssh-security-review.md
- [[SSH AllowDeny List Evaluation Order]] - concept - docs/ssh-configuration.md
- [[SSH Auto-Approve Commands]] - concept - docs/ssh-configuration.md
- [[SSH Proxy Config Schema (agentshroud.yaml ssh section)]] - concept - docs/ssh-configuration.md
- [[SSH Proxy Threat Model (6 threats)]] - concept - docs/ssh-security-review.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/34_Security_Modules_Pipeline_P0-P3
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Slack Channel Setup]]

## Top bridge nodes
- [[Open Findings (C3-C5, H4-H7, M1-M5)]] - degree 2, connects to 1 community
