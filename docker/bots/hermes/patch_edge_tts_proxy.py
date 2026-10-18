#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Edge TTS DNS-failure fix (2026-10-14): Hermes runs on the agentshroud-isolated
# Docker network (internal: true, no general internet egress by design) and
# relies on HTTP_PROXY/HTTPS_PROXY (set in run-standalone.sh) for all outbound
# traffic. edge_tts.Communicate's websocket connection to
# speech.platform.bing.com does NOT honor those env vars -- aiohttp's
# `trust_env=True` is only applied by ClientSession.get()/post(); ws_connect()
# ignores it and always attempts a direct connection unless a `proxy=` kwarg
# is passed explicitly (confirmed live: ws_connect raised
# ClientConnectorDNSError / "Temporary failure in name resolution" with
# trust_env=True and HTTPS_PROXY set, and only reached the gateway proxy once
# proxy= was passed directly). tools/tts_tool_providers.py's _generate_edge_tts
# never threads a proxy through to Communicate(), so every "Test speaking" /
# Edge TTS call failed outright on this network.
#
# Patches _generate_edge_tts to resolve a proxy via Hermes's own
# gateway.platforms.base.resolve_proxy_url() -- the same helper
# patch_telegram_send_base_url.py's Bot() fallback uses -- which already
# reads HTTPS_PROXY/HTTP_PROXY and respects NO_PROXY, and pass it to
# Communicate(proxy=...). Also requires speech.platform.bing.com to be in
# gateway/security/egress_config.py's PERMANENT_EGRESS_DOMAINS so the
# gateway's own CONNECT-tunnel proxy doesn't 403 it (added same commit).
#
# A second, independent bug surfaced once the proxy/allowlist fix above let
# the request actually reach speech.platform.bing.com: the exact pin
# "edge-tts==7.2.7" in tools/lazy_deps.py's LAZY_DEPS["tts.edge"] is rejected
# by Microsoft's endpoint with "WSServerHandshakeError: 403, message='Invalid
# response status'" (confirmed live -- Microsoft periodically rotates its
# Sec-MS-GEC anti-abuse token requirements and older edge-tts releases start
# failing the handshake). 7.3.1 (latest on PyPI as of 2026-10-14) was
# confirmed live to complete the same handshake and save real audio.
# _is_satisfied() in lazy_deps.py already re-checks the installed version
# against this exact spec on every lazy-install pass and reinstalls on a
# mismatch ("so hermes update propagates pin bumps to installed backends"),
# so bumping the pin here is sufficient -- no separate reinstall step needed.

import os
import sys

p = "/opt/hermes/tools/tts_tool_providers.py"
src = open(p, encoding="utf-8").read()

anchor = (
    '    kwargs = {"voice": edge_config.get("voice", DEFAULT_EDGE_VOICE)}\n'
    "    if speed != 1.0:\n"
    '        kwargs["rate"] = f"{round((speed - 1.0) * 100):+d}%"\n'
    "    await edge_tts.Communicate(text, **kwargs).save(output_path)\n"
)
if anchor not in src:
    sys.exit(
        "PATCH ANCHOR NOT FOUND in tools/tts_tool_providers.py -- upstream "
        "_generate_edge_tts shape drifted; re-verify "
        "docker/bots/hermes/patch_edge_tts_proxy.py."
    )

replacement = (
    '    kwargs = {"voice": edge_config.get("voice", DEFAULT_EDGE_VOICE)}\n'
    "    if speed != 1.0:\n"
    '        kwargs["rate"] = f"{round((speed - 1.0) * 100):+d}%"\n'
    "    # AgentShroud patch: edge_tts's websocket connect doesn't honor\n"
    "    # HTTP_PROXY/HTTPS_PROXY (aiohttp ws_connect ignores trust_env), and\n"
    "    # Hermes has no general internet egress on this network without it.\n"
    "    try:\n"
    "        from gateway.platforms.base import resolve_proxy_url\n"
    '        _tts_proxy = resolve_proxy_url(target_hosts=["speech.platform.bing.com"])\n'
    "    except Exception:\n"
    "        _tts_proxy = None\n"
    "    if _tts_proxy:\n"
    '        kwargs["proxy"] = _tts_proxy\n'
    "    await edge_tts.Communicate(text, **kwargs).save(output_path)\n"
)

new_src = src.replace(anchor, replacement, 1)
if new_src == src:
    sys.exit("PATCH DID NOT APPLY -- replace() was a no-op")
compile(new_src, p, "exec")
open(p, "w", encoding="utf-8").write(new_src)
print(f"[hermes-build] edge-tts proxy patch applied to {p}")

# --- Patch 2: bump the pinned edge-tts version (Microsoft rejects 7.2.7's
# handshake; 7.3.1 confirmed working) ---

p2 = "/opt/hermes/tools/lazy_deps.py"
src2 = open(p2, encoding="utf-8").read()

anchor2 = '"tts.edge": ("edge-tts==7.2.7",),'
if anchor2 not in src2 and os.path.isfile("/opt/hermes/pm/extras.py"):
    # Hermes >= v0.22: the lazy_deps.py LAZY_DEPS table is gone; the pin lives in
    # pyproject.toml's `edge-tts` extra (+ uv.lock) and availability is a bare
    # find_spec("edge_tts") (pm/extras.py ANCHORS). The Dockerfile therefore
    # pre-installs edge-tts==7.3.1 into the venv right after this patch, so the
    # extra reads as already satisfied and the 7.2.7 pin is never synced.
    print("[hermes-build] lazy_deps.py has no tts.edge pin (Hermes pm/extras layout); "
          "edge-tts 7.3.1 is installed by the Dockerfile instead")
    sys.exit(0)
if anchor2 not in src2:
    sys.exit(
        "PATCH ANCHOR NOT FOUND in tools/lazy_deps.py -- the tts.edge pin "
        "moved or its version changed; re-verify "
        "docker/bots/hermes/patch_edge_tts_proxy.py."
    )
replacement2 = '"tts.edge": ("edge-tts==7.3.1",),'
new_src2 = src2.replace(anchor2, replacement2, 1)
if new_src2 == src2:
    sys.exit("PATCH DID NOT APPLY -- replace() was a no-op (lazy_deps.py)")
compile(new_src2, p2, "exec")
open(p2, "w", encoding="utf-8").write(new_src2)
print(f"[hermes-build] edge-tts version pin bumped 7.2.7 -> 7.3.1 in {p2}")
