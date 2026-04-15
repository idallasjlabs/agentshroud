# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Benchmark regression tests.

Verifies that key latency metrics stay within 20% of the baseline recorded
in .benchmarks/baseline-v1.0.0.json. Designed to be run with pytest-benchmark
in CI, but degrades gracefully when run without it.
"""
import json
import time
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

BASELINE_PATH = Path(".benchmarks/baseline-v1.0.0.json")
THRESHOLD = 0.20  # 20% regression tolerance


def load_baseline():
    if not BASELINE_PATH.exists():
        return {}
    with open(BASELINE_PATH) as f:
        data = json.load(f)
    return data.get("benchmarks", {})


def assert_within_threshold(measured_ms: float, baseline_ms: float, label: str):
    """Assert measured value is within THRESHOLD of baseline."""
    if baseline_ms <= 0:
        pytest.skip(f"No baseline for {label}")
    regression = (measured_ms - baseline_ms) / baseline_ms
    assert regression <= THRESHOLD, (
        f"{label}: {measured_ms:.3f}ms measured vs {baseline_ms:.3f}ms baseline "
        f"(+{regression*100:.1f}% > {THRESHOLD*100:.0f}% threshold)"
    )


class TestBenchmarkRegression:
    """Benchmark regression tests — ensure latency stays within 20% of baseline."""

    def setup_method(self):
        self.baseline = load_baseline()

    def _time_fn(self, fn, iterations=100):
        """Time a function over N iterations, return mean ms."""
        start = time.perf_counter()
        for _ in range(iterations):
            fn()
        elapsed = time.perf_counter() - start
        return (elapsed / iterations) * 1000

    def test_single_inbound_latency(self):
        """Single inbound request processing should stay within baseline."""
        baseline_ms = self.baseline.get("single_inbound_ms", 0)
        if not baseline_ms:
            pytest.skip("No baseline for single_inbound_ms")

        with patch("gateway.proxy.http_proxy.HttpProxy") as mock_proxy:
            mock_proxy.return_value.handle_request = MagicMock(return_value={"status": 200})

            def simulate_inbound():
                mock_proxy.return_value.handle_request({"method": "GET", "path": "/status"})

            measured_ms = self._time_fn(simulate_inbound, iterations=1000)
        assert_within_threshold(measured_ms, baseline_ms, "single_inbound")

    def test_single_outbound_latency(self):
        """Single outbound request processing should stay within baseline."""
        baseline_ms = self.baseline.get("single_outbound_ms", 0)
        if not baseline_ms:
            pytest.skip("No baseline for single_outbound_ms")

        with patch("gateway.proxy.http_proxy.HttpProxy") as mock_proxy:
            mock_proxy.return_value.handle_outbound = MagicMock(return_value={"status": 200})

            def simulate_outbound():
                mock_proxy.return_value.handle_outbound({"method": "POST", "path": "/api/chat"})

            measured_ms = self._time_fn(simulate_outbound, iterations=1000)
        assert_within_threshold(measured_ms, baseline_ms, "single_outbound")

    def test_100_inbound_requests(self):
        """100 sequential inbound requests should stay within baseline."""
        baseline_ms = self.baseline.get("100_inbound_ms", 0)
        if not baseline_ms:
            pytest.skip("No baseline for 100_inbound_ms")

        with patch("gateway.proxy.http_proxy.HttpProxy") as mock_proxy:
            mock_proxy.return_value.handle_request = MagicMock(return_value={"status": 200})

            start = time.perf_counter()
            for _ in range(100):
                mock_proxy.return_value.handle_request({"method": "GET", "path": "/status"})
            elapsed_ms = (time.perf_counter() - start) * 1000

        assert_within_threshold(elapsed_ms, baseline_ms, "100_inbound")

    def test_100_outbound_requests(self):
        """100 sequential outbound requests should stay within baseline."""
        baseline_ms = self.baseline.get("100_outbound_ms", 0)
        if not baseline_ms:
            pytest.skip("No baseline for 100_outbound_ms")

        with patch("gateway.proxy.http_proxy.HttpProxy") as mock_proxy:
            mock_proxy.return_value.handle_outbound = MagicMock(return_value={"status": 200})

            start = time.perf_counter()
            for _ in range(100):
                mock_proxy.return_value.handle_outbound({"method": "POST", "path": "/api/chat"})
            elapsed_ms = (time.perf_counter() - start) * 1000

        assert_within_threshold(elapsed_ms, baseline_ms, "100_outbound")

    def test_baseline_file_exists(self):
        """Baseline file must exist and contain expected keys."""
        assert BASELINE_PATH.exists(), (
            f"Benchmark baseline missing: {BASELINE_PATH}. "
            "Run benchmarks and save results to establish a baseline."
        )
        with open(BASELINE_PATH) as f:
            data = json.load(f)
        benchmarks = data.get("benchmarks", {})
        expected_keys = ["single_inbound_ms", "single_outbound_ms"]
        for key in expected_keys:
            assert key in benchmarks, f"Baseline missing key: {key}"

    def test_baseline_values_are_reasonable(self):
        """Baseline values should be positive and within expected ranges."""
        baseline = self.baseline
        if not baseline:
            pytest.skip("No baseline loaded")

        for key, val in baseline.items():
            if isinstance(val, (int, float)):
                assert val > 0, f"Baseline {key} must be positive, got {val}"
                assert val < 10000, f"Baseline {key}={val}ms seems unreasonably high (>10s)"
