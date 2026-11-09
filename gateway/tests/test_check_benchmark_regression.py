# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Tests for scripts/check_benchmark_regression.py (SCRUM-201).

The checker used to SKIP every metric (its METRIC_MAP named keys the harness
never emitted) and still exit 0 — a gate that could not fail. These tests pin
the contract: missing data fails, regression fails, only in-threshold passes.
"""

import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "check_benchmark_regression.py"


def _load_checker():
    spec = importlib.util.spec_from_file_location("check_benchmark_regression", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checker = _load_checker()

BASELINE = {
    "single_inbound_ms": 0.44,
    "single_outbound_ms": 0.28,
    "100_inbound_s": 0.03,
    "_meta": {"version": "1.0.0"},
}


def _current(**overrides):
    data = {
        "single_inbound_ms_mean": 0.40,
        "single_inbound_ms_p50": 0.39,
        "single_inbound_ms_p99": 0.90,
        "single_outbound_ms_mean": 0.25,
        "single_outbound_ms_p50": 0.24,
        "single_outbound_ms_p99": 0.60,
        "100_inbound_s": 0.025,
    }
    data.update(overrides)
    return {k: v for k, v in data.items() if v is not None}


def _run(tmp_path, baseline, current):
    b = tmp_path / "baseline.json"
    c = tmp_path / "current.json"
    if baseline is not None:
        b.write_text(json.dumps(baseline))
    if current is not None:
        c.write_text(current if isinstance(current, str) else json.dumps(current))
    return checker.main(["--baseline", str(b), "--current", str(c)])


def test_within_threshold_exits_zero(tmp_path, capsys):
    assert _run(tmp_path, BASELINE, _current()) == 0
    out = capsys.readouterr().out
    assert "single_inbound_ms_mean" in out
    assert "SKIP" not in out


def test_regression_beyond_threshold_exits_nonzero(tmp_path, capsys):
    # 0.44 * 1.25 = 0.55 -> +25% > 20%
    assert _run(tmp_path, BASELINE, _current(single_inbound_ms_mean=0.55)) != 0
    assert "FAIL" in capsys.readouterr().out


def test_regression_just_under_threshold_exits_zero(tmp_path):
    # 0.44 * 1.19 = 0.5236 -> +19%
    assert _run(tmp_path, BASELINE, _current(single_inbound_ms_mean=0.5236)) == 0


def test_batch_metric_regression_exits_nonzero(tmp_path):
    assert _run(tmp_path, BASELINE, _current(**{"100_inbound_s": 0.05})) != 0


@pytest.mark.parametrize(
    "missing", ["single_inbound_ms_mean", "single_outbound_ms_mean", "100_inbound_s"]
)
def test_missing_expected_metric_exits_nonzero(tmp_path, capsys, missing):
    assert _run(tmp_path, BASELINE, _current(**{missing: None})) != 0
    assert "MISSING" in capsys.readouterr().out


def test_missing_percentile_metric_exits_nonzero(tmp_path):
    assert _run(tmp_path, BASELINE, _current(single_inbound_ms_p99=None)) != 0


def test_missing_current_file_exits_nonzero(tmp_path):
    assert _run(tmp_path, BASELINE, None) != 0


def test_empty_current_file_exits_nonzero(tmp_path):
    assert _run(tmp_path, BASELINE, "") != 0


def test_missing_baseline_file_exits_nonzero(tmp_path):
    assert _run(tmp_path, None, _current()) != 0


def test_baseline_missing_mean_key_exits_nonzero(tmp_path):
    baseline = {k: v for k, v in BASELINE.items() if k != "single_outbound_ms"}
    assert _run(tmp_path, baseline, _current()) != 0


def test_percentiles_without_baseline_are_reported_not_failed(tmp_path, capsys):
    # Baseline has no p99 keys: a huge P99 is reported, not gated.
    assert _run(tmp_path, BASELINE, _current(single_inbound_ms_p99=50.0)) == 0
    out = capsys.readouterr().out
    assert "single_inbound_ms_p99" in out
    assert "no baseline" in out.lower()


def test_percentile_regression_against_recorded_baseline_exits_nonzero(tmp_path):
    baseline = dict(BASELINE, single_inbound_ms_p99=0.90)
    assert _run(tmp_path, baseline, _current(single_inbound_ms_p99=1.20)) != 0


def test_non_numeric_metric_exits_nonzero(tmp_path):
    assert _run(tmp_path, BASELINE, _current(single_inbound_ms_mean="fast")) != 0


def test_real_baseline_has_every_gated_mean_key():
    """The shipped baseline must carry every mean key the checker gates on."""
    baseline = json.loads((SCRIPT.parents[1] / ".benchmarks" / "baseline-v1.0.0.json").read_text())
    for baseline_key in checker.MEAN_METRICS.values():
        assert baseline_key in baseline, baseline_key
