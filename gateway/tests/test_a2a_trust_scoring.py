# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SCRUM-129 Phase 4 — A2A trust-scoring wiring.

Reuses TrustManager as-is (already agent-id-keyed, protocol-agnostic — an A2A
peer_id is registered exactly like any other agent_id) with two new typed
violations added to the shared ViolationType enum, and wires A2AProxy to
record them on the two policy denials that map to independently-mitigated
upstream Hermes gaps: task-ownership violation (gap #83701) and SSRF-callback
rejection (gap #78298, placed in severe_violation_types — unambiguous
malicious intent, not an accident).
"""

from __future__ import annotations

import pytest

from gateway.proxy.a2a_proxy import A2AProxy
from gateway.security.a2a_policy import A2APolicyConfig, A2APolicyEngine
from gateway.security.progressive_trust_config import ProgressiveTrustConfig, ViolationType
from gateway.security.trust_manager import TrustManager


class _StubForwarder:
    async def forward(self, body: str):
        return 200, '{"result": "ok"}'


def _jsonrpc(method: str, params: dict) -> dict:
    return {"jsonrpc": "2.0", "id": "1", "method": method, "params": params}


# ---------------------------------------------------------------------------
# ViolationType / ProgressiveTrustConfig additions
# ---------------------------------------------------------------------------


def test_a2a_violation_types_exist() -> None:
    assert ViolationType.A2A_TASK_OWNERSHIP_VIOLATION.value == "a2a_task_ownership_violation"
    assert ViolationType.A2A_SSRF_CALLBACK_ATTEMPT.value == "a2a_ssrf_callback_attempt"


def test_a2a_ssrf_callback_is_a_severe_violation_by_default() -> None:
    """Unambiguous malicious intent — immediate demotion, not a slow decay."""
    cfg = ProgressiveTrustConfig()
    assert ViolationType.A2A_SSRF_CALLBACK_ATTEMPT in cfg.severe_violation_types


def test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy() -> (
    None
):
    cfg = ProgressiveTrustConfig()
    ownership_penalty = cfg.violation_penalties[ViolationType.A2A_TASK_OWNERSHIP_VIOLATION]
    generic_penalty = cfg.violation_penalties[ViolationType.POLICY_VIOLATION]
    assert ownership_penalty > generic_penalty


def test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier() -> None:
    cfg = ProgressiveTrustConfig()
    assert (
        cfg.violation_penalties[ViolationType.A2A_SSRF_CALLBACK_ATTEMPT]
        == cfg.violation_penalties[ViolationType.MALICIOUS_INTENT]
    )


# ---------------------------------------------------------------------------
# A2AProxy -> TrustManager wiring
# ---------------------------------------------------------------------------


@pytest.fixture()
def trust_manager():
    manager = TrustManager(progressive_config=ProgressiveTrustConfig())
    yield manager
    manager.close()


def test_proxy_without_trust_manager_does_not_raise() -> None:
    """trust_manager is an optional dependency — a proxy built without one
    (e.g. before Phase 4 wiring lands in lifespan.py) must keep working."""
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice", "bob"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice", "bob-token": "bob"},
        forwarder=_StubForwarder(),
    )
    assert proxy is not None


@pytest.mark.asyncio
async def test_task_ownership_violation_records_a2a_violation_type(
    trust_manager: TrustManager,
) -> None:
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice", "bob"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice", "bob-token": "bob"},
        forwarder=_StubForwarder(),
        trust_manager=trust_manager,
    )
    trust_manager.register_agent("bob")
    before_score = trust_manager.get_trust("bob")[1]

    await proxy.process_inbound_request(
        raw_body=_jsonrpc("SendMessage", {"message": {"taskId": "t-1", "parts": []}}),
        auth_header="Bearer alice-token",
        source_ip="1.1.1.1",
    )
    result = await proxy.process_inbound_request(
        raw_body=_jsonrpc("GetTask", {"taskId": "t-1"}),
        auth_header="Bearer bob-token",
        source_ip="2.2.2.2",
    )

    assert result.blocked is True
    after_score = trust_manager.get_trust("bob")[1]
    assert after_score < before_score


@pytest.mark.asyncio
async def test_ssrf_callback_rejection_triggers_severe_demotion(
    trust_manager: TrustManager,
) -> None:
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"alice-token": "alice"},
        forwarder=_StubForwarder(),
        trust_manager=trust_manager,
    )
    trust_manager.register_agent("alice")
    before_level, _ = trust_manager.get_trust("alice")

    result = await proxy.process_inbound_request(
        raw_body=_jsonrpc(
            "SetTaskPushNotificationConfig",
            {
                "taskId": "t-1",
                "pushNotificationConfig": {"url": "http://2130706433/steal-secrets"},
            },
        ),
        auth_header="Bearer alice-token",
        source_ip="1.1.1.1",
    )

    assert result.blocked is True
    assert result.matched_rule == "ssrf_callback_blocked"
    after_level, _ = trust_manager.get_trust("alice")
    # Severe violation -> immediate one-level demotion, not just a score dip.
    assert after_level < before_level


@pytest.mark.asyncio
async def test_generic_denial_does_not_record_a2a_specific_violation_types(
    trust_manager: TrustManager,
) -> None:
    """A plain default-deny (unknown/unlisted peer) is a routing decision, not
    evidence of an attack against a specific known peer — it must not be
    recorded as either A2A violation type (there's no established peer
    identity to attribute it to in the trust ladder in the first place)."""
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"stranger-token": "stranger"},
        forwarder=_StubForwarder(),
        trust_manager=trust_manager,
    )
    result = await proxy.process_inbound_request(
        raw_body=_jsonrpc("GetTask", {"taskId": "t-1"}),
        auth_header="Bearer stranger-token",
        source_ip="1.1.1.1",
    )
    assert result.blocked is True
    assert result.matched_rule == "default_deny"
    # No crash, and nothing registered a score for an agent_id never
    # explicitly registered — default-deny doesn't touch the trust ladder.
    assert trust_manager.get_trust("stranger") is None
