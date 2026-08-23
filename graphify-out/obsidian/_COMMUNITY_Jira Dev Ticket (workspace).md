---
type: community
cohesion: 0.15
members: 15
---

# Jira Dev Ticket (workspace)

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[jira_dev_ticket add_comment()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_basic_auth_header()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_comment_url()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_issue_url()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_op_proxy_request()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_tenant_info_url()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket build_transitions_url()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket create_issue()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket fetch_credentials()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket fetch_op_secret()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket find_transition_id()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket resolve_cloud_id()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket run()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket transition_issue()]] - code - docker/config/hermes/workspace/jira_dev_ticket.py
- [[jira_dev_ticket.py (OpenClaw copy)]] - code - docker/config/openclaw/workspace/jira_dev_ticket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Jira_Dev_Ticket_workspace
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Jira Weekly Review (workspace)]]
- 2 edges to [[_COMMUNITY_Jira Dev Ticket]]

## Top bridge nodes
- [[jira_dev_ticket run()]] - degree 7, connects to 2 communities
- [[jira_dev_ticket build_basic_auth_header()]] - degree 4, connects to 1 community
- [[jira_dev_ticket resolve_cloud_id()]] - degree 3, connects to 1 community
- [[jira_dev_ticket build_op_proxy_request()]] - degree 2, connects to 1 community
- [[jira_dev_ticket.py (OpenClaw copy)]] - degree 2, connects to 1 community