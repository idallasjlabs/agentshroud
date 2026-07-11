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


# ── Adversarial-review hardening (2026-07-11) ────────────────────────────────


class _DedupDispatchFake:
    """Mimics AlertDispatcher's id-based 24h dedup — the real downstream."""

    def __init__(self):
        self.seen: set[str] = set()
        self.delivered: list[dict] = []

    def __call__(self, alert: dict) -> dict:
        if alert["id"] in self.seen:
            return {"action": "deduped"}
        self.seen.add(alert["id"])
        self.delivered.append(alert)
        return {"action": "notified"}


class TestAdversarial:
    def test_malformed_consecutive_errors_does_not_blind_store(self, tmp_path):
        # One crafted job must not discard the whole pass (was: ValueError
        # from int() killed the store; a real failing job went unreported).
        spy = _DispatchSpy()
        bad = _oc_job(job_id="crafted", status="ok")
        bad["state"]["consecutiveErrors"] = "NaNlol"
        good = _oc_job(job_id="real", name="real job", status="error", consecutive=1)
        path = _openclaw_store(tmp_path, [bad, good])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        assert len(spy.alerts) == 1
        assert "real job" in spy.alerts[0]["message"]

    def test_oversized_store_skipped(self, tmp_path):
        spy = _DispatchSpy()
        p = tmp_path / "huge.json"
        p.write_text('{"jobs": [' + '"x",' * 2_000_000 + '"x"]}')
        mon = CronStateMonitor({"openclaw": str(p)}, dispatch_fn=spy)
        mon.check()  # must not OOM-parse or raise
        assert spy.alerts == []

    def test_flood_capped_with_aggregate_alert(self, tmp_path):
        # Thousands of fake failing jobs must not exhaust the shared
        # AlertDispatcher hourly budget: at most 5 individual episodes per
        # bot per pass, the rest fold into ONE aggregate.
        spy = _DispatchSpy()
        jobs = [
            _oc_job(job_id=f"fake{i}", name=f"fake {i}", status="error", consecutive=1)
            for i in range(50)
        ]
        path = _openclaw_store(tmp_path, jobs)
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        assert len(spy.alerts) == 6  # 5 individual + 1 aggregate
        agg = spy.alerts[-1]
        assert "45" in agg["message"] and "flood guard" in agg["message"]
        # Second pass: episodes already open — no re-flood.
        mon.check()
        assert len(spy.alerts) == 6

    def test_recovery_refail_realerts_through_real_dedup(self, tmp_path):
        # fail → recover → fail with an UNCHANGED last_run marker must still
        # re-alert against AlertDispatcher's id-dedup (was: same episode id
        # regenerated and swallowed).
        fake = _DedupDispatchFake()
        path = _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=fake)
        mon.check()
        _openclaw_store(tmp_path, [_oc_job(status="ok", consecutive=0)])
        mon.check()
        _openclaw_store(tmp_path, [_oc_job(status="error", consecutive=1)])
        mon.check()
        assert len(fake.delivered) == 2, "re-failure after recovery was dedup-swallowed"

    def test_hermes_jobs_reach_critical_via_observed_runs(self, tmp_path):
        # Hermes stores have no consecutiveErrors counter — escalation must
        # come from the monitor observing repeated failing RUNS (last_run
        # advancing while failing).
        spy = _DispatchSpy()
        for i, run_at in enumerate(["t1", "t2", "t3"]):
            job = _hermes_job(status="fail", error="down")
            job["last_run_at"] = run_at
            path = _hermes_store(tmp_path, [job])
            if i == 0:
                mon = CronStateMonitor({"hermes": path}, dispatch_fn=spy)
            else:
                mon._stores["hermes"] = path
            mon.check()
        severities = [a["severity"] for a in spy.alerts]
        assert severities == ["HIGH", "CRITICAL"]

    def test_job_name_capped_in_alert(self, tmp_path):
        spy = _DispatchSpy()
        path = _openclaw_store(
            tmp_path, [_oc_job(name="N" * 100_000, status="error", consecutive=1)]
        )
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy)
        mon.check()
        assert len(spy.alerts[0]["message"]) < 1000

    @pytest.mark.asyncio
    async def test_start_is_idempotent(self, tmp_path):
        spy = _DispatchSpy()
        path = _openclaw_store(tmp_path, [_oc_job()])
        mon = CronStateMonitor({"openclaw": path}, dispatch_fn=spy, interval_seconds=10)
        t1 = mon.start()
        t2 = mon.start()
        assert t1 is t2
        await mon.stop()
