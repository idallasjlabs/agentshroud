# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Retry behavior of AlertDispatcher._send_notification (kaizen fix).

Before this change, a single 10s timeout failure logged at ERROR — the top
gateway error category (14/wk). After this change: 3 attempts with
exponential backoff, success on any attempt returns True, final failure
logs at WARNING because the alert is already persisted to alert_log.
"""

from __future__ import annotations

import logging
import socket
import time
from pathlib import Path
from unittest.mock import patch

import pytest

from gateway.security.alert_dispatcher import AlertDispatcher


@pytest.fixture
def dispatcher(tmp_path: Path):
    return AlertDispatcher(
        alert_log=tmp_path / "alerts.jsonl",
        gateway_url="http://localhost:9",  # unused; urlopen is patched
    )


def _alert():
    return {
        "id": "test-alert-1",
        "severity": "WARNING",
        "tool": "unit-test",
        "message": "synthetic",
        "details": "",
    }


def test_succeeds_on_first_attempt(dispatcher, caplog):
    caplog.set_level(logging.DEBUG, logger="gateway.security.alert_dispatcher")
    with patch("urllib.request.urlopen") as mock_open:
        mock_open.return_value.__enter__ = lambda s: s
        mock_open.return_value.__exit__ = lambda *a: None
        ok = dispatcher._send_notification(_alert())
    assert ok is True
    assert mock_open.call_count == 1
    # No retry debug messages
    assert not any("retrying" in r.message for r in caplog.records)


def test_succeeds_after_one_transient_failure(dispatcher, caplog):
    caplog.set_level(logging.DEBUG, logger="gateway.security.alert_dispatcher")
    calls = {"n": 0}

    def flaky(*a, **k):
        calls["n"] += 1
        if calls["n"] == 1:
            raise socket.timeout("transient")
        # Second attempt: a real response (context manager)
        from unittest.mock import MagicMock

        m = MagicMock()
        m.__enter__ = lambda s: s
        m.__exit__ = lambda *a: None
        return m

    with patch("urllib.request.urlopen", side_effect=flaky), patch.object(time, "sleep"):
        ok = dispatcher._send_notification(_alert())
    assert ok is True
    assert calls["n"] == 2
    # Debug retry message present, no WARNING/ERROR
    assert any("retrying" in r.message for r in caplog.records)
    assert not [r for r in caplog.records if r.levelno >= logging.WARNING]


def test_all_attempts_fail_logs_warning_not_error(dispatcher, caplog):
    caplog.set_level(logging.DEBUG, logger="gateway.security.alert_dispatcher")
    with (
        patch("urllib.request.urlopen", side_effect=socket.timeout("persistent")),
        patch.object(time, "sleep"),
    ):
        ok = dispatcher._send_notification(_alert())
    assert ok is False
    warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
    errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
    assert warnings, "expected a final WARNING-level log"
    assert any("after 3 attempts" in r.message for r in warnings)
    assert not errors, f"unexpected ERROR-level logs: {[r.message for r in errors]}"


def test_backoff_called_between_attempts(dispatcher):
    sleep_calls = []
    with (
        patch("urllib.request.urlopen", side_effect=socket.timeout("nope")),
        patch.object(time, "sleep", side_effect=lambda s: sleep_calls.append(s)),
    ):
        dispatcher._send_notification(_alert())
    # Two sleeps for 3 attempts
    assert sleep_calls == [1.0, 3.0]


def test_dispatch_persists_alert_even_if_notification_fails(dispatcher, tmp_path):
    """The alert must already be in alert_log before notification runs.

    Before the kaizen fix this guarantee was already in place — verify
    nothing regressed.
    """
    with (
        patch("urllib.request.urlopen", side_effect=socket.timeout("nope")),
        patch.object(time, "sleep"),
    ):
        result = dispatcher.dispatch({**_alert(), "severity": "CRITICAL"})
    log_lines = (tmp_path / "alerts.jsonl").read_text().strip().splitlines()
    assert len(log_lines) == 1
    assert "test-alert-1" in log_lines[0]
    # Dispatch returns 'notify_failed' (or similar) when the notification
    # call failed; the alert was still persisted to alert_log (asserted
    # above). The dispatch must not raise.
    assert result["action"] in (
        "notified",
        "notify_failed",
        "buffered",
        "deduped",
        "rate_limited",
    )
