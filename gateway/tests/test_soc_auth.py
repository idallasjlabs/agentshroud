# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/soc/auth.py — SCL authentication and WS token issuance."""

from __future__ import annotations

import time

import pytest

from gateway.soc.auth import (
    _session_tokens,
    _verify_session_token,
    _ws_tokens,
    issue_session_token,
    issue_ws_token,
    redeem_ws_token,
)


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


class TestSessionTokens:
    def setup_method(self):
        _session_tokens.clear()

    def test_issue_returns_hex_string(self):
        token = issue_session_token("secret", "owner-1")
        assert isinstance(token, str)
        assert len(token) == 64  # sha256 hex digest

    def test_verify_valid_token(self):
        token = issue_session_token("secret", "owner-1")
        assert _verify_session_token(token) == "owner-1"

    def test_verify_unknown_token_returns_none(self):
        assert _verify_session_token("not-a-real-token") is None

    def test_verify_expired_token_returns_none(self):
        token = issue_session_token("secret", "owner-2")
        # Backdate issued_at beyond the 8h TTL
        user_id, _ = _session_tokens[token]
        _session_tokens[token] = (user_id, time.time() - 29000)
        assert _verify_session_token(token) is None
        # Token should be pruned from store after expiry
        assert token not in _session_tokens

    def test_different_keys_produce_different_tokens(self):
        t1 = issue_session_token("secret-a", "owner-1")
        t2 = issue_session_token("secret-b", "owner-1")
        assert t1 != t2

    def test_different_owners_produce_different_tokens(self):
        t1 = issue_session_token("secret", "owner-1")
        t2 = issue_session_token("secret", "owner-2")
        assert t1 != t2

    def test_verify_after_clear_returns_none(self):
        token = issue_session_token("secret", "owner-3")
        _session_tokens.clear()
        assert _verify_session_token(token) is None
