# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the A2A (Agent-to-Agent) security policy engine (SCRUM-129).

Governance for Hermes v0.20.0+'s inbound A2A protocol surface (real Google/Linux
Foundation A2A v1.0.1, JSON-RPC 2.0 over HTTP). Mirrors gateway/security/
mcp_policy.py's evaluate()/enforce() shape and default-deny posture, extended
with A2A-specific task-ownership tracking and a hardened push-notification
callback-URL validator (independent SSRF mitigation for upstream gap #78298).

No network, no real subprocess — the approval queue is mocked. Deterministic
fixtures only.
"""

from __future__ import annotations

import socket
from unittest.mock import patch

import pytest

from gateway.security.a2a_policy import (
    A2AMethod,
    A2APolicyAction,
    A2APolicyConfig,
    A2APolicyDecision,
    A2APolicyEngine,
    is_safe_a2a_callback_url,
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _base_config() -> A2APolicyConfig:
    """Two allowlisted peers, one denylisted peer, default-deny for everyone else."""
    return A2APolicyConfig.from_dict(
        {
            "default_action": "deny",
            "allowed_peers": ["alice", "bob"],
            "denied_peers": ["mallory"],
        }
    )


@pytest.fixture()
def engine() -> A2APolicyEngine:
    return A2APolicyEngine(_base_config())


# ---------------------------------------------------------------------------
# evaluate(): pure decision logic — peer allow/deny
# ---------------------------------------------------------------------------


def test_allowlisted_peer_low_risk_method_is_allowed(engine: A2APolicyEngine) -> None:
    decision = engine.evaluate("alice", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.allowed is True
    assert decision.peer_id == "alice"
    assert decision.risk_tier == "low"


def test_unknown_peer_is_denied_by_default(engine: A2APolicyEngine) -> None:
    decision = engine.evaluate("stranger", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.allowed is False
    assert "not in the allowlist" in decision.reason
    assert decision.matched_rule == "default_deny"


def test_denylisted_peer_is_denied_even_if_method_safe(engine: A2APolicyEngine) -> None:
    decision = engine.evaluate("mallory", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.allowed is False
    assert "denylist" in decision.reason
    assert decision.matched_rule == "peer_denylist"


def test_deny_wins_over_allow_for_a_peer_on_both_lists() -> None:
    cfg = A2APolicyConfig.from_dict(
        {"default_action": "deny", "allowed_peers": ["alice"], "denied_peers": ["alice"]}
    )
    engine = A2APolicyEngine(cfg)
    decision = engine.evaluate("alice", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "peer_denylist"


# ---------------------------------------------------------------------------
# evaluate(): method risk tiers
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "method",
    [
        A2AMethod.GET_TASK,
        A2AMethod.LIST_TASKS,
        A2AMethod.GET_PUSH_NOTIFICATION_CONFIG,
    ],
)
def test_low_risk_methods_are_allowed(engine: A2APolicyEngine, method: A2AMethod) -> None:
    decision = engine.evaluate("alice", method, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.risk_tier == "low"


@pytest.mark.parametrize(
    "method",
    [A2AMethod.SEND_MESSAGE, A2AMethod.SUBSCRIBE_TO_TASK],
)
def test_medium_risk_methods_are_allowed(engine: A2APolicyEngine, method: A2AMethod) -> None:
    decision = engine.evaluate("alice", method)
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.risk_tier == "medium"


@pytest.mark.parametrize(
    "method",
    [
        A2AMethod.SEND_STREAMING_MESSAGE,
        A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
        A2AMethod.DELETE_PUSH_NOTIFICATION_CONFIG,
        A2AMethod.CANCEL_TASK,
    ],
)
def test_high_risk_methods_require_approval(engine: A2APolicyEngine, method: A2AMethod) -> None:
    decision = engine.evaluate("alice", method, task_id="t-1")
    assert decision.action is A2APolicyAction.REQUIRE_APPROVAL
    assert decision.allowed is False
    assert decision.risk_tier == "high"


def test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk() -> None:
    """A2A peers are never equivalent to the human operator — unlike MCP,
    owner_bypass must never let a "peer" skip approval, since the "owner" RBAC
    identity is not a meaningful concept for an external A2A caller."""
    cfg = A2APolicyConfig.from_dict(
        {
            "default_action": "deny",
            "allowed_peers": ["alice"],
            "owner_bypass": True,
            "owner_user_id": "alice",
        }
    )
    assert cfg.owner_bypass is False, "A2A config must force owner_bypass off unconditionally"
    engine = A2APolicyEngine(cfg)
    decision = engine.evaluate("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.REQUIRE_APPROVAL


# ---------------------------------------------------------------------------
# evaluate(): task-ownership enforcement (independent mitigation for the
# upstream contextId-collision gap, #83701)
# ---------------------------------------------------------------------------


def test_task_creator_can_access_their_own_task(engine: A2APolicyEngine) -> None:
    create = engine.evaluate("alice", A2AMethod.SEND_MESSAGE, task_id="t-42")
    assert create.allowed is True
    follow_up = engine.evaluate("alice", A2AMethod.GET_TASK, task_id="t-42")
    assert follow_up.action is A2APolicyAction.ALLOW


def test_peer_cannot_access_another_peers_task(engine: A2APolicyEngine) -> None:
    engine.evaluate("alice", A2AMethod.SEND_MESSAGE, task_id="t-42")
    decision = engine.evaluate("bob", A2AMethod.GET_TASK, task_id="t-42")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "task_ownership"
    assert "does not own task" in decision.reason


def test_peer_cannot_cancel_another_peers_task(engine: A2APolicyEngine) -> None:
    engine.evaluate("alice", A2AMethod.SEND_MESSAGE, task_id="t-99")
    decision = engine.evaluate("bob", A2AMethod.CANCEL_TASK, task_id="t-99")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "task_ownership"


def test_peer_cannot_subscribe_to_another_peers_task(engine: A2APolicyEngine) -> None:
    engine.evaluate("alice", A2AMethod.SEND_MESSAGE, task_id="t-7")
    decision = engine.evaluate("bob", A2AMethod.SUBSCRIBE_TO_TASK, task_id="t-7")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "task_ownership"


def test_task_ownership_check_is_a_no_op_for_an_unknown_task_id(engine: A2APolicyEngine) -> None:
    """A task_id AgentShroud never saw created (e.g. the very first GetTask
    against a task that predates this engine, or the engine restarted) should
    not be treated as an ownership violation — it falls through to normal
    risk-tier evaluation instead of being denied on a false-positive basis."""
    decision = engine.evaluate("alice", A2AMethod.GET_TASK, task_id="never-seen")
    assert decision.matched_rule != "task_ownership"


def test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path() -> None:
    """Ownership is checked before the risk-tier gate — a mismatched peer must
    be denied outright, not routed to REQUIRE_APPROVAL."""
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice", "bob"]})
    engine = A2APolicyEngine(cfg)
    engine.evaluate("alice", A2AMethod.SEND_MESSAGE, task_id="t-1")
    decision = engine.evaluate("bob", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.action is not A2APolicyAction.REQUIRE_APPROVAL


# ---------------------------------------------------------------------------
# is_safe_a2a_callback_url(): hardened SSRF guard (independent mitigation for
# the upstream gap #78298 — alternate-IP-encoding bypass)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "url",
    [
        "http://127.0.0.1/callback",
        "http://localhost/callback",
        "http://169.254.169.254/latest/meta-data/",  # cloud metadata endpoint
        "http://[::1]/callback",
        "http://2130706433/callback",  # decimal for 127.0.0.1
        "http://0x7f000001/callback",  # hex for 127.0.0.1
        "http://0177.0.0.1/callback",  # octal for 127.0.0.1
        "http://127.1/callback",  # short-form dotted-decimal
        "http://localhost./callback",  # trailing dot
        "http://0x7f.0.0.1/callback",  # mixed hex/decimal octet
    ],
)
def test_callback_url_ssrf_bypass_encodings_are_rejected(url: str) -> None:
    assert is_safe_a2a_callback_url(url) is False, f"{url!r} must be rejected as unsafe"


@pytest.mark.parametrize(
    "url,resolved_ip",
    [
        ("https://example.com/a2a/callback", "93.184.216.34"),
        ("https://peer.partner-agent.org:8443/webhook", "1.1.1.1"),
    ],
)
def test_callback_url_legitimate_public_urls_are_allowed(url: str, resolved_ip: str) -> None:
    """Hostname resolution is mocked — this test asserts the validator's own
    logic, not real DNS/network reachability (test file contract: no network)."""
    fake_addrinfo = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (resolved_ip, 0))]
    with patch("gateway.security.a2a_policy.socket.getaddrinfo", return_value=fake_addrinfo):
        assert is_safe_a2a_callback_url(url) is True


def test_callback_url_hostname_resolving_to_a_private_ip_is_rejected() -> None:
    """DNS rebinding: a public-looking hostname that currently resolves to a
    private/internal address must be rejected — re-checked on every call, not
    trusted from config-set time."""
    fake_addrinfo = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.5", 0))]
    with patch("gateway.security.a2a_policy.socket.getaddrinfo", return_value=fake_addrinfo):
        assert is_safe_a2a_callback_url("https://looks-public.example.com/hook") is False


def test_callback_url_unresolvable_hostname_fails_closed() -> None:
    with patch(
        "gateway.security.a2a_policy.socket.getaddrinfo",
        side_effect=socket.gaierror("nope"),
    ):
        assert is_safe_a2a_callback_url("https://does-not-resolve.invalid/hook") is False


def test_callback_url_rejects_non_http_schemes() -> None:
    assert is_safe_a2a_callback_url("file:///etc/passwd") is False
    assert is_safe_a2a_callback_url("gopher://127.0.0.1:6379/") is False


def test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe(
    engine: A2APolicyEngine,
) -> None:
    decision = engine.evaluate(
        "alice",
        A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
        task_id="t-1",
        callback_url="http://2130706433/steal-secrets",
    )
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "ssrf_callback_blocked"


def test_set_push_notification_config_with_safe_callback_still_requires_approval(
    engine: A2APolicyEngine,
) -> None:
    fake_addrinfo = [(socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 0))]
    with patch("gateway.security.a2a_policy.socket.getaddrinfo", return_value=fake_addrinfo):
        decision = engine.evaluate(
            "alice",
            A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
            task_id="t-1",
            callback_url="https://example.com/webhook",
        )
    assert decision.action is A2APolicyAction.REQUIRE_APPROVAL
    assert decision.risk_tier == "high"


# ---------------------------------------------------------------------------
# A2APolicyDecision
# ---------------------------------------------------------------------------


def test_decision_allowed_property_only_true_for_terminal_allow() -> None:
    allow = A2APolicyDecision(action=A2APolicyAction.ALLOW, peer_id="alice", method="GetTask")
    deny = A2APolicyDecision(action=A2APolicyAction.DENY, peer_id="alice", method="GetTask")
    pending = A2APolicyDecision(
        action=A2APolicyAction.REQUIRE_APPROVAL, peer_id="alice", method="CancelTask"
    )
    assert allow.allowed is True
    assert deny.allowed is False
    assert pending.allowed is False


# ---------------------------------------------------------------------------
# enforce(): async approval-queue round-trip
# ---------------------------------------------------------------------------


class _StubApprovalQueue:
    def __init__(self, requires_wait: bool = True, approved: bool = True):
        self._requires_wait = requires_wait
        self._approved = approved
        self.submitted = []

    async def submit_tool_request(self, qualified, args, agent_id, force_tier=None):
        self.submitted.append((qualified, args, agent_id, force_tier))
        return "req-1", self._requires_wait

    async def wait_for_decision(self, request_id):
        return self._approved


@pytest.mark.asyncio
async def test_enforce_low_risk_method_bypasses_approval_queue_entirely(
    engine: A2APolicyEngine,
) -> None:
    decision = await engine.enforce("alice", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW


@pytest.mark.asyncio
async def test_enforce_high_risk_method_approved_resolves_to_allow() -> None:
    queue = _StubApprovalQueue(requires_wait=True, approved=True)
    engine = A2APolicyEngine(_base_config(), approval_queue=queue)
    decision = await engine.enforce("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.matched_rule == "approved"
    assert queue.submitted[0][3] == "high"  # force_tier passed through


@pytest.mark.asyncio
async def test_enforce_high_risk_method_rejected_resolves_to_deny() -> None:
    queue = _StubApprovalQueue(requires_wait=True, approved=False)
    engine = A2APolicyEngine(_base_config(), approval_queue=queue)
    decision = await engine.enforce("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "rejected"


@pytest.mark.asyncio
async def test_enforce_task_ownership_violation_never_reaches_approval_queue() -> None:
    queue = _StubApprovalQueue()
    engine = A2APolicyEngine(_base_config(), approval_queue=queue)
    await engine.enforce("alice", A2AMethod.SEND_MESSAGE, task_id="t-5")
    decision = await engine.enforce("bob", A2AMethod.CANCEL_TASK, task_id="t-5")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "task_ownership"


@pytest.mark.asyncio
async def test_enforce_high_risk_method_with_no_approval_queue_fails_closed(
    engine: A2APolicyEngine,
) -> None:
    """The `engine` fixture has no approval_queue configured at all — a
    high-risk method must deny, never silently proceed."""
    decision = await engine.enforce("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "approval_unavailable"


class _LegacyStubApprovalQueue:
    """A duck-typed queue predating the ``force_tier`` kwarg — enforce() must
    fall back to the legacy call signature via the TypeError branch."""

    def __init__(self, requires_wait: bool = True, approved: bool = True):
        self._requires_wait = requires_wait
        self._approved = approved
        self.submitted = []

    async def submit_tool_request(self, qualified, args, agent_id):
        self.submitted.append((qualified, args, agent_id))
        return "req-legacy", self._requires_wait

    async def wait_for_decision(self, request_id):
        return self._approved


@pytest.mark.asyncio
async def test_enforce_falls_back_to_legacy_queue_signature_without_force_tier() -> None:
    queue = _LegacyStubApprovalQueue(requires_wait=True, approved=True)
    engine = A2APolicyEngine(_base_config(), approval_queue=queue)
    decision = await engine.enforce("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert len(queue.submitted) == 1


@pytest.mark.asyncio
async def test_enforce_denies_when_queue_downgrades_requires_wait_to_false() -> None:
    """A queue reporting requires_wait=False for a call the engine deemed
    high-risk must never be treated as an implicit ALLOW."""
    queue = _StubApprovalQueue(requires_wait=False)
    engine = A2APolicyEngine(_base_config(), approval_queue=queue)
    decision = await engine.enforce("alice", A2AMethod.CANCEL_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.DENY
    assert decision.matched_rule == "approval_downgrade_refused"


# ---------------------------------------------------------------------------
# Remaining edge cases (default-allow posture, string-typed methods, IPv6,
# malformed URLs, integer-overflow IP literals)
# ---------------------------------------------------------------------------


def test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check() -> None:
    """An operator who explicitly opts into default_action=allow gets normal
    risk-tier evaluation for peers not on any list, rather than an outright
    deny — the opt-in itself is the security decision being tested here."""
    cfg = A2APolicyConfig.from_dict({"default_action": "allow"})
    engine = A2APolicyEngine(cfg)
    decision = engine.evaluate("nobody-listed", A2AMethod.GET_TASK, task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.matched_rule == "allowlist"


def test_evaluate_accepts_a_plain_string_method_not_just_the_enum(
    engine: A2APolicyEngine,
) -> None:
    """Real JSON-RPC payloads deliver the method as a plain string — evaluate()
    must coerce it to A2AMethod itself, not require callers to pre-convert."""
    decision = engine.evaluate("alice", "GetTask", task_id="t-1")
    assert decision.action is A2APolicyAction.ALLOW
    assert decision.method == "GetTask"


def test_callback_url_ipv4_mapped_ipv6_loopback_is_rejected() -> None:
    assert is_safe_a2a_callback_url("http://[::ffff:127.0.0.1]/callback") is False


def test_callback_url_malformed_url_is_rejected() -> None:
    # A URL with characters urlsplit cannot parse into a scheme/host at all.
    assert is_safe_a2a_callback_url("http://\x00\x01/callback") is False


def test_callback_url_scheme_only_no_host_is_rejected() -> None:
    assert is_safe_a2a_callback_url("http:///no-host-path") is False


def test_callback_url_bare_dot_host_is_rejected() -> None:
    assert is_safe_a2a_callback_url("http://./callback") is False


def test_callback_url_out_of_range_decimal_literal_is_not_treated_as_a_valid_ip() -> None:
    """A 10-digit decimal string (matches the decimal-IPv4 pattern) whose
    value exceeds 0xFFFFFFFF is not a valid IPv4 address at all — it must
    fall through to hostname resolution (then fail closed, since it can't
    resolve) rather than crash or be silently treated as safe."""
    with patch(
        "gateway.security.a2a_policy.socket.getaddrinfo",
        side_effect=socket.gaierror("nope"),
    ):
        assert is_safe_a2a_callback_url("http://9999999999/callback") is False
