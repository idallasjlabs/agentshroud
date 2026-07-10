# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for AlertTelegramRelay (SCRUM-61) — security_alert events → owner Telegram."""

from __future__ import annotations

import pytest

from gateway.ingest_api.alert_telegram_relay import AlertTelegramRelay
from gateway.ingest_api.event_bus import EventBus, make_event


class _SendSpy:
    def __init__(self, fail: bool = False):
        self.sent: list[tuple[str, str]] = []
        self.fail = fail

    async def __call__(self, chat_id: str, text: str) -> None:
        if self.fail:
            raise RuntimeError("telegram down")
        self.sent.append((chat_id, text))


def _alert_event(severity="critical", tool="cron-scheduler", message="job X failed"):
    return make_event(
        "security_alert",
        summary=f"{tool}: {message}",
        details={"tool": tool, "message": message, "alert_severity": severity.upper()},
        severity=severity,
    )


@pytest.mark.asyncio
async def test_critical_alert_relayed_to_owner():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="8096968754")
    await relay(_alert_event("critical"))
    assert len(spy.sent) == 1
    chat_id, text = spy.sent[0]
    assert chat_id == "8096968754"
    assert "cron-scheduler" in text and "job X failed" in text
    assert "🔴" in text  # severity marker


@pytest.mark.asyncio
async def test_warning_alert_relayed_with_orange_marker():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    await relay(_alert_event("warning", message="job Y failed"))
    assert len(spy.sent) == 1
    assert "🟠" in spy.sent[0][1]


@pytest.mark.asyncio
async def test_info_severity_not_relayed():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    await relay(_alert_event("info"))
    assert spy.sent == []


@pytest.mark.asyncio
async def test_non_alert_events_ignored():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    await relay(make_event("auth_failed", "nope", severity="critical"))
    assert spy.sent == []


@pytest.mark.asyncio
async def test_dedup_same_alert_sent_once():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    e = _alert_event("critical")
    await relay(e)
    await relay(e)
    assert len(spy.sent) == 1


@pytest.mark.asyncio
async def test_rate_limit_caps_sends_per_hour():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1", max_per_hour=3)
    for i in range(6):
        await relay(_alert_event("critical", message=f"failure {i}"))
    assert len(spy.sent) == 3


@pytest.mark.asyncio
async def test_send_failure_swallowed():
    relay = AlertTelegramRelay(send_fn=_SendSpy(fail=True), owner_chat_id="1")
    await relay(_alert_event("critical"))  # must not raise


@pytest.mark.asyncio
async def test_plain_dict_event_tolerated():
    # Defensive: subscribers may receive dicts from legacy emitters.
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    await relay(
        {"type": "security_alert", "severity": "critical", "summary": "dict alert", "details": {}}
    )
    assert len(spy.sent) == 1


@pytest.mark.asyncio
async def test_subscribed_relay_receives_bus_emissions():
    spy = _SendSpy()
    relay = AlertTelegramRelay(send_fn=spy, owner_chat_id="1")
    bus = EventBus()
    await bus.subscribe(relay)
    await bus.emit(_alert_event("critical"))
    assert len(spy.sent) == 1


@pytest.mark.asyncio
async def test_api_alerts_endpoint_emits_bus_event(monkeypatch):
    """Regression (SCRUM-61): /api/alerts used to call event_bus.publish(),
    a method EventBus never had — the bare except swallowed the
    AttributeError and alerts silently never reached subscribers."""
    from gateway.ingest_api import main as main_mod

    bus = EventBus()
    received: list = []

    async def _capture(event):
        received.append(event)

    await bus.subscribe(_capture)
    monkeypatch.setattr(main_mod.app_state, "event_bus", bus, raising=False)

    class _Req:
        client = type("C", (), {"host": "127.0.0.1"})()

        async def json(self):
            return {
                "type": "security_alert",
                "severity": "CRITICAL",
                "tool": "cron-scheduler",
                "message": "job nightly-report failed (exit 1)",
            }

    resp = await main_mod.receive_security_alert(_Req())
    assert resp["ok"] is True
    assert len(received) == 1, "alert never reached the event bus"
    ev = received[0]
    assert ev.type == "security_alert"
    assert ev.severity == "critical"
    assert "cron-scheduler" in ev.summary
    assert ev.details["alert_severity"] == "CRITICAL"
