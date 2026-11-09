# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""The internet-facing ``agentshroud-mcp-edge`` container (SCRUM-215).

A protocol terminator and nothing more. It runs the official MCP Python SDK
(Streamable HTTP, spec 2026-07-28 plus the SDK's legacy revisions, stateless, JSON
responses) and the SDK's OAuth 2.1 routes, and forwards every decision to the
gateway over ``POST /edge/v1/rpc``. It holds no signing key, no policy and no
state: compromising it yields the public key and a service token that opens only
that one RPC door.

Before the SDK sees a byte, :class:`EdgeGuard` enforces a fixed route allowlist, a
request-size cap and single-message JSON-RPC bodies. Exposed routes — and nothing
else, so the Command Center and every gateway API stay tailnet-only:

    POST /mcp                                  MCP endpoint
    GET  /.well-known/oauth-protected-resource[/mcp]   RFC 9728
    GET  /.well-known/oauth-authorization-server       RFC 8414
    GET  /authorize, POST /token, /register, /revoke   OAuth 2.1
    GET|POST /oauth/consent                    owner consent (enrollment code)
    GET  /healthz                              liveness

Run: ``python -m gateway.inbound_edge.edge_app`` (see docker/mcp-edge/Dockerfile).
"""

import html
import logging
import os
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

import httpx
import mcp_types as types
from mcp.server.auth.middleware.auth_context import get_access_token
from mcp.server.auth.provider import (
    AccessToken,
    AuthorizationCode,
    AuthorizationParams,
    AuthorizeError,
    ProviderTokenVerifier,
    RefreshToken,
    RegistrationError,
    TokenError,
)
from mcp.server.auth.settings import AuthSettings, ClientRegistrationOptions, RevocationOptions
from mcp.server.lowlevel import Server
from mcp.server.transport_security import TransportSecuritySettings
from mcp.shared.auth import OAuthClientInformationFull, OAuthToken
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse
from starlette.routing import Route

from gateway.inbound_edge.edge_jwt import TokenRejected, verify_signature_only

logger = logging.getLogger("agentshroud.inbound_edge.edge_app")

MAX_REQUEST_BYTES = 64 * 1024
SERVICE_HEADER = "X-Edge-Service-Token"
_EXACT_PATHS = {
    "/mcp",
    "/authorize",
    "/token",
    "/register",
    "/revoke",
    "/oauth/consent",
    "/healthz",
    "/.well-known/oauth-authorization-server",
    "/.well-known/oauth-protected-resource",
    "/.well-known/oauth-protected-resource/mcp",
}


@dataclass(frozen=True)
class EdgeSettings:
    public_url: str  # https://<node>.ts.net:8443 — OAuth issuer and origin
    gateway_url: str  # http://agentshroud-gateway:8080 (DMZ)
    service_token: str
    internal_hosts: tuple = ("agentshroud-mcp-edge:8443", "127.0.0.1:8443", "localhost:8443")

    @property
    def resource(self) -> str:
        return f"{self.public_url}/mcp"


class GatewayError(Exception):
    def __init__(self, status: int, error: Dict[str, Any]):
        super().__init__(error.get("message") or error.get("code"))
        self.status = status
        self.error = error


class GatewayClient:
    """The edge's only client: the gateway's /edge/v1/rpc door."""

    def __init__(
        self, settings: EdgeSettings, transport: Optional[httpx.AsyncBaseTransport] = None
    ):
        self._settings = settings
        self._client = httpx.AsyncClient(
            base_url=settings.gateway_url,
            transport=transport,
            timeout=httpx.Timeout(connect=5.0, read=200.0, write=10.0, pool=5.0),
            headers={SERVICE_HEADER: settings.service_token},
            trust_env=False,
        )

    async def call(self, method: str, **params: Any) -> Any:
        resp = await self._client.post("/edge/v1/rpc", json={"method": method, "params": params})
        try:
            body = resp.json()
        except ValueError:
            raise GatewayError(resp.status_code, {"code": "bad_gateway"})
        if resp.status_code != 200 or "error" in body:
            raise GatewayError(resp.status_code, body.get("error") or {"code": "bad_gateway"})
        return body["result"]

    async def aclose(self) -> None:
        await self._client.aclose()


class GatewayBackedProvider:
    """``OAuthAuthorizationServerProvider`` whose every decision is made by the gateway."""

    def __init__(self, gw: GatewayClient, settings: EdgeSettings):
        self.gw = gw
        self.settings = settings
        self.public_key_pem: Optional[bytes] = None

    async def ensure_keys(self) -> None:
        if self.public_key_pem is None:
            keys = await self.gw.call("keys")
            if keys["issuer"] != self.settings.public_url:
                raise RuntimeError("gateway issuer does not match EDGE_PUBLIC_URL")
            self.public_key_pem = keys["public_key_pem"].encode()

    @staticmethod
    def _oauth_code(exc: GatewayError) -> str:
        return exc.error.get("oauth_error") or "invalid_request"

    async def get_client(self, client_id: str) -> Optional[OAuthClientInformationFull]:
        info = await self.gw.call("oauth.get_client", client_id=client_id)
        if info is None:
            return None
        info = {k: v for k, v in info.items() if k != "vendor"}
        return OAuthClientInformationFull.model_validate(info)

    async def register_client(self, client_info: OAuthClientInformationFull) -> None:
        try:
            await self.gw.call(
                "oauth.register_client", info=client_info.model_dump(mode="json", exclude_none=True)
            )
        except GatewayError as exc:
            code = self._oauth_code(exc)
            if code not in ("invalid_redirect_uri", "invalid_client_metadata"):
                code = "invalid_client_metadata"
            raise RegistrationError(code, exc.error.get("message"))

    async def authorize(
        self, client: OAuthClientInformationFull, params: AuthorizationParams
    ) -> str:
        try:
            return await self.gw.call(
                "oauth.authorize",
                client_id=client.client_id,
                params={
                    "state": params.state,
                    "scopes": params.scopes or [],
                    "code_challenge": params.code_challenge,
                    "redirect_uri": str(params.redirect_uri),
                    "redirect_uri_provided_explicitly": params.redirect_uri_provided_explicitly,
                    "resource": params.resource,
                },
            )
        except GatewayError as exc:
            code = self._oauth_code(exc)
            if code not in ("invalid_target", "unauthorized_client", "access_denied"):
                code = "server_error"
            raise AuthorizeError(code, exc.error.get("message"))

    async def load_authorization_code(
        self, client: OAuthClientInformationFull, authorization_code: str
    ) -> Optional[AuthorizationCode]:
        data = await self.gw.call(
            "oauth.load_code", client_id=client.client_id, code=authorization_code
        )
        if data is None:
            return None
        return AuthorizationCode(
            code=authorization_code,
            scopes=data["scopes"],
            expires_at=data["expires_at"],
            client_id=client.client_id,
            code_challenge=data["code_challenge"],
            redirect_uri=data["redirect_uri"],
            redirect_uri_provided_explicitly=data["redirect_uri_provided_explicitly"],
            resource=data.get("resource"),
        )

    async def _token(self, method: str, **params: Any) -> OAuthToken:
        try:
            return OAuthToken.model_validate(await self.gw.call(method, **params))
        except GatewayError as exc:
            code = self._oauth_code(exc)
            if code not in ("invalid_grant", "invalid_scope", "invalid_target", "invalid_client"):
                code = "invalid_grant"
            raise TokenError(code, exc.error.get("message"))

    async def exchange_authorization_code(
        self, client: OAuthClientInformationFull, authorization_code: AuthorizationCode
    ) -> OAuthToken:
        if authorization_code.resource not in (None, self.settings.resource):
            raise TokenError("invalid_target", "token requested for a different resource")
        return await self._token(
            "oauth.exchange_code", client_id=client.client_id, code=authorization_code.code
        )

    async def load_refresh_token(
        self, client: OAuthClientInformationFull, refresh_token: str
    ) -> Optional[RefreshToken]:
        data = await self.gw.call(
            "oauth.load_refresh", client_id=client.client_id, token=refresh_token
        )
        if data is None:
            return None
        return RefreshToken(
            token=refresh_token,
            client_id=client.client_id,
            scopes=data["scopes"],
            resource=self.settings.resource,
        )

    async def exchange_refresh_token(
        self, client: OAuthClientInformationFull, refresh_token: RefreshToken, scopes: List[str]
    ) -> OAuthToken:
        return await self._token(
            "oauth.exchange_refresh",
            client_id=client.client_id,
            token=refresh_token.token,
            scopes=scopes,
        )

    async def load_access_token(self, token: str) -> Optional[AccessToken]:
        """Cheap local pre-screen; the gateway re-verifies on every tools call."""
        await self.ensure_keys()
        try:
            claims = verify_signature_only(
                token, self.public_key_pem, self.settings.public_url, self.settings.resource
            )
        except TokenRejected:
            return None
        return AccessToken(
            token=token,
            client_id=str(claims["client_id"]),
            scopes=str(claims.get("scope", "")).split(),
            expires_at=int(claims["exp"]),
            resource=self.settings.resource,
            subject=str(claims["sub"]),
            claims={"iss": claims["iss"]},
        )

    async def revoke_token(self, token: Any) -> None:
        await self.gw.call("oauth.revoke", token=getattr(token, "token", token))

    async def exchange_identity_assertion(self, *args: Any, **kwargs: Any) -> OAuthToken:
        raise TokenError("unsupported_grant_type", "identity assertion grants are not accepted")


_CONSENT_PAGE = """<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AgentShroud — link {vendor}</title>
<style>body{{font:16px system-ui;max-width:32rem;margin:3rem auto;padding:0 1rem}}
input,button{{font:inherit;padding:.5rem}}</style></head><body>
<h1>Link {vendor} to AgentShroud</h1>
<p><b>{vendor}</b> is asking to call your AgentShroud Inbound Edge tools. After you
approve, your browser returns to <b>{host}</b>.</p>
<p>Enter the one-time enrollment code from <code>asb edge enroll --vendor {vendor_id}</code>.
Every tool call stays subject to AgentShroud policy, and writes still need your approval.</p>
<form method="post" action="/oauth/consent"><input type="hidden" name="req" value="{req}">
<input name="code" autocomplete="one-time-code" required minlength="8" maxlength="64">
<button type="submit">Link</button></form>{error}</body></html>"""

_CONSENT_HEADERS = {
    "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; frame-ancestors 'none'",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Cache-Control": "no-store",
}


def _consent_routes(gw: GatewayClient) -> List[Route]:
    async def render(req: str, error: str = "") -> HTMLResponse:
        view = await gw.call("oauth.consent_view", request_id=req)
        if view is None:
            return HTMLResponse("Authorisation request expired.", 400, headers=_CONSENT_HEADERS)
        page = _CONSENT_PAGE.format(
            vendor=html.escape(view["vendor_display"]),
            vendor_id=html.escape(view["vendor"]),
            host=html.escape(view["redirect_host"] or "?"),
            req=html.escape(req),
            error=f"<p role='alert'>{html.escape(error)}</p>" if error else "",
        )
        return HTMLResponse(page, headers=_CONSENT_HEADERS)

    async def consent(request: Request):
        if request.method == "GET":
            req = request.query_params.get("req", "")
            if not req or len(req) > 64:
                return PlainTextResponse("bad request", 400, headers=_CONSENT_HEADERS)
            return await render(req)
        form = await request.form()
        req, code = str(form.get("req", ""))[:64], str(form.get("code", ""))[:64]
        try:
            target = await gw.call("oauth.consent_submit", request_id=req, enrollment_code=code)
        except GatewayError as exc:
            if "expired" in str(exc):
                return HTMLResponse("Authorisation request expired.", 400, headers=_CONSENT_HEADERS)
            return await render(req, "That code is wrong or expired.")
        return RedirectResponse(target, status_code=302, headers=_CONSENT_HEADERS)

    async def healthz(request: Request):
        return JSONResponse({"status": "ok"})

    return [
        Route("/oauth/consent", consent, methods=["GET", "POST"]),
        Route("/healthz", healthz, methods=["GET"]),
    ]


def _request_token(ctx) -> Optional[AccessToken]:
    """The bearer token the SDK's auth middleware accepted for this request.

    Stateless Streamable HTTP runs handlers in the session manager's task group, so
    the auth context variable is not always visible; the Starlette request scope is.
    """
    token = get_access_token()
    if token is not None:
        return token
    request = getattr(ctx, "request", None)
    user = request.scope.get("user") if request is not None else None
    return getattr(user, "access_token", None)


def _build_server(gw: GatewayClient) -> Server:
    async def on_list_tools(ctx, params) -> types.ListToolsResult:
        token = _request_token(ctx)
        if token is None:
            raise PermissionError("unauthenticated")
        try:
            tools = await gw.call("tools.list", token=token.token)
        except GatewayError as exc:
            raise PermissionError(exc.error.get("message") or "forbidden")
        return types.ListToolsResult(tools=[types.Tool.model_validate(t) for t in tools])

    async def on_call_tool(ctx, params) -> types.CallToolResult:
        token = _request_token(ctx)
        if token is None:
            raise PermissionError("unauthenticated")
        try:
            result = await gw.call(
                "tools.call",
                token=token.token,
                name=params.name,
                arguments=dict(params.arguments or {}),
                request_id=str(uuid.uuid4()),
            )
        except GatewayError:
            result = {
                "content": [{"type": "text", "text": "denied: gateway error"}],
                "isError": True,
            }
        return types.CallToolResult.model_validate(result)

    return Server(
        "agentshroud-inbound-edge",
        version="1.0.0",
        instructions=(
            "AgentShroud Inbound Edge. Read tools answer directly. Write tools return an "
            "approval ticket first; repeat the identical call with it after the owner approves."
        ),
        on_list_tools=on_list_tools,
        on_call_tool=on_call_tool,
    )


class EdgeGuard:
    """ASGI guard in front of the SDK: route allowlist, size cap, no JSON-RPC batches."""

    def __init__(self, app, max_bytes: int = MAX_REQUEST_BYTES):
        self.app = app
        self.max_bytes = max_bytes

    @staticmethod
    async def _send_plain(send, status: int, text: str) -> None:
        body = text.encode()
        await send(
            {
                "type": "http.response.start",
                "status": status,
                "headers": [
                    (b"content-type", b"text/plain"),
                    (b"content-length", str(len(body)).encode()),
                ],
            }
        )
        await send({"type": "http.response.body", "body": body})

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            return await self.app(scope, receive, send)
        if scope["type"] != "http":
            return await self._send_plain(send, 404, "not found")
        path = scope.get("path", "")
        if path not in _EXACT_PATHS:
            return await self._send_plain(send, 404, "not found")
        for name, value in scope.get("headers", []):
            if name == b"content-length" and value.isdigit() and int(value) > self.max_bytes:
                return await self._send_plain(send, 413, "request too large")

        body = b""
        more = True
        while more:
            message = await receive()
            if message["type"] == "http.disconnect":
                return
            body += message.get("body", b"")
            more = message.get("more_body", False)
            if len(body) > self.max_bytes:
                return await self._send_plain(send, 413, "request too large")
        if path == "/mcp" and scope.get("method") == "POST" and body.lstrip()[:1] == b"[":
            return await self._send_plain(send, 400, "JSON-RPC batches are not accepted")

        replayed = False

        async def replay():
            nonlocal replayed
            if not replayed:
                replayed = True
                return {"type": "http.request", "body": body, "more_body": False}
            return await receive()

        return await self.app(scope, replay, send)


def create_app(
    settings: EdgeSettings, gateway_transport: Optional[httpx.AsyncBaseTransport] = None
):
    gw = GatewayClient(settings, transport=gateway_transport)
    provider = GatewayBackedProvider(gw, settings)
    server = _build_server(gw)
    public = urlparse(settings.public_url)
    hosts = [public.netloc, *settings.internal_hosts]
    app = server.streamable_http_app(
        streamable_http_path="/mcp",
        json_response=True,
        stateless_http=True,
        max_request_body_size=MAX_REQUEST_BYTES,
        transport_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=True,
            allowed_hosts=hosts,
            allowed_origins=[settings.public_url],
        ),
        host="0.0.0.0",  # nosec B104 - container-internal; only reachable via the gateway relay
        auth=AuthSettings(
            issuer_url=settings.public_url,
            resource_server_url=settings.resource,
            client_registration_options=ClientRegistrationOptions(
                enabled=True, valid_scopes=["mcp"], default_scopes=["mcp"]
            ),
            revocation_options=RevocationOptions(enabled=True),
            validate_token_resource=True,
        ),
        auth_server_provider=provider,
        # The low-level app guards /mcp only when a verifier is passed explicitly;
        # with just a provider it serves /mcp unauthenticated (SDK 2.3.0
        # lowlevel/server.py streamable_http_app). Pass it, always.
        token_verifier=ProviderTokenVerifier(provider),
        custom_starlette_routes=_consent_routes(gw),
    )
    guarded = EdgeGuard(app)
    guarded.provider = provider  # type: ignore[attr-defined]
    guarded.gateway = gw  # type: ignore[attr-defined]
    return guarded


def settings_from_env() -> EdgeSettings:
    token = Path(os.environ.get("EDGE_SERVICE_TOKEN_FILE", "/run/secrets/edge_gateway_token"))
    return EdgeSettings(
        public_url=os.environ["EDGE_PUBLIC_URL"].rstrip("/"),
        gateway_url=os.environ.get("EDGE_GATEWAY_URL", "http://agentshroud-gateway:8080"),
        service_token=token.read_text().strip(),
    )


def main() -> None:  # pragma: no cover - container entry point
    import uvicorn

    from gateway.inbound_edge.descriptors import verify_shipped_descriptors

    logging.basicConfig(level=logging.INFO)
    verify_shipped_descriptors()
    uvicorn.run(
        create_app(settings_from_env()),
        host="0.0.0.0",  # nosec B104 - container-internal
        port=int(os.environ.get("EDGE_PORT", "8443")),
        proxy_headers=False,
        server_header=False,
        log_level="info",
    )


if __name__ == "__main__":  # pragma: no cover
    main()
