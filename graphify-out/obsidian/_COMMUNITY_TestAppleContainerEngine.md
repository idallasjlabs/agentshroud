---
type: community
cohesion: 0.29
members: 8
---

# TestAppleContainerEngine

**Cohesion:** 0.29 - loosely connected
**Members:** 8 nodes

## Members
- [[ADR-008 Progressive Trust Level System]] - concept - docs/architecture/adr/ADR-008-progressive-trust-levels.md
- [[Approval DB (SQLiteaiosqlite)]] - image - docs/diagrams/images/diagram-02-c4-container.svg
- [[ApprovalRequest (data entity)]] - concept - docs/data/data-dictionary.md
- [[RateLimitBucket (data entity)]] - concept - docs/data/data-dictionary.md
- [[TrustLevel (data entity)]] - concept - docs/data/data-dictionary.md
- [[agent_trust SQLite table]] - code - docs/data/schema-documentation.md
- [[agentshroud.yaml (main config schema)]] - code - docs/data/schema-documentation.md
- [[approval_requests SQLite table]] - code - docs/data/schema-documentation.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAppleContainerEngine
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_test_cron_jobs_prompts.py]]

## Top bridge nodes
- [[ADR-008 Progressive Trust Level System]] - degree 3, connects to 1 community
- [[Approval DB (SQLiteaiosqlite)]] - degree 2, connects to 1 community