---
type: community
cohesion: 0.06
members: 40
---

# Jira Dev Ticket

**Cohesion:** 0.06 - loosely connected
**Members:** 40 nodes

## Members
- [[.__call__()_7]] - code - gateway/tests/test_jira_dev_ticket.py
- [[.__init__()_167]] - code - gateway/tests/test_jira_dev_ticket.py
- [[Records requests; serves op-proxy secrets then a scripted Jira response.]] - rationale - gateway/tests/test_jira_dev_ticket.py
- [[_MockTransport]] - code - gateway/tests/test_jira_dev_ticket.py
- [[_load_module()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_basic_auth_header_is_base64_email_colon_token()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_basic_auth_header_rejects_empty()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_comment_payload_is_valid_adf_doc()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_comment_payload_never_empty()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_comment_url_rejects_empty_issue_key()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_comment_url_targets_arbitrary_issue()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_create_issue_payload_full()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_create_issue_payload_minimal()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_create_issue_payload_rejects_missing_project()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_create_issue_payload_rejects_missing_summary()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_find_transition_id_matches_destination_status_name()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_find_transition_id_matches_transition_name()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_find_transition_id_returns_none_when_no_match()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_issue_url_rejects_empty_cloud_id()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_issue_url_targets_cloud_id_gateway()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_jira_dev_ticket.py]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_op_proxy_request_has_bearer_and_system_header()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_op_refs_target_the_atlassian_item()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_openclaw_copy_is_byte_identical_to_hermes_copy()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_resolve_cloud_id_parses_response()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_resolve_cloud_id_raises_on_non_200()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_resolve_cloud_id_raises_when_field_missing()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_aborts_without_gateway_token()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_comment_posts_to_correct_issue()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_create_posts_issue_with_basic_auth()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_create_with_labels_and_parent()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_returns_1_on_jira_rejection()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_returns_1_when_op_proxy_denies()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_transition_applies_matching_transition()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_run_transition_fails_when_no_matching_transition()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_tenant_info_url_accepts_full_https_domain()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_tenant_info_url_rejects_empty_domain()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_tenant_info_url_targets_edge_endpoint()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_transitions_url_rejects_empty_issue_key()]] - code - gateway/tests/test_jira_dev_ticket.py
- [[test_transitions_url_targets_arbitrary_issue()]] - code - gateway/tests/test_jira_dev_ticket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Jira_Dev_Ticket
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Jira Dev Ticket (workspace)]]

## Top bridge nodes
- [[test_jira_dev_ticket.py]] - degree 38, connects to 1 community