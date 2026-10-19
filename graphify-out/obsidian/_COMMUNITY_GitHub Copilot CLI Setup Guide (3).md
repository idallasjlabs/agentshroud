---
type: community
members: 6
---

# GitHub Copilot CLI Setup Guide (3)

**Members:** 6 nodes

## Members
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GitHub_Copilot_CLI_Setup_Guide_3
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - degree 6, connects to 1 community
