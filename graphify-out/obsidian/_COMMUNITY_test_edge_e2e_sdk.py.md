---
type: community
members: 90
---

# test_edge_e2e_sdk.py

**Members:** 90 nodes

## Members
- [[dot-__call__()_10]] - code - gateway/tests/test_edge_jwt.py
- [[dot-__call__()_11]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-__init__()_165]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[dot-__init__()_166]] - code - gateway/tests/test_edge_jwt.py
- [[dot-__init__()_167]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-__init__()_168]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-close()_14]] - code - gateway/inbound_edge/service.py
- [[dot-mint_access()]] - code - gateway/inbound_edge/edge_jwt.py
- [[dot-run()_5]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[dot-run()_6]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-service_token_ok()]] - code - gateway/inbound_edge/service.py
- [[dot-test_bad_kill_scope_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_edge_can_check_signature_with_public_key_only()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_enrollment_code_single_use_and_vendor_bound()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_enrollment_expires()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_es256_with_wrong_curve_key_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_expired()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_hs256_signed_with_public_key()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_issued_in_the_future()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_jti_never_issued_is_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_kill_takes_effect_within_one_second()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_killed_client()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_killed_vendor_blocks_all_its_tokens()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_lifetime_is_15_minutes()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_lifetime_longer_than_policy()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_minted_token_verifies()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_missing_required_claims()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_open_window_names_vendor()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_revoked_jti()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_signed_by_another_key()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_sub_must_match_vendor_and_client()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_tampered_payload()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_unkill_restores()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_unsigned_alg_none()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_wrong_audience()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_wrong_issuer()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-verify_access()]] - code - gateway/inbound_edge/edge_jwt.py
- [[A correctly signed token the issuer has no record of (e.g. from another…]] - rationale - gateway/tests/test_edge_jwt.py
- [[AES-256 key for sealing client secrets, derived from the gateway-only signing…]] - rationale - gateway/inbound_edge/oauth_service.py
- [[Algorithm confusion HMAC 'signed' with the published public key.]] - rationale - gateway/tests/test_edge_jwt.py
- [[Any_64]] - code
- [[Clock]] - code - gateway/tests/test_edge_jwt.py
- [[Clock_1]] - code - gateway/tests/test_edge_pipeline.py
- [[Edge-side pre-screen signature, alg, iss, aud, exp. No revocation check.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[EdgeDeps]] - code - gateway/inbound_edge/call_pipeline.py
- [[EdgeService]] - code - gateway/inbound_edge/service.py
- [[Exception_15]] - code
- [[Facade_1]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[FakeFacade]] - code - gateway/tests/test_edge_pipeline.py
- [[Mint and authoritatively verify edge access tokens (gateway only).]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[Shared secret-reading utilities for gateway components.]] - rationale - gateway/utils/secrets.py
- [[Sign arbitrary claims with the real key (as if minted outside the issuer).]] - rationale - gateway/tests/test_edge_jwt.py
- [[TestEnrollment]] - code - gateway/tests/test_edge_jwt.py
- [[TestRejected]] - code - gateway/tests/test_edge_jwt.py
- [[TestRevocationAndKill]] - code - gateway/tests/test_edge_jwt.py
- [[TestValidToken]] - code - gateway/tests/test_edge_jwt.py
- [[The presented token must not be honoured. ``str(exc)`` is safe to audit.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[TokenRejected]] - code - gateway/inbound_edge/edge_jwt.py
- [[TokenService]] - code - gateway/inbound_edge/edge_jwt.py
- [[_client()]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[_decode()]] - code - gateway/inbound_edge/edge_jwt.py
- [[_forge()]] - code - gateway/tests/test_edge_jwt.py
- [[_token()_1]] - code - gateway/tests/test_edge_jwt.py
- [[derive_seal_key()]] - code - gateway/inbound_edge/oauth_service.py
- [[edge()_1]] - code - gateway/tests/test_edge_pipeline.py
- [[edge_jwt.py]] - code - gateway/inbound_edge/edge_jwt.py
- [[emit()_8]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[emit()_9]] - code - gateway/tests/test_edge_pipeline.py
- [[fixture_110]] - code
- [[fixture_111]] - code
- [[fixture_112]] - code
- [[generate_signing_key_pem()]] - code - gateway/inbound_edge/edge_jwt.py
- [[inbound_edgestore.py]] - code - gateway/inbound_edge/store.py
- [[notify()_2]] - code - gateway/tests/test_edge_oauth.py
- [[oauth_service.py]] - code - gateway/inbound_edge/oauth_service.py
- [[profiles.py]] - code - gateway/inbound_edge/profiles.py
- [[secrets.py]] - code - gateway/utils/secrets.py
- [[service.py]] - code - gateway/inbound_edge/service.py
- [[stack()]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[store()_3]] - code - gateway/tests/test_edge_jwt.py
- [[svc()]] - code - gateway/tests/test_edge_jwt.py
- [[svc()_1]] - code - gateway/tests/test_edge_oauth.py
- [[test_edge_e2e_sdk.py]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[test_edge_guard()]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[test_edge_jwt.py]] - code - gateway/tests/test_edge_jwt.py
- [[test_edge_oauth.py]] - code - gateway/tests/test_edge_oauth.py
- [[test_edge_pipeline.py]] - code - gateway/tests/test_edge_pipeline.py
- [[test_gateway_rpc_requires_service_token()]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[test_registration_refused_without_enrollment_window()]] - code - gateway/tests/test_edge_e2e_sdk.py
- [[verify_signature_only()]] - code - gateway/inbound_edge/edge_jwt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_edge_e2e_sdkpy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 27 edges to [[_COMMUNITY_make_event]]
- 22 edges to [[_COMMUNITY_lifespan.py]]
- 17 edges to [[_COMMUNITY_EdgeStore]]
- 16 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 15 edges to [[_COMMUNITY__token]]
- 15 edges to [[_COMMUNITY_test_edge_approvals.py]]
- 14 edges to [[_COMMUNITY_EdgeOAuthService]]
- 10 edges to [[_COMMUNITY_GatewayBackedProvider]]
- 8 edges to [[_COMMUNITY__client_info]]
- 7 edges to [[_COMMUNITY_CanaryTripwire]]
- 7 edges to [[_COMMUNITY_EncodingDetector]]
- 6 edges to [[_COMMUNITY_EnvelopeSigner]]
- 5 edges to [[_COMMUNITY_load_profiles]]
- 5 edges to [[_COMMUNITY_socrouter.py]]
- 4 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 4 edges to [[_COMMUNITY_AuditStore]]
- 3 edges to [[_COMMUNITY_LockdownLevel]]
- 3 edges to [[_COMMUNITY_read_secret]]
- 3 edges to [[_COMMUNITY_prompt_guard.py]]
- 3 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_AuditEvent]]
- 1 edge to [[_COMMUNITY_MemoryTokenStorage]]
- 1 edge to [[_COMMUNITY_TestSingleUseGrants]]
- 1 edge to [[_COMMUNITY_normalize_input]]
- 1 edge to [[_COMMUNITY_test_edge_fuzz.py]]
- 1 edge to [[_COMMUNITY_dot-test_events_api_envelope_dispatches_handle_event]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY__write]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_SessionManager]]
- 1 edge to [[_COMMUNITY_mcp_oauth_preflight.py]]

## Top bridge nodes
- [[test_edge_e2e_sdk.py]] - degree 52, connects to 17 communities
- [[service.py]] - degree 39, connects to 14 communities
- [[test_edge_pipeline.py]] - degree 50, connects to 13 communities
- [[secrets.py]] - degree 22, connects to 13 communities
- [[stack()]] - degree 31, connects to 11 communities
