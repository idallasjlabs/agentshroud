# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SkillGuard preflight CLI — ``python -m gateway.skills.scan <source>`` (SCRUM-97).

The gated HTTP endpoint (``POST /api/skills/reload``) is not the only path that
syncs ``~/.llm_settings/`` into the running bots: ``scripts/sync-llm-settings.sh``
performs the *same* copy from the command line.  Without a gate that bash path
reaches the bots fully unscanned.  This module is the SkillGuard entry point that
the bash sync shells out to *before* it copies anything.

Behaviour (matches the endpoint's fail-CLOSED contract):

- Walks ``<source>`` with :class:`~gateway.skills.manifest.SkillsManifest`.
- Reads every manifest entry.  A file that raises ``OSError`` on read is
  **unscannable** — that BLOCKS (unreadable artefacts must not deploy), it is
  never silently skipped.
- Runs :meth:`SkillGuard.scan_skill_tree` over the whole tree.
- Prints a human-readable summary.

Exit codes:

- ``0``  — tree is clean or only FLAG-level findings (deploy may proceed).
- ``2``  — SkillGuard BLOCKED (dangerous or unscannable artefact); do NOT deploy.
- ``3``  — usage / source error (missing or empty source directory).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from gateway.security.skill_guard import Recommendation, ScanResult, SkillGuard

_EXIT_OK = 0
_EXIT_BLOCKED = 2
_EXIT_USAGE = 3


def _build_tree(source: Path) -> dict[str, str]:
    """Read every manifest entry under *source*, failing CLOSED on unreadable files.

    Raises:
        FileNotFoundError / ValueError: propagated from ``SkillsManifest.from_source``.
        SkillScanError: (via caller) never — unreadable files raise OSError here.
        OSError: re-raised so the caller can treat it as an unscannable BLOCK.
    """
    from gateway.skills.manifest import SkillsManifest

    manifest = SkillsManifest.from_source(source)
    tree: dict[str, str] = {}
    for entry in manifest.entries:
        tree[entry.name] = (source / entry.name).read_text(errors="replace")
    return tree


def _print_findings(result: ScanResult) -> None:
    for finding in sorted(result.findings, key=lambda f: (-int(f.severity), f.location)):
        print(
            f"  [{finding.severity.name:8}] {finding.category:20} {finding.location}\n"
            f"             {finding.description}",
            file=sys.stderr,
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m gateway.skills.scan",
        description="SkillGuard preflight: scan a ~/.llm_settings tree before deploy.",
    )
    parser.add_argument(
        "source",
        help="source directory to scan (e.g. ~/.llm_settings)",
    )
    args = parser.parse_args(argv)

    source = Path(args.source).expanduser()

    try:
        tree = _build_tree(source)
    except FileNotFoundError as exc:
        print(f"SkillGuard preflight ERROR: {exc}", file=sys.stderr)
        return _EXIT_USAGE
    except ValueError as exc:
        print(f"SkillGuard preflight ERROR: {exc}", file=sys.stderr)
        return _EXIT_USAGE
    except OSError as exc:
        # Fail CLOSED: an unreadable artefact is unscannable and must not deploy.
        print(
            "SkillGuard preflight BLOCKED: unscannable artefact could not be read "
            f"({exc}). Deploy aborted.",
            file=sys.stderr,
        )
        return _EXIT_BLOCKED

    guard = SkillGuard()
    result = guard.scan_skill_tree(tree)

    if result.recommendation is Recommendation.BLOCK:
        offenders = sorted({f.location for f in result.findings if int(f.severity) >= 4})
        print(
            "SkillGuard preflight BLOCKED skill deployment: dangerous supply-chain "
            f"patterns detected (severity={result.severity.name}).",
            file=sys.stderr,
        )
        _print_findings(result)
        print(f"Blocking findings at: {offenders}", file=sys.stderr)
        return _EXIT_BLOCKED

    if result.findings:
        print(
            f"SkillGuard preflight: {len(result.findings)} finding(s) "
            f"(severity={result.severity.name}) — review recommended, deploy allowed.",
            file=sys.stderr,
        )
        _print_findings(result)
    else:
        print("SkillGuard preflight: clean — no supply-chain findings.", file=sys.stderr)
    return _EXIT_OK


if __name__ == "__main__":  # pragma: no cover - exercised via subprocess in tests
    sys.exit(main())
