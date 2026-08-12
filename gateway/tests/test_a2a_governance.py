# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for A2A Governance Proxy."""

import time
import pytest

from gateway.security.a2a_governance import (
    A2ADecision,
    A2AGovernanceConfig,
    A2AGovernanceProxy,
    A2AMessage,
    A2AMessageType,
    A2APeer,
)


@pytest.fixture
def proxy():
    return A2AGovernanceProxy(A2AGovernanceConfig(enabled=True, mode="enforce"))


@pytest.fixture
def monitor_proxy():
    return A2AGovernanceProxy(A2AGovernanceConfig(enabled=True, mode="monitor"))


@pytest.fixture
def trusted_peer():
    return A2APeer(
        agent_id="agent-b",
        agent_name="Agent B",
        endpoint="https://agent-b.example.com/a2a",
        trust_score=80,
        capabilities=["code_review", "testing"],
    )


@pytest.fixture
def untrusted_peer():
    return A2APeer(
        agent_id="agent-c",
        agent_name="Agent C",
        endpoint="https://agent-c.example.com/a2a",
        trust_score=20,
    )


def _msg(source="agent-a", target="agent-b", msg_type=A2AMessageType.TASK_REQUEST, payload=None):
    return A2AMessage(
        message_id=f"msg-{time.time()}",
        message_type=msg_type,
        source_agent=source,
        target_agent=target,
        payload=payload or {"task": "review code"},
    )


class TestPeerManagement:
    def test_register_peer(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        assert proxy.get_peer("agent-b") is not None

    def test_unregister_peer(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        removed = proxy.unregister_peer("agent-b")
        assert removed is not None
        assert proxy.get_peer("agent-b") is None

    def test_update_trust(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        proxy.update_peer_trust("agent-b", 30)
        assert proxy.get_peer("agent-b").trust_score == 30

    def test_trust_clamped(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        proxy.update_peer_trust("agent-b", 150)
        assert proxy.get_peer("agent-b").trust_score == 100
        proxy.update_peer_trust("agent-b", -10)
        assert proxy.get_peer("agent-b").trust_score == 0


class TestInboundProcessing:
    def test_trusted_peer_allowed(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", target="agent-a")
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.ALLOW

    def test_unknown_peer_quarantined(self, proxy):
        msg = _msg(source="unknown-agent", target="agent-a")
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.QUARANTINE

    def test_untrusted_peer_denied(self, proxy, untrusted_peer):
        proxy.register_peer(untrusted_peer)
        msg = _msg(source="agent-c", target="agent-a")
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.DENY

    def test_untrusted_peer_allowed_in_monitor(self, monitor_proxy, untrusted_peer):
        monitor_proxy.register_peer(untrusted_peer)
        msg = _msg(source="agent-c", target="agent-a")
        decision = monitor_proxy.process_inbound(msg)
        assert decision == A2ADecision.ALLOW  # Monitor mode doesn't block


class TestOutboundProcessing:
    def test_outbound_to_trusted_peer(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-a", target="agent-b")
        decision = proxy.process_outbound(msg)
        assert decision == A2ADecision.ALLOW

    def test_outbound_to_unknown_quarantined(self, proxy):
        msg = _msg(source="agent-a", target="unknown")
        decision = proxy.process_outbound(msg)
        assert decision == A2ADecision.QUARANTINE


class TestRateLimiting:
    def test_within_rate_limit(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        for _ in range(5):
            msg = _msg(source="agent-b", target="agent-a")
            decision = proxy.process_inbound(msg)
            assert decision == A2ADecision.ALLOW

    def test_rate_limit_exceeded(self, proxy, trusted_peer):
        config = A2AGovernanceConfig(rate_limit_per_minute=3)
        proxy = A2AGovernanceProxy(config)
        proxy.register_peer(trusted_peer)

        for i in range(3):
            msg = _msg(source="agent-b", target="agent-a")
            decision = proxy.process_inbound(msg)
            assert decision == A2ADecision.ALLOW

        msg = _msg(source="agent-b", target="agent-a")
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.DENY


class TestMessageSize:
    def test_normal_size_allowed(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", payload={"data": "x" * 100})
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.ALLOW

    def test_oversized_denied(self, proxy, trusted_peer):
        config = A2AGovernanceConfig(max_message_size_bytes=100)
        proxy = A2AGovernanceProxy(config)
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", payload={"data": "x" * 200})
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.DENY


class TestTaskConcurrency:
    def test_task_within_limit(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-a", target="agent-b", msg_type=A2AMessageType.TASK_REQUEST)
        decision = proxy.process_outbound(msg)
        assert decision == A2ADecision.ALLOW

    def test_task_limit_exceeded(self, proxy, trusted_peer):
        config = A2AGovernanceConfig(max_concurrent_tasks=2)
        proxy = A2AGovernanceProxy(config)
        proxy.register_peer(trusted_peer)

        for _ in range(2):
            msg = _msg(target="agent-b", msg_type=A2AMessageType.TASK_REQUEST)
            proxy.process_outbound(msg)

        msg = _msg(target="agent-b", msg_type=A2AMessageType.TASK_REQUEST)
        decision = proxy.process_outbound(msg)
        assert decision == A2ADecision.DENY

    def test_complete_task_frees_slot(self, proxy, trusted_peer):
        config = A2AGovernanceConfig(max_concurrent_tasks=1)
        proxy = A2AGovernanceProxy(config)
        proxy.register_peer(trusted_peer)

        msg = _msg(target="agent-b", msg_type=A2AMessageType.TASK_REQUEST)
        proxy.process_outbound(msg)

        proxy.complete_task("agent-b")

        msg2 = _msg(target="agent-b", msg_type=A2AMessageType.TASK_REQUEST)
        decision = proxy.process_outbound(msg2)
        assert decision == A2ADecision.ALLOW


class TestPIISanitization:
    def test_ssn_sanitized(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", payload={"data": "SSN: 123-45-6789"})
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.SANITIZE
        assert msg.sanitized is True

    def test_api_key_sanitized(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", payload={"key": "sk-proj-1234567890abcdef"})
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.SANITIZE

    def test_clean_payload_not_sanitized(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", payload={"task": "review the auth module"})
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.ALLOW
        assert msg.sanitized is False


class TestMessageFingerprint:
    def test_fingerprint_deterministic(self):
        msg1 = A2AMessage(
            message_id="m1", message_type=A2AMessageType.TASK_REQUEST,
            source_agent="a", target_agent="b", payload={"x": 1},
        )
        msg2 = A2AMessage(
            message_id="m2", message_type=A2AMessageType.TASK_REQUEST,
            source_agent="a", target_agent="b", payload={"x": 1},
        )
        assert msg1.fingerprint == msg2.fingerprint

    def test_fingerprint_differs_for_different_payloads(self):
        msg1 = A2AMessage(
            message_id="m1", message_type=A2AMessageType.TASK_REQUEST,
            source_agent="a", target_agent="b", payload={"x": 1},
        )
        msg2 = A2AMessage(
            message_id="m2", message_type=A2AMessageType.TASK_REQUEST,
            source_agent="a", target_agent="b", payload={"x": 2},
        )
        assert msg1.fingerprint != msg2.fingerprint


class TestReporting:
    def test_summary(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        msg = _msg(source="agent-b", target="agent-a")
        proxy.process_inbound(msg)
        summary = proxy.get_summary()
        assert summary["registered_peers"] == 1
        assert summary["trusted_peers"] == 1
        assert summary["total_messages"] >= 1

    def test_get_events_filtered(self, proxy, trusted_peer, untrusted_peer):
        proxy.register_peer(trusted_peer)
        proxy.register_peer(untrusted_peer)
        # Trusted message
        proxy.process_inbound(_msg(source="agent-b"))
        # Untrusted message (denied)
        proxy.process_inbound(_msg(source="agent-c"))

        denied = proxy.get_events(decision=A2ADecision.DENY)
        assert len(denied) >= 1

        agent_c_events = proxy.get_events(agent_id="agent-c")
        assert len(agent_c_events) >= 1

    def test_peer_stats_updated(self, proxy, trusted_peer):
        proxy.register_peer(trusted_peer)
        proxy.process_inbound(_msg(source="agent-b"))
        peer = proxy.get_peer("agent-b")
        assert peer.messages_received == 1


class TestDisabledProxy:
    def test_disabled_allows_all(self):
        proxy = A2AGovernanceProxy(A2AGovernanceConfig(enabled=False))
        msg = _msg(source="unknown", target="unknown")
        decision = proxy.process_inbound(msg)
        assert decision == A2ADecision.ALLOW
