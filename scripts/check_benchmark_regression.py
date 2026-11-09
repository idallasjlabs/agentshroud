#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Benchmark regression checker (SCRUM-201).

Reads the results JSON written by gateway/tests/test_benchmark_regression.py
(default .benchmarks/current.json) and compares it against the baseline
(default .benchmarks/baseline-v1.0.0.json). Exits non-zero when:

  * the baseline or current file is missing, empty or unparseable;
  * any expected metric is absent from the current results or non-numeric;
  * a gated mean is absent from the baseline;
  * any metric regressed by more than THRESHOLD against its baseline.

Means are always gated. P50/P99 are gated only when the baseline carries a
matching key (e.g. ``single_inbound_ms_p99``); otherwise they are reported
with "no baseline" and do not fail. The v1.0.0 baseline records means only.
A percentile baseline must be measured on the reference machine (the arm64
macOS host named in the baseline's _meta) and added to the baseline file —
never estimated.

Exit codes: 0 = all gated metrics within threshold, 1 = regression,
2 = missing/invalid data (the gate could not evaluate, which is not a pass).
"""

import argparse
import json
import sys
from pathlib import Path

THRESHOLD = 0.20  # 20% regression tolerance
BASELINE_PATH = Path(".benchmarks/baseline-v1.0.0.json")
CURRENT_PATH = Path(".benchmarks/current.json")

EXIT_OK = 0
EXIT_REGRESSION = 1
EXIT_MISSING = 2

# Current-results key -> baseline key. Always gated.
MEAN_METRICS = {
    "single_inbound_ms_mean": "single_inbound_ms",
    "single_outbound_ms_mean": "single_outbound_ms",
    "100_inbound_s": "100_inbound_s",
}

# Must be present in current results; gated only if the baseline has the same key.
PERCENTILE_METRICS = (
    "single_inbound_ms_p50",
    "single_inbound_ms_p99",
    "single_outbound_ms_p50",
    "single_outbound_ms_p99",
)


def _is_number(value) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _load_json(path: Path, label: str):
    """Return the parsed dict, or None after printing why it could not be loaded."""
    if not path.exists():
        print(f"  MISSING {label} file: {path}")
        return None
    content = path.read_text().strip()
    if not content:
        print(f"  MISSING {label} file is empty: {path}")
        return None
    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        print(f"  MISSING {label} file is not valid JSON: {path} ({exc})")
        return None
    if not isinstance(data, dict):
        print(f"  MISSING {label} file is not a JSON object: {path}")
        return None
    return data


def _compare(name: str, current: float, baseline: float, failures: list) -> None:
    regression = (current - baseline) / baseline
    sign = "+" if regression >= 0 else ""
    detail = (
        f"{name}: {current:.4f} vs baseline {baseline:.4f} ({sign}{regression * 100:.1f}%, "
        f"threshold {THRESHOLD * 100:.0f}%)"
    )
    if regression > THRESHOLD:
        failures.append(detail)
        print(f"  FAIL {detail}")
    else:
        print(f"  OK   {detail}")


def check(baseline_path: Path, current_path: Path) -> int:
    baseline = _load_json(baseline_path, "baseline")
    current = _load_json(current_path, "current")
    if baseline is None or current is None:
        print("\nBenchmark gate could not evaluate: required data missing.")
        return EXIT_MISSING

    missing = []
    failures = []

    for current_key, baseline_key in MEAN_METRICS.items():
        cur = current.get(current_key)
        base = baseline.get(baseline_key)
        if not _is_number(cur):
            missing.append(f"current[{current_key}]={cur!r}")
            print(f"  MISSING {current_key}: not a number in current results ({cur!r})")
            continue
        if not _is_number(base) or base <= 0:
            missing.append(f"baseline[{baseline_key}]={base!r}")
            print(f"  MISSING {baseline_key}: no positive baseline value ({base!r})")
            continue
        _compare(current_key, cur, base, failures)

    for metric in PERCENTILE_METRICS:
        cur = current.get(metric)
        if not _is_number(cur):
            missing.append(f"current[{metric}]={cur!r}")
            print(f"  MISSING {metric}: not a number in current results ({cur!r})")
            continue
        base = baseline.get(metric)
        if _is_number(base) and base > 0:
            _compare(metric, cur, base, failures)
        else:
            print(
                f"  INFO {metric}: {cur:.4f} (no baseline recorded — reported, not gated; "
                "record it on the reference machine)"
            )

    if missing:
        print(f"\n{len(missing)} expected metric(s) missing: {', '.join(missing)}")
        return EXIT_MISSING
    if failures:
        print(f"\n{len(failures)} benchmark(s) regressed beyond threshold. See details above.")
        return EXIT_REGRESSION
    print("\nAll gated benchmarks within threshold. No regression detected.")
    return EXIT_OK


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--baseline", type=Path, default=BASELINE_PATH)
    parser.add_argument("--current", type=Path, default=CURRENT_PATH)
    args = parser.parse_args(argv)
    return check(args.baseline, args.current)


if __name__ == "__main__":
    sys.exit(main())
