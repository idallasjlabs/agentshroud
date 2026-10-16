---
type: community
cohesion: 0.08
members: 32
---

# _is_op_reference_allowed

**Cohesion:** 0.08 - loosely connected
**Members:** 32 nodes

## Members
- [[dot-test_allowed_path_different_item()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_allowed_path_passes()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_atlassian_token_allowed()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_brave_api_key_reference_allowed()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_disallowed_vault_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_disallowed_vault_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_empty_reference_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_every_dedicated_op_ref_is_allowlisted()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_malformed_reference_returns_422()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_missing_op_prefix_blocked()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_op_subprocess_failure_returns_502()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_path_traversal_blocked()_1]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_path_traversal_returns_403()]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_requires_auth()_2]] - code - gateway/tests/test_op_proxy.py
- [[dot-test_valid_reference_returns_value()]] - code - gateway/tests/test_op_proxy.py
- [[1Password credential proxy (P2 credential isolation). Reads a secret from…]] - rationale - gateway/ingest_api/main.py
- [[Endpoint returns 401 without auth override.]] - rationale - gateway/tests/test_op_proxy.py
- [[OpProxyRequest]] - code - gateway/ingest_api/main.py
- [[Real functional check, not a boot-time smoke test every op reference     doc]] - rationale - gateway/tests/test_op_proxy.py
- [[Request body for POST credentialsop-proxy.]] - rationale - gateway/ingest_api/main.py
- [[Return True if the op reference matches an allowed path pattern.]] - rationale - gateway/ingest_api/main.py
- [[SCRUM-81 Hermes weekly Jira review needs tokenemaildomain fields.]] - rationale - gateway/tests/test_op_proxy.py
- [[TestIsOpReferenceAllowed]] - code - gateway/tests/test_op_proxy.py
- [[TestOpProxyEndpoint]] - code - gateway/tests/test_op_proxy.py
- [[TestOpRefAllowlistCoverage]] - code - gateway/tests/test_op_proxy.py
- [[The vault has no item literally titled Brave Search API Key —         the real]] - rationale - gateway/tests/test_op_proxy.py
- [[_do_op_read()]] - code - gateway/ingest_api/main.py
- [[_is_op_reference_allowed()]] - code - gateway/ingest_api/main.py
- [[_refresh_session()]] - code - gateway/ingest_api/main.py
- [[client()_8]] - code - gateway/tests/test_op_proxy.py
- [[op_proxy()]] - code - gateway/ingest_api/main.py
- [[test_op_proxy.py]] - code - gateway/tests/test_op_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_is_op_reference_allowed
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 2 edges to [[_COMMUNITY_test_main_endpoints.py]]
- 1 edge to [[_COMMUNITY__FakeRBAC]]
- 1 edge to [[_COMMUNITY_AuditChain_1]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh]]
- 1 edge to [[_COMMUNITY_start-agentshroud.sh]]
- 1 edge to [[_COMMUNITY_setup-secrets.sh_1]]

## Top bridge nodes
- [[TestIsOpReferenceAllowed]] - degree 12, connects to 2 communities
- [[op_proxy()]] - degree 8, connects to 2 communities
- [[test_op_proxy.py]] - degree 7, connects to 2 communities
- [[OpProxyRequest]] - degree 4, connects to 2 communities
- [[_is_op_reference_allowed()]] - degree 15, connects to 1 community
