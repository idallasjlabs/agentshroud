---
type: community
cohesion: 0.10
members: 41
---

# Module Group 106

**Cohesion:** 0.10 - loosely connected
**Members:** 41 nodes

## Members
- [[.__init__()_3]] - code - gateway/cli/client.py
- [[._request()]] - code - gateway/cli/client.py
- [[.add_collaborator()]] - code - gateway/cli/client.py
- [[.add_group_member()]] - code - gateway/cli/client.py
- [[.approve_egress()]] - code - gateway/cli/client.py
- [[.block_egress()]] - code - gateway/cli/client.py
- [[.delete()]] - code - gateway/cli/client.py
- [[.deny_egress()]] - code - gateway/cli/client.py
- [[.freeze()]] - code - gateway/cli/client.py
- [[.get()_1]] - code - gateway/cli/client.py
- [[.get_correlation()]] - code - gateway/cli/client.py
- [[.get_egress_pending()]] - code - gateway/cli/client.py
- [[.get_events()]] - code - gateway/cli/client.py
- [[.get_groups()]] - code - gateway/cli/client.py
- [[.get_health()]] - code - gateway/cli/client.py
- [[.get_logs()]] - code - gateway/cli/client.py
- [[.get_risk()]] - code - gateway/cli/client.py
- [[.get_services()]] - code - gateway/cli/client.py
- [[.get_users()]] - code - gateway/cli/client.py
- [[.post()_1]] - code - gateway/cli/client.py
- [[.put()]] - code - gateway/cli/client.py
- [[.restart_service()]] - code - gateway/cli/client.py
- [[.run_scan()]] - code - gateway/cli/client.py
- [[.set_group_mode()]] - code - gateway/cli/client.py
- [[.stop_service()]] - code - gateway/cli/client.py
- [[.test_empty_response_body_returns_empty_dict()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_get_builds_url_headers_and_parses_json()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_get_with_params_encodes_query_string()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_http_error_with_json_body_returns_parsed_payload()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_http_error_with_non_json_body_returns_error_dict()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_init_strips_trailing_slash_and_builds_soc_base()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_post_serializes_body()]] - code - gateway/tests/test_cli_coverage.py
- [[.test_put_and_delete_methods()]] - code - gateway/tests/test_cli_coverage.py
- [[Any_2]] - code - gateway/cli/client.py
- [[Exception_2]] - code - gateway/tests/test_cli_coverage.py
- [[Minimal synchronous httpx-free client for the SCL API.]] - rationale - gateway/cli/client.py
- [[Patch gateway.cli.client.urlopen; return list of captured Request objects.]] - rationale - gateway/tests/test_cli_coverage.py
- [[SCLClient]] - code - gateway/cli/client.py
- [[TestSCLClientRequest]] - code - gateway/tests/test_cli_coverage.py
- [[_patch_urlopen()]] - code - gateway/tests/test_cli_coverage.py
- [[test_convenience_methods_hit_expected_endpoints()]] - code - gateway/tests/test_cli_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_106
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Module Group 204]]
- 5 edges to [[_COMMUNITY_Module Group 300]]
- 5 edges to [[_COMMUNITY_CLI Interface]]
- 4 edges to [[_COMMUNITY_Module Group 149]]

## Top bridge nodes
- [[SCLClient]] - degree 54, connects to 4 communities
- [[.get()_1]] - degree 13, connects to 1 community
- [[_patch_urlopen()]] - degree 11, connects to 1 community
- [[TestSCLClientRequest]] - degree 10, connects to 1 community
- [[test_convenience_methods_hit_expected_endpoints()]] - degree 3, connects to 1 community
