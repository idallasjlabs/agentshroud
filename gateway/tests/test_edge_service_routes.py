# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — start-up assembly, RPC error mapping, TCP relay, edge provider errors."""

import asyncio
import base64
import io
import json
import logging
from types import SimpleNamespace

import httpx
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from fastapi import FastAPI

from gateway.inbound_edge import descriptors as d
from gateway.inbound_edge import service as svc_mod
from gateway.inbound_edge.edge_jwt import generate_signing_key_pem
from gateway.inbound_edge.oauth_service import OAuthFailure
from gateway.inbound_edge.routes import router, start_edge_forwarder

# ── start-up assembly ───────────────────────────────────────────────────────


@pytest.fixture
def signed_descriptors(tmp_path, monkeypatch):
    """A correctly signed manifest in a temp dir, wired in place of the committed one."""
    key = Ed25519PrivateKey.generate()
    manifest = d.build_manifest()
    (tmp_path / "m.json").write_text(json.dumps(manifest))
    (tmp_path / "m.sig").write_text(
        base64.b64encode(key.sign(d.canonical_bytes(manifest))).decode()
    )
    (tmp_path / "p.pem").write_bytes(
        key.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
    monkeypatch.setattr(d, "MANIFEST_PATH", tmp_path / "m.json")
    monkeypatch.setattr(d, "SIGNATURE_PATH", tmp_path / "m.sig")
    monkeypatch.setattr(d, "PUBLIC_KEY_PATH", tmp_path / "p.pem")
    return tmp_path


@pytest.fixture
def secrets_dir(tmp_path, monkeypatch):
    sec = tmp_path / "secrets"
    sec.mkdir()
    (sec / "edge_signing_key").write_bytes(generate_signing_key_pem())
    (sec / "edge_gateway_token").write_text("t" * 48 + "\n")
    (sec / "hermes_api_key").write_text("hk\n")
    monkeypatch.setattr(svc_mod, "_SECRETS_DIR", sec)
    return sec


def _app_state(tmp_path, audit=True):
    from gateway.ingest_api.config import PIIConfig
    from gateway.security.progressive_lockdown import ProgressiveLockdown

    events = []

    async def emit(e):
        events.append(e)

    return SimpleNamespace(
        approval_queue=SimpleNamespace(bot_token=None, admin_chat_id=None),
        audit_store=object() if audit else None,
        event_bus=SimpleNamespace(emit=emit, events=events),
        progressive_lockdown=ProgressiveLockdown(),
        pipeline=None,
        sanitizer=None,
        config=SimpleNamespace(pii=PIIConfig()),
    )


async def test_disabled_by_default(tmp_path, monkeypatch):
    monkeypatch.delenv("AGENTSHROUD_INBOUND_EDGE", raising=False)
    assert await svc_mod.build_edge_service(_app_state(tmp_path)) is None


async def test_enabled_without_secrets_refuses(tmp_path, monkeypatch, caplog):
    monkeypatch.setenv("AGENTSHROUD_INBOUND_EDGE", "1")
    monkeypatch.setattr(svc_mod, "_SECRETS_DIR", tmp_path / "none")
    monkeypatch.setenv("AGENTSHROUD_EDGE_PUBLIC_URL", "https://e.ts.net:8443")
    with caplog.at_level(logging.CRITICAL):
        assert await svc_mod.build_edge_service(_app_state(tmp_path)) is None
    assert "NOT started" in caplog.text


async def test_http_public_url_refused(tmp_path, monkeypatch, secrets_dir):
    monkeypatch.setenv("AGENTSHROUD_INBOUND_EDGE", "1")
    monkeypatch.setenv("AGENTSHROUD_EDGE_PUBLIC_URL", "http://e.ts.net:8443")
    assert await svc_mod.build_edge_service(_app_state(tmp_path)) is None


async def test_unsigned_descriptors_refuse(tmp_path, monkeypatch, secrets_dir):
    monkeypatch.setenv("AGENTSHROUD_INBOUND_EDGE", "1")
    monkeypatch.setenv("AGENTSHROUD_EDGE_PUBLIC_URL", "https://e.ts.net:8443")
    monkeypatch.setattr(d, "SIGNATURE_PATH", tmp_path / "missing.sig")
    with pytest.raises(d.DescriptorIntegrityError):
        await svc_mod.build_edge_service(_app_state(tmp_path))


async def test_builds_with_everything_enabled(
    tmp_path, monkeypatch, secrets_dir, signed_descriptors
):
    monkeypatch.setenv("AGENTSHROUD_INBOUND_EDGE", "1")
    monkeypatch.setenv("AGENTSHROUD_EDGE_PUBLIC_URL", "https://e.ts.net:8443/")
    monkeypatch.setenv("AGENTSHROUD_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("AGENTSHROUD_EDGE_PKE_FEEDS", "https://a/feed.xml, ,")
    monkeypatch.setenv("AGENTSHROUD_EDGE_DELEGATE", "1")
    state = _app_state(tmp_path)
    edge = await svc_mod.build_edge_service(state)
    try:
        assert edge.issuer == "https://e.ts.net:8443" and edge.resource.endswith("/mcp")
        assert sorted(edge.pipeline.d.facades) == ["delegate_to_hermes", "lab_search", "pke_status"]
        assert edge.pipeline.d.local_agents == {"hermes"}
        assert edge.service_token_ok("t" * 48) and not edge.service_token_ok("x" * 48)
        assert not edge.service_token_ok(None)
        assert state.event_bus.events[0].summary == "Inbound MCP Edge started"
        canaries = await svc_mod.store_canaries(edge.store)
        assert len(canaries) == svc_mod.CANARY_COUNT
        assert await svc_mod.store_canaries(edge.store) == canaries  # stable per install
        for value in canaries:
            assert edge.pipeline.d.tripwire.scan_response(f"x {value} y", source="t").is_blocked
    finally:
        await edge.close()


async def test_no_audit_store_refuses(tmp_path, monkeypatch, secrets_dir, signed_descriptors):
    monkeypatch.setenv("AGENTSHROUD_INBOUND_EDGE", "1")
    monkeypatch.setenv("AGENTSHROUD_EDGE_PUBLIC_URL", "https://e.ts.net:8443")
    monkeypatch.setenv("AGENTSHROUD_DATA_DIR", str(tmp_path))
    assert await svc_mod.build_edge_service(_app_state(tmp_path, audit=False)) is None


async def test_telegram_send_posts_card(monkeypatch):
    sent = {}

    class FakeClient:
        def __init__(self, **kw):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def post(self, url, json):
            sent["url"], sent["json"] = url, json
            return SimpleNamespace(raise_for_status=lambda: None)

    monkeypatch.setattr(svc_mod.httpx, "AsyncClient", FakeClient)
    await svc_mod._telegram_send("BOT", "42", "hi", {"inline_keyboard": []})
    assert sent["url"].endswith("/botBOT/sendMessage")
    assert sent["json"] == {"chat_id": "42", "text": "hi", "reply_markup": {"inline_keyboard": []}}


# ── /edge/v1/rpc error mapping ──────────────────────────────────────────────


def _rpc_app(monkeypatch, oauth=None, pipeline=None):
    from gateway.ingest_api.state import app_state

    edge = SimpleNamespace(
        service_token_ok=lambda t: t == "t" * 40,
        oauth=oauth or SimpleNamespace(),
        pipeline=pipeline or SimpleNamespace(),
        tokens=SimpleNamespace(public_key_pem=b"pem"),
        issuer="https://e",
        resource="https://e/mcp",
    )
    monkeypatch.setattr(app_state, "inbound_edge", edge, raising=False)
    app = FastAPI()
    app.include_router(router)
    return app


async def _post(app, body, raw=False):
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://g") as c:
        kw = {"content": body} if raw else {"json": body}
        return await c.post("/edge/v1/rpc", headers={"X-Edge-Service-Token": "t" * 40}, **kw)


class Raises:
    def __init__(self, exc):
        self.exc = exc

    def __getattr__(self, name):
        async def method(**kw):
            raise self.exc

        return method


@pytest.mark.parametrize(
    "exc,status,code",
    [
        (OAuthFailure("invalid_grant", "nope"), 400, "oauth"),
        (PermissionError("vendor disabled"), 403, "forbidden"),
        (TypeError("x"), 400, "bad_params"),
        (RuntimeError("boom"), 500, "internal"),
    ],
)
async def test_rpc_error_mapping(monkeypatch, exc, status, code):
    app = _rpc_app(monkeypatch, oauth=Raises(exc), pipeline=Raises(exc))
    r = await _post(app, {"method": "oauth.get_client", "params": {"client_id": "c"}})
    assert r.status_code == status and r.json()["error"]["code"] == code
    assert "boom" not in r.text  # internals never leak


async def test_rpc_too_large_and_disabled(monkeypatch):
    app = _rpc_app(monkeypatch)
    r = await _post(app, b"{" + b" " * 300_000 + b"}", raw=True)
    assert r.status_code == 413
    from gateway.ingest_api.state import app_state

    monkeypatch.setattr(app_state, "inbound_edge", None)
    assert (await _post(app, {"method": "keys"})).status_code == 503


async def test_rpc_params_must_be_object(monkeypatch):
    app = _rpc_app(monkeypatch)
    assert (await _post(app, {"method": "keys", "params": [1]})).status_code == 400


# ── TCP relay ──────────────────────────────────────────────────────────────


async def test_forwarder_relays_bytes_both_ways():
    async def echo(reader, writer):
        data = await reader.read(100)
        writer.write(b"echo:" + data)
        await writer.drain()
        writer.close()

    upstream = await asyncio.start_server(echo, "127.0.0.1", 0)
    up_port = upstream.sockets[0].getsockname()[1]
    probe = await asyncio.start_server(lambda r, w: None, "127.0.0.1", 0)
    listen_port = probe.sockets[0].getsockname()[1]
    probe.close()
    await probe.wait_closed()
    task = start_edge_forwarder(listen_port, "127.0.0.1", up_port)
    try:
        for _ in range(50):
            try:
                reader, writer = await asyncio.open_connection("127.0.0.1", listen_port)
                break
            except OSError:
                await asyncio.sleep(0.02)
        writer.write(b"GET /healthz")
        await writer.drain()
        assert await asyncio.wait_for(reader.read(100), 2) == b"echo:GET /healthz"
        writer.close()
    finally:
        task.cancel()
        upstream.close()
        await upstream.wait_closed()


async def test_forwarder_answers_502_when_edge_down():
    probe = await asyncio.start_server(lambda r, w: None, "127.0.0.1", 0)
    dead_port = probe.sockets[0].getsockname()[1]
    probe.close()
    await probe.wait_closed()
    probe2 = await asyncio.start_server(lambda r, w: None, "127.0.0.1", 0)
    listen_port = probe2.sockets[0].getsockname()[1]
    probe2.close()
    await probe2.wait_closed()
    task = start_edge_forwarder(listen_port, "127.0.0.1", dead_port)
    try:
        for _ in range(50):
            try:
                reader, writer = await asyncio.open_connection("127.0.0.1", listen_port)
                break
            except OSError:
                await asyncio.sleep(0.02)
        assert (await asyncio.wait_for(reader.read(100), 2)).startswith(b"HTTP/1.1 502")
        writer.close()
    finally:
        task.cancel()


# ── edge provider error mapping ────────────────────────────────────────────


def _provider(handler):
    from gateway.inbound_edge.edge_app import EdgeSettings, GatewayBackedProvider, GatewayClient

    settings = EdgeSettings(
        public_url="https://e.test", gateway_url="http://g", service_token="s" * 40
    )
    gw = GatewayClient(settings, transport=httpx.MockTransport(handler))
    return GatewayBackedProvider(gw, settings), gw


def _err(status, **error):
    return lambda request: httpx.Response(status, json={"error": error})


async def test_gateway_client_non_json_is_error():
    from gateway.inbound_edge.edge_app import GatewayError

    provider, gw = _provider(lambda r: httpx.Response(502, content=b"<html>"))
    with pytest.raises(GatewayError):
        await gw.call("keys")
    await gw.aclose()


async def test_register_and_authorize_errors_map_to_oauth_codes():
    from mcp.server.auth.provider import AuthorizeError, RegistrationError
    from mcp.shared.auth import OAuthClientInformationFull

    provider, gw = _provider(_err(400, code="oauth", oauth_error="weird", message="m"))
    info = OAuthClientInformationFull(client_id="c", redirect_uris=["https://x/cb"])
    with pytest.raises(RegistrationError) as reg:
        await provider.register_client(info)
    assert reg.value.error == "invalid_client_metadata"
    params = SimpleNamespace(
        state=None,
        scopes=None,
        code_challenge="x",
        redirect_uri="https://x/cb",
        redirect_uri_provided_explicitly=True,
        resource=None,
    )
    with pytest.raises(AuthorizeError) as auth:
        await provider.authorize(info, params)
    assert auth.value.error == "server_error"
    await gw.aclose()


async def test_token_errors_and_foreign_resource():
    from mcp.server.auth.provider import AuthorizationCode, RefreshToken, TokenError
    from mcp.shared.auth import OAuthClientInformationFull

    provider, gw = _provider(_err(400, code="oauth", oauth_error="odd", message="m"))
    client = OAuthClientInformationFull(client_id="c", redirect_uris=["https://x/cb"])
    code = AuthorizationCode(
        code="k",
        scopes=[],
        expires_at=0,
        client_id="c",
        code_challenge="x",
        redirect_uri="https://x/cb",
        redirect_uri_provided_explicitly=True,
        resource="https://elsewhere/mcp",
    )
    with pytest.raises(TokenError) as wrong:
        await provider.exchange_authorization_code(client, code)
    assert wrong.value.error == "invalid_target"
    with pytest.raises(TokenError) as grant:
        await provider.exchange_refresh_token(
            client, RefreshToken(token="r", client_id="c", scopes=[]), []
        )
    assert grant.value.error == "invalid_grant"
    with pytest.raises(TokenError):
        await provider.exchange_identity_assertion()
    await gw.aclose()


async def test_issuer_mismatch_refuses_keys():
    provider, gw = _provider(
        lambda r: httpx.Response(
            200, json={"result": {"issuer": "https://other", "public_key_pem": "x"}}
        )
    )
    with pytest.raises(RuntimeError, match="issuer"):
        await provider.ensure_keys()
    await gw.aclose()


async def test_loaders_return_none_and_revoke_passes_token():
    seen = []

    def handler(request):
        body = json.loads(request.content)
        seen.append(body)
        return httpx.Response(200, json={"result": None})

    from mcp.shared.auth import OAuthClientInformationFull

    provider, gw = _provider(handler)
    client = OAuthClientInformationFull(client_id="c", redirect_uris=["https://x/cb"])
    assert await provider.get_client("c") is None
    assert await provider.load_authorization_code(client, "k") is None
    assert await provider.load_refresh_token(client, "r") is None
    await provider.revoke_token(SimpleNamespace(token="tok"))
    assert seen[-1] == {"method": "oauth.revoke", "params": {"token": "tok"}}
    await gw.aclose()


async def test_consent_route_error_paths():
    from gateway.inbound_edge.edge_app import EdgeGuard, EdgeSettings, create_app

    calls = []

    def handler(request):
        body = json.loads(request.content)
        calls.append(body["method"])
        if body["method"] == "oauth.consent_view":
            if body["params"]["request_id"] == "gone":
                return httpx.Response(200, json={"result": None})
            return httpx.Response(
                200,
                json={
                    "result": {
                        "vendor": "poke",
                        "vendor_display": "<b>Poke</b>",
                        "redirect_host": "p",
                    }
                },
            )
        if body["params"]["request_id"] == "old":
            return httpx.Response(
                400, json={"error": {"code": "oauth", "message": "authorisation request expired"}}
            )
        return httpx.Response(400, json={"error": {"code": "oauth", "message": "wrong"}})

    app = create_app(
        EdgeSettings(public_url="https://e.test", gateway_url="http://g", service_token="s" * 40),
        gateway_transport=httpx.MockTransport(handler),
    )
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="https://e.test"
    ) as c:
        assert (await c.get("/oauth/consent")).status_code == 400
        assert (await c.get("/oauth/consent?req=gone")).status_code == 400
        page = await c.get("/oauth/consent?req=ok")
        assert "&lt;b&gt;Poke&lt;/b&gt;" in page.text and "<b>Poke</b>" not in page.text
        wrong = await c.post("/oauth/consent", data={"req": "ok", "code": "zzzzzzzz"})
        assert wrong.status_code == 200 and "wrong or expired" in wrong.text
        old = await c.post("/oauth/consent", data={"req": "old", "code": "zzzzzzzz"})
        assert old.status_code == 400
        assert (await c.get("/healthz")).json() == {"status": "ok"}
    assert isinstance(app, EdgeGuard)
    await app.gateway.aclose()


def test_settings_from_env(tmp_path, monkeypatch):
    from gateway.inbound_edge.edge_app import settings_from_env

    (tmp_path / "tok").write_text("abc\n")
    monkeypatch.setenv("EDGE_SERVICE_TOKEN_FILE", str(tmp_path / "tok"))
    monkeypatch.setenv("EDGE_PUBLIC_URL", "https://e.test/")
    s = settings_from_env()
    assert s.public_url == "https://e.test" and s.service_token == "abc"
    assert s.resource == "https://e.test/mcp"


# ── descriptors CLI verify path ────────────────────────────────────────────


def test_cli_verify_ok_and_bad_stdin(signed_descriptors, capsys):
    assert d.main(["verify"]) == 0
    assert "verify: OK" in capsys.readouterr().out
    assert d.main(["sign"], stdin=io.StringIO("not base64!!\n")) == 1
    d.verify_shipped_descriptors()


def test_unreadable_public_key_refuses():
    with pytest.raises(d.DescriptorIntegrityError, match="unreadable"):
        d.verify_descriptors(d.build_manifest(), "AAAA", b"not a pem", d.TOOL_DESCRIPTORS)
