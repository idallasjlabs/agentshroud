#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Automated CVE remediation — actually patch the advisories, don't just file them.

Why this exists (owner decision 2026-09-15): registering an upstream advisory as
``under_review`` is bookkeeping, not remediation. AgentShroud's job is to close
the exposure. For an advisory with a published upstream fix, the honest
remediation is to *stop running the vulnerable code* — bump the pin, rebuild,
and verify — not to reason about whether a proxy control happens to cover it.

Division of labour (mirrors sunday-upgrade-apply.sh, deliberately):

  THIS SCRIPT — mechanical + verifiable: read the registry, work out the
                minimum version bump that clears the most advisories, write the
                pin, hand off to the gated upgrade, and revert the pin if that
                upgrade does not survive its gates. No LLM required. Exit code
                is the contract.

  THE SESSION — judgement only: any *code* changes the new upstream version
                requires (API breakage, config migration, patch re-anchoring).
                The Sunday session owns that arm; see prompts/sunday-upgrade.md.

THE INVARIANT THIS MODULE EXISTS TO PROTECT
-------------------------------------------
An advisory may be reported as remediated only when the vulnerable code is
genuinely gone from the running image. So the version pin and the registry must
never be allowed to disagree. If the upgrade fails and rolls back, the pin is
reverted too — otherwise the next triage run reads a pin that is not running and
promotes advisories on false evidence. That is the precise shape of the
"phantom tag" class of bug that already bit the scan gate twice; it is not
hypothetical.

Status promotion is NOT done here. After a verified deploy this script invokes
scripts/triage-cve-mitigations.py, which re-derives each verdict against the
now-actually-running version. Nothing in this file writes a ``*_mitigated``
status directly.

Usage:
    python3 scripts/auto_remediate_cves.py --plan            # report only
    python3 scripts/auto_remediate_cves.py --apply           # bump + gated deploy
    python3 scripts/auto_remediate_cves.py --apply --env prod
    python3 scripts/auto_remediate_cves.py --plan --json     # machine-readable

Exit codes (the contract — the Sunday job depends on these):
    0   success (or --plan with nothing to do)
    1   usage / unreadable registry
    20  planned a bump, but the gated upgrade failed — pin reverted
    30  upgrade succeeded but post-deploy triage failed
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSIONS_ENV = REPO_ROOT / "docker" / "versions.env"
APPLY_SH = REPO_ROOT / "scripts" / "sunday-upgrade-apply.sh"
TRIAGE_PY = REPO_ROOT / "scripts" / "triage-cve-mitigations.py"
PIN_KEY = "OPENCLAW_VERSION"


# ── version handling ──────────────────────────────────────────────────────────
def parse_version(value: Optional[str]) -> Optional[tuple[int, ...]]:
    """Parse a dotted numeric version to a comparable tuple.

    A trailing ``-N`` on any component is AgentShroud's own downstream rebuild
    counter (e.g. ``2026.7.1-2``), not part of OpenClaw's upstream semver, so it
    is stripped before comparing against an advisory's ``fixed_in``.

    Returns None for empty or non-numeric input — honest "unknown", which the
    planner treats as not-remediable rather than guessing.
    """
    if not value:
        return None
    try:
        return tuple(int(p.split("-", 1)[0]) for p in value.strip().split("."))
    except ValueError:
        return None


def read_pin(path: Path, key: str) -> Optional[str]:
    """Read one ``KEY=value`` pin from a versions.env-style file."""
    try:
        text = path.read_text()
    except OSError:
        return None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k.strip() == key:
            return v.strip() or None
    return None


def write_pin(path: Path, key: str, value: str) -> None:
    """Rewrite one pin in place, preserving every other line byte for byte.

    Raises KeyError if the pin is absent: appending a brand new key would create
    a pin that nothing in the compose/build chain actually consumes, which would
    look like a successful bump while changing nothing.
    """
    text = path.read_text()
    out, found = [], False
    for line in text.splitlines(keepends=True):
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            k, _, _ = stripped.partition("=")
            if k.strip() == key:
                eol = "\n" if line.endswith("\n") else ""
                out.append(f"{key}={value}{eol}")
                found = True
                continue
        out.append(line)
    if not found:
        raise KeyError(f"{key} not present in {path} — refusing to append a new pin")
    path.write_text("".join(out))


# ── planning ──────────────────────────────────────────────────────────────────
@dataclass
class RemediationPlan:
    """What a version bump would and would not remediate.

    Every ``under_review`` advisory lands in exactly one bucket, so the counts
    always reconcile and a report can never quietly lose one:

      already_fixed — fixed_in <= the current pin. The vulnerable code is not
                      present; these are mis-filed and need retriage, NOT an
                      upgrade. Counting them as "cleared by the bump" would
                      overstate what the bump achieved.
      cleared       — fixed_in is above the pin and at or below the target.
                      These are the advisories the bump genuinely remediates.
      remaining     — no fixed_in, an unparseable one, or a fix beyond the
                      target cap. Honestly still outstanding afterwards.
    """

    current_version: str
    target_version: Optional[str] = None
    cleared: list[dict[str, Any]] = field(default_factory=list)
    remaining: list[dict[str, Any]] = field(default_factory=list)
    already_fixed: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialise for the unattended run's audit trail."""
        return {
            "current_version": self.current_version,
            "target_version": self.target_version,
            "cleared_count": len(self.cleared),
            "cleared_ids": [e.get("ghsa_id") or e.get("id") for e in self.cleared],
            "remaining_count": len(self.remaining),
            "remaining_ids": [e.get("ghsa_id") or e.get("id") for e in self.remaining],
            "already_fixed_count": len(self.already_fixed),
            "already_fixed_ids": [
                e.get("ghsa_id") or e.get("id") for e in self.already_fixed
            ],
        }


def plan_remediation(
    registry: list[dict[str, Any]],
    current_version: str,
    max_target: Optional[str] = None,
) -> RemediationPlan:
    """Work out the minimum version bump that remediates the most advisories.

    Only ``under_review`` entries are considered. An entry that has already been
    triaged carries somebody's assessed verdict; a mechanical planner must not
    silently re-open or re-claim it.

    Args:
        registry: Registry entries (agent_cve_registry.py shape).
        current_version: The pin as written, e.g. "2026.7.1-2".
        max_target: Optional cap on how far forward an unattended run may jump.

    Returns:
        A RemediationPlan whose three buckets partition the under_review set.
    """
    plan = RemediationPlan(current_version=current_version)
    pinned = parse_version(current_version)
    cap = parse_version(max_target) if max_target else None

    candidates: list[tuple[tuple[int, ...], dict[str, Any]]] = []
    for entry in registry:
        if entry.get("status") != "under_review":
            continue
        fixed = parse_version(entry.get("fixed_in"))
        if fixed is None:
            plan.remaining.append(entry)
            continue
        if pinned is not None and fixed <= pinned:
            plan.already_fixed.append(entry)
            continue
        if cap is not None and fixed > cap:
            plan.remaining.append(entry)
            continue
        candidates.append((fixed, entry))

    if not candidates:
        return plan

    # The minimum version clearing every candidate is simply the highest
    # fixed_in among them — anything lower leaves one behind.
    target = max(v for v, _ in candidates)
    plan.target_version = ".".join(str(p) for p in target)
    plan.cleared = [e for _, e in candidates]
    return plan


# ── orchestration ─────────────────────────────────────────────────────────────
def load_registry() -> list[dict[str, Any]]:
    """Import the committed OpenClaw registry."""
    sys.path.insert(0, str(REPO_ROOT))
    from gateway.security.agent_cve_registry import (  # noqa: PLC0415
        _OPENCLAW_CVE_REGISTRY,
    )

    return _OPENCLAW_CVE_REGISTRY


def _run(cmd: list[str], **kw) -> int:
    print(f"[remediate] $ {' '.join(cmd)}", flush=True)
    return subprocess.call(cmd, cwd=str(REPO_ROOT), **kw)


def apply_remediation(plan: RemediationPlan, environment: str, soak: int) -> int:
    """Bump the pin, run the gated upgrade, revert the pin if it does not hold.

    Returns a process exit code (see module docstring).
    """
    if not plan.target_version:
        print("[remediate] nothing to remediate by version bump.")
        return 0

    original = read_pin(VERSIONS_ENV, PIN_KEY)
    if original is None:
        print(f"[remediate] ERROR: {PIN_KEY} not found in {VERSIONS_ENV}", file=sys.stderr)
        return 1

    print(
        f"[remediate] bumping {PIN_KEY}: {original} -> {plan.target_version} "
        f"({len(plan.cleared)} advisor{'y' if len(plan.cleared) == 1 else 'ies'} remediated)"
    )
    write_pin(VERSIONS_ENV, PIN_KEY, plan.target_version)

    rc = _run(
        [
            "bash",
            str(APPLY_SH),
            "--env",
            environment,
            "--phase",
            "all",
            "--soak-seconds",
            str(soak),
        ]
    )
    if rc != 0:
        # The upgrade did not survive its gates. sunday-upgrade-apply.sh has
        # already rolled the IMAGES back; roll the PIN back too, or the repo
        # would claim a version it is not running and the next triage pass
        # would promote advisories on evidence that is not true.
        print(
            f"[remediate] gated upgrade FAILED (rc={rc}) — reverting {PIN_KEY} to {original}",
            file=sys.stderr,
        )
        write_pin(VERSIONS_ENV, PIN_KEY, original)
        return 20

    print("[remediate] upgrade verified. Re-triaging against the now-running version.")
    rc = _run([sys.executable, str(TRIAGE_PY), "--apply"])
    if rc != 0:
        print(f"[remediate] post-deploy triage failed (rc={rc})", file=sys.stderr)
        return 30
    return 0


def _print_plan(plan: RemediationPlan) -> None:
    print(f"  current pin      : {plan.current_version}")
    print(f"  target version   : {plan.target_version or '(no bump needed)'}")
    print(f"  remediated by it : {len(plan.cleared)}")
    print(f"  already fixed    : {len(plan.already_fixed)}  (mis-filed; need retriage)")
    print(f"  still outstanding: {len(plan.remaining)}  (no upstream fix / beyond cap)")
    if plan.cleared:
        by_sev: dict[str, int] = {}
        for e in plan.cleared:
            by_sev[e.get("severity", "?")] = by_sev.get(e.get("severity", "?"), 0) + 1
        print(f"  cleared by severity: {by_sev}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--plan", action="store_true", help="Report only; change nothing.")
    mode.add_argument("--apply", action="store_true", help="Bump, deploy through the gates, retriage.")
    ap.add_argument("--env", default="dev", choices=("dev", "prod"))
    ap.add_argument("--max-target", default=None, help="Cap how far forward to jump.")
    ap.add_argument("--soak-seconds", type=int, default=120)
    ap.add_argument("--json", action="store_true", help="Machine-readable plan on stdout.")
    args = ap.parse_args()

    current = read_pin(VERSIONS_ENV, PIN_KEY)
    if current is None:
        print(f"ERROR: {PIN_KEY} not found in {VERSIONS_ENV}", file=sys.stderr)
        return 1

    plan = plan_remediation(load_registry(), current, max_target=args.max_target)

    if args.json:
        print(json.dumps(plan.to_dict(), indent=2))
    else:
        print("AgentShroud™ — automated CVE remediation plan")
        _print_plan(plan)

    if args.plan:
        return 0
    return apply_remediation(plan, args.env, args.soak_seconds)


if __name__ == "__main__":
    sys.exit(main())
