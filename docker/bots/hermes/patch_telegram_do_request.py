#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Crash-loop fix (2026-07-17): the Telegram adapter's getUpdates health instrumentation
# does `request.do_request = _do_request` to wrap polling requests, but the vendored
# python-telegram-bot 22.6 makes HTTPXRequest __slots__-based (do_request is a class
# method, not an instance attribute) — the assignment raises "AttributeError:
# 'HTTPXRequest' object attribute 'do_request' is read-only" on EVERY boot. Telegram is
# Hermes's only enabled platform (docker/config/hermes/config.yaml.tmpl `telegram.enabled:
# true`), so the failed connect drops the gateway to 0 connected platforms and it exits;
# `restart: unless-stopped` then crash-loops it forever (observed: 175 restarts in prod).
#
# Patches the assignment to fall back to a __class__ swap onto an instrumented subclass,
# which preserves the getUpdates progress instrumentation under PTB's slots. Self-
# verifying: fails loudly if the upstream anchor moved (digest drift) instead of silently
# no-op'ing, and re-checks the fix against the PTB actually vendored in this image rather
# than trusting it blindly.
#
# Run as a standalone script at build time (docker/bots/hermes/Dockerfile), NOT as a
# Dockerfile-embedded RUN heredoc: Docker's `RUN <<'EOF' ... EOF` heredoc syntax is a
# BuildKit-only feature. On a Docker Engine without the buildx component, the classic
# builder silently mishandles it (reports "Using cache" and never actually runs the
# patch), producing an image that looks built successfully but still has the
# crash-causing bug. Reproduced live on a real host lacking buildx. A plain .py file
# invoked via `RUN python3 /path/to/script.py` works identically under both builders.

import sys

p = "/opt/hermes/plugins/platforms/telegram/adapter.py"
src = open(p, encoding="utf-8").read()
anchor = "        request.do_request = _do_request\n        return request"
if anchor not in src:
    sys.exit(
        "PATCH ANCHOR NOT FOUND in telegram adapter.py -- upstream digest drift; "
        "re-verify the do_request fix in docker/bots/hermes/patch_telegram_do_request.py."
    )

replacement = (
    "        try:\n"
    "            request.do_request = _do_request\n"
    "        except AttributeError:\n"
    "            # AgentShroud patch: PTB >=22 HTTPXRequest is __slots__-based; instance\n"
    "            # override raises \"attribute 'do_request' is read-only\". Swap to a\n"
    "            # subclass whose do_request delegates to the wrapper so getUpdates\n"
    "            # progress instrumentation survives on PTB 22.x.\n"
    "            _wrapped = _do_request\n"
    "            class _InstrumentedHTTPXRequest(type(request)):\n"
    "                __slots__ = ()\n"
    "                async def do_request(self, *a, **k):\n"
    "                    return await _wrapped(*a, **k)\n"
    "            request.__class__ = _InstrumentedHTTPXRequest\n"
    "        return request"
)

new_src = src.replace(anchor, replacement, 1)
if new_src == src:
    sys.exit("PATCH DID NOT APPLY -- replace() was a no-op")
compile(new_src, p, "exec")
open(p, "w", encoding="utf-8").write(new_src)
print("[hermes-build] telegram do_request patch applied (anchor matched, syntax verified)")

# Runtime self-verify: confirm the __class__-swap technique actually works against
# the python-telegram-bot version vendored in THIS image.
from telegram.request import HTTPXRequest

r = HTTPXRequest()
orig = type(r).do_request


async def _wrapped(*a, **k):
    return await orig(r, *a, **k)


try:
    r.do_request = _wrapped
    print(
        "[hermes-build] WARNING: instance-assign succeeded directly on this PTB "
        "version -- the fallback branch is now dead code (harmless, but re-check "
        "on next digest refresh)."
    )
except AttributeError:
    cls = type(r)
    _w2 = _wrapped

    class _Instr(cls):
        __slots__ = ()

        async def do_request(self, *a, **k):
            return await _w2(*a, **k)

    r.__class__ = _Instr
    assert r.do_request.__func__ is _Instr.do_request
    print("[hermes-build] telegram do_request patch verified against live PTB (class swap works)")
