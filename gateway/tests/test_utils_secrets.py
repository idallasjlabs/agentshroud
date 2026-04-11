# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Unit tests for gateway.utils.secrets — secret-file reading and normalization.

Regression suite for the garbled multi-line secret bug: pre-017e7bd
setup-secrets.sh captured TUI output (label line + asterisk preview + real
token on the last line) via $(...) and wrote the whole blob to the secret
backend. These tests assert that read_secret() and _normalize_secret() always
return only the last non-empty line.
"""

from __future__ import annotations

from gateway.utils import secrets as secrets_mod
from gateway.utils.secrets import _normalize_secret, read_secret

# Real-world garbled blob captured from the marvin-dev gateway logs 2026-04-10.
_GARBLED_BLOB = (
    "\n  \u2192 Telegram bot token (marvin dev): "
    "**********************************************"
    "\n8736289266:AAGVzcmqiSaTSyPz5B8lJCcxkmZPg9jTe28"
)
_REAL_TOKEN = "8736289266:AAGVzcmqiSaTSyPz5B8lJCcxkmZPg9jTe28"


# ── _normalize_secret ─────────────────────────────────────────────────────────


class TestNormalizeSecret:
    def test_clean_single_line(self):
        """Normal single-line value is returned unchanged (modulo outer whitespace)."""
        assert _normalize_secret("xoxb-test-token-abc") == "xoxb-test-token-abc"

    def test_trailing_newline_stripped(self):
        """Single-line value with trailing newline is stripped."""
        assert _normalize_secret("mytoken\n") == "mytoken"

    def test_crlf_stripped(self):
        """CRLF line endings are handled correctly."""
        assert _normalize_secret("mytoken\r\n") == "mytoken"

    def test_garbled_blob_returns_last_line(self):
        """The exact garbled blob from the marvin-dev bug returns only the real token."""
        assert _normalize_secret(_GARBLED_BLOB) == _REAL_TOKEN

    def test_multiline_interior_blank_lines(self):
        """When the value has interior blank lines, the last non-empty line is returned."""
        value = "line1\n\n\nline2\n\n"
        assert _normalize_secret(value) == "line2"

    def test_all_whitespace_returns_empty(self):
        """An all-whitespace / blank file returns an empty string."""
        assert _normalize_secret("   \n\t\n  \n") == ""

    def test_empty_string_returns_empty(self):
        assert _normalize_secret("") == ""

    def test_label_lines_stripped(self):
        """Label + masked preview lines before the real token are discarded."""
        raw = "  \u2192 Slack bot token: ****\nxoxb-real-bot-token-abc123"
        assert _normalize_secret(raw) == "xoxb-real-bot-token-abc123"


# ── read_secret ───────────────────────────────────────────────────────────────


class TestReadSecret:
    def test_missing_file_returns_default(self, tmp_path, monkeypatch):
        monkeypatch.setattr(secrets_mod, "_SECRETS_DIR", tmp_path)
        assert read_secret("nonexistent") == ""
        assert read_secret("nonexistent", default="fallback") == "fallback"

    def test_clean_token_returned(self, tmp_path, monkeypatch):
        monkeypatch.setattr(secrets_mod, "_SECRETS_DIR", tmp_path)
        (tmp_path / "telegram_bot_token").write_text(
            "9876543210:BBTokenBBTokenBBTokenBBTokenBBToken1\n"
        )
        assert (
            read_secret("telegram_bot_token") == "9876543210:BBTokenBBTokenBBTokenBBTokenBBToken1"
        )

    def test_garbled_blob_returns_real_token(self, tmp_path, monkeypatch):
        """The exact marvin-dev garbled blob on disk yields only the real token."""
        monkeypatch.setattr(secrets_mod, "_SECRETS_DIR", tmp_path)
        (tmp_path / "telegram_bot_token").write_text(_GARBLED_BLOB)
        assert read_secret("telegram_bot_token") == _REAL_TOKEN

    def test_crlf_secret_file(self, tmp_path, monkeypatch):
        monkeypatch.setattr(secrets_mod, "_SECRETS_DIR", tmp_path)
        (tmp_path / "api_key").write_bytes(b"sk-someapikey123\r\n")
        assert read_secret("api_key") == "sk-someapikey123"

    def test_all_whitespace_file_returns_default(self, tmp_path, monkeypatch):
        monkeypatch.setattr(secrets_mod, "_SECRETS_DIR", tmp_path)
        (tmp_path / "empty_secret").write_text("   \n\t  \n")
        assert read_secret("empty_secret") == ""
        assert read_secret("empty_secret", default="fb") == "fb"
