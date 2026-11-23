---
type: community
members: 28
---

# TestRejected

**Members:** 28 nodes

## Members
- [[dot-test_bad_kill_scope_rejected()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_edge_can_check_signature_with_public_key_only()]] - code - gateway/tests/test_edge_jwt.py
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
- [[dot-test_revoked_jti()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_sub_must_match_vendor_and_client()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_tampered_payload()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_unkill_restores()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_unsigned_alg_none()]] - code - gateway/tests/test_edge_jwt.py
- [[dot-test_wrong_issuer()]] - code - gateway/tests/test_edge_jwt.py
- [[A correctly signed token the issuer has no record of (e.g. from another…]] - rationale - gateway/tests/test_edge_jwt.py
- [[Algorithm confusion HMAC 'signed' with the published public key.]] - rationale - gateway/tests/test_edge_jwt.py
- [[Sign arbitrary claims with the real key (as if minted outside the issuer).]] - rationale - gateway/tests/test_edge_jwt.py
- [[TestRejected]] - code - gateway/tests/test_edge_jwt.py
- [[TestRevocationAndKill]] - code - gateway/tests/test_edge_jwt.py
- [[TestValidToken]] - code - gateway/tests/test_edge_jwt.py
- [[_forge()]] - code - gateway/tests/test_edge_jwt.py
- [[_token()_1]] - code - gateway/tests/test_edge_jwt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestRejected
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_EnhancedApprovalQueue]]

## Top bridge nodes
- [[TestRejected]] - degree 16, connects to 1 community
- [[_token()_1]] - degree 12, connects to 1 community
- [[TestRevocationAndKill]] - degree 8, connects to 1 community
- [[_forge()]] - degree 8, connects to 1 community
- [[TestValidToken]] - degree 4, connects to 1 community
