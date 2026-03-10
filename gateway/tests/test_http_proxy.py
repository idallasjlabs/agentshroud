# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for HTTPConnectProxy — CONNECT tunnel server on port 8181."""
from __future__ import annotations


import asyncio
import pytest
from types import SimpleNamespace

from gateway.proxy.http_proxy import HTTPConnectProxy, ALLOWED_DOMAINS, SYSTEM_BYPASS_DOMAINS
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

    # Even when WebProxy policy would block api.telegram.org in allowlist mode,
    # CONNECT must pass for system bypass domains.
    config = WebProxyConfig(mode="allowlist", allowed_domains=["api.openai.com"])
    egress = _DenyEgress()
    p = HTTPConnectProxy(web_proxy=WebProxy(config=config), egress_filter=egress)
    req = b"CONNECT api.telegram.org:443 HTTP/1.1\r\nHost: api.telegram.org\r\n\r\n"
    reader = _make_stream(req)
    writer = _MockWriter()

    await p._process_connect(reader, writer)

    assert b"200 Connection Established" in writer.written
    assert egress.called is False


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
    assert "api.telegram.org" not in ALLOWED_DOMAINS, "api.telegram.org must not be in CONNECT allowlist"

    # Also verify via WebProxy check
    from gateway.proxy.web_config import WebProxyConfig
    from gateway.proxy.web_proxy import WebProxy
    config = WebProxyConfig(mode="allowlist", allowed_domains=ALLOWED_DOMAINS)
    proxy = WebProxy(config=config)
    result = proxy.check_request("https://api.telegram.org/bot123/sendMessage")
    assert result.blocked, "api.telegram.org must be blocked in CONNECT proxy"


def test_telegram_is_system_bypass_domain():
    assert "api.telegram.org" in SYSTEM_BYPASS_DOMAINS
