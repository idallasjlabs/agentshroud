#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Relays 0.0.0.0:HERMES_DASHBOARD_BRIDGE_PORT -> 127.0.0.1:HERMES_DASHBOARD_PORT.

Hermes's own dashboard binds loopback-only (HERMES_DASHBOARD_HOST=127.0.0.1) to satisfy
the vendored hermes-agent image's v0.15.1+ auth gate without configuring basic auth. That
makes it unreachable from the gateway container over the Docker network, since loopback
in one container's network namespace is never the same loopback as another container's.

This bridge runs inside Hermes's own container (same network namespace as the dashboard
server), so its 127.0.0.1 really is the dashboard's loopback. It just re-exposes that
dashboard on a second, network-reachable port. It carries no auth of its own — access
control is Tailscale network membership + Docker network isolation, same as documented
in gateway/ingest_api/lifespan.py's Hermes dashboard forwarder.

The dashboard also enforces Starlette's TrustedHostMiddleware: any request whose Host
header isn't exactly "127.0.0.1:<port>" gets a 400 ("Invalid Host header..."), regardless
of the actual TCP source — this checks the HTTP header, not the socket peer. Every real
request arrives with Host: marvin.tail240ea8.ts.net (or whatever the tailnet hostname is),
so this bridge rewrites the Host header of the first request on each connection to match
what the dashboard expects, and forces Connection: close (unless it's a WebSocket upgrade)
so we never need to track HTTP/1.1 keep-alive framing just to find the next request.
"""

import asyncio
import os
import sys

BRIDGE_PORT = int(os.environ.get("HERMES_DASHBOARD_BRIDGE_PORT", "9120"))
TARGET_HOST = "127.0.0.1"
TARGET_PORT = int(os.environ.get("HERMES_DASHBOARD_PORT", "9119"))
DASHBOARD_ENABLED = os.environ.get("HERMES_DASHBOARD", "").strip() == "1"

_MAX_HEADER_BYTES = 65536


def rewrite_request_headers(headers: bytes, new_host: bytes) -> bytes:
    """Rewrite the Host header to `new_host` and normalize Connection framing.

    `headers` is the request line + header lines (no trailing blank line).
    WebSocket upgrades keep their original Connection header (must stay
    "Upgrade", not "close", or the handshake and the long-lived session
    after it break). Everything else gets Connection: close so the
    dashboard never keeps the connection alive for a second request whose
    Host header we wouldn't otherwise get a chance to rewrite.
    """
    lines = headers.split(b"\r\n")
    is_websocket = any(
        line.lower().startswith(b"upgrade:") and b"websocket" in line.lower() for line in lines
    )

    out = []
    saw_connection = False
    for line in lines:
        lower = line.lower()
        if lower.startswith(b"host:"):
            out.append(b"Host: " + new_host)
        elif lower.startswith(b"connection:"):
            saw_connection = True
            out.append(line if is_websocket else b"Connection: close")
        else:
            out.append(line)

    if not saw_connection and not is_websocket:
        out.append(b"Connection: close")

    return b"\r\n".join(out)


async def _read_request_headers(reader: asyncio.StreamReader) -> tuple[bytes, bytes]:
    """Read up to the end of the request's header block (\\r\\n\\r\\n).

    Returns (headers, leftover) where leftover is any already-buffered bytes
    that belong to the request body (or a pipelined next request — dropped
    on the floor is fine here since we force Connection: close).
    """
    buf = b""
    while b"\r\n\r\n" not in buf and len(buf) < _MAX_HEADER_BYTES:
        chunk = await reader.read(4096)
        if not chunk:
            break
        buf += chunk
    headers, _, rest = buf.partition(b"\r\n\r\n")
    return headers, rest


async def _pipe(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        while True:
            chunk = await reader.read(65536)
            if not chunk:
                break
            writer.write(chunk)
            await writer.drain()
    except Exception:
        pass
    finally:
        try:
            writer.close()
        except Exception:
            pass


async def _handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        r2, w2 = await asyncio.open_connection(TARGET_HOST, TARGET_PORT)
    except Exception:
        try:
            writer.write(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            writer.close()
        except Exception:
            pass
        return

    new_host = f"{TARGET_HOST}:{TARGET_PORT}".encode()
    try:
        headers, rest = await _read_request_headers(reader)
        if headers:
            rewritten = rewrite_request_headers(headers, new_host)
            w2.write(rewritten + b"\r\n\r\n" + rest)
            await w2.drain()
        elif rest:
            w2.write(rest)
            await w2.drain()
    except Exception:
        pass

    await asyncio.gather(_pipe(reader, w2), _pipe(r2, writer), return_exceptions=True)


async def main() -> None:
    if not DASHBOARD_ENABLED:
        # Dashboard disabled for this deploy — idle rather than bind a pointless port.
        await asyncio.Event().wait()
        return
    server = await asyncio.start_server(_handle, "0.0.0.0", BRIDGE_PORT)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
