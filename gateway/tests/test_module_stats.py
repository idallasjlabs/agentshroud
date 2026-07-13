# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for ModuleStatsCollector (SCRUM-80) — live per-module enforcement counts."""

from __future__ import annotations

import threading

from gateway.security.module_stats import Decision, ModuleStatsCollector


def test_record_and_snapshot():
    c = ModuleStatsCollector()
    c.record("egress_filter", Decision.BLOCK)
    c.record("egress_filter", Decision.ALLOW)
    c.record("egress_filter", Decision.ALLOW)
    snap = c.snapshot()
    assert snap["egress_filter"]["blocked"] == 1
    assert snap["egress_filter"]["allowed"] == 2
    assert snap["egress_filter"]["sanitized"] == 0
    assert snap["egress_filter"]["total"] == 3


def test_sanitize_decision():
    c = ModuleStatsCollector()
    c.record("sanitizer", Decision.SANITIZE)
    assert c.snapshot()["sanitizer"]["sanitized"] == 1


def test_unknown_module_created_on_demand():
    c = ModuleStatsCollector()
    c.record("brand_new_module", Decision.ALLOW)
    assert "brand_new_module" in c.snapshot()


def test_block_rate_computed():
    c = ModuleStatsCollector()
    for _ in range(3):
        c.record("m", Decision.BLOCK)
    c.record("m", Decision.ALLOW)
    assert c.snapshot()["m"]["block_rate"] == 0.75


def test_empty_module_zero_rate_not_division_error():
    c = ModuleStatsCollector()
    c.record("m", Decision.ALLOW)
    # allow-only module: block_rate 0.0, no ZeroDivision anywhere
    assert c.snapshot()["m"]["block_rate"] == 0.0


def test_thread_safe_under_concurrency():
    c = ModuleStatsCollector()

    def worker():
        for _ in range(1000):
            c.record("m", Decision.BLOCK)

    threads = [threading.Thread(target=worker) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert c.snapshot()["m"]["blocked"] == 8000


def test_record_ignores_invalid_decision_safely():
    c = ModuleStatsCollector()
    # A bad decision value must never raise into an enforcement path.
    c.record("m", "not-a-decision")  # type: ignore[arg-type]
    # nothing counted, no crash
    assert c.snapshot().get("m", {}).get("total", 0) == 0


def test_reset():
    c = ModuleStatsCollector()
    c.record("m", Decision.BLOCK)
    c.reset()
    assert c.snapshot() == {}


class TestEnforcementWiring:
    """SCRUM-80 — the record helper + wrapped enforcement points feed real data."""

    def setup_method(self):
        from gateway.security.module_stats import get_collector

        get_collector().reset()

    def test_record_decision_helper(self):
        from gateway.security.module_stats import get_collector, record_decision

        record_decision("egress_filter", allowed=False)
        record_decision("egress_filter", allowed=True)
        record_decision("sanitizer", allowed=True, sanitized=True)
        snap = get_collector().snapshot()
        assert snap["egress_filter"]["blocked"] == 1
        assert snap["egress_filter"]["allowed"] == 1
        assert snap["sanitizer"]["sanitized"] == 1

    def test_record_decision_never_raises(self):
        from gateway.security.module_stats import record_decision

        # Bad module type / weird args must not propagate.
        record_decision(None, allowed=True)  # type: ignore[arg-type]

    def test_tool_acl_can_use_tool_records(self):
        from gateway.security.module_stats import get_collector
        from gateway.security.tool_acl import ToolACLEnforcer

        enforcer = ToolACLEnforcer()  # no trust manager — pure ACL path
        enforcer.can_use_tool("owner-does-not-exist", "web_search")
        snap = get_collector().snapshot()
        assert "tool_acl" in snap
        assert snap["tool_acl"]["total"] >= 1
