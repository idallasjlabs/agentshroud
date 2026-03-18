# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Privacy Policy Enforcer (v0.9.0 Tranche 2)

Admin-defined configuration declaring which services are "private" (owner-only),
"shared" (all collaborators), or "group_only" (specific group members).

Enforced by the gateway pipeline before responses reach collaborator sessions.
All access attempts to private services are logged and can trigger owner alerts.

Usage:
    policy = PrivacyPolicy.from_dict(yaml_section)
    enforcer = PrivacyPolicyEnforcer(policy, rbac_config)
    allowed = enforcer.is_service_allowed(user_id, "gmail")
    filtered_text, was_modified = enforcer.filter_response(raw_text, user_id)
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.security.rbac_config import RBACConfig

logger = logging.getLogger("agentshroud.security.privacy_policy")


# ---------------------------------------------------------------------------
# Domain types
# ---------------------------------------------------------------------------

class ServicePrivacy(str, Enum):
    """Privacy classification for a service."""
    PRIVATE = "private"       # Owner-only — collaborators cannot access
    SHARED = "shared"         # All collaborators may access
    GROUP_ONLY = "group_only" # Only members of specified groups may access


@dataclass
class ServicePolicy:
    """Privacy policy for a single service."""
    name: str
    privacy: ServicePrivacy
    allowed_groups: List[str] = field(default_factory=list)  # Only used when privacy=GROUP_ONLY
    description: str = ""

    @classmethod
    def from_dict(cls, name: str, data: dict) -> "ServicePolicy":
        privacy_str = data.get("privacy", "private")
        try:
            privacy = ServicePrivacy(privacy_str)
        except ValueError:
            logger.warning("Unknown privacy value %r for service %r — defaulting to private", privacy_str, name)
            privacy = ServicePrivacy.PRIVATE
        return cls(
            name=name,
            privacy=privacy,
            allowed_groups=data.get("allowed_groups", []),
            description=data.get("description", ""),
        )


# ---------------------------------------------------------------------------
# Policy config
# ---------------------------------------------------------------------------

# Default private services (in addition to any YAML config).
# These are the known admin-private services that must never be accessible
# to collaborators without explicit owner override.
_DEFAULT_PRIVATE_SERVICES: Set[str] = {
    "gmail", "google_mail", "icloud", "apple_mail", "apple_messages",
    "home_assistant", "homekit", "banking", "stripe", "paypal",
    "1password", "onepassword", "aws_iam", "ssh", "terraform",
}

# Response content patterns that signal private service data was included.
_PRIVATE_RESPONSE_PATTERNS: List[re.Pattern] = [
    # Email-like content
    re.compile(r"(?i)(from|to|subject|cc|bcc):\s+\S+@\S+"),
    # Calendar/appointment details
    re.compile(r"(?i)(meeting|appointment|event)\s+at\s+\d{1,2}:\d{2}"),
    # Home automation state
    re.compile(r"(?i)(device|sensor|switch|light)\s+(is\s+)?(on|off|locked|unlocked)"),
    # Financial amounts
    re.compile(r"\$\d+(?:\.\d{2})?\s+(?:transferred|charged|debited|credited)"),
    # API credentials
    re.compile(r"(?i)(token|key|secret|password)\s*[:=]\s*\S{8,}"),
]

_SENSITIVE_BLOCK_MARKER = "[CONTENT BLOCKED — ADMIN-PRIVATE DATA]"


@dataclass
class PrivacyPolicy:
    """Privacy policy configuration.

    Loaded from agentshroud.yaml `privacy:` section.
    """
    services: Dict[str, ServicePolicy] = field(default_factory=dict)
    # Additional regex patterns to redact from all collaborator responses
    extra_redact_patterns: List[str] = field(default_factory=list)
    # Whether to log access attempts to private services
    audit_access_attempts: bool = True
    # Whether to alert owner on private data access attempts
    alert_on_private_access: bool = True

    @classmethod
    def from_dict(cls, data: dict) -> "PrivacyPolicy":
        """Parse from a YAML/dict representation.

        Example YAML:
            privacy:
              services:
                gmail:
                  privacy: private
                jira:
                  privacy: shared
                monitoring_ops:
                  privacy: group_only
                  allowed_groups: [sort, gsde]
              audit_access_attempts: true
        """
        services: Dict[str, ServicePolicy] = {}

        # Start with default private services
        for name in _DEFAULT_PRIVATE_SERVICES:
            services[name] = ServicePolicy(name=name, privacy=ServicePrivacy.PRIVATE)

        # Override/extend from config
        for svc_name, svc_data in data.get("services", {}).items():
            if isinstance(svc_data, str):
                # Short form: "gmail: private"
                svc_data = {"privacy": svc_data}
            services[svc_name] = ServicePolicy.from_dict(svc_name, svc_data)

        return cls(
            services=services,
            extra_redact_patterns=data.get("extra_redact_patterns", []),
            audit_access_attempts=bool(data.get("audit_access_attempts", True)),
            alert_on_private_access=bool(data.get("alert_on_private_access", True)),
        )

    @classmethod
    def default(cls) -> "PrivacyPolicy":
        """Return a default policy with all known private services locked down."""
        return cls.from_dict({})


# ---------------------------------------------------------------------------
# Enforcer
# ---------------------------------------------------------------------------

class PrivacyPolicyEnforcer:
    """Evaluates access control and filters responses per privacy policy."""

    def __init__(self, policy: Optional[PrivacyPolicy] = None, rbac_config: Optional["RBACConfig"] = None):
        self._policy = policy or PrivacyPolicy.default()
        self._rbac = rbac_config
        self._compiled_extra: List[re.Pattern] = []
        for pat_str in self._policy.extra_redact_patterns:
            try:
                self._compiled_extra.append(re.compile(pat_str))
            except re.error as exc:
                logger.warning("Invalid redact pattern %r: %s", pat_str, exc)

    # ------------------------------------------------------------------
    # Service access control
    # ------------------------------------------------------------------

    def is_service_allowed(self, user_id: str, service_name: str) -> bool:
        """Return True if user_id may access the named service."""
        svc_key = service_name.lower().strip()
        svc = self._policy.services.get(svc_key)

        role_value = self._get_role_value(user_id)

        # Owner: unrestricted
        if role_value == "owner":
            return True

        # Unknown service: allow (only block explicitly classified private services)
        if svc is None:
            return True

        if svc.privacy == ServicePrivacy.SHARED:
            return True

        if svc.privacy == ServicePrivacy.PRIVATE:
            if self._policy.audit_access_attempts:
                logger.warning(
                    "Private service access blocked: user=%s service=%s role=%s",
                    user_id, service_name, role_value,
                )
            return False

        if svc.privacy == ServicePrivacy.GROUP_ONLY:
            if self._user_in_allowed_groups(user_id, svc.allowed_groups):
                return True
            if self._policy.audit_access_attempts:
                logger.warning(
                    "Group-restricted service access blocked: user=%s service=%s allowed_groups=%s role=%s",
                    user_id, service_name, svc.allowed_groups, role_value,
                )
            return False

        return False  # deny-by-default for unknown privacy values

    def should_audit(self, user_id: str, service_name: str) -> bool:
        """Return True if an access attempt to this service should be logged."""
        if not self._policy.audit_access_attempts:
            return False
        svc = self._policy.services.get(service_name.lower().strip())
        if svc is None:
            return False
        return svc.privacy == ServicePrivacy.PRIVATE

    def should_alert(self, user_id: str, service_name: str) -> bool:
        """Return True if the owner should be alerted about this access attempt."""
        return (
            self._policy.alert_on_private_access
            and self.should_audit(user_id, service_name)
            and self._get_role_value(user_id) != "owner"
        )

    # ------------------------------------------------------------------
    # Response filtering
    # ------------------------------------------------------------------

    def filter_response(self, response: str, user_id: str) -> Tuple[str, bool]:
        """Strip admin-private content from a response before delivering to user.

        Args:
            response: Raw bot response text.
            user_id: The recipient user ID.

        Returns:
            (filtered_text, was_modified): filtered text and whether anything was changed.
        """
        if self._get_role_value(user_id) == "owner":
            return response, False

        filtered = response
        was_modified = False

        # Apply built-in private response patterns
        for pattern in _PRIVATE_RESPONSE_PATTERNS:
            new_text = pattern.sub(_SENSITIVE_BLOCK_MARKER, filtered)
            if new_text != filtered:
                filtered = new_text
                was_modified = True

        # Apply extra configured patterns
        for pattern in self._compiled_extra:
            new_text = pattern.sub(_SENSITIVE_BLOCK_MARKER, filtered)
            if new_text != filtered:
                filtered = new_text
                was_modified = True

        if was_modified:
            logger.info(
                "Response filtered for non-owner user %s: private content redacted (len_before=%d len_after=%d)",
                user_id, len(response), len(filtered),
            )

        return filtered, was_modified

    def contains_private_data(self, text: str) -> bool:
        """Return True if text appears to contain admin-private data."""
        for pattern in _PRIVATE_RESPONSE_PATTERNS:
            if pattern.search(text):
                return True
        for pattern in self._compiled_extra:
            if pattern.search(text):
                return True
        return False

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_role_value(self, user_id: str) -> str:
        if self._rbac is None:
            return "viewer"
        role = self._rbac.get_user_role(user_id)
        return role.value if hasattr(role, "value") else str(role)

    def _user_in_allowed_groups(self, user_id: str, allowed_groups: List[str]) -> bool:
        if self._rbac is None:
            return False
        teams = getattr(self._rbac, "teams_config", None)
        if teams is None:
            return False
        for gid in allowed_groups:
            group = teams.groups.get(gid)
            if group and user_id in group.members:
                return True
        return False
