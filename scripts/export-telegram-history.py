#!/usr/bin/env python3
"""
Export full Telegram chat history with a contact/bot to JSONL.

Requirements:
  pip install telethon

Credentials (environment variables):
  TELEGRAM_API_ID    - From https://my.telegram.org/apps
  TELEGRAM_API_HASH  - From https://my.telegram.org/apps
  TELEGRAM_PHONE     - Your phone number (e.g. +15551234567)

Usage:
  python scripts/export-telegram-history.py
  python scripts/export-telegram-history.py --entity @therealidallasj --out history.jsonl
  python scripts/export-telegram-history.py --entity @therealidallasj --limit 1000
  python scripts/export-telegram-history.py --entity @agentshroud_bot --since 2026-08-01
  python scripts/export-telegram-history.py --entity @agentshroud_bot --since "2026-08-01 14:30"

Output format (JSONL — one JSON object per line):
  {"id": 1234, "date": "2026-01-01T10:00:00+00:00", "out": true, "sender": "@you",
   "text": "hello", "reply_to_msg_id": null, "media": null, "edit_date": null}
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    from telethon import TelegramClient
    from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto
except ImportError:
    print("ERROR: telethon is not installed.", file=sys.stderr)
    print("  pip install telethon", file=sys.stderr)
    sys.exit(1)


def _require_env(key: str) -> str:
    val = os.environ.get(key, "").strip()
    if not val:
        print(f"ERROR: ${key} is not set", file=sys.stderr)
        sys.exit(1)
    return val


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


def _serialize(msg) -> dict:
    sender = None
    if msg.sender:
        s = msg.sender
        if getattr(s, "username", None):
            sender = f"@{s.username}"
        elif getattr(s, "first_name", None):
            sender = f"{s.first_name or ''} {s.last_name or ''}".strip()
        elif getattr(s, "title", None):
            sender = s.title

    media = None
    if msg.media:
        if isinstance(msg.media, MessageMediaPhoto):
            photo = msg.media.photo
            media = {"type": "photo", "id": photo.id if photo else None}
        elif isinstance(msg.media, MessageMediaDocument):
            doc = msg.media.document
            media = {"type": "document", "id": doc.id if doc else None}
        else:
            media = {"type": type(msg.media).__name__}

    return {
        "id": msg.id,
        "date": msg.date.isoformat() if msg.date else None,
        "out": bool(msg.out),
        "sender": sender,
        "text": msg.message or "",
        "reply_to_msg_id": msg.reply_to.reply_to_msg_id if msg.reply_to else None,
        "media": media,
        "edit_date": msg.edit_date.isoformat() if msg.edit_date else None,
    }


async def export(
    entity: str, out_path: Path, limit: int, session: str, since: datetime | None = None
) -> int:
    api_id = int(_require_env("TELEGRAM_API_ID"))
    api_hash = _require_env("TELEGRAM_API_HASH")
    phone = _require_env("TELEGRAM_PHONE")

    async with TelegramClient(session, api_id, api_hash) as client:
        await client.start(phone=phone)

        print(f"Resolving: {entity}", file=sys.stderr)
        target = await client.get_entity(entity)
        name = getattr(target, "username", None) or getattr(target, "first_name", str(target.id))
        print(f"Exporting history with: {name} (id={target.id})", file=sys.stderr)
        print(f"Output: {out_path}", file=sys.stderr)
        if since:
            print(f"Since: {since.isoformat()}", file=sys.stderr)

        count = 0
        skipped_before_since = 0
        with out_path.open("w", encoding="utf-8") as fh:
            async for msg in client.iter_messages(
                target,
                limit=limit or None,
                reverse=True,  # oldest first
                # Telethon: with reverse=True, offset_date acts as an inclusive
                # LOWER bound (only messages on/after this date are returned) —
                # this is a native API-level filter, not a client-side cut.
                offset_date=since,
            ):
                # Defensive client-side cut: guards against any off-by-one/edge
                # behavior in offset_date so --since is always honored exactly,
                # even if a boundary message slips through from the API.
                if since and msg.date and msg.date < since:
                    skipped_before_since += 1
                    continue
                fh.write(json.dumps(_serialize(msg), ensure_ascii=False) + "\n")
                count += 1
                if count % 500 == 0:
                    print(f"  {count} messages...", file=sys.stderr)

        if skipped_before_since:
            print(f"  (filtered {skipped_before_since} message(s) before --since)", file=sys.stderr)
        print(f"Done. {count} messages written to {out_path}", file=sys.stderr)
        return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Telegram chat history to JSONL")
    parser.add_argument(
        "--entity",
        default="@agentshroud_bot",
        help="Username, phone number, or numeric chat ID (default: @agentshroud_bot)",
    )
    parser.add_argument(
        "--out",
        default="telegram_history.jsonl",
        help="Output file path (default: telegram_history.jsonl)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max messages to fetch; 0 = all (default: 0)",
    )
    parser.add_argument(
        "--session",
        default="tg_export_session",
        help="Telethon session file name (default: tg_export_session)",
    )
    parser.add_argument(
        "--since",
        default=None,
        help="Only export messages on/after this date/time "
        "(YYYY-MM-DD or 'YYYY-MM-DD HH:MM'; naive values are treated as UTC). "
        "Default: export full history.",
    )
    args = parser.parse_args()

    since = _parse_since(args.since) if args.since else None
    asyncio.run(export(args.entity, Path(args.out), args.limit, args.session, since))


if __name__ == "__main__":
    main()
