# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Key Rotation Configuration — defines rotation schedules and policies per credential type.

Supports time-based rotation schedules, alert thresholds, and emergency rotation triggers.
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, Optional

logger = logging.getLogger("agentshroud.security.key_rotation_config")


@dataclass
class CredentialRotationPolicy:
    """Rotation policy for a specific credential type."""
    
    # Rotation schedule
    max_age_days: int
    """Maximum age before credential must be rotated (in days)"""
    
    warn_threshold_percent: float = 80.0
    """Warn when credential reaches this percentage of max age"""
    
    # Grace period settings
    grace_period_hours: int = 24
    """Hours to keep old credential valid during rotation"""
    
    # Emergency rotation triggers
    enable_emergency_rotation: bool = True
    """Whether emergency rotation is supported for this credential type"""
    
    # Validation settings
    validation_timeout_seconds: int = 30
    """Timeout for validating new credentials"""
    
    # Retry settings
    max_rotation_attempts: int = 3
    """Maximum attempts for rotation before marking as failed"""
    
    retry_delay_seconds: int = 300
    """Delay between rotation attempts (in seconds)"""


@dataclass
class KeyRotationConfig:
    """Configuration for key rotation policies and schedules."""
    
    # Default policies for common credential types
    policies: Dict[str, CredentialRotationPolicy] = field(default_factory=lambda: {
        "api_key": CredentialRotationPolicy(
            max_age_days=90,
            warn_threshold_percent=80.0,
            grace_period_hours=24,
            validation_timeout_seconds=30,
        ),
        "access_token": CredentialRotationPolicy(
            max_age_days=30,
            warn_threshold_percent=75.0,
            grace_period_hours=12,
            validation_timeout_seconds=15,
        ),
        "service_account_key": CredentialRotationPolicy(
            max_age_days=180,
            warn_threshold_percent=85.0,
            grace_period_hours=48,
            validation_timeout_seconds=60,
        ),
        "database_password": CredentialRotationPolicy(
            max_age_days=60,
            warn_threshold_percent=80.0,
            grace_period_hours=36,
            validation_timeout_seconds=45,
        ),
    })
    
    # Global settings
    enable_scheduled_rotation: bool = True
    """Whether scheduled rotation is enabled globally"""
    
    enable_emergency_rotation: bool = True
    """Whether emergency rotation is enabled globally"""
    
    rotation_check_interval_hours: int = 6
    """How often to check for credentials needing rotation"""
    
    # Alert settings
    alert_on_rotation_failure: bool = True
    """Whether to alert when rotation fails"""
    
    alert_on_validation_failure: bool = True
    """Whether to alert when new credential validation fails"""
    
    # 1Password integration settings
    op_vault_name: str = "Agent Shroud Bot Credentials"
    """1Password vault name for storing rotated credentials"""
    
    op_reference_prefix: str = "op://Agent Shroud Bot Credentials"
    """Prefix for op:// references"""
    
    # Emergency rotation triggers
    emergency_triggers: Dict[str, bool] = field(default_factory=lambda: {
        "suspected_compromise": True,
        "failed_authentication": True,
        "security_scan_detection": True,
        "manual_trigger": True,
    })

    def get_policy(self, credential_type: str) -> CredentialRotationPolicy:
        """Get rotation policy for a credential type, falling back to api_key default."""
        return self.policies.get(credential_type, self.policies["api_key"])
    
    def add_custom_policy(self, credential_type: str, policy: CredentialRotationPolicy) -> None:
        """Add or update a rotation policy for a specific credential type."""
        self.policies[credential_type] = policy
        logger.info(f"Updated rotation policy for credential type: {credential_type}")
    
    def is_emergency_trigger_enabled(self, trigger_type: str) -> bool:
        """Check if a specific emergency trigger is enabled."""
        return (
            self.enable_emergency_rotation and 
            self.emergency_triggers.get(trigger_type, False)
        )
    
    def get_op_reference(self, item_name: str, field_name: str = "credential") -> str:
        """Build a complete op:// reference for a credential."""
        return f"{self.op_reference_prefix}/{item_name}/{field_name}"
