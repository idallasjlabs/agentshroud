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
    from gateway.security.group_rbac import GroupRoleResolver  # type: ignore[import]  # noqa: F401
    from gateway.security.rbac_config import RBACConfig

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
        # Terminal access (CVE-2026-9367 — command injection bypass via terminal_tool)
        "terminal_tool",
        "terminal",
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
        self,
        acl_config: Optional[ToolACLConfig] = None,
        rbac_config: Optional["RBACConfig"] = None,
        trust_manager=None,
    ):
        self._acl = acl_config or ToolACLConfig()
        self._rbac = rbac_config
        # Optional TrustManager with a progressive trust ladder: consulted as an
        # additional deny gate (deny wins) for tools the ladder knows about.
        self._trust_manager = trust_manager
        # C35: sliding window call-time store  { user_id: { tool_name: [timestamps] } }
        self._tool_call_times: Dict[str, Dict[str, List[float]]] = {}
        # V9-2: per-user denial counter for SOC cross-signal correlation
        self._denial_counts: Dict[str, int] = {}
        # Monitor-mode (SCRUM-78) would-have-denied counts, per user — lets an
        # operator size the enforcement blast radius before flipping to enforce.
        self._monitor_would_deny_counts: Dict[str, int] = {}

    def can_use_tool(self, user_id: str, tool_name: str) -> Tuple[bool, str]:
        """Public entry — records the decision for the SOC heat-map (SCRUM-80),
        then delegates.  Counted once per call.  Honest coverage gap: only the
        group-context fall-through (step 7) reaches here; a group check's
        earlier owner/private/high-risk short-circuits return directly and are
        NOT yet counted."""
        allowed, reason = self._can_use_tool_impl(user_id, tool_name)
        try:
            from gateway.security.module_stats import record_decision

            record_decision("tool_acl", allowed)
        except Exception:
            pass
        return allowed, reason

    def _can_use_tool_impl(self, user_id: str, tool_name: str) -> Tuple[bool, str]:
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

        # Progressive trust ladder: deny wins over any ACL allow below. The
        # ladder only rules on identities it tracks and tools in its vocabulary
        # (is_tool_allowed returns None otherwise), so unrelated tools and
        # untracked users fall through to the role-based ACL unchanged.
        if self._trust_manager is not None:
            try:
                verdict = self._trust_manager.is_tool_allowed(user_id, tool_lower)
            except Exception:
                verdict = None
            if verdict is False:
                reason = f"tool '{tool_name}' requires a higher trust level for {user_id}"
                # Monitor mode (SCRUM-78): log the would-be denial and fall
                # through to the role-based ACL instead of blocking, so a new
                # or expanded ladder vocabulary can be measured before it
                # starts denying — and flipped back instantly if it misfires.
                _cfg = getattr(self._trust_manager, "progressive_config", None)
                _mode = getattr(_cfg, "enforcement_mode", "enforce")
                if _mode == "monitor":
                    logger.warning(
                        "ToolACL MONITOR (would-deny) by trust ladder: " "user=%s role=%s tool=%s",
                        user_id,
                        role_value,
                        tool_name,
                    )
                    self._monitor_would_deny_counts[user_id] = (
                        self._monitor_would_deny_counts.get(user_id, 0) + 1
                    )
                else:
                    logger.warning(
                        "ToolACL DENIED by trust ladder: user=%s role=%s tool=%s",
                        user_id,
                        role_value,
                        tool_name,
                    )
                    self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
                    return False, reason

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

    def can_use_tool_in_group_context(
        self,
        user_id: str,
        tool_name: str,
        group_chat_id: str,
        group_role_resolver: "GroupRoleResolver",  # noqa: F821 — resolved at runtime
    ) -> Tuple[bool, str]:
        """Check whether user_id may invoke tool_name when acting inside a group workspace.

        Resolution order:
          1. If user is the system owner (RBACConfig.owner_user_id) → unrestricted.
          2. Resolve the per-group role via group_role_resolver.get_role().
          3. OWNER group-role → unrestricted (same as system owner for this group).
          4. Any group role → deny private tools outright (owner-only tier).
          5. READ_ONLY group-role → deny high-risk tools outright.
          6. MEMBER group-role → allow high-risk tools but flag as approval-required.
          7. Fall through to standard can_use_tool() for remaining checks.

        Args:
            user_id: Telegram user ID of the requesting member.
            tool_name: Name of the tool being invoked.
            group_chat_id: Telegram chat_id of the active group workspace.
            group_role_resolver: GroupRoleResolver instance with per-group role maps.

        Returns:
            (allowed: bool, reason: str)

        IEC 62443 FR3 (SL3): per-identity access control at every tool call boundary.
        """
        from gateway.security.group_rbac import GroupRole  # type: ignore[import]  # noqa: F811

        tool_lower = tool_name.lower().strip()

        # Step 1: System owner is always unrestricted.
        if self._rbac is not None and self._rbac.is_owner(user_id):
            return True, "owner has unrestricted tool access"

        # Step 2: Resolve per-group role.
        group_role = group_role_resolver.get_role(group_chat_id, user_id)

        # Step 3: Group owner-role → unrestricted within the group.
        if group_role == GroupRole.OWNER:
            return True, "group owner has unrestricted tool access"

        # Step 4: Private tools are owner-only regardless of group role.
        if tool_lower in self._acl.effective_private:
            reason = (
                f"tool '{tool_name}' is owner-private; "
                f"group role '{group_role.value}' cannot use it"
            )
            logger.warning(
                "ToolACL DENIED private-tier tool in group context: "
                "user=%s group_role=%s tool=%s tier=PRIVATE group=%s",
                user_id,
                group_role.value,
                tool_name,
                group_chat_id,
            )
            self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
            return False, reason

        # Step 5: Read-only members are denied high-risk tools outright.
        if group_role == GroupRole.READ_ONLY and group_role_resolver.is_high_risk_tool(tool_lower):
            reason = (
                f"tool '{tool_name}' is high-risk; " f"read-only group members cannot invoke it"
            )
            logger.warning(
                "ToolACL DENIED high-risk tool for read-only member: "
                "user=%s group_role=%s tool=%s group=%s",
                user_id,
                group_role.value,
                tool_name,
                group_chat_id,
            )
            self._denial_counts[user_id] = self._denial_counts.get(user_id, 0) + 1
            return False, reason

        # Step 6: Member role with a high-risk tool → allowed but requires approval queue.
        if group_role == GroupRole.MEMBER and group_role_resolver.is_high_risk_tool(tool_lower):
            logger.info(
                "ToolACL ALLOWED high-risk tool for group member (approval required): "
                "user=%s group_role=%s tool=%s group=%s",
                user_id,
                group_role.value,
                tool_name,
                group_chat_id,
            )
            return True, f"group member may request '{tool_name}' — approval required"

        # Step 7: Fall through to standard RBAC check for remaining cases.
        return self.can_use_tool(user_id, tool_name)

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
