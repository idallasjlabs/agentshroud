#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Crash-loop fix (2026-09-18): slack_sdk's AsyncSocketModeClient (aiohttp
# backend) creates exactly one aiohttp.ClientSession in __init__ and reuses it
# for every WSS reconnect in connect()'s retry loop. But close() -- called by
# slack_bolt.AsyncApp's own supervisor on some disconnects, not only on final
# shutdown -- permanently closes that same aiohttp_client_session. Every
# connect() attempt after that calls
# self.aiohttp_client_session.ws_connect(...) against an already-closed
# session, which aiohttp itself raises as "RuntimeError: Session is closed".
# connect()'s except-and-retry loop then retries forever against the same
# dead session -- observed live in prod, continuous
# "slack_bolt.AsyncApp: Failed to connect (error: Session is closed);
# Retrying..." with no recovery possible short of restarting the whole
# process (which is the only thing that re-runs __init__ and gets a fresh
# session).
#
# Patches connect() to transparently recreate aiohttp_client_session when it
# finds it closed, before attempting ws_connect() -- the same self-healing
# behavior the loop already gives current_session (the individual WS
# connection), just extended to the ClientSession that creates it.
#
# PARTIAL FIX -- does not fully stop the crash-loop; see the owner-relayed
# investigation notes for 2026-09-18. Hermes's own adapter.py already has
# defensive cancellation around this exact upstream bug
# (slackapi/python-slack-sdk#1913) and it still recurs, suggesting a deeper
# TOCTOU race between the watchdog's _restart_socket_mode() and an in-flight
# connect() that this patch alone does not close. Ship as a real
# improvement, not a resolution.

import glob
import sys

candidates = glob.glob(
    "/opt/hermes/.venv/lib/python3.*/site-packages/slack_sdk/socket_mode/aiohttp/__init__.py"
)
if not candidates:
    sys.exit(
        "PATCH ANCHOR NOT FOUND -- slack_sdk socket_mode/aiohttp/__init__.py not present "
        "at the expected venv path; re-verify docker/bots/hermes/patch_slack_session_recreate.py."
    )
p = candidates[0]
src = open(p, encoding="utf-8").read()

anchor = (
    "                self.current_session = await self.aiohttp_client_session.ws_connect(\n"
    "                    self.wss_uri,"
)
if anchor not in src:
    sys.exit(
        "PATCH ANCHOR NOT FOUND in slack_sdk socket_mode/aiohttp/__init__.py -- "
        "upstream slack_sdk version drift; re-verify "
        "docker/bots/hermes/patch_slack_session_recreate.py against the vendored version."
    )

replacement = (
    "                # AgentShroud patch: aiohttp_client_session is a long-lived singleton\n"
    "                # (created once in __init__) that close() can permanently close on a\n"
    "                # non-final disconnect. Recreate it here so this retry loop can actually\n"
    "                # recover instead of raising \"Session is closed\" forever.\n"
    "                if self.aiohttp_client_session is None or self.aiohttp_client_session.closed:\n"
    "                    # NOTE: __init__ takes a `loop` param but never stores it on self,\n"
    "                    # so it isn't available to recreate against here -- omitting it is\n"
    "                    # correct anyway: aiohttp.ClientSession() with no loop arg binds to\n"
    "                    # the current running loop, which is what we're already inside.\n"
    "                    self.aiohttp_client_session = aiohttp.ClientSession()\n"
    "                    self.logger.info(\"Recreated a closed aiohttp ClientSession before reconnecting\")\n"
    "                self.current_session = await self.aiohttp_client_session.ws_connect(\n"
    "                    self.wss_uri,"
)

new_src = src.replace(anchor, replacement, 1)
if new_src == src:
    sys.exit("PATCH DID NOT APPLY -- replace() was a no-op")
compile(new_src, p, "exec")
open(p, "w", encoding="utf-8").write(new_src)
print(f"[hermes-build] slack socket-mode session-recreate patch applied ({p})")
