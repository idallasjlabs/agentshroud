---
type: community
members: 2
---

# scripts/gen-code-graph.sh

**Members:** 2 nodes

## Members
- [[Issue one HTTP request and return (status_code, response_text).      HTTPError i]] - rationale - docker/config/hermes/workspace/jira_dev_ticket.py
- [[_http_request()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scripts/gen-code-graphsh
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Bot Skill Config]]

## Top bridge nodes
- [[_http_request()]] - degree 2, connects to 1 community