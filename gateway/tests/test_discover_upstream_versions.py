"""Tests for scripts/discover_upstream_versions.py — latest-release discovery.

Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
Patent Pending — U.S. Provisional Application No. 64/018,744

Why this module exists at all: for seven weeks every Sunday upgrade reported
PASS while rebuilding the SAME upstream version, because nothing in the
pipeline ever asked what the latest release was — version selection was left to
an LLM session's judgement and silently never happened. OPENCLAW_VERSION moved
exactly once between 2026-07-29 and 2026-09-15, and only to a downstream
rebuild counter.

These cover the PURE selection logic (which version wins, which are rejected).
Network fetches are exercised via injected payloads — no test here touches npm
or Docker Hub.
"""

from __future__ import annotations

import socket
import sys
import threading
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

import pytest  # noqa: E402
from discover_upstream_versions import (  # noqa: E402
    _call_with_deadline,
    _guarded_fetch,
    _ipv4_only,
    _retry,
    discover,
    is_stable,
    pick_latest_hermes_tag,
    pick_latest_stable,
)


class TestIsStable:
    """Pre-release builds must never be shipped to production automatically."""

    def test_plain_releases_are_stable(self):
        assert is_stable("2026.9.4")
        assert is_stable("2026.8.1")

    def test_downstream_rebuild_counter_is_stable(self):
        """'2026.7.1-2' is a real published OpenClaw release, not a prerelease
        marker — the running container reports exactly this string."""
        assert is_stable("2026.7.1-2")

    def test_beta_rc_alpha_are_not_stable(self):
        assert not is_stable("2026.9.1-beta.1")
        assert not is_stable("2026.8.1-beta.3")
        assert not is_stable("2026.7.2-rc.1")
        assert not is_stable("2026.7.2-alpha")
        assert not is_stable("1.0.0-dev")
        assert not is_stable("2026.9.1-NEXT")  # case-insensitive

    def test_empty_is_not_stable(self):
        assert not is_stable("")
        assert not is_stable(None)


class TestPickLatestStable:
    """Selecting the newest shippable npm release."""

    def test_picks_the_highest_stable_version(self):
        versions = ["2026.8.1", "2026.9.4", "2026.9.2", "2026.8.2"]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_ignores_prereleases_even_when_numerically_highest(self):
        versions = ["2026.9.4", "2026.9.5-beta.1", "2026.9.5-rc.2"]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_real_openclaw_tail_picks_2026_9_4(self):
        """The actual npm tail as of 2026-09-15."""
        versions = [
            "2026.7.2-beta.6",
            "2026.7.2-beta.7",
            "2026.8.1-beta.1",
            "2026.8.1-beta.2",
            "2026.8.1-beta.3",
            "2026.8.1",
            "2026.8.2",
            "2026.9.1-beta.1",
            "2026.9.1",
            "2026.9.2",
            "2026.9.3",
            "2026.9.4",
        ]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_numeric_ordering_not_lexicographic(self):
        """'2026.10.1' must beat '2026.9.4' — string compare gets this wrong."""
        assert pick_latest_stable(["2026.9.4", "2026.10.1"]) == "2026.10.1"

    def test_downstream_counter_sorts_above_its_base_release(self):
        """2026.7.1-2 is a patch published after 2026.7.1, so it must win."""
        assert pick_latest_stable(["2026.7.1", "2026.7.1-2"]) == "2026.7.1-2"

    def test_unparseable_entries_are_skipped_not_crashed_on(self):
        assert pick_latest_stable(["garbage", "2026.9.4", ""]) == "2026.9.4"

    def test_no_stable_versions_returns_none(self):
        assert pick_latest_stable(["1.0.0-beta.1", "2.0.0-rc.1"]) is None

    def test_empty_returns_none(self):
        assert pick_latest_stable([]) is None


class TestPickLatestHermesTag:
    """Hermes publishes date-based image tags (vYYYY.M.D)."""

    def test_picks_newest_date_tag(self):
        tags = ["latest", "main", "v2026.9.14", "v2026.9.11", "v2026.8.31"]
        assert pick_latest_hermes_tag(tags) == "v2026.9.14"

    def test_rejects_floating_tags(self):
        """'latest'/'main' float and would defeat the whole point of pinning."""
        assert pick_latest_hermes_tag(["latest", "main"]) is None

    def test_handles_four_component_tags(self):
        tags = ["v2026.8.16", "v2026.8.16.2"]
        assert pick_latest_hermes_tag(tags) == "v2026.8.16.2"

    def test_real_hermes_tail_picks_latest_date(self):
        tags = [
            "latest",
            "main",
            "v2026.9.14",
            "v2026.9.11",
            "v2026.9.7",
            "v2026.8.31",
            "v2026.8.16.2",
            "v2026.7.7.2",
        ]
        assert pick_latest_hermes_tag(tags) == "v2026.9.14"

    def test_empty_returns_none(self):
        assert pick_latest_hermes_tag([]) is None


class TestRetry:
    """Upstream fetches must survive a transient blip.

    2026-10-16, dev host marvin: two consecutive runs of this script failed
    the Hermes lookup ("<urlopen error timed out>", then
    "SSL: UNEXPECTED_EOF_WHILE_READING") while the identical URL succeeded
    10/10 immediately before and after from both curl and urllib. This host
    has a documented pattern of intermittent transport failures (see
    scripts/sunday-upgrade.sh's git-fetch retry loop). A single-shot fetch
    turns one blip into "Hermes latest = UNKNOWN" for the whole unattended
    Sunday run, which the no-op gate then cannot catch.
    """

    def test_returns_result_after_transient_failures(self):
        calls = {"n": 0}

        def flaky(_attempt):
            calls["n"] += 1
            if calls["n"] < 3:
                raise OSError("transient")
            return "ok"

        slept: list[float] = []
        assert _retry(flaky, attempts=4, delays=(5, 10, 20), sleep=slept.append) == "ok"
        assert calls["n"] == 3
        assert slept == [5, 10]

    def test_gives_up_after_attempts_and_reraises_last_error(self):
        calls = {"n": 0}

        def always_fails(_attempt):
            calls["n"] += 1
            raise OSError(f"boom {calls['n']}")

        slept: list[float] = []
        with pytest.raises(OSError, match="boom 4"):
            _retry(always_fails, attempts=4, delays=(5, 10, 20), sleep=slept.append)
        assert calls["n"] == 4
        assert slept == [5, 10, 20]

    def test_single_attempt_never_sleeps(self):
        slept: list[float] = []
        with pytest.raises(OSError):
            _retry(
                lambda _i: (_ for _ in ()).throw(OSError("x")),
                attempts=1,
                sleep=slept.append,
            )
        assert slept == []

    def test_passes_zero_based_attempt_index(self):
        seen: list[int] = []

        def fn(attempt):
            seen.append(attempt)
            if attempt < 2:
                raise OSError("again")
            return attempt

        assert _retry(fn, attempts=3, delays=(0,), sleep=lambda _s: None) == 2
        assert seen == [0, 1, 2]


class TestCallWithDeadline:
    """A fetch that never returns must not hang the unattended run.

    2026-10-16: the Sunday job's python3 (Homebrew 3.15 / OpenSSL 4.0.3) sat
    10+ minutes at 0% CPU inside one urlopen(timeout=60) to hub.docker.com,
    socket in CLOSE_WAIT on an IPv6 address — the socket timeout never fired.
    """

    def test_returns_value_when_fn_finishes_in_time(self):
        assert _call_with_deadline(lambda: "done", seconds=5) == "done"

    def test_propagates_fn_exception(self):
        def boom():
            raise OSError("SSL: UNEXPECTED_EOF_WHILE_READING")

        with pytest.raises(OSError, match="UNEXPECTED_EOF"):
            _call_with_deadline(boom, seconds=5)

    def test_raises_timeout_when_fn_hangs(self):
        release = threading.Event()
        try:
            with pytest.raises(TimeoutError, match="hard deadline"):
                _call_with_deadline(release.wait, seconds=0.05)
        finally:
            release.set()  # free the abandoned daemon thread


class TestIPv4Only:
    """Every Docker Hub failure on marvin was on IPv6; curl -4 was 100% clean."""

    def test_forces_af_inet_inside_block_and_restores_after(self, monkeypatch):
        seen: list[tuple] = []

        def recorder(host, port, family=0, type=0, proto=0, flags=0):
            seen.append((host, port, family))
            return []

        monkeypatch.setattr(socket, "getaddrinfo", recorder)
        with _ipv4_only():
            socket.getaddrinfo("hub.docker.com", 443)
            assert socket.getaddrinfo is not recorder
        assert seen == [("hub.docker.com", 443, socket.AF_INET)]
        assert socket.getaddrinfo is recorder  # restored on exit

    def test_restores_even_when_block_raises(self, monkeypatch):
        def recorder(host, port, family=0, type=0, proto=0, flags=0):
            return []

        monkeypatch.setattr(socket, "getaddrinfo", recorder)
        with pytest.raises(RuntimeError), _ipv4_only():
            raise RuntimeError("inside")
        assert socket.getaddrinfo is recorder


class TestGuardedFetch:
    def test_first_attempt_keeps_default_resolver(self, monkeypatch):
        def recorder(host, port, family=0, type=0, proto=0, flags=0):
            return []

        monkeypatch.setattr(socket, "getaddrinfo", recorder)
        observed = {}

        def fetch():
            observed["resolver_is_default"] = socket.getaddrinfo is recorder
            return "ok"

        assert _guarded_fetch(fetch, attempt=0, deadline=5) == "ok"
        assert observed["resolver_is_default"] is True

    def test_retry_attempts_force_ipv4(self, monkeypatch):
        def recorder(host, port, family=0, type=0, proto=0, flags=0):
            return []

        monkeypatch.setattr(socket, "getaddrinfo", recorder)
        observed = {}

        def fetch():
            observed["resolver_is_default"] = socket.getaddrinfo is recorder
            return "ok"

        assert _guarded_fetch(fetch, attempt=1, deadline=5) == "ok"
        assert observed["resolver_is_default"] is False
        assert socket.getaddrinfo is recorder

    def test_hang_is_cut_by_deadline(self):
        release = threading.Event()
        try:
            with pytest.raises(TimeoutError):
                _guarded_fetch(release.wait, attempt=0, deadline=0.05)
        finally:
            release.set()


class TestDiscoverRetries:
    """discover() applies the retry to both sources, independently."""

    _TAGS = [
        {"name": "latest", "digest": "sha256:aaa"},
        {"name": "v0.22.2", "digest": "sha256:bbb"},
        {"name": "v0.21.5", "digest": "sha256:ccc"},
    ]

    def test_hermes_recovers_from_one_transient_failure(self):
        calls = {"n": 0}

        def hub():
            calls["n"] += 1
            if calls["n"] == 1:
                raise OSError("<urlopen error timed out>")
            return list(self._TAGS)

        found = discover(fetch_npm=lambda: ["2026.10.4"], fetch_hub=hub, sleep=lambda _s: None)
        assert found["hermes"]["latest"] == "v0.22.2"
        assert found["hermes"]["digest"] == "sha256:bbb"
        assert found["hermes"]["error"] is None
        assert found["openclaw"]["latest"] == "2026.10.4"
        assert calls["n"] == 2

    def test_hermes_failure_is_reported_as_unknown_after_exhaustion(self):
        def hub():
            raise OSError("SSL: UNEXPECTED_EOF_WHILE_READING")

        found = discover(fetch_npm=lambda: ["2026.10.4"], fetch_hub=hub, sleep=lambda _s: None)
        assert found["hermes"]["latest"] is None
        assert found["hermes"]["digest"] is None
        assert "UNEXPECTED_EOF" in found["hermes"]["error"]
        # One source failing must never mask the other.
        assert found["openclaw"]["latest"] == "2026.10.4"
        assert found["openclaw"]["error"] is None

    def test_openclaw_recovers_from_one_transient_failure(self):
        calls = {"n": 0}

        def npm():
            calls["n"] += 1
            if calls["n"] == 1:
                raise RuntimeError("npm view openclaw failed: ETIMEDOUT")
            return ["2026.10.2", "2026.10.4"]

        found = discover(fetch_npm=npm, fetch_hub=lambda: list(self._TAGS), sleep=lambda _s: None)
        assert found["openclaw"]["latest"] == "2026.10.4"
        assert found["openclaw"]["error"] is None
        assert calls["n"] == 2

    def test_hung_hub_fetch_is_cut_by_deadline_and_retried(self):
        """The 2026-10-16 CLOSE_WAIT hang: attempt 1 never returns; the hard
        deadline must cut it and attempt 2 (IPv4-forced) must succeed."""
        release = threading.Event()
        calls = {"n": 0}

        def hub():
            calls["n"] += 1
            if calls["n"] == 1:
                release.wait()  # hangs until the test releases it
                return []
            return list(self._TAGS)

        try:
            found = discover(
                fetch_npm=lambda: ["2026.10.4"],
                fetch_hub=hub,
                sleep=lambda _s: None,
                deadline=0.05,
            )
        finally:
            release.set()
        assert found["hermes"]["latest"] == "v0.22.2"
        assert found["hermes"]["error"] is None
        assert calls["n"] == 2

    def test_retry_attempt_runs_with_ipv4_forced(self, monkeypatch):
        def recorder(host, port, family=0, type=0, proto=0, flags=0):
            return []

        monkeypatch.setattr(socket, "getaddrinfo", recorder)
        resolver_default_per_call: list[bool] = []

        def hub():
            resolver_default_per_call.append(socket.getaddrinfo is recorder)
            if len(resolver_default_per_call) == 1:
                raise OSError("<urlopen error timed out>")
            return list(self._TAGS)

        found = discover(fetch_npm=lambda: ["2026.10.4"], fetch_hub=hub, sleep=lambda _s: None)
        assert found["hermes"]["latest"] == "v0.22.2"
        assert resolver_default_per_call == [True, False]
        assert socket.getaddrinfo is recorder
