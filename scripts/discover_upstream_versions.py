#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Discover the latest upstream releases of the tools AgentShroud wraps.

WHY THIS EXISTS (owner escalation 2026-09-15)
---------------------------------------------
For seven weeks every Sunday upgrade reported PASS while rebuilding the SAME
upstream version. OPENCLAW_VERSION was introduced as 2026.7.1 on 2026-07-29 and
moved exactly once since — to 2026.7.1-2, a downstream rebuild counter — while
npm had shipped 2026.8.1, 2026.8.2, 2026.9.1, 2026.9.2, 2026.9.3 and 2026.9.4.
HERMES_VERSION moved once, in a feature PR, never in a Sunday run.

The cause was architectural, not an oversight by any one run:
sunday-upgrade-apply.sh says of itself "the agent proposes versions; this script
disposes" — it builds whatever docker/versions.env already says and never asks
what the latest release is. Version discovery was delegated to an LLM session's
judgement, and the deterministic gates then verified only that the rebuild
worked. Rebuilding an identical version passes every one of those gates.

So discovery belongs HERE: mechanical, verifiable, no judgement required.

Sources (authoritative, matching how each tool is actually installed):
  OpenClaw — the npm registry. docker/bots/openclaw/Dockerfile:141 runs
             `npm install -g openclaw@${OPENCLAW_VERSION}` and then asserts the
             installed version equals the pin, so npm IS the source of truth.
  Hermes   — Docker Hub tags for nousresearch/hermes-agent, which publishes
             date-based tags (vYYYY.M.D). docker/versions.env pins an immutable
             sha256 digest; this resolves the newest tag and its digest.

Stable only: a pre-release (-beta/-rc/-alpha/-dev/-next) is never proposed for
an unattended production upgrade.

Usage:
    python3 scripts/discover_upstream_versions.py              # human report
    python3 scripts/discover_upstream_versions.py --json
    python3 scripts/discover_upstream_versions.py --shell      # KEY=VALUE for bash eval

Exit codes:
    0  discovery succeeded (whether or not anything is behind)
    1  no source could be reached — callers must treat this as "unknown",
       never as "already current"
"""

from __future__ import annotations

import argparse
import contextlib
import json
import re
import socket
import subprocess
import sys
import threading
import time
from collections.abc import Callable, Iterator
from typing import Any, Optional, TypeVar

_T = TypeVar("_T")

# Hard wall-clock bound per fetch attempt, enforced from OUTSIDE the call.
# 2026-10-16 on marvin: the Sunday job's `python3` (Homebrew 3.15 / OpenSSL
# 4.0.3) sat for 10+ minutes at 0% CPU inside a single urlopen(timeout=60) to
# hub.docker.com — the socket was in CLOSE_WAIT on an IPv6 Cloudflare address
# and the read never returned. A socket timeout does not cover every state an
# SSL read can block in, and urllib also walks every resolved address
# sequentially (an attempt with timeout=20 was observed to take 84s). An
# unattended run has no one to notice a hang; it would sit until
# sunday-upgrade.sh's 180-minute watchdog killed the whole session.
FETCH_DEADLINE_S = 90.0

# Set inside _ipv4_only(); read by curl-based fetches, which bypass getaddrinfo.
_FORCE_IPV4 = False

# Bounded retry for the two upstream fetches. 2026-10-16 on marvin: two
# consecutive runs failed the Hermes lookup ("<urlopen error timed out>", then
# "SSL: UNEXPECTED_EOF_WHILE_READING") while the identical URL succeeded 10/10
# from both urllib and curl immediately before and after. This host has a
# documented pattern of intermittent transport failures (scripts/sunday-
# upgrade.sh retries `git fetch` 5x for the same reason). A single-shot fetch
# turns one blip into "latest = UNKNOWN" for the whole unattended Sunday run,
# and the no-op gate in sunday-upgrade-apply.sh then cannot tell "behind" from
# "already current". ~35s of total backoff is negligible against a weekly job.
RETRY_ATTEMPTS = 4
RETRY_DELAYS: tuple[float, ...] = (5, 10, 20)

NPM_PACKAGE = "openclaw"
HERMES_REPO = "nousresearch/hermes-agent"
DOCKERHUB_TAGS = (
    "https://hub.docker.com/v2/repositories/{repo}/tags" "?page_size=100&ordering=last_updated"
)

# A hyphenated suffix that is a pure integer is a downstream patch release
# (OpenClaw publishes e.g. 2026.7.1-2 as a real release; the running container
# reports exactly that string). Anything alphabetic after the hyphen is a
# pre-release and must never ship unattended.
_PRERELEASE_RE = re.compile(r"-(?![0-9]+$)", re.IGNORECASE)
_HERMES_TAG_RE = re.compile(r"^v(\d+(?:\.\d+)+)$")


# ── pure selection logic ──────────────────────────────────────────────────────
def is_stable(version: Optional[str]) -> bool:
    """True when ``version`` is a shippable release rather than a pre-release."""
    if not version:
        return False
    return not _PRERELEASE_RE.search(version)


def _sortable(version: str) -> Optional[tuple[int, ...]]:
    """Version -> comparable int tuple, or None if not numeric.

    A trailing ``-N`` patch counter becomes an extra component so that
    2026.7.1-2 sorts ABOVE 2026.7.1, which is the real publication order.
    """
    base, _, suffix = version.partition("-")
    try:
        parts = [int(p) for p in base.split(".")]
    except ValueError:
        return None
    parts.append(int(suffix) if suffix.isdigit() else 0)
    return tuple(parts)


def pick_latest_stable(versions: list[str]) -> Optional[str]:
    """Newest stable release from an npm version list, or None."""
    best: Optional[str] = None
    best_key: Optional[tuple[int, ...]] = None
    for v in versions:
        if not is_stable(v):
            continue
        key = _sortable(v)
        if key is None:
            continue
        if best_key is None or key > best_key:
            best, best_key = v, key
    return best


def pick_latest_hermes_tag(tags: list[str]) -> Optional[str]:
    """Newest ``vYYYY.M.D`` Docker tag, ignoring floating tags.

    'latest' and 'main' move under you — pinning to them would defeat the point
    of having a pin at all.
    """
    best: Optional[str] = None
    best_key: Optional[tuple[int, ...]] = None
    for tag in tags:
        m = _HERMES_TAG_RE.match(tag)
        if not m:
            continue
        try:
            key = tuple(int(p) for p in m.group(1).split("."))
        except ValueError:
            continue
        if best_key is None or key > best_key:
            best, best_key = tag, key
    return best


# ── network fetches ───────────────────────────────────────────────────────────
def fetch_npm_versions(package: str = NPM_PACKAGE) -> list[str]:
    """All published versions of an npm package (via the npm CLI)."""
    out = subprocess.run(
        ["npm", "view", package, "versions", "--json"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    if out.returncode != 0:
        raise RuntimeError(f"npm view {package} failed: {out.stderr.strip()[:200]}")
    data = json.loads(out.stdout)
    return [data] if isinstance(data, str) else list(data)


def fetch_dockerhub_tags(repo: str = HERMES_REPO) -> list[dict[str, Any]]:
    """Tag records for a Docker Hub repository, newest first (via curl).

    curl, not urllib: 2026-10-23 on marvin every Python HTTPS read to
    hub.docker.com hung (Homebrew 3.15 and /usr/bin/python3 alike) while curl
    fetched the same URL in 0.2s, so Hermes came back UNKNOWN after ~6.5 minutes
    of retries. The deadline/retry guards below still bound it.
    """
    url = DOCKERHUB_TAGS.format(repo=repo)
    cmd = ["curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "60"]
    if _FORCE_IPV4:
        cmd.append("-4")
    out = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=90, check=False)
    if out.returncode != 0:
        raise RuntimeError(f"curl {url} failed (exit {out.returncode}): {out.stderr.strip()[:200]}")
    return json.loads(out.stdout).get("results", [])


def _digest_for_tag(tags: list[dict[str, Any]], tag: str) -> Optional[str]:
    for rec in tags:
        if rec.get("name") == tag:
            return rec.get("digest")
    return None


def _call_with_deadline(fn: Callable[[], _T], seconds: float) -> _T:
    """Run ``fn`` in a daemon thread; raise ``TimeoutError`` if it outlives ``seconds``.

    The hung thread is abandoned (daemon, so it cannot keep the process alive
    at exit). This is the only bound that holds when the socket layer itself
    stops honouring its timeout — see FETCH_DEADLINE_S.
    """
    outcome: dict[str, Any] = {}

    def _run() -> None:
        try:
            outcome["value"] = fn()
        except BaseException as exc:  # noqa: BLE001 - re-raised in the caller
            outcome["error"] = exc

    worker = threading.Thread(target=_run, name="discover-fetch", daemon=True)
    worker.start()
    worker.join(seconds)
    if worker.is_alive():
        raise TimeoutError(f"fetch exceeded hard deadline of {seconds:g}s")
    if "error" in outcome:
        raise outcome["error"]
    return outcome["value"]


@contextlib.contextmanager
def _ipv4_only() -> Iterator[None]:
    """Force AF_INET for name resolution inside the block.

    Every Docker Hub failure seen on marvin (timeout, SSL EOF, the CLOSE_WAIT
    hang) was on an IPv6 path; `curl -4` to the same URL succeeded 100% of the
    time. Used from the SECOND attempt onwards — the first attempt keeps the
    system default so a healthy dual-stack host is never second-guessed.
    """
    global _FORCE_IPV4
    original = socket.getaddrinfo

    def _getaddrinfo_v4(
        host: Any,
        port: Any,
        family: int = 0,
        type: int = 0,
        proto: int = 0,
        flags: int = 0,
    ) -> Any:
        return original(host, port, socket.AF_INET, type, proto, flags)

    socket.getaddrinfo = _getaddrinfo_v4  # type: ignore[assignment]
    _FORCE_IPV4 = True  # curl resolves names itself; tell it with -4
    try:
        yield
    finally:
        socket.getaddrinfo = original  # type: ignore[assignment]
        _FORCE_IPV4 = False


def _guarded_fetch(fetch: Callable[[], _T], attempt: int, deadline: float) -> _T:
    """One attempt of ``fetch``: hard-bounded, IPv4-only after the first failure."""
    ctx = _ipv4_only() if attempt >= 1 else contextlib.nullcontext()
    with ctx:
        return _call_with_deadline(fetch, deadline)


def _retry(
    fn: Callable[[int], _T],
    *,
    attempts: int = RETRY_ATTEMPTS,
    delays: tuple[float, ...] = RETRY_DELAYS,
    sleep: Callable[[float], Any] = time.sleep,
) -> _T:
    """Call ``fn(attempt)`` up to ``attempts`` times; re-raise the last error if all fail.

    ``attempt`` is 0-based so a callee can change strategy on retries.
    ``delays[i]`` is slept after the i-th failure (the last delay repeats if
    there are more gaps than delays). ``sleep`` is injectable so tests never
    actually wait.
    """
    if attempts < 1:
        raise ValueError("attempts must be >= 1")
    last_exc: Optional[BaseException] = None
    for i in range(attempts):
        try:
            return fn(i)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last_exc = exc
            if i < attempts - 1:
                delay = delays[min(i, len(delays) - 1)] if delays else 0
                print(
                    f"[discover] attempt {i + 1}/{attempts} failed ({str(exc)[:80]}) "
                    f"— retrying in {delay}s",
                    file=sys.stderr,
                )
                sleep(delay)
    assert last_exc is not None  # attempts >= 1 guarantees a raise or a return
    raise last_exc


# ── discovery ─────────────────────────────────────────────────────────────────
def discover(
    fetch_npm: Callable[[], list[str]] = fetch_npm_versions,
    fetch_hub: Callable[[], list[dict[str, Any]]] = fetch_dockerhub_tags,
    sleep: Callable[[float], Any] = time.sleep,
    deadline: float = FETCH_DEADLINE_S,
) -> dict[str, Any]:
    """Resolve the latest stable release of each wrapped tool.

    Each entry is independent: one source being unreachable must not mask the
    other. A failed lookup reports ``error`` and a null version — "unknown",
    never "already current", which would silently re-introduce the exact no-op
    this module exists to prevent.
    """
    result: dict[str, Any] = {}

    try:
        result["openclaw"] = {
            "latest": pick_latest_stable(
                _retry(lambda i: _guarded_fetch(fetch_npm, i, deadline), sleep=sleep)
            ),
            "source": f"npm:{NPM_PACKAGE}",
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001 - reported, not swallowed
        result["openclaw"] = {
            "latest": None,
            "source": f"npm:{NPM_PACKAGE}",
            "error": str(exc),
        }

    try:
        tags = _retry(lambda i: _guarded_fetch(fetch_hub, i, deadline), sleep=sleep)
        latest = pick_latest_hermes_tag([t.get("name", "") for t in tags])
        result["hermes"] = {
            "latest": latest,
            "digest": _digest_for_tag(tags, latest) if latest else None,
            "source": f"dockerhub:{HERMES_REPO}",
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001
        result["hermes"] = {
            "latest": None,
            "digest": None,
            "source": f"dockerhub:{HERMES_REPO}",
            "error": str(exc),
        }

    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--shell", action="store_true", help="KEY=VALUE lines for bash eval")
    args = ap.parse_args()

    found = discover()

    if args.shell:
        oc = found["openclaw"]["latest"] or ""
        hm = found["hermes"]["latest"] or ""
        hd = found["hermes"].get("digest") or ""
        print(f"DISCOVERED_OPENCLAW_VERSION={oc}")
        print(f"DISCOVERED_HERMES_TAG={hm}")
        print(f"DISCOVERED_HERMES_DIGEST={hd}")
    elif args.json:
        print(json.dumps(found, indent=2))
    else:
        print("AgentShroud™ — upstream release discovery")
        for name, info in found.items():
            if info["error"]:
                print(f"  {name:<9} UNKNOWN — {info['source']} failed: {info['error'][:80]}")
            else:
                print(f"  {name:<9} latest={info['latest']}  ({info['source']})")

    if all(info["latest"] is None for info in found.values()):
        print("ERROR: no upstream source could be reached", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
