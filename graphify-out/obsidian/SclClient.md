---
source_file: "gateway/cli/client.py"
type: "code"
community: "Client (cli)"
location: "L14"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Client_cli
---

# SCLClient

## Connections
- [[.__init__()_7]] - `method` [EXTRACTED]
- [[._request()]] - `method` [EXTRACTED]
- [[.add_collaborator()]] - `method` [EXTRACTED]
- [[.add_group_member()]] - `method` [EXTRACTED]
- [[.approve_egress()]] - `method` [EXTRACTED]
- [[.block_egress()]] - `method` [EXTRACTED]
- [[.delete()]] - `method` [EXTRACTED]
- [[.deny_egress()]] - `method` [EXTRACTED]
- [[.freeze()]] - `method` [EXTRACTED]
- [[.get()_2]] - `method` [EXTRACTED]
- [[.get_correlation()]] - `method` [EXTRACTED]
- [[.get_egress_pending()]] - `method` [EXTRACTED]
- [[.get_events()]] - `method` [EXTRACTED]
- [[.get_groups()]] - `method` [EXTRACTED]
- [[.get_health()]] - `method` [EXTRACTED]
- [[.get_logs()]] - `method` [EXTRACTED]
- [[.get_risk()]] - `method` [EXTRACTED]
- [[.get_services()]] - `method` [EXTRACTED]
- [[.get_users()]] - `method` [EXTRACTED]
- [[.post()_2]] - `method` [EXTRACTED]
- [[.put()]] - `method` [EXTRACTED]
- [[.restart_service()]] - `method` [EXTRACTED]
- [[.run_scan()]] - `method` [EXTRACTED]
- [[.set_group_mode()]] - `method` [EXTRACTED]
- [[.stop_service()]] - `method` [EXTRACTED]
- [[.test_empty_response_body_returns_empty_dict()]] - `calls` [EXTRACTED]
- [[.test_get_builds_url_headers_and_parses_json()]] - `calls` [EXTRACTED]
- [[.test_get_with_params_encodes_query_string()]] - `calls` [EXTRACTED]
- [[.test_http_error_with_json_body_returns_parsed_payload()]] - `calls` [EXTRACTED]
- [[.test_http_error_with_non_json_body_returns_error_dict()]] - `calls` [EXTRACTED]
- [[.test_init_strips_trailing_slash_and_builds_soc_base()]] - `calls` [EXTRACTED]
- [[.test_post_serializes_body()]] - `calls` [EXTRACTED]
- [[.test_put_and_delete_methods()]] - `calls` [EXTRACTED]
- [[Any_4]] - `uses` [INFERRED]
- [[Exception_3]] - `uses` [INFERRED]
- [[Minimal synchronous httpx-free client for the SCL API.]] - `rationale_for` [EXTRACTED]
- [[TestClientFromEnv]] - `uses` [INFERRED]
- [[TestEgressAndAdminCommands]] - `uses` [INFERRED]
- [[TestGetCommands]] - `uses` [INFERRED]
- [[TestLifecycleCommands]] - `uses` [INFERRED]
- [[TestOutputHelpers]] - `uses` [INFERRED]
- [[TestSCLClientRequest]] - `uses` [INFERRED]
- [[TestTailCommand]] - `uses` [INFERRED]
- [[TestTailWS]] - `uses` [INFERRED]
- [[_FakeConnect]] - `uses` [INFERRED]
- [[_FakeHTTPResponse]] - `uses` [INFERRED]
- [[_FakeWS]] - `uses` [INFERRED]
- [[agentshroud-soc CLI Group]] - `calls` [EXTRACTED]
- [[cli()]] - `calls` [EXTRACTED]
- [[client.py]] - `contains` [EXTRACTED]
- [[client_from_env()]] - `references` [EXTRACTED]
- [[main.py_1]] - `imports` [EXTRACTED]
- [[tail()]] - `calls` [EXTRACTED]
- [[test_cli_coverage.py]] - `imports` [EXTRACTED]
- [[test_convenience_methods_hit_expected_endpoints()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Client_cli