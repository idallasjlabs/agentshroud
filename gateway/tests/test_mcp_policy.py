# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the MCP (Model Context Protocol) security policy engine (SCRUM-84).

Covers the enforcement half of the "Integration hub" epic: a per-(server, tool)
allow / deny / require-approval decision engine with a default-deny posture,
composed with the existing MCPProxy dispatch point.

No network, no real subprocess — the approval queue and MCP server execution are
mocked. Deterministic fixtures only.
"""

from __future__ import annotations

import asyncio

import pytest

from gateway.security.mcp_policy import (
    MCPPolicyAction,
    MCPPolicyConfig,
    MCPPolicyEngine,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _base_config() -> MCPPolicyConfig:
    """A representative policy: two allowlisted servers, one denylisted server,
    a per-server denied tool, and explicit high-risk / critical tool tiers."""
    return MCPPolicyConfig.from_dict(
        {
            "default_action": "deny",
            "allowed_servers": ["github", "filesystem"],
            "denied_servers": ["shady_server"],
            "denied_tools": ["filesystem:delete_all"],
            "risk_tiers": {
                "high": ["github:delete_repo", "filesystem:write_file"],
                "critical": ["github:transfer_ownership"],
            },
            "high_risk_actions": ["high", "critical"],
        }
    )


@pytest.fixture()
def engine() -> MCPPolicyEngine:
    return MCPPolicyEngine(_base_config())


# ---------------------------------------------------------------------------
# evaluate(): pure decision logic
# ---------------------------------------------------------------------------


def test_allowlisted_server_safe_tool_is_allowed(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("github", "list_issues", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.ALLOW
    assert decision.allowed is True
    assert decision.server == "github"
    assert decision.tool == "list_issues"
    assert decision.risk_tier == "low"


def test_unknown_server_is_denied_by_default(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("mystery_server", "read", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.DENY
    assert decision.allowed is False
    assert "not in the allowlist" in decision.reason


def test_denylisted_server_is_denied_even_if_tool_safe(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("shady_server", "list_things", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.DENY
    assert decision.allowed is False
    assert "denylist" in decision.reason


def test_denylisted_tool_is_denied(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("filesystem", "delete_all", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.DENY
    assert decision.allowed is False
    assert "tool denylist" in decision.reason


def test_high_risk_tool_requires_approval(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("github", "delete_repo", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.REQUIRE_APPROVAL
    assert decision.allowed is False  # not allowed until approved
    assert decision.risk_tier == "high"


def test_critical_tool_requires_approval(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("github", "transfer_ownership", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.REQUIRE_APPROVAL
    assert decision.risk_tier == "critical"


def test_default_deny_posture_when_no_config() -> None:
    """An empty config denies everything — never a blanket allow."""
    empty = MCPPolicyEngine(MCPPolicyConfig())
    decision = empty.evaluate("anything", "anything", agent_id="agent-1")
    assert decision.action is MCPPolicyAction.DENY
    assert decision.allowed is False


def test_denylist_wins_over_allowlist() -> None:
    """A server both allowed and denied is denied (deny wins)."""
    cfg = MCPPolicyConfig.from_dict(
        {
            "allowed_servers": ["dup"],
            "denied_servers": ["dup"],
        }
    )
    decision = MCPPolicyEngine(cfg).evaluate("dup", "tool", agent_id="a")
    assert decision.action is MCPPolicyAction.DENY
    assert "denylist" in decision.reason


def test_server_and_tool_matching_is_case_insensitive(engine: MCPPolicyEngine) -> None:
    decision = engine.evaluate("GitHub", "List_Issues", agent_id="a")
    assert decision.action is MCPPolicyAction.ALLOW


def test_denied_tool_can_be_specified_bare_or_qualified() -> None:
    cfg = MCPPolicyConfig.from_dict(
        {
            "allowed_servers": ["fs"],
            "denied_tools": ["rm_rf"],  # bare tool name → any server
        }
    )
    decision = MCPPolicyEngine(cfg).evaluate("fs", "rm_rf", agent_id="a")
    assert decision.action is MCPPolicyAction.DENY


def test_owner_bypasses_approval_but_not_hard_deny() -> None:
    """Owner skips the approval gate for high-risk tools, but a denylisted
    tool is still denied for everyone (hard deny is not bypassable)."""
    cfg = MCPPolicyConfig.from_dict(
        {
            "allowed_servers": ["github"],
            "denied_tools": ["github:nuke"],
            "risk_tiers": {"high": ["github:delete_repo"]},
            "high_risk_actions": ["high"],
            "owner_bypass": True,
            "owner_user_id": "owner-1",
        }
    )
    eng = MCPPolicyEngine(cfg)
    # Owner + high-risk → allowed (bypass approval)
    d1 = eng.evaluate("github", "delete_repo", agent_id="owner-1")
    assert d1.action is MCPPolicyAction.ALLOW
    # Non-owner + high-risk → approval
    d2 = eng.evaluate("github", "delete_repo", agent_id="agent-x")
    assert d2.action is MCPPolicyAction.REQUIRE_APPROVAL
    # Owner + hard-denied tool → still denied
    d3 = eng.evaluate("github", "nuke", agent_id="owner-1")
    assert d3.action is MCPPolicyAction.DENY


def test_invalid_default_action_falls_back_to_deny() -> None:
    """A malformed default_action in YAML must not fail open — it becomes deny."""
    cfg = MCPPolicyConfig.from_dict({"default_action": "bogus", "allowed_servers": []})
    assert cfg.default_action is MCPPolicyAction.DENY
    decision = MCPPolicyEngine(cfg).evaluate("x", "y", agent_id="a")
    assert decision.action is MCPPolicyAction.DENY


def test_default_allow_opt_in_permits_non_allowlisted_safe_tool() -> None:
    """When an operator explicitly opts into default-allow, a non-allowlisted
    server with a safe tool is permitted, but denylists still apply and
    high-risk tools still require approval."""
    cfg = MCPPolicyConfig.from_dict(
        {
            "default_action": "allow",
            "denied_servers": ["evil"],
            "risk_tiers": {"high": ["any:delete_repo"]},
            "high_risk_actions": ["high"],
        }
    )
    eng = MCPPolicyEngine(cfg)
    # Non-allowlisted safe tool → allowed under default-allow opt-in.
    assert eng.evaluate("random", "read", agent_id="a").action is MCPPolicyAction.ALLOW
    # Denylist still wins.
    assert eng.evaluate("evil", "read", agent_id="a").action is MCPPolicyAction.DENY
    # High-risk tool still gated even under default-allow.
    assert (
        eng.evaluate("random", "delete_repo", agent_id="a").action
        is MCPPolicyAction.REQUIRE_APPROVAL
    )


def test_bare_tool_name_risk_tier_applies_across_servers() -> None:
    """A risk tier declared with a bare tool name applies on any allowlisted
    server (not just a single qualified server:tool)."""
    cfg = MCPPolicyConfig.from_dict(
        {
            "allowed_servers": ["srv_a", "srv_b"],
            "risk_tiers": {"high": ["publish"]},  # bare name → any server
            "high_risk_actions": ["high"],
        }
    )
    eng = MCPPolicyEngine(cfg)
    assert eng.evaluate("srv_a", "publish", agent_id="a").risk_tier == "high"
    assert eng.evaluate("srv_b", "publish", agent_id="a").action is MCPPolicyAction.REQUIRE_APPROVAL


def test_keyword_heuristic_auto_classifies_unlisted_destructive_tool() -> None:
    """A destructive tool the operator forgot to classify is still caught as
    high-risk by the conservative keyword heuristic."""
    cfg = MCPPolicyConfig.from_dict({"allowed_servers": ["fs"]})
    decision = MCPPolicyEngine(cfg).evaluate("fs", "delete_everything", agent_id="a")
    assert decision.action is MCPPolicyAction.REQUIRE_APPROVAL
    assert decision.risk_tier == "high"


def test_decision_records_soc_heatmap(monkeypatch: pytest.MonkeyPatch) -> None:
    """evaluate() records the decision for the SOC module heat-map."""
    calls: list[tuple[str, bool]] = []

    def _fake_record(module: str, allowed: bool, sanitized: bool = False) -> None:
        calls.append((module, allowed))

    monkeypatch.setattr("gateway.security.module_stats.record_decision", _fake_record, raising=True)
    eng = MCPPolicyEngine(_base_config())
    eng.evaluate("github", "list_issues", agent_id="a")
    eng.evaluate("mystery", "x", agent_id="a")
    assert ("mcp_policy", True) in calls
    assert ("mcp_policy", False) in calls


# ---------------------------------------------------------------------------
# enforce(): async decision + approval-queue wiring
# ---------------------------------------------------------------------------


class _FakeApprovalQueue:
    """Minimal stand-in for EnhancedApprovalQueue.

    Records submissions and returns a scripted approval outcome.
    """

    def __init__(self, approve: bool = True, requires_wait: bool = True):
        self.approve = approve
        self.requires_wait = requires_wait
        self.submitted: list[tuple[str, dict, str]] = []
        self.waited: list[str] = []

    async def submit_tool_request(self, tool_name, parameters, agent_id="default"):
        self.submitted.append((tool_name, parameters, agent_id))
        if not self.requires_wait:
            return "", False
        return "req-123", True

    async def wait_for_decision(self, request_id, timeout: float = 300) -> bool:
        self.waited.append(request_id)
        return self.approve


def test_enforce_allows_allowlisted_safe_tool() -> None:
    eng = MCPPolicyEngine(_base_config())
    decision = asyncio.run(eng.enforce("github", "list_issues", agent_id="a", args={}))
    assert decision.allowed is True
    assert decision.action is MCPPolicyAction.ALLOW


def test_enforce_blocks_unknown_server() -> None:
    eng = MCPPolicyEngine(_base_config())
    decision = asyncio.run(eng.enforce("unknown", "x", agent_id="a", args={}))
    assert decision.allowed is False
    assert decision.action is MCPPolicyAction.DENY


def test_enforce_high_risk_enqueues_and_allows_on_approval() -> None:
    q = _FakeApprovalQueue(approve=True)
    eng = MCPPolicyEngine(_base_config(), approval_queue=q)
    decision = asyncio.run(eng.enforce("github", "delete_repo", agent_id="a", args={"repo": "x"}))
    # The approval request was actually enqueued through the queue.
    assert len(q.submitted) == 1
    submitted_tool, submitted_args, submitted_agent = q.submitted[0]
    assert submitted_tool == "github:delete_repo"
    assert submitted_args == {"repo": "x"}
    assert submitted_agent == "a"
    assert q.waited == ["req-123"]
    # Approved → allowed.
    assert decision.allowed is True
    assert decision.action is MCPPolicyAction.ALLOW


def test_enforce_high_risk_denied_on_rejection() -> None:
    q = _FakeApprovalQueue(approve=False)
    eng = MCPPolicyEngine(_base_config(), approval_queue=q)
    decision = asyncio.run(eng.enforce("github", "delete_repo", agent_id="a", args={}))
    assert len(q.submitted) == 1
    assert decision.allowed is False
    assert decision.action is MCPPolicyAction.DENY
    assert "denied" in decision.reason.lower()


def test_enforce_high_risk_without_queue_denies_closed() -> None:
    """Fail-closed: a high-risk tool with no approval queue wired is denied,
    never silently allowed."""
    eng = MCPPolicyEngine(_base_config(), approval_queue=None)
    decision = asyncio.run(eng.enforce("github", "delete_repo", agent_id="a", args={}))
    assert decision.allowed is False
    assert decision.action is MCPPolicyAction.DENY


def test_enforce_high_risk_queue_no_wait_allows() -> None:
    """If the queue decides the tool doesn't actually need approval
    (requires_wait False), the call proceeds."""
    q = _FakeApprovalQueue(requires_wait=False)
    eng = MCPPolicyEngine(_base_config(), approval_queue=q)
    decision = asyncio.run(eng.enforce("github", "delete_repo", agent_id="a", args={}))
    assert decision.allowed is True
    assert decision.action is MCPPolicyAction.ALLOW


# ---------------------------------------------------------------------------
# Integration: MCPProxy blocks a denied MCP tool call end-to-end
# ---------------------------------------------------------------------------


def test_mcp_proxy_blocks_policy_denied_call() -> None:
    """The engine wired into MCPProxy blocks a denied call before dispatch —
    the fake MCP server is never contacted."""
    from gateway.proxy.mcp_proxy import MCPProxy, MCPToolCall

    engine = MCPPolicyEngine(_base_config())
    proxy = MCPProxy(policy_engine=engine)

    executed: list[str] = []

    async def _boom(*_a, **_k):  # pragma: no cover - must never run
        executed.append("executed")
        raise AssertionError("denied call reached the MCP server")

    proxy._execute_tool_call = _boom  # type: ignore[assignment]

    call = MCPToolCall(
        id="c1",
        server_name="unknown_server",
        tool_name="read",
        parameters={},
        agent_id="agent-1",
    )
    result = asyncio.run(proxy.process_tool_call(call, execute=True))
    assert result.allowed is False
    assert result.blocked is True
    assert "MCP policy" in result.block_reason
    assert executed == []


def test_mcp_proxy_allows_policy_permitted_call() -> None:
    """A policy-permitted call passes the policy gate (inspection/permission
    layers still apply, but the policy engine does not block it)."""
    from gateway.proxy.mcp_proxy import MCPProxy, MCPToolCall, MCPToolResult

    engine = MCPPolicyEngine(_base_config())
    proxy = MCPProxy(policy_engine=engine)

    async def _ok(tool_call, sanitized_params=None):
        return MCPToolResult(
            call_id=tool_call.id,
            server_name=tool_call.server_name,
            tool_name=tool_call.tool_name,
            content={"ok": True},
        )

    proxy._execute_tool_call = _ok  # type: ignore[assignment]

    call = MCPToolCall(
        id="c2",
        server_name="github",
        tool_name="list_issues",
        parameters={},
        agent_id="agent-1",
    )
    result = asyncio.run(proxy.process_tool_call(call, execute=True))
    assert result.allowed is True
    assert result.blocked is False
