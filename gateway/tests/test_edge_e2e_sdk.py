# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""End to end with the official MCP SDK client (SCRUM-218).

SDK client ──httpx2 ASGI──► edge app (SDK server + OAuth routes + EdgeGuard)
                              ──httpx ASGI──► gateway /edge/v1/rpc ──► real pipeline.

Covers: RFC 9728/8414 discovery, dynamic registration inside an enrollment window,
PKCE, owner consent with the one-time code, token exchange bound to the resource,
tools/list, a read call, and a write call that returns an approval ticket.
"""

from contextlib import asynccontextmanager
from urllib.parse import parse_qs, urlparse

import httpx
import httpx2
from fastapi import FastAPI
from mcp.client.auth import OAuthClientProvider
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.shared.auth import AuthorizationCodeResult, OAuthClientMetadata

from gateway.approval_queue.enhanced_queue import EnhancedApprovalQueue
from gateway.approval_queue.store import ApprovalStore
from gateway.inbound_edge import profiles as p
from gateway.inbound_edge.approvals import EdgeApprovals
from gateway.inbound_edge.call_pipeline import EdgeCallPipeline, EdgeDeps
from gateway.inbound_edge.edge_app import EdgeSettings, create_app
from gateway.inbound_edge.edge_jwt import TokenService, generate_signing_key_pem
from gateway.inbound_edge.oauth_service import EdgeOAuthService, derive_seal_key
from gateway.inbound_edge.routes import router as edge_router
from gateway.inbound_edge.service import EdgeService
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.config import ApprovalQueueConfig, PIIConfig, ToolRiskConfig
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.security.audit_store import AuditStore
from gateway.security.canary_tripwire import CanaryTripwire
from gateway.security.encoding_detector import EncodingDetector
from gateway.security.mfa_guard import MFAGuard
from gateway.security.progressive_lockdown import ProgressiveLockdown
from gateway.security.prompt_guard import PromptGuard

PUBLIC = "https://edge.test"
CALLBACK = "https://claude.ai/api/mcp/auth_callback"
SERVICE_TOKEN = "s" * 48


class Facade:
    def __init__(self, name, result, target="fake", requires_local_agent=None):
        self.name, self.result, self.target = name, result, target
        self.requires_local_agent = requires_local_agent
        self.calls = []

    async def run(self, args, call):
        self.calls.append(args)
        return dict(self.result)


class MemoryTokenStorage:
    def __init__(self):
        self.tokens = None
        self.client_info = None

    async def get_tokens(self):
        return self.tokens

    async def set_tokens(self, tokens):
        self.tokens = tokens

    async def get_client_info(self):
        return self.client_info

    async def set_client_info(self, client_info):
        self.client_info = client_info


@asynccontextmanager
async def stack(tmp_path):
    key = generate_signing_key_pem()
    store = EdgeStore(tmp_path / "edge.db", seal_key=derive_seal_key(key))
    await store.init()
    tokens = TokenService(store, key, PUBLIC, PUBLIC + "/mcp")
    profile = p.VendorProfile(
        vendor="claude-duet",
        display_name="Claude Duet",
        enabled=True,
        mode="enforce",
        oauth=True,
        dynamic_registration=True,
        redirect_uris=(CALLBACK,),
        static_bearer=False,
        tools={"lab_search": "read", "delegate_to_hermes": "write"},
        per_client_per_minute=30,
        per_vendor_per_minute=60,
        max_concurrency=4,
        daily_calls=500,
        daily_delegations=20,
        dlp_mode="redact",
        dlp_min_confidence=0.9,
        max_response_bytes=1_048_576,
    )
    queue = EnhancedApprovalQueue(
        ApprovalQueueConfig(),
        ToolRiskConfig(),
        store=ApprovalStore(tmp_path / "approvals.db"),
        mfa_guard=MFAGuard(secret_b32="", enabled=False),
    )
    await queue.initialize()
    audit = AuditStore(tmp_path / "audit.db")
    await audit.initialize()

    async def emit(event):
        pass

    facades = {
        "lab_search": Facade("lab_search", {"results": [{"title": "sunny"}]}),
        "delegate_to_hermes": Facade(
            "delegate_to_hermes", {"reply": "ok"}, "hermes:edge-delegate", "hermes"
        ),
    }
    approvals = EdgeApprovals(store, queue)
    pipeline = EdgeCallPipeline(
        EdgeDeps(
            profiles={"claude-duet": profile},
            tokens=tokens,
            store=store,
            approvals=approvals,
            audit=audit,
            emit=emit,
            prompt_guard=PromptGuard(),
            encoding_detector=EncodingDetector(),
            lockdown=ProgressiveLockdown(),
            tripwire=CanaryTripwire(),
            sanitizer=PIISanitizer(PIIConfig()),
            facades=facades,
            local_agents={"hermes"},
        )
    )
    service = EdgeService(
        store=store,
        tokens=tokens,
        oauth=EdgeOAuthService(store, tokens, {"claude-duet": profile}, PUBLIC, PUBLIC + "/mcp"),
        approvals=approvals,
        pipeline=pipeline,
        service_token=SERVICE_TOKEN,
        issuer=PUBLIC,
        resource=PUBLIC + "/mcp",
    )
    from gateway.ingest_api.state import app_state

    previous = getattr(app_state, "inbound_edge", None)
    app_state.inbound_edge = service
    gateway = FastAPI()
    gateway.include_router(edge_router)
    edge = create_app(
        EdgeSettings(public_url=PUBLIC, gateway_url="http://gateway", service_token=SERVICE_TOKEN),
        gateway_transport=httpx.ASGITransport(app=gateway),
    )
    try:
        async with edge.app.router.lifespan_context(edge.app):
            yield edge, service, facades, queue
    finally:
        app_state.inbound_edge = previous
        await edge.gateway.aclose()
        await queue.close()
        await audit.close()
        await store.close()


def _client(edge, **kw):
    return httpx2.AsyncClient(transport=httpx2.ASGITransport(app=edge), base_url=PUBLIC, **kw)


async def test_full_oauth_and_tool_calls_with_sdk_client(tmp_path):
    async with stack(tmp_path) as (edge, service, facades, queue):
        enrollment = await service.store.open_enrollment("claude-duet", ttl_s=600)
        captured = {}

        async def redirect_handler(url: str) -> None:
            async with _client(edge) as browser:
                r = await browser.get(url)
                assert r.status_code == 302
                consent = r.headers["location"]
                page = await browser.get(consent)
                assert page.status_code == 200 and "Claude Duet" in page.text
                assert "default-src 'none'" in page.headers["content-security-policy"]
                req = parse_qs(urlparse(consent).query)["req"][0]
                back = await browser.post("/oauth/consent", data={"req": req, "code": enrollment})
                assert back.status_code == 302
                q = parse_qs(urlparse(back.headers["location"]).query)
                captured["code"], captured["state"] = q["code"][0], q.get("state", [None])[0]

        async def callback_handler() -> AuthorizationCodeResult:
            return AuthorizationCodeResult(code=captured["code"], state=captured["state"])

        auth = OAuthClientProvider(
            server_url=PUBLIC + "/mcp",
            client_metadata=OAuthClientMetadata(
                client_name="Claude",
                redirect_uris=[CALLBACK],
                grant_types=["authorization_code", "refresh_token"],
                response_types=["code"],
                scope="mcp",
            ),
            storage=MemoryTokenStorage(),
            redirect_handler=redirect_handler,
            callback_handler=callback_handler,
        )
        async with _client(edge, auth=auth) as http:
            async with streamable_http_client(PUBLIC + "/mcp", http_client=http) as streams:
                async with ClientSession(streams[0], streams[1]) as session:
                    await session.initialize()
                    tools = await session.list_tools()
                    names = sorted(t.name for t in tools.tools)
                    assert names == ["delegate_to_hermes", "lab_search"]

                    read = await session.call_tool("lab_search", {"query": "weather"})
                    assert not read.is_error
                    assert read.structured_content["results"][0]["title"] == "sunny"

                    write = await session.call_tool(
                        "delegate_to_hermes", {"task": "tidy notes", "priority": "low"}
                    )
                    assert not write.is_error
                    pending = write.structured_content
                    assert pending["status"] == "awaiting_human_approval"
                    assert facades["delegate_to_hermes"].calls == []

                    await queue.decide(pending["approval_request_id"], True, decided_by="owner")
                    done = await session.call_tool(
                        "delegate_to_hermes",
                        {
                            "task": "tidy notes",
                            "priority": "low",
                            "approval_ticket": pending["approval_ticket"],
                        },
                    )
                    assert not done.is_error and done.structured_content == {"reply": "ok"}
        clients = await service.store.list_clients()
        assert [c["vendor"] for c in clients] == ["claude-duet"]


async def test_registration_refused_without_enrollment_window(tmp_path):
    async with stack(tmp_path) as (edge, *_):
        async with _client(edge) as http:
            r = await http.post(
                "/register",
                json={
                    "redirect_uris": [CALLBACK],
                    "client_name": "x",
                    "token_endpoint_auth_method": "none",
                },
            )
        assert r.status_code == 400
        assert "enrollment" in r.text


async def test_edge_guard(tmp_path):
    async with stack(tmp_path) as (edge, *_):
        async with _client(edge) as http:
            for path in ("/soc/v1/health", "/edge/v1/rpc", "/v1/chat/completions", "/forward", "/"):
                assert (await http.get(path)).status_code == 404, path
            assert (await http.post("/mcp", content=b"[" + b" " * 10 + b"]")).status_code == 400
            big = b"{" + b" " * (64 * 1024) + b"}"
            assert (await http.post("/mcp", content=big)).status_code == 413
            unauth = await http.post(
                "/mcp",
                json={"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
                headers={"accept": "application/json, text/event-stream"},
            )
            assert unauth.status_code == 401
            assert "resource_metadata" in unauth.headers.get("www-authenticate", "")
            meta = await http.get("/.well-known/oauth-protected-resource/mcp")
            assert meta.status_code == 200 and meta.json()["resource"] == PUBLIC + "/mcp"
            asm = await http.get("/.well-known/oauth-authorization-server")
            assert asm.json()["code_challenge_methods_supported"] == ["S256"]


async def test_gateway_rpc_requires_service_token(tmp_path):
    async with stack(tmp_path):
        gateway = FastAPI()
        gateway.include_router(edge_router)
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=gateway), base_url="http://gw"
        ) as c:
            assert (await c.post("/edge/v1/rpc", json={"method": "keys"})).status_code == 401
            bad = await c.post(
                "/edge/v1/rpc", json={"method": "keys"}, headers={"X-Edge-Service-Token": "x" * 48}
            )
            assert bad.status_code == 401
            ok = await c.post(
                "/edge/v1/rpc",
                json={"method": "keys"},
                headers={"X-Edge-Service-Token": SERVICE_TOKEN},
            )
            assert (
                ok.status_code == 200
                and "BEGIN PUBLIC KEY" in ok.json()["result"]["public_key_pem"]
            )
            nope = await c.post(
                "/edge/v1/rpc",
                json={"method": "store.kill"},
                headers={"X-Edge-Service-Token": SERVICE_TOKEN},
            )
            assert nope.status_code == 404
