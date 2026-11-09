# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""``POST /edge/v1/rpc`` — the only door from the edge container into the gateway.

Authenticated by the ``edge_gateway_token`` service secret (constant-time
compare). It exposes a fixed method table — OAuth provider operations and
``tools.list`` / ``tools.call`` — and nothing else: no ``/v1`` model proxy, no
``/forward``, no ``/soc``. The bearer token a hosted agent presented travels as a
parameter so the gateway re-verifies it on every call (kills apply immediately).

Also hosts the tailnet-only owner endpoints used by ``asb edge`` and the Command
Center under ``/soc/v1/edge`` (see gateway/soc/router.py).
"""

import asyncio
import json
import logging
from typing import Any, Awaitable, Callable, Dict

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from gateway.inbound_edge.oauth_service import OAuthFailure

logger = logging.getLogger("agentshroud.inbound_edge.routes")

router = APIRouter(prefix="/edge/v1", tags=["inbound-edge"])

MAX_RPC_BYTES = 256 * 1024
SERVICE_HEADER = "X-Edge-Service-Token"


def _edge():
    from gateway.ingest_api.state import app_state

    return getattr(app_state, "inbound_edge", None)


def _methods(edge) -> Dict[str, Callable[..., Awaitable[Any]]]:
    o, pipe = edge.oauth, edge.pipeline

    async def keys() -> Dict[str, Any]:
        return {
            "public_key_pem": edge.tokens.public_key_pem.decode(),
            "issuer": edge.issuer,
            "resource": edge.resource,
        }

    return {
        "keys": keys,
        "oauth.get_client": o.get_client,
        "oauth.register_client": o.register_client,
        "oauth.authorize": o.authorize,
        "oauth.consent_view": o.consent_view,
        "oauth.consent_submit": o.consent_submit,
        "oauth.load_code": o.load_authorization_code,
        "oauth.exchange_code": o.exchange_authorization_code,
        "oauth.load_refresh": o.load_refresh_token,
        "oauth.exchange_refresh": o.exchange_refresh_token,
        "oauth.load_access": o.load_access_token,
        "oauth.revoke": o.revoke_token,
        "tools.list": pipe.list_tools,
        "tools.call": pipe.call_tool,
    }


@router.post("/rpc")
async def edge_rpc(request: Request) -> JSONResponse:
    edge = _edge()
    if edge is None:
        return JSONResponse({"error": {"code": "edge_disabled"}}, status_code=503)
    if not edge.service_token_ok(request.headers.get(SERVICE_HEADER)):
        logger.warning("edge rpc: bad service token from %s", request.client)
        return JSONResponse({"error": {"code": "unauthorized"}}, status_code=401)
    body = await request.body()
    if len(body) > MAX_RPC_BYTES:
        return JSONResponse({"error": {"code": "too_large"}}, status_code=413)
    try:
        envelope = json.loads(body)
        method = envelope["method"]
        params = envelope.get("params") or {}
        if not isinstance(method, str) or not isinstance(params, dict):
            raise TypeError
    except (ValueError, KeyError, TypeError):
        return JSONResponse({"error": {"code": "bad_request"}}, status_code=400)
    handler = _methods(edge).get(method)
    if handler is None:
        return JSONResponse({"error": {"code": "unknown_method"}}, status_code=404)
    try:
        result = await handler(**params)
    except OAuthFailure as exc:
        return JSONResponse(
            {"error": {"code": "oauth", "oauth_error": exc.error, "message": exc.description}},
            status_code=400,
        )
    except PermissionError as exc:
        return JSONResponse({"error": {"code": "forbidden", "message": str(exc)}}, status_code=403)
    except TypeError:
        return JSONResponse({"error": {"code": "bad_params"}}, status_code=400)
    except Exception as exc:  # fail closed, never leak internals
        logger.exception("edge rpc %s failed: %s", method, type(exc).__name__)
        return JSONResponse({"error": {"code": "internal"}}, status_code=500)
    return JSONResponse({"result": result})


def start_edge_forwarder(listen_port: int, upstream_host: str, upstream_port: int):
    """Raw TCP forwarder: host 127.0.0.1:<port> (published by compose) → edge container.

    The edge sits on the internal agentshroud-dmz network, which cannot publish a
    host port, so the gateway relays bytes. It never parses or alters them; TLS is
    terminated by tailscaled before this hop.
    """

    async def _pipe(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            while chunk := await reader.read(65536):
                writer.write(chunk)
                await writer.drain()
        except (ConnectionError, OSError):
            pass
        finally:
            writer.close()

    async def _handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            up_r, up_w = await asyncio.open_connection(upstream_host, upstream_port)
        except OSError:
            writer.write(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\n\r\n")
            await writer.drain()
            writer.close()
            return
        await asyncio.gather(_pipe(reader, up_w), _pipe(up_r, writer), return_exceptions=True)

    async def _serve() -> None:
        try:
            server = await asyncio.start_server(_handle, "0.0.0.0", listen_port)  # nosec B104
            async with server:
                await server.serve_forever()
        except OSError as exc:
            logger.critical("Inbound edge forwarder port %d unavailable: %s", listen_port, exc)

    return asyncio.create_task(_serve())
