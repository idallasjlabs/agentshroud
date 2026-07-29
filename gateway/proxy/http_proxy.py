# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
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
import concurrent.futures
import ipaddress
import logging
import os
import socket
import tempfile
import time
from typing import Optional

from ..security.egress_config import PERMANENT_EGRESS_DOMAINS
from ..security.egress_filter import EgressAction, EgressFilter
from .web_config import WebProxyConfig
from .web_proxy import WebProxy

logger = logging.getLogger("agentshroud.proxy.http_proxy")

# Whether the active event loop's create_connection() accepts
# happy_eyeballs_delay. uvicorn defaults to uvloop when installed (it is, in
# this image) and uvloop 0.22.1's create_connection() does not implement this
# kwarg, unlike stock asyncio — raises TypeError on every single call. Starts
# True (optimistic) and is set False permanently on first TypeError, so a
# uvloop deployment pays the cost of detecting this exactly once instead of
# on every CONNECT for the container's lifetime. See the retry loop below for
# why an uncaught TypeError here is far worse than a plain missing feature —
# it turned into an 800+ req/s busy-loop with a misbehaving client (2026-07-29).
HAS_HAPPY_EYEBALLS = True

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
    # GitHub API: required for competitive intelligence, CVE triage, and extension
    # update checks.  Blocking this triggers approval prompts for routine cron jobs.
    "api.github.com",
}

# Domains that are unconditionally BLOCKED from direct CONNECT tunnels,
# even if the egress filter policy would otherwise allow them.
# The bot MUST use its configured base URL (e.g. TELEGRAM_API_BASE_URL)
# to reach these hosts through the gateway proxy, not via a raw tunnel.
CONNECT_FORCE_BLOCK_DOMAINS: set[str] = {
    "api.telegram.org",
}

# Default internet allowlist — derived from the canonical PERMANENT_EGRESS_DOMAINS registry.
# Internal Docker/SSH targets (host.docker.internal, marvin, trillian, raspberrypi) are
# declared in agentshroud.yaml proxy.allowed_domains and merged at startup in lifespan.py.
#
# CONNECT_FORCE_BLOCK_DOMAINS entries are excluded (defense-in-depth): api.telegram.org
# must not appear here so the bot is always routed through the gateway's /telegram-api/
# reverse proxy (where the Slack bridge intercept lives).
ALLOWED_DOMAINS: list[str] = [
    d for d in PERMANENT_EGRESS_DOMAINS if d not in CONNECT_FORCE_BLOCK_DOMAINS
]


class HTTPConnectProxy:
    """Asyncio HTTP CONNECT proxy server.

    Intercepts CONNECT tunnel requests, validates the target domain
    against the allowlist, and either establishes a TCP relay or
    returns 403 Forbidden.

    **Enforcement posture — allowlist-only:**
    This proxy operates exclusively in allowlist mode: destinations that are
    not explicitly permitted (via ``ALLOWED_DOMAINS`` / ``agentshroud.yaml``
    ``proxy.allowed_domains``) are blocked by default.  There is no fallback
    "allow unknown" path.  ``CONNECT_FORCE_BLOCK_DOMAINS`` (e.g.
    ``api.telegram.org``) adds a hard-block layer that cannot be overridden by
    the runtime egress-approval queue — the bot *must* use the gateway's
    ``/telegram-api/`` reverse proxy for those destinations.

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
        ip_to_bot_registry: Optional[dict] = None,
        bot_hostnames: Optional[dict] = None,
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
        # Mapping of source-IP string → bot_id (e.g. "172.21.0.3" → "hermes").
        # Populated at startup for any bot resolvable then; lazily extended via
        # reverse-DNS for bots that start after the gateway (e.g. Hermes).
        self._ip_to_bot_registry: dict = ip_to_bot_registry or {}
        # bot_id → Docker service hostname, used for lazy reverse-DNS attribution.
        self._bot_hostnames: dict = bot_hostnames or {}
        self._server: Optional[asyncio.Server] = None
        # Dedicated single-thread executor for clamscan runs.  NEVER share the
        # default executor with LLM upstream calls: each clamscan holds a
        # thread 30-60 s (full DB cold-load) — on the shared pool this starved
        # LLM forwards by 35-60 s per request (live incident 2026-07-04).
        # max_workers=1 also caps concurrency so at most one ~1.3 GB clamscan
        # process exists at a time (their overlap OOM-killed the container).
        self._clamav_executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="clamav-scan"
        )
        self._stats: dict = {
            "total": 0,
            "allowed": 0,
            "blocked": 0,
            "recent": [],
        }

    async def start(self) -> None:
        """Start the CONNECT proxy server."""
        self._server = await asyncio.start_server(self._handle_client, self.host, self.port)
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

    def _agent_id_for_peer(self, peer) -> str:
        """Resolve source IP to a bot_id; lazily extends registry via DNS.

        The startup registry may be empty for bots that start after the gateway
        (e.g. Hermes).  On first CONNECT from an unknown IP, two lookups are tried:
         1. Reverse-DNS (PTR): gethostbyaddr — fast but Docker's embedded DNS may
            not serve PTR records, so this frequently fails for container IPs.
         2. Forward-DNS (A): getaddrinfo for each known bot hostname — more
            reliable in Docker networks where only A records are guaranteed.
        Cache both hits and misses so DNS is queried at most once per source IP.
        """
        if not peer:
            return "http_connect_proxy"
        ip = peer[0] if isinstance(peer, (tuple, list)) else str(peer)
        if ip in self._ip_to_bot_registry:
            return self._ip_to_bot_registry[ip]
        if self._bot_hostnames:
            # --- Attempt 1: reverse DNS (PTR record) ---
            try:
                rdns_host = socket.gethostbyaddr(ip)[0]
                for bot_id, bot_host in self._bot_hostnames.items():
                    if rdns_host == bot_host or rdns_host.startswith(bot_host + "."):
                        self._ip_to_bot_registry[ip] = bot_id
                        logger.debug(
                            "IP→bot registry (lazy rDNS): %s → %s (hostname=%s)",
                            ip,
                            bot_id,
                            rdns_host,
                        )
                        return bot_id
            except Exception:
                pass
            # --- Attempt 2: forward DNS (A record) ---
            # Docker's embedded DNS reliably serves A records but may not serve PTR.
            # Resolve each known bot hostname and compare to the source IP.
            for bot_id, bot_host in self._bot_hostnames.items():
                try:
                    for info in socket.getaddrinfo(bot_host, None):
                        if info[4][0] == ip:
                            self._ip_to_bot_registry[ip] = bot_id
                            logger.debug(
                                "IP→bot registry (lazy fDNS): %s → %s (hostname=%s)",
                                ip,
                                bot_id,
                                bot_host,
                            )
                            return bot_id
                except Exception:
                    pass
        self._ip_to_bot_registry[ip] = "http_connect_proxy"
        return "http_connect_proxy"

    async def _process_connect(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        """Parse CONNECT request, check allowlist, relay or block."""
        # Identify which bot is making this request from its source IP.
        peer = writer.get_extra_info("peername")
        agent_id = self._agent_id_for_peer(peer)
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
                writer.write(b"HTTP/1.1 408 Request Timeout\r\nContent-Length: 0\r\n\r\n")
                await writer.drain()
                return
            if header_line in (b"\r\n", b"\n", b""):
                break

        if method.upper() != "CONNECT":
            writer.write(b"HTTP/1.1 405 Method Not Allowed\r\nContent-Length: 0\r\n\r\n")
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

        # Bare-IP-literal CONNECT targets (e.g. 1.1.1.1, 8.8.8.8) have no domain to
        # match against SYSTEM_BYPASS_DOMAINS/CONNECT_FORCE_BLOCK_DOMAINS/allowlist,
        # so they fall through to the interactive egress-approval path below and can
        # hang for its full prompt-wait window before auto-denying — observed
        # 2026-07-18 hanging a Hermes boot (DNS-over-HTTPS fallback-IP discovery
        # probing raw resolver IPs) for ~8s+ per target, compounding across several
        # probed IPs into a container-killing delay. A well-behaved agent has no
        # legitimate reason to CONNECT to a bare IP without going through DNS, so
        # deny immediately instead of queuing an approval prompt nobody can usefully
        # answer for a raw IP.
        try:
            ipaddress.ip_address(host)
            is_ip_literal = True
        except ValueError:
            is_ip_literal = False

        if force_blocked_domain:
            # Hard block — takes priority over egress filter and system bypass.
            # Bot must use its configured gateway base URL (e.g. TELEGRAM_API_BASE_URL)
            # rather than a direct CONNECT tunnel.
            result_blocked = True
            block_reason = f"direct CONNECT tunnel to {host} is blocked; use gateway proxy"
        elif is_ip_literal and not bypass_system_domain:
            result_blocked = True
            block_reason = f"direct CONNECT to bare IP {host} is blocked; use a hostname"
        elif bypass_system_domain:
            block_reason = "system egress bypass domain"
            # Log bypass-domain connections to the SOC decision history so that
            # outbound web_search / web_fetch calls to pre-approved domains
            # (e.g. api.search.brave.com) are visible in the SOC Egress tab.
            if self.egress_filter is not None:
                _aq = getattr(self.egress_filter, "_approval_queue", None)
                if _aq is not None and hasattr(_aq, "log_external_decision"):
                    try:
                        _aq.log_external_decision(
                            domain=host,
                            decision="allow",
                            agent_id=agent_id,
                            reason="system egress bypass domain",
                        )
                    except Exception:
                        pass
        elif self.egress_filter is not None:
            # Primary policy path: interactive egress approval + policy engine.
            # This is required so unknown domains can raise approval prompts
            # instead of being hard-blocked by static CONNECT allowlists.
            egress_attempt = await self.egress_filter.check_async(
                agent_id=agent_id,
                destination=url,
                port=port,
                tool_name="http_connect_tunnel",
            )
            if egress_attempt.action != EgressAction.ALLOW:
                result_blocked = True
                block_reason = egress_attempt.details or egress_attempt.rule or "egress denied"
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
                block_reason = egress_attempt.details or egress_attempt.rule or "egress allowed"
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
            # Known force-blocked domains (e.g. api.telegram.org) are expected — log at DEBUG
            # to avoid noise in docker logs. Unknown hosts are genuine security signals → WARNING.
            if host.lower().rstrip(".") in CONNECT_FORCE_BLOCK_DOMAINS:
                logger.debug(f"CONNECT blocked (expected): {host}:{port} — {block_reason}")
            else:
                logger.warning(f"CONNECT blocked: {host}:{port} — {block_reason}")
            writer.write(b"HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            return

        # Establish TCP tunnel to target.
        # Retry up to 3 times with brief backoff to handle transient network
        # hiccups (VPN reconnect, Colima networking blip) without immediately
        # returning 502 — which crashes OpenClaw's unhandled Bolt error path.
        #
        # happy_eyeballs_delay (RFC 8305): without it, a hostname resolving to
        # both an AAAA and A record ties this connection to whichever address
        # getaddrinfo() returns first — if that family is dead (confirmed on
        # marvin: IPv6 to api.anthropic.com/hc-ping.com fails outright, IPv4
        # works), every attempt eats several seconds before failing outright,
        # instead of racing both and using whichever answers. Under concurrent
        # load this pushed real attempts past the 10s per-attempt timeout,
        # surfacing as "CONNECT tunnel failed ... after 3 attempts" and
        # breaking every proxied HTTPS call — LLM completions, Healthchecks.io
        # pings — until traced back here.
        _MAX_CONNECT_ATTEMPTS = 3
        _CONNECT_RETRY_DELAYS = [0.5, 1.5]  # seconds between attempts
        target_reader = target_writer = None
        _last_exc: Exception = OSError("no attempts made")
        for _attempt in range(_MAX_CONNECT_ATTEMPTS):
            if _attempt > 0:
                _delay = _CONNECT_RETRY_DELAYS[min(_attempt - 1, len(_CONNECT_RETRY_DELAYS) - 1)]
                logger.warning(
                    f"CONNECT tunnel retry {_attempt}/{_MAX_CONNECT_ATTEMPTS - 1} "
                    f"to {host}:{port} in {_delay}s (last error: {_last_exc})"
                )
                await asyncio.sleep(_delay)
            try:
                global HAS_HAPPY_EYEBALLS
                try:
                    if HAS_HAPPY_EYEBALLS:
                        target_reader, target_writer = await asyncio.wait_for(
                            asyncio.open_connection(host, port, happy_eyeballs_delay=0.25),
                            timeout=10.0,
                        )
                    else:
                        raise TypeError  # short-circuit straight to the fallback below
                except TypeError:
                    # See the module-level HAS_HAPPY_EYEBALLS comment for why this
                    # branch exists and why it must never be allowed to propagate
                    # uncaught (2026-07-29: an 800+ req/s busy-loop).
                    HAS_HAPPY_EYEBALLS = False
                    target_reader, target_writer = await asyncio.wait_for(
                        asyncio.open_connection(host, port),
                        timeout=10.0,
                    )
                break  # success
            except (OSError, asyncio.TimeoutError) as exc:
                _last_exc = exc

        if target_reader is None:
            logger.error(
                f"CONNECT tunnel failed to {host}:{port} after {_MAX_CONNECT_ATTEMPTS} attempts: {_last_exc}"
            )
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

        # Relay bytes in both directions until one side closes.
        # Inbound (client→target): plain relay — client data is already
        # validated by ingest_api before reaching the proxy.
        # Outbound (target→client): relay with ClamAV sampling so that
        # downloaded file data is scanned for malware signatures.
        await asyncio.gather(
            self._relay(reader, target_writer),
            self._relay_and_scan(target_reader, writer, host, port=port),
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
        idle_timeout: float = 120.0,
    ) -> None:
        """Copy bytes from reader to writer until EOF.

        ``idle_timeout`` (default 120 s) closes the tunnel if no data
        arrives for that long.  This prevents stale SSH/TLS connections
        from hanging the proxy indefinitely when the remote peer stops
        sending without closing the TCP connection.
        """
        try:
            while True:
                data = await asyncio.wait_for(reader.read(65536), timeout=idle_timeout)
                if not data:
                    break
                writer.write(data)
                await writer.drain()
        except asyncio.TimeoutError:
            logger.debug("_relay: idle timeout (%.0fs) — closing tunnel", idle_timeout)
        except Exception:
            pass
        finally:
            try:
                writer.close()
            except Exception:
                pass

    async def _relay_and_scan(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
        host: str,
        scan_limit: int = 4 * 1024 * 1024,
        port: int = 0,
    ) -> None:
        """Copy bytes from reader to writer, sampling the first scan_limit bytes
        for ClamAV malware scanning (non-blocking, fire-and-forget).

        Catches malware in non-TLS (port 80) downloads.  Port-443 tunnels are
        NOT scanned: the sampled bytes are TLS ciphertext, so clamscan can
        never match a signature — every scan is pure waste.  Live incident
        2026-07-04: ciphertext scans of routine LLM API tunnels each held a
        shared-executor thread 30-60 s (clamscan cold-loads its whole DB) and
        spiked ~1.3 GB RAM, adding 35-60 s to every LLM proxy call and
        OOM-killing the gateway container.
        """
        if port == 443:
            await self._relay(reader, writer)
            return
        buf = bytearray()
        scanned = False
        idle_timeout = 120.0
        try:
            while True:
                data = await asyncio.wait_for(reader.read(65536), timeout=idle_timeout)
                if not data:
                    break
                writer.write(data)
                await writer.drain()
                if not scanned and len(buf) < scan_limit:
                    buf.extend(data)
                    if len(buf) >= scan_limit:
                        asyncio.create_task(self._clamav_scan_bytes(bytes(buf), host))
                        scanned = True
        except asyncio.TimeoutError:
            logger.debug("_relay_and_scan: idle timeout (%.0fs) — closing tunnel", idle_timeout)
        except Exception:
            pass
        finally:
            if not scanned and buf:
                asyncio.create_task(self._clamav_scan_bytes(bytes(buf), host))
            try:
                writer.close()
            except Exception:
                pass

    async def _clamav_scan_bytes(self, data: bytes, host: str) -> None:
        """Write data to a temp file and scan with ClamAV.

        Runs in a thread executor so it does not block the event loop.
        Logs CRITICAL if malware signatures are detected; logs DEBUG otherwise.
        Silently degrades if clamscan binary is unavailable (sidecar not running).
        """
        tmp_path: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as f:
                f.write(data)
                tmp_path = f.name

            from ..security.clamav_scanner import run_clamscan

            result = await asyncio.get_event_loop().run_in_executor(
                self._clamav_executor,
                lambda: run_clamscan(tmp_path, recursive=False),
            )
            infected = result.get("infected_count", 0)
            if infected > 0:
                sigs = [f.get("signature", "?") for f in result.get("infected_files", [])]
                logger.critical(
                    "ClamAV MALWARE DETECTED in download from %s: %s",
                    host,
                    sigs,
                )
                self._stats.setdefault("clamav_infections", []).append(
                    {"host": host, "signatures": sigs, "timestamp": time.time()}
                )
            else:
                logger.debug("ClamAV scan clean for download from %s", host)
        except Exception as exc:
            logger.debug("ClamAV scan unavailable (sidecar may not be running): %s", exc)
        finally:
            if tmp_path:
                try:
                    os.unlink(tmp_path)
                except Exception:
                    pass
