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
import logging
import time
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Request, HTTPException, Query, WebSocket, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.responses import RedirectResponse

from ..auth import create_auth_dependency
from ..event_bus import make_event

# Create router
router = APIRouter()

# Set up logger
logger = logging.getLogger(__name__)


# Authentication dependency
async def auth_dep(request: Request):
    """Auth dependency that uses the app state config."""
    app_state = request.app.state.app_state
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

    return result


@router.get("/dashboard")
async def serve_dashboard(request: Request, token: str | None = Query(None)):
    """Serve the dashboard HTML (requires auth via query param or cookie)

    On first auth via query param, sets an httpOnly cookie and redirects
    to a clean URL (token removed from query string / browser history).
    """
    app_state = request.app.state.app_state

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
        response = HTMLResponse(html)
        response.headers["Content-Security-Policy"] = (
            "default-src 'none'; script-src 'unsafe-inline'; "
            "style-src 'unsafe-inline'; connect-src 'self'; "
            "img-src 'self'; font-src 'self'"
        )
        return response
    return HTMLResponse("<h1>Dashboard not found</h1>", status_code=404)


@router.get("/dashboard/stats")
async def dashboard_stats(req: Request, auth: AuthRequired):
    """JSON stats for dashboard"""
    app_state = req.app.state.app_state
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
    """Return a WS auth token for cookie-authenticated dashboard sessions.

    The dashboard JS calls this to get the token for WebSocket connections,
    avoiding direct token injection into HTML (XSS mitigation).
    """
    app_state = request.app.state.app_state
    cookie_token = request.cookies.get("dashboard_token")
    if not cookie_token or not hmac.compare_digest(
        cookie_token, app_state.config.auth_token
    ):
        return JSONResponse(status_code=403, content={"detail": "Forbidden"})
    return JSONResponse(content={"token": app_state.config.auth_token})


@router.websocket("/ws/activity")
async def activity_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket for real-time activity feed"""
    # Access app_state from websocket state
    app_state = websocket.scope["app"].state.app_state
    
    if not token or not hmac.compare_digest(token, app_state.config.auth_token):
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