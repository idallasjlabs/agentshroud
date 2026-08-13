#!/usr/bin/env python3
"""
Export Hermes/OpenClaw's own persisted Telegram conversation history to JSONL.

Telegram's Bot API has no "get chat history" method (only a short rolling
getUpdates buffer), and a full MTProto/Telethon export requires a personal
user-account login. This script sidesteps both: Hermes and OpenClaw already
persist every conversation turn locally for their own memory/context, so this
reads directly from those stores — richer than a raw Telegram export (full
message content, not just what a client would show) and requires no
additional credentials.

Sources:
  Hermes    /opt/data/state.db (sqlite) — sessions/messages tables,
            filtered to sessions.source = 'telegram'.
  OpenClaw  /home/node/.openclaw/agents/main/sessions/*.jsonl — per-session
            transcripts, filtered to sessions whose companion .trajectory.jsonl
            tags messageChannel:"telegram".

Usage:
  python scripts/export-bot-conversations.py
  python scripts/export-bot-conversations.py --since 2026-06-01
  python scripts/export-bot-conversations.py --since 2026-06-01 --bot hermes
  python scripts/export-bot-conversations.py --out-dir /tmp/conversations_export
"""

import argparse
import json
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
from datetime import datetime, timezone
from pathlib import Path

_HERMES_CONTAINER = "agentshroud-hermes-v2"
_HERMES_DB_PATH = "/opt/data/state.db"
_OPENCLAW_CONTAINER = "agentshroud-openclaw"
_OPENCLAW_SESSIONS_DIR = "/home/node/.openclaw/agents/main/sessions"


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


def _docker_read_file(container: str, remote_path: str, local_path: Path) -> bool:
    """Read a file out of a container via `exec cat` rather than `docker cp` —
    on this host `docker cp` unreliably reports "file not found" for files that
    demonstrably exist (confirmed via `exec ls`) and were just written by a
    prior `exec` call in the same container; `exec cat` reads the same live
    view and does not have this problem."""
    with local_path.open("wb") as fh:
        result = subprocess.run(
            ["docker", "exec", container, "cat", remote_path],
            stdout=fh,
            stderr=subprocess.PIPE,
            check=False,
        )
    if result.returncode != 0:
        print(
            f"  WARN: could not read {remote_path} from {container}: {result.stderr.decode(errors='replace').strip()}",
            file=sys.stderr,
        )
        return False
    return True


def export_hermes(out_dir: Path, since: datetime | None) -> int:
    print(f"[hermes] copying {_HERMES_DB_PATH} from {_HERMES_CONTAINER}...", file=sys.stderr)
    with tempfile.TemporaryDirectory() as tmp:
        local_db = Path(tmp) / "state.db"
        if not _docker_read_file(_HERMES_CONTAINER, _HERMES_DB_PATH, local_db):
            return 0

        conn = sqlite3.connect(str(local_db))
        conn.row_factory = sqlite3.Row
        since_epoch = since.timestamp() if since else 0.0
        rows = conn.execute(
            """
            SELECT m.id, m.session_id, s.chat_id, m.role, m.timestamp, m.content
            FROM messages m
            JOIN sessions s ON m.session_id = s.id
            WHERE s.source = 'telegram' AND m.timestamp >= ?
            ORDER BY m.timestamp
            """,
            (since_epoch,),
        ).fetchall()
        conn.close()

    out_path = out_dir / "hermes_conversations.jsonl"
    out_dir.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as fh:
        for row in rows:
            record = {
                "id": row["id"],
                "session_id": row["session_id"],
                "chat_id": row["chat_id"],
                "role": row["role"],
                "date": datetime.fromtimestamp(row["timestamp"], tz=timezone.utc).isoformat(),
                "text": row["content"] or "",
            }
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"[hermes] {len(rows)} message(s) written to {out_path}", file=sys.stderr)
    return len(rows)


def _extract_text(content) -> str:
    """OpenClaw message content is a list of blocks (text/tool_use/tool_result/...);
    flatten to just the human-readable text portions."""
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    parts = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(p for p in parts if p)


def export_openclaw(out_dir: Path, since: datetime | None) -> int:
    print(
        f"[openclaw] finding telegram-channel sessions in {_OPENCLAW_CONTAINER}...", file=sys.stderr
    )
    # Server-side: find trajectory files tagged messageChannel:"telegram", map each to
    # its companion plain-transcript file, and tar just those up in one shot — far
    # cheaper than docker-cp'ing hundreds of files individually.
    find_and_tar = (
        f"cd {_OPENCLAW_SESSIONS_DIR} && "
        'grep -l \'"messageChannel":"telegram"\' *.trajectory.jsonl 2>/dev/null '
        "| sed 's/\\.trajectory\\.jsonl$/.jsonl/' "
        "| tar czf /tmp/openclaw_tg_sessions.tar.gz -T - 2>/dev/null; "
        "echo DONE"
    )
    result = subprocess.run(
        ["docker", "exec", _OPENCLAW_CONTAINER, "sh", "-c", find_and_tar],
        capture_output=True,
        text=True,
        check=False,
    )
    if "DONE" not in result.stdout:
        print(
            f"  WARN: could not enumerate OpenClaw sessions: {result.stderr.strip()}",
            file=sys.stderr,
        )
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        local_tar = tmp_path / "openclaw_tg_sessions.tar.gz"
        if not _docker_read_file(
            _OPENCLAW_CONTAINER, "/tmp/openclaw_tg_sessions.tar.gz", local_tar
        ):
            return 0
        subprocess.run(
            ["docker", "exec", _OPENCLAW_CONTAINER, "rm", "-f", "/tmp/openclaw_tg_sessions.tar.gz"],
            capture_output=True,
            check=False,
        )

        extract_dir = tmp_path / "sessions"
        extract_dir.mkdir()
        with tarfile.open(local_tar) as tf:
            tf.extractall(extract_dir, filter="data")

        session_files = sorted(extract_dir.glob("*.jsonl"))
        print(
            f"[openclaw] {len(session_files)} telegram-channel session file(s) found",
            file=sys.stderr,
        )

        matched = []
        for session_file in session_files:
            session_id = session_file.stem
            with session_file.open(encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if entry.get("type") != "message":
                        continue
                    ts_raw = entry.get("timestamp")
                    if not ts_raw:
                        continue
                    try:
                        ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                    except ValueError:
                        continue
                    if since and ts < since:
                        continue
                    message = entry.get("message", {})
                    matched.append(
                        {
                            "session_id": session_id,
                            "id": entry.get("id"),
                            "role": message.get("role"),
                            "date": ts.isoformat(),
                            "text": _extract_text(message.get("content")),
                        }
                    )

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "openclaw_conversations.jsonl"
    matched.sort(key=lambda m: m["date"])
    with out_path.open("w", encoding="utf-8") as fh:
        for record in matched:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"[openclaw] {len(matched)} message(s) written to {out_path}", file=sys.stderr)
    return len(matched)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export Hermes/OpenClaw's own persisted Telegram conversation history to JSONL"
    )
    parser.add_argument(
        "--bot",
        choices=["hermes", "openclaw", "all"],
        default="all",
        help="Which bot's conversations to export (default: all)",
    )
    parser.add_argument(
        "--out-dir",
        default="bot_conversations_export",
        help="Local output directory (default: bot_conversations_export)",
    )
    parser.add_argument(
        "--since",
        default=None,
        help="Only export messages on/after this date "
        "(YYYY-MM-DD or 'YYYY-MM-DD HH:MM'; naive values are treated as UTC). "
        "Default: export full history.",
    )
    args = parser.parse_args()

    since = _parse_since(args.since) if args.since else None
    out_dir = Path(args.out_dir)

    total = 0
    if args.bot in ("hermes", "all"):
        total += export_hermes(out_dir, since)
    if args.bot in ("openclaw", "all"):
        total += export_openclaw(out_dir, since)
    print(f"Done. {total} message(s) total written under {out_dir}", file=sys.stderr)


if __name__ == "__main__":
    main()
