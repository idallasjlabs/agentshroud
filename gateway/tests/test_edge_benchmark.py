# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — gateway-side latency, P50/P99 (SCRUM-218).

Times ``EdgeCallPipeline.call_tool`` for a read call end to end through the real
modules: ES256 verification + jti/kill lookups (SQLite), schema, limits, P0
(PromptGuard + EncodingDetector over raw/normalised/decoded leaves), canary scan,
per-leaf DLP + credential scrub, size cap and the hash-chained audit write. Only
the facade is fake, so network time to SearXNG is excluded.

There is no recorded baseline yet; the test reports the numbers and asserts a
generous ceiling that only catches pathological regressions. Record a baseline on
the reference arm64/macOS machine before tightening it.
"""

import statistics
import time

from gateway.tests.test_edge_pipeline import _token, edge  # noqa: F401  (fixture reuse)

ITERATIONS = 300
P99_CEILING_MS = 50.0


def _pct(samples, p):
    s = sorted(samples)
    return s[max(1, -(-len(s) * p // 100)) - 1]


async def test_edge_read_call_latency(edge, capsys):  # noqa: F811
    pipe, deps, *_ = edge
    deps.profiles["claude-duet"] = deps.profiles["claude-duet"].__class__(
        **{
            **deps.profiles["claude-duet"].__dict__,
            "per_client_per_minute": 10_000,
            "per_vendor_per_minute": 10_000,
            "daily_calls": 100_000,
        }
    )
    token = await _token(deps)
    for i in range(20):
        await pipe.call_tool(token, "lab_search", {"query": "weather saturday"}, f"w{i}")
    samples = []
    for i in range(ITERATIONS):
        t = time.perf_counter()
        r = await pipe.call_tool(token, "lab_search", {"query": "weather saturday"}, f"b{i}")
        samples.append((time.perf_counter() - t) * 1000)
        assert not r["isError"]
    p50, p99 = _pct(samples, 50), _pct(samples, 99)
    with capsys.disabled():
        print(
            f"\nedge read call: mean={statistics.fmean(samples):.3f}ms "
            f"p50={p50:.3f}ms p99={p99:.3f}ms n={ITERATIONS}"
        )
    assert p99 < P99_CEILING_MS
