---
type: community
cohesion: 0.06
members: 36
---

# Community 197

**Cohesion:** 0.06 - loosely connected
**Members:** 36 nodes

## Members
- [[Limit param caps the number of returned items.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Returns empty result when scanner_result_history is empty.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Returns scanner events from app_state.scanner_result_history.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Status query param filters by summary.status.]] - rationale - gateway/tests/test_soc_egress_endpoints.py
- [[Synthetic v1modelsid shim for hermes v0.16.0 OAuth-token preflight incompatibility]] - rationale - gateway/tests/test_v1_models_synthetic.py
- [[TestClient with a stubbed proxy IP that passes the network allowlist.]] - rationale - gateway/tests/test_v1_models_synthetic.py
- [[app_state]] - code - gateway/ingest_api/main.py
- [[client()_18]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_manage_egress_add_remove_rule_and_risk()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_emergency_toggle()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_log_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_pending_endpoint_includes_summary()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_egress_rules_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_privacy_policy_and_audit_endpoints()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scan_all_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scanners_history_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_scanners_summary_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_correlation_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_events_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_export_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_export_invalid_format()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_report_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_manage_soc_report_falls_back_to_contributor_logs()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_outbound_quarantine_endpoints()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_list_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_release_and_discard_flow()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_quarantine_summary_endpoint()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_egress_endpoints.py]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_empty()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_limit()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_returns_history()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_soc_scanners_recent_status_filter()]] - code - gateway/tests/test_soc_egress_endpoints.py
- [[test_v1_messages_still_goes_through_proxy()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_get_returns_synthetic_200()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_post_still_goes_through_proxy()]] - code - gateway/tests/test_v1_models_synthetic.py
- [[test_v1_models_synthetic.py]] - code - gateway/tests/test_v1_models_synthetic.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_197
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 21]]
- 1 edge to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 884]]
- 1 edge to [[_COMMUNITY_Community 24]]

## Top bridge nodes
- [[test_soc_egress_endpoints.py]] - degree 25, connects to 2 communities
- [[test_manage_soc_report_endpoint()]] - degree 4, connects to 2 communities
- [[client()_18]] - degree 3, connects to 1 community
- [[test_manage_soc_events_endpoint()]] - degree 2, connects to 1 community