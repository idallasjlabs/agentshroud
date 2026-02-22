"""AgentShroud Gateway - Main FastAPI Application

Entry point for the gateway API. Wires together all components:
- PII sanitization
- Data ledger
- Multi-agent routing
- Approval queue
- Authentication
"""

import hashlib
import logging
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Annotated

import hmac

from fastapi import Depends, FastAPI, HTTPException, Query, Request, WebSocket, status
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.responses import RedirectResponse
from pathlib import Path

from ..approval_queue.queue import ApprovalQueue
from .auth import create_auth_dependency
from .config import GatewayConfig, load_config
from .ledger import DataLedger
from .models import (
    ApprovalDecision,
    ApprovalQueueItem,
    ApprovalRequest,
    ForwardRequest,
    ForwardResponse,
    LedgerEntry,
    LedgerQueryResponse,
    SSHExecRequest,
    SSHExecResponse,
    StatusResponse,
)
from ..ssh_proxy.proxy import SSHProxy
from .router import ForwardError, MultiAgentRouter
from .sanitizer import PIISanitizer
from .event_bus import EventBus, make_event
from ..web.api import router as management_api_router
from ..web.management import router as management_dashboard_router
from .version_routes import router as version_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
)
logger = logging.getLogger("agentshroud.gateway.main")


# === Application State ===


class AppState:
    """Container for application-wide state"""

    config: GatewayConfig
    sanitizer: PIISanitizer
    ledger: DataLedger
    router: MultiAgentRouter
    approval_queue: ApprovalQueue
    start_time: float
    event_bus: EventBus


app_state = AppState()


# === Lifespan Management ===


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - startup and shutdown"""

    # === STARTUP ===
    logger.info("=" * 80)
    logger.info("AgentShroud Gateway starting up...")

    # Load configuration
    try:
        app_state.config = load_config()
        logger.info("Configuration loaded successfully")
    except Exception as e:
        logger.critical(f"Failed to load configuration: {e}")
        raise

    # Set log level from config
    logging.getLogger().setLevel(app_state.config.log_level)
    logger.info(f"CORS configured with origins: {app_state.config.cors_origins}")

    # Initialize PII sanitizer
    try:
        app_state.sanitizer = PIISanitizer(app_state.config.pii)
        logger.info(
            f"PII sanitizer initialized (mode: {app_state.sanitizer.get_mode()})"
        )
    except Exception as e:
        logger.critical(f"Failed to initialize PII sanitizer: {e}")
        raise

    # Initialize data ledger
    try:
        app_state.ledger = DataLedger(app_state.config.ledger)
        await app_state.ledger.initialize()
        logger.info("Data ledger initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize data ledger: {e}")
        raise

    # Initialize router
    try:
        app_state.router = MultiAgentRouter(app_state.config.router)
        logger.info("Multi-agent router initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize router: {e}")
        raise

    # Initialize approval queue
    try:
        app_state.approval_queue = ApprovalQueue(app_state.config.approval_queue)
        logger.info("Approval queue initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize approval queue: {e}")
        raise

    # Initialize SSH proxy
    if app_state.config.ssh.enabled:
        app_state.ssh_proxy = SSHProxy(app_state.config.ssh)
        logger.info("SSH proxy initialized")
    else:
        app_state.ssh_proxy = None

    # Initialize event bus
    app_state.event_bus = EventBus()
    logger.info("Event bus initialized")

    # Record start time
    app_state.start_time = time.time()

    logger.info(
        f"AgentShroud Gateway ready at {app_state.config.bind}:{app_state.config.port}"
    )
    logger.info("=" * 80)

    yield

    # === SHUTDOWN ===
    logger.info("AgentShroud Gateway shutting down...")

    # Close ledger
    await app_state.ledger.close()

    logger.info("Shutdown complete")


# === Application ===

app = FastAPI(
    title="AgentShroud Gateway",
    description="Ingest API for the AgentShroud proxy layer framework",
    version="0.5.0",
    lifespan=lifespan,
)

# === Dependency: Authentication ===


async def auth_dep(request: Request) -> None:
    """Authentication dependency for protected endpoints"""
    dep = create_auth_dependency(app_state.config)
    await dep(request)


AuthRequired = Annotated[None, Depends(auth_dep)]



# Mount management API (has its own Bearer auth on each endpoint)
app.include_router(management_api_router)

# Mount management dashboard (serves /manage/)
app.include_router(management_dashboard_router)

# Mount version management routes (gateway Bearer auth)
app.include_router(version_router, dependencies=[Depends(auth_dep)])


# === CORS Middleware ===
# Custom CORS middleware that reads from app_state.config at runtime
# This allows agentshroud.yaml overrides to take effect


@app.middleware("http")
async def cors_middleware(request: Request, call_next):
    """CORS middleware that uses config from app_state"""
    # Handle preflight requests
    if request.method == "OPTIONS":
        origin = request.headers.get("origin")
        if hasattr(app_state, "config") and origin in app_state.config.cors_origins:
            return JSONResponse(
                content={},
                headers={
                    "Access-Control-Allow-Origin": origin,
                    "Access-Control-Allow-Credentials": "true",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
                },
            )
        return JSONResponse(content={}, status_code=403)

    # Process request
    response = await call_next(request)

    # Add CORS headers to response
    origin = request.headers.get("origin")
    if hasattr(app_state, "config") and origin in app_state.config.cors_origins:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"

    return response


# === Request Logging Middleware ===


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests

    Never logs request bodies (may contain PII).
    """
    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time
    logger.info(
        f"{request.method} {request.url.path} -> {response.status_code} "
        f"({duration:.3f}s)"
    )

    return response


# === Global Exception Handler ===


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch-all error handler

    Never leaks stack traces or internal details to client.
    Logs full traceback at ERROR level.
    """
    logger.error(f"Unhandled exception: {exc}", exc_info=True)

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )



# === Endpoints ===


@app.get("/", response_class=HTMLResponse)
async def system_control():
    """System Control - Live Dashboard

    Shows real-time system status with links to controls.
    """
    uptime = time.time() - app_state.start_time
    stats = await app_state.ledger.get_stats()
    pending = await app_state.approval_queue.get_pending()

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>AgentShroud Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: monospace; background: #1a1a1a; color: #e0e0e0; padding: 2rem; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #4ade80; }}
        .status {{ background: #2a2a2a; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; }}
        .healthy {{ color: #4ade80; }}
        .warning {{ color: #fbbf24; }}
        .error {{ color: #ef4444; }}
        .section {{ margin: 2rem 0; }}
        a {{ color: #60a5fa; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .metric {{ display: inline-block; margin-right: 2rem; }}
        code {{ background: #3a3a3a; padding: 0.2rem 0.5rem; border-radius: 4px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ AgentShroud Control Center</h1>

        <div class="status">
            <h2 class="healthy">● System Status: HEALTHY</h2>
            <div class="metric">Version: 0.5.0</div>
            <div class="metric">Uptime: {int(uptime)}s</div>
            <div class="metric">PII Engine: {app_state.sanitizer.get_mode()}</div>
        </div>

        <div class="section">
            <h2>📊 Metrics</h2>
            <div class="status">
                <div class="metric">Ledger Entries: {stats.get('total_entries', 0)}</div>
                <div class="metric">Pending Approvals: {len(pending)}</div>
            </div>
        </div>

        <div class="section">
            <h2>🎛️ Controls</h2>
            <div class="status">
                <p><a href="http://localhost:18790" target="_blank">→ OpenClaw Control UI</a> (Bot interface)</p>
                <p><a href="/dashboard">→ Activity Dashboard</a> (real-time event feed)</p>
                <p><a href="/manage/">→ Management Dashboard</a> (service controls, config, logs)</p>
                <p><a href="/status">→ Gateway Status API</a></p>
                <p><a href="/ledger">→ Data Ledger</a></p>
                <p><a href="/approve/pending">→ Approval Queue</a></p>
            </div>
        </div>

        <div class="section">
            <h2>📡 Endpoints</h2>
            <div class="status">
                <p><code>POST /forward</code> - Forward content to agent</p>
                <p><code>GET /status</code> - Health check</p>
                <p><code>GET /ledger</code> - Query ledger</p>
                <p><code>GET /approval-queue</code> - List pending approvals</p>
            </div>
        </div>

        <div class="section">
            <h2>🔗 Access</h2>
            <div class="status">
                <p>Local: <code>http://localhost:8080</code></p>
                <p>Tailscale: <code>http://100.90.175.83:8080</code></p>
            </div>
        </div>
    </div>

    <script>
        // Auto-refresh every 30 seconds
        setTimeout(() => location.reload(), 30000);
    </script>
</body>
</html>"""
    return HTMLResponse(html)


@app.get("/status", response_model=StatusResponse)
async def health_check():
    """Health check endpoint

    No authentication required.
    """
    uptime = time.time() - app_state.start_time
    stats = await app_state.ledger.get_stats()
    pending = await app_state.approval_queue.get_pending()

    return StatusResponse(
        status="healthy",
        version="0.5.0",
        uptime_seconds=uptime,
        ledger_entries=stats.get("total_entries", 0),
        pending_approvals=len(pending),
        pii_engine=app_state.sanitizer.get_mode(),
        config_loaded=True,
    )


@app.post(
    "/forward", response_model=ForwardResponse, status_code=status.HTTP_201_CREATED
)
async def forward_content(request: ForwardRequest, auth: AuthRequired):
    """Main ingest endpoint

    Receives data from iOS Shortcuts, browser extension, or API.
    Sanitizes PII, logs to ledger, and forwards to agent.

    Authentication required.
    """
    logger.info(
        f"Ingest request: source={request.source}, "
        f"type={request.content_type}, size={len(request.content)}"
    )

    # Step 1: Sanitize PII
    try:
        sanitization_result = await app_state.sanitizer.sanitize(request.content)
    except Exception as e:
        logger.error(f"PII sanitization failed: {e}")
        # CRITICAL: Fail closed - never forward unsanitized content
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Content sanitization failed. Request blocked for safety.",
        )

    sanitized_content = sanitization_result.sanitized_content
    sanitized = len(sanitization_result.redactions) > 0

    # Step 2: Resolve routing target
    try:
        target = await app_state.router.resolve_target(request)
    except Exception as e:
        logger.error(f"Routing failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to resolve routing target",
        )

    # Step 3: Forward to agent
    forwarded_to = target.name
    agent_response = None
    try:
        agent_response = await app_state.router.forward_to_agent(
            target=target,
            sanitized_content=sanitized_content,
            ledger_id="pending",  # Will be updated with actual ID
            metadata={
                "source": request.source,
                "content_type": request.content_type,
                **request.metadata,
            },
        )
        logger.info(f"Content forwarded to {target.name}")
        logger.info(f"DEBUG: agent_response = {agent_response}")

    except ForwardError as e:
        # Agent offline - log but continue (graceful degradation)
        logger.warning(f"Forward failed: {e}. Content logged but not delivered.")
        forwarded_to = f"{target.name} (offline)"

    # Step 4: Record in ledger
    try:
        ledger_entry = await app_state.ledger.record(
            source=request.source,
            content=sanitized_content,
            original_content=request.content,
            sanitized=sanitized,
            redaction_count=len(sanitization_result.redactions),
            redaction_types=sanitization_result.entity_types_found,
            forwarded_to=forwarded_to,
            content_type=request.content_type,
            metadata=request.metadata,
        )
    except Exception as e:
        logger.error(f"Ledger recording failed: {e}")
        # Non-critical - content was already forwarded
        # But we should still notify
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to record in ledger",
        )

    # Emit forward event
    await app_state.event_bus.emit(
        make_event(
            "forward",
            f"Content forwarded from {request.source} to {forwarded_to}",
            {
                "source": request.source,
                "content_type": request.content_type,
                "forwarded_to": forwarded_to,
            },
            "warning" if sanitized else "info",
        )
    )
    if sanitized:
        await app_state.event_bus.emit(
            make_event(
                "pii_detected",
                f"{len(sanitization_result.redactions)} PII entities redacted",
                {
                    "types": sanitization_result.entity_types_found,
                    "count": len(sanitization_result.redactions),
                },
                "warning",
            )
        )

    # Step 5: Return response
    response_data = {
        "id": ledger_entry.id,
        "sanitized": sanitized,
        "redactions": sanitization_result.entity_types_found,
        "redaction_count": len(sanitization_result.redactions),
        "content_hash": ledger_entry.content_hash,
        "forwarded_to": forwarded_to,
        "timestamp": ledger_entry.timestamp,
    }

    # Include agent response if available
    if agent_response:
        # Step 5.0: Filter out Claude XML internal blocks
        filtered_response, xml_was_filtered = app_state.sanitizer.filter_xml_blocks(
            agent_response
        )
        if xml_was_filtered:
            logger.info(
                f"Filtered XML blocks from agent response for source={request.source}"
            )

        # Step 5.1: Block credentials from being displayed via untrusted sources
        blocked_response, was_blocked = await app_state.sanitizer.block_credentials(
            content=filtered_response, source=request.source
        )

        if was_blocked:
            logger.warning(
                f"Blocked credential display from source={request.source}, "
                f"ledger_id={ledger_entry.id}"
            )
            # Log the blocking event in ledger
            await app_state.ledger.record(
                source="gateway_security",
                content=f"Blocked credential display to {request.source}",
                original_content=agent_response[:100],  # First 100 chars for audit
                sanitized=True,
                redaction_count=1,
                redaction_types=["CREDENTIALS"],
                forwarded_to="blocked",
                content_type="security_event",
                metadata={"original_ledger_id": ledger_entry.id},
            )

        response_data["agent_response"] = blocked_response

    return response_data


@app.get("/ledger", response_model=LedgerQueryResponse)
async def query_ledger(
    auth: AuthRequired,
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    source: str | None = Query(None),
    since: str | None = Query(None),
    until: str | None = Query(None),
    forwarded_to: str | None = Query(None),
):
    """Query the data ledger

    Returns paginated results with optional filters.
    Authentication required.
    """
    return await app_state.ledger.query(
        page=page,
        page_size=page_size,
        source=source,
        since=since,
        until=until,
        forwarded_to=forwarded_to,
    )


@app.get("/ledger/{entry_id}", response_model=LedgerEntry)
async def get_ledger_entry(entry_id: str, auth: AuthRequired):
    """Get a single ledger entry by ID

    Authentication required.
    """
    entry = await app_state.ledger.get_entry(entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Ledger entry not found")
    return entry


@app.delete("/ledger/{entry_id}")
async def delete_ledger_entry(entry_id: str, auth: AuthRequired):
    """'Forget this' - permanently delete a ledger entry

    Implements right to erasure.
    Authentication required.
    """
    deleted = await app_state.ledger.delete_entry(entry_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ledger entry not found")

    return {"deleted": True, "id": entry_id}


@app.get("/agents")
async def list_agents(auth: AuthRequired):
    """List all configured agent targets with health status

    Authentication required.
    """
    targets = app_state.router.list_targets()
    return {"agents": [t.model_dump() for t in targets]}


@app.post("/approve", response_model=ApprovalQueueItem)
async def submit_approval_request(request: ApprovalRequest, auth: AuthRequired):
    """Submit an action for human approval

    Called by agents when attempting sensitive actions.
    Authentication required.
    """
    item = await app_state.approval_queue.submit(request)
    await app_state.event_bus.emit(
        make_event(
            "approval_submitted",
            f"Approval requested: {request.action_type} - {request.description}",
            {"request_id": item.request_id, "action_type": request.action_type},
        )
    )
    return item


@app.post("/approve/{request_id}/decide", response_model=ApprovalQueueItem)
async def decide_approval(
    request_id: str, decision: ApprovalDecision, auth: AuthRequired
):
    """Approve or reject a pending action

    Authentication required.
    """
    try:
        item = await app_state.approval_queue.decide(
            request_id=request_id, approved=decision.approved, reason=decision.reason
        )
        await app_state.event_bus.emit(
            make_event(
                "approval_decided",
                f"Approval {'approved' if decision.approved else 'rejected'}: {request_id}",
                {"request_id": request_id, "approved": decision.approved},
            )
        )
        return item

    except KeyError:
        raise HTTPException(status_code=404, detail="Approval request not found")

    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.get("/approve/pending", response_model=list[ApprovalQueueItem])
async def list_pending_approvals(auth: AuthRequired):
    """List all pending approval requests

    Authentication required.
    """
    return await app_state.approval_queue.get_pending()


@app.websocket("/ws/approvals")
async def approval_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket endpoint for real-time approval notifications

    Protocol:
    1. Client connects with token as query param: /ws/approvals?token=<token>
    2. Server validates token during handshake - rejects before accepting
    3. Server pushes new approval requests and decisions
    4. Client can send decisions: {"type": "decide", "request_id": "...", "approved": true}
    """
    if not token or not hmac.compare_digest(token, app_state.config.auth_token):
        await websocket.close(code=4003, reason="Authentication failed")
        await app_state.event_bus.emit(
            make_event("auth_failed", "WebSocket authentication failed", {}, "warning")
        )
        return

    await app_state.approval_queue.connect(websocket)

    try:
        await websocket.send_json({"type": "authenticated"})

        # Keep connection open and handle messages
        while True:
            message = await websocket.receive_json()

            # Handle decision messages
            if message.get("type") == "decide":
                request_id = message.get("request_id")
                approved = message.get("approved")

                if not request_id or approved is None:
                    await websocket.send_json(
                        {"type": "error", "message": "Invalid decision message"}
                    )
                    continue

                try:
                    item = await app_state.approval_queue.decide(
                        request_id=request_id,
                        approved=approved,
                        reason=message.get("reason", ""),
                    )

                    await websocket.send_json(
                        {
                            "type": "decision_ack",
                            "data": {
                                "request_id": request_id,
                                "status": item.status,
                            },
                        }
                    )

                except (KeyError, ValueError) as e:
                    await websocket.send_json({"type": "error", "message": str(e)})

    except Exception as e:
        logger.warning(f"WebSocket error: {e}")

    finally:
        await app_state.approval_queue.disconnect(websocket)


# === Collaborators Endpoint ===


@app.get("/collaborators")
async def get_collaborators(auth: AuthRequired):
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


# === Entry Point for Testing ===

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)


# === Dashboard Endpoints ===


@app.get("/dashboard")
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
    dashboard_path = Path(__file__).parent.parent / "dashboard" / "index.html"
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


@app.get("/dashboard/stats")
async def dashboard_stats(auth: AuthRequired):
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


@app.get("/dashboard/ws-token")
async def dashboard_ws_token(request: Request):
    """Return a WS auth token for cookie-authenticated dashboard sessions.

    The dashboard JS calls this to get the token for WebSocket connections,
    avoiding direct token injection into HTML (XSS mitigation).
    """
    cookie_token = request.cookies.get("dashboard_token")
    if not cookie_token or not hmac.compare_digest(
        cookie_token, app_state.config.auth_token
    ):
        return JSONResponse(status_code=403, content={"detail": "Forbidden"})
    return JSONResponse(content={"token": app_state.config.auth_token})


@app.websocket("/ws/activity")
async def activity_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket for real-time activity feed"""
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
        import asyncio

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


# === SSH Endpoints ===


@app.post("/ssh/exec")
async def ssh_exec(request: SSHExecRequest, auth: AuthRequired):
    """Execute SSH command with validation and approval"""
    if app_state.ssh_proxy is None:
        raise HTTPException(status_code=503, detail="SSH proxy not configured")

    proxy: SSHProxy = app_state.ssh_proxy

    # Check host exists
    if request.host not in proxy.config.hosts:
        raise HTTPException(status_code=404, detail=f"Unknown SSH host: {request.host}")

    # Validate command
    valid, denial_reason = proxy.validate_command(request.host, request.command)
    if not valid:
        # Audit denied command — sanitize PII before storing
        sanitized = await app_state.sanitizer.sanitize(request.command)
        content_hash = hashlib.sha256(
            f"{request.command}:{request.host}".encode()
        ).hexdigest()
        await app_state.ledger.record(
            source="ssh",
            content=f"DENIED: {sanitized.sanitized_content}",
            original_content=content_hash,
            sanitized=len(sanitized.redactions) > 0,
            redaction_count=len(sanitized.redactions),
            redaction_types=[r.entity_type for r in sanitized.redactions],
            forwarded_to=request.host,
            content_type="ssh_command",
            metadata={
                "host": request.host,
                "denied_reason": denial_reason,
                "reason": request.reason,
            },
        )
        await app_state.event_bus.emit(
            make_event(
                "ssh_denied",
                f"SSH denied on {request.host}: {denial_reason}",
                {"host": request.host, "reason": denial_reason},
                "critical" if "injection" in denial_reason.lower() else "warning",
            )
        )
        raise HTTPException(status_code=403, detail=denial_reason)

    async def _execute_and_record(approved_by: str) -> SSHExecResponse:
        """Execute command and record to ledger with PII sanitization."""
        result = await proxy.execute(request.host, request.command, request.timeout)
        # Sanitize command for ledger storage
        sanitized = await app_state.sanitizer.sanitize(request.command)
        content_hash = hashlib.sha256(
            f"{request.command}:{request.host}".encode()
        ).hexdigest()
        entry = await app_state.ledger.record(
            source="ssh",
            content=sanitized.sanitized_content,
            original_content=content_hash,
            sanitized=len(sanitized.redactions) > 0,
            redaction_count=len(sanitized.redactions),
            redaction_types=[r.entity_type for r in sanitized.redactions],
            forwarded_to=request.host,
            content_type="ssh_command",
            metadata={
                "host": request.host,
                "exit_code": result.exit_code,
                "duration": result.duration_seconds,
                "approved_by": approved_by,
                "reason": request.reason,
            },
        )
        await app_state.event_bus.emit(
            make_event(
                "ssh_exec",
                f"SSH command on {request.host} (exit {result.exit_code})",
                {
                    "host": request.host,
                    "command": request.command[:80],
                    "exit_code": result.exit_code,
                    "duration": result.duration_seconds,
                },
            )
        )
        now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        return SSHExecResponse(
            request_id=entry.id,
            host=request.host,
            command=request.command,
            stdout=result.stdout,
            stderr=result.stderr,
            exit_code=result.exit_code,
            duration_seconds=result.duration_seconds,
            approved_by=approved_by,
            timestamp=now,
            audit_id=entry.id,
        )

    # Check auto-approval
    if proxy.is_auto_approved(request.host, request.command):
        return await _execute_and_record("auto")

    # If require_approval is false, execute directly (still validated above)
    if not proxy.config.require_approval:
        return await _execute_and_record("policy")

    # Requires approval — submit to queue and return 202
    # Sanitize command/reason before storing in approval queue (PII leak prevention)

    sanitized_cmd = await app_state.sanitizer.sanitize(request.command)
    sanitized_reason = ""
    if request.reason:
        sanitized_reason_result = await app_state.sanitizer.sanitize(request.reason)
        sanitized_reason = sanitized_reason_result.sanitized_content
    approval_req = ApprovalRequest(
        action_type="ssh_exec",
        description=f"SSH command on {request.host}: {sanitized_cmd.sanitized_content}",
        details={
            "host": request.host,
            "command": sanitized_cmd.sanitized_content,
            "timeout": request.timeout,
            "reason": sanitized_reason,
        },
        agent_id="ssh-proxy",
    )
    item = await app_state.approval_queue.submit(approval_req)
    return JSONResponse(
        status_code=202,
        content={
            "request_id": item.request_id,
            "status": "pending_approval",
            "message": f"Command requires approval: {request.command}",
        },
    )


@app.get("/ssh/hosts")
async def ssh_hosts(auth: AuthRequired):
    """List configured SSH hosts (names only)"""
    if app_state.ssh_proxy is None:
        return {"hosts": []}
    return {"hosts": list(app_state.ssh_proxy.config.hosts.keys())}


@app.get("/ssh/history")
async def ssh_history(
    auth: AuthRequired,
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
):
    """Query SSH audit entries from ledger"""
    return await app_state.ledger.query(
        page=page,
        page_size=page_size,
        source="ssh",
    )
