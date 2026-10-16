---
type: community
cohesion: 0.08
members: 44
---

# _FakeRBAC

**Cohesion:** 0.08 - loosely connected
**Members:** 44 nodes

## Members
- [[dot-_build_record()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_rbac()]] - code - gateway/soc/contributors.py
- [[dot-_ensure_teams()]] - code - gateway/soc/contributors.py
- [[dot-_load_paused_ids()]] - code - gateway/soc/contributors.py
- [[dot-get_contributor()]] - code - gateway/soc/contributors.py
- [[dot-list_contributors()]] - code - gateway/soc/contributors.py
- [[dot-test_approved_status()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_confirmation_required()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_1]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_2]] - code - gateway/tests/test_soc_models.py
- [[dot-test_defaults()_2]] - code - gateway/tests/test_soc_models.py
- [[dot-test_destructive_requires_confirmation()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_error_model()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_pending_status_default()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_permission_denied_error()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_red_risk_high_threat()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_with_resource_usage()]] - code - gateway/tests/test_soc_models.py
- [[Alarm]] - code - gateway/soc/models.py
- [[AlarmStatus]] - code - gateway/soc/models.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[ContributorRecord_1]] - code - gateway/soc/models.py
- [[EgressRequest_1]] - code - gateway/soc/models.py
- [[EgressStatus]] - code - gateway/soc/models.py
- [[Platform]] - code - gateway/soc/models.py
- [[ResourceUsage_2]] - code - gateway/soc/models.py
- [[RiskLevel_6]] - code - gateway/soc/models.py
- [[SCLError]] - code - gateway/soc/models.py
- [[TestConfirmationModel]] - code - gateway/tests/test_soc_egress.py
- [[TestContributorRecord]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequest]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequestModel]] - code - gateway/tests/test_soc_egress.py
- [[TestSCLError]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptor]] - code - gateway/tests/test_soc_models.py
- [[TestWSEvent]] - code - gateway/tests/test_soc_models.py
- [[UserRole]] - code - gateway/soc/models.py
- [[UserRole_1]] - code - gateway/soc/contributors.py
- [[_new_uuid()]] - code - gateway/soc/models.py
- [[_now_iso()]] - code - gateway/soc/models.py
- [[_role_enum()]] - code - gateway/soc/contributors.py
- [[contributors.py]] - code - gateway/soc/contributors.py
- [[socmodels.py]] - code - gateway/soc/models.py
- [[test_soc_egress.py]] - code - gateway/tests/test_soc_egress.py
- [[test_soc_models.py]] - code - gateway/tests/test_soc_models.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeRBAC
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY__FakeRBAC]]
- 9 edges to [[_COMMUNITY_ServiceManager_1]]
- 8 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 8 edges to [[_COMMUNITY_MiddlewareManager]]
- 6 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_SlackAPIProxy]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py_1]]
- 2 edges to [[_COMMUNITY_soc.js]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[socmodels.py]] - degree 29, connects to 6 communities
- [[test_soc_models.py]] - degree 22, connects to 4 communities
- [[ContributorRecord_1]] - degree 10, connects to 3 communities
- [[contributors.py]] - degree 8, connects to 3 communities
- [[Platform]] - degree 8, connects to 3 communities
