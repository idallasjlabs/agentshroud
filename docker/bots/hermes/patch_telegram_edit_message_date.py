#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Streaming-edit failure fix (2026-10-16): Hermes's _edit_text
# (plugins/platforms/telegram/adapter.py) calls self._bot.edit_message_text(),
# which on success parses Telegram's response into a python-telegram-bot
# Message object via MaybeInaccessibleMessage._de_json (telegram/_message.py):
#
#     if data["date"] == 0:
#         ...
#
# a bare dict subscript, not .get(). Confirmed live tonight: Telegram returned
# an edit-success payload with NO "date" key at all (not an InaccessibleMessage
# -- those use date=0, a present key with value 0) -- so parsing raised
# KeyError('date') AFTER the edit had already applied server-side. Hermes's
# own exception handling (_edit_markdown_or_plain's caller) then logged this
# as "Failed to edit Telegram message N: 'date'" and gave up, even though the
# edit succeeded -- a spurious failure on a parsing bug in the pinned library,
# not an actual delivery failure.
#
# Patches _edit_text to catch this specific KeyError and treat it as success
# (mirrors the existing "not modified" handling in _edit_markdown_or_plain --
# a known Telegram response quirk that isn't a real failure). Re-raises any
# other KeyError untouched.
#
# Run as a standalone script at build time (docker/bots/hermes/Dockerfile),
# NOT as a Dockerfile-embedded RUN heredoc -- see patch_telegram_do_request.py
# for why (BuildKit-only heredoc syntax silently no-ops on classic builders).

import sys

PATH = "/opt/hermes/plugins/platforms/telegram/adapter.py"

anchor = (
    "    async def _edit_text(self, chat_id: str, message_id: str, text: str, parse_mode: Any = None) -> None:\n"
    '        """``editMessageText`` with normalized ids; ``parse_mode=None`` sends plain text."""\n'
    '        kwargs: Dict[str, Any] = {"chat_id": normalize_telegram_chat_id(chat_id), "message_id": int(message_id), "text": text}\n'
    "        if parse_mode is not None:\n"
    '            kwargs["parse_mode"] = parse_mode\n'
    "        await _await_with_thread_deadline(\n"
    '            self._bot.edit_message_text(**kwargs), timeout=_TEXT_SEND_DEADLINE, label="telegram-send", dump_on_blocked_loop=False)\n'
)

replacement = (
    "    async def _edit_text(self, chat_id: str, message_id: str, text: str, parse_mode: Any = None) -> None:\n"
    '        """``editMessageText`` with normalized ids; ``parse_mode=None`` sends plain text."""\n'
    '        kwargs: Dict[str, Any] = {"chat_id": normalize_telegram_chat_id(chat_id), "message_id": int(message_id), "text": text}\n'
    "        if parse_mode is not None:\n"
    '            kwargs["parse_mode"] = parse_mode\n'
    "        try:\n"
    "            await _await_with_thread_deadline(\n"
    '                self._bot.edit_message_text(**kwargs), timeout=_TEXT_SEND_DEADLINE, label="telegram-send", dump_on_blocked_loop=False)\n'
    "        except KeyError as _date_err:\n"
    "            # AgentShroud patch: python-telegram-bot's Message._de_json does a bare\n"
    '            # data["date"] (telegram/_message.py) when parsing editMessageText\'s\n'
    "            # response. Telegram has returned success payloads missing a 'date' key\n"
    "            # entirely (observed live, not an InaccessibleMessage case -- those use\n"
    "            # date=0, a present key). The edit already applied server-side by the\n"
    "            # time this raises; only the client-side response parsing failed. Treat\n"
    "            # as success rather than surface a spurious failure for an edit that\n"
    "            # actually went through.\n"
    '            if _date_err.args and _date_err.args[0] == "date":\n'
    "                logger.warning(\n"
    "                    \"[%s] editMessageText succeeded but response parsing raised \"\n"
    "                    \"KeyError('date') (python-telegram-bot response-parsing quirk) \"\n"
    '                    "-- treating as success", self.name)\n'
    "            else:\n"
    "                raise\n"
)

src = open(PATH, encoding="utf-8").read()
# Hermes >= v0.22 annotates kwargs as builtin `dict[...]` instead of typing `Dict[...]`;
# accept either spelling and keep whichever the vendor file uses.
if anchor not in src and anchor.replace("Dict[str, Any]", "dict[str, Any]") in src:
    anchor = anchor.replace("Dict[str, Any]", "dict[str, Any]")
    replacement = replacement.replace("Dict[str, Any]", "dict[str, Any]")
if anchor not in src:
    sys.exit(
        "PATCH ANCHOR NOT FOUND (_edit_text) -- upstream digest drift. "
        "Re-verify docker/bots/hermes/patch_telegram_edit_message_date.py "
        f"against {PATH}."
    )

new_src = src.replace(anchor, replacement, 1)
compile(new_src, PATH, "exec")
open(PATH, "w", encoding="utf-8").write(new_src)
print(f"[hermes-build] telegram edit_message KeyError('date') patch applied to {PATH}")
