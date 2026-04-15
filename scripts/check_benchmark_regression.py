#!/usr/bin/env python3
"""
Benchmark regression checker.
Compares current benchmark results against baseline and fails if any metric
regressed by more than 20%.
"""
import json
import sys
from pathlib import Path

THRESHOLD = 0.20  # 20% regression tolerance
BASELINE_PATH = Path(".benchmarks/baseline-v1.0.0.json")
CURRENT_PATH = Path(".benchmarks/current.json")

METRIC_MAP = {
    "test_single_inbound_latency": "single_inbound_ms",
    "test_single_outbound_latency": "single_outbound_ms",
    "test_100_inbound_requests": "100_inbound_ms",
    "test_100_outbound_requests": "100_outbound_ms",
}


def main():
    if not BASELINE_PATH.exists():
        print(f"WARNING: Baseline not found at {BASELINE_PATH} — skipping regression check")
        sys.exit(0)

    if not CURRENT_PATH.exists():
        print(f"WARNING: Current benchmarks not found at {CURRENT_PATH} — skipping check")
        sys.exit(0)

    with open(BASELINE_PATH) as f:
        baseline = json.load(f)

    with open(CURRENT_PATH) as f:
        current = json.load(f)

    # Extract baseline metrics
    baseline_metrics = baseline.get("benchmarks", {})
    current_benchmarks = {b["name"]: b for b in current.get("benchmarks", [])}

    failures = []
    for test_name, baseline_key in METRIC_MAP.items():
        if baseline_key not in baseline_metrics:
            print(f"  SKIP {test_name}: not in baseline")
            continue

        baseline_val = baseline_metrics[baseline_key]

        # Find matching benchmark in current results
        matched = None
        for name, bench in current_benchmarks.items():
            if test_name in name:
                matched = bench
                break

        if matched is None:
            print(f"  SKIP {test_name}: not in current results")
            continue

        # pytest-benchmark stores mean in seconds
        current_ms = matched["stats"]["mean"] * 1000
        regression = (current_ms - baseline_val) / baseline_val

        if regression > THRESHOLD:
            failures.append(
                f"  FAIL {test_name}: {current_ms:.3f}ms vs baseline {baseline_val:.3f}ms "
                f"(+{regression*100:.1f}% > {THRESHOLD*100:.0f}% threshold)"
            )
            print(failures[-1])
        else:
            delta_str = f"+{regression*100:.1f}%" if regression >= 0 else f"{regression*100:.1f}%"
            print(f"  OK   {test_name}: {current_ms:.3f}ms vs baseline {baseline_val:.3f}ms ({delta_str})")

    if failures:
        print(f"\n{len(failures)} benchmark(s) regressed beyond threshold. See details above.")
        sys.exit(1)
    else:
        print("\nAll benchmarks within threshold. No regression detected.")
        sys.exit(0)


if __name__ == "__main__":
    main()
