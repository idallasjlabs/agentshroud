---
type: community
cohesion: 0.13
members: 15
---

# 04 Separation Of Privilege (redteam)

**Cohesion:** 0.13 - loosely connected
**Members:** 15 nodes

## Members
- [[04-separation-of-privilege]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Constraints_7]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Evidence_4]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Make gateway source code, config, and security policies read-only to the agent]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Problem_7]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Remediation_5]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Root Cause_6]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Severity_7]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 1 Mount gateway source as read-only Docker volumes]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 2 Add AgentShroud paths to File IO Sandboxing deny list]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 3 Block SSH commands targeting the gateway host]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 4 Make SOUL.md and system prompts immutable]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 5 Add integrity checking for security-critical files]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Step 6 Enforce read-only at the Docker layer]] - document - docs/planning/redteam/04-separation-of-privilege.md
- [[Verification_6]] - document - docs/planning/redteam/04-separation-of-privilege.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/04_Separation_Of_Privilege_redteam
SORT file.name ASC
```
