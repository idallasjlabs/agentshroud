# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for CronStateMonitor (SCRUM-61 part 2) — bot cron failures → AlertDispatcher."""

from __future__ import annotations

import json

import pytest

from gateway.security.cron_state_monitor import CronStateMonitor


def _openclaw_store(tmp_path, jobs):
    p = tmp_path / "openclaw-jobs.json"
    p.write_text(json.dumps({"jobs": jobs}))
    return str(p)


def _hermes_store(tmp_path, jobs):
    p = tmp_path / "hermes-jobs.json"
    p.write_text(json.dumps({"jobs": jobs}))
    return str(p)


def _oc_job(job_id="j1", name="nightly report", status="ok", consecutive=0, enabled=True):
    return {
        "id": job_id,
        "name": name,
        "enabled": enabled,
        "state": {
            "lastStatus": status,
            "consecutiveErrors": consecutive,
            "lastRunAtMs": 1771777019837,
            "lastDurationMs": 28323,
        },
    }


def _hermes_job(job_id="h1", name="daily check-in", status="ok", error=None, enabled=True):
    return {
        "id": job_id,
        "name": name,
        "enabled": enabled,
        "last_status": status,
        "last_error": error,
        "last_run_at": "2026-07-10T14:02:16+00:00",
    }


class _DispatchSpy:
    def __init__(self):
        self.alerts: list[dict] = []

    def __call__(self, alert: dict) -> dict:
        self.alerts.append(alert)
        return {"action": "notified"}


class TestParsing:
    def test_parses_openclaw_schema(self, tmp_path):
        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=2)])
        jobs = CronStateMonitor.parse_store("openclaw", path)
        assert len(jobs) == 1
        j = jobs[0]
        assert j.bot == "openclaw"
        assert j.job_id == "j1"
        assert j.name == "nightly report"
        assert j.failing is True
        assert j.consecutive_errors == 2

    def test_parses_hermes_schema(self, tmp_path):
        path = _hermes_store(tmp_path, [_hermes_job(status="fail", error="boom")])
        jobs = CronStateMonitor.parse_store("hermes", path)
        assert len(jobs) == 1
        j = jobs[0]
        assert j.bot == "hermes"
        assert j.failing is True
        assert "boom" in (j.error or "")

    def test_ok_jobs_not_failing(self, tmp_path):
        path = _openclaw_store(tmp_path, [_oc_job(status="ok")])
        assert CronStateMonitor.parse_store("openclaw", path)[0].failing is False

    def test_missing_file_returns_empty(self, tmp_path):
        assert CronStateMonitor.parse_store("openclaw", str(tmp_path / "nope.json")) == []

    def test_corrupt_file_returns_empty(self, tmp_path):
        p = tmp_path / "bad.json"
        p.write_text("{not json")
        assert CronStateMonitor.parse_store("openclaw", str(p)) == []

    def test_disabled_jobs_ignored(self, tmp_path):
        path = _openclaw_store(tmp_path, [_oc_job(status="error", enabled=False)])
        assert CronStateMonitor.parse_store("openclaw", path) == []


class TestTransitions:
    def test_ok_to_fail_dispatches_high_alert(self, tmp_path):
        spy = _DispatchSpy()
        path = _openclaw_store(tmp_path, [_oc_job(status="ok")])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        assert spy.alerts == []
        _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon.check()
        assert len(spy.alerts) == 1
        a = spy.alerts[0]
        assert a["severity"] == "HIGH"
        assert a["tool"] == "cron-scheduler"
        assert "nightly report" in a["message"]
        assert "openclaw" in a["message"]

    def test_first_sight_failing_alerts_once(self, tmp_path):
        # A job already failing when the monitor starts must alert (the
        # failure is live), but only once — not every poll.
        spy = _DispatchSpy()
        path = _hermes_store(tmp_path, [_hermes_job(status="fail", error="x")])
        mon = CronStateMonitor({"hermes": path}, dispatch_fn=spy)
        mon.check()
        mon.check()
        mon.check()
        assert len(spy.alerts) == 1

    def test_repeated_failure_escalates_to_critical(self, tmp_path):
        spy = _DispatchSpy()
        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=3)])
        mon.check()
        assert len(spy.alerts) == 2
        assert spy.alerts[1]["severity"] == "CRITICAL"

    def test_recovery_resets_alerting(self, tmp_path):
        spy = _DispatchSpy()
        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        _openclaw_store(tmp_path, [_oc_job(status="ok", consecutive=0)])
        mon.check()
        _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon.check()
        assert len(spy.alerts) == 2  # re-alerted after recovery

    def test_multiple_stores_checked(self, tmp_path):
        spy = _DispatchSpy()
        oc = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        hm = _hermes_store(tmp_path, [_hermes_job(status="fail", error="y")])
        mon = CronStateMonitor({"openclaw": oc, "hermes": hm}, dispatch_fn=spy)
        mon.check()
        assert len(spy.alerts) == 2

    def test_dispatch_failure_does_not_raise(self, tmp_path):
        def _boom(alert):
            raise RuntimeError("dispatcher down")

        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=_boom)
        mon.check()  # must not raise

    def test_alert_ids_stable_per_job_episode(self, tmp_path):
        # AlertDispatcher dedups on id — the id must be stable for a failure
        # episode so restarts of the monitor don't re-ping the owner.
        spy = _DispatchSpy()
        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon1 = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon1.check()
        mon2 = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon2.check()
        assert spy.alerts[0]["id"] == spy.alerts[1]["id"]


@pytest.mark.asyncio
async def test_poll_loop_runs_and_stops(tmp_path):
    spy = _DispatchSpy()
    path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
    mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy, interval_seconds=0.01)
    task = mon.start()
    import asyncio

    await asyncio.sleep(0.05)
    await mon.stop()
    assert task.done()
    assert len(spy.alerts) == 1
