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
import socket
import time
from typing import Optional

from .web_config import WebProxyConfig
from .web_proxy import WebProxy
from ..security.egress_filter import EgressAction, EgressFilter

logger = logging.getLogger("agentshroud.proxy.http_proxy")

# Default allowlist: only the domains the bot legitimately needs
ALLOWED_DOMAINS: list[str] = [
    "api.openai.com",
    "api.anthropic.com",
    "oauth2.googleapis.com",
    "www.googleapis.com",
    "gmail.googleapis.com",
    "*.github.com",
    "*.githubusercontent.com",
    # Slack Socket Mode WebSocket endpoint (OpenClaw native Slack channel)
    "wss-primary.slack.com",
    "wss-backup.slack.com",
    "slack.com",
    "*.slack.com",
]

# Internal control-plane destinations required for channel transport.
# These are bypassed from interactive egress approval to avoid deadlocking
# the approval channel itself.
# NOTE: api.telegram.org is intentionally NOT listed here.  The bot is
# configured with TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
# and NO_PROXY=gateway, so all Telegram API calls must go through the
# gateway's /telegram-api/ proxy (where the Slack bridge intercept lives).
# Allowing direct CONNECT tunnels to api.telegram.org bypasses the bridge
# and causes sendMessage responses to disappear silently.
SYSTEM_BYPASS_DOMAINS: set[str] = {
    # Slack: required for OpenClaw's native Slack channel (Socket Mode WebSocket +
    # Web API REST calls).  Must bypass interactive egress approval to avoid the
    # approval channel itself depending on Slack being reachable.
    "slack.com",
    "wss-primary.slack.com",
    "wss-backup.slack.com",
    "edgeapi.slack.com",
}

# Domains that are unconditionally BLOCKED from direct CONNECT tunnels,
# even if the egress filter policy would otherwise allow them.
# The bot MUST use its configured base URL (e.g. TELEGRAM_API_BASE_URL)
# to reach these hosts through the gateway proxy, not via a raw tunnel.
CONNECT_FORCE_BLOCK_DOMAINS: set[str] = {
    "api.telegram.org",
}


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
        egress_filter: Optional[EgressFilter] = None,
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
        self.egress_filter = egress_filter
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

        bypass_system_domain = host.lower().rstrip(".") in SYSTEM_BYPASS_DOMAINS
        force_blocked_domain = host.lower().rstrip(".") in CONNECT_FORCE_BLOCK_DOMAINS

        url = f"https://{host}:{port}/"
        result_blocked = False
        block_reason = "allowed"

        if force_blocked_domain:
            # Hard block — takes priority over egress filter and system bypass.
            # Bot must use its configured gateway base URL (e.g. TELEGRAM_API_BASE_URL)
            # rather than a direct CONNECT tunnel.
            result_blocked = True
            block_reason = f"direct CONNECT tunnel to {host} is blocked; use gateway proxy"
        elif bypass_system_domain:
            block_reason = "system egress bypass domain"
        elif self.egress_filter is not None:
            # Primary policy path: interactive egress approval + policy engine.
            # This is required so unknown domains can raise approval prompts
            # instead of being hard-blocked by static CONNECT allowlists.
            egress_attempt = await self.egress_filter.check_async(
                agent_id="http_connect_proxy",
                destination=url,
                port=port,
                tool_name="http_connect_tunnel",
            )
            if egress_attempt.action != EgressAction.ALLOW:
                result_blocked = True
                block_reason = (
                    egress_attempt.details
                    or egress_attempt.rule
                    or "egress denied"
                )
            else:
                # Keep static allowlist as observability signal when interactive
                # approval/policy allows an otherwise unknown domain.
                web_result = self.web_proxy.check_request(url)
                if web_result.blocked:
                    logger.info(
                        "CONNECT allowed by egress policy despite static allowlist miss: %s:%s",
                        host,
                        port,
                    )
                block_reason = (
                    egress_attempt.details
                    or egress_attempt.rule
                    or "egress allowed"
                )
        else:
            # Fallback path when egress filter is unavailable.
            result = self.web_proxy.check_request(url)
            result_blocked = result.blocked
            block_reason = result.block_reason

        # Track stats
        self._stats["total"] += 1
        entry = {
            "timestamp": time.time(),
            "host": host,
            "port": port,
            "allowed": not result_blocked,
            "block_reason": block_reason,
        }
        self._stats["recent"].insert(0, entry)
        if len(self._stats["recent"]) > 100:
            self._stats["recent"] = self._stats["recent"][:100]

        if result_blocked:
            self._stats["blocked"] += 1
            logger.warning(f"CONNECT blocked: {host}:{port} — {block_reason}")
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

        # Enable TCP keepalive on both ends of the tunnel so the OS sends
        # keepalive probes on idle connections. Without this, Cisco AnyConnect
        # (and similar VPNs) silently drop idle TCP sessions after ~10 minutes,
        # causing WebSocket ping/pong timeouts (e.g. Slack Socket Mode).
        for _transport in (
            getattr(writer, "transport", None),
            getattr(target_writer, "transport", None),
        ):
            if _transport is None:
                continue
            try:
                _sock = _transport.get_extra_info("socket")
                if _sock is not None:
                    _sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                    # Start probes after 60s idle, then every 15s, drop after 6 missed.
                    if hasattr(socket, "TCP_KEEPIDLE"):
                        _sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
                    if hasattr(socket, "TCP_KEEPINTVL"):
                        _sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 15)
                    if hasattr(socket, "TCP_KEEPCNT"):
                        _sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 6)
            except Exception:
                pass

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
