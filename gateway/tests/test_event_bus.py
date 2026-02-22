# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for EventBus"""

import pytest
from gateway.ingest_api.event_bus import EventBus, make_event


@pytest.fixture
def bus():
    return EventBus()


@pytest.mark.asyncio
async def test_subscribe_receive_events(bus):
    """Subscriber receives emitted events"""
    received = []
    await bus.subscribe(lambda e: received.append(e))
    event = make_event("forward", "Content forwarded")
    await bus.emit(event)
    assert len(received) == 1
    assert received[0].type == "forward"
    assert received[0].summary == "Content forwarded"


@pytest.mark.asyncio
async def test_unsubscribe_stops_events(bus):
    """Unsubscribed callback stops receiving events"""
    received = []

    def cb(e):
        received.append(e)

    await bus.subscribe(cb)
    await bus.emit(make_event("forward", "first"))
    assert len(received) == 1
    await bus.unsubscribe(cb)
    await bus.emit(make_event("forward", "second"))
    assert len(received) == 1  # no new events


@pytest.mark.asyncio
async def test_emit_to_multiple_subscribers(bus):
    """Multiple subscribers all receive the same event"""
    r1, r2 = [], []
    await bus.subscribe(lambda e: r1.append(e))
    await bus.subscribe(lambda e: r2.append(e))
    await bus.emit(make_event("ssh_exec", "Command executed"))
    assert len(r1) == 1
    assert len(r2) == 1


@pytest.mark.asyncio
async def test_event_has_required_fields(bus):
    """Events have type, timestamp, summary, details, severity"""
    event = make_event("auth_failed", "Bad token", {"ip": "1.2.3.4"}, "warning")
    d = event.to_dict()
    assert "type" in d
    assert "timestamp" in d
    assert "summary" in d
    assert "details" in d
    assert "severity" in d
    assert d["type"] == "auth_failed"
    assert d["severity"] == "warning"
    assert d["details"]["ip"] == "1.2.3.4"


@pytest.mark.asyncio
async def test_emit_no_subscribers_no_error(bus):
    """Emitting with no subscribers doesn't raise"""
    await bus.emit(make_event("forward", "test"))  # should not raise


@pytest.mark.asyncio
async def test_get_stats(bus):
    """Stats track event counts"""
    await bus.emit(make_event("forward", "a"))
    await bus.emit(make_event("forward", "b"))
    await bus.emit(make_event("ssh_exec", "c"))
    stats = await bus.get_stats()
    assert stats["total_events"] == 3
    assert stats["events_by_type"]["forward"] == 2
    assert stats["events_by_type"]["ssh_exec"] == 1


@pytest.mark.asyncio
async def test_get_recent(bus):
    """Recent events are returned in order"""
    for i in range(5):
        await bus.emit(make_event("forward", f"event {i}"))
    recent = await bus.get_recent(3)
    assert len(recent) == 3
    assert recent[-1]["summary"] == "event 4"


@pytest.mark.asyncio
async def test_auth_failure_escalation(bus):
    """3+ auth failures in 5 min escalates to critical"""
    received = []
    await bus.subscribe(lambda e: received.append(e))
    for i in range(3):
        await bus.emit(make_event("auth_failed", f"fail {i}"))
    # Third one should be critical
    assert received[2].severity == "critical"


@pytest.mark.asyncio
async def test_async_subscriber(bus):
    """Async callbacks work"""
    received = []

    async def cb(e):
        received.append(e)

    await bus.subscribe(cb)
    await bus.emit(make_event("forward", "async test"))
    assert len(received) == 1
