"""SecureClaw Gateway - Main FastAPI Application

Entry point for the gateway API. Wires together all components:
- PII sanitization
- Data ledger
- Multi-agent routing
- Approval queue
- Authentication
"""

import logging
import time
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, Request, WebSocket, status
from fastapi.responses import JSONResponse, HTMLResponse
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
    StatusResponse,
)
from .router import ForwardError, MultiAgentRouter
from .sanitizer import PIISanitizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
)
logger = logging.getLogger("secureclaw.gateway.main")


# === Application State ===

class AppState:
    """Container for application-wide state"""

    config: GatewayConfig
    sanitizer: PIISanitizer
    ledger: DataLedger
    router: MultiAgentRouter
    approval_queue: ApprovalQueue
    start_time: float


app_state = AppState()


# === Lifespan Management ===


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - startup and shutdown"""

    # === STARTUP ===
    logger.info("=" * 80)
    logger.info("SecureClaw Gateway starting up...")

    # Load configuration
    try:
        app_state.config = load_config()
        logger.info("Configuration loaded successfully")
    except Exception as e:
        logger.critical(f"Failed to load configuration: {e}")
        raise

    # Set log level from config
    logging.getLogger().setLevel(app_state.config.log_level)

    # Initialize PII sanitizer
    try:
        app_state.sanitizer = PIISanitizer(app_state.config.pii)
        logger.info(f"PII sanitizer initialized (mode: {app_state.sanitizer.get_mode()})")
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

    # Record start time
    app_state.start_time = time.time()

    logger.info(
        f"SecureClaw Gateway ready at {app_state.config.bind}:{app_state.config.port}"
    )
    logger.info("=" * 80)

    yield

    # === SHUTDOWN ===
    logger.info("SecureClaw Gateway shutting down...")

    # Close ledger
    await app_state.ledger.close()

    logger.info("Shutdown complete")


# === Application ===

app = FastAPI(
    title="SecureClaw Gateway",
    description="Ingest API for the SecureClaw proxy layer framework",
    version="0.1.0",
    lifespan=lifespan,
)


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


# === Dependency: Authentication ===


async def auth_dep(request: Request) -> None:
    """Authentication dependency for protected endpoints"""
    dep = create_auth_dependency(app_state.config)
    await dep(request)


AuthRequired = Annotated[None, Depends(auth_dep)]


# === Endpoints ===


@app.get("/", response_class=HTMLResponse)
async def web_chat():
    """Web chat interface

    No authentication required for the HTML page.
    Authentication happens via JavaScript when calling /forward.
    """
    chat_html_path = Path(__file__).parent / "static" / "chat.html"
    if chat_html_path.exists():
        return chat_html_path.read_text()
    else:
        return "<h1>Chat interface not found</h1>"


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
        version="0.1.0",
        uptime_seconds=uptime,
        ledger_entries=stats.get("total_entries", 0),
        pending_approvals=len(pending),
        pii_engine=app_state.sanitizer.get_mode(),
        config_loaded=True,
    )


@app.post("/forward", response_model=ForwardResponse, status_code=status.HTTP_201_CREATED)
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
        response_data["agent_response"] = agent_response

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
async def approval_websocket(websocket: WebSocket):
    """WebSocket endpoint for real-time approval notifications

    Protocol:
    1. Client connects
    2. Client sends auth token as first message: {"token": "<token>"}
    3. Server validates token
    4. Server pushes new approval requests and decisions
    5. Client can send decisions: {"type": "decide", "request_id": "...", "approved": true}
    """
    await app_state.approval_queue.connect(websocket)

    try:
        # Wait for auth token
        auth_msg = await websocket.receive_json()
        token = auth_msg.get("token")

        if not token or token != app_state.config.auth_token:
            await websocket.send_json({"type": "error", "message": "Authentication failed"})
            await websocket.close()
            return

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
                    await websocket.send_json(
                        {"type": "error", "message": str(e)}
                    )

    except Exception as e:
        logger.warning(f"WebSocket error: {e}")

    finally:
        await app_state.approval_queue.disconnect(websocket)


# === Entry Point for Testing ===

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
