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
import os
import re
import secrets
import time
from datetime import datetime
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, Request, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.responses import RedirectResponse

from ..auth import create_auth_dependency
from ..event_bus import make_event
from ..state import app_state

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


def _parse_collaborator_log_dirs() -> list[Path]:
    """Resolve contributor log directories (ordered, de-duplicated)."""
    configured = str(
        os.environ.get(
            "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS",
            "/app/data/contributors",
        )
    )
    resolved: list[Path] = []
    for raw in configured.split(","):
        value = raw.strip()
        if not value:
            continue
        path = Path(value)
        if path not in resolved:
            resolved.append(path)
    return resolved


def _load_contributor_logs(log_dirs: list[Path]) -> list[dict]:
    """Load contributor logs from multiple directories with de-dup by filename."""
    logs: list[dict] = []
    seen_filenames: set[str] = set()
    for log_dir in log_dirs:
        if not log_dir.is_dir():
            continue
        for f in sorted(log_dir.iterdir(), reverse=True):
            if not f.is_file():
                continue
            if f.name in seen_filenames:
                continue
            try:
                logs.append(
                    {
                        "filename": f.name,
                        "content": f.read_text(),
                        "source_dir": str(log_dir),
                    }
                )
                seen_filenames.add(f.name)
            except Exception:
                continue
    return logs


def _build_activity_summary_from_contributor_logs(logs: list[dict]) -> dict:
    """Fallback activity summary when tracker data is unavailable/empty."""
    total_messages = 0
    unique_users: set[str] = set()
    last_activity: float | None = None

    for item in logs:
        content = str(item.get("content", "") or "")
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("- "):
                line = line[2:].strip()
            if "|" not in line:
                continue
            total_messages += 1
            # Expected format:
            # - 2026-03-10T16:33:22+00:00 | username (12345) | source | preview
            match_uid = re.search(r"\(([^)]+)\)", line)
            if match_uid:
                unique_users.add(match_uid.group(1).strip())
            ts_token = line.split("|", 1)[0].strip()
            if ts_token.endswith("Z"):
                ts_token = ts_token[:-1] + "+00:00"
            try:
                ts = datetime.fromisoformat(ts_token).timestamp()
                if last_activity is None or ts > last_activity:
                    last_activity = ts
            except Exception:
                continue

    return {
        "total_messages": total_messages,
        "unique_users": len(unique_users),
        "last_activity": last_activity,
        "by_user": {},
    }


def _build_activity_entries_from_contributor_logs(logs: list[dict], limit: int = 50) -> list[dict]:
    """Fallback activity entries when tracker data is unavailable/empty."""
    entries: list[dict] = []
    for item in logs:
        content = str(item.get("content", "") or "")
        for line in content.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("- "):
                line = line[2:].strip()
            if "|" not in line:
                continue
            payload = line
            parts = [p.strip() for p in payload.split("|")]
            if len(parts) < 4:
                continue
            ts_token, user_token, source_token, preview = (
                parts[0],
                parts[1],
                parts[2],
                " | ".join(parts[3:]),
            )
            if ts_token.endswith("Z"):
                ts_token = ts_token[:-1] + "+00:00"
            try:
                ts = datetime.fromisoformat(ts_token).timestamp()
            except Exception:
                continue
            match_uid = re.search(r"\(([^)]+)\)", user_token)
            uid = match_uid.group(1).strip() if match_uid else "unknown"
            username = re.sub(r"\s*\([^)]+\)\s*$", "", user_token).strip() or "unknown"
            entries.append(
                {
                    "timestamp": ts,
                    "user_id": uid,
                    "username": username,
                    "message_preview": preview[:80],
                    "source": source_token or "unknown",
                }
            )
    entries.sort(key=lambda e: float(e.get("timestamp", 0) or 0), reverse=True)
    return entries[: max(1, int(limit or 50))]


async def _build_egress_live_snapshot() -> dict:
    """Build compact egress dashboard snapshot for websocket/API clients."""
    egress_filter = getattr(app_state, "egress_filter", None)
    approval_queue = getattr(app_state, "egress_approval_queue", None)
    stats = egress_filter.get_stats() if egress_filter else {}
    recent_log = []
    if egress_filter:
        recent = egress_filter.get_log(limit=20)
        recent_log = [
            {
                "timestamp": a.timestamp,
                "agent_id": a.agent_id,
                "destination": a.destination,
                "port": a.port,
                "action": a.action.value,
                "rule": a.rule,
            }
            for a in recent
        ]
    pending_items = []
    emergency = {"enabled": False, "reason": ""}
    if approval_queue:
        pending = await approval_queue.get_pending_requests()
        pending_items = pending[-20:]
        emergency = await approval_queue.get_emergency_status()
    now_ts = time.time()
    enriched_pending: list[dict] = []
    for item in pending_items:
        enriched = dict(item)
        ts = float(item.get("timestamp", now_ts) or now_ts)
        timeout_at = float(item.get("timeout_at", now_ts) or now_ts)
        enriched["age_seconds"] = max(0.0, now_ts - ts)
        enriched["remaining_seconds"] = max(0.0, timeout_at - now_ts)
        enriched_pending.append(enriched)
    pending_items = enriched_pending
    pending_by_risk = {"green": 0, "yellow": 0, "red": 0, "unknown": 0}
    pending_domains: dict[str, int] = {}
    pending_agents: dict[str, int] = {}
    pending_tools: dict[str, int] = {}
    for item in pending_items:
        risk = str(item.get("risk_level", "unknown")).lower()
        pending_by_risk[risk if risk in pending_by_risk else "unknown"] += 1
        domain = str(item.get("domain", "")).strip().lower()
        if domain:
            pending_domains[domain] = pending_domains.get(domain, 0) + 1
        agent_id = str(item.get("agent_id", "")).strip()
        if agent_id:
            pending_agents[agent_id] = pending_agents.get(agent_id, 0) + 1
        tool_name = str(item.get("tool_name", "")).strip().lower()
        if tool_name:
            pending_tools[tool_name] = pending_tools.get(tool_name, 0) + 1
    pending_domain_top = [
        {"domain": d, "count": c}
        for d, c in sorted(pending_domains.items(), key=lambda kv: kv[1], reverse=True)[:10]
    ]
    pending_agent_top = [
        {"agent_id": a, "count": c}
        for a, c in sorted(pending_agents.items(), key=lambda kv: kv[1], reverse=True)[:10]
    ]
    pending_tool_top = [
        {"tool_name": t, "count": c}
        for t, c in sorted(pending_tools.items(), key=lambda kv: kv[1], reverse=True)[:10]
    ]
    pending_average_age_seconds = (
        sum(float(item.get("age_seconds", 0.0) or 0.0) for item in pending_items)
        / len(pending_items)
        if pending_items
        else 0.0
    )
    pending_oldest_age_seconds = max(
        (float(item.get("age_seconds", 0.0) or 0.0) for item in pending_items),
        default=0.0,
    )
    pending_expiring_soon_count = sum(
        1 for item in pending_items if float(item.get("remaining_seconds", 0.0) or 0.0) <= 30.0
    )
    recent_security_events = []
    event_bus = getattr(app_state, "event_bus", None)
    if event_bus is not None:
        events = await event_bus.get_recent(limit=200)
        for evt in events:
            evt_type = str(evt.get("type", ""))
            if evt_type.startswith(("egress_", "privacy_", "quarantine_", "scanner_", "auth_")):
                recent_security_events.append(evt)
        recent_security_events = recent_security_events[-20:]
    soc_risk = {"risk_score": 0, "severity": "low"}
    soc_summary: dict = {}
    try:
        from ...security.soc_correlation import build_correlation_summary
        from ..main import app_state as _app_state

        corr = build_correlation_summary(_app_state, limit=200)
        soc_risk = {"risk_score": corr.risk_score, "severity": corr.severity}
        soc_summary = corr.to_dict()
    except Exception:
        pass
    quarantine = getattr(app_state, "blocked_message_quarantine", []) or []
    quarantine_pending = sum(1 for q in quarantine if str(q.get("status", "pending")) == "pending")
    outbound_quarantine = getattr(app_state, "blocked_outbound_quarantine", []) or []
    outbound_quarantine_pending = sum(
        1 for q in outbound_quarantine if str(q.get("status", "pending")) == "pending"
    )
    quarantine_summary = {
        "inbound": {
            "total": len(quarantine),
            "pending": quarantine_pending,
            "released": sum(
                1 for q in quarantine if str(q.get("status", "")).lower() == "released"
            ),
            "discarded": sum(
                1 for q in quarantine if str(q.get("status", "")).lower() == "discarded"
            ),
        },
        "outbound": {
            "total": len(outbound_quarantine),
            "pending": outbound_quarantine_pending,
            "released": sum(
                1 for q in outbound_quarantine if str(q.get("status", "")).lower() == "released"
            ),
            "discarded": sum(
                1 for q in outbound_quarantine if str(q.get("status", "")).lower() == "discarded"
            ),
        },
    }
    privacy_policy_summary = {
        "violations": 0,
        "redaction_events": 0,
        "total_redactions": 0,
        "top_violating_agents": {},
        "top_violating_tools": {},
    }
    privacy_access_summary = {"total": 0, "by_agent": {}, "by_tool": {}}
    privacy_redaction_summary = {"events": 0, "total_redactions": 0, "by_agent": {}, "by_tool": {}}
    try:
        mcp = getattr(app_state, "mcp_proxy", None)
        perms = getattr(mcp, "permissions", None) if mcp else None
        if perms and hasattr(perms, "get_private_access_summary"):
            access_summary = perms.get_private_access_summary(limit=200)
            redaction_summary = (
                perms.get_private_redaction_summary(limit=200)
                if hasattr(perms, "get_private_redaction_summary")
                else {"events": 0, "total_redactions": 0, "by_agent": {}, "by_tool": {}}
            )
            privacy_access_summary = access_summary
            privacy_redaction_summary = redaction_summary
            privacy_policy_summary = {
                "violations": int(access_summary.get("total", 0) or 0),
                "redaction_events": int(redaction_summary.get("events", 0) or 0),
                "total_redactions": int(redaction_summary.get("total_redactions", 0) or 0),
                "top_violating_agents": access_summary.get("by_agent", {}),
                "top_violating_tools": access_summary.get("by_tool", {}),
            }
    except Exception:
        pass

    return {
        "egress_stats": stats,
        "egress_recent_log": recent_log,
        "pending_requests": len(pending_items),
        "pending_items": pending_items,
        "pending_by_risk": pending_by_risk,
        "pending_domain_top": pending_domain_top,
        "pending_agent_top": pending_agent_top,
        "pending_tool_top": pending_tool_top,
        "pending_average_age_seconds": pending_average_age_seconds,
        "pending_oldest_age_seconds": pending_oldest_age_seconds,
        "pending_expiring_soon_count": pending_expiring_soon_count,
        "emergency": emergency,
        "quarantined_blocked_messages": len(quarantine),
        "quarantined_blocked_messages_pending": quarantine_pending,
        "quarantined_blocked_outbound": len(outbound_quarantine),
        "quarantined_blocked_outbound_pending": outbound_quarantine_pending,
        "quarantine_summary": quarantine_summary,
        "recent_security_events": recent_security_events,
        "soc_risk": soc_risk,
        "soc_summary": soc_summary,
        "privacy_policy_summary": privacy_policy_summary,
        "privacy_access_summary": privacy_access_summary,
        "privacy_redaction_summary": privacy_redaction_summary,
        "scanner_summaries": {
            k: v.get("summary", {})
            for k, v in (getattr(app_state, "scanner_results", {}) or {}).items()
            if isinstance(v, dict)
        },
        "scanner_recent_events": (getattr(app_state, "scanner_result_history", []) or [])[-20:],
    }


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

    configured_dirs = _parse_collaborator_log_dirs()
    workspace_default = workspace / "memory" / "contributors"
    if workspace_default not in configured_dirs:
        configured_dirs.append(workspace_default)
    result["contributor_logs"] = _load_contributor_logs(configured_dirs)
    result["contributor_log_sources"] = [str(p) for p in configured_dirs]

    # Append gateway-level activity tracker data (authoritative source)
    tracker = getattr(app_state, "collaborator_tracker", None)
    if tracker:
        result["activity"] = tracker.get_activity(limit=50)
        result["summary"] = tracker.get_activity_summary()
        if (
            isinstance(result.get("summary"), dict)
            and int(result["summary"].get("total_messages", 0) or 0) == 0
            and result.get("contributor_logs")
        ):
            result["activity"] = _build_activity_entries_from_contributor_logs(
                result["contributor_logs"], limit=50
            )
            result["summary"] = _build_activity_summary_from_contributor_logs(
                result["contributor_logs"]
            )
            result["activity_source"] = "contributor_logs_fallback"
        else:
            result["activity_source"] = "tracker"
    else:
        result["activity"] = _build_activity_entries_from_contributor_logs(
            result["contributor_logs"], limit=50
        )
        result["summary"] = _build_activity_summary_from_contributor_logs(
            result["contributor_logs"]
        )
        result["activity_source"] = "contributor_logs_fallback"

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
            request.url.scheme == "https" or request.headers.get("x-forwarded-proto") == "https"
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
    quarantine = getattr(app_state, "blocked_message_quarantine", []) or []
    egress_stats = {}
    if getattr(app_state, "egress_filter", None):
        egress_stats = app_state.egress_filter.get_stats()
    live = await _build_egress_live_snapshot()
    return {
        "uptime_seconds": uptime,
        "ledger_entries": ledger_stats.get("total_entries", 0),
        "pending_approvals": len(pending),
        "pending_approval_items": pending_items,
        "egress_stats": egress_stats,
        "quarantined_blocked_messages": len(quarantine),
        "egress_live": live,
        **bus_stats,
    }


@router.get("/dashboard/ws-token")
async def dashboard_ws_token(request: Request):
    """Return a short-lived WS-only auth token for cookie-authenticated sessions.

    Returns a scoped, single-use token valid for 5 minutes.
    This token can ONLY be used for WebSocket connections, not API auth.
    """
    cookie_token = request.cookies.get("dashboard_token")
    if not cookie_token or not hmac.compare_digest(cookie_token, app_state.config.auth_token):
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
            make_event("auth_failed", "Activity WebSocket authentication failed", {}, "warning")
        )
        return

    await websocket.accept()

    try:
        await websocket.send_json({"type": "authenticated"})
        await websocket.send_json(
            {"type": "egress_snapshot", "details": await _build_egress_live_snapshot()}
        )

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


@router.websocket("/ws/egress")
async def egress_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket stream specialized for egress/security dashboard updates."""
    if not token or not _validate_ws_token(token):
        await websocket.close(code=4003, reason="Authentication failed")
        await app_state.event_bus.emit(
            make_event("auth_failed", "Egress WebSocket authentication failed", {}, "warning")
        )
        return

    await websocket.accept()
    await websocket.send_json({"type": "authenticated"})
    await websocket.send_json(
        {"type": "egress_snapshot", "details": await _build_egress_live_snapshot()}
    )

    queue: asyncio.Queue = asyncio.Queue()

    async def on_event(event):
        if (
            event.type.startswith("egress_")
            or event.type.startswith("quarantine_")
            or event.type.startswith("privacy_")
            or event.type.startswith("scanner_")
            or event.type.startswith("auth_")
        ):
            await queue.put(event)

    await app_state.event_bus.subscribe(on_event)
    try:
        while True:
            try:
                event = await asyncio.wait_for(queue.get(), timeout=20)
                await websocket.send_json(event.to_dict())
            except asyncio.TimeoutError:
                await websocket.send_json(
                    {"type": "egress_snapshot", "details": await _build_egress_live_snapshot()}
                )
    except Exception as e:
        logger.warning(f"Egress WebSocket error: {e}")
    finally:
        await app_state.event_bus.unsubscribe(on_event)
