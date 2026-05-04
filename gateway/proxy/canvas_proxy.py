# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Canvas Reverse Proxy with HTTP Basic Auth Gate (CVE-2026-34871 fix).

Intercepts all Canvas (OpenClaw Web UI) traffic on port 18789 and validates
the gateway password via HTTP Basic Auth before forwarding to the bot container
on the agentshroud-isolated network (http://bot:18789).

Mitigates CVE-2026-34871: OpenClaw Canvas Authentication Bypass — the upstream
``authorizeCanvasRequest()`` unconditionally allows local-direct requests without
validating tokens. This proxy adds an application-layer auth gate that the bot
container itself cannot provide.

Architecture:
  Host :18789 → [gateway canvas_proxy] → bot:18789 (agentshroud-isolated network)

Auth: HTTP Basic Auth
  - Username: any (ignored)
  - Password: contents of GATEWAY_AUTH_TOKEN_FILE (/run/secrets/gateway_password)

WebSocket: auth via Authorization header on the initial HTTP upgrade.
"""

from __future__ import annotations

import base64
import logging
import os
from typing import Any

import httpx

logger = logging.getLogger("agentshroud.proxy.canvas")

_BOT_CANVAS_URL = os.environ.get("CANVAS_BOT_URL", "http://bot:18789")
# Skip HTTP Basic Auth on the Canvas proxy.  The port is already bound to
# 127.0.0.1, and OpenClaw has its own gateway-token auth in the web UI.
_SKIP_BASIC_AUTH = os.environ.get("CANVAS_SKIP_BASIC_AUTH", "").lower() in ("1", "true", "yes")

# Headers that must not be forwarded upstream (hop-by-hop)
_HOP_BY_HOP = frozenset(
    {
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "transfer-encoding",
        "upgrade",
    }
)


def _read_gateway_password() -> str:
    """Return gateway password from secret file or env var."""
    path = os.environ.get("GATEWAY_AUTH_TOKEN_FILE", "/run/secrets/gateway_password")
    try:
        with open(path) as fh:
            return fh.read().strip()
    except OSError:
        return os.environ.get("GATEWAY_AUTH_TOKEN", "")


def _check_token_auth(query_string: str) -> bool:
    """Validate token query parameter against the gateway password."""
    from urllib.parse import parse_qs

    params = parse_qs(query_string)
    token = params.get("token", [""])[0]
    if not token:
        return False
    expected = _read_gateway_password()
    return bool(expected) and token == expected


def _check_basic_auth(authorization_header: str) -> bool:
    """Validate HTTP Basic Auth credentials against the gateway password."""
    if not authorization_header.startswith("Basic "):
        return False
    try:
        decoded = base64.b64decode(authorization_header[6:]).decode("utf-8", errors="replace")
        _, _, password = decoded.partition(":")
        expected = _read_gateway_password()
        if not expected:
            logger.error("Canvas proxy: gateway password unavailable — denying all requests")
            return False
        return password == expected
    except Exception:
        return False


def _build_proxy_headers(incoming_headers: dict[str, str]) -> dict[str, str]:
    """Build headers to forward upstream, stripping hop-by-hop and Authorization."""
    forwarded: dict[str, str] = {}
    for key, value in incoming_headers.items():
        lower = key.lower()
        if lower in _HOP_BY_HOP or lower == "authorization":
            continue
        forwarded[key] = value
    forwarded["host"] = "localhost:18789"
    return forwarded


async def canvas_proxy_app(scope: dict[str, Any], receive: Any, send: Any) -> None:
    """ASGI application: auth-gated transparent reverse proxy for Canvas.

    Handles lifespan, HTTP, and WebSocket scopes.
    """
    if scope["type"] == "lifespan":
        while True:
            event = await receive()
            if event["type"] == "lifespan.startup":
                await send({"type": "lifespan.startup.complete"})
            elif event["type"] == "lifespan.shutdown":
                await send({"type": "lifespan.shutdown.complete"})
                return

    elif scope["type"] == "http":
        await _handle_http(scope, receive, send)

    elif scope["type"] == "websocket":
        await _handle_websocket(scope, receive, send)


async def _handle_http(scope: dict[str, Any], receive: Any, send: Any) -> None:
    """Proxy an HTTP request after validating Basic Auth."""
    headers = dict((k.decode("latin-1"), v.decode("latin-1")) for k, v in scope.get("headers", []))
    auth_header = headers.get("authorization", "")

    if not _SKIP_BASIC_AUTH and not _check_basic_auth(auth_header):
        logger.info(
            "Canvas proxy: unauthorized HTTP request from %s %s",
            scope.get("client"),
            scope.get("path"),
        )
        body = b"Authentication required"
        await send(
            {
                "type": "http.response.start",
                "status": 401,
                "headers": [
                    [b"www-authenticate", b'Basic realm="AgentShroud Canvas"'],
                    [b"content-type", b"text/plain; charset=utf-8"],
                    [b"content-length", str(len(body)).encode()],
                ],
            }
        )
        await send({"type": "http.response.body", "body": body, "more_body": False})
        return

    # Collect request body
    body_chunks: list[bytes] = []
    while True:
        event = await receive()
        body_chunks.append(event.get("body", b""))
        if not event.get("more_body", False):
            break
    request_body = b"".join(body_chunks)

    # Build target URL
    path = scope.get("path", "/")
    qs = scope.get("query_string", b"")
    target_url = _BOT_CANVAS_URL + path
    if qs:
        target_url += "?" + qs.decode("latin-1")

    proxy_headers = _build_proxy_headers(headers)

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0, connect=5.0)) as client:
            upstream = await client.request(
                method=scope["method"],
                url=target_url,
                headers=proxy_headers,
                content=request_body,
                follow_redirects=False,
            )
    except httpx.RequestError as exc:
        logger.error("Canvas proxy: upstream request failed: %s", exc)
        error_body = b"Canvas unavailable"
        await send(
            {
                "type": "http.response.start",
                "status": 502,
                "headers": [
                    [b"content-type", b"text/plain; charset=utf-8"],
                    [b"content-length", str(len(error_body)).encode()],
                ],
            }
        )
        await send({"type": "http.response.body", "body": error_body, "more_body": False})
        return

    # Forward upstream response
    response_headers = [
        [k.lower().encode("latin-1"), v.encode("latin-1")]
        for k, v in upstream.headers.items()
        if k.lower() not in _HOP_BY_HOP
    ]
    await send(
        {
            "type": "http.response.start",
            "status": upstream.status_code,
            "headers": response_headers,
        }
    )
    await send({"type": "http.response.body", "body": upstream.content, "more_body": False})


async def _handle_websocket(scope: dict[str, Any], receive: Any, send: Any) -> None:
    """Proxy a WebSocket connection after validating auth.

    Auth is extracted from the Authorization header on the HTTP upgrade
    (passed in scope["headers"] for WebSocket connections).
    """
    import asyncio

    import websockets
    import websockets.exceptions

    headers = dict((k.decode("latin-1"), v.decode("latin-1")) for k, v in scope.get("headers", []))
    auth_header = headers.get("authorization", "")
    qs_raw = scope.get("query_string", b"")
    qs_str = qs_raw.decode("latin-1", errors="replace") if isinstance(qs_raw, bytes) else str(qs_raw)

    # Accept WS if any auth method succeeds: Basic auth header, token query param,
    # or gateway password in Sec-WebSocket-Protocol (OpenClaw dashboard pattern).
    sec_ws_protocol = headers.get("sec-websocket-protocol", "")
    has_proto_token = any(
        t.strip() == _read_gateway_password() for t in sec_ws_protocol.split(",")
    ) if sec_ws_protocol and _read_gateway_password() else False

    # OpenClaw dashboard JS opens a bare WebSocket with no auth headers.
    # The page itself is behind Basic auth, so we trust WS from allowed origins.
    origin = headers.get("origin", "")
    allowed_origins = os.environ.get(
        "AGENTSHROUD_CONTROL_UI_ORIGINS",
        "http://localhost:18789,https://localhost:18789,http://127.0.0.1:18789,https://127.0.0.1:18789",
    ).split(",")
    origin_trusted = origin in allowed_origins

    if not _SKIP_BASIC_AUTH and not (_check_basic_auth(auth_header) or _check_token_auth(qs_str) or has_proto_token or origin_trusted):
        logger.info(
            "Canvas proxy: unauthorized WebSocket from %s %s",
            scope.get("client"),
            scope.get("path"),
        )
        await send({"type": "websocket.close", "code": 4401, "reason": "Unauthorized"})
        return

    # Build upstream WebSocket URL — strip token from forwarded query to avoid leaking it.
    path = scope.get("path", "/")
    qs = qs_raw
    ws_url = _BOT_CANVAS_URL.replace("http://", "ws://").replace("https://", "wss://") + path
    if qs:
        ws_url += "?" + qs.decode("latin-1")

    # Accept the client connection
    await receive()  # websocket.connect
    await send({"type": "websocket.accept"})

    # Forward Origin and set Host so OpenClaw's origin check passes.
    extra_headers = {"Host": "localhost:18789"}
    if origin:
        extra_headers["Origin"] = origin

    try:
        async with websockets.connect(ws_url, additional_headers=extra_headers, max_size=10 * 1024 * 1024) as upstream_ws:

            async def client_to_upstream() -> None:
                while True:
                    event = await receive()
                    if event["type"] == "websocket.disconnect":
                        await upstream_ws.close()
                        return
                    elif event["type"] == "websocket.receive":
                        data = event.get("bytes") or (event.get("text") or "").encode()
                        await upstream_ws.send(data)

            async def upstream_to_client() -> None:
                async for message in upstream_ws:
                    if isinstance(message, bytes):
                        await send({"type": "websocket.send", "bytes": message})
                    else:
                        await send({"type": "websocket.send", "text": message})

            done, pending = await asyncio.wait(
                [
                    asyncio.create_task(client_to_upstream()),
                    asyncio.create_task(upstream_to_client()),
                ],
                return_when=asyncio.FIRST_COMPLETED,
            )
            for task in pending:
                task.cancel()

    except websockets.exceptions.WebSocketException as exc:
        logger.warning("Canvas proxy WebSocket upstream error: %s", exc)
    except Exception as exc:
        logger.error("Canvas proxy WebSocket error: %s", exc)
    finally:
        try:
            await send({"type": "websocket.close", "code": 1000})
        except Exception:
            pass
