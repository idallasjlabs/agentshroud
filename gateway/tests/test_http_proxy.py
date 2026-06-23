# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for HTTPConnectProxy — CONNECT tunnel server on port 8181."""

from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest

from gateway.proxy.http_proxy import (
    ALLOWED_DOMAINS,
    SYSTEM_BYPASS_DOMAINS,
    HTTPConnectProxy,
)
from gateway.proxy.web_config import WebProxyConfig
from gateway.proxy.web_proxy import WebProxy
from gateway.security.egress_filter import EgressAction

# ============================================================
# Default config
# ============================================================


def test_default_allowed_domains_non_empty():
    """HTTPConnectProxy ships with a populated default allowlist."""
    assert len(ALLOWED_DOMAINS) > 0
    assert "api.openai.com" in ALLOWED_DOMAINS
    assert "api.anthropic.com" in ALLOWED_DOMAINS


def test_proxy_created_with_default_web_proxy():
    p = HTTPConnectProxy()
    assert p.web_proxy is not None
    assert p.web_proxy.config.mode == "allowlist"


def test_proxy_created_with_custom_web_proxy():
    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    wp = WebProxy(config=config)
    p = HTTPConnectProxy(web_proxy=wp, port=9999)
    assert p.port == 9999
    assert p.web_proxy is wp


def test_proxy_created_with_egress_filter():
    ef = object()
    p = HTTPConnectProxy(egress_filter=ef)
    assert p.egress_filter is ef


# ============================================================
# Stats
# ============================================================


def test_initial_stats_are_zero():
    p = HTTPConnectProxy()
    s = p.get_stats()
    assert s["total"] == 0
    assert s["allowed"] == 0
    assert s["blocked"] == 0
    assert s["recent"] == []


def test_stats_structure():
    p = HTTPConnectProxy()
    s = p.get_stats()
    assert set(s.keys()) >= {"total", "allowed", "blocked", "recent"}


# ============================================================
# CONNECT request parsing (via asyncio streams)
# ============================================================


def _make_stream(data: bytes):
    """Create a StreamReader loaded with data and a mock StreamWriter."""
    reader = asyncio.StreamReader()
    reader.feed_data(data)
    reader.feed_eof()
    return reader


class _MockWriter:
    """Minimal asyncio.StreamWriter mock that captures written bytes."""

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
            return ("127.0.0.1", 12345)
        return default


class _DummyTargetWriter:
    def write(self, _data: bytes) -> None:
        pass

    async def drain(self) -> None:
        pass

    def close(self) -> None:
        pass


@pytest.mark.asyncio
async def test_connect_blocked_domain_returns_403():
    config = WebProxyConfig(
        mode="allowlist",
        allowed_domains=["api.openai.com"],
    )
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config))

    connect_req = b"CONNECT evil.com:443 HTTP/1.1\r\nHost: evil.com\r\n\r\n"
    reader = _make_stream(connect_req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"403" in writer.written
    assert p.get_stats()["total"] == 1
    assert p.get_stats()["blocked"] == 1
    assert p.get_stats()["allowed"] == 0


@pytest.mark.asyncio
async def test_non_connect_method_returns_405():
    p = HTTPConnectProxy()
    get_req = b"GET http://example.com/ HTTP/1.1\r\nHost: example.com\r\n\r\n"
    reader = _make_stream(get_req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"405" in writer.written


@pytest.mark.asyncio
async def test_malformed_request_line_returns_400():
    p = HTTPConnectProxy()
    bad_req = b"BADREQUEST\r\n\r\n"
    reader = _make_stream(bad_req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"400" in writer.written


@pytest.mark.asyncio
async def test_ssrf_attempt_returns_403():
    """CONNECT to a private IP is blocked by SSRF protection."""
    p = HTTPConnectProxy()
    req = b"CONNECT 127.0.0.1:8080 HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"403" in writer.written


@pytest.mark.asyncio
async def test_blocked_domain_is_tracked_in_recent():
    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config))

    req = b"CONNECT attacker.com:443 HTTP/1.1\r\nHost: attacker.com\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    recent = p.get_stats()["recent"]
    assert len(recent) == 1
    assert recent[0]["host"] == "attacker.com"
    assert recent[0]["allowed"] is False


@pytest.mark.asyncio
async def test_connect_denied_by_egress_filter_returns_403():
    class _DenyEgress:
        async def check_async(self, *args, **kwargs):
            return SimpleNamespace(
                action=EgressAction.DENY,
                details="interactive egress approval denied",
                rule="deny",
            )

    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config), egress_filter=_DenyEgress())
    req = b"CONNECT api.openai.com:443 HTTP/1.1\r\nHost: api.openai.com\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"403" in writer.written
    assert p.get_stats()["blocked"] == 1


@pytest.mark.asyncio
async def test_connect_system_bypass_domain_skips_policy_checks(monkeypatch):
    class _DenyEgress:
        called = False

        async def check_async(self, *args, **kwargs):
            self.called = True
            return SimpleNamespace(
                action=EgressAction.DENY,
                details="denied",
                rule="deny",
            )

    async def _open_conn(_host, _port):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)

    # api.telegram.org is force-blocked (CONNECT_FORCE_BLOCK_DOMAINS) to prevent
    # the bot from bypassing the /telegram-api/ proxy path. Verify the CONNECT
    # is rejected even when the system would normally skip egress policy for bypasses.
    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    egress = _DenyEgress()
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config), egress_filter=egress)
    req = b"CONNECT api.telegram.org:443 HTTP/1.1\r\nHost: api.telegram.org\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"403" in writer.written
    assert egress.called is False  # blocked before egress policy is consulted


@pytest.mark.asyncio
async def test_connect_unknown_domain_can_be_allowed_by_interactive_egress(monkeypatch):
    class _AllowEgress:
        called = False

        async def check_async(self, *args, **kwargs):
            self.called = True
            return SimpleNamespace(
                action=EgressAction.ALLOW,
                details="interactive egress approval granted",
                rule="allow",
            )

    async def _open_conn(_host, _port):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)

    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    egress = _AllowEgress()
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config), egress_filter=egress)
    req = b"CONNECT weather.com:443 HTTP/1.1\r\nHost: weather.com\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"200 Connection Established" in writer.written
    assert egress.called is True
    assert p.get_stats()["allowed"] == 1


def test_telegram_api_blocked_in_connect_proxy():
    """CONNECT tunnel must NOT allow api.telegram.org — forces traffic through reverse proxy for RBAC."""
    from gateway.proxy.http_proxy import ALLOWED_DOMAINS

    assert (
        "api.telegram.org" not in ALLOWED_DOMAINS
    ), "api.telegram.org must not be in CONNECT allowlist"

    # Also verify via WebProxy check
    from gateway.proxy.web_config import WebProxyConfig
    from gateway.proxy.web_proxy import WebProxy

    config = WebProxyConfig(mode="allowlist", allowed_domains=ALLOWED_DOMAINS)
    proxy = WebProxy(config=config)
    result = proxy.check_request("https://api.telegram.org/bot123/sendMessage")
    assert result.blocked, "api.telegram.org must be blocked in CONNECT proxy"


def test_telegram_is_force_blocked_not_bypass():
    """api.telegram.org must NOT be a system bypass domain.

    Direct CONNECT tunnels to Telegram are blocked so all bot traffic is
    routed through the /telegram-api/ proxy path.  See CONNECT_FORCE_BLOCK_DOMAINS
    in http_proxy.py.
    """
    from gateway.proxy.http_proxy import CONNECT_FORCE_BLOCK_DOMAINS

    assert "api.telegram.org" not in SYSTEM_BYPASS_DOMAINS
    assert "api.telegram.org" in CONNECT_FORCE_BLOCK_DOMAINS


@pytest.mark.asyncio
async def test_system_bypass_domain_logs_external_decision(monkeypatch):
    """System bypass domains should be logged to the SOC decision history."""
    log_calls = []

    class _MockApprovalQueue:
        def log_external_decision(self, **kwargs):
            log_calls.append(kwargs)

    class _MockEgressFilter:
        _approval_queue = _MockApprovalQueue()

    async def _open_conn(_host, _port):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)

    # Use a real SYSTEM_BYPASS_DOMAINS member (not api.telegram.org which is force-blocked)
    bypass_host = next(iter(SYSTEM_BYPASS_DOMAINS))
    p = HTTPConnectProxy(egress_filter=_MockEgressFilter())
    req = f"CONNECT {bypass_host}:443 HTTP/1.1\r\nHost: {bypass_host}\r\n\r\n".encode()
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert len(log_calls) == 1
    assert log_calls[0]["domain"] == bypass_host
    assert log_calls[0]["decision"] == "allow"
    assert log_calls[0]["agent_id"] == "http_connect_proxy"
    assert log_calls[0]["reason"] == "system egress bypass domain"


@pytest.mark.asyncio
async def test_system_bypass_without_egress_filter(monkeypatch):
    """System bypass domains should not error when egress_filter is None."""

    async def _open_conn(_host, _port):
        r = asyncio.StreamReader()
        r.feed_eof()
        return r, _DummyTargetWriter()

    monkeypatch.setattr(asyncio, "open_connection", _open_conn)

    bypass_host = next(iter(SYSTEM_BYPASS_DOMAINS))
    p = HTTPConnectProxy(egress_filter=None)
    req = f"CONNECT {bypass_host}:443 HTTP/1.1\r\nHost: {bypass_host}\r\n\r\n".encode()
    reader = _make_stream(req)
    writer = _MockWriter()

    # Must not raise
    await p._process_connect(reader, writer)
    assert b"200 Connection Established" in writer.written


# ============================================================
# _agent_id_for_peer — IP→bot registry + lazy rDNS attribution
# ============================================================


def test_agent_id_for_peer_known_ip():
    """Startup registry hit returns correct bot_id immediately."""
    p = HTTPConnectProxy(ip_to_bot_registry={"10.1.2.3": "hermes"})
    assert p._agent_id_for_peer(("10.1.2.3", 12345)) == "hermes"


def test_agent_id_for_peer_none_peer():
    """None peer falls back to generic label without error."""
    p = HTTPConnectProxy()
    assert p._agent_id_for_peer(None) == "http_connect_proxy"


def test_agent_id_for_peer_unknown_no_hostnames():
    """Unknown IP with no bot_hostnames registered → generic label, cached."""
    p = HTTPConnectProxy()
    result = p._agent_id_for_peer(("10.9.9.9", 5000))
    assert result == "http_connect_proxy"
    assert p._ip_to_bot_registry["10.9.9.9"] == "http_connect_proxy"


def test_agent_id_for_peer_lazy_rdns_hit(monkeypatch):
    """Unknown IP resolved via reverse-DNS to a known bot hostname → correct bot_id cached."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: ("agentshroud-hermes", [], [ip]),
    )
    result = p._agent_id_for_peer(("172.22.0.5", 9999))
    assert result == "hermes"
    assert p._ip_to_bot_registry["172.22.0.5"] == "hermes"


def test_agent_id_for_peer_lazy_rdns_miss(monkeypatch):
    """Unknown IP whose rDNS doesn't match any bot, and fDNS fails → generic label, cached."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: ("some-unknown-host.local", [], [ip]),
    )
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.getaddrinfo",
        lambda host, port: (_ for _ in ()).throw(OSError("NXDOMAIN")),
    )
    result = p._agent_id_for_peer(("192.168.5.5", 1234))
    assert result == "http_connect_proxy"
    assert p._ip_to_bot_registry["192.168.5.5"] == "http_connect_proxy"


def test_agent_id_for_peer_lazy_rdns_error(monkeypatch):
    """rDNS failure + fDNS failure → generic label, cached, no exception."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: (_ for _ in ()).throw(OSError("nodename nor servname provided")),
    )
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.getaddrinfo",
        lambda host, port: (_ for _ in ()).throw(OSError("NXDOMAIN")),
    )
    result = p._agent_id_for_peer(("10.0.0.1", 8080))
    assert result == "http_connect_proxy"


def test_agent_id_for_peer_cached_after_first_lookup(monkeypatch):
    """Second call for same IP uses cache; rDNS is only called once, fDNS never."""
    rdns_calls = {"n": 0}
    fdns_calls = {"n": 0}

    def _rdns(ip):
        rdns_calls["n"] += 1
        return ("agentshroud-hermes", [], [ip])

    def _fdns(host, port):
        fdns_calls["n"] += 1
        return [(0, 0, 0, "", ("172.22.0.7", 0))]

    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr("gateway.proxy.http_proxy.socket.gethostbyaddr", _rdns)
    monkeypatch.setattr("gateway.proxy.http_proxy.socket.getaddrinfo", _fdns)

    p._agent_id_for_peer(("172.22.0.7", 111))
    p._agent_id_for_peer(("172.22.0.7", 222))
    assert rdns_calls["n"] == 1
    assert fdns_calls["n"] == 0  # rDNS hit → fDNS never reached


def test_agent_id_for_peer_forward_dns_hit(monkeypatch):
    """rDNS fails; forward DNS resolves bot hostname to source IP → correct bot_id cached."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: (_ for _ in ()).throw(OSError("no PTR record")),
    )
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.getaddrinfo",
        lambda host, port: [(0, 0, 0, "", ("172.22.0.5", 0))],
    )
    result = p._agent_id_for_peer(("172.22.0.5", 9999))
    assert result == "hermes"
    assert p._ip_to_bot_registry["172.22.0.5"] == "hermes"


def test_agent_id_for_peer_rdns_miss_forward_dns_hit(monkeypatch):
    """rDNS returns non-matching hostname; forward DNS matches → correct bot_id cached."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: ("some-other-host.local", [], [ip]),
    )
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.getaddrinfo",
        lambda host, port: [(0, 0, 0, "", ("10.20.30.40", 0))],
    )
    result = p._agent_id_for_peer(("10.20.30.40", 443))
    assert result == "hermes"
    assert p._ip_to_bot_registry["10.20.30.40"] == "hermes"


def test_agent_id_for_peer_forward_dns_no_ip_match(monkeypatch):
    """rDNS fails; forward DNS resolves to a DIFFERENT IP → generic label, cached."""
    p = HTTPConnectProxy(bot_hostnames={"hermes": "agentshroud-hermes"})
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.gethostbyaddr",
        lambda ip: (_ for _ in ()).throw(OSError("no PTR record")),
    )
    monkeypatch.setattr(
        "gateway.proxy.http_proxy.socket.getaddrinfo",
        lambda host, port: [(0, 0, 0, "", ("1.2.3.4", 0))],  # different IP
    )
    result = p._agent_id_for_peer(("192.168.99.99", 443))
    assert result == "http_connect_proxy"
    assert p._ip_to_bot_registry["192.168.99.99"] == "http_connect_proxy"
