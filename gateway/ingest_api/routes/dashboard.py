# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Dashboard and collaborator routes.

Dashboard and activity monitoring endpoints:
- /collaborators - Get collaborator data
- /dashboard - Serve dashboard HTML
- /dashboard/stats - JSON stats for dashboard
- /dashboard/ws-token - Get WebSocket token for dashboard
- /ws/activity - WebSocket for real-time activity feed
"""

import asyncio
import hmac
import secrets
import time
import logging
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Request, HTTPException, Query, WebSocket, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.responses import RedirectResponse

from ..auth import create_auth_dependency
from ..state import app_state
from ..event_bus import make_event

# Create router
# Short-lived WS tokens (token -> expiry timestamp)
# These are scoped tokens that cannot be used for API auth
_ws_tokens: dict[str, float] = {}
_WS_TOKEN_TTL = 300  # 5 minutes

def _create_ws_token() -> str:
    """Create a short-lived WebSocket-only token."""
    token = f"ws_{secrets.token_urlsafe(32)}"
    _ws_tokens[token] = time.time() + _WS_TOKEN_TTL
    # Clean expired tokens
    now = time.time()
    expired = [t for t, exp in _ws_tokens.items() if exp < now]
    for t in expired:
        del _ws_tokens[t]
    return token

def _validate_ws_token(token: str) -> bool:
    """Validate a WebSocket token (single-use, time-limited)."""
    if not token or not token.startswith("ws_"):
        return False
    expiry = _ws_tokens.pop(token, None)  # Single-use: remove on validation
    if expiry is None:
        return False
    return time.time() < expiry

router = APIRouter()

# Set up logger
logger = logging.getLogger(__name__)


# Authentication dependency
async def auth_dep(request: Request):
    """Auth dependency that uses the app state config."""
    if not hasattr(app_state, "config"):
        raise HTTPException(
            status_code=401,
            detail="Service not initialized",
        )
    dep = create_auth_dependency(app_state.config)
    await dep(request)


AuthRequired = Annotated[None, Depends(auth_dep)]


# Route endpoints
@router.get("/collaborators")
async def get_collaborators(req: Request, auth: AuthRequired):
    """Return collaborator data from the shared bot workspace volume.

    Reads COLLABORATORS.md and contributor logs from /data/bot-workspace.
    Authentication required.
    """
    workspace = Path("/data/bot-workspace")
    result: dict = {"collaborators_md": None, "contributor_logs": []}

    collab_file = workspace / "COLLABORATORS.md"
    if collab_file.exists():
        result["collaborators_md"] = collab_file.read_text()

    contrib_dir = workspace / "memory" / "contributors"
    if contrib_dir.is_dir():
        logs = []
        for f in sorted(contrib_dir.iterdir()):
            if f.is_file():
                try:
                    logs.append({"filename": f.name, "content": f.read_text()})
                except Exception:
                    pass
        result["contributor_logs"] = logs

    # Append gateway-level activity tracker data (authoritative source)
    tracker = getattr(app_state, "collaborator_tracker", None)
    if tracker:
        result["activity"] = tracker.get_activity(limit=50)
        result["summary"] = tracker.get_activity_summary()
    else:
        result["activity"] = []
        result["summary"] = {"total_messages": 0, "unique_users": 0, "last_activity": None, "by_user": {}}

    return result


@router.get("/dashboard")
async def serve_dashboard(request: Request, token: str | None = Query(None)):
    """Serve the dashboard HTML (requires auth via query param or cookie)

    On first auth via query param, sets an httpOnly cookie and redirects
    to a clean URL (token removed from query string / browser history).
    """

    # Check cookie first
    cookie_token = request.cookies.get("dashboard_token")
    authenticated = False

    if cookie_token and hmac.compare_digest(cookie_token, app_state.config.auth_token):
        authenticated = True
    elif token and hmac.compare_digest(token, app_state.config.auth_token):
        # Valid token in query param - set cookie and redirect to clean URL
        redirect = RedirectResponse(url="/dashboard", status_code=302)
        is_secure = (
            request.url.scheme == "https"
            or request.headers.get("x-forwarded-proto") == "https"
        )
        redirect.set_cookie(
            key="dashboard_token",
            value=token,
            httponly=True,
            samesite="strict",
            secure=is_secure,
            max_age=86400,  # 24 hours
        )
        return redirect

    if not authenticated:
        return JSONResponse(status_code=403, content={"detail": "Forbidden"})
    
    dashboard_path = Path(__file__).parent.parent.parent / "dashboard" / "index.html"
    if dashboard_path.exists():
        html = dashboard_path.read_text()
        # L4: Generate nonce for inline scripts/styles
        import secrets as _secrets
        nonce = _secrets.token_urlsafe(24)
        # Inject nonce into script/style tags
        html = html.replace("<script", f'<script nonce="{nonce}"')
        html = html.replace("<style", f'<style nonce="{nonce}"')
        response = HTMLResponse(html)
        response.headers["Content-Security-Policy"] = (
            f"default-src 'none'; "
            f"script-src 'nonce-{nonce}'; "
            f"style-src 'nonce-{nonce}'; "
            f"connect-src 'self'; "
            f"img-src 'self'; "
            f"font-src 'self'; "
            f"frame-ancestors 'none'; "
            f"base-uri 'self'"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response
    return HTMLResponse("<h1>Dashboard not found</h1>", status_code=404)


@router.get("/dashboard/stats")
async def dashboard_stats(req: Request, auth: AuthRequired):
    """JSON stats for dashboard"""
    uptime = time.time() - app_state.start_time
    ledger_stats = await app_state.ledger.get_stats()
    pending = await app_state.approval_queue.get_pending()
    bus_stats = await app_state.event_bus.get_stats()
    pending_items = [
        {
            "request_id": p.request_id,
            "action_type": p.action_type,
            "description": p.description,
            "submitted_at": p.submitted_at,
        }
        for p in pending
    ]
    return {
        "uptime_seconds": uptime,
        "ledger_entries": ledger_stats.get("total_entries", 0),
        "pending_approvals": len(pending),
        "pending_approval_items": pending_items,
        **bus_stats,
    }


@router.get("/dashboard/ws-token")
async def dashboard_ws_token(request: Request):
    """Return a short-lived WS-only auth token for cookie-authenticated sessions.

    Returns a scoped, single-use token valid for 5 minutes.
    This token can ONLY be used for WebSocket connections, not API auth.
    """
    cookie_token = request.cookies.get("dashboard_token")
    if not cookie_token or not hmac.compare_digest(
        cookie_token, app_state.config.auth_token
    ):
        return JSONResponse(status_code=403, content={"detail": "Forbidden"})
    ws_token = _create_ws_token()
    return JSONResponse(content={"token": ws_token})


@router.websocket("/ws/activity")
async def activity_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket for real-time activity feed"""
    # Access app_state from websocket state
    
    # Accept either master auth token or scoped WS token
    # R3-L4: Only accept scoped WS tokens (no master token fallback)
    if not token or not _validate_ws_token(token):
        await websocket.close(code=4003, reason="Authentication failed")
        await app_state.event_bus.emit(
            make_event(
                "auth_failed", "Activity WebSocket authentication failed", {}, "warning"
            )
        )
        return

    await websocket.accept()

    try:
        await websocket.send_json({"type": "authenticated"})

        # Subscribe to events
        queue: asyncio.Queue = asyncio.Queue()

        async def on_event(event):
            await queue.put(event)

        await app_state.event_bus.subscribe(on_event)

        try:
            while True:
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=30)
                    await websocket.send_json(event.to_dict())
                except asyncio.TimeoutError:
                    # Send ping to keep alive
                    await websocket.send_json({"type": "ping"})
        finally:
            await app_state.event_bus.unsubscribe(on_event)

    except Exception as e:
        logger.warning(f"Activity WebSocket error: {e}")
