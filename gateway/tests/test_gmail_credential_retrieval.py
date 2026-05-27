# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for _get_gmail_app_password in gateway/ingest_api/routes/forward.py.

Covers the secrets-fallback path that was incorrectly short-circuited when
OP_SESSION env var is absent.
"""

import os
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from gateway.ingest_api.routes.forward import _get_gmail_app_password


# ──────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────

def _completed(returncode: int, stdout: str = "", stderr: str = "") -> subprocess.CompletedProcess:
    r = MagicMock(spec=subprocess.CompletedProcess)
    r.returncode = returncode
    r.stdout = stdout
    r.stderr = stderr
    return r


# ──────────────────────────────────────────────
# Tests
# ──────────────────────────────────────────────

class TestGetGmailAppPasswordNoSession:
    """OP_SESSION absent — must fall back to mounted secrets."""

    def test_returns_none_when_no_session_and_no_secrets(self, tmp_path, monkeypatch):
        monkeypatch.delenv("OP_SESSION", raising=False)
        # secrets dir is empty (OSError on read)
        monkeypatch.setattr(
            "gateway.ingest_api.routes.forward.Path",
            lambda p: Path(tmp_path / Path(p).name),
        )
        assert _get_gmail_app_password() is None

    def test_falls_back_to_secrets_when_op_session_absent(self, tmp_path, monkeypatch):
        """Core regression test: empty OP_SESSION must NOT short-circuit the secrets path."""
        monkeypatch.delenv("OP_SESSION", raising=False)

        # Write fake secret files
        (tmp_path / "1password_bot_email").write_text("bot@example.com")
        (tmp_path / "1password_bot_master_password").write_text("masterpass")
        (tmp_path / "1password_bot_secret_key").write_text("A3-FAKEKEY-000")

        def fake_path(p: str) -> Path:
            name = Path(p).name
            if name in ("1password_bot_email", "1password_bot_master_password", "1password_bot_secret_key"):
                return tmp_path / name
            return Path(p)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.Path", fake_path)

        # op account add succeeds and returns a session token
        # op read with that token succeeds
        sessions = {"token": "FAKE_SESSION_TOKEN"}

        def fake_run(cmd, **kwargs):
            if "account" in cmd and "add" in cmd:
                return _completed(0, stdout=sessions["token"])
            if "read" in cmd:
                if "--session" in cmd:
                    idx = cmd.index("--session")
                    sess = cmd[idx + 1] if idx + 1 < len(cmd) else ""
                    if sess == sessions["token"]:
                        return _completed(0, stdout="my-gmail-app-password")
                return _completed(1)
            return _completed(1)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.subprocess.run", fake_run)

        result = _get_gmail_app_password()
        assert result == "my-gmail-app-password"

    def test_falls_back_to_op_signin_when_account_add_fails(self, tmp_path, monkeypatch):
        monkeypatch.delenv("OP_SESSION", raising=False)

        (tmp_path / "1password_bot_email").write_text("bot@example.com")
        (tmp_path / "1password_bot_master_password").write_text("masterpass")
        (tmp_path / "1password_bot_secret_key").write_text("A3-FAKEKEY-000")

        def fake_path(p: str) -> Path:
            name = Path(p).name
            if name in ("1password_bot_email", "1password_bot_master_password", "1password_bot_secret_key"):
                return tmp_path / name
            return Path(p)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.Path", fake_path)

        def fake_run(cmd, **kwargs):
            if "account" in cmd and "add" in cmd:
                return _completed(1)  # account add fails
            if "signin" in cmd:
                return _completed(0, stdout="SIGNIN_TOKEN")
            if "read" in cmd:
                if "--session" in cmd:
                    idx = cmd.index("--session")
                    sess = cmd[idx + 1] if idx + 1 < len(cmd) else ""
                    if sess == "SIGNIN_TOKEN":
                        return _completed(0, stdout="my-gmail-app-password")
                return _completed(1)
            return _completed(1)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.subprocess.run", fake_run)

        result = _get_gmail_app_password()
        assert result == "my-gmail-app-password"


class TestGetGmailAppPasswordWithSession:
    """OP_SESSION is set — primary op read path."""

    def test_uses_existing_session_when_op_read_succeeds(self, monkeypatch):
        monkeypatch.setenv("OP_SESSION", "VALID_SESSION")

        def fake_run(cmd, **kwargs):
            if "read" in cmd:
                return _completed(0, stdout="gmail-password-from-session")
            return _completed(1)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.subprocess.run", fake_run)
        assert _get_gmail_app_password() == "gmail-password-from-session"

    def test_falls_back_to_secrets_when_op_read_fails(self, tmp_path, monkeypatch):
        monkeypatch.setenv("OP_SESSION", "STALE_SESSION")

        (tmp_path / "1password_bot_email").write_text("bot@example.com")
        (tmp_path / "1password_bot_master_password").write_text("masterpass")
        (tmp_path / "1password_bot_secret_key").write_text("A3-FAKEKEY-000")

        def fake_path(p: str) -> Path:
            name = Path(p).name
            if name in ("1password_bot_email", "1password_bot_master_password", "1password_bot_secret_key"):
                return tmp_path / name
            return Path(p)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.Path", fake_path)

        def fake_run(cmd, **kwargs):
            if "account" in cmd and "add" in cmd:
                return _completed(0, stdout="NEW_SESSION")
            if "read" in cmd:
                if "--session" in cmd:
                    idx = cmd.index("--session")
                    sess = cmd[idx + 1] if idx + 1 < len(cmd) else ""
                    if sess == "STALE_SESSION":
                        return _completed(1)  # stale session fails
                    if sess == "NEW_SESSION":
                        return _completed(0, stdout="refreshed-password")
                return _completed(1)
            return _completed(1)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.subprocess.run", fake_run)

        result = _get_gmail_app_password()
        assert result == "refreshed-password"

    def test_returns_none_when_all_paths_fail(self, tmp_path, monkeypatch):
        monkeypatch.setenv("OP_SESSION", "BAD_SESSION")

        (tmp_path / "1password_bot_email").write_text("bot@example.com")
        (tmp_path / "1password_bot_master_password").write_text("masterpass")
        (tmp_path / "1password_bot_secret_key").write_text("A3-FAKEKEY-000")

        def fake_path(p: str) -> Path:
            name = Path(p).name
            if name in ("1password_bot_email", "1password_bot_master_password", "1password_bot_secret_key"):
                return tmp_path / name
            return Path(p)

        monkeypatch.setattr("gateway.ingest_api.routes.forward.Path", fake_path)
        monkeypatch.setattr(
            "gateway.ingest_api.routes.forward.subprocess.run",
            lambda *a, **kw: _completed(1),
        )

        assert _get_gmail_app_password() is None
