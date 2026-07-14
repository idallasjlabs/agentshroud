# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MCP (Model Context Protocol) security policy engine (SCRUM-84).

The enforcement half of the "Integration hub" epic. Given a
(mcp_server, tool_name, agent/context, args) tuple, this engine returns an
allow / deny / require-approval decision from a configurable policy:

  - Server allowlist / denylist (deny always wins over allow).
  - Per-tool hard denylist (never invocable by anyone, including the owner).
  - Per-tool risk tiers (low / medium / high / critical). Tools whose tier is in
    ``high_risk_actions`` route through the human-in-the-loop approval queue.
  - Default-DENY posture: an unknown server, or a server absent from the
    allowlist, is denied. This is deliberately the inverse of the transparent,
    default-allow ``MCPPermissionManager`` (gateway/proxy/mcp_permissions.py):
    this engine is the explicit governance gate, not the passthrough layer.

Design notes
------------
* Composes with, does not replace, ``ToolACLEnforcer`` and
  ``MCPPermissionManager``. The proxy runs this engine first as a hard gate;
  the existing permission / inspection / egress layers still apply afterward.
* Config is loaded from the ``mcp_policy:`` YAML section via
  :meth:`MCPPolicyConfig.from_dict`, mirroring ``MCPProxyConfig.from_dict``.
* ``evaluate`` is pure (no I/O, no await) so it is trivially unit-testable and
  cheap enough to sit on the hot path. ``enforce`` wraps it with the async
  approval-queue round-trip.

IEC 62443 alignment: FR3 (SL3) — per-identity, per-resource access control at
every MCP tool-call boundary; deny-by-default with an explicit allowlist.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger("agentshroud.security.mcp_policy")


# ---------------------------------------------------------------------------
# Decision types
# ---------------------------------------------------------------------------


class MCPPolicyAction(str, Enum):
    """The three terminal policy outcomes for an MCP tool call."""

    ALLOW = "allow"
    DENY = "deny"
    REQUIRE_APPROVAL = "require_approval"


@dataclass
class MCPPolicyDecision:
    """The result of evaluating a single MCP tool call against the policy."""

    action: MCPPolicyAction
    server: str
    tool: str
    reason: str = ""
    risk_tier: str = "low"
    matched_rule: str = ""

    @property
    def allowed(self) -> bool:
        """True only for a terminal ALLOW.

        REQUIRE_APPROVAL is *not* allowed on its own — the call is pending a
        human decision. ``enforce`` resolves it to ALLOW/DENY.
        """
        return self.action is MCPPolicyAction.ALLOW


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


# Baseline high-risk MCP tool substrings. A tool whose (bare) name matches one
# of these is treated as high-risk even if the operator did not classify it,
# so a newly-added destructive tool is not silently low-risk. These are
# conservative, destructive/exfiltration verbs — never a blanket match.
_DEFAULT_HIGH_RISK_KEYWORDS: frozenset[str] = frozenset(
    {
        "delete",
        "destroy",
        "drop",
        "truncate",
        "rm_rf",
        "rmrf",
        "wipe",
        "purge",
        "exec",
        "execute_command",
        "run_command",
        "shell",
        "sudo",
        "transfer_ownership",
        "grant_admin",
        "rotate_key",
        "exfiltrate",
    }
)


@dataclass
class MCPPolicyConfig:
    """Declarative MCP security policy.

    Loaded from the ``mcp_policy:`` section of agentshroud.yaml via
    :meth:`from_dict`. Empty config → deny everything (fail closed).
    """

    # Terminal action for a server that is neither allow- nor deny-listed and
    # matches no other rule. "deny" by design; may be relaxed to "allow" only
    # by explicit operator opt-in.
    default_action: MCPPolicyAction = MCPPolicyAction.DENY

    # Servers explicitly permitted. Empty allowlist + default_action=deny means
    # nothing is allowed (locked down).
    allowed_servers: List[str] = field(default_factory=list)
    # Servers explicitly forbidden. Deny always wins over allow.
    denied_servers: List[str] = field(default_factory=list)

    # Hard tool denylist. Entries may be qualified ("server:tool") or bare
    # ("tool" → any server). Never invocable, not even by the owner.
    denied_tools: List[str] = field(default_factory=list)

    # Per-tier tool classifications: tier name → list of tool refs
    # ("server:tool" or bare "tool").
    risk_tiers: Dict[str, List[str]] = field(default_factory=dict)

    # Tiers that must route through the approval queue.
    high_risk_actions: List[str] = field(default_factory=lambda: ["high", "critical"])

    # Additional substrings that mark a tool high-risk (merged with the
    # conservative built-in defaults).
    extra_high_risk_keywords: List[str] = field(default_factory=list)

    # When True, the owner skips the approval gate for high-risk tools (but is
    # still subject to hard denies).
    owner_bypass: bool = False
    owner_user_id: str = ""

    # ---- normalized lookup tables (built in __post_init__) ----
    _allowed: frozenset[str] = field(default_factory=frozenset, init=False, repr=False)
    _denied_servers: frozenset[str] = field(default_factory=frozenset, init=False, repr=False)
    _denied_tools: frozenset[str] = field(default_factory=frozenset, init=False, repr=False)
    _tool_tier: Dict[str, str] = field(default_factory=dict, init=False, repr=False)
    _high_risk_keywords: frozenset[str] = field(default_factory=frozenset, init=False, repr=False)

    def __post_init__(self) -> None:
        self._allowed = frozenset(_norm(s) for s in self.allowed_servers)
        self._denied_servers = frozenset(_norm(s) for s in self.denied_servers)
        self._denied_tools = frozenset(_norm(t) for t in self.denied_tools)
        # Tool → tier map (last tier wins for a duplicate ref, which is fine —
        # config authors should not double-classify).
        tier_map: Dict[str, str] = {}
        for tier, tools in self.risk_tiers.items():
            for tool_ref in tools:
                tier_map[_norm(tool_ref)] = tier.lower()
        self._tool_tier = tier_map
        self._high_risk_keywords = _DEFAULT_HIGH_RISK_KEYWORDS | frozenset(
            _norm(k) for k in self.extra_high_risk_keywords
        )

    @classmethod
    def from_dict(cls, data: Optional[Dict[str, Any]]) -> "MCPPolicyConfig":
        """Parse a policy config from a plain dict (e.g. loaded from YAML)."""
        data = data or {}
        default_raw = str(data.get("default_action", "deny")).lower()
        try:
            default_action = MCPPolicyAction(default_raw)
        except ValueError:
            logger.warning(
                "Invalid mcp_policy.default_action=%r — falling back to deny", default_raw
            )
            default_action = MCPPolicyAction.DENY
        return cls(
            default_action=default_action,
            allowed_servers=list(data.get("allowed_servers", [])),
            denied_servers=list(data.get("denied_servers", [])),
            denied_tools=list(data.get("denied_tools", [])),
            risk_tiers={k: list(v) for k, v in dict(data.get("risk_tiers", {})).items()},
            high_risk_actions=list(data.get("high_risk_actions", ["high", "critical"])),
            extra_high_risk_keywords=list(data.get("extra_high_risk_keywords", [])),
            owner_bypass=bool(data.get("owner_bypass", False)),
            owner_user_id=str(data.get("owner_user_id", "") or ""),
        )


def _norm(value: str) -> str:
    """Normalize a server/tool reference for case-insensitive matching."""
    return str(value).strip().lower()


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------


class MCPPolicyEngine:
    """Decides allow / deny / require-approval for MCP tool calls.

    Usage::

        engine = MCPPolicyEngine(config, approval_queue=queue)
        decision = engine.evaluate("github", "delete_repo", agent_id="a")
        # or, resolving the approval round-trip:
        decision = await engine.enforce("github", "delete_repo", agent_id="a", args={})
    """

    def __init__(
        self,
        config: Optional[MCPPolicyConfig] = None,
        approval_queue=None,
    ):
        self._cfg = config or MCPPolicyConfig()
        # EnhancedApprovalQueue (duck-typed: submit_tool_request + wait_for_decision).
        self._approval_queue = approval_queue

    # ---- pure decision ----------------------------------------------------

    def evaluate(
        self,
        mcp_server: str,
        tool_name: str,
        agent_id: str = "default",
        args: Optional[Dict[str, Any]] = None,
    ) -> MCPPolicyDecision:
        """Evaluate a single MCP tool call. Pure — no I/O, no side effects
        beyond best-effort SOC heat-map telemetry.

        Precedence (first match wins):
          1. Hard tool denylist  → DENY (not bypassable, even by owner).
          2. Server denylist     → DENY (deny wins over allow).
          3. Server not allowlisted (under default-deny) → DENY.
          4. High-risk tier tool → REQUIRE_APPROVAL (owner may bypass → ALLOW).
          5. Otherwise           → ALLOW.
        """
        server = _norm(mcp_server)
        tool = _norm(tool_name)
        qualified = f"{server}:{tool}"

        decision = self._decide(server, tool, qualified, agent_id)

        # SOC module heat-map (SCRUM-80): REQUIRE_APPROVAL counts as a block
        # since the call is not permitted to proceed on its own.
        try:
            from gateway.security.module_stats import record_decision

            record_decision("mcp_policy", decision.action is MCPPolicyAction.ALLOW)
        except Exception:  # pragma: no cover - telemetry must never raise
            pass

        if decision.action is not MCPPolicyAction.ALLOW:
            logger.warning(
                "MCP policy %s: agent=%s server=%s tool=%s tier=%s rule=%s",
                decision.action.value,
                agent_id,
                mcp_server,
                tool_name,
                decision.risk_tier,
                decision.matched_rule,
            )
        return decision

    def _decide(self, server: str, tool: str, qualified: str, agent_id: str) -> MCPPolicyDecision:
        cfg = self._cfg

        # 1. Hard tool denylist — qualified or bare. Never bypassable.
        if qualified in cfg._denied_tools or tool in cfg._denied_tools:
            return MCPPolicyDecision(
                action=MCPPolicyAction.DENY,
                server=server,
                tool=tool,
                reason=f"tool '{qualified}' is on the MCP tool denylist",
                risk_tier=self._tier_for(server, tool, qualified),
                matched_rule="tool_denylist",
            )

        # 2. Server denylist — deny wins over allow.
        if server in cfg._denied_servers:
            return MCPPolicyDecision(
                action=MCPPolicyAction.DENY,
                server=server,
                tool=tool,
                reason=f"MCP server '{server}' is on the server denylist",
                risk_tier=self._tier_for(server, tool, qualified),
                matched_rule="server_denylist",
            )

        # 3. Allowlist / default action.
        if server not in cfg._allowed:
            if cfg.default_action is MCPPolicyAction.ALLOW:
                # Operator explicitly opted into default-allow; fall through to
                # the risk-tier check below.
                pass
            else:
                return MCPPolicyDecision(
                    action=MCPPolicyAction.DENY,
                    server=server,
                    tool=tool,
                    reason=(
                        f"MCP server '{server}' is not in the allowlist " f"(default-deny posture)"
                    ),
                    risk_tier=self._tier_for(server, tool, qualified),
                    matched_rule="default_deny",
                )

        # 4. Risk tier → approval gate.
        tier = self._tier_for(server, tool, qualified)
        if tier in {t.lower() for t in cfg.high_risk_actions}:
            # Owner may bypass the approval gate (but not hard denies above).
            if cfg.owner_bypass and cfg.owner_user_id and str(agent_id) == str(cfg.owner_user_id):
                return MCPPolicyDecision(
                    action=MCPPolicyAction.ALLOW,
                    server=server,
                    tool=tool,
                    reason=f"owner bypass for high-risk tool '{qualified}'",
                    risk_tier=tier,
                    matched_rule="owner_bypass",
                )
            return MCPPolicyDecision(
                action=MCPPolicyAction.REQUIRE_APPROVAL,
                server=server,
                tool=tool,
                reason=(f"tool '{qualified}' is {tier}-risk and requires human approval"),
                risk_tier=tier,
                matched_rule="risk_tier",
            )

        # 5. Allowlisted + safe tool → allow.
        return MCPPolicyDecision(
            action=MCPPolicyAction.ALLOW,
            server=server,
            tool=tool,
            reason=f"server '{server}' allowlisted; tool '{tool}' is {tier}-risk",
            risk_tier=tier,
            matched_rule="allowlist",
        )

    def _tier_for(self, server: str, tool: str, qualified: str) -> str:
        """Resolve the risk tier for a tool.

        Explicit classification (qualified beats bare) wins; otherwise a
        conservative keyword heuristic marks obviously-destructive tools
        high-risk; otherwise low.
        """
        cfg = self._cfg
        if qualified in cfg._tool_tier:
            return cfg._tool_tier[qualified]
        if tool in cfg._tool_tier:
            return cfg._tool_tier[tool]
        for keyword in cfg._high_risk_keywords:
            if keyword in tool:
                return "high"
        return "low"

    # ---- async enforcement (approval-queue round-trip) --------------------

    async def enforce(
        self,
        mcp_server: str,
        tool_name: str,
        agent_id: str = "default",
        args: Optional[Dict[str, Any]] = None,
    ) -> MCPPolicyDecision:
        """Evaluate and resolve the decision to a terminal ALLOW/DENY.

        For REQUIRE_APPROVAL, this actually enqueues an approval request through
        the wired approval queue and waits for the human decision, returning
        ALLOW on approval and DENY on rejection. Fails CLOSED (DENY) if no
        approval queue is configured — a high-risk tool is never silently run.
        """
        args = args or {}
        decision = self.evaluate(mcp_server, tool_name, agent_id=agent_id, args=args)

        if decision.action is not MCPPolicyAction.REQUIRE_APPROVAL:
            return decision

        server = _norm(mcp_server)
        tool = _norm(tool_name)
        qualified = f"{server}:{tool}"

        if self._approval_queue is None:
            # Fail closed: cannot obtain human approval → deny.
            logger.warning(
                "MCP policy DENY (fail-closed): high-risk tool '%s' but no approval "
                "queue configured (agent=%s)",
                qualified,
                agent_id,
            )
            return MCPPolicyDecision(
                action=MCPPolicyAction.DENY,
                server=server,
                tool=tool,
                reason=(
                    f"tool '{qualified}' requires approval but no approval queue "
                    f"is configured — denied (fail-closed)"
                ),
                risk_tier=decision.risk_tier,
                matched_rule="approval_unavailable",
            )

        # Enqueue through the human-in-the-loop approval queue. The queue keys
        # its own risk policy off the qualified "server:tool" name.
        request_id, requires_wait = await self._approval_queue.submit_tool_request(
            qualified, args, agent_id
        )
        if not requires_wait:
            # Queue determined no approval is actually required for this tool.
            return MCPPolicyDecision(
                action=MCPPolicyAction.ALLOW,
                server=server,
                tool=tool,
                reason=f"approval queue permitted '{qualified}' without wait",
                risk_tier=decision.risk_tier,
                matched_rule="approval_not_required",
            )

        approved = await self._approval_queue.wait_for_decision(request_id)
        if approved:
            return MCPPolicyDecision(
                action=MCPPolicyAction.ALLOW,
                server=server,
                tool=tool,
                reason=f"human operator approved '{qualified}' (request {request_id})",
                risk_tier=decision.risk_tier,
                matched_rule="approved",
            )
        return MCPPolicyDecision(
            action=MCPPolicyAction.DENY,
            server=server,
            tool=tool,
            reason=(
                f"tool '{qualified}' was denied by the human operator " f"(request {request_id})"
            ),
            risk_tier=decision.risk_tier,
            matched_rule="rejected",
        )
