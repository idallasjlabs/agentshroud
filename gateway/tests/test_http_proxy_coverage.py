# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for HTTPConnectProxy — server lifecycle, timeout paths,
tunnel retry/failure, keepalive socket options, byte relays, and ClamAV
download scanning.

Complements gateway/tests/test_http_proxy.py which covers allowlist /
egress-policy decision logic.  No real network egress: all connections are
either loopback-only or use monkeypatched asyncio.open_connection.
"""

from __future__ import annotations

import asyncio
import contextlib
import os
import socket
from types import SimpleNamespace
from unittest import mock

import gateway.proxy.http_proxy as http_proxy_module
from gateway.proxy.http_proxy import HTTPConnectProxy
from gateway.proxy.web_config import WebProxyConfig
from gateway.proxy.web_proxy import WebProxy

# ============================================================
# Helpers
# ============================================================


def _make_stream(data: bytes) -> asyncio.StreamReader:
    reader = asyncio.StreamReader()
    reader.feed_data(data)
    reader.feed_eof()
    return reader


class _MockWriter:
    """Minimal StreamWriter stand-in that records written bytes."""

    def __init__(self):
        self.written = b""
        self.closed = False

    def write(self, data: bytes) -> None:
        self.written += data

    async def drain(self) -> None:
        pass

    def close(self) -> None:
        self.closed = True

    def get_extra_info(self, key, default=None):
        if key == "peername":
            return ("127.0.0.1", 54321)
        return default


class _CloseRaisesWriter(_MockWriter):
    def close(self) -> None:
        self.closed = True
        raise RuntimeError("transport already closed")


class _TimeoutReader:
    """readline() always raises TimeoutError — simulates a stalled client."""

    async def readline(self) -> bytes:
        raise asyncio.TimeoutError


class _HeaderTimeoutReader:
    """First readline returns the request line; the next stalls."""

    def __init__(self, first_line: bytes):
        self._lines = [first_line]

    async def readline(self) -> bytes:
        if self._lines:
            return self._lines.pop(0)
        raise asyncio.TimeoutError


class _DummyTargetWriter:
    def __init__(self):
        self.closed = False

    def write(self, _data: bytes) -> None:
        pass

    async def drain(self) -> None:
        pass

    def close(self) -> None:
        self.closed = True


class _CloseRaisesTargetWriter(_DummyTargetWriter):
    def close(self) -> None:
        self.closed = True
        raise RuntimeError("already closed")


def _allowlist_proxy(domains=("api.openai.com",), **kwargs) -> HTTPConnectProxy:
    config = WebProxyConfig(mode="allowlist", allowed_domains=list(domains))
    return HTTPConnectProxy(web_proxy=WebProxy(config=config), **kwargs)


def _eof_target_connection():
    """asyncio.open_connection replacement returning an immediately-EOF stream."""

    async def _open_conn(_host, _port, **_kwargs):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    return _open_conn


# ============================================================
# start() / stop() — real loopback server lifecycle
# ============================================================


async def test_start_serves_and_stop_closes_loopback():
    """start() binds a real loopback server; a client gets a parsed response;
    stop() shuts the server down."""
    p = HTTPConnectProxy(host="127.0.0.1", port=0)
    await p.start()
    try:
        assert p._server is not None
        assert p._server.is_serving()
        port = p._server.sockets[0].getsockname()[1]

        reader, writer = await asyncio.open_connection("127.0.0.1", port)
        try:
            writer.write(b"NOTAREQUEST\r\n\r\n")
            await writer.drain()
            status_line = await asyncio.wait_for(reader.readline(), timeout=5.0)
            assert b"400" in status_line
        finally:
            writer.close()
            with contextlib.suppress(Exception):
                await writer.wait_closed()
    finally:
        await p.stop()
    assert not p._server.is_serving()


async def test_stop_without_start_is_noop():
    p = HTTPConnectProxy()
    # Must not raise when the server was never started.
    await p.stop()
    assert p._server is None


# ============================================================
# _handle_client — error containment
# ============================================================


async def test_handle_client_swallows_timeout_and_closes_writer():
    p = HTTPConnectProxy()

    async def _stall(_reader, _writer):
        raise asyncio.TimeoutError

    p._process_connect = _stall  # type: ignore[method-assign]
    writer = _MockWriter()
    await p._handle_client(asyncio.StreamReader(), writer)
    assert writer.closed is True


async def test_handle_client_swallows_generic_exception():
    p = HTTPConnectProxy()

    async def _boom(_reader, _writer):
        raise RuntimeError("unexpected")

    p._process_connect = _boom  # type: ignore[method-assign]
    writer = _MockWriter()
    await p._handle_client(asyncio.StreamReader(), writer)
    assert writer.closed is True


async def test_handle_client_tolerates_writer_close_failure():
    p = HTTPConnectProxy()

    async def _ok(_reader, _writer):
        return None

    p._process_connect = _ok  # type: ignore[method-assign]
    writer = _CloseRaisesWriter()
    # close() raising in the finally block must not propagate.
    await p._handle_client(asyncio.StreamReader(), writer)
    assert writer.closed is True


# ============================================================
# _process_connect — parse / timeout edge cases
# ============================================================


async def test_request_line_timeout_returns_408():
    p = HTTPConnectProxy()
    writer = _MockWriter()
    await p._process_connect(_TimeoutReader(), writer)
    assert b"408 Request Timeout" in writer.written


async def test_empty_request_line_returns_nothing():
    p = HTTPConnectProxy()
    reader = asyncio.StreamReader()
    reader.feed_eof()  # readline() -> b""
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert writer.written == b""
    assert p.get_stats()["total"] == 0


async def test_header_read_timeout_returns_408():
    p = HTTPConnectProxy()
    reader = _HeaderTimeoutReader(b"CONNECT api.openai.com:443 HTTP/1.1\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"408 Request Timeout" in writer.written


async def test_non_numeric_port_returns_400():
    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT evil.com:notaport HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"400 Bad Request" in writer.written


async def test_target_without_port_defaults_to_443():
    """Host-only CONNECT target defaults to port 443; blocked host -> 403."""
    p = _allowlist_proxy()
    reader = _make_stream(b"CONNECT not-allowed.example HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"403" in writer.written
    recent = p.get_stats()["recent"]
    assert recent[0]["host"] == "not-allowed.example"
    assert recent[0]["port"] == 443


# ============================================================
# System-bypass SOC logging edge cases
# ============================================================


async def test_bypass_logging_failure_does_not_block_tunnel(monkeypatch):
    """log_external_decision raising must not break the CONNECT."""

    class _RaisingQueue:
        def log_external_decision(self, **_kwargs):
            raise RuntimeError("soc store unavailable")

    egress = SimpleNamespace(_approval_queue=_RaisingQueue())
    monkeypatch.setattr(asyncio, "open_connection", _eof_target_connection())

    p = HTTPConnectProxy(egress_filter=egress)
    reader = _make_stream(b"CONNECT slack.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written
    assert p.get_stats()["allowed"] == 1


async def test_bypass_with_egress_filter_lacking_approval_queue(monkeypatch):
    """Egress filter without _approval_queue attr -> bypass proceeds silently."""
    monkeypatch.setattr(asyncio, "open_connection", _eof_target_connection())
    p = HTTPConnectProxy(egress_filter=SimpleNamespace())
    reader = _make_stream(b"CONNECT slack.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written


# ============================================================
# Stats — recent ring buffer trimming
# ============================================================


async def test_recent_stats_trimmed_to_100_entries():
    p = _allowlist_proxy()
    p._stats["recent"] = [{"host": f"old-{i}"} for i in range(100)]
    reader = _make_stream(b"CONNECT blocked.example:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert len(p._stats["recent"]) == 100
    assert p._stats["recent"][0]["host"] == "blocked.example"
    # get_stats only surfaces the 20 most recent
    assert len(p.get_stats()["recent"]) == 20


# ============================================================
# Tunnel establishment — retry and 502 paths
# ============================================================


async def test_tunnel_retries_then_succeeds(monkeypatch):
    """First open_connection attempt fails; retry (with patched sleep) succeeds."""
    attempts = {"n": 0}
    sleeps: list[float] = []

    async def _flaky_open(_host, _port, **_kwargs):
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise OSError("transient VPN blip")
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    async def _fake_sleep(delay):
        sleeps.append(delay)

    monkeypatch.setattr(asyncio, "open_connection", _flaky_open)
    monkeypatch.setattr("gateway.proxy.http_proxy.asyncio.sleep", _fake_sleep)

    p = HTTPConnectProxy()  # default allowlist includes api.openai.com
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)

    assert attempts["n"] == 2
    assert sleeps == [0.5]
    assert b"200 Connection Established" in writer.written
    assert p.get_stats()["allowed"] == 1


async def test_tunnel_connect_uses_happy_eyeballs(monkeypatch):
    """CONNECT tunnel establishment must race IPv4/IPv6 (RFC 8305) instead of
    trying one resolved address and failing outright.

    Real-world regression: on a host where IPv6 is dead but IPv4 works,
    hostnames with both AAAA and A records (api.anthropic.com, hc-ping.com)
    resolved to the IPv6 address, and a plain `asyncio.open_connection(host,
    port)` call — with no `family`/`happy_eyeballs_delay` — either wasted
    several seconds falling back to IPv4 sequentially, or under concurrent
    load exceeded the per-attempt 10s timeout outright, surfacing as
    'CONNECT tunnel failed ... after 3 attempts' and breaking every proxied
    HTTPS call (LLM completions, Healthchecks.io pings) until traced here.
    """
    seen_kwargs: dict = {}

    async def _capture_open(_host, _port, **kwargs):
        seen_kwargs.update(kwargs)
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _capture_open)

    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)

    assert "happy_eyeballs_delay" in seen_kwargs, (
        "asyncio.open_connection must be called with happy_eyeballs_delay so a "
        "dead address family (e.g. broken IPv6) doesn't waste the whole "
        "per-attempt timeout before falling back to a working one"
    )
    assert b"200 Connection Established" in writer.written


async def test_tunnel_connect_falls_back_when_happy_eyeballs_unsupported(monkeypatch):
    """Real-world regression (2026-07-29): uvloop (the active event loop under
    uvicorn in production — confirmed via uvicorn's default loop selection)
    does not implement happy_eyeballs_delay on create_connection(), unlike
    stock asyncio. Calling asyncio.open_connection(..., happy_eyeballs_delay=…)
    under uvloop raises TypeError immediately, on every single call, for
    every destination. TypeError is not one of the (OSError, TimeoutError)
    exceptions the retry loop catches, so it propagated out of the whole
    _process_connect call to _handle_client's generic exception handler —
    meaning every CONNECT failed instantly regardless of network state. A
    misbehaving client (observed live: OpenClaw) retried fast enough on each
    instant failure to spin this into an 800+ req/s busy-loop that pegged the
    gateway and OpenClaw containers before being traced here.

    This must never happen again: a TypeError from the happy-eyeballs kwarg
    must be caught, fall back to a plain open_connection() call, and the
    connection must still succeed.
    """
    monkeypatch.setattr(http_proxy_module, "HAS_HAPPY_EYEBALLS", True)
    calls: list[dict] = []

    async def _uvloop_like_open(_host, _port, **kwargs):
        calls.append(dict(kwargs))
        if "happy_eyeballs_delay" in kwargs:
            raise TypeError(
                "create_connection() got an unexpected keyword argument " "'happy_eyeballs_delay'"
            )
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _uvloop_like_open)

    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.anthropic.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)

    assert (
        b"200 Connection Established" in writer.written
    ), "the tunnel must still succeed via fallback, not fail outright"
    assert len(calls) == 2, "expected one failed happy-eyeballs attempt then one fallback"
    assert "happy_eyeballs_delay" in calls[0]
    assert "happy_eyeballs_delay" not in calls[1]
    assert http_proxy_module.HAS_HAPPY_EYEBALLS is False, (
        "detection must be cached so subsequent CONNECTs on this loop skip "
        "straight to the fallback instead of eating the same failure again"
    )

    # Second CONNECT on the same (now-detected-incompatible) loop must go
    # straight to the fallback — no repeated failed attempt.
    calls.clear()
    reader2 = _make_stream(b"CONNECT api.anthropic.com:443 HTTP/1.1\r\n\r\n")
    writer2 = _MockWriter()
    await p._process_connect(reader2, writer2)
    assert len(calls) == 1
    assert "happy_eyeballs_delay" not in calls[0]


async def test_tunnel_all_attempts_fail_returns_502(monkeypatch):
    attempts = {"n": 0}

    async def _always_fail(_host, _port, **_kwargs):
        attempts["n"] += 1
        raise OSError("connection refused")

    async def _fake_sleep(_delay):
        pass

    monkeypatch.setattr(asyncio, "open_connection", _always_fail)
    monkeypatch.setattr("gateway.proxy.http_proxy.asyncio.sleep", _fake_sleep)

    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)

    assert attempts["n"] == 3  # _MAX_CONNECT_ATTEMPTS
    assert b"502 Bad Gateway" in writer.written
    assert p.get_stats()["allowed"] == 0
    assert p.get_stats()["total"] == 1


async def test_tunnel_target_writer_close_failure_swallowed(monkeypatch):
    """target_writer.close() raising after relay completes must not propagate."""

    async def _open_conn(_host, _port, **_kwargs):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _CloseRaisesTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)
    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _MockWriter()
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written


# ============================================================
# TCP keepalive socket options on established tunnels
# ============================================================


class _SocketTransportWriter(_MockWriter):
    """Writer exposing a .transport whose socket records setsockopt calls."""

    def __init__(self, sock):
        super().__init__()
        self.transport = SimpleNamespace(get_extra_info=lambda _key: sock)


async def test_keepalive_set_on_both_tunnel_ends(monkeypatch):
    client_sock = mock.MagicMock()
    target_sock = mock.MagicMock()

    class _TargetWriterWithTransport(_DummyTargetWriter):
        transport = SimpleNamespace(get_extra_info=lambda _key: target_sock)

    async def _open_conn(_host, _port, **_kwargs):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _TargetWriterWithTransport()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)
    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _SocketTransportWriter(client_sock)
    await p._process_connect(reader, writer)

    assert b"200 Connection Established" in writer.written
    for sock_mock in (client_sock, target_sock):
        sock_mock.setsockopt.assert_any_call(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        if hasattr(socket, "TCP_KEEPIDLE"):
            sock_mock.setsockopt.assert_any_call(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)
        if hasattr(socket, "TCP_KEEPINTVL"):
            sock_mock.setsockopt.assert_any_call(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 15)
        if hasattr(socket, "TCP_KEEPCNT"):
            sock_mock.setsockopt.assert_any_call(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 6)


async def test_keepalive_socket_lookup_failure_is_swallowed(monkeypatch):
    """get_extra_info raising must not break the established tunnel."""

    def _raise(_key):
        raise RuntimeError("no socket on this transport")

    class _BrokenTransportWriter(_MockWriter):
        transport = SimpleNamespace(get_extra_info=_raise)

    monkeypatch.setattr(asyncio, "open_connection", _eof_target_connection())
    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _BrokenTransportWriter()
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written
    assert p.get_stats()["allowed"] == 1


async def test_keepalive_skipped_when_socket_is_none(monkeypatch):
    """Transport without an underlying socket (None) is skipped cleanly."""

    class _NoSocketWriter(_MockWriter):
        transport = SimpleNamespace(get_extra_info=lambda _key: None)

    monkeypatch.setattr(asyncio, "open_connection", _eof_target_connection())
    p = HTTPConnectProxy()
    reader = _make_stream(b"CONNECT api.openai.com:443 HTTP/1.1\r\n\r\n")
    writer = _NoSocketWriter()
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written


# ============================================================
# _relay — client→target byte pump
# ============================================================


async def test_relay_copies_bytes_until_eof():
    reader = asyncio.StreamReader()
    reader.feed_data(b"hello ")
    reader.feed_data(b"world")
    reader.feed_eof()
    writer = _MockWriter()
    await HTTPConnectProxy._relay(reader, writer)
    assert writer.written == b"hello world"
    assert writer.closed is True


async def test_relay_idle_timeout_closes_writer():
    class _StallReader:
        async def read(self, _n):
            raise asyncio.TimeoutError

    writer = _MockWriter()
    await HTTPConnectProxy._relay(_StallReader(), writer)
    assert writer.closed is True
    assert writer.written == b""


async def test_relay_swallows_read_errors():
    class _ErrorReader:
        async def read(self, _n):
            raise ConnectionResetError("peer reset")

    writer = _MockWriter()
    await HTTPConnectProxy._relay(_ErrorReader(), writer)
    assert writer.closed is True


async def test_relay_swallows_writer_close_failure():
    reader = asyncio.StreamReader()
    reader.feed_eof()
    writer = _CloseRaisesWriter()
    # close() raising in the finally block must not propagate.
    await HTTPConnectProxy._relay(reader, writer)
    assert writer.closed is True


# ============================================================
# _relay_and_scan — target→client byte pump with ClamAV sampling
# ============================================================


def _capture_scans(proxy: HTTPConnectProxy):
    scans: list[tuple[bytes, str]] = []

    async def _fake_scan(data: bytes, host: str) -> None:
        scans.append((data, host))

    proxy._clamav_scan_bytes = _fake_scan  # type: ignore[method-assign]
    return scans


async def test_relay_and_scan_small_download_scanned_at_eof():
    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    reader = asyncio.StreamReader()
    reader.feed_data(b"small payload")
    reader.feed_eof()
    writer = _MockWriter()
    await p._relay_and_scan(reader, writer, "dl.example")
    await asyncio.sleep(0)  # let the fire-and-forget scan task run
    assert writer.written == b"small payload"
    assert scans == [(b"small payload", "dl.example")]
    assert writer.closed is True


async def test_relay_and_scan_limit_reached_scans_once():
    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    reader = asyncio.StreamReader()
    reader.feed_data(b"0123456789")  # 10 bytes > scan_limit=4
    reader.feed_eof()
    writer = _MockWriter()
    await p._relay_and_scan(reader, writer, "dl.example", scan_limit=4)
    await asyncio.sleep(0)
    assert writer.written == b"0123456789"
    # Exactly one scan of the sampled prefix, not a second one at EOF.
    assert scans == [(b"0123456789", "dl.example")]


async def test_relay_and_scan_idle_timeout_no_data_no_scan():
    class _StallReader:
        async def read(self, _n):
            raise asyncio.TimeoutError

    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    writer = _MockWriter()
    await p._relay_and_scan(_StallReader(), writer, "dl.example")
    await asyncio.sleep(0)
    assert scans == []
    assert writer.closed is True


async def test_relay_and_scan_tls_tunnel_skips_ciphertext_scan():
    """Port-443 tunnel bytes are TLS ciphertext — clamscan can never match a
    signature on them, so scanning is pure waste.  Live incident 2026-07-04:
    ciphertext scans of routine LLM API tunnels each held a shared-executor
    thread 30-60 s (clamscan cold-loads its full DB) and spiked ~1.3 GB RAM,
    adding 35-60 s latency to every LLM proxy call and OOM-killing the
    gateway container.  TLS tunnels must relay without scanning."""
    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    reader = asyncio.StreamReader()
    reader.feed_data(b"\x17\x03\x03 encrypted application data")
    reader.feed_eof()
    writer = _MockWriter()
    await p._relay_and_scan(reader, writer, "api.anthropic.com", port=443)
    await asyncio.sleep(0)
    assert writer.written == b"\x17\x03\x03 encrypted application data"
    assert scans == [], "ciphertext from a TLS tunnel must not be ClamAV-scanned"
    assert writer.closed is True


async def test_relay_and_scan_plain_http_port_still_scans():
    """Port-80 downloads are plaintext — malware sampling must keep working."""
    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    reader = asyncio.StreamReader()
    reader.feed_data(b"MZ fake executable bytes")
    reader.feed_eof()
    writer = _MockWriter()
    await p._relay_and_scan(reader, writer, "mirror.example", port=80)
    await asyncio.sleep(0)
    assert scans == [(b"MZ fake executable bytes", "mirror.example")]


def test_clamav_scans_use_dedicated_single_thread_executor():
    """clamscan runs must never share the default executor with LLM upstream
    calls (thread starvation = 35-60 s added latency), and concurrency must be
    capped at 1 so at most one ~1.3 GB clamscan process exists at a time."""
    p = HTTPConnectProxy()
    assert getattr(p, "_clamav_executor", None) is not None, "dedicated ClamAV executor missing"
    assert p._clamav_executor._max_workers == 1


async def test_relay_and_scan_read_error_scans_partial_buffer():
    """Bytes relayed before a connection error are still sampled for scanning."""

    class _PartialThenErrorReader:
        def __init__(self):
            self._sent = False

        async def read(self, _n):
            if not self._sent:
                self._sent = True
                return b"partial"
            raise ConnectionResetError("peer reset")

    p = HTTPConnectProxy()
    scans = _capture_scans(p)
    writer = _MockWriter()
    await p._relay_and_scan(_PartialThenErrorReader(), writer, "dl.example")
    await asyncio.sleep(0)
    assert writer.written == b"partial"
    assert scans == [(b"partial", "dl.example")]


async def test_relay_and_scan_swallows_writer_close_failure():
    p = HTTPConnectProxy()
    _capture_scans(p)
    reader = asyncio.StreamReader()
    reader.feed_eof()
    writer = _CloseRaisesWriter()
    await p._relay_and_scan(reader, writer, "dl.example")
    assert writer.closed is True


# ============================================================
# _clamav_scan_bytes — malware sampling of downloads
# ============================================================


async def test_clamav_scan_infected_records_stats(monkeypatch):
    scanned_paths: list[str] = []

    def _fake_clamscan(target, recursive=True):
        assert recursive is False
        assert os.path.exists(target)  # temp file exists during the scan
        scanned_paths.append(target)
        return {
            "infected_count": 1,
            "infected_files": [{"signature": "Eicar-Test-Signature"}],
        }

    monkeypatch.setattr("gateway.security.clamav_scanner.run_clamscan", _fake_clamscan)
    p = HTTPConnectProxy()
    await p._clamav_scan_bytes(b"X5O!P%@AP", "malware.example")

    infections = p._stats["clamav_infections"]
    assert len(infections) == 1
    assert infections[0]["host"] == "malware.example"
    assert infections[0]["signatures"] == ["Eicar-Test-Signature"]
    # Temp file is removed after the scan.
    assert not os.path.exists(scanned_paths[0])


async def test_clamav_scan_clean_records_nothing(monkeypatch):
    scanned_paths: list[str] = []

    def _fake_clamscan(target, recursive=True):
        scanned_paths.append(target)
        return {"infected_count": 0, "infected_files": []}

    monkeypatch.setattr("gateway.security.clamav_scanner.run_clamscan", _fake_clamscan)
    p = HTTPConnectProxy()
    await p._clamav_scan_bytes(b"clean bytes", "ok.example")

    assert "clamav_infections" not in p._stats
    assert not os.path.exists(scanned_paths[0])


async def test_clamav_scan_unavailable_degrades_silently(monkeypatch):
    """clamscan binary missing (sidecar down) -> no exception, temp file removed."""
    captured: dict[str, str] = {}

    def _fake_clamscan(target, recursive=True):
        captured["path"] = target
        raise FileNotFoundError("clamscan not found")

    monkeypatch.setattr("gateway.security.clamav_scanner.run_clamscan", _fake_clamscan)
    p = HTTPConnectProxy()
    await p._clamav_scan_bytes(b"whatever", "host.example")

    assert "clamav_infections" not in p._stats
    assert not os.path.exists(captured["path"])


async def test_clamav_scan_unlink_failure_swallowed(monkeypatch):
    captured: dict[str, str] = {}

    def _fake_clamscan(target, recursive=True):
        captured["path"] = target
        return {"infected_count": 0, "infected_files": []}

    monkeypatch.setattr("gateway.security.clamav_scanner.run_clamscan", _fake_clamscan)
    p = HTTPConnectProxy()
    with mock.patch("gateway.proxy.http_proxy.os.unlink", side_effect=OSError("file busy")):
        # Must not raise even though cleanup fails.
        await p._clamav_scan_bytes(b"data", "host.example")

    # The temp file survives the failed unlink; clean it up here.
    assert os.path.exists(captured["path"])
    os.unlink(captured["path"])
