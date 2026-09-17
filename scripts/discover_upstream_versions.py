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
import json
import re
import subprocess
import sys
import urllib.request
from typing import Any, Optional

NPM_PACKAGE = "openclaw"
HERMES_REPO = "nousresearch/hermes-agent"
DOCKERHUB_TAGS = (
    "https://hub.docker.com/v2/repositories/{repo}/tags"
    "?page_size=100&ordering=last_updated"
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
    """Tag records for a Docker Hub repository, newest first."""
    url = DOCKERHUB_TAGS.format(repo=repo)
    with urllib.request.urlopen(url, timeout=60) as resp:  # noqa: S310
        return json.load(resp).get("results", [])


def _digest_for_tag(tags: list[dict[str, Any]], tag: str) -> Optional[str]:
    for rec in tags:
        if rec.get("name") == tag:
            return rec.get("digest")
    return None


# ── discovery ─────────────────────────────────────────────────────────────────
def discover() -> dict[str, Any]:
    """Resolve the latest stable release of each wrapped tool.

    Each entry is independent: one source being unreachable must not mask the
    other. A failed lookup reports ``error`` and a null version — "unknown",
    never "already current", which would silently re-introduce the exact no-op
    this module exists to prevent.
    """
    result: dict[str, Any] = {}

    try:
        result["openclaw"] = {
            "latest": pick_latest_stable(fetch_npm_versions()),
            "source": f"npm:{NPM_PACKAGE}",
            "error": None,
        }
    except Exception as exc:  # noqa: BLE001 - reported, not swallowed
        result["openclaw"] = {"latest": None, "source": f"npm:{NPM_PACKAGE}", "error": str(exc)}

    try:
        tags = fetch_dockerhub_tags()
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
