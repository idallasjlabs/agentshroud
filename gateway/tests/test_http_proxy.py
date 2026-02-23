# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for HTTPConnectProxy — CONNECT tunnel server on port 8181."""
from __future__ import annotations


import asyncio
import pytest

from gateway.proxy.http_proxy import HTTPConnectProxy, ALLOWED_DOMAINS
from gateway.proxy.web_config import WebProxyConfig
from gateway.proxy.web_proxy import WebProxy


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
