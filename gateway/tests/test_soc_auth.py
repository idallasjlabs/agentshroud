# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/soc/auth.py — SCL authentication and WS token issuance."""

from __future__ import annotations

import time
import pytest

from gateway.soc.auth import issue_ws_token, redeem_ws_token, _ws_tokens


class TestWSTokens:
    def setup_method(self):
        """Clear token store before each test."""
        _ws_tokens.clear()

    def test_issue_and_redeem(self):
        token = issue_ws_token("user-1")
        assert token is not None
        user_id = redeem_ws_token(token)
        assert user_id == "user-1"

    def test_single_use(self):
        token = issue_ws_token("user-2")
        redeem_ws_token(token)
        # Second redemption must fail
        assert redeem_ws_token(token) is None

    def test_expired_token_rejected(self):
        token = issue_ws_token("user-3")
        # Backdate the issued_at timestamp so it exceeds the 300s TTL
        user_id, _issued = _ws_tokens[token]
        _ws_tokens[token] = (user_id, time.time() - 400)
        assert redeem_ws_token(token) is None

    def test_invalid_token_rejected(self):
        assert redeem_ws_token("not-a-real-token") is None

    def test_empty_token_rejected(self):
        assert redeem_ws_token("") is None

    def test_multiple_tokens_independent(self):
        t1 = issue_ws_token("user-a")
        t2 = issue_ws_token("user-b")
        assert redeem_ws_token(t1) == "user-a"
        assert redeem_ws_token(t2) == "user-b"
