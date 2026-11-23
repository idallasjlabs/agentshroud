---
type: community
members: 12
---

# Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)

**Members:** 12 nodes

## Members
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py
- [[can_use_tool_from_origin]] - code - gateway/security/tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Owner-elevation-over-unverified-origin_refusal_owner_directive_2026-09-15
SORT file.name ASC
```
