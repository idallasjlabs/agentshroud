---
type: community
cohesion: 0.12
members: 16
---

# 05 Credential Isolation (redteam)

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[05-credential-isolation]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Constraints_8]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Evidence_5]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Problem_8]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Remediation_6]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Remove secret mounts from agent container and implement transparent credential injection]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Severity_8]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 1 Audit current secret mounts]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 2 Move all secrets to gateway-only Docker Secrets]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 3 Remove credential environment variables from agent container]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 4 Implement transparent credential injection in the gateway]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 5 Route all outbound requests through the gateway egress proxy]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 6 Handle 1Password specifically]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 7 Add credential leak detection to egress filtering]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Step 8 Verify no credentials remain in agent container]] - document - docs/planning/redteam/05-credential-isolation.md
- [[Verification_7]] - document - docs/planning/redteam/05-credential-isolation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/05_Credential_Isolation_redteam
SORT file.name ASC
```
