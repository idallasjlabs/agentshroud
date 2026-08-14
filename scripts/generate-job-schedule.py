#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Generate docs/job-schedule.html from Hermes + OpenClaw's live cron state.

Reads each bot's actual running config via `docker exec` (not the repo's
baked-in seed files, which drift from what's really scheduled once jobs are
added/edited live) and renders a single self-contained HTML page listing
every job: bot, name, schedule, timezone, enabled/disabled, last run status.

Usage:
    python3 scripts/generate-job-schedule.py [--out docs/job-schedule.html]

Must run on a host with `docker exec` access to agentshroud-hermes-v2 and
agentshroud-openclaw (or agentshroud-marvin-hermes-v2 / agentshroud-marvin-openclaw
on a marvin-profile dev deploy — pass --hermes-container / --openclaw-container
to override).
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from datetime import datetime, timezone


def docker_exec(container: str, *cmd: str) -> str:
    result = subprocess.run(
        ["docker", "exec", container, *cmd],
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.stdout


def load_hermes_jobs(container: str) -> list[dict]:
    raw = docker_exec(container, "cat", "/opt/data/cron/jobs.json")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []
    jobs = []
    for j in data.get("jobs", []):
        sched = j.get("schedule") or {}
        jobs.append(
            {
                "bot": "Hermes",
                "name": j.get("name", "?"),
                "enabled": bool(j.get("enabled", True)),
                "expr": sched.get("expr") or sched.get("display") or "?",
                "tz": j.get("timezone") or "server-local",
                "last_status": j.get("last_status") or "never run",
                "last_run_at": j.get("last_run_at"),
                "next_run_at": j.get("next_run_at"),
                "id": j.get("id", ""),
            }
        )
    return jobs


def load_openclaw_jobs(container: str) -> list[dict]:
    raw = docker_exec(container, "openclaw", "cron", "list", "--all", "--json")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return []
    jobs = []
    for j in data.get("jobs", []):
        sched = j.get("schedule") or {}
        state = j.get("state") or {}
        jobs.append(
            {
                "bot": "OpenClaw",
                "name": j.get("name", "?"),
                "enabled": bool(j.get("enabled", True)),
                "expr": sched.get("expr", "?"),
                "tz": sched.get("tz") or "server-local",
                "last_status": state.get("lastStatus") or "never run",
                "last_run_at": state.get("lastRunAtMs"),
                "next_run_at": state.get("nextRunAtMs"),
                "id": j.get("id", ""),
            }
        )
    return jobs


def describe_cron(expr: str) -> str:
    """Best-effort plain-language gloss of a 5-field cron expression."""
    parts = expr.split()
    if len(parts) != 5:
        return expr
    minute, hour, dom, month, dow = parts
    if dom == "*" and month == "*" and dow == "*":
        if minute.isdigit() and hour.isdigit():
            return f"daily at {int(hour):02d}:{int(minute):02d}"
        return f"daily ({expr})"
    if dom == "*" and month == "*" and re.fullmatch(r"\d+", dow or ""):
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        d = int(dow) % 7
        if minute.isdigit() and hour.isdigit():
            return f"weekly on {days[d]} at {int(hour):02d}:{int(minute):02d}"
    if dom.isdigit() and month == "*" and dow == "*":
        if minute.isdigit() and hour.isdigit():
            return f"monthly on day {dom} at {int(hour):02d}:{int(minute):02d}"
    if "," in hour and dom == "*" and month == "*" and dow == "*":
        return f"daily at {hour.replace(',', ', ')}:{minute.zfill(2)}"
    return expr


def fmt_ts(val) -> str:
    if not val:
        return "—"
    try:
        if isinstance(val, (int, float)) or (isinstance(val, str) and val.isdigit()):
            dt = datetime.fromtimestamp(int(val) / 1000, tz=timezone.utc)
        else:
            dt = datetime.fromisoformat(str(val).replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d %H:%M UTC")
    except Exception:
        return str(val)


STATUS_CLASS = {
    "ok": "status-ok",
    "running": "status-running",
    "failed": "status-failed",
    "blocked_config": "status-failed",
    "pending": "status-pending",
    "never run": "status-pending",
}


def render_html(jobs: list[dict], generated_at: str) -> str:
    rows = []
    for j in sorted(jobs, key=lambda x: (x["bot"], x["name"])):
        status = str(j["last_status"])
        status_class = STATUS_CLASS.get(status, "status-pending")
        enabled_badge = (
            '<span class="badge badge-on">enabled</span>'
            if j["enabled"]
            else '<span class="badge badge-off">disabled</span>'
        )
        bot_class = "bot-hermes" if j["bot"] == "Hermes" else "bot-openclaw"
        rows.append(
            f"""
      <tr class="{'row-disabled' if not j['enabled'] else ''}">
        <td><span class="bot-pill {bot_class}">{html.escape(j['bot'])}</span></td>
        <td class="job-name">{html.escape(j['name'])}</td>
        <td>{enabled_badge}</td>
        <td><code>{html.escape(j['expr'])}</code><div class="gloss">{html.escape(describe_cron(j['expr']))} ({html.escape(j['tz'])})</div></td>
        <td><span class="status {status_class}">{html.escape(status)}</span></td>
        <td>{fmt_ts(j['last_run_at'])}</td>
        <td>{fmt_ts(j['next_run_at'])}</td>
      </tr>"""
        )

    n_total = len(jobs)
    n_enabled = sum(1 for j in jobs if j["enabled"])
    n_hermes = sum(1 for j in jobs if j["bot"] == "Hermes")
    n_openclaw = sum(1 for j in jobs if j["bot"] == "OpenClaw")

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AgentShroud — Job Schedule</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{
    --bg: #0b0d12; --card: #12151c; --border: #232733; --text: #e6e8ee;
    --muted: #8b93a7; --accent: #1583f0;
  }}
  @media (prefers-color-scheme: light) {{
    :root {{ --bg: #f7f8fa; --card: #ffffff; --border: #e2e5eb; --text: #14161c; --muted: #5b6373; --accent: #1583f0; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 32px 20px 60px; background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }}
  .wrap {{ max-width: 1080px; margin: 0 auto; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 4px; }}
  .subtitle {{ color: var(--muted); font-size: 0.9rem; margin: 0 0 24px; }}
  .stats {{ display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }}
  .stat {{
    background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 12px 18px; min-width: 120px;
  }}
  .stat .num {{ font-size: 1.4rem; font-weight: 600; }}
  .stat .label {{ font-size: 0.78rem; color: var(--muted); }}
  table {{ width: 100%; border-collapse: collapse; background: var(--card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }}
  thead th {{
    text-align: left; padding: 10px 14px; font-size: 0.75rem; text-transform: uppercase;
    letter-spacing: 0.04em; color: var(--muted); border-bottom: 1px solid var(--border);
  }}
  tbody td {{ padding: 12px 14px; border-bottom: 1px solid var(--border); font-size: 0.88rem; vertical-align: top; }}
  tbody tr:last-child td {{ border-bottom: none; }}
  tbody tr.row-disabled {{ opacity: 0.5; }}
  .job-name {{ font-weight: 500; }}
  code {{ background: rgba(127,127,127,0.15); padding: 2px 6px; border-radius: 5px; font-size: 0.82rem; }}
  .gloss {{ color: var(--muted); font-size: 0.76rem; margin-top: 3px; }}
  .bot-pill {{ display: inline-block; padding: 3px 10px; border-radius: 999px; font-size: 0.75rem; font-weight: 600; }}
  .bot-hermes {{ background: rgba(21,131,240,0.15); color: #1583f0; }}
  .bot-openclaw {{ background: rgba(168,85,247,0.15); color: #a855f7; }}
  .badge {{ display: inline-block; padding: 2px 9px; border-radius: 999px; font-size: 0.72rem; font-weight: 600; }}
  .badge-on {{ background: rgba(34,197,94,0.15); color: #22c55e; }}
  .badge-off {{ background: rgba(148,163,184,0.2); color: #94a3b8; }}
  .status {{ font-weight: 600; font-size: 0.82rem; }}
  .status-ok {{ color: #22c55e; }}
  .status-running {{ color: #eab308; }}
  .status-failed {{ color: #ef4444; }}
  .status-pending {{ color: var(--muted); }}
  footer {{ margin-top: 24px; color: var(--muted); font-size: 0.78rem; }}
  @media (max-width: 640px) {{
    table, thead, tbody, tr {{ display: block; }}
    thead {{ display: none; }}
    tr {{ border-bottom: 1px solid var(--border); padding: 10px 0; }}
    td {{ border: none !important; padding: 4px 14px !important; }}
    td:before {{ content: attr(data-label); display: block; font-size: 0.7rem; color: var(--muted); text-transform: uppercase; }}
  }}
</style>
</head>
<body>
<div class="wrap">
  <h1>AgentShroud — Job Schedule</h1>
  <p class="subtitle">Live cron state pulled directly from Hermes and OpenClaw. Regenerate anytime with <code>scripts/generate-job-schedule.py</code>.</p>

  <div class="stats">
    <div class="stat"><div class="num">{n_total}</div><div class="label">total jobs</div></div>
    <div class="stat"><div class="num">{n_enabled}</div><div class="label">enabled</div></div>
    <div class="stat"><div class="num">{n_hermes}</div><div class="label">Hermes</div></div>
    <div class="stat"><div class="num">{n_openclaw}</div><div class="label">OpenClaw</div></div>
  </div>

  <table>
    <thead>
      <tr>
        <th>Bot</th><th>Job</th><th>State</th><th>Schedule</th>
        <th>Last status</th><th>Last run</th><th>Next run</th>
      </tr>
    </thead>
    <tbody>{''.join(rows)}
    </tbody>
  </table>

  <footer>Generated {html.escape(generated_at)} · {n_total} jobs across 2 bots</footer>
</div>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="docs/job-schedule.html")
    parser.add_argument("--hermes-container", default="agentshroud-hermes-v2")
    parser.add_argument("--openclaw-container", default="agentshroud-openclaw")
    args = parser.parse_args()

    jobs = []
    try:
        jobs += load_hermes_jobs(args.hermes_container)
    except Exception as exc:  # noqa: BLE001 - best-effort, report and continue
        print(f"warning: could not read Hermes jobs from {args.hermes_container}: {exc}", file=sys.stderr)
    try:
        jobs += load_openclaw_jobs(args.openclaw_container)
    except Exception as exc:  # noqa: BLE001
        print(f"warning: could not read OpenClaw jobs from {args.openclaw_container}: {exc}", file=sys.stderr)

    if not jobs:
        print("error: no jobs read from either bot — is docker exec reachable?", file=sys.stderr)
        return 1

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    out_html = render_html(jobs, generated_at)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(out_html)
    print(f"Wrote {args.out} ({len(jobs)} jobs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
