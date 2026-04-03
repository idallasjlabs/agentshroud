# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for automated key rotation (R-22)"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.security.key_rotation import (
    CredentialInfo,
    CredentialValidator,
    KeyRotationManager,
    RotationStatus,
)
from gateway.security.key_rotation_config import (
    CredentialRotationPolicy,
    KeyRotationConfig,
)


class MockValidator(CredentialValidator):
    """Mock validator for testing."""

    def __init__(self, should_pass: bool = True, delay: float = 0):
        self.should_pass = should_pass
        self.delay = delay
        self.calls = []

    async def validate(self, op_reference: str, metadata: dict) -> tuple[bool, str]:
        """Mock validation that can be controlled."""
        self.calls.append((op_reference, metadata))
        if self.delay:
            await asyncio.sleep(self.delay)

        if self.should_pass:
            return True, "Validation passed"
        else:
            return False, "Mock validation failure"


class TestCredentialRotationPolicy:
    """Test credential rotation policy configuration."""

    def test_default_policy_values(self):
        """Test default policy has reasonable values."""
        policy = CredentialRotationPolicy(max_age_days=90)

        assert policy.max_age_days == 90
        assert policy.warn_threshold_percent == 80.0
        assert policy.grace_period_hours == 24
        assert policy.enable_emergency_rotation is True
        assert policy.validation_timeout_seconds == 30


class TestKeyRotationConfig:
    """Test key rotation configuration."""

    def test_default_config_has_common_policies(self):
        """Test default config includes policies for common credential types."""
        config = KeyRotationConfig()

        assert "api_key" in config.policies
        assert "access_token" in config.policies
        assert "service_account_key" in config.policies
        assert "database_password" in config.policies

    def test_get_policy_returns_default_for_unknown_type(self):
        """Test get_policy falls back to api_key for unknown types."""
        config = KeyRotationConfig()

        policy = config.get_policy("unknown_type")
        assert policy == config.policies["api_key"]

    def test_add_custom_policy(self):
        """Test adding custom policy for new credential type."""
        config = KeyRotationConfig()
        custom_policy = CredentialRotationPolicy(max_age_days=30)

        config.add_custom_policy("custom_key", custom_policy)

        assert config.get_policy("custom_key") == custom_policy

    def test_get_op_reference_builds_correctly(self):
        """Test op:// reference building."""
        config = KeyRotationConfig()

        ref = config.get_op_reference("test_item", "password")
        assert ref == "op://Agent Shroud Bot Credentials/test_item/password"


class TestCredentialInfo:
    """Test credential information tracking."""

    def test_age_calculation(self):
        """Test credential age calculation."""
        now = datetime.now(timezone.utc)
        two_days_ago = now - timedelta(days=2)

        cred = CredentialInfo(
            id="test", credential_type="api_key", op_reference="op://test", created_at=two_days_ago
        )

        assert abs(cred.age_days - 2.0) < 0.1

    def test_should_warn(self):
        """Test warning threshold calculation."""
        now = datetime.now(timezone.utc)
        old_time = now - timedelta(days=80)  # 80 days old

        cred = CredentialInfo(
            id="test", credential_type="api_key", op_reference="op://test", created_at=old_time
        )

        policy = CredentialRotationPolicy(max_age_days=100, warn_threshold_percent=75.0)

        assert cred.should_warn(policy) is True  # 80 days > 75% of 100 days

    def test_should_rotate(self):
        """Test rotation requirement calculation."""
        now = datetime.now(timezone.utc)
        old_time = now - timedelta(days=100)  # 100 days old

        cred = CredentialInfo(
            id="test", credential_type="api_key", op_reference="op://test", created_at=old_time
        )

        policy = CredentialRotationPolicy(max_age_days=90)

        assert cred.should_rotate(policy) is True

    def test_grace_period_tracking(self):
        """Test grace period status tracking."""
        cred = CredentialInfo(
            id="test",
            credential_type="api_key",
            op_reference="op://test",
            created_at=datetime.now(timezone.utc),
        )

        # Not in grace period initially
        assert cred.is_in_grace_period is False

        # Set grace period
        cred.grace_period_end = datetime.now(timezone.utc) + timedelta(hours=24)
        assert cred.is_in_grace_period is True

        # Grace period expired
        cred.grace_period_end = datetime.now(timezone.utc) - timedelta(hours=1)
        assert cred.is_in_grace_period is False


class TestKeyRotationManager:
    """Test key rotation manager functionality."""

    @pytest.fixture
    def manager(self):
        """Create a manager with test configuration."""
        config = KeyRotationConfig()
        return KeyRotationManager(config)

    @pytest.fixture
    def sample_credential(self):
        """Create a sample credential for testing."""
        return CredentialInfo(
            id="test_api_key",
            credential_type="api_key",
            op_reference="op://Agent Shroud Bot Credentials/test/api_key",
            created_at=datetime.now(timezone.utc)
            - timedelta(days=95),  # Old enough to need rotation
        )

    def test_register_credential(self, manager):
        """Test credential registration."""
        manager.register_credential(
            "test_cred", "api_key", "op://test", metadata={"service": "test"}
        )

        assert "test_cred" in manager._credentials
        cred = manager._credentials["test_cred"]
        assert cred.credential_type == "api_key"
        assert cred.metadata["service"] == "test"

    def test_register_validator(self, manager):
        """Test validator registration."""
        validator = MockValidator()
        manager.register_validator("api_key", validator)

        assert manager._validators["api_key"] == validator

    def test_get_credential_status(self, manager, sample_credential):
        """Test credential status reporting."""
        manager._credentials["test_cred"] = sample_credential

        status = manager.get_credential_status("test_cred")

        assert status is not None
        assert status["id"] == "test_api_key"
        assert status["type"] == "api_key"
        assert status["should_rotate"] is True
        assert status["age_days"] > 90

    def test_get_health_score_all_healthy(self, manager):
        """Test health score calculation with all healthy credentials."""
        # Add a healthy credential (new)
        manager._credentials["healthy"] = CredentialInfo(
            id="healthy",
            credential_type="api_key",
            op_reference="op://test",
            created_at=datetime.now(timezone.utc),
        )

        health = manager.get_health_score()

        assert health["score"] == 100.0
        assert health["status"] == "healthy"
        assert health["healthy"] == 1

    def test_get_health_score_mixed_states(self, manager):
        """Test health score with mixed credential states."""
        now = datetime.now(timezone.utc)

        # Healthy credential
        manager._credentials["healthy"] = CredentialInfo(
            id="healthy", credential_type="api_key", op_reference="op://test", created_at=now
        )

        # Warning credential (75 days old, warn at 80% of 90 = 72 days)
        manager._credentials["warning"] = CredentialInfo(
            id="warning",
            credential_type="api_key",
            op_reference="op://test",
            created_at=now - timedelta(days=75),
        )

        # Overdue credential
        manager._credentials["overdue"] = CredentialInfo(
            id="overdue",
            credential_type="api_key",
            op_reference="op://test",
            created_at=now - timedelta(days=100),
        )

        # Failed credential
        manager._credentials["failed"] = CredentialInfo(
            id="failed",
            credential_type="api_key",
            op_reference="op://test",
            created_at=now,
            status=RotationStatus.FAILED,
        )

        health = manager.get_health_score()

        assert health["total_credentials"] == 4
        assert health["healthy"] == 1
        assert health["warnings"] == 1
        assert health["overdue"] == 1
        assert health["failed"] == 1
        assert health["score"] == 50.0  # (1*100 + 1*75 + 1*25 + 1*0) / 4


class TestKeyRotationWorkflow:
    """Test the complete rotation workflow."""

    @pytest.fixture
    def setup_manager_with_credential(self):
        """Set up manager with a credential that needs rotation."""
        manager = KeyRotationManager(KeyRotationConfig())
        validator = MockValidator(should_pass=True)
        manager.register_validator("api_key", validator)

        # Add an old credential that needs rotation
        old_cred = CredentialInfo(
            id="test_key",
            credential_type="api_key",
            op_reference="op://Agent Shroud Bot Credentials/test/api_key",
            created_at=datetime.now(timezone.utc) - timedelta(days=100),
        )
        manager._credentials["test_key"] = old_cred

        return manager, validator

    @pytest.mark.asyncio
    async def test_successful_rotation_workflow(self, setup_manager_with_credential):
        """Test complete successful rotation workflow."""
        manager, validator = setup_manager_with_credential

        with patch.object(manager, "_generate_new_credential", return_value="new_key_value"):
            with patch.object(manager, "_store_credential_in_1password", return_value=True):
                result = await manager.rotate_credential("test_key")

        assert result["success"] is True
        assert result["rotation_count"] == 1

        # Verify credential state
        cred = manager._credentials["test_key"]
        assert cred.status == RotationStatus.ACTIVE
        assert cred.rotation_count == 1
        assert cred.last_rotated_at is not None
        assert cred.is_in_grace_period is True
        assert cred.failed_attempts == 0

        # Verify validator was called
        assert len(validator.calls) == 1

    @pytest.mark.asyncio
    async def test_rotation_with_validation_failure(self, setup_manager_with_credential):
        """Test rotation workflow with validation failure and rollback."""
        manager, _ = setup_manager_with_credential

        # Set up validator to fail
        failing_validator = MockValidator(should_pass=False)
        manager.register_validator("api_key", failing_validator)

        original_op_ref = manager._credentials["test_key"].op_reference

        with patch.object(manager, "_generate_new_credential", return_value="new_key_value"):
            with patch.object(manager, "_store_credential_in_1password", return_value=True):
                result = await manager.rotate_credential("test_key")

        assert result["success"] is False
        assert "validation failed" in result["error"].lower()

        # Verify credential was not rotated
        cred = manager._credentials["test_key"]
        assert cred.status == RotationStatus.FAILED
        assert cred.failed_attempts == 1
        assert cred.rotation_count == 0

    @pytest.mark.asyncio
    #     async def test_rotation_prevents_concurrent_rotations(self, setup_manager_with_credential):
    #         """Test that concurrent rotations are prevented."""
    #         manager, validator = setup_manager_with_credential
    #
    #         # Make validation slow to simulate concurrent access
    #         slow_validator = MockValidator(should_pass=True, delay=0.1)
    #         manager.register_validator("api_key", slow_validator)
    #
    #         with patch.object(manager, '_generate_new_credential', return_value="new_key"):
    #             with patch.object(manager, '_store_credential_in_1password', return_value=True):
    #                 # Start two concurrent rotations
    #                 task1 = asyncio.create_task(manager.rotate_credential("test_key"))
    #                 await asyncio.sleep(0.05)  # Let first rotation start
    #                 task2 = asyncio.create_task(manager.rotate_credential("test_key"))
    #
    #                 result1, result2 = await asyncio.gather(task1, task2)
    #
    #         # One should succeed, one should fail due to concurrent access
    #         successes = sum(1 for r in [result1, result2] if r["success"])
    #         failures = sum(1 for r in [result1, result2] if not r["success"])
    #
    #         assert successes == 1
    #         assert failures == 1

    @pytest.mark.asyncio
    async def test_emergency_rotation(self, setup_manager_with_credential):
        """Test emergency rotation workflow."""
        manager, validator = setup_manager_with_credential

        with patch.object(manager, "_generate_new_credential", return_value="emergency_key"):
            with patch.object(manager, "_store_credential_in_1password", return_value=True):
                result = await manager.emergency_rotate_credential(
                    "test_key", "suspected_compromise"
                )

        assert result["success"] is True

        cred = manager._credentials["test_key"]
        assert cred.status == RotationStatus.ACTIVE
        assert cred.rotation_count == 1

    @pytest.mark.asyncio
    async def test_grace_period_cleanup(self, setup_manager_with_credential):
        """Test grace period and old credential cleanup."""
        manager, validator = setup_manager_with_credential

        # Perform rotation
        with patch.object(manager, "_generate_new_credential", return_value="new_key"):
            with patch.object(manager, "_store_credential_in_1password", return_value=True):
                await manager.rotate_credential("test_key")

        cred = manager._credentials["test_key"]

        # Verify grace period is active
        assert cred.is_in_grace_period is True
        assert cred.old_op_reference is not None

        # Simulate grace period expiry
        cred.grace_period_end = datetime.now(timezone.utc) - timedelta(seconds=1)

        # Clean up
        result = manager.cleanup_retired_credentials()

        assert result["cleaned"] == 1
        assert "test_key" in result["credential_ids"]
        assert cred.old_op_reference is None
        assert cred.grace_period_end is None

    @pytest.mark.asyncio
    async def test_check_and_rotate_due_credentials(self):
        """Test bulk rotation check and execution."""
        manager = KeyRotationManager(KeyRotationConfig())
        validator = MockValidator(should_pass=True)
        manager.register_validator("api_key", validator)

        now = datetime.now(timezone.utc)

        # Add credentials in different states
        manager._credentials["old"] = CredentialInfo(
            id="old",
            credential_type="api_key",
            op_reference="op://test/old",
            created_at=now - timedelta(days=100),  # Needs rotation
        )

        manager._credentials["warning"] = CredentialInfo(
            id="warning",
            credential_type="api_key",
            op_reference="op://test/warning",
            created_at=now - timedelta(days=75),  # Warning threshold
        )

        manager._credentials["fresh"] = CredentialInfo(
            id="fresh",
            credential_type="api_key",
            op_reference="op://test/fresh",
            created_at=now,  # Fresh
        )

        with patch.object(manager, "_generate_new_credential", return_value="rotated_key"):
            with patch.object(manager, "_store_credential_in_1password", return_value=True):
                result = await manager.check_and_rotate_due_credentials()

        assert result["checked"] == 3
        assert result["rotated"] == 1  # Only the old one
        assert result["warnings"] == 1  # The warning one
        assert result["failures"] == 0


# ============================================================
# API Endpoint Tests
# ============================================================


@pytest.mark.asyncio
async def test_credentials_status_endpoint():
    """Test the /manage/credentials/status endpoint."""
    # Create test app
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from gateway.web.api import require_auth
    from gateway.web.management import router

    app = FastAPI()

    # Mock auth
    app.dependency_overrides[require_auth] = lambda: True
    app.include_router(router)

    client = TestClient(app)

    response = client.get("/manage/credentials/status")
    assert response.status_code == 200

    data = response.json()
    assert "credentials" in data
    assert "health" in data
    assert isinstance(data["credentials"], list)
    assert isinstance(data["health"], dict)


@pytest.mark.asyncio
async def test_credentials_health_endpoint():
    """Test the /manage/credentials/health endpoint."""
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from gateway.web.api import require_auth
    from gateway.web.management import router

    app = FastAPI()
    app.dependency_overrides[require_auth] = lambda: True
    app.include_router(router)

    client = TestClient(app)

    response = client.get("/manage/credentials/health")
    assert response.status_code == 200

    data = response.json()
    assert "score" in data
    assert "status" in data
    assert isinstance(data["score"], (int, float))
    assert data["status"] in ["healthy", "warning", "degraded", "critical"]


@pytest.mark.asyncio
async def test_rotate_credential_endpoint():
    """Test the POST /manage/credentials/rotate/{credential_id} endpoint."""
    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    from gateway.web.api import require_auth
    from gateway.web.management import router

    app = FastAPI()
    app.dependency_overrides[require_auth] = lambda: True
    app.include_router(router)

    client = TestClient(app)

    # Test with non-existent credential
    response = client.post("/manage/credentials/rotate/nonexistent")
    assert response.status_code == 404
