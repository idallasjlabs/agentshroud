# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Behavior tests for KeyRotationManager internals and guard branches.

The existing test_key_rotation.py covers the happy-path workflow and health
scoring. These target the subprocess-backed op-CLI helpers (read/store),
the experimental generator, validator dispatch, and the rotate_credential guard
clauses (not-found / in-progress / max-attempts / not-due). subprocess is mocked
so no real `op` CLI or network is invoked; no sleeps.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from gateway.security.key_rotation import (
    CredentialInfo,
    CredentialValidator,
    KeyRotationManager,
    RotationStatus,
)
from gateway.security.key_rotation_config import KeyRotationConfig


@pytest.fixture
def manager():
    return KeyRotationManager(KeyRotationConfig())


def _old_cred(cred_id="c1"):
    return CredentialInfo(
        id=cred_id,
        credential_type="api_key",
        op_reference="op://Vault/item/api_key",
        created_at=datetime.now(timezone.utc) - timedelta(days=200),
    )


class TestReadFrom1Password:
    @pytest.mark.asyncio
    async def test_read_success_strips_whitespace(self, manager):
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.return_value = MagicMock(returncode=0, stdout="secret-value\n", stderr="")
            value = await manager._read_credential_from_1password("op://V/i/f")
        assert value == "secret-value"

    @pytest.mark.asyncio
    async def test_read_nonzero_returncode_yields_none(self, manager):
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.return_value = MagicMock(returncode=1, stdout="", stderr="not found")
            value = await manager._read_credential_from_1password("op://V/i/f")
        assert value is None

    @pytest.mark.asyncio
    async def test_read_timeout_yields_none(self, manager):
        import subprocess

        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.side_effect = subprocess.TimeoutExpired(cmd="op", timeout=30)
            value = await manager._read_credential_from_1password("op://V/i/f")
        assert value is None

    @pytest.mark.asyncio
    async def test_read_generic_exception_yields_none(self, manager):
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.side_effect = OSError("op not installed")
            value = await manager._read_credential_from_1password("op://V/i/f")
        assert value is None


class TestStoreIn1Password:
    @pytest.mark.asyncio
    async def test_store_success(self, manager):
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.return_value = MagicMock(returncode=0, stderr="")
            ok = await manager._store_credential_in_1password("op://Vault/item/field", "val")
        assert ok is True

    @pytest.mark.asyncio
    async def test_store_rejects_malformed_reference(self, manager):
        # Fewer than 3 path components → invalid op:// reference → False, no subprocess.
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            ok = await manager._store_credential_in_1password("op://only-vault", "val")
            run.assert_not_called()
        assert ok is False

    @pytest.mark.asyncio
    async def test_store_nonzero_returncode_is_false(self, manager):
        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.return_value = MagicMock(returncode=2, stderr="permission denied")
            ok = await manager._store_credential_in_1password("op://Vault/item/field", "val")
        assert ok is False

    @pytest.mark.asyncio
    async def test_store_timeout_is_false(self, manager):
        import subprocess

        with patch("gateway.security.key_rotation.subprocess.run") as run:
            run.side_effect = subprocess.TimeoutExpired(cmd="op", timeout=30)
            ok = await manager._store_credential_in_1password("op://Vault/item/field", "val")
        assert ok is False


class TestGenerateAndValidate:
    @pytest.mark.asyncio
    async def test_generate_returns_typed_token(self, manager):
        value = await manager._generate_new_credential("api_key", {})
        assert value.startswith("agentshroud-api_key-")

    @pytest.mark.asyncio
    async def test_validate_without_registered_validator_passes(self, manager):
        ok, msg = await manager._validate_credential("api_key", "op://V/i/f", {})
        assert ok is True
        assert "No validator" in msg

    @pytest.mark.asyncio
    async def test_validate_with_validator_that_raises_fails_closed(self, manager):
        class Boom(CredentialValidator):
            async def validate(self, op_reference, metadata):
                raise RuntimeError("network down")

        manager.register_validator("api_key", Boom())
        ok, msg = await manager._validate_credential("api_key", "op://V/i/f", {})
        assert ok is False
        assert "exception" in msg.lower()


class TestRotateGuardBranches:
    @pytest.mark.asyncio
    async def test_unknown_credential_returns_error(self, manager):
        result = await manager.rotate_credential("does-not-exist")
        assert result["success"] is False
        assert "not found" in result["error"]

    @pytest.mark.asyncio
    async def test_not_due_without_force_is_rejected(self, manager):
        fresh = CredentialInfo(
            id="fresh",
            credential_type="api_key",
            op_reference="op://V/i/f",
            created_at=datetime.now(timezone.utc),
        )
        manager._credentials["fresh"] = fresh
        result = await manager.rotate_credential("fresh")
        assert result["success"] is False
        assert "does not need rotation" in result["error"]

    @pytest.mark.asyncio
    async def test_in_progress_is_rejected(self, manager):
        cred = _old_cred("busy")
        cred.status = RotationStatus.IN_PROGRESS
        manager._credentials["busy"] = cred
        result = await manager.rotate_credential("busy")
        assert result["success"] is False
        assert "already in progress" in result["error"]

    @pytest.mark.asyncio
    async def test_max_attempts_exceeded_is_rejected(self, manager):
        cred = _old_cred("maxed")
        policy = manager.config.get_policy("api_key")
        cred.failed_attempts = policy.max_rotation_attempts
        manager._credentials["maxed"] = cred
        result = await manager.rotate_credential("maxed")
        assert result["success"] is False
        assert "Max rotation attempts" in result["error"]

    @pytest.mark.asyncio
    async def test_store_failure_marks_failed(self, manager):
        cred = _old_cred("storefail")
        manager._credentials["storefail"] = cred
        with patch.object(manager, "_generate_new_credential", return_value="new"):
            with patch.object(manager, "_store_credential_in_1password", return_value=False):
                result = await manager.rotate_credential("storefail")
        assert result["success"] is False
        assert cred.status == RotationStatus.FAILED
        assert cred.failed_attempts == 1


class TestStatusHelpers:
    def test_get_credential_status_none_for_unknown(self, manager):
        assert manager.get_credential_status("nope") is None

    def test_get_all_credentials_status_lists_registered(self, manager):
        manager._credentials["a"] = _old_cred("a")
        manager._credentials["b"] = _old_cred("b")
        statuses = manager.get_all_credentials_status()
        ids = {s["id"] for s in statuses}
        assert ids == {"a", "b"}

    def test_health_score_empty_is_perfect(self, manager):
        health = manager.get_health_score()
        assert health["score"] == 100.0
        assert health["status"] == "healthy"


class TestEmergencyAndRetire:
    @pytest.mark.asyncio
    async def test_emergency_disabled_trigger_rejected(self, manager):
        cred = _old_cred("em")
        manager._credentials["em"] = cred
        # Force the config to report this trigger as disabled.
        with patch.object(manager.config, "is_emergency_trigger_enabled", return_value=False):
            result = await manager.emergency_rotate_credential("em", "unknown_trigger")
        assert result["success"] is False
        assert "not enabled" in result["error"]

    @pytest.mark.asyncio
    async def test_retire_clears_old_reference_when_grace_expired(self, manager):
        cred = _old_cred("ret")
        cred.old_op_reference = "op://V/i/old"
        # Grace period already in the past → no sleep, immediate retire.
        cred.grace_period_end = datetime.now(timezone.utc) - timedelta(seconds=1)
        manager._credentials["ret"] = cred
        await manager._retire_old_credential_after_grace_period("ret")
        assert cred.old_op_reference is None
        assert cred.grace_period_end is None

    @pytest.mark.asyncio
    async def test_retire_noop_when_no_grace_period(self, manager):
        cred = _old_cred("nog")
        cred.grace_period_end = None
        manager._credentials["nog"] = cred
        # Must return without error and leave state untouched.
        await manager._retire_old_credential_after_grace_period("nog")
        assert cred.grace_period_end is None


class TestCheckAndRotateDisabled:
    @pytest.mark.asyncio
    async def test_scheduled_rotation_disabled_short_circuits(self, manager):
        manager.config.enable_scheduled_rotation = False
        result = await manager.check_and_rotate_due_credentials()
        assert "disabled" in result["message"].lower()
