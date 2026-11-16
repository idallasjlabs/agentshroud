---
type: community
members: 96
---

# Community 50

**Members:** 96 nodes

## Members
- [[.__call__()_7]] - code - gateway/tests/test_edge_jwt.py
- [[.__init__()_23]] - code - gateway/inbound_edge/store.py
- [[.__init__()_172]] - code - gateway/tests/test_edge_jwt.py
- [[._one()]] - code - gateway/inbound_edge/store.py
- [[.add_client()]] - code - gateway/inbound_edge/store.py
- [[.add_ticket()]] - code - gateway/inbound_edge/store.py
- [[.approval_for_ticket()]] - code - gateway/inbound_edge/store.py
- [[.close()_6]] - code - gateway/inbound_edge/store.py
- [[.consume_approval()]] - code - gateway/inbound_edge/store.py
- [[.consume_enrollment()]] - code - gateway/inbound_edge/store.py
- [[.db()]] - code - gateway/inbound_edge/store.py
- [[.enrollment_window_vendor()]] - code - gateway/inbound_edge/store.py
- [[.get_client()_2]] - code - gateway/inbound_edge/store.py
- [[.has_jti()]] - code - gateway/inbound_edge/store.py
- [[.jti_issued()]] - code - gateway/inbound_edge/store.py
- [[.kill()]] - code - gateway/inbound_edge/store.py
- [[.killed_reason()]] - code - gateway/inbound_edge/store.py
- [[.list_clients()]] - code - gateway/inbound_edge/store.py
- [[.list_kills()]] - code - gateway/inbound_edge/store.py
- [[.open_approval_for()]] - code - gateway/inbound_edge/store.py
- [[.open_enrollment()]] - code - gateway/inbound_edge/store.py
- [[.peek_code()]] - code - gateway/inbound_edge/store.py
- [[.peek_pending()]] - code - gateway/inbound_edge/store.py
- [[.peek_refresh()]] - code - gateway/inbound_edge/store.py
- [[.purge_expired()]] - code - gateway/inbound_edge/store.py
- [[.put_approval()]] - code - gateway/inbound_edge/store.py
- [[.put_code()]] - code - gateway/inbound_edge/store.py
- [[.put_pending()]] - code - gateway/inbound_edge/store.py
- [[.put_refresh()]] - code - gateway/inbound_edge/store.py
- [[.record_jti()]] - code - gateway/inbound_edge/store.py
- [[.revoke_refresh_family()]] - code - gateway/inbound_edge/store.py
- [[.rotate_refresh()]] - code - gateway/inbound_edge/store.py
- [[.take_code()]] - code - gateway/inbound_edge/store.py
- [[.take_pending()]] - code - gateway/inbound_edge/store.py
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
- [[.test_sub_must_match_vendor_and_client()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_tampered_payload()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_unkill_restores()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_unsigned_alg_none()]] - code - gateway/tests/test_edge_jwt.py
- [[.test_wrong_issuer()]] - code - gateway/tests/test_edge_jwt.py
- [[.unkill()]] - code - gateway/inbound_edge/store.py
- [[A correctly signed token the issuer has no record of (e.g. from another]] - rationale - gateway/tests/test_edge_jwt.py
- [[Algorithm confusion HMAC 'signed' with the published public key.]] - rationale - gateway/tests/test_edge_jwt.py
- [[Any_9]] - code - gateway/inbound_edge/edge_jwt.py
- [[Any_14]] - code - gateway/inbound_edge/store.py
- [[Async SQLite store. One instance per gateway process.]] - rationale - gateway/inbound_edge/store.py
- [[Atomically mark an approval used. True for exactly one caller.]] - rationale - gateway/inbound_edge/store.py
- [[Clock]] - code - gateway/tests/test_edge_jwt.py
- [[Connection]] - code - gateway/inbound_edge/store.py
- [[Consume a refresh token. Reuse of a consumed token revokes its family.]] - rationale - gateway/inbound_edge/store.py
- [[Edge-side pre-screen signature, alg, iss, aud, exp. No revocation check.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[EdgeStore_4]] - code - gateway/inbound_edge/store.py
- [[Mint a one-time code the owner types on the consent page. Returned once.]] - rationale - gateway/inbound_edge/store.py
- [[Path_2]] - code - gateway/inbound_edge/store.py
- [[RFC 7009 revocation of a refresh token kills its whole family.]] - rationale - gateway/inbound_edge/store.py
- [[Return and delete an unexpired code. A second call returns None.]] - rationale - gateway/inbound_edge/store.py
- [[Sign arbitrary claims with the real key (as if minted outside the issuer).]] - rationale - gateway/tests/test_edge_jwt.py
- [[TestEnrollment]] - code - gateway/tests/test_edge_jwt.py
- [[TestRejected]] - code - gateway/tests/test_edge_jwt.py
- [[TestRevocationAndKill]] - code - gateway/tests/test_edge_jwt.py
- [[TestSingleUseGrants]] - code - gateway/tests/test_edge_jwt.py
- [[TestValidToken]] - code - gateway/tests/test_edge_jwt.py
- [[The newest unconsumed, unexpired request_id for this idempotency key.]] - rationale - gateway/inbound_edge/store.py
- [[The vendor with an open (unused, unexpired) enrollment, if exactly one.]] - rationale - gateway/inbound_edge/store.py
- [[True exactly once for an unexpired code bound to ``vendor``; else None.]] - rationale - gateway/inbound_edge/store.py
- [[Whether ``jti`` was ever issued (and not yet purged) — guards a typo'd kill.]] - rationale - gateway/inbound_edge/store.py
- [[_decode()]] - code - gateway/inbound_edge/edge_jwt.py
- [[_forge()]] - code - gateway/tests/test_edge_jwt.py
- [[_h()]] - code - gateway/inbound_edge/store.py
- [[_token()]] - code - gateway/tests/test_edge_jwt.py
- [[edge_jwt.py]] - code - gateway/inbound_edge/edge_jwt.py
- [[store()_2]] - code - gateway/tests/test_edge_jwt.py
- [[store.py_1]] - code - gateway/inbound_edge/store.py
- [[test_edge_jwt.py]] - code - gateway/tests/test_edge_jwt.py
- [[verify_signature_only()]] - code - gateway/inbound_edge/edge_jwt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_50
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_Community 32]]
- 14 edges to [[_COMMUNITY_Community 2048]]
- 2 edges to [[_COMMUNITY_Community 41]]
- 2 edges to [[_COMMUNITY_Community 75]]
- 1 edge to [[_COMMUNITY_Community 30]]

## Top bridge nodes
- [[EdgeStore_4]] - degree 53, connects to 4 communities
- [[TestRejected]] - degree 16, connects to 2 communities
- [[test_edge_jwt.py]] - degree 15, connects to 2 communities
- [[TestRevocationAndKill]] - degree 9, connects to 2 communities
- [[edge_jwt.py]] - degree 7, connects to 2 communities