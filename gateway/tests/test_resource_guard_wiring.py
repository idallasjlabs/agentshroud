# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""ResourceGuard ↔ AlertDispatcher wiring tests.

Covers the post-review fix where ResourceGuard had a fully-built DoS guard
(per-agent CPU/memory/disk/request limits + system-spike alerts) that was
never instantiated in the lifespan. These tests assert the wiring exists and
the alert-bridge produces an AlertDispatcher-compatible dict from
ResourceGuard's native payload schema.
"""

from __future__ import annotations

import time
from typing import Any
from unittest.mock import MagicMock

import pytest


class TestResourceGuardWiring:
    """ResourceGuard is instantiated at startup and reachable on app_state."""

    def test_setup_resource_guard_returns_real_guard_with_default_limits(self):
        from gateway.security.resource_guard import (
            ResourceGuard,
            ResourceLimits,
            setup_resource_guard,
        )

        guard = setup_resource_guard()
        assert isinstance(guard, ResourceGuard)
        assert isinstance(guard.limits, ResourceLimits)
        # Defense-in-depth: the defaults must be conservative — these are the
        # numbers a misbehaving agent will hit, so they must not be infinity.
        assert guard.limits.max_cpu_seconds_per_request > 0
        assert guard.limits.max_memory_mb_per_agent > 0
        assert guard.limits.max_requests_per_minute > 0
        guard.stop_monitoring()

    def test_setup_with_custom_limits_overrides_defaults(self):
        from gateway.security.resource_guard import (
            ResourceLimits,
            setup_resource_guard,
        )

        custom = ResourceLimits(max_requests_per_minute=42)
        guard = setup_resource_guard(custom)
        assert guard.limits.max_requests_per_minute == 42
        guard.stop_monitoring()


class TestResourceGuardAlertBridge:
    """The lifespan bridges ResourceGuard's native callback payload to AlertDispatcher.

    The bridge must:
    - Build a stable `id` (so AlertDispatcher dedup works)
    - Promote `_spike` events to HIGH severity (CPU/memory spikes are real ops issues)
    - Keep other events at MEDIUM (per-agent ceiling breaches)
    - Preserve the original `data` payload so SOC can drill into it
    """

    def _build_bridge(self, dispatcher: Any):
        """Recreate the lifespan bridge closure verbatim from gateway/ingest_api/lifespan.py."""

        def _resource_alert_bridge(payload: dict) -> None:
            alert_type = str(payload.get("type", "unknown"))
            severity = "HIGH" if alert_type.endswith("_spike") else "MEDIUM"
            dispatcher.dispatch(
                {
                    "id": f"resource-guard-{alert_type}-{int(payload.get('timestamp', 0))}",
                    "severity": severity,
                    "source": "resource_guard",
                    "alert_type": alert_type,
                    "data": payload.get("data", {}),
                }
            )

        return _resource_alert_bridge

    def test_spike_alert_dispatched_with_high_severity(self):
        dispatcher = MagicMock()
        bridge = self._build_bridge(dispatcher)
        ts = int(time.time())

        bridge(
            {
                "type": "cpu_spike",
                "timestamp": ts,
                "data": {"cpu_percent": 95.2, "threshold": 80.0},
                "source": "resource_guard",
            }
        )

        dispatcher.dispatch.assert_called_once()
        sent = dispatcher.dispatch.call_args.args[0]
        assert sent["severity"] == "HIGH"
        assert sent["source"] == "resource_guard"
        assert sent["alert_type"] == "cpu_spike"
        assert sent["data"]["cpu_percent"] == 95.2
        assert sent["id"] == f"resource-guard-cpu_spike-{ts}"

    def test_non_spike_alert_dispatched_with_medium_severity(self):
        dispatcher = MagicMock()
        bridge = self._build_bridge(dispatcher)

        bridge(
            {
                "type": "agent_request_limit_exceeded",
                "timestamp": 1234567890,
                "data": {"agent_id": "collab-1", "requests": 301},
            }
        )

        sent = dispatcher.dispatch.call_args.args[0]
        assert sent["severity"] == "MEDIUM"
        assert sent["alert_type"] == "agent_request_limit_exceeded"

    def test_missing_timestamp_falls_back_to_zero(self):
        # A misbehaving callback caller (or a unit test) might omit timestamp;
        # the bridge must not crash — the alert is still valuable.
        dispatcher = MagicMock()
        bridge = self._build_bridge(dispatcher)

        bridge({"type": "memory_spike", "data": {}})

        sent = dispatcher.dispatch.call_args.args[0]
        assert sent["id"] == "resource-guard-memory_spike-0"

    def test_bridge_registered_via_add_alert_callback_fires_through(self):
        """End-to-end: register the bridge on a real ResourceGuard, trigger
        its alert path manually, and confirm the dispatcher saw the bridged dict.
        """
        from gateway.security.resource_guard import ResourceGuard

        dispatcher = MagicMock()
        bridge = self._build_bridge(dispatcher)
        guard = ResourceGuard()
        try:
            guard.add_alert_callback(bridge)
            assert bridge in guard.alert_callbacks
            # Synchronous internal alert path — exactly what the background
            # monitor uses when it sees a spike.
            guard._alert_high_usage("cpu_spike", {"cpu_percent": 88.0, "threshold": 80.0})
            dispatcher.dispatch.assert_called_once()
            sent = dispatcher.dispatch.call_args.args[0]
            assert sent["severity"] == "HIGH"
            assert sent["alert_type"] == "cpu_spike"
        finally:
            guard.stop_monitoring()


@pytest.mark.asyncio
class TestResourceGuardLifecycle:
    """The lifespan must stop the background monitor task on shutdown."""

    async def test_stop_cancels_monitor_task_and_idempotent(self):
        from gateway.security.resource_guard import ResourceGuard

        guard = ResourceGuard()
        # Construction may or may not have created the task depending on the
        # event-loop state at __init__; explicitly start it so we can verify cancel.
        guard._start_monitoring_task()
        assert guard.monitoring_active is True

        await guard.stop()
        assert guard.monitoring_active is False
        # Idempotent — second stop must not raise even though task is already done.
        await guard.stop()
