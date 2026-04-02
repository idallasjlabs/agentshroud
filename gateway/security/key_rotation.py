# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Automated Key Rotation Manager — zero-downtime credential rollover.

Provides automated rotation of credentials with validation, graceful rollback,
and integration with 1Password via op-proxy for secure storage.
"""

import asyncio
import logging
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, Awaitable, Callable, Dict, List, Optional
from uuid import uuid4

from .key_rotation_config import CredentialRotationPolicy, KeyRotationConfig

logger = logging.getLogger("agentshroud.security.key_rotation")


class RotationStatus(Enum):
    """Status of a credential rotation."""

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    VALIDATING = "validating"
    ACTIVE = "active"
    FAILED = "failed"
    ROLLED_BACK = "rolled_back"
    RETIRED = "retired"


@dataclass
class CredentialInfo:
    """Information about a managed credential."""

    id: str
    """Unique identifier for this credential"""

    credential_type: str
    """Type of credential (api_key, access_token, etc.)"""

    op_reference: str
    """1Password op:// reference for the current active credential"""

    created_at: datetime
    """When this credential was first created"""

    last_rotated_at: Optional[datetime] = None
    """When this credential was last rotated"""

    rotation_count: int = 0
    """Number of times this credential has been rotated"""

    status: RotationStatus = RotationStatus.ACTIVE
    """Current rotation status"""

    # Grace period management
    old_op_reference: Optional[str] = None
    """op:// reference for the old credential during grace period"""

    grace_period_end: Optional[datetime] = None
    """When the grace period ends and old credential is retired"""

    # Failure tracking
    failed_attempts: int = 0
    """Number of consecutive failed rotation attempts"""

    last_failure_reason: Optional[str] = None
    """Reason for the last rotation failure"""

    # Metadata
    metadata: Dict[str, Any] = field(default_factory=dict)
    """Additional metadata for this credential"""

    @property
    def age_days(self) -> float:
        """Age of credential in days."""
        ref_time = self.last_rotated_at or self.created_at
        return (datetime.now(timezone.utc) - ref_time).total_seconds() / 86400

    @property
    def is_in_grace_period(self) -> bool:
        """Whether credential is currently in grace period."""
        return (
            self.grace_period_end is not None and datetime.now(timezone.utc) < self.grace_period_end
        )

    def should_warn(self, policy: CredentialRotationPolicy) -> bool:
        """Whether credential age warrants a warning."""
        threshold_days = policy.max_age_days * (policy.warn_threshold_percent / 100.0)
        return self.age_days >= threshold_days

    def should_rotate(self, policy: CredentialRotationPolicy) -> bool:
        """Whether credential needs rotation based on age."""
        return self.age_days >= policy.max_age_days


class CredentialValidator:
    """Base class for credential validators."""

    async def validate(self, op_reference: str, metadata: Dict[str, Any]) -> tuple[bool, str]:
        """Validate a credential.

        Returns:
            tuple: (is_valid, message)
        """
        raise NotImplementedError("Subclasses must implement validate()")


class KeyRotationManager:
    """Manages automated rotation of credentials with zero downtime."""

    def __init__(self, config: Optional[KeyRotationConfig] = None):
        """Initialize the key rotation manager."""
        self.config = config or KeyRotationConfig()
        self._credentials: Dict[str, CredentialInfo] = {}
        self._validators: Dict[str, CredentialValidator] = {}
        self._rotation_lock = asyncio.Lock()
        self._rotation_tasks: Dict[str, asyncio.Task] = {}

        logger.info("KeyRotationManager initialized")

    def register_credential(
        self,
        credential_id: str,
        credential_type: str,
        op_reference: str,
        created_at: Optional[datetime] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Register a credential for rotation management."""
        if credential_id in self._credentials:
            logger.warning(f"Credential {credential_id} already registered, updating")

        cred_info = CredentialInfo(
            id=credential_id,
            credential_type=credential_type,
            op_reference=op_reference,
            created_at=created_at or datetime.now(timezone.utc),
            metadata=metadata or {},
        )

        self._credentials[credential_id] = cred_info
        logger.info(f"Registered credential: {credential_id} (type: {credential_type})")

    def register_validator(self, credential_type: str, validator: CredentialValidator) -> None:
        """Register a validator for a credential type."""
        self._validators[credential_type] = validator
        logger.info(f"Registered validator for credential type: {credential_type}")

    def get_credential_status(self, credential_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed status for a credential."""
        cred = self._credentials.get(credential_id)
        if not cred:
            return None

        policy = self.config.get_policy(cred.credential_type)

        return {
            "id": cred.id,
            "type": cred.credential_type,
            "status": cred.status.value,
            "age_days": round(cred.age_days, 2),
            "max_age_days": policy.max_age_days,
            "should_warn": cred.should_warn(policy),
            "should_rotate": cred.should_rotate(policy),
            "rotation_count": cred.rotation_count,
            "last_rotated_at": cred.last_rotated_at.isoformat() if cred.last_rotated_at else None,
            "is_in_grace_period": cred.is_in_grace_period,
            "grace_period_end": (
                cred.grace_period_end.isoformat() if cred.grace_period_end else None
            ),
            "failed_attempts": cred.failed_attempts,
            "last_failure_reason": cred.last_failure_reason,
        }

    def get_all_credentials_status(self) -> List[Dict[str, Any]]:
        """Get status for all managed credentials."""
        return [
            status
            for cred_id in self._credentials
            if (status := self.get_credential_status(cred_id))
        ]

    def get_health_score(self) -> Dict[str, Any]:
        """Calculate overall credential health score."""
        if not self._credentials:
            return {"score": 100.0, "status": "healthy", "details": "No credentials managed"}

        total_creds = len(self._credentials)
        warnings = 0
        overdue = 0
        failed = 0

        for cred in self._credentials.values():
            policy = self.config.get_policy(cred.credential_type)

            if cred.status == RotationStatus.FAILED:
                failed += 1
            elif cred.should_rotate(policy):
                overdue += 1
            elif cred.should_warn(policy):
                warnings += 1

        # Calculate score: failed = 0 points, overdue = 25 points, warning = 75 points, healthy = 100 points
        score = (
            (total_creds - failed - overdue - warnings) * 100
            + warnings * 75
            + overdue * 25
            + failed * 0
        ) / total_creds

        if score >= 90:
            status = "healthy"
        elif score >= 70:
            status = "warning"
        elif score >= 40:
            status = "degraded"
        else:
            status = "critical"

        return {
            "score": round(score, 1),
            "status": status,
            "total_credentials": total_creds,
            "healthy": total_creds - failed - overdue - warnings,
            "warnings": warnings,
            "overdue": overdue,
            "failed": failed,
        }

    async def _read_credential_from_1password(self, op_reference: str) -> Optional[str]:
        """Safely read a credential from 1Password using op CLI."""
        try:
            result = subprocess.run(
                ["op", "read", op_reference],
                capture_output=True,
                text=True,
                timeout=30,  # Shorter timeout for individual reads during rotation
            )

            if result.returncode != 0:
                logger.error(f"Failed to read {op_reference} from 1Password")
                return None

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            logger.error(f"Timeout reading {op_reference} from 1Password")
            return None
        except Exception as e:
            logger.error(f"Exception reading {op_reference} from 1Password: {e}")
            return None

    async def _generate_new_credential(
        self, credential_type: str, metadata: Dict[str, Any]
    ) -> Optional[str]:
        """[EXPERIMENTAL] Generate a new credential value.

        WARNING: This method generates UUID-based tokens only and is NOT suitable
        for production use. Real credential generation requires provider-specific
        integration (1Password SDK, AWS IAM CreateAccessKey, etc.).

        To implement production credential generation:
        - For API keys: integrate with the target service's key management API
        - For AWS credentials: use boto3.client('iam').create_access_key()
        - For 1Password: use the 1Password SDK to create and store credentials
        """
        logger.warning(
            f"[EXPERIMENTAL] _generate_new_credential called for type={credential_type!r}. "
            "UUID-based token generated — NOT suitable for production use. "
            "Implement provider-specific credential generation before v1.0."
        )
        new_value = f"agentshroud-{credential_type}-{uuid4().hex[:16]}"
        logger.info(f"Generated new {credential_type} credential (experimental UUID token)")
        return new_value

    async def _store_credential_in_1password(
        self, op_reference: str, credential_value: str
    ) -> bool:
        """Store a new credential in 1Password."""
        try:
            # Extract components from op:// reference
            # Format: op://vault/item/field
            parts = op_reference.replace("op://", "").split("/")
            if len(parts) < 3:
                logger.error(f"Invalid op:// reference format: {op_reference}")
                return False

            vault, item, field = parts[0], parts[1], parts[2]

            # Use op CLI to update the field
            result = subprocess.run(
                ["op", "item", "edit", item, f"{field}={credential_value}", f"--vault={vault}"],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                logger.error(f"Failed to store credential in 1Password: {result.stderr}")
                return False

            logger.info(f"Successfully stored new credential in {op_reference}")
            return True

        except subprocess.TimeoutExpired:
            logger.error("Timeout storing credential in 1Password")
            return False
        except Exception as e:
            logger.error(f"Exception storing credential in 1Password: {e}")
            return False

    async def _validate_credential(
        self, credential_type: str, op_reference: str, metadata: Dict[str, Any]
    ) -> tuple[bool, str]:
        """Validate a credential using registered validator."""
        validator = self._validators.get(credential_type)
        if not validator:
            logger.warning(f"No validator registered for {credential_type}, skipping validation")
            return True, "No validator configured"

        try:
            return await validator.validate(op_reference, metadata)
        except Exception as e:
            logger.error(f"Validation failed with exception: {e}")
            return False, f"Validation exception: {str(e)}"

    async def rotate_credential(
        self, credential_id: str, force: bool = False, emergency: bool = False
    ) -> Dict[str, Any]:
        """Rotate a single credential with zero downtime.

        Workflow: generate new → validate new → swap active → retire old
        """
        if credential_id not in self._credentials:
            return {"success": False, "error": f"Credential {credential_id} not found"}

        cred = self._credentials[credential_id]
        policy = self.config.get_policy(cred.credential_type)

        # Check if rotation is needed
        if not force and not emergency and not cred.should_rotate(policy):
            return {
                "success": False,
                "error": f"Credential {credential_id} does not need rotation yet",
            }

        # Check if already in progress
        if cred.status == RotationStatus.IN_PROGRESS:
            return {"success": False, "error": f"Rotation already in progress for {credential_id}"}

        # Check failure limits
        if cred.failed_attempts >= policy.max_rotation_attempts and not force:
            return {
                "success": False,
                "error": f"Max rotation attempts exceeded for {credential_id}",
            }

        async with self._rotation_lock:
            try:
                logger.info(f"Starting rotation for credential: {credential_id}")
                cred.status = RotationStatus.IN_PROGRESS

                # Step 1: Generate new credential
                new_credential = await self._generate_new_credential(
                    cred.credential_type, cred.metadata
                )
                if not new_credential:
                    raise Exception("Failed to generate new credential")

                # Step 2: Create new op:// reference for the new credential
                # In practice, this might involve creating a new 1Password item
                # For now, we'll simulate by appending a timestamp
                timestamp = int(time.time())
                new_op_ref = f"{cred.op_reference}-new-{timestamp}"

                # Step 3: Store new credential in 1Password
                if not await self._store_credential_in_1password(new_op_ref, new_credential):
                    raise Exception("Failed to store new credential in 1Password")

                # Step 4: Validate new credential
                cred.status = RotationStatus.VALIDATING
                is_valid, validation_msg = await self._validate_credential(
                    cred.credential_type, new_op_ref, cred.metadata
                )

                if not is_valid:
                    raise Exception(f"New credential validation failed: {validation_msg}")

                # Step 5: Swap active → Start grace period
                cred.old_op_reference = cred.op_reference
                cred.op_reference = new_op_ref
                cred.grace_period_end = datetime.now(timezone.utc) + timedelta(
                    hours=policy.grace_period_hours
                )
                cred.last_rotated_at = datetime.now(timezone.utc)
                cred.rotation_count += 1
                cred.status = RotationStatus.ACTIVE
                cred.failed_attempts = 0  # Reset on success
                cred.last_failure_reason = None

                # Schedule old credential retirement
                asyncio.create_task(self._retire_old_credential_after_grace_period(credential_id))

                logger.info(f"Successfully rotated credential: {credential_id}")
                return {
                    "success": True,
                    "credential_id": credential_id,
                    "rotation_count": cred.rotation_count,
                    "grace_period_end": cred.grace_period_end.isoformat(),
                }

            except Exception as e:
                # Rollback on failure
                logger.error(f"Credential rotation failed for {credential_id}: {e}")
                cred.status = RotationStatus.FAILED
                cred.failed_attempts += 1
                cred.last_failure_reason = str(e)

                # Attempt rollback if we got far enough to swap references
                if hasattr(locals(), "new_op_ref") and cred.old_op_reference:
                    try:
                        cred.op_reference = cred.old_op_reference
                        cred.old_op_reference = None
                        cred.grace_period_end = None
                        cred.status = RotationStatus.ROLLED_BACK
                        logger.info(f"Rolled back credential {credential_id}")
                    except Exception as rollback_e:
                        logger.error(f"Rollback also failed for {credential_id}: {rollback_e}")

                return {
                    "success": False,
                    "error": str(e),
                    "credential_id": credential_id,
                    "failed_attempts": cred.failed_attempts,
                }

    async def _retire_old_credential_after_grace_period(self, credential_id: str) -> None:
        """Retire old credential after grace period ends."""
        cred = self._credentials.get(credential_id)
        if not cred or not cred.grace_period_end:
            return

        # Wait for grace period to end
        now = datetime.now(timezone.utc)
        if cred.grace_period_end > now:
            sleep_seconds = (cred.grace_period_end - now).total_seconds()
            await asyncio.sleep(sleep_seconds)

        # Retire old credential
        if cred.old_op_reference:
            logger.info(f"Retiring old credential for {credential_id}")
            # In practice, might remove from 1Password or mark as inactive
            cred.old_op_reference = None
            cred.grace_period_end = None

    async def check_and_rotate_due_credentials(self) -> Dict[str, Any]:
        """Check all credentials and rotate those that are due."""
        if not self.config.enable_scheduled_rotation:
            return {"message": "Scheduled rotation is disabled"}

        results = {"checked": 0, "rotated": 0, "warnings": 0, "failures": 0, "details": []}

        for cred_id, cred in self._credentials.items():
            results["checked"] += 1
            policy = self.config.get_policy(cred.credential_type)

            if cred.should_rotate(policy):
                result = await self.rotate_credential(cred_id)
                if result["success"]:
                    results["rotated"] += 1
                    results["details"].append(f"Rotated {cred_id}")
                else:
                    results["failures"] += 1
                    results["details"].append(f"Failed to rotate {cred_id}: {result.get(error)}")

            elif cred.should_warn(policy):
                results["warnings"] += 1
                results["details"].append(f"Warning: {cred_id} approaching rotation age")

        return results

    async def emergency_rotate_credential(
        self, credential_id: str, trigger_reason: str
    ) -> Dict[str, Any]:
        """Perform emergency rotation of a credential."""
        if not self.config.is_emergency_trigger_enabled(trigger_reason):
            return {"success": False, "error": f"Emergency trigger {trigger_reason} is not enabled"}

        logger.warning(f"Emergency rotation triggered for {credential_id}: {trigger_reason}")
        return await self.rotate_credential(credential_id, force=True, emergency=True)

    def cleanup_retired_credentials(self) -> Dict[str, Any]:
        """Clean up any credentials past their grace period."""
        cleaned = []
        for cred_id, cred in self._credentials.items():
            if (
                cred.grace_period_end
                and datetime.now(timezone.utc) > cred.grace_period_end
                and cred.old_op_reference
            ):

                cred.old_op_reference = None
                cred.grace_period_end = None
                cleaned.append(cred_id)
                logger.info(f"Cleaned up expired grace period for {cred_id}")

        return {"cleaned": len(cleaned), "credential_ids": cleaned}
