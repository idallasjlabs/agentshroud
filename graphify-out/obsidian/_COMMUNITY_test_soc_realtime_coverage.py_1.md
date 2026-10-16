---
type: community
cohesion: 0.12
members: 31
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.12 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-setup_method()_23]] - code - gateway/tests/test_soc_auth.py
- [[dot-setup_method()_24]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[dot-test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestTokenStorePruning]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 7 edges to [[_COMMUNITY_Action]]
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[issue_ws_token()]] - degree 15, connects to 3 communities
- [[issue_session_token()]] - degree 14, connects to 3 communities
- [[TestTokenStorePruning]] - degree 10, connects to 3 communities
- [[redeem_ws_token()]] - degree 14, connects to 2 communities
- [[_verify_session_token()]] - degree 10, connects to 2 communities
