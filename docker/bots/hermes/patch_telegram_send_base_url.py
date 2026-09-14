#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Silent-delivery-failure fix (2026-08-18): Hermes's standalone/cron Telegram
# delivery path (tools/send_message_senders.py::_send_telegram, invoked via
# plugins/platforms/telegram/adapter.py::_standalone_send) ignores the
# telegram.extra.base_url/base_file_url config (config.yaml), unlike the
# interactive polling adapter which honours it. It falls back to a bare
# `Bot(token=token)`, which defaults to a direct api.telegram.org connection.
#
# Hermes's own NO_PROXY intentionally keeps api.telegram.org un-proxied
# (docker-compose.yml: "Hermes never connects to api.telegram.org directly;
# EgressFilter still blocks any accidental direct Telegram egress at the
# network level") — Telegram traffic is meant to route through the dedicated
# gateway:8080/telegram-api reverse proxy exclusively, via base_url. On the
# agentshroud-isolated Docker network (no direct external DNS/egress), every
# standalone/cron delivery therefore failed with a silent DNS ConnectError
# while the cron job's own execution still reported "completed" — no error
# surfaced except a per-target delivery warning in `hermes cron list`. This is
# why scheduled reports/newsletters stopped reaching Telegram for days despite
# jobs completing successfully.
#
# Patches _send_telegram to accept base_url/base_file_url and prefer them over
# the proxy-resolution fallback, and _standalone_send to pass pconfig.extra's
# base_url/base_file_url through. Self-verifying: fails loudly if either
# upstream anchor moved (digest drift) instead of silently no-op'ing.
#
# Re-anchored 2026-09-14 for hermes-agent v0.20.6: upstream moved
# _send_telegram out of tools/send_message_tool.py into a new
# tools/send_message_senders.py module, and extracted the old inline
# proxy-fallback Bot-construction block into a shared `_telegram_bot(token)`
# helper (same proxy-resolution logic we used to patch inline — upstream
# independently converged on the same shape). Both call sites were also
# reformatted (fewer lines) and _standalone_send gained an unrelated
# secret_scope token fallback that must be preserved, not clobbered.
#
# Run as a standalone script at build time (docker/bots/hermes/Dockerfile),
# NOT as a Dockerfile-embedded RUN heredoc — see patch_telegram_do_request.py
# for why (BuildKit-only heredoc syntax silently no-ops on classic builders).

import sys

# --- Patch 1: tools/send_message_senders.py — _send_telegram signature + Bot construction ---

p1 = "/opt/hermes/tools/send_message_senders.py"
src1 = open(p1, encoding="utf-8").read()

sig_anchor = (
    "async def _send_telegram(token, chat_id, message, media_files=None, "
    "thread_id=None, disable_link_previews=False, force_document=False):"
)
if sig_anchor not in src1:
    sys.exit(
        "PATCH ANCHOR NOT FOUND (_send_telegram signature) -- upstream digest "
        "drift; re-verify docker/bots/hermes/patch_telegram_send_base_url.py."
    )
sig_replacement = (
    "async def _send_telegram(token, chat_id, message, media_files=None, "
    "thread_id=None, disable_link_previews=False, force_document=False, "
    "base_url=None, base_file_url=None):"
)
src1 = src1.replace(sig_anchor, sig_replacement, 1)

bot_anchor = "        bot = _telegram_bot(token)\n"
if bot_anchor not in src1:
    sys.exit(
        "PATCH ANCHOR NOT FOUND (_send_telegram Bot construction) -- upstream "
        "digest drift; re-verify docker/bots/hermes/patch_telegram_send_base_url.py."
    )
bot_replacement = (
    "        if base_url:\n"
    "            # AgentShroud patch: reuse the gateway:8080/telegram-api reverse\n"
    "            # proxy (config.yaml telegram.extra.base_url) exactly like the\n"
    "            # interactive polling adapter, instead of a direct connection.\n"
    "            from telegram import Bot\n"
    '            _bot_kwargs = {"token": token, "base_url": base_url}\n'
    "            if base_file_url:\n"
    '                _bot_kwargs["base_file_url"] = base_file_url\n'
    '            logger.info("send_message: standalone Telegram send routed via base_url %s", base_url)\n'
    "            bot = Bot(**_bot_kwargs)\n"
    "        else:\n"
    "            bot = _telegram_bot(token)\n"
)
new_src1 = src1.replace(bot_anchor, bot_replacement, 1)
if new_src1 == src1:
    sys.exit("PATCH DID NOT APPLY (send_message_senders.py) -- replace() was a no-op")
compile(new_src1, p1, "exec")
open(p1, "w", encoding="utf-8").write(new_src1)
print("[hermes-build] telegram send_message base_url patch applied to send_message_senders.py")

# --- Patch 1b: tools/send_message_tool.py — _send_to_platform's own Telegram
# call site (cron job "Deliver: telegram" targets go through this function
# directly, NEVER through plugins/platforms/telegram/adapter.py — Patch 2
# below only covers agent-invoked send_message tool calls). Found 2026-08-23:
# every cron job configured with `Deliver: telegram` (not the send_message
# tool) still fell back to a direct api.telegram.org connection because this
# call site never passed base_url/base_file_url, even after Patch 1/2 shipped. ---

p1b = "/opt/hermes/tools/send_message_tool.py"
src1b = open(p1b, encoding="utf-8").read()

call1b_anchor = (
    "    if platform == Platform.TELEGRAM:\n"
    "        return await _send_telegram(\n"
    "            pconfig.token, chat_id, message, media_files=media_files, thread_id=thread_id, force_document=force_document,\n"
    '            disable_link_previews=bool(getattr(pconfig, "extra", {}) and pconfig.extra.get("disable_link_previews")))\n'
)
if call1b_anchor not in src1b:
    sys.exit(
        "PATCH ANCHOR NOT FOUND (_send_to_platform Telegram call site) -- "
        "upstream digest drift; re-verify "
        "docker/bots/hermes/patch_telegram_send_base_url.py."
    )
call1b_replacement = (
    "    if platform == Platform.TELEGRAM:\n"
    "        # AgentShroud patch: pass telegram.extra.base_url/base_file_url\n"
    "        # through here too — cron job Telegram delivery routes through\n"
    "        # this function directly, bypassing plugins/platforms/telegram/\n"
    "        # adapter.py entirely, so Patch 2's fix never applied to it.\n"
    '        _extra1b = getattr(pconfig, "extra", {}) or {}\n'
    "        return await _send_telegram(\n"
    "            pconfig.token, chat_id, message, media_files=media_files, thread_id=thread_id, force_document=force_document,\n"
    '            disable_link_previews=bool(_extra1b and _extra1b.get("disable_link_previews")),\n'
    '            base_url=_extra1b.get("base_url"), base_file_url=_extra1b.get("base_file_url"))\n'
)
new_src1b = src1b.replace(call1b_anchor, call1b_replacement, 1)
if new_src1b == src1b:
    sys.exit("PATCH DID NOT APPLY (send_message_tool.py _send_to_platform) -- replace() was a no-op")
compile(new_src1b, p1b, "exec")
open(p1b, "w", encoding="utf-8").write(new_src1b)
print("[hermes-build] telegram base_url patch applied to _send_to_platform call site")

# --- Patch 2: plugins/platforms/telegram/adapter.py — _standalone_send passthrough ---

p2 = "/opt/hermes/plugins/platforms/telegram/adapter.py"
src2 = open(p2, encoding="utf-8").read()

call_anchor = (
    "async def _standalone_send(pconfig, chat_id, message, *, thread_id=None, media_files=None, force_document=False):\n"
    '    """Out-of-process delivery (standalone_sender_fn) so deliver=telegram cron jobs succeed without the\n'
    "    gateway; delegates to the REST ``_send_telegram`` sender.\"\"\"\n"
    '    token = getattr(pconfig, "token", None)\n'
    "    if not token:\n"
    "        from agent.secret_scope import get_secret  # profile-scoped: never borrow another profile's token\n"
    '        token = get_secret("TELEGRAM_BOT_TOKEN", "") or ""\n'
    '    disable_link_previews = bool(getattr(pconfig, "extra", {}) and pconfig.extra.get("disable_link_previews"))\n'
    "    from tools.send_message_tool import _send_telegram\n"
    "    return await _send_telegram(\n"
    "        token, chat_id, message, media_files=media_files, thread_id=thread_id,\n"
    "        disable_link_previews=disable_link_previews, force_document=force_document)\n"
)
if call_anchor not in src2:
    sys.exit(
        "PATCH ANCHOR NOT FOUND (_standalone_send call site) -- upstream digest "
        "drift; re-verify docker/bots/hermes/patch_telegram_send_base_url.py."
    )
call_replacement = (
    "async def _standalone_send(pconfig, chat_id, message, *, thread_id=None, media_files=None, force_document=False):\n"
    '    """Out-of-process delivery (standalone_sender_fn) so deliver=telegram cron jobs succeed without the\n'
    "    gateway; delegates to the REST ``_send_telegram`` sender.\"\"\"\n"
    '    token = getattr(pconfig, "token", None)\n'
    "    if not token:\n"
    "        from agent.secret_scope import get_secret  # profile-scoped: never borrow another profile's token\n"
    '        token = get_secret("TELEGRAM_BOT_TOKEN", "") or ""\n'
    '    disable_link_previews = bool(getattr(pconfig, "extra", {}) and pconfig.extra.get("disable_link_previews"))\n'
    "    # AgentShroud patch: pass telegram.extra.base_url/base_file_url through so\n"
    "    # standalone/cron delivery reuses the gateway:8080/telegram-api reverse\n"
    "    # proxy instead of silently defaulting to a direct connection.\n"
    '    _extra = getattr(pconfig, "extra", {}) or {}\n'
    '    base_url = _extra.get("base_url")\n'
    '    base_file_url = _extra.get("base_file_url")\n'
    "    from tools.send_message_tool import _send_telegram\n"
    "    return await _send_telegram(\n"
    "        token, chat_id, message, media_files=media_files, thread_id=thread_id,\n"
    "        disable_link_previews=disable_link_previews, force_document=force_document,\n"
    "        base_url=base_url, base_file_url=base_file_url)\n"
)
new_src2 = src2.replace(call_anchor, call_replacement, 1)
if new_src2 == src2:
    sys.exit("PATCH DID NOT APPLY (adapter.py) -- replace() was a no-op")
compile(new_src2, p2, "exec")
open(p2, "w", encoding="utf-8").write(new_src2)
print("[hermes-build] telegram send_message base_url patch applied to adapter.py")
