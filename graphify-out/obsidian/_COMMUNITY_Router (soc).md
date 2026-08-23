---
type: community
cohesion: 0.07
members: 84
---

# Router (soc)

**Cohesion:** 0.07 - loosely connected
**Members:** 84 nodes

## Members
- [[.__init__()_129]] - code - gateway/soc/auth.py
- [[.__init__()_130]] - code - gateway/soc/contributors.py
- [[.__init__()_181]] - code - gateway/tests/test_soc_contributors.py
- [[.__init__()_182]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.check_permission()_2]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.get_user_role()_3]] - code - gateway/tests/test_soc_contributors.py
- [[.is_group_admin()_1]] - code - gateway/soc/auth.py
- [[.is_owner()_2]] - code - gateway/soc/auth.py
- [[.require()]] - code - gateway/soc/auth.py
- [[.test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_get_caller_passthrough()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_get_rbac_manager_builds_real_manager()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_with_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_group_admin_without_teams_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_is_owner_delegates_to_config()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[.test_require_allowed_does_not_raise()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_raises_403_with_reason()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_require_denied_without_reason_uses_forbidden()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[Action_2]] - code - gateway/soc/auth.py
- [[AddCollaboratorRequest]] - code - gateway/soc/router.py
- [[AddGroupMemberRequest]] - code - gateway/soc/router.py
- [[Any_67]] - code - gateway/soc/router.py
- [[ApprovalDecisionRequest]] - code - gateway/soc/router.py
- [[AuditLogEntry]] - code - gateway/soc/models.py
- [[AuditResult_1]] - code - gateway/soc/router.py
- [[AuditResult]] - code - gateway/soc/models.py
- [[BaseModel]] - code
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Builds ContributorRecord instances from RBACConfig + TeamsConfig.]] - rationale - gateway/soc/contributors.py
- [[Check group admin status via TeamsConfig if available.]] - rationale - gateway/soc/auth.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[ContributorManager]] - code - gateway/soc/contributors.py
- [[CreateDelegationRequest]] - code - gateway/soc/router.py
- [[CreateGroupRequest]] - code - gateway/soc/router.py
- [[DisconnectRequest]] - code - gateway/soc/router.py
- [[EgressApproveRequest]] - code - gateway/soc/router.py
- [[EgressRuleOverrideRequest]] - code - gateway/soc/router.py
- [[EgressScopeRequest]] - code - gateway/soc/router.py
- [[EmergencyBlockRequest]] - code - gateway/soc/router.py
- [[Fallback minimal dashboard when template file is missing.]] - rationale - gateway/soc/router.py
- [[GET users endpoint]] - code - gateway/soc/router.py
- [[LoginRequest]] - code - gateway/soc/router.py
- [[Minimal RBAC stand-in with controllable check_permission results.]] - rationale - gateway/tests/test_soc_realtime_coverage.py
- [[Public FastAPI dependency injected by SCL route handlers.]] - rationale - gateway/soc/auth.py
- [[RBACManager_2]] - code - gateway/soc/auth.py
- [[Raise 403 if the caller lacks the required permission.]] - rationale - gateway/soc/auth.py
- [[RenameGroupRequest]] - code - gateway/soc/router.py
- [[Request_6]] - code - gateway/soc/router.py
- [[Request_10]] - code - gateway/soc/router.py
- [[Resolved identity of the SCL caller, including role and user_id.]] - rationale - gateway/soc/auth.py
- [[Resource_2]] - code - gateway/soc/auth.py
- [[Role_2]] - code - gateway/soc/auth.py
- [[SCLCaller]] - code - gateway/soc/auth.py
- [[SCLConfirmationRequired]] - code - gateway/soc/models.py
- [[SCLInterface_1]] - code - gateway/soc/router.py
- [[SCLInterface]] - code - gateway/soc/models.py
- [[ScanRequest_1]] - code - gateway/soc/router.py
- [[Serve the unified SOC web dashboard.]] - rationale - gateway/soc/router.py
- [[SetLogLevelRequest]] - code - gateway/soc/router.py
- [[SetModeRequest]] - code - gateway/soc/router.py
- [[SetModuleModeRequest]] - code - gateway/soc/router.py
- [[SetRoleRequest]] - code - gateway/soc/router.py
- [[SetUserModeRequest]] - code - gateway/soc/router.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestSCLCaller]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[UpdateDisplayNameRequest]] - code - gateway/soc/router.py
- [[WebSocket_5]] - code - gateway/soc/router.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_FakeRBAC_2]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[_minimal_dashboard_html()]] - code - gateway/soc/router.py
- [[get_caller()]] - code - gateway/soc/auth.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[soc_dashboard()]] - code - gateway/soc/router.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Router_soc
SORT file.name ASC
```

## Connections to other communities
- 78 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 25 edges to [[_COMMUNITY_SOC Services]]
- 23 edges to [[_COMMUNITY_Soc Models]]
- 23 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 9 edges to [[_COMMUNITY_Progressive Lockdown]]
- 7 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 5 edges to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]
- 4 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 4 edges to [[_COMMUNITY_Api (web)]]
- 4 edges to [[_COMMUNITY_Soc Realtime Coverage]]
- 3 edges to [[_COMMUNITY_Config]]
- 3 edges to [[_COMMUNITY_Enhanced Approval]]
- 3 edges to [[_COMMUNITY_Forward (routes)]]
- 3 edges to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 3 edges to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 3 edges to [[_COMMUNITY_Soc Bots]]
- 3 edges to [[_COMMUNITY_Soc Websocket]]
- 3 edges to [[_COMMUNITY_Web Api Coverage]]
- 3 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 2 edges to [[_COMMUNITY_Main (chatbot)]]
- 2 edges to [[_COMMUNITY_All Modules Enforce]]
- 2 edges to [[_COMMUNITY_Tool Result Pii]]
- 2 edges to [[_COMMUNITY_Agentshroud Manager]]
- 2 edges to [[_COMMUNITY_Intel Report (security)]]
- 2 edges to [[_COMMUNITY_Installer (web)]]
- 2 edges to [[_COMMUNITY_Management (web)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Router]]
- 1 edge to [[_COMMUNITY_Soc Egress Endpoints]]
- 1 edge to [[_COMMUNITY_Queue (approval_queue)]]
- 1 edge to [[_COMMUNITY_Approval Queue]]
- 1 edge to [[_COMMUNITY_Config Validation & Router]]
- 1 edge to [[_COMMUNITY_Auth]]
- 1 edge to [[_COMMUNITY_Intel Pipeline]]
- 1 edge to [[_COMMUNITY_Rbac Config (security)]]
- 1 edge to [[_COMMUNITY_SOC Router Coverage]]

## Top bridge nodes
- [[BaseModel]] - degree 86, connects to 29 communities
- [[ContributorManager]] - degree 60, connects to 5 communities
- [[SCLCaller]] - degree 46, connects to 4 communities
- [[AuditResult]] - degree 33, connects to 3 communities
- [[SCLInterface]] - degree 33, connects to 3 communities