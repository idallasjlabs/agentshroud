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

Output format (JSONL — one JSON object per line):
  {"id": 1234, "date": "2026-01-01T10:00:00+00:00", "out": true, "sender": "@you",
   "text": "hello", "reply_to_msg_id": null, "media": null, "edit_date": null}
"""

import argparse
import asyncio
import json
import os
import sys
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


async def export(entity: str, out_path: Path, limit: int, session: str) -> int:
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

        count = 0
        with out_path.open("w", encoding="utf-8") as fh:
            async for msg in client.iter_messages(
                target,
                limit=limit or None,
                reverse=True,  # oldest first
            ):
                fh.write(json.dumps(_serialize(msg), ensure_ascii=False) + "\n")
                count += 1
                if count % 500 == 0:
                    print(f"  {count} messages...", file=sys.stderr)

        print(f"Done. {count} messages written to {out_path}", file=sys.stderr)
        return count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export Telegram chat history to JSONL"
    )
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
    args = parser.parse_args()

    asyncio.run(export(args.entity, Path(args.out), args.limit, args.session))


if __name__ == "__main__":
    main()
