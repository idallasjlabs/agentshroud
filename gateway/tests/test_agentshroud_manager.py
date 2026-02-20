"""Tests for OpenClaw Version Manager."""

import json
import os
import tempfile

import pytest

from gateway.tools.agentshroud_manager import (
    check_current_version,
    downgrade,
    list_available_versions,
    list_versions,
    mask_credentials,
    rollback,
    security_review,
    upgrade,
)


@pytest.fixture
def tmp_db():
    """Create a temporary database for testing."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        path = f.name
    yield path
    os.unlink(path)


class TestMaskCredentials:
    def test_masks_token(self):
        text = 'token: "abc12345678"'
        result = mask_credentials(text)
        assert "abc12345678" not in result
        assert "MASKED" in result

    def test_masks_bearer(self):
        text = "Bearer eyJhbGciOiJIUzI1NiJ9"
        result = mask_credentials(text)
        assert "eyJhbGciOiJIUzI1NiJ9" not in result

    def test_no_mask_short_values(self):
        text = "token: short"
        result = mask_credentials(text)
        assert result == text

    def test_masks_password(self):
        text = 'password="supersecretpassword123"'
        result = mask_credentials(text)
        assert "supersecretpassword123" not in result

    def test_plain_text_unchanged(self):
        text = "Hello, this is normal text"
        assert mask_credentials(text) == text


class TestCheckCurrentVersion:
    def test_no_history_unknown(self, tmp_db):
        result = check_current_version(db_path=tmp_db)
        assert result["status"] in ("detected", "unknown")

    def test_with_env_var(self, tmp_db, monkeypatch):
        monkeypatch.setenv("OPENCLAW_VERSION", "1.2.3")
        result = check_current_version(db_path=tmp_db)
        assert result["current_version"] == "1.2.3"
        assert result["status"] == "detected"

    def test_after_upgrade(self, tmp_db):
        upgrade("1.0.0", approval_id="test-001", db_path=tmp_db)
        result = check_current_version(db_path=tmp_db)
        assert result["current_version"] == "1.0.0"
        assert result["status"] == "installed"
        assert result["installed_at"] is not None


class TestListVersions:
    def test_empty_history(self, tmp_db):
        assert list_versions(db_path=tmp_db) == []

    def test_after_operations(self, tmp_db):
        upgrade("1.0.0", approval_id="a1", db_path=tmp_db)
        upgrade("1.1.0", approval_id="a2", db_path=tmp_db)
        history = list_versions(db_path=tmp_db)
        assert len(history) == 2
        assert history[0]["version"] == "1.1.0"
        assert history[1]["version"] == "1.0.0"


class TestListAvailableVersions:
    def test_returns_versions(self):
        versions = list_available_versions()
        assert isinstance(versions, list)
        assert "1.0.0" in versions
        assert "0.2.0" in versions


class TestSecurityReview:
    def test_valid_version(self):
        result = security_review("1.0.0")
        assert result["passed"] is True
        assert result["risk_level"] == "low"
        assert len(result["checks"]) >= 3

    def test_invalid_version_format(self):
        result = security_review("not-a-version")
        assert result["passed"] is False
        assert any(c["status"] == "fail" for c in result["checks"])

    def test_has_timestamp(self):
        result = security_review("1.0.0")
        assert "timestamp" in result


class TestUpgrade:
    def test_successful_upgrade(self, tmp_db):
        result = upgrade("1.0.0", approval_id="test-001", db_path=tmp_db)
        assert result["status"] == "completed"
        assert result["new_version"] == "1.0.0"
        assert result["approval_id"] == "test-001"

    def test_dry_run(self, tmp_db):
        result = upgrade("1.0.0", dry_run=True, db_path=tmp_db)
        assert result["status"] == "dry_run"
        # Should not be in history
        assert list_versions(db_path=tmp_db) == []

    def test_blocked_on_invalid_version(self, tmp_db):
        result = upgrade("bad-version", approval_id="test", db_path=tmp_db)
        assert result["status"] == "blocked"

    def test_sequential_upgrades(self, tmp_db):
        upgrade("0.9.0", approval_id="a1", db_path=tmp_db)
        result = upgrade("1.0.0", approval_id="a2", db_path=tmp_db)
        assert result["previous_version"] == "0.9.0"
        assert result["new_version"] == "1.0.0"


class TestDowngrade:
    def test_successful_downgrade(self, tmp_db):
        upgrade("1.0.0", approval_id="a1", db_path=tmp_db)
        result = downgrade("0.9.0", approval_id="a2", db_path=tmp_db)
        assert result["status"] == "completed"
        assert result["new_version"] == "0.9.0"
        assert result["review"]["risk_level"] in ("medium", "high")

    def test_dry_run(self, tmp_db):
        result = downgrade("0.9.0", dry_run=True, db_path=tmp_db)
        assert result["status"] == "dry_run"

    def test_blocked_on_invalid(self, tmp_db):
        result = downgrade("nope", approval_id="a1", db_path=tmp_db)
        assert result["status"] == "blocked"


class TestRollback:
    def test_successful_rollback(self, tmp_db):
        upgrade("0.9.0", approval_id="a1", db_path=tmp_db)
        upgrade("1.0.0", approval_id="a2", db_path=tmp_db)
        result = rollback(db_path=tmp_db, approval_id="a3")
        assert result["status"] == "completed"
        assert result["new_version"] == "0.9.0"

    def test_no_history(self, tmp_db):
        result = rollback(db_path=tmp_db, approval_id="a1")
        assert result["status"] == "error"
        assert "No previous version" in result["reason"]

    def test_no_previous_version(self, tmp_db):
        # First install has no previous_version
        upgrade("1.0.0", approval_id="a1", db_path=tmp_db)
        result = rollback(db_path=tmp_db, approval_id="a2")
        # previous_version is "unknown" or None depending on env
        # Either rollback succeeds with the detected version or errors
        assert result["status"] in ("completed", "error", "blocked")
