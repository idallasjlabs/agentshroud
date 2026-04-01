# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Progressive Trust Configuration — Graduated permissions for new users.

Defines trust levels, promotion thresholds, tool tier mappings, and violation penalties.
New users start with minimal permissions and earn more over time based on behavior.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Set


class TrustLevel(Enum):
    """Trust levels from untrusted to verified."""
    UNTRUSTED = "untrusted"  # New users - read-only, no tool calls
    BASIC = "basic"          # Low-risk tools only (search, status)
    STANDARD = "standard"    # Low + medium tools (file read, web fetch)
    TRUSTED = "trusted"      # Low + medium + high (file write, email, iCloud)
    VERIFIED = "verified"    # All tools (owner-verified users)


class ViolationType(Enum):
    """Types of security violations."""
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    SUSPICIOUS_BEHAVIOR = "suspicious_behavior"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    MALICIOUS_INTENT = "malicious_intent"
    POLICY_VIOLATION = "policy_violation"


@dataclass
class PromotionThreshold:
    """Threshold for promoting to a trust level."""
    min_interactions: int
    min_days_since_first: int
    max_violations: int
    requires_owner_vouching: bool = False


@dataclass
class ProgressiveTrustConfig:
    """Configuration for the progressive trust system."""
    
    # Default trust level for new users
    default_trust_level: TrustLevel = TrustLevel.UNTRUSTED
    
    # Promotion thresholds for each level (except UNTRUSTED which is the default)
    promotion_thresholds: Dict[TrustLevel, PromotionThreshold] = field(default_factory=lambda: {
        TrustLevel.BASIC: PromotionThreshold(
            min_interactions=10,
            min_days_since_first=1,
            max_violations=0
        ),
        TrustLevel.STANDARD: PromotionThreshold(
            min_interactions=50,
            min_days_since_first=7,
            max_violations=0
        ),
        TrustLevel.TRUSTED: PromotionThreshold(
            min_interactions=200,
            min_days_since_first=30,
            max_violations=1
        ),
        TrustLevel.VERIFIED: PromotionThreshold(
            min_interactions=500,
            min_days_since_first=90,
            max_violations=1,
            requires_owner_vouching=True
        ),
    })
    
    # Tool access by trust level
    tool_access: Dict[TrustLevel, Set[str]] = field(default_factory=lambda: {
        TrustLevel.UNTRUSTED: {
            # Read-only access, no tool calls
            "read_status", "view_logs"
        },
        TrustLevel.BASIC: {
            # Low-risk tools
            "read_status", "view_logs", "web_search", "get_weather", 
            "list_files", "get_time", "check_system_status"
        },
        TrustLevel.STANDARD: {
            # Low + medium risk tools
            "read_status", "view_logs", "web_search", "get_weather",
            "list_files", "get_time", "check_system_status",
            "read_file", "web_fetch", "browse_web", "search_documents",
            "get_calendar", "check_connectivity"
        },
        TrustLevel.TRUSTED: {
            # Low + medium + high risk tools
            "read_status", "view_logs", "web_search", "get_weather",
            "list_files", "get_time", "check_system_status",
            "read_file", "web_fetch", "browse_web", "search_documents", 
            "get_calendar", "check_connectivity",
            "write_file", "send_email", "access_icloud", "modify_calendar",
            "execute_safe_commands", "install_packages"
        },
        TrustLevel.VERIFIED: {
            # All tools - no restrictions
            "*"  # Special marker for all tools
        }
    })
    
    # Violation penalties - how much trust to lose per violation type
    violation_penalties: Dict[ViolationType, int] = field(default_factory=lambda: {
        ViolationType.UNAUTHORIZED_ACCESS: 50,
        ViolationType.SUSPICIOUS_BEHAVIOR: 25,
        ViolationType.RATE_LIMIT_EXCEEDED: 10,
        ViolationType.MALICIOUS_INTENT: 100,
        ViolationType.POLICY_VIOLATION: 30,
    })
    
    # Automatic demotion settings
    auto_demotion_enabled: bool = True
    severe_violation_immediate_demotion: bool = True
    severe_violation_types: Set[ViolationType] = field(default_factory=lambda: {
        ViolationType.MALICIOUS_INTENT,
        ViolationType.UNAUTHORIZED_ACCESS
    })
    
    # Database settings
    db_path: str = "progressive_trust.db"
    
    # Rate limiting settings
    max_interactions_per_hour: Dict[TrustLevel, int] = field(default_factory=lambda: {
        TrustLevel.UNTRUSTED: 5,
        TrustLevel.BASIC: 20,
        TrustLevel.STANDARD: 50,
        TrustLevel.TRUSTED: 100,
        TrustLevel.VERIFIED: 1000,
    })
    
    def is_tool_allowed(self, trust_level: TrustLevel, tool_name: str) -> bool:
        """Check if a tool is allowed for the given trust level."""
        allowed_tools = self.tool_access.get(trust_level, set())
        
        # Verified users get access to all tools
        if "*" in allowed_tools:
            return True
            
        return tool_name in allowed_tools
    
    def get_trust_level_order(self) -> List[TrustLevel]:
        """Get trust levels in ascending order."""
        return [
            TrustLevel.UNTRUSTED,
            TrustLevel.BASIC,
            TrustLevel.STANDARD, 
            TrustLevel.TRUSTED,
            TrustLevel.VERIFIED
        ]
    
    def get_next_trust_level(self, current_level: TrustLevel) -> TrustLevel | None:
        """Get the next trust level for promotion, or None if already at max."""
        levels = self.get_trust_level_order()
        try:
            current_index = levels.index(current_level)
            if current_index < len(levels) - 1:
                return levels[current_index + 1]
        except ValueError:
            pass
        return None
    
    def get_previous_trust_level(self, current_level: TrustLevel) -> TrustLevel | None:
        """Get the previous trust level for demotion, or None if already at min."""
        levels = self.get_trust_level_order()
        try:
            current_index = levels.index(current_level)
            if current_index > 0:
                return levels[current_index - 1]
        except ValueError:
            pass
        return None
