# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/soak_status.py's classify() — the soak-period gate.

This gate exists because post-deploy-check.sh only proves the stack booted,
not that anything real actually ran successfully on it. The
models.json/openai-local, missing-sandbox-image, and op-proxy-allowlist bugs
fixed 2026-09-18 were all invisible to boot-only checks; this is the gate
that should catch that class of bug before a dev build is promoted to prod.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_SCRIPT_PATH = Path(__file__).parent.parent.parent / "scripts" / "soak_status.py"
_spec = importlib.util.spec_from_file_location("soak_status", _SCRIPT_PATH)
soak_status = importlib.util.module_from_spec(_spec)
sys.modules["soak_status"] = soak_status
_spec.loader.exec_module(soak_status)

classify = soak_status.classify


def _job(name, status, last_run_at_ms, last_error=None):
    return {
        "name": name,
        "status": status,
        "state": {"lastRunAtMs": last_run_at_ms, "lastError": last_error},
    }


class TestClassify:
    def test_no_runs_since_boot_not_soaked(self):
        jobs = [_job("memory-dream", "ok", last_run_at_ms=100)]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is False
        assert "only 0/1" in message

    def test_one_success_since_boot_meets_default_threshold(self):
        jobs = [_job("heartbeat-main", "ok", last_run_at_ms=300)]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is True
        assert "1 successful run" in message

    def test_below_threshold_not_soaked(self):
        jobs = [_job("heartbeat-main", "ok", last_run_at_ms=300)]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=3)
        assert soaked is False
        assert "only 1/3" in message

    def test_any_error_since_boot_blocks_regardless_of_successes(self):
        """An actively-failing job since redeploy must block soak even if
        other jobs succeeded — a partial regression is still a regression."""
        jobs = [
            _job("heartbeat-main", "error", last_run_at_ms=300, last_error="agent-runner-failure"),
            _job("memory-dream", "ok", last_run_at_ms=310),
            _job("memory-dream-2", "ok", last_run_at_ms=320),
        ]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is False
        assert "errored_since_boot" in message
        assert "heartbeat-main" in message
        assert "agent-runner-failure" in message

    def test_skipped_status_counts_as_not_ok(self):
        """The 2026-09-18 heartbeat regression showed status='skipped', not
        'error' — must not be misclassified as a success."""
        jobs = [_job("heartbeat-main", "skipped", last_run_at_ms=300, last_error="empty-heartbeat-file")]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is False
        assert "skipped" in message

    def test_runs_before_boot_are_ignored(self):
        """A job that last succeeded before this boot proves nothing about
        THIS deploy — must not count toward the threshold."""
        jobs = [_job("memory-dream", "ok", last_run_at_ms=50)]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is False

    def test_empty_job_list(self):
        soaked, message = classify([], started_at_ms=200, min_successes=1)
        assert soaked is False

    def test_missing_state_key_does_not_crash(self):
        jobs = [{"name": "malformed-job", "status": "idle"}]
        soaked, message = classify(jobs, started_at_ms=200, min_successes=1)
        assert soaked is False
