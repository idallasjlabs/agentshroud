# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Kill switch monitoring configuration.

Configuration for automated kill switch verification and heartbeat monitoring
to ensure the emergency shutdown mechanism remains functional.
"""

import os
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path
from typing import Any


@dataclass
class KillSwitchConfig:
    """Configuration for kill switch monitoring and verification."""

    # Verification Schedule
    verification_interval: timedelta = timedelta(days=30)  # Monthly verification
    verification_timeout: timedelta = timedelta(seconds=30)  # Timeout for kill switch checks
    
    # Heartbeat Monitoring
    heartbeat_interval: timedelta = timedelta(minutes=5)  # How often to check heartbeat
    heartbeat_timeout: timedelta = timedelta(seconds=10)  # Max response time for heartbeat
    heartbeat_miss_threshold: int = 3  # Consecutive misses before alert
    
    # Anomaly Detection Thresholds
    max_tool_calls_per_minute: int = 20  # Excessive tool usage
    max_tokens_per_hour: int = 100000  # Excessive token usage
    max_requests_per_minute: int = 30  # Rapid-fire requests
    memory_threshold_mb: int = 1024  # Memory usage alert threshold
    cpu_threshold_percent: float = 80.0  # CPU usage alert threshold
    
    # File Paths
    killswitch_script_path: Path = Path("/app/docker/scripts/killswitch.sh")
    verification_log_path: Path = Path("/var/log/security/killswitch_verification.jsonl")
    heartbeat_log_path: Path = Path("/var/log/security/heartbeat.jsonl")
    
    # Alert Settings
    alert_on_verification_failure: bool = True
    alert_on_heartbeat_miss: bool = True
    alert_on_anomaly: bool = True
    alert_severity: str = "CRITICAL"
    
    # Test Configuration
    dry_run_enabled: bool = True  # Always start in dry-run mode for safety
    test_freeze_mode: bool = True  # Test freeze mode by default
    test_shutdown_mode: bool = False  # Test shutdown mode (more disruptive)
    test_disconnect_mode: bool = False  # Test disconnect mode (most disruptive)
    
    @classmethod
    def from_env(cls) -> "KillSwitchConfig":
        """Load configuration from environment variables."""
        return cls(
            verification_interval=timedelta(
                days=int(os.getenv("KILLSWITCH_VERIFY_DAYS", "30"))
            ),
            verification_timeout=timedelta(
                seconds=int(os.getenv("KILLSWITCH_VERIFY_TIMEOUT", "30"))
            ),
            heartbeat_interval=timedelta(
                minutes=int(os.getenv("KILLSWITCH_HEARTBEAT_MINUTES", "5"))
            ),
            heartbeat_timeout=timedelta(
                seconds=int(os.getenv("KILLSWITCH_HEARTBEAT_TIMEOUT", "10"))
            ),
            heartbeat_miss_threshold=int(
                os.getenv("KILLSWITCH_HEARTBEAT_MISS_THRESHOLD", "3")
            ),
            max_tool_calls_per_minute=int(
                os.getenv("KILLSWITCH_MAX_TOOL_CALLS_PER_MIN", "20")
            ),
            max_tokens_per_hour=int(
                os.getenv("KILLSWITCH_MAX_TOKENS_PER_HOUR", "100000")
            ),
            max_requests_per_minute=int(
                os.getenv("KILLSWITCH_MAX_REQUESTS_PER_MIN", "30")
            ),
            memory_threshold_mb=int(
                os.getenv("KILLSWITCH_MEMORY_THRESHOLD_MB", "1024")
            ),
            cpu_threshold_percent=float(
                os.getenv("KILLSWITCH_CPU_THRESHOLD_PERCENT", "80.0")
            ),
            killswitch_script_path=Path(
                os.getenv("KILLSWITCH_SCRIPT_PATH", "/app/docker/scripts/killswitch.sh")
            ),
            verification_log_path=Path(
                os.getenv("KILLSWITCH_VERIFY_LOG", "/var/log/security/killswitch_verification.jsonl")
            ),
            heartbeat_log_path=Path(
                os.getenv("KILLSWITCH_HEARTBEAT_LOG", "/var/log/security/heartbeat.jsonl")
            ),
            alert_on_verification_failure=os.getenv("KILLSWITCH_ALERT_VERIFY_FAIL", "true").lower() == "true",
            alert_on_heartbeat_miss=os.getenv("KILLSWITCH_ALERT_HEARTBEAT_MISS", "true").lower() == "true",
            alert_on_anomaly=os.getenv("KILLSWITCH_ALERT_ANOMALY", "true").lower() == "true",
            alert_severity=os.getenv("KILLSWITCH_ALERT_SEVERITY", "CRITICAL"),
            dry_run_enabled=os.getenv("KILLSWITCH_DRY_RUN", "true").lower() == "true",
            test_freeze_mode=os.getenv("KILLSWITCH_TEST_FREEZE", "true").lower() == "true",
            test_shutdown_mode=os.getenv("KILLSWITCH_TEST_SHUTDOWN", "false").lower() == "true",
            test_disconnect_mode=os.getenv("KILLSWITCH_TEST_DISCONNECT", "false").lower() == "true",
        )

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary for serialization."""
        return {
            "verification_interval_days": self.verification_interval.days,
            "verification_timeout_seconds": int(self.verification_timeout.total_seconds()),
            "heartbeat_interval_minutes": int(self.heartbeat_interval.total_seconds() // 60),
            "heartbeat_timeout_seconds": int(self.heartbeat_timeout.total_seconds()),
            "heartbeat_miss_threshold": self.heartbeat_miss_threshold,
            "max_tool_calls_per_minute": self.max_tool_calls_per_minute,
            "max_tokens_per_hour": self.max_tokens_per_hour,
            "max_requests_per_minute": self.max_requests_per_minute,
            "memory_threshold_mb": self.memory_threshold_mb,
            "cpu_threshold_percent": self.cpu_threshold_percent,
            "killswitch_script_path": str(self.killswitch_script_path),
            "verification_log_path": str(self.verification_log_path),
            "heartbeat_log_path": str(self.heartbeat_log_path),
            "alert_on_verification_failure": self.alert_on_verification_failure,
            "alert_on_heartbeat_miss": self.alert_on_heartbeat_miss,
            "alert_on_anomaly": self.alert_on_anomaly,
            "alert_severity": self.alert_severity,
            "dry_run_enabled": self.dry_run_enabled,
            "test_freeze_mode": self.test_freeze_mode,
            "test_shutdown_mode": self.test_shutdown_mode,
            "test_disconnect_mode": self.test_disconnect_mode,
        }
