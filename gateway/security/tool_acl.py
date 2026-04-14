# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tool-Level Access Control (v0.9.0 Tranche 2)

Enforces per-user, per-group tool allowlists/blocklists at the MCP proxy layer.
Collaborators cannot invoke admin-only tools (Gmail, Home Assistant, iCloud,
financial services, key management, etc.).

Design decisions:
  - PRIVATE_TOOLS: owner-only tools (never accessible to collaborators)
  - ADMIN_TOOLS: admin+ tools (not accessible to plain collaborators/viewers)
  - Group tool allowlists: per-group override to grant additional tools
    (e.g. an "ops" group might be allowed "monitoring" tools)
  - Deny-by-default for unknown tools when not in collaborator allowlist

Integrates with:
  - RBACConfig for role resolution
  - TeamsConfig for group tool_tier_max and per-group overrides
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple

if TYPE_CHECKING:
    from gateway.security.rbac_config import RBACConfig, Role

logger = logging.getLogger("agentshroud.security.tool_acl")

# ---------------------------------------------------------------------------
# Tool classification sets
# ---------------------------------------------------------------------------

# Owner-only: collaborators and admins cannot use these regardless of context.
PRIVATE_TOOLS: frozenset[str] = frozenset(
    {
        # Personal services
        "gmail",
        "google_mail",
        "icloud",
        "icloud_calendar",
        "icloud_contacts",
        "icloud_notes",
        "apple_messages",
        "apple_mail",
        # Financial
        "banking",
        "financial",
        "stripe",
        "paypal",
        "venmo",
        # Key / credential management
        "key_rotation",
        "secret_manager",
        "1password",
        "onepassword",
        "op",  # 1Password CLI
        "credential_injector",
        # Infrastructure
        "ssh",
        "aws_iam",
        "terraform",
        "ansible",
        # Home automation (personal)
        "home_assistant",
        "homekit",
        "ha_automation",
        # Shell / command execution (CVE-2026-35190 fix — owner-only)
        "execute_command",
        "exec",
        "bash",
        "shell",
        "run_command",
    }
)

# Admin+: available to owner + admin roles only.
ADMIN_TOOLS: frozenset[str] = frozenset(
    {
        "rbac_manage",
        "user_management",
        "config_write",
        "gateway_config",
        "audit_export",
        "security_scan",
        "trivy",
        "wazuh",
        "clamav",
        "openscap",
        "egress_policy",
        "memory_manage",
        "session_admin",
        "kill_session",
        "delegation_manage",
    }
)

# Collaborator allowlist: tools collaborators CAN use (additive to PRIVATE/ADMIN blocklists)
# These are the "safe" subset. Everything not in this list is also denied for
# collaborators unless explicitly in a group allowlist.
COLLABORATOR_ALLOWED_TOOLS: frozenset[str] = frozenset(
    {
        "read",
        "write",
        "edit",
        "search",
        "grep",
        "glob",
        "web_search",
        "web_fetch",
        "calculator",
        "translate",
        "summarize",
        "draft",
        "calendar_read",  # read-only calendar access
        "notes_read",  # read-only notes
        "slack_send",  # outbound Slack (gated by egress)
        "jira_read",
        "jira_comment",
        "confluence_read",
        "github_read",
        "github_comment",
        "monitoring_read",  # Zabbix/Grafana read-only
        "athena_query",  # data platform read-only
        "s3_read",  # S3 read-only
    }
)


# ---------------------------------------------------------------------------
# C35: Per-Tool Rate Limits
# ---------------------------------------------------------------------------


@dataclass
class ToolRateLimit:
    """Per-tool call rate limit configuration."""

    tool_name: str
    max_calls_per_minute: int
    max_calls_per_hour: int


_DEFAULT_TOOL_RATE_LIMITS: Dict[str, ToolRateLimit] = {
    "execute_command": ToolRateLimit("execute_command", 5, 30),
    "exec": ToolRateLimit("exec", 5, 30),
    "bash": ToolRateLimit("bash", 5, 30),
    "delete_file": ToolRateLimit("delete_file", 3, 15),
    "delete": ToolRateLimit("delete", 3, 15),
    "write_file": ToolRateLimit("write_file", 10, 60),
    "write": ToolRateLimit("write", 10, 60),
}


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


@dataclass
class ToolACLConfig:
    """Policy configuration for tool ACL enforcement.

    Loaded from agentshroud.yaml `tool_acl:` section; defaults match the
    conservative security posture above.
    """

    # Override the built-in sets via YAML config (appended, not replaced)
    extra_private_tools: List[str] = field(default_factory=list)
    extra_admin_tools: List[str] = field(default_factory=list)
    extra_collaborator_allowed: List[str] = field(default_factory=list)

    # Per-group allowlists: group_id → additional tools allowed for that group
    group_tool_allowlists: Dict[str, List[str]] = field(default_factory=dict)

    # When True, unknown tools are denied for non-owner users
    deny_unknown_tools: bool = True

    @property
    def effective_private(self) -> frozenset[str]:
        return PRIVATE_TOOLS | frozenset(self.extra_private_tools)

    @property
    def effective_admin(self) -> frozenset[str]:
        return ADMIN_TOOLS | frozenset(self.extra_admin_tools)

    @property
    def effective_collaborator_allowed(self) -> frozenset[str]:
        return COLLABORATOR_ALLOWED_TOOLS | frozenset(self.extra_collaborator_allowed)


# ---------------------------------------------------------------------------
# Enforcer
# ---------------------------------------------------------------------------


class ToolACLEnforcer:
    """Enforces tool-level access control based on user role and group membership.

    Usage:
        enforcer = ToolACLEnforcer(config, rbac_config)
        allowed, reason = enforcer.can_use_tool(user_id, "gmail")
    """

    def __init__(
        self, acl_config: Optional[ToolACLConfig] = None, rbac_config: Optional["RBACConfig"] = None
    ):
        self._acl = acl_config or ToolACLConfig()
        self._rbac = rbac_config
        # C35: sliding window call-time store  { user_id: { tool_name: [timestamps] } }
        self._tool_call_times: Dict[str, Dict[str, List[float]]] = {}
        # V9-2: per-user denial counter for SOC cross-signal correlation
        self._denial_counts: Dict[str, int] = {}

    def can_use_tool(self, user_id: str, tool_name: str) -> Tuple[bool, str]:
        """Check whether user_id may invoke the named tool.

        Returns:
            (allowed: bool, reason: str)
        """
        tool_lower = tool_name.lower().strip()

        role = self._get_role(user_id)
        role_value = role.value if hasattr(role, "value") else str(role)

        # Owner: unrestricted
        if role_value == "owner":
            return True, "owner has unrestricted tool access"

        # Private tools: owner-only
        if tool_lower in self._acl.effective_private:
            reason = f"tool '{tool_name}' is owner-private and cannot be used by {role_value}"
            logger.warning(
                "ToolACL DENIED private-tier tool: user=%s role=%s tool=%s tier=PRIVATE",
                user_id,
                role_value,
                tool_name,
            )
            self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
            return False, reason

        # Admin+: access to admin tools
        if role_value == "admin":
            if tool_lower in self._acl.effective_admin:
                return True, f"admin has access to admin-tier tool '{tool_name}'"
            # Admins can also use all collaborator-allowed tools + anything not private
            if tool_lower in self._acl.effective_collaborator_allowed:
                return True, "tool in collaborator allowlist"
            if not self._acl.deny_unknown_tools:
                return True, "unknown tool allowed (deny_unknown_tools=False)"
            return True, "admin has broad tool access"

        # Collaborator/Viewer: restricted
        if role_value in ("collaborator", "viewer", "operator"):
            if tool_lower in self._acl.effective_admin:
                reason = f"tool '{tool_name}' requires admin role"
                logger.warning(
                    "ToolACL DENIED admin-tier tool: user=%s role=%s tool=%s tier=ADMIN",
                    user_id,
                    role_value,
                    tool_name,
                )
                self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
                return False, reason

            # Check group allowlist override
            group_allowed = self._get_group_tool_allowlist(user_id)
            if tool_lower in group_allowed:
                return True, f"tool '{tool_name}' allowed by group policy"

            if tool_lower in self._acl.effective_collaborator_allowed:
                return True, "tool in collaborator allowlist"

            if self._acl.deny_unknown_tools:
                reason = (
                    f"tool '{tool_name}' not in collaborator allowlist (deny_unknown_tools=True)"
                )
                logger.warning(
                    "ToolACL DENIED unknown tool: user=%s role=%s tool=%s policy=deny_unknown",
                    user_id,
                    role_value,
                    tool_name,
                )
                self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
                return False, reason

            return True, "unknown tool not denied (deny_unknown_tools=False)"

        # Unknown role: deny
        reason = f"unknown role '{role_value}' — denying by default"
        logger.warning(
            "ToolACL DENIED unknown role: user=%s role=%s tool=%s",
            user_id,
            role_value,
            tool_name,
        )
        self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
        return False, reason

    def get_allowed_tools(self, user_id: str) -> List[str]:
        """Return the list of tools the user is allowed to use (union of all sets)."""
        role = self._get_role(user_id)
        role_value = role.value if hasattr(role, "value") else str(role)

        if role_value == "owner":
            return ["<all tools>"]
        if role_value == "admin":
            return sorted(
                self._acl.effective_collaborator_allowed
                | self._acl.effective_admin
                | self._get_group_tool_allowlist(user_id)
            )

        # collaborator / viewer / operator
        base = self._acl.effective_collaborator_allowed | self._get_group_tool_allowlist(user_id)
        return sorted(base - self._acl.effective_private - self._acl.effective_admin)

    def get_denied_tools(self, user_id: str) -> List[str]:
        """Return tools explicitly denied for this user."""
        role = self._get_role(user_id)
        role_value = role.value if hasattr(role, "value") else str(role)

        if role_value == "owner":
            return []
        if role_value == "admin":
            return sorted(self._acl.effective_private)

        return sorted(self._acl.effective_private | self._acl.effective_admin)

    def get_denial_counts(self) -> Dict[str, int]:
        """Return per-user tool denial counts since last restart (V9-2: SOC correlation)."""
        return dict(self._denial_counts)

    # ── C35: Per-Tool Rate Limiting ───────────────────────────────────────────

    def check_tool_rate_limit(self, user_id: str, tool_name: str) -> bool:
        """Return True if the user is within rate limits for the given tool.

        Side-effect: records the call timestamp on success (returns True).
        """
        limit = _DEFAULT_TOOL_RATE_LIMITS.get(tool_name.lower())
        if limit is None:
            return True  # No limit defined for this tool

        now = time.time()
        user_calls = self._tool_call_times.setdefault(user_id, {})
        times = user_calls.get(tool_name.lower(), [])

        # Drop calls older than 1 hour
        times = [t for t in times if now - t < 3600]

        per_minute = sum(1 for t in times if now - t < 60)
        if per_minute >= limit.max_calls_per_minute or len(times) >= limit.max_calls_per_hour:
            logger.warning(
                "Tool rate limit hit: user=%s tool=%s per_min=%d/%d per_hr=%d/%d",
                user_id,
                tool_name,
                per_minute,
                limit.max_calls_per_minute,
                len(times),
                limit.max_calls_per_hour,
            )
            user_calls[tool_name.lower()] = times
            return False

        times.append(now)
        user_calls[tool_name.lower()] = times
        return True

    # ─────────────────────────────────────────────────────────────────────────

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _get_role(self, user_id: str):
        if self._rbac is None:
            from gateway.security.rbac_config import Role

            return Role.VIEWER
        return self._rbac.get_user_role(user_id)

    def _get_group_tool_allowlist(self, user_id: str) -> frozenset[str]:
        """Collect additional tools granted to the user via their group memberships."""
        extra: set[str] = set()

        # Per-group YAML overrides
        if self._rbac is not None:
            teams = getattr(self._rbac, "teams_config", None)
            if teams is not None:
                for gid, group in teams.groups.items():
                    if user_id in group.members:
                        group_list = self._acl.group_tool_allowlists.get(gid, [])
                        extra.update(group_list)
                        # Also respect ProjectConfig.allowed_tools
                        for pid in group.projects:
                            proj = teams.projects.get(pid)
                            if proj:
                                extra.update(proj.allowed_tools)

        return frozenset(extra)
