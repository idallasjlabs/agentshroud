# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration for the Outbound Information Filter

Defines default patterns, trust-level overrides, and customization options.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CustomPattern:
    """A custom filter pattern."""

    name: str
    pattern: str
    category: str
    replacement: str
    flags: int = 0
    enabled: bool = True


@dataclass
class OutboundFilterConfig:
    """Configuration for the outbound information filter."""

    # Operating mode: "enforce" (redact matches) or "monitor" (log only)
    mode: str = "enforce"

    # Trust-level disclosure overrides
    # Maps trust level -> category -> allowed (bool)
    trust_overrides: Dict[str, Dict[str, bool]] = field(
        default_factory=lambda: {
            "FULL": {
                # Admin/owner can see security details and operational info
                "security_architecture": True,
                "operational": True,
                # But never credentials or user IDs
                "credential": False,
                "user_identity": False,
                "infrastructure": False,
                "tool_inventory": False,
                "code_blocks": False,
            },
            "ELEVATED": {
                # Can see some operational details
                "operational": True,
                "security_architecture": False,
                "credential": False,
                "user_identity": False,
                "infrastructure": False,
                "tool_inventory": False,
                "code_blocks": False,
            },
            "STANDARD": {
                # Default user -- nothing extra
            },
            "BASIC": {
                # New user -- nothing extra
            },
            "UNTRUSTED": {
                # Unknown user -- strictest filtering
            },
        }
    )

    # Custom patterns to add beyond the built-in ones
    additional_patterns: List[CustomPattern] = field(default_factory=list)

    # Enable high-density response alerting
    enable_density_alerts: bool = True

    # Threshold for high-density alerting (number of matches)
    high_density_threshold: int = 5

    # Whether to enable progressive trust score decrements for probing
    enable_trust_penalties: bool = True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OutboundFilterConfig":
        """Create configuration from dictionary (e.g., from YAML)."""
        config = cls()

        if "mode" in data:
            config.mode = data["mode"]

        if "trust_overrides" in data:
            config.trust_overrides.update(data["trust_overrides"])

        if "additional_patterns" in data:
            patterns = []
            for pattern_data in data["additional_patterns"]:
                patterns.append(
                    CustomPattern(
                        name=pattern_data["name"],
                        pattern=pattern_data["pattern"],
                        category=pattern_data["category"],
                        replacement=pattern_data["replacement"],
                        flags=pattern_data.get("flags", 0),
                        enabled=pattern_data.get("enabled", True),
                    )
                )
            config.additional_patterns = patterns

        if "enable_density_alerts" in data:
            config.enable_density_alerts = data["enable_density_alerts"]

        if "high_density_threshold" in data:
            config.high_density_threshold = data["high_density_threshold"]

        if "enable_trust_penalties" in data:
            config.enable_trust_penalties = data["enable_trust_penalties"]

        return config

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "mode": self.mode,
            "trust_overrides": self.trust_overrides,
            "additional_patterns": [
                {
                    "name": p.name,
                    "pattern": p.pattern,
                    "category": p.category,
                    "replacement": p.replacement,
                    "flags": p.flags,
                    "enabled": p.enabled,
                }
                for p in self.additional_patterns
            ],
            "enable_density_alerts": self.enable_density_alerts,
            "high_density_threshold": self.high_density_threshold,
            "enable_trust_penalties": self.enable_trust_penalties,
        }
