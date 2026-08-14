---
type: community
members: 6
---

# .github/workflows

**Members:** 6 nodes

## Members
- [[CI Workflow]] - code - .github/workflows/ci.yml
- [[Dependabot Configuration]] - code - .github/dependabot.yml
- [[Leak Gate Scoped to ubuntu+3.11]] - rationale - .github/workflows/ci.yml
- [[Presidio-Anonymizer 2.2.364 Version Pin-Out]] - rationale - .github/dependabot.yml
- [[cryptography=50.0.0 Security Floor]] - rationale - gateway/requirements.txt
- [[gatewayrequirements.txt Dependency File]] - code - gateway/requirements.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/github/workflows
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_AGENTS]]

## Top bridge nodes
- [[gatewayrequirements.txt Dependency File]] - degree 4, connects to 1 community