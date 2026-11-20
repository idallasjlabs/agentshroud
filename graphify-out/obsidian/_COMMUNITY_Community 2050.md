---
type: community
members: 27
---

# Community 2050

**Members:** 27 nodes

## Members
- [[.test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Regression tests for v1beta proxy response handling.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test mcpproxy endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test status endpoint.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test approval queue endpoints.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestApprovalEndpoints]] - code - gateway/tests/test_main_endpoints.py
- [[TestGoogleAPIProxy]] - code - gateway/tests/test_main_endpoints.py
- [[TestMCPProxyEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestStatusEndpoint]] - code - gateway/tests/test_main_endpoints.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2050
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 37]]
- 4 edges to [[_COMMUNITY_Community 1]]
- 4 edges to [[_COMMUNITY_Community 53]]
- 4 edges to [[_COMMUNITY_Community 1658]]
- 1 edge to [[_COMMUNITY_Community 2154]]

## Top bridge nodes
- [[TestApprovalEndpoints]] - degree 6, connects to 3 communities
- [[TestGoogleAPIProxy]] - degree 6, connects to 3 communities
- [[TestStatusEndpoint]] - degree 5, connects to 3 communities
- [[TestMCPProxyEndpoint]] - degree 5, connects to 3 communities
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community