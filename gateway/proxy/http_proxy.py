# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""HTTP CONNECT proxy server — intercepts all bot outbound traffic.

Listens on port 8181. When the bot's HTTP_PROXY / HTTPS_PROXY env vars
point here (activated in the FINAL PR), every outbound connection from
the bot must pass through this server and be validated against the
domain allowlist before a TCP tunnel is established.

Running this server now adds zero risk — the bot has no HTTP_PROXY set
yet, so it doesn't use this server until FINAL.
"""
from __future__ import annotations


import asyncio
import logging
import time
from typing import Optional

from .web_config import WebProxyConfig
from .web_proxy import WebProxy

logger = logging.getLogger("agentshroud.proxy.http_proxy")

# Default allowlist: only the domains the bot legitimately needs
ALLOWED_DOMAINS: list[str] = [
    "api.openai.com",
    "api.anthropic.com",
    "api.telegram.org",
    "oauth2.googleapis.com",
    "www.googleapis.com",
    "gmail.googleapis.com",
    "*.github.com",
    "*.githubusercontent.com",
]


class HTTPConnectProxy:
    """Asyncio HTTP CONNECT proxy server.

    Intercepts CONNECT tunnel requests, validates the target domain
    against the allowlist, and either establishes a TCP relay or
    returns 403 Forbidden.

    Usage:
        proxy = HTTPConnectProxy()
        await proxy.start()          # called in FastAPI lifespan
        ...
        await proxy.stop()           # called in FastAPI shutdown
    """

    def __init__(
        self,
        web_proxy: Optional[WebProxy] = None,
        host: str = "0.0.0.0",
        port: int = 8181,
    ):
        if web_proxy is None:
            config = WebProxyConfig(
                mode="allowlist",
                allowed_domains=ALLOWED_DOMAINS,
            )
            web_proxy = WebProxy(config=config)
        self.web_proxy = web_proxy
        self.host = host
        self.port = port
        self._server: Optional[asyncio.Server] = None
        self._stats: dict = {
            "total": 0,
            "allowed": 0,
            "blocked": 0,
            "recent": [],
        }

    async def start(self) -> None:
        """Start the CONNECT proxy server."""
        self._server = await asyncio.start_server(
            self._handle_client, self.host, self.port
        )
        logger.info(f"HTTP CONNECT proxy listening on {self.host}:{self.port}")

    async def stop(self) -> None:
        """Stop the CONNECT proxy server."""
        if self._server:
            self._server.close()
            await self._server.wait_closed()
            logger.info("HTTP CONNECT proxy stopped")

    def get_stats(self) -> dict:
        """Return proxy traffic statistics."""
        return {
            "total": self._stats["total"],
            "allowed": self._stats["allowed"],
            "blocked": self._stats["blocked"],
            "recent": list(self._stats["recent"][:20]),
        }

    async def _handle_client(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """Handle a single incoming client connection."""
        peer = writer.get_extra_info("peername")
        try:
            await self._process_connect(reader, writer)
        except asyncio.TimeoutError:
            logger.warning(f"CONNECT timeout from {peer}")
        except Exception as exc:
            logger.error(f"CONNECT error from {peer}: {exc}")
        finally:
            try:
                writer.close()
            except Exception:
                pass

    async def _process_connect(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """Parse CONNECT request, check allowlist, relay or block."""
        # Read request line
        try:
            request_line = await asyncio.wait_for(reader.readline(), timeout=10.0)
        except asyncio.TimeoutError:
            writer.write(b"HTTP/1.1 408 Request Timeout\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            return

        if not request_line:
            return

        line = request_line.decode("ascii", errors="replace").strip()
        parts = line.split()
        if len(parts) != 3:
            writer.write(b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            return

        method, target, _version = parts

        # Consume remaining headers (read until blank line)
        while True:
            try:
                header_line = await asyncio.wait_for(reader.readline(), timeout=10.0)
            except asyncio.TimeoutError:
                writer.write(
                    b"HTTP/1.1 408 Request Timeout\r\nContent-Length: 0\r\n\r\n"
                )
                await writer.drain()
                return
            if header_line in (b"\r\n", b"\n", b""):
                break

        if method.upper() != "CONNECT":
            writer.write(
                b"HTTP/1.1 405 Method Not Allowed\r\nContent-Length: 0\r\n\r\n"
            )
            await writer.drain()
            return

        # Parse host:port
        if ":" in target:
            host, port_str = target.rsplit(":", 1)
            try:
                port = int(port_str)
            except ValueError:
                writer.write(b"HTTP/1.1 400 Bad Request\r\nContent-Length: 0\r\n\r\n")
                await writer.drain()
                return
        else:
            host = target
            port = 443

        # Check domain against allowlist (via WebProxy)
        url = f"https://{host}:{port}/"
        result = self.web_proxy.check_request(url)

        # Track stats
        self._stats["total"] += 1
        entry = {
            "timestamp": time.time(),
            "host": host,
            "port": port,
            "allowed": not result.blocked,
            "block_reason": result.block_reason,
        }
        self._stats["recent"].insert(0, entry)
        if len(self._stats["recent"]) > 100:
            self._stats["recent"] = self._stats["recent"][:100]

        if result.blocked:
            self._stats["blocked"] += 1
            logger.warning(f"CONNECT blocked: {host}:{port} — {result.block_reason}")
            writer.write(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            return

        # Establish TCP tunnel to target
        try:
            target_reader, target_writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=10.0,
            )
        except (OSError, asyncio.TimeoutError) as exc:
            logger.error(f"CONNECT tunnel failed to {host}:{port}: {exc}")
            writer.write(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            return

        self._stats["allowed"] += 1
        logger.info(f"CONNECT tunnel established: {host}:{port}")
        writer.write(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        await writer.drain()

        # Relay bytes in both directions until one side closes
        await asyncio.gather(
            self._relay(reader, target_writer),
            self._relay(target_reader, writer),
            return_exceptions=True,
        )
        try:
            target_writer.close()
        except Exception:
            pass

    @staticmethod
    async def _relay(
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """Copy bytes from reader to writer until EOF."""
        try:
            while True:
                data = await reader.read(65536)
                if not data:
                    break
                writer.write(data)
                await writer.drain()
        except Exception:
            pass
        finally:
            try:
                writer.close()
            except Exception:
                pass
