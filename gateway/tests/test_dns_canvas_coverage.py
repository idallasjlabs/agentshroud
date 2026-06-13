# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for dns_forwarder, dns_blocklist, and canvas_proxy.

Exercises DNS wire-format parsing, upstream failover, blocked-response
synthesis, blocklist download/update lifecycle, and the Canvas reverse
proxy ASGI app (auth gate, HTTP forwarding, WebSocket relay) — all with
mocked boundaries (no real network).
"""

from __future__ import annotations

import asyncio
import base64
import importlib
import struct
import sys
import types
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
import websockets
import websockets.exceptions

import gateway.proxy.canvas_proxy as canvas_proxy
import gateway.proxy.dns_blocklist as dns_blocklist_mod
import gateway.proxy.dns_forwarder as dns_forwarder
from gateway.proxy.dns_blocklist import DNSBlocklist
from gateway.proxy.dns_forwarder import (
    DNSForwarderProtocol,
    forward_query,
    parse_domain_name,
    parse_query,
    start_dns_forwarder,
)

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────


def build_dns_query(domain: str, qtype: int = 1, txn_id: int = 0x1234) -> bytes:
    """Build a minimal DNS query packet in wire format."""
    header = struct.pack("!HHHHHH", txn_id, 0x0100, 1, 0, 0, 0)
    qname = b"".join(bytes([len(p)]) + p.encode("ascii") for p in domain.split("."))
    qname += b"\x00"
    return header + qname + struct.pack("!HH", qtype, 1)


class _BlockAll:
    """Blocklist stub that blocks every domain."""

    def is_blocked(self, domain: str) -> bool:
        return True


class _BlockNone:
    """Blocklist stub that blocks nothing."""

    def is_blocked(self, domain: str) -> bool:
        return False


def make_fake_socket_module(behaviors: list) -> tuple:
    """Build a fake `socket` module namespace driving forward_query without I/O.

    Each entry in *behaviors* configures the next created socket:
      send_exc — exception raised by sendto()
      close_exc — exception raised by close()
      response — bytes returned by recv()
    """
    created: list = []

    class FakeSock:
        def __init__(self, *args, **kwargs):
            self.behavior = behaviors[len(created)]
            created.append(self)
            self.closed = False
            self.sent: list = []

        def settimeout(self, timeout):
            self.timeout = timeout

        def sendto(self, data, addr):
            if self.behavior.get("send_exc"):
                raise self.behavior["send_exc"]
            self.sent.append((data, addr))

        def recv(self, bufsize):
            return self.behavior["response"]

        def close(self):
            already_closed = self.closed
            self.closed = True
            if self.behavior.get("close_exc") and not already_closed:
                raise self.behavior["close_exc"]

    ns = types.SimpleNamespace(
        socket=FakeSock,
        AF_INET=2,
        SOCK_DGRAM=2,
        error=OSError,
    )
    return ns, created


# ──────────────────────────────────────────────────────────────────────────────
# dns_forwarder: parse_domain_name / parse_query
# ──────────────────────────────────────────────────────────────────────────────


class TestParseDomainName:
    def test_simple_name(self):
        data = b"\x03foo\x03com\x00"
        domain, offset = parse_domain_name(data, 0)
        assert domain == "foo.com"
        assert offset == 9

    def test_compression_pointer(self):
        # "foo" at offset 0, pointer at offset 5 referencing it
        data = b"\x03foo\x00" + b"\xc0\x00"
        domain, offset = parse_domain_name(data, 5)
        assert domain == "foo"
        assert offset == 7  # original_offset = pointer position + 2

    def test_truncated_name_breaks(self):
        # Label claims 3 bytes but packet ends without terminator
        data = b"\x03foo"
        domain, offset = parse_domain_name(data, 0)
        assert domain == "foo"
        assert offset == 4

    def test_pointer_loop_bounded(self):
        # Pointer that points to itself: max_jumps prevents infinite loop
        data = b"\xc0\x00"
        domain, offset = parse_domain_name(data, 0)
        assert domain == ""
        assert offset == 2


class TestParseQuery:
    def test_valid_a_query(self):
        data = build_dns_query("example.com", qtype=1)
        assert parse_query(data) == ("example.com", 1, 1)

    def test_valid_aaaa_query(self):
        data = build_dns_query("v6.example.com", qtype=28)
        assert parse_query(data) == ("v6.example.com", 28, 1)

    def test_too_short(self):
        assert parse_query(b"\x00\x01") is None

    def test_zero_qdcount(self):
        header = struct.pack("!HHHHHH", 1, 0, 0, 0, 0, 0)
        assert parse_query(header) is None

    def test_truncated_after_name(self):
        # Valid name but missing the 4-byte qtype/qclass
        header = struct.pack("!HHHHHH", 1, 0, 1, 0, 0, 0)
        data = header + b"\x03foo\x00"
        assert parse_query(data) is None

    def test_malformed_pointer_returns_none(self):
        # Compression pointer with only one byte → struct.error → None
        header = struct.pack("!HHHHHH", 1, 0, 1, 0, 0, 0)
        data = header + b"\xc0"
        assert parse_query(data) is None


# ──────────────────────────────────────────────────────────────────────────────
# dns_forwarder: forward_query (mocked sockets)
# ──────────────────────────────────────────────────────────────────────────────


class TestForwardQuery:
    async def test_first_upstream_succeeds(self, monkeypatch):
        fake_mod, created = make_fake_socket_module([{"response": b"\xab\xcd"}])
        monkeypatch.setattr(dns_forwarder, "socket", fake_mod)

        result = await forward_query(b"\x00\x01query")
        assert result == b"\xab\xcd"
        assert len(created) == 1
        assert created[0].closed is True
        assert created[0].sent[0][1] == ("8.8.8.8", 53)

    async def test_failover_to_second_upstream(self, monkeypatch):
        fake_mod, created = make_fake_socket_module(
            [
                # First upstream fails on send AND close raises (covers the
                # nested close() exception swallow)
                {"send_exc": OSError("network down"), "close_exc": OSError("bad fd")},
                {"response": b"\x99\x88"},
            ]
        )
        monkeypatch.setattr(dns_forwarder, "socket", fake_mod)

        result = await forward_query(b"\x00\x01query")
        assert result == b"\x99\x88"
        assert len(created) == 2
        assert created[1].sent[0][1] == ("8.8.4.4", 53)

    async def test_all_upstreams_fail_returns_none(self, monkeypatch):
        fake_mod, created = make_fake_socket_module(
            [{"send_exc": OSError("down")}, {"send_exc": OSError("down")}]
        )
        monkeypatch.setattr(dns_forwarder, "socket", fake_mod)

        result = await forward_query(b"\x00\x01query")
        assert result is None
        assert len(created) == 2


# ──────────────────────────────────────────────────────────────────────────────
# dns_forwarder: DNSForwarderProtocol
# ──────────────────────────────────────────────────────────────────────────────


class TestDNSForwarderProtocol:
    def _make_protocol(self, blocklist=None):
        proto = DNSForwarderProtocol(blocklist=blocklist)
        transport = MagicMock()
        proto.connection_made(transport)
        assert proto.transport is transport
        return proto, transport

    async def test_blocked_a_query_returns_zero_ip(self):
        proto, transport = self._make_protocol(blocklist=_BlockAll())
        query = build_dns_query("ads.example.com", qtype=1)

        await proto._handle_query(query, ("10.0.0.1", 41000))

        assert proto.blocked_count == 1
        assert proto.query_count == 1
        sent_data, sent_addr = transport.sendto.call_args[0]
        assert sent_addr == ("10.0.0.1", 41000)
        # QR/AA/RD flags set, ANCOUNT=1
        assert sent_data[2] == 0x85
        assert sent_data[3] == 0x80
        assert sent_data[6:8] == b"\x00\x01"
        # Answer ends with A record 0.0.0.0
        assert sent_data.endswith(b"\x00\x04" + b"\x00\x00\x00\x00")

    async def test_blocked_aaaa_query_returns_null_ipv6(self):
        proto, transport = self._make_protocol(blocklist=_BlockAll())
        query = build_dns_query("ads.example.com", qtype=28)

        await proto._handle_query(query, ("10.0.0.1", 41001))

        sent_data, _ = transport.sendto.call_args[0]
        assert sent_data[6:8] == b"\x00\x01"
        # AAAA answer: RDLENGTH 16 + sixteen zero bytes (::)
        assert sent_data.endswith(b"\x00\x10" + b"\x00" * 16)

    async def test_blocked_other_qtype_returns_nxdomain(self):
        proto, transport = self._make_protocol(blocklist=_BlockAll())
        query = build_dns_query("ads.example.com", qtype=16)  # TXT

        await proto._handle_query(query, ("10.0.0.1", 41002))

        sent_data, _ = transport.sendto.call_args[0]
        assert sent_data[3] == 0x83  # RCODE=3 NXDOMAIN
        assert sent_data[6:8] == b"\x00\x00"  # ANCOUNT=0

    async def test_forwarded_query_relays_upstream_response(self, monkeypatch):
        proto, transport = self._make_protocol(blocklist=_BlockNone())
        upstream_response = build_dns_query("example.com", qtype=1)
        monkeypatch.setattr(
            dns_forwarder, "forward_query", AsyncMock(return_value=upstream_response)
        )

        await proto._handle_query(build_dns_query("example.com"), ("10.0.0.2", 5000))

        sent_data, sent_addr = transport.sendto.call_args[0]
        assert sent_data == upstream_response
        assert sent_addr == ("10.0.0.2", 5000)
        assert proto.blocked_count == 0

    async def test_short_upstream_response_still_relayed(self, monkeypatch):
        # Response shorter than 4 bytes → rcode unparseable but still relayed
        proto, transport = self._make_protocol()
        monkeypatch.setattr(dns_forwarder, "forward_query", AsyncMock(return_value=b"\x12"))

        await proto._handle_query(build_dns_query("example.com"), ("10.0.0.3", 5001))

        sent_data, _ = transport.sendto.call_args[0]
        assert sent_data == b"\x12"

    async def test_all_upstreams_fail_sends_servfail(self, monkeypatch):
        proto, transport = self._make_protocol()
        monkeypatch.setattr(dns_forwarder, "forward_query", AsyncMock(return_value=None))
        query = build_dns_query("example.com", txn_id=0xBEEF)

        await proto._handle_query(query, ("10.0.0.4", 5002))

        sent_data, _ = transport.sendto.call_args[0]
        assert len(sent_data) == 12
        assert sent_data[0:2] == b"\xbe\xef"  # transaction ID preserved
        assert sent_data[2] == 0x81  # QR=1, RD=1
        assert sent_data[3] == 0x02  # RCODE=SERVFAIL

    async def test_unparseable_short_query_no_servfail_sent(self, monkeypatch):
        # Data < 12 bytes: unparseable AND too short to build a SERVFAIL
        proto, transport = self._make_protocol()
        monkeypatch.setattr(dns_forwarder, "forward_query", AsyncMock(return_value=None))

        await proto._handle_query(b"\x01\x02\x03", ("10.0.0.5", 5003))

        transport.sendto.assert_not_called()
        assert proto.query_count == 1

    async def test_datagram_received_schedules_handler(self):
        proto, transport = self._make_protocol(blocklist=_BlockAll())
        before = set(asyncio.all_tasks())

        proto.datagram_received(build_dns_query("ads.example.com"), ("10.0.0.6", 5004))

        new_tasks = set(asyncio.all_tasks()) - before - {asyncio.current_task()}
        assert new_tasks  # handler was scheduled
        await asyncio.gather(*new_tasks)
        assert proto.blocked_count == 1
        transport.sendto.assert_called_once()

    def test_error_received_logs(self, caplog):
        proto = DNSForwarderProtocol()
        with caplog.at_level("ERROR", logger="agentshroud.dns_forwarder"):
            proto.error_received(RuntimeError("boom"))
        assert "boom" in caplog.text


class TestStartDNSForwarder:
    async def test_binds_and_returns_transport(self):
        transport = await start_dns_forwarder(host="127.0.0.1", port=0)
        try:
            assert transport is not None
            sockname = transport.get_extra_info("sockname")
            assert sockname[0] == "127.0.0.1"
            assert sockname[1] > 0
        finally:
            transport.close()
            await asyncio.sleep(0)  # let the loop process the close


class TestImportFallback:
    def test_dns_blocklist_import_failure_sets_none(self):
        saved_fwd = sys.modules.get("gateway.proxy.dns_forwarder")
        saved_bl = sys.modules.get("gateway.proxy.dns_blocklist")
        try:
            sys.modules.pop("gateway.proxy.dns_forwarder", None)
            # None in sys.modules forces ImportError on `from .dns_blocklist import ...`
            sys.modules["gateway.proxy.dns_blocklist"] = None
            mod = importlib.import_module("gateway.proxy.dns_forwarder")
            assert mod.DNSBlocklist is None
        finally:
            sys.modules.pop("gateway.proxy.dns_forwarder", None)
            if saved_bl is not None:
                sys.modules["gateway.proxy.dns_blocklist"] = saved_bl
            else:
                sys.modules.pop("gateway.proxy.dns_blocklist", None)
            if saved_fwd is not None:
                sys.modules["gateway.proxy.dns_forwarder"] = saved_fwd
                # Re-point the parent package attribute at the original module
                setattr(sys.modules["gateway.proxy"], "dns_forwarder", saved_fwd)


# ──────────────────────────────────────────────────────────────────────────────
# dns_blocklist: wildcard denylist, parent allowlist, parsing edge cases
# ──────────────────────────────────────────────────────────────────────────────


class TestBlocklistWildcardsAndAllowlist:
    def test_wildcard_denylist_blocks_subdomains(self, tmp_path):
        bl = DNSBlocklist(
            blocklist_urls=[],
            custom_denylist={"*.evil.test", "plain.evil.test"},
            data_dir=tmp_path,
        )
        assert bl.is_blocked("sub.evil.test") is True
        assert bl.is_blocked("deep.sub.evil.test") is True
        assert bl.is_blocked("plain.evil.test") is True  # exact denylist entry
        assert bl.is_blocked("unrelated.test") is False

    def test_parent_allowlist_overrides_grandparent_block(self, tmp_path):
        bl = DNSBlocklist(
            blocklist_urls=[],
            custom_allowlist={"trusted.evil.test"},
            data_dir=tmp_path,
        )
        bl.blocked_domains.add("evil.test")
        # Parent "trusted.evil.test" is allowlisted → not blocked even though
        # grandparent "evil.test" is on the blocklist
        assert bl.is_blocked("api.trusted.evil.test") is False
        assert bl.is_blocked("other.evil.test") is True

    def test_hosts_line_without_domain_returns_none(self, tmp_path):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=tmp_path)
        assert bl.parse_hosts_line("0.0.0.0") is None
        assert bl.parse_hosts_line("0.0.0.0 .leading-dot.test") is None


class TestBlocklistDownload:
    async def test_download_success_caches_to_disk(self, tmp_path):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=tmp_path)
        url = "https://lists.example.test/hosts"
        fake_resp = MagicMock()
        fake_resp.read.return_value = b"0.0.0.0 ads.example.test\n"

        with patch("urllib.request.urlopen", return_value=fake_resp):
            text = await bl.download_blocklist(url)

        assert text == "0.0.0.0 ads.example.test\n"
        cache_file = tmp_path / f"blocklist_{hash(url) & 0xFFFFFFFF:08x}.txt"
        assert cache_file.exists()
        assert "ads.example.test" in cache_file.read_text()

    async def test_download_failure_no_cache_returns_none(self, tmp_path):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=tmp_path)

        with patch("urllib.request.urlopen", side_effect=OSError("refused")):
            text = await bl.download_blocklist("https://down.example.test/hosts")

        assert text is None

    async def test_download_failure_falls_back_to_cache(self, tmp_path):
        bl = DNSBlocklist(blocklist_urls=[], data_dir=tmp_path)
        url = "https://flaky.example.test/hosts"
        cache_file = tmp_path / f"blocklist_{hash(url) & 0xFFFFFFFF:08x}.txt"
        cache_file.write_text("0.0.0.0 cached.example.test\n")

        with patch("urllib.request.urlopen", side_effect=OSError("timeout")):
            text = await bl.download_blocklist(url)

        assert text == "0.0.0.0 cached.example.test\n"


class TestBlocklistUpdate:
    async def test_update_rebuilds_blocked_domains(self, tmp_path):
        bl = DNSBlocklist(
            blocklist_urls=["https://a.example.test/hosts", "https://b.example.test/hosts"],
            custom_denylist={"deny.example.test"},
            data_dir=tmp_path,
        )
        bl.blocked_domains.add("stale.example.test")
        # First source returns text (one valid + one allowlisted + junk),
        # second source fails (None)
        bl.download_blocklist = AsyncMock(
            side_effect=["0.0.0.0 ads.example.test\n0.0.0.0 localhost\nnot a domain!", None]
        )

        await bl.update()

        assert "ads.example.test" in bl.blocked_domains
        assert "deny.example.test" in bl.blocked_domains  # custom denylist included
        assert "stale.example.test" not in bl.blocked_domains  # rebuilt from scratch
        assert bl.last_update > 0

    async def test_periodic_loop_survives_errors_until_cancelled(self, tmp_path, monkeypatch):
        monkeypatch.setattr(dns_blocklist_mod, "UPDATE_INTERVAL_SECONDS", 0)
        bl = DNSBlocklist(blocklist_urls=[], data_dir=tmp_path)
        bl.update = AsyncMock(side_effect=[Exception("boom"), asyncio.CancelledError()])

        await bl.start_periodic_updates()
        with pytest.raises(asyncio.CancelledError):
            await bl.update_task

        # First failure was swallowed and logged; loop ran a second iteration
        assert bl.update.await_count == 2
        bl.stop()


# ──────────────────────────────────────────────────────────────────────────────
# canvas_proxy: auth helpers
# ──────────────────────────────────────────────────────────────────────────────


@pytest.fixture
def gateway_password(tmp_path, monkeypatch):
    """Provision a gateway password file and return the password."""
    secret_file = tmp_path / "gateway_password"
    secret_file.write_text("s3cret-pw\n")
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(secret_file))
    monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)
    return "s3cret-pw"


def _basic(password: str, user: str = "admin") -> str:
    return "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode()


class TestCanvasAuthHelpers:
    def test_read_password_from_file(self, gateway_password):
        assert canvas_proxy._read_gateway_password() == gateway_password

    def test_read_password_env_fallback(self, tmp_path, monkeypatch):
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "missing"))
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "env-token")
        assert canvas_proxy._read_gateway_password() == "env-token"

    def test_token_auth_valid(self, gateway_password):
        assert canvas_proxy._check_token_auth(f"token={gateway_password}") is True

    def test_token_auth_wrong_and_missing(self, gateway_password):
        assert canvas_proxy._check_token_auth("token=wrong") is False
        assert canvas_proxy._check_token_auth("other=1") is False

    def test_token_auth_empty_expected_password(self, tmp_path, monkeypatch):
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "missing"))
        monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)
        assert canvas_proxy._check_token_auth("token=anything") is False

    def test_basic_auth_valid(self, gateway_password):
        assert canvas_proxy._check_basic_auth(_basic(gateway_password)) is True

    def test_basic_auth_wrong_password(self, gateway_password):
        assert canvas_proxy._check_basic_auth(_basic("nope")) is False

    def test_basic_auth_not_basic_scheme(self, gateway_password):
        assert canvas_proxy._check_basic_auth("Bearer abc") is False
        assert canvas_proxy._check_basic_auth("") is False

    def test_basic_auth_invalid_base64(self, gateway_password):
        assert canvas_proxy._check_basic_auth("Basic !!!not-base64!!!") is False

    def test_basic_auth_no_password_configured(self, tmp_path, monkeypatch):
        monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "missing"))
        monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)
        assert canvas_proxy._check_basic_auth(_basic("anything")) is False

    def test_build_proxy_headers_strips_hop_by_hop_and_auth(self):
        headers = {
            "Connection": "keep-alive",
            "Authorization": "Basic abc",
            "Transfer-Encoding": "chunked",
            "X-Custom": "1",
            "Accept": "text/html",
        }
        forwarded = canvas_proxy._build_proxy_headers(headers)
        assert "Connection" not in forwarded
        assert "Authorization" not in forwarded
        assert "Transfer-Encoding" not in forwarded
        assert forwarded["X-Custom"] == "1"
        assert forwarded["Accept"] == "text/html"
        assert forwarded["host"] == "localhost:18789"


# ──────────────────────────────────────────────────────────────────────────────
# canvas_proxy: ASGI app — lifespan + HTTP
# ──────────────────────────────────────────────────────────────────────────────


def _http_scope(headers: list, path: str = "/dashboard", query: bytes = b"") -> dict:
    return {
        "type": "http",
        "method": "GET",
        "path": path,
        "query_string": query,
        "headers": headers,
        "client": ("127.0.0.1", 50000),
    }


async def _run_asgi(scope: dict, events: list) -> list:
    """Drive the canvas ASGI app with scripted receive events; collect sends."""
    pending = list(events)
    sent: list = []

    async def receive():
        if pending:
            return pending.pop(0)
        await asyncio.Event().wait()  # block until cancelled

    async def send(message):
        sent.append(message)

    await canvas_proxy.canvas_proxy_app(scope, receive, send)
    # Give the loop one cycle so any relay tasks cancelled by the proxy
    # finish unwinding (prevents "task destroyed while pending" noise).
    await asyncio.sleep(0)
    return sent


class _FakeUpstreamResponse:
    def __init__(self, status_code=200, headers=None, content=b"<html>ok</html>"):
        self.status_code = status_code
        self.headers = headers or {"content-type": "text/html", "transfer-encoding": "chunked"}
        self.content = content


class _FakeAsyncClient:
    """Stands in for httpx.AsyncClient; records request kwargs."""

    instances: list = []
    response: _FakeUpstreamResponse = None
    raise_exc: Exception = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.requests: list = []
        _FakeAsyncClient.instances.append(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        return False

    async def request(self, **kwargs):
        self.requests.append(kwargs)
        if _FakeAsyncClient.raise_exc is not None:
            raise _FakeAsyncClient.raise_exc
        return _FakeAsyncClient.response


@pytest.fixture
def fake_httpx_client(monkeypatch):
    _FakeAsyncClient.instances = []
    _FakeAsyncClient.response = _FakeUpstreamResponse()
    _FakeAsyncClient.raise_exc = None
    monkeypatch.setattr(canvas_proxy.httpx, "AsyncClient", _FakeAsyncClient)
    return _FakeAsyncClient


class TestCanvasLifespan:
    async def test_lifespan_startup_shutdown(self):
        sent = await _run_asgi(
            {"type": "lifespan"},
            [{"type": "lifespan.startup"}, {"type": "lifespan.shutdown"}],
        )
        assert sent == [
            {"type": "lifespan.startup.complete"},
            {"type": "lifespan.shutdown.complete"},
        ]


class TestCanvasHTTP:
    async def test_unauthorized_returns_401(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        scope = _http_scope(headers=[(b"accept", b"text/html")])

        sent = await _run_asgi(scope, [])

        start = sent[0]
        assert start["status"] == 401
        header_map = {k: v for k, v in start["headers"]}
        assert header_map[b"www-authenticate"] == b'Basic realm="AgentShroud Canvas"'
        assert sent[1]["body"] == b"Authentication required"

    async def test_authorized_request_proxied_upstream(
        self, gateway_password, monkeypatch, fake_httpx_client
    ):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        scope = _http_scope(
            headers=[
                (b"authorization", _basic(gateway_password).encode()),
                (b"connection", b"keep-alive"),
                (b"x-custom", b"yes"),
            ],
            path="/api/status",
            query=b"a=b",
        )
        events = [
            {"type": "http.request", "body": b"par", "more_body": True},
            {"type": "http.request", "body": b"t2", "more_body": False},
        ]

        sent = await _run_asgi(scope, events)

        # Upstream request: URL includes query, body reassembled, headers cleaned
        req = fake_httpx_client.instances[0].requests[0]
        assert req["url"].endswith("/api/status?a=b")
        assert req["content"] == b"part2"
        assert "authorization" not in {k.lower() for k in req["headers"]}
        assert req["headers"]["x-custom"] == "yes"
        assert req["headers"]["host"] == "localhost:18789"
        # Response relayed with hop-by-hop headers stripped
        start = sent[0]
        assert start["status"] == 200
        response_header_names = {k for k, _ in start["headers"]}
        assert b"content-type" in response_header_names
        assert b"transfer-encoding" not in response_header_names
        assert sent[1]["body"] == b"<html>ok</html>"

    async def test_upstream_failure_returns_502(
        self, gateway_password, monkeypatch, fake_httpx_client
    ):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        fake_httpx_client.raise_exc = httpx.ConnectError("connection refused")
        scope = _http_scope(headers=[(b"authorization", _basic(gateway_password).encode())])
        events = [{"type": "http.request", "body": b"", "more_body": False}]

        sent = await _run_asgi(scope, events)

        assert sent[0]["status"] == 502
        assert sent[1]["body"] == b"Canvas unavailable"

    async def test_skip_basic_auth_bypasses_gate(
        self, gateway_password, monkeypatch, fake_httpx_client
    ):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", True)
        scope = _http_scope(headers=[])  # no auth header at all
        events = [{"type": "http.request", "body": b"", "more_body": False}]

        sent = await _run_asgi(scope, events)

        assert sent[0]["status"] == 200  # proxied without auth challenge


# ──────────────────────────────────────────────────────────────────────────────
# canvas_proxy: WebSocket relay
# ──────────────────────────────────────────────────────────────────────────────


class _FakeUpstreamWS:
    """Fake upstream WebSocket: yields scripted messages, records sends."""

    def __init__(self, messages):
        self.messages = list(messages)
        self.sent: list = []
        self.closed = asyncio.Event()

    async def send(self, data):
        self.sent.append(data)

    async def close(self):
        self.closed.set()

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.messages:
            return self.messages.pop(0)
        # Hold the iterator open until the client side disconnects
        await self.closed.wait()
        raise StopAsyncIteration


class _FakeWSConnect:
    """Async context manager mimicking websockets.connect()."""

    captured: dict = {}

    def __init__(self, ws):
        self.ws = ws

    async def __aenter__(self):
        return self.ws

    async def __aexit__(self, *args):
        return False


def _ws_scope(headers: list, query: bytes = b"", path: str = "/ws") -> dict:
    return {
        "type": "websocket",
        "path": path,
        "query_string": query,
        "headers": headers,
        "client": ("127.0.0.1", 50001),
    }


class TestCanvasWebSocket:
    async def test_unauthorized_ws_closed_4401(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        scope = _ws_scope(headers=[(b"origin", b"http://evil.example.test")])
        # str (not bytes) query_string exercises the str() normalization branch
        scope["query_string"] = ""

        sent = await _run_asgi(scope, [])

        assert sent == [{"type": "websocket.close", "code": 4401, "reason": "Unauthorized"}]

    async def test_relay_with_trusted_origin(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        upstream = _FakeUpstreamWS(messages=[b"bin-from-upstream", "text-from-upstream"])

        def fake_connect(url, **kwargs):
            _FakeWSConnect.captured = {"url": url, **kwargs}
            return _FakeWSConnect(upstream)

        monkeypatch.setattr(websockets, "connect", fake_connect)
        scope = _ws_scope(
            headers=[(b"origin", b"http://localhost:18789")],
            query=b"session=1",
        )
        events = [
            {"type": "websocket.connect"},
            {"type": "websocket.receive", "text": "hello"},
            {"type": "websocket.receive", "bytes": b"\x01\x02"},
            {"type": "websocket.receive"},  # neither text nor bytes → b""
            {"type": "websocket.disconnect"},
        ]

        sent = await _run_asgi(scope, events)

        # Upstream URL: ws scheme + path + query; Origin forwarded
        assert _FakeWSConnect.captured["url"].startswith("ws://")
        assert _FakeWSConnect.captured["url"].endswith("/ws?session=1")
        assert _FakeWSConnect.captured["additional_headers"]["Origin"] == "http://localhost:18789"
        assert _FakeWSConnect.captured["additional_headers"]["Host"] == "localhost:18789"
        # Client → upstream messages relayed
        assert upstream.sent == [b"hello", b"\x01\x02", b""]
        assert upstream.closed.is_set()
        # Upstream → client messages relayed, then closed cleanly
        assert {"type": "websocket.accept"} in sent
        assert {"type": "websocket.send", "bytes": b"bin-from-upstream"} in sent
        assert {"type": "websocket.send", "text": "text-from-upstream"} in sent
        assert sent[-1] == {"type": "websocket.close", "code": 1000}

    async def test_token_query_param_authenticates_ws(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        upstream = _FakeUpstreamWS(messages=[])
        monkeypatch.setattr(websockets, "connect", lambda url, **kw: _FakeWSConnect(upstream))
        scope = _ws_scope(headers=[], query=f"token={gateway_password}".encode())
        events = [
            {"type": "websocket.connect"},
            {"type": "websocket.disconnect"},
        ]

        sent = await _run_asgi(scope, events)

        assert {"type": "websocket.accept"} in sent  # token auth accepted

    async def test_sec_websocket_protocol_token_authenticates(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)
        upstream = _FakeUpstreamWS(messages=[])
        monkeypatch.setattr(websockets, "connect", lambda url, **kw: _FakeWSConnect(upstream))
        scope = _ws_scope(
            headers=[(b"sec-websocket-protocol", f"chat, {gateway_password}".encode())]
        )
        events = [
            {"type": "websocket.connect"},
            {"type": "websocket.disconnect"},
        ]

        sent = await _run_asgi(scope, events)

        assert {"type": "websocket.accept"} in sent

    async def test_upstream_ws_exception_closes_gracefully(self, gateway_password, monkeypatch):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)

        def failing_connect(url, **kwargs):
            raise websockets.exceptions.WebSocketException("upstream refused")

        monkeypatch.setattr(websockets, "connect", failing_connect)
        scope = _ws_scope(headers=[(b"authorization", _basic(gateway_password).encode())])
        events = [{"type": "websocket.connect"}]

        sent = await _run_asgi(scope, events)

        assert {"type": "websocket.accept"} in sent
        assert sent[-1] == {"type": "websocket.close", "code": 1000}

    async def test_generic_exception_and_failing_close_swallowed(
        self, gateway_password, monkeypatch
    ):
        monkeypatch.setattr(canvas_proxy, "_SKIP_BASIC_AUTH", False)

        def broken_connect(url, **kwargs):
            raise RuntimeError("totally unexpected")

        monkeypatch.setattr(websockets, "connect", broken_connect)
        scope = _ws_scope(headers=[(b"origin", b"http://127.0.0.1:18789")])
        pending = [{"type": "websocket.connect"}]
        sent: list = []

        async def receive():
            return pending.pop(0)

        async def send(message):
            if message["type"] == "websocket.close":
                # Client already gone — the finally block must swallow this
                raise RuntimeError("client disconnected")
            sent.append(message)

        # Must not raise despite both the upstream error and the failing close
        await canvas_proxy.canvas_proxy_app(scope, receive, send)
        assert {"type": "websocket.accept"} in sent
