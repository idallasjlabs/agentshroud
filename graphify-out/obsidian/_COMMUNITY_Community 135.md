---
type: community
members: 50
---

# Community 135

**Members:** 50 nodes

## Members
- [[.__call__()_7]] - code - gateway/tests/test_edge_jwt.py
- [[.__init__()_169]] - code - gateway/tests/test_edge_jwt.py
- [[.test_auth_code_is_single_use()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_bad_kill_scope_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_edge_can_check_signature_with_public_key_only()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_enrollment_code_single_use_and_vendor_bound()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_enrollment_expires()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_es256_with_wrong_curve_key_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_expired()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_expired_auth_code()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_hs256_signed_with_public_key()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_issued_in_the_future()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_jti_never_issued_is_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_kill_takes_effect_within_one_second()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_killed_client()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_killed_vendor_blocks_all_its_tokens()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_lifetime_is_15_minutes()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_lifetime_longer_than_policy()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_minted_token_verifies()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_missing_required_claims()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_open_window_names_vendor()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_refresh_rotation_and_reuse_revokes_family()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_revoked_jti()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_secrets_are_stored_hashed()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_signed_by_another_key()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_sub_must_match_vendor_and_client()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_tampered_payload()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_unkill_restores()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_unsigned_alg_none()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_wrong_audience()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_wrong_issuer()]] - code - gateway/tests/test_edge_jwt.py
- [[A correctly signed token the issuer has no record of (e.g. from another]] - rationale - gateway/tests/test_edge_jwt.py
- [[Algorithm confusion HMAC 'signed' with the published public key.]] - rationale - gateway/tests/test_edge_jwt.py
- [[Any_9]] - code - gateway/inbound_edge/edge_jwt.py
- [[Clock]] - code - gateway/tests/test_edge_jwt.py
- [[Edge-side pre-screen signature, alg, iss, aud, exp. No revocation check.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[Sign arbitrary claims with the real key (as if minted outside the issuer).]] - rationale - gateway/tests/test_edge_jwt.py
- [[TestEnrollment]] - code - gateway/tests/test_edge_jwt.py
- [[TestRejected]] - code - gateway/tests/test_edge_jwt.py
- [[TestRevocationAndKill]] - code - gateway/tests/test_edge_jwt.py
- [[TestSingleUseGrants]] - code - gateway/tests/test_edge_jwt.py
- [[TestValidToken]] - code - gateway/tests/test_edge_jwt.py
- [[_forge()]] - code - gateway/tests/test_edge_jwt.py
- [[_token()]] - code - gateway/tests/test_edge_jwt.py
- [[generate_signing_key_pem()]] - code - gateway/inbound_edge/edge_jwt.py
- [[secrets_dir()_1]] - code - gateway/tests/test_edge_service_routes.py
- [[store()_2]] - code - gateway/tests/test_edge_jwt.py
- [[svc()]] - code - gateway/tests/test_edge_jwt.py
- [[test_edge_jwt.py]] - code - gateway/tests/test_edge_jwt.py
- [[verify_signature_only()]] - code - gateway/inbound_edge/edge_jwt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_135
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Community 2048]]
- 6 edges to [[_COMMUNITY_Community 41]]
- 2 edges to [[_COMMUNITY_Community 32]]
- 2 edges to [[_COMMUNITY_Community 84]]
- 2 edges to [[_COMMUNITY_Community 50]]

## Top bridge nodes
- [[generate_signing_key_pem()]] - degree 13, connects to 4 communities
- [[test_edge_jwt.py]] - degree 15, connects to 2 communities
- [[verify_signature_only()]] - degree 9, connects to 2 communities
- [[TestRejected]] - degree 16, connects to 1 community
- [[TestRevocationAndKill]] - degree 9, connects to 1 community