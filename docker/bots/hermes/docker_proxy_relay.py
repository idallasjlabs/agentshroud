#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Relays 127.0.0.1:HERMES_DOCKER_RELAY_PORT -> docker-socket-proxy:2375.

Hermes's sandboxed terminal tool (terminal.backend=docker) checks Docker
availability via `docker version` before every sandboxed run
(tools/terminal_tool.py::check_terminal_requirements). Connecting the Docker
CLI directly to docker-socket-proxy over TCP fails with a spurious
"405 Method Not Allowed" on the CLI's second request on the connection (the
`GET /vX.Y/version` that follows the `HEAD /_ping` version-negotiation probe)
— confirmed 2026-08-22: curl issuing the identical two requests on the same
kept-alive connection succeeds every time; only the Docker CLI's own Go HTTP
client triggers it. This silently disabled the terminal tool for every cron
job (check_terminal_requirements returns False -> "dependent tools will be
unavailable this turn"), which is why cron jobs whose prompts run a script
via terminal (e.g. the newsletter jobs' append_finding.py step) produced
empty output despite reporting "completed".

The exact HAProxy-side mechanism was never pinned down (tried switching
`option http-server-close` -> `http-keep-alive`; no effect) — this is the
same category of HTTP/1.1 keep-alive framing mismatch already worked around
once in this codebase for the same underlying proxy stack, see
dashboard_bridge.py's docstring. That fix forced `Connection: close` at the
HTTP level; this one sidesteps the whole class of bug more simply by not
parsing HTTP at all — a dumb byte-for-byte TCP relay conclusively fixes it
(verified live: `docker version`/`ps`/`info` all succeed through it,
consistently, in a way direct connection to docker-socket-proxy never does).

Point DOCKER_HOST at 127.0.0.1:<this port> instead of docker-socket-proxy:2375
directly. Runs inside Hermes's own container/network namespace — no
additional network exposure, no changes to docker-socket-proxy's own ACLs.
"""

import asyncio
import os

RELAY_PORT = int(os.environ.get("HERMES_DOCKER_RELAY_PORT", "12375"))
TARGET_HOST = os.environ.get("HERMES_DOCKER_PROXY_HOST", "docker-socket-proxy")
TARGET_PORT = int(os.environ.get("HERMES_DOCKER_PROXY_PORT", "2375"))


async def _pump(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    try:
        while True:
            chunk = await reader.read(65536)
            if not chunk:
                break
            writer.write(chunk)
            await writer.drain()
    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        writer.close()


async def _handle(client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter) -> None:
    try:
        upstream_reader, upstream_writer = await asyncio.open_connection(TARGET_HOST, TARGET_PORT)
    except OSError:
        client_writer.close()
        return
    await asyncio.gather(
        _pump(client_reader, upstream_writer),
        _pump(upstream_reader, client_writer),
    )


async def main() -> None:
    server = await asyncio.start_server(_handle, "127.0.0.1", RELAY_PORT)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
