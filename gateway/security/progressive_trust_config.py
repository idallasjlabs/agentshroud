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

VALID_ENFORCEMENT_MODES = ("enforce", "monitor")


def resolve_enforcement_mode(value: object) -> str:
    """Fail-closed resolver for the enforcement-mode env var (SCRUM-78).

    Returns "monitor" ONLY for the exact case-insensitive token "monitor";
    any other input — None, "", whitespace, "off", "true", typos like
    "moniter" — resolves to "enforce".  A security lever must never open
    (degrade to log-only) by accident.
    """
    if isinstance(value, str) and value.strip().lower() == "monitor":
        return "monitor"
    return "enforce"


class TrustLevel(Enum):
    """Trust levels from untrusted to verified."""

    UNTRUSTED = "untrusted"  # New users - read-only, no tool calls
    BASIC = "basic"  # Low-risk tools only (search, status)
    STANDARD = "standard"  # Low + medium tools (file read, web fetch)
    TRUSTED = "trusted"  # Low + medium + high (file write, email, iCloud)
    VERIFIED = "verified"  # All tools (owner-verified users)


class ViolationType(Enum):
    """Types of security violations."""

    UNAUTHORIZED_ACCESS = "unauthorized_access"
    SUSPICIOUS_BEHAVIOR = "suspicious_behavior"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    MALICIOUS_INTENT = "malicious_intent"
    POLICY_VIOLATION = "policy_violation"

    # A2A (Agent-to-Agent) protocol governance (SCRUM-129) — see
    # docs/security/threat-model.md, "A2A Protocol Threat Analysis".
    #
    # A peer attempted GetTask/CancelTask/SubscribeToTask on a task_id it did
    # not create. Independent mitigation for upstream Hermes issue #83701
    # (contextId collision can merge cross-tenant conversation history) — a
    # strong signal of either a client bug or active cross-tenant probing,
    # heavier than a generic POLICY_VIOLATION but not immediate-demotion
    # severe (a single ownership mismatch could still be a legitimate client
    # retry race; a pattern of them is caught by the score decay, not a
    # one-shot demotion).
    A2A_TASK_OWNERSHIP_VIOLATION = "a2a_task_ownership_violation"
    # A peer's SetTaskPushNotificationConfig callback URL failed the hardened
    # SSRF canonicalization check (is_safe_a2a_callback_url — independent
    # mitigation for upstream issue #78298: decimal/hex/octal/trailing-dot
    # IP-encoding bypasses). Unlike a task-ownership mismatch, there is no
    # benign explanation for a callback URL that canonicalizes to a private/
    # loopback/metadata address — this is unambiguous malicious intent,
    # hence severe_violation_types below.
    A2A_SSRF_CALLBACK_ATTEMPT = "a2a_ssrf_callback_attempt"


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
    promotion_thresholds: Dict[TrustLevel, PromotionThreshold] = field(
        default_factory=lambda: {
            TrustLevel.BASIC: PromotionThreshold(
                min_interactions=10, min_days_since_first=1, max_violations=0
            ),
            TrustLevel.STANDARD: PromotionThreshold(
                min_interactions=50, min_days_since_first=7, max_violations=0
            ),
            TrustLevel.TRUSTED: PromotionThreshold(
                min_interactions=200, min_days_since_first=30, max_violations=1
            ),
            TrustLevel.VERIFIED: PromotionThreshold(
                min_interactions=500,
                min_days_since_first=90,
                max_violations=1,
                requires_owner_vouching=True,
            ),
        }
    )

    # Tool access by trust level
    tool_access: Dict[TrustLevel, Set[str]] = field(
        default_factory=lambda: {
            TrustLevel.UNTRUSTED: {
                # Read-only access, no tool calls
                "read_status",
                "view_logs",
            },
            TrustLevel.BASIC: {
                # Low-risk tools
                "read_status",
                "view_logs",
                "web_search",
                "get_weather",
                "list_files",
                "get_time",
                "check_system_status",
            },
            TrustLevel.STANDARD: {
                # Low + medium risk tools
                "read_status",
                "view_logs",
                "web_search",
                "get_weather",
                "list_files",
                "get_time",
                "check_system_status",
                "read_file",
                "web_fetch",
                "browse_web",
                "search_documents",
                "get_calendar",
                "check_connectivity",
            },
            TrustLevel.TRUSTED: {
                # Low + medium + high risk tools
                "read_status",
                "view_logs",
                "web_search",
                "get_weather",
                "list_files",
                "get_time",
                "check_system_status",
                "read_file",
                "web_fetch",
                "browse_web",
                "search_documents",
                "get_calendar",
                "check_connectivity",
                "write_file",
                "send_email",
                "access_icloud",
                "modify_calendar",
                "execute_safe_commands",
                "install_packages",
            },
            TrustLevel.VERIFIED: {
                # All tools - no restrictions
                "*"  # Special marker for all tools
            },
        }
    )

    # Violation penalties - how much trust to lose per violation type
    violation_penalties: Dict[ViolationType, int] = field(
        default_factory=lambda: {
            ViolationType.UNAUTHORIZED_ACCESS: 50,
            ViolationType.SUSPICIOUS_BEHAVIOR: 25,
            ViolationType.RATE_LIMIT_EXCEEDED: 10,
            ViolationType.MALICIOUS_INTENT: 100,
            ViolationType.POLICY_VIOLATION: 30,
            # Heavier than generic POLICY_VIOLATION (a real cross-tenant
            # boundary probe, not just an unlisted-peer routing miss) but
            # below MALICIOUS_INTENT — see ViolationType docstring above.
            ViolationType.A2A_TASK_OWNERSHIP_VIOLATION: 60,
            # Same tier as MALICIOUS_INTENT — no benign explanation exists
            # for a callback URL that canonicalizes to a private/loopback/
            # metadata address.
            ViolationType.A2A_SSRF_CALLBACK_ATTEMPT: 100,
        }
    )

    # Automatic demotion settings
    auto_demotion_enabled: bool = True
    severe_violation_immediate_demotion: bool = True
    severe_violation_types: Set[ViolationType] = field(
        default_factory=lambda: {
            ViolationType.MALICIOUS_INTENT,
            ViolationType.UNAUTHORIZED_ACCESS,
            # Unambiguous malicious intent — see ViolationType docstring above.
            ViolationType.A2A_SSRF_CALLBACK_ATTEMPT,
        }
    )

    # Enforcement mode — the operational monitor↔enforce lever (SCRUM-78).
    # "enforce" (default): a trust-ladder deny blocks the tool call — current,
    #   tested behavior; the default is unchanged so no rollout regresses.
    # "monitor": the would-be denial is logged but the call falls through to
    #   the role-based ACL — used to measure blast radius before enforcing a
    #   new/expanded ladder vocabulary, and as an instant rollback valve.
    enforcement_mode: str = "enforce"

    # Database settings
    db_path: str = "progressive_trust.db"

    # Rate limiting settings
    max_interactions_per_hour: Dict[TrustLevel, int] = field(
        default_factory=lambda: {
            TrustLevel.UNTRUSTED: 5,
            TrustLevel.BASIC: 20,
            TrustLevel.STANDARD: 50,
            TrustLevel.TRUSTED: 100,
            TrustLevel.VERIFIED: 1000,
        }
    )

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
            TrustLevel.VERIFIED,
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
