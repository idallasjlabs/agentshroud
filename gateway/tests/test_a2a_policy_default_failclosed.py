# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SCRUM-129 — A2A policy engine must never ship dormant or default-open.

Mirrors the lesson from WS-E finding RT-11 (test_mcp_policy_default_failclosed.py):
an MCP policy engine that only activates when an operator explicitly authors a
config section shipped DORMANT on a stock deploy, running with governance
effectively disabled. The A2A engine must fail closed by construction — with
no config authored at all, every peer is denied, not silently allowed.
"""

from __future__ import annotations

from gateway.security.a2a_policy import (
    A2AMethod,
    A2APolicyAction,
    A2APolicyConfig,
    A2APolicyEngine,
)


class TestDefaultA2APolicyIsFailClosed:
    def test_bare_config_denies_every_peer(self) -> None:
        """A2APolicyConfig() with no arguments — the shape a fresh deploy gets
        if nothing configures a2a_policy: at all — must deny everything."""
        engine = A2APolicyEngine(A2APolicyConfig())
        decision = engine.evaluate("anyone", A2AMethod.GET_TASK, task_id="t-1")
        assert decision.action is A2APolicyAction.DENY
        assert decision.allowed is False

    def test_from_dict_none_is_fail_closed(self) -> None:
        """load_config-style callers pass whatever the YAML section resolved
        to, which is None when the section is absent entirely."""
        cfg = A2APolicyConfig.from_dict(None)
        engine = A2APolicyEngine(cfg)
        decision = engine.evaluate("anyone", A2AMethod.SEND_MESSAGE)
        assert decision.action is A2APolicyAction.DENY

    def test_from_dict_empty_dict_is_fail_closed(self) -> None:
        cfg = A2APolicyConfig.from_dict({})
        engine = A2APolicyEngine(cfg)
        decision = engine.evaluate("anyone", A2AMethod.GET_TASK, task_id="t-1")
        assert decision.action is A2APolicyAction.DENY

    def test_engine_constructed_with_no_config_at_all_is_fail_closed(self) -> None:
        """`A2APolicyEngine()` with no config argument — the laziest possible
        call site — must still deny by default."""
        engine = A2APolicyEngine()
        decision = engine.evaluate("anyone", A2AMethod.GET_TASK, task_id="t-1")
        assert decision.action is A2APolicyAction.DENY

    def test_invalid_default_action_string_falls_back_to_deny(self) -> None:
        """A typo'd default_action (e.g. 'allow-all') must not silently open
        the gate — fall back to the safe default and log a warning."""
        cfg = A2APolicyConfig.from_dict({"default_action": "allow-all-bogus-value"})
        assert cfg.default_action is A2APolicyAction.DENY

    def test_owner_bypass_is_always_false_regardless_of_input(self) -> None:
        """Unlike MCP, owner_bypass is not operator-configurable for A2A at
        all — an external peer is never the human operator. Config authors
        cannot accidentally (or deliberately) turn this on."""
        cfg = A2APolicyConfig.from_dict({"owner_bypass": True, "owner_user_id": "some-owner"})
        assert cfg.owner_bypass is False

    def test_configured_allowlist_still_works_alongside_fail_closed_default(self) -> None:
        """Fail-closed-by-default must not mean "impossible to allow anything"
        — an explicit allowlist still functions normally."""
        cfg = A2APolicyConfig.from_dict({"allowed_peers": ["trusted-peer"]})
        engine = A2APolicyEngine(cfg)
        allowed = engine.evaluate("trusted-peer", A2AMethod.GET_TASK, task_id="t-1")
        denied = engine.evaluate("random-peer", A2AMethod.GET_TASK, task_id="t-1")
        assert allowed.action is A2APolicyAction.ALLOW
        assert denied.action is A2APolicyAction.DENY
