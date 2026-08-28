---
type: community
cohesion: 0.12
members: 30
---

# Community 265

**Cohesion:** 0.12 - loosely connected
**Members:** 30 nodes

## Members
- [[.setup_method()_35]] - code - gateway/tests/test_soc_auth.py
- [[.setup_method()_34]] - code - gateway/tests/test_soc_auth.py
- [[.test_different_keys_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_different_owners_produce_different_tokens()]] - code - gateway/tests/test_soc_auth.py
- [[.test_empty_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_expired_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_invalid_token_rejected()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_and_redeem()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_returns_hex_string()]] - code - gateway/tests/test_soc_auth.py
- [[.test_issue_session_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_issue_ws_token_prunes_expired()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_multiple_tokens_independent()]] - code - gateway/tests/test_soc_auth.py
- [[.test_redeem_expired_ws_token_returns_none()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_single_use()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_after_clear_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_expired_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_unknown_token_returns_none()]] - code - gateway/tests/test_soc_auth.py
- [[.test_verify_valid_token()]] - code - gateway/tests/test_soc_auth.py
- [[Clear token store before each test.]] - rationale - gateway/tests/test_soc_auth.py
- [[Consume a WS token and return the user_id, or None if invalidexpired.]] - rationale - gateway/soc/auth.py
- [[Derive an HMAC session token and register it in the session store.]] - rationale - gateway/soc/auth.py
- [[Issue a short-lived, single-use WebSocket token for a user.]] - rationale - gateway/soc/auth.py
- [[Return user_id if token is a valid unexpired session token, else None.]] - rationale - gateway/soc/auth.py
- [[TestSessionTokens]] - code - gateway/tests/test_soc_auth.py
- [[TestWSTokens]] - code - gateway/tests/test_soc_auth.py
- [[_verify_session_token()]] - code - gateway/soc/auth.py
- [[issue_session_token()]] - code - gateway/soc/auth.py
- [[issue_ws_token()]] - code - gateway/soc/auth.py
- [[redeem_ws_token()]] - code - gateway/soc/auth.py
- [[test_soc_auth.py]] - code - gateway/tests/test_soc_auth.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_265
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_RBAC & SOC Realtime]]
- 5 edges to [[_COMMUNITY_Community 69]]
- 3 edges to [[_COMMUNITY_SOC Collaborators]]
- 1 edge to [[_COMMUNITY_Community 14]]

## Top bridge nodes
- [[issue_ws_token()]] - degree 15, connects to 3 communities
- [[issue_session_token()]] - degree 14, connects to 3 communities
- [[redeem_ws_token()]] - degree 14, connects to 2 communities
- [[_verify_session_token()]] - degree 10, connects to 1 community
- [[.test_issue_session_token_prunes_expired()]] - degree 3, connects to 1 community