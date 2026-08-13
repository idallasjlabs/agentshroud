#!/usr/bin/env python3
"""
Export dated competitive-report .md files (the source content actually emailed
by Hermes/OpenClaw's cron jobs) from a bot's workspace into a local directory,
optionally filtered to reports on/after a given date.

No sent-mail ledger exists in this repo — cron jobs render these .md files to
HTML and send them fresh each run, without archiving the outbound email. This
script instead collects the .md report *source* files that are the report
content, which is what "export the email reports" means in the absence of a
real send-time log.

Usage:
  python scripts/export-email-reports.py
  python scripts/export-email-reports.py --since 2026-06-01
  python scripts/export-email-reports.py --since 2026-06-01 --bot hermes
  python scripts/export-email-reports.py --out-dir /tmp/reports_export
"""

import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

_BOTS = {
    "hermes": {
        "container": "agentshroud-hermes-v2",
        "reports_dir": "/opt/data/workspace/reports",
    },
    "openclaw": {
        "container": "agentshroud-openclaw",
        "reports_dir": "/home/node/.openclaw/workspace/reports",
    },
}


def _parse_since(value: str) -> datetime:
    """Parse --since into a UTC-aware datetime. Accepts 'YYYY-MM-DD' or
    'YYYY-MM-DD HH:MM[:SS]' (space or 'T' separator); naive input is treated as UTC."""
    text = value.strip()
    for candidate in (text, text.replace(" ", "T")):
        try:
            dt = datetime.fromisoformat(candidate)
        except ValueError:
            continue
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    print(
        f"ERROR: could not parse --since value {value!r} (expected YYYY-MM-DD or YYYY-MM-DD HH:MM)",
        file=sys.stderr,
    )
    sys.exit(1)


def _list_report_files(container: str, reports_dir: str) -> list[str]:
    result = subprocess.run(
        [
            "docker",
            "exec",
            container,
            "find",
            reports_dir,
            "-maxdepth",
            "1",
            "-name",
            "*.md",
            "-type",
            "f",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        print(
            f"  WARN: could not list {reports_dir} in {container}: {result.stderr.strip()}",
            file=sys.stderr,
        )
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def _report_date(path: str) -> datetime | None:
    match = _DATE_RE.search(Path(path).name)
    if not match:
        return None
    try:
        return datetime.fromisoformat(match.group(1)).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def export_bot(bot: str, out_dir: Path, since: datetime | None) -> int:
    cfg = _BOTS[bot]
    container, reports_dir = cfg["container"], cfg["reports_dir"]
    print(f"[{bot}] listing {reports_dir} in {container}...", file=sys.stderr)

    remote_paths = _list_report_files(container, reports_dir)
    dated = [(p, _report_date(p)) for p in remote_paths]
    undated = [p for p, d in dated if d is None]
    if undated:
        print(
            f"  skipping {len(undated)} file(s) with no YYYY-MM-DD in the filename", file=sys.stderr
        )

    matched = sorted((p, d) for p, d in dated if d is not None and (since is None or d >= since))
    skipped_before_since = sum(
        1 for _, d in dated if d is not None and since is not None and d < since
    )

    bot_out = out_dir / bot
    bot_out.mkdir(parents=True, exist_ok=True)
    count = 0
    for remote_path, _ in matched:
        dest = bot_out / Path(remote_path).name
        cp = subprocess.run(
            ["docker", "cp", f"{container}:{remote_path}", str(dest)],
            capture_output=True,
            text=True,
            check=False,
        )
        if cp.returncode != 0:
            print(f"  WARN: failed to copy {remote_path}: {cp.stderr.strip()}", file=sys.stderr)
            continue
        count += 1

    if skipped_before_since:
        print(f"  (filtered {skipped_before_since} report(s) before --since)", file=sys.stderr)
    print(f"[{bot}] {count} report(s) written to {bot_out}", file=sys.stderr)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export dated .md report files (email report source content) to a local directory"
    )
    parser.add_argument(
        "--bot",
        choices=["hermes", "openclaw", "all"],
        default="all",
        help="Which bot's reports to export (default: all)",
    )
    parser.add_argument(
        "--out-dir",
        default="email_reports_export",
        help="Local output directory (default: email_reports_export)",
    )
    parser.add_argument(
        "--since",
        default=None,
        help="Only export reports dated on/after this date "
        "(YYYY-MM-DD or 'YYYY-MM-DD HH:MM'; naive values are treated as UTC). "
        "Default: export all reports.",
    )
    args = parser.parse_args()

    since = _parse_since(args.since) if args.since else None
    out_dir = Path(args.out_dir)
    bots = list(_BOTS) if args.bot == "all" else [args.bot]

    total = 0
    for bot in bots:
        total += export_bot(bot, out_dir, since)
    print(f"Done. {total} report(s) total written under {out_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
