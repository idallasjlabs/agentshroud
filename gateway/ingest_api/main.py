# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""AgentShroud Gateway - Main FastAPI Application

Entry point for the gateway API. Wires together all components:
- PII sanitization
- Data ledger
- Multi-agent routing
- Approval queue
- Authentication
"""

import fnmatch
import hashlib
import logging
import os
import subprocess
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone
import hmac
from typing import Annotated, Optional

from fastapi import Depends, FastAPI, HTTPException, Query, Request, WebSocket, status
from pydantic import BaseModel
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
    EmailSendRequest,
    EmailSendResponse,
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
from ..security.prompt_guard import PromptGuard
from ..security.trust_manager import TrustManager, TrustLevel
from ..security.egress_filter import EgressFilter
from .middleware import MiddlewareManager
from .event_bus import EventBus, make_event
from ..proxy.http_proxy import ALLOWED_DOMAINS, HTTPConnectProxy
from ..proxy.mcp_proxy import MCPProxy, MCPToolCall, MCPToolResult
from ..proxy.mcp_config import MCPProxyConfig
from ..proxy.web_config import WebProxyConfig
from ..proxy.web_proxy import WebProxy
from ..proxy.webhook_receiver import WebhookReceiver
from ..proxy.pipeline import SecurityPipeline
from ..web.api import router as management_api_router
from ..web.management import router as management_dashboard_router
from .version_routes import router as version_router

# === Credential Isolation (P2) ===

# Allowed op:// reference patterns for the gateway op-proxy.
# Uses fnmatch glob syntax: * matches any characters within a path segment.
# Add entries here when the bot legitimately needs access to a new secret.
_ALLOWED_OP_PATHS: list[str] = [
    "op://Agent Shroud Bot Credentials/*",
]


def _is_op_reference_allowed(reference: str) -> bool:
    """Return True if the op:// reference matches an allowed path pattern."""
    if not reference or not reference.startswith("op://"):
        return False
    # Reject path traversal attempts
    if ".." in reference:
        return False
    for pattern in _ALLOWED_OP_PATHS:
        if fnmatch.fnmatch(reference, pattern):
            return True
    return False


class OpProxyRequest(BaseModel):
    """Request body for POST /credentials/op-proxy."""

    reference: str  # e.g. "op://AgentShroud Bot Credentials/API Keys/openai"


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
    prompt_guard: PromptGuard
    trust_manager: TrustManager
    egress_filter: EgressFilter
    mcp_proxy: Optional[MCPProxy]
    pipeline: Optional[SecurityPipeline]
    start_time: float
    event_bus: EventBus
    http_proxy: Optional[HTTPConnectProxy]


app_state = AppState()


# === Lifespan Management ===


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - startup and shutdown"""

    # === STARTUP ===
    logger.info("=" * 80)
    logger.info("AgentShroud Gateway starting up...")

    # Load 1Password service account token first — bot op-proxy calls depend on it
    # being available as early as possible to minimize startup race window.
    _op_token_file = os.getenv("OP_SERVICE_ACCOUNT_TOKEN_FILE")
    if _op_token_file and not os.getenv("OP_SERVICE_ACCOUNT_TOKEN"):
        try:
            os.environ["OP_SERVICE_ACCOUNT_TOKEN"] = Path(_op_token_file).read_text().strip()
            logger.info("1Password service account token loaded")
        except OSError as e:
            logger.warning(f"Could not load 1Password service account token: {e}")

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

    # Initialize security components
    try:
        app_state.prompt_guard = PromptGuard(block_threshold=0.8, warn_threshold=0.4)
        logger.info("PromptGuard initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize PromptGuard: {e}")
        raise

    try:
        app_state.trust_manager = TrustManager()
        app_state.trust_manager.register_agent("default")
        # Elevate default agent to STANDARD so internal API calls work
        app_state.trust_manager._conn.execute(
            "UPDATE trust_scores SET score = 200, level = ? WHERE agent_id = ?",
            (int(TrustLevel.STANDARD), "default")
        )
        app_state.trust_manager._conn.commit()
        logger.info("TrustManager initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize TrustManager: {e}")
        raise

    try:
        app_state.egress_filter = EgressFilter()
        logger.info("EgressFilter initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize EgressFilter: {e}")
        raise
    # Initialize P1 middleware manager
    try:
        app_state.middleware_manager = MiddlewareManager()
        logger.info("P1 MiddlewareManager initialized")
    except Exception as e:
        logger.critical(f"Failed to initialize MiddlewareManager: {e}")
        raise

    # Wire log sanitizer into Python logging
    try:
        log_sanitizer = app_state.middleware_manager.get_log_sanitizer()
        if log_sanitizer:
            # Add the log sanitizer filter to all handlers
            for handler in logging.getLogger().handlers:
                handler.addFilter(log_sanitizer)
            logger.info("Log sanitizer wired into logging system")
        else:
            logger.warning("Log sanitizer not available - logging may contain sensitive data")
    except Exception as e:
        logger.warning(f"Failed to wire log sanitizer: {e}")


    # Initialize security pipeline
    app_state.pipeline = SecurityPipeline(
        prompt_guard=app_state.prompt_guard,
        pii_sanitizer=app_state.sanitizer,
        trust_manager=app_state.trust_manager,
        egress_filter=app_state.egress_filter,
        approval_queue=app_state.approval_queue,
    )
    logger.info("Security pipeline initialized")

    # Initialize MCP proxy — load server registry from agentshroud.yaml mcp_proxy section
    mcp_proxy_config = (
        MCPProxyConfig.from_dict(app_state.config.mcp_proxy_data)
        if app_state.config.mcp_proxy_data
        else MCPProxyConfig()
    )
    app_state.mcp_proxy = MCPProxy(config=mcp_proxy_config)
    logger.info(
        f"MCP proxy initialized: {len(mcp_proxy_config.servers)} server(s) registered"
    )

    # Initialize SSH proxy
    if app_state.config.ssh.enabled:
        app_state.ssh_proxy = SSHProxy(app_state.config.ssh)
        logger.info("SSH proxy initialized")
    else:
        app_state.ssh_proxy = None

    # Initialize event bus
    app_state.event_bus = EventBus()
    logger.info("Event bus initialized")

    # Initialize HTTP CONNECT proxy (port 8181)
    # Activated in the FINAL PR by setting HTTP_PROXY on the bot container.
    # Running it now adds zero risk — the bot doesn't use it until then.
    try:
        # Use allowed_domains from agentshroud.yaml (proxy.allowed_domains),
        # falling back to the hardcoded default if the YAML section is absent.
        _proxy_domains = app_state.config.proxy_allowed_domains or ALLOWED_DOMAINS
        _web_proxy = WebProxy(config=WebProxyConfig(mode="allowlist", allowed_domains=_proxy_domains))
        app_state.http_proxy = HTTPConnectProxy(web_proxy=_web_proxy)
        await app_state.http_proxy.start()
        logger.info("HTTP CONNECT proxy started on port 8181")
    except Exception as e:
        logger.warning(f"HTTP CONNECT proxy failed to start: {e} (continuing)")
        app_state.http_proxy = None

    # Record start time
    app_state.start_time = time.time()

    logger.info(
        f"AgentShroud Gateway ready at {app_state.config.bind}:{app_state.config.port}"
    )
    logger.info("=" * 80)

    yield

    # === SHUTDOWN ===
    logger.info("AgentShroud Gateway shutting down...")

    # Stop HTTP CONNECT proxy
    if getattr(app_state, "http_proxy", None):
        await app_state.http_proxy.stop()

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
    if not hasattr(app_state, "config"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Service not initialized",
        )
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


@app.get("/proxy/status")
async def proxy_status(auth: AuthRequired):
    """HTTP CONNECT proxy traffic statistics.

    Shows allowed/blocked counts and recent requests.
    Returns enabled: false if the proxy failed to start.
    Authentication required.
    """
    if not getattr(app_state, "http_proxy", None):
        return {"enabled": False, "total": 0, "allowed": 0, "blocked": 0, "recent": []}
    stats = app_state.http_proxy.get_stats()
    return {"enabled": True, **stats}


@app.post("/credentials/op-proxy")
async def op_proxy(request: OpProxyRequest, auth: AuthRequired):
    """1Password credential proxy (P2: credential isolation).

    Reads a secret from 1Password on behalf of the bot. The bot sends an
    op:// reference; the gateway validates it against the allowlist and
    returns the value. This keeps the 1Password service account token on
    the gateway rather than the bot.

    Activated in the FINAL PR when OP_SERVICE_ACCOUNT_TOKEN is moved from
    the bot to the gateway. Until then, the gateway won't have the token
    and calls will fail with 502 — that's expected during development.

    Authentication required.
    """
    reference = request.reference

    # Validate op:// format
    if not reference.startswith("op://"):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="reference must start with op://",
        )

    # Validate against allowlist (also blocks path traversal)
    if not _is_op_reference_allowed(reference):
        logger.warning(f"op-proxy: disallowed reference blocked: {reference!r}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="op:// reference not in allowed paths",
        )

    # Call op read on the gateway (requires OP_SERVICE_ACCOUNT_TOKEN env var)
    try:
        result = subprocess.run(
            ["op", "read", reference],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except subprocess.TimeoutExpired:
        logger.error("op-proxy: 1Password read timed out")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="1Password read timed out",
        )
    except FileNotFoundError:
        logger.error("op-proxy: 'op' CLI not found on gateway")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="1Password CLI not available on gateway",
        )

    if result.returncode != 0:
        logger.error(f"op-proxy: op read failed (exit {result.returncode})")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to read secret from 1Password",
        )

    # Never log the value — only confirm success
    logger.info("op-proxy: secret read successfully for reference pattern")
    return {"value": result.stdout.strip()}


# === MCP Proxy (P4) ===


class MCPProxyRequest(BaseModel):
    """Request body for POST /mcp/proxy — intercept a single MCP tool call."""

    server_name: str
    tool_name: str
    parameters: dict = {}
    agent_id: str = "default"


@app.post("/mcp/proxy", status_code=status.HTTP_200_OK)
async def mcp_proxy_endpoint(request: MCPProxyRequest, auth: AuthRequired):
    """MCP tool call interception endpoint.

    Receives an MCP tool call, runs it through the security inspector
    (injection detection, PII scan, permission check), and returns the
    proxy result. The bot should send all MCP tool calls here before
    forwarding to the actual MCP server.

    Authentication required.
    """
    proxy = getattr(app_state, "mcp_proxy", None)
    if proxy is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="MCP proxy not initialized",
        )

    # iMessage recipient allowlist (P5: iMessage channel ownership).
    # Checked before security inspection so unknown recipients never reach the tool.
    if request.server_name == _IMESSAGE_SERVER and request.tool_name == _IMESSAGE_SEND_TOOL:
        recipient = request.parameters.get("to", "")
        config = getattr(app_state, "config", None)
        allowed = config.channels.imessage_allowed_recipients if config else []
        if not _is_imessage_recipient_allowed(recipient, allowed):
            approval_queue = getattr(app_state, "approval_queue", None)
            if approval_queue:
                approval_req = ApprovalRequest(
                    action_type="imessage_sending",
                    description=f"Send iMessage to {recipient}",
                    details={
                        "to": recipient,
                        "body": str(request.parameters.get("body", ""))[:200],
                    },
                    agent_id=request.agent_id,
                )
                item = await approval_queue.submit(approval_req)
                logger.info(f"imessage-send: queued for approval (id={item.request_id})")
                return JSONResponse(
                    status_code=status.HTTP_202_ACCEPTED,
                    content={"status": "queued", "approval_id": item.request_id},
                )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="iMessage recipient not in allowlist and no approval queue available",
            )

    tool_call = MCPToolCall(
        id="",  # auto-generated in __post_init__
        server_name=request.server_name,
        tool_name=request.tool_name,
        parameters=request.parameters,
        agent_id=request.agent_id,
    )

    result = await proxy.process_tool_call(tool_call, execute=False)

    if result.blocked:
        logger.warning(
            f"MCP proxy blocked tool call: server={request.server_name} "
            f"tool={request.tool_name} agent={request.agent_id} "
            f"reason={result.block_reason}"
        )
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Tool call blocked: {result.block_reason}",
        )

    return {
        "allowed": result.allowed,
        "call_id": result.call_id,
        "sanitized_params": result.sanitized_params,
        "audit_entry_id": result.audit_entry_id,
        "findings_count": result.findings_count,
        "threat_level": result.threat_level,
        "processing_time_ms": result.processing_time_ms,
    }


class MCPResultRequest(BaseModel):
    """Request body for POST /mcp/result — submit a tool result for outbound audit."""

    server_name: str
    tool_name: str
    call_id: str = ""
    content: Optional[dict] = None
    agent_id: str = "default"


@app.post("/mcp/result", status_code=status.HTTP_200_OK)
async def mcp_result_endpoint(request: MCPResultRequest, auth: AuthRequired):
    """MCP tool result outbound audit endpoint.

    Receives a tool result from the bot's mcp-proxy-wrapper.js after the actual
    MCP server has executed the call. Runs it through the security inspector for
    PII/credential scanning and logs to the tamper-evident audit trail.

    Results are never blocked — only redacted and audited.
    Authentication required.
    """
    proxy = getattr(app_state, "mcp_proxy", None)
    if proxy is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="MCP proxy not initialized",
        )

    tool_result = MCPToolResult(
        call_id=request.call_id,
        server_name=request.server_name,
        tool_name=request.tool_name,
        content=request.content,
    )

    result = await proxy.process_tool_result(tool_result, agent_id=request.agent_id)

    return {
        "audit_entry_id": result.audit_entry_id,
        "findings_count": result.findings_count,
        "threat_level": result.threat_level,
        "sanitized_result": result.sanitized_result,
        "processing_time_ms": result.processing_time_ms,
    }


# === Channel Ownership (P3) ===
#
# Telegram: all inbound messages route through WebhookReceiver + SecurityPipeline
# Email:    bot submits send requests here; gateway validates, scans PII, and
#           either approves or queues for human review.
#
# Activated now. The bot uses these endpoints once it's updated to call the
# gateway instead of sending directly (FINAL PR wires docker-compose).

# Allowed recipient list for email_send — add addresses as needed.
# Empty list = all recipients require approval queue.
_EMAIL_ALLOWED_RECIPIENTS: list[str] = [
    # Fill in trusted addresses; unknown recipients always go to approval queue.
]


def _is_email_recipient_allowed(address: str) -> bool:
    """Return True if the email address is on the pre-approved recipient list."""
    return address.lower().strip() in {r.lower() for r in _EMAIL_ALLOWED_RECIPIENTS}


# iMessage channel ownership (P5)
_IMESSAGE_SERVER = "mac-messages"
_IMESSAGE_SEND_TOOL = "tool_send_message"


def _is_imessage_recipient_allowed(recipient: str, allowed: list[str]) -> bool:
    """Return True if the iMessage recipient is on the pre-approved list."""
    return recipient.strip() in {r.strip() for r in allowed}


@app.post("/webhook/telegram")
async def telegram_webhook(request: Request, auth: AuthRequired):
    """Telegram inbound webhook (P3: channel ownership).

    All Telegram messages destined for the bot pass through this endpoint.
    Messages are scanned for prompt injection and PII before being forwarded.
    Authentication required.
    """
    try:
        payload = await request.json()
    except Exception:
        payload = {}

    # Build receiver using available app_state components
    pipeline = getattr(app_state, "pipeline", None)
    forwarder = getattr(app_state, "forwarder", None)
    receiver = WebhookReceiver(pipeline=pipeline, forwarder=forwarder)

    result = await receiver.process_webhook(payload, source="telegram")
    logger.info(f"telegram-webhook: status={result.get('status')}")
    return result


@app.post("/email/send", status_code=status.HTTP_200_OK)
async def email_send(request: EmailSendRequest, auth: AuthRequired):
    """Email send gateway (P3: channel ownership).

    The bot submits email send requests here instead of calling Gmail directly.
    Controls:
    - PII scan on body (redacts before logging)
    - Recipient allowlist: known addresses return 200 (approved)
    - Unknown recipients: submitted to approval queue → 202 (queued)

    Authentication required.
    """
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # PII scan on body
    sanitizer = getattr(app_state, "sanitizer", None)
    pii_redacted = False
    sanitized_body = request.body
    if sanitizer:
        try:
            scan = sanitizer.sanitize(request.body)
            sanitized_body = scan.sanitized_content
            pii_redacted = len(scan.redactions) > 0
            if pii_redacted:
                logger.warning(
                    f"email-send: PII redacted from body ({len(scan.redactions)} items)"
                )
        except Exception as e:
            logger.warning(f"email-send: PII scan failed ({e}), proceeding with original body")

    # Recipient allowlist check
    if _is_email_recipient_allowed(request.to):
        logger.info("email-send: approved for allowed recipient")
        return EmailSendResponse(
            status="approved",
            sanitized_body=sanitized_body,
            pii_redacted=pii_redacted,
            timestamp=now,
        )

    # Unknown recipient → queue for approval
    approval_queue = getattr(app_state, "approval_queue", None)
    if approval_queue:
        approval_req = ApprovalRequest(
            action_type="email_sending",
            description=f"Send email to {request.to}: {request.subject}",
            details={
                "to": request.to,
                "subject": request.subject,
                "body": sanitized_body,
                "pii_redacted": pii_redacted,
            },
            agent_id=request.agent_id,
        )
        item = await approval_queue.submit(approval_req)
        logger.info(f"email-send: queued for approval (id={item.request_id})")
        from fastapi.responses import JSONResponse as _JSONResponse
        return _JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content=EmailSendResponse(
                status="queued",
                sanitized_body=sanitized_body,
                pii_redacted=pii_redacted,
                approval_id=item.request_id,
                timestamp=now,
            ).model_dump(),
        )

    # No approval queue available (e.g. during startup or tests) — block send
    logger.warning("email-send: unknown recipient blocked (no approval queue available)")
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Recipient not in allowlist and no approval queue available",
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

    # Step 0: P1 Middleware Security Processing
    middleware_manager = getattr(app_state, "middleware_manager", None)
    if middleware_manager:
        try:
            # Prepare request data for middleware processing
            request_data = {
                "message": request.content,
                "content_type": request.content_type,
                "source": request.source,
                "headers": {}  # Add headers if available in request
            }

            # Process through middleware
            middleware_result = middleware_manager.process(request_data, "unknown")

            if not middleware_result.allowed:
                logger.warning(f"Middleware blocked request: {middleware_result.reason}")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Request blocked by middleware: {middleware_result.reason}"
                )

            # If middleware modified the request, update it
            if middleware_result.modified_request:
                if "message" in middleware_result.modified_request:
                    request.content = middleware_result.modified_request["message"]
                logger.info("Request modified by middleware")

        except HTTPException:
            # Re-raise HTTP exceptions (these are intentional blocks)
            raise
        except Exception as e:
            logger.error(f"Middleware processing error: {e}")
            # Fail closed - block request on middleware error
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Middleware processing failed. Request blocked for safety."
            )
    else:
        logger.warning("MiddlewareManager not available - middleware security checks skipped")

    # Step 1: Run through security pipeline (injection scan + PII sanitization + audit)
    pipeline = getattr(app_state, "pipeline", None)
    audit_entry_id: str = ""
    audit_hash: str = ""
    prompt_score: float = 0.0
    if pipeline:
        try:
            pipeline_result = await pipeline.process_inbound(
                message=request.content,
                agent_id="default",
                action="send_message",
                source=request.source,
            )
        except Exception as e:
            logger.error(f"Security pipeline failed: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Content security check failed. Request blocked for safety.",
            )
        if pipeline_result.blocked:
            logger.warning(
                f"Pipeline blocked request: {pipeline_result.block_reason} "
                f"(source={request.source})"
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Request blocked: {pipeline_result.block_reason}",
            )
        if pipeline_result.queued_for_approval:
            return JSONResponse(
                status_code=status.HTTP_202_ACCEPTED,
                content={"status": "queued", "approval_id": pipeline_result.approval_id},
            )
        sanitized_content = pipeline_result.sanitized_message
        sanitized = pipeline_result.pii_redaction_count > 0
        entity_types_found = pipeline_result.pii_redactions
        redaction_count = pipeline_result.pii_redaction_count
        audit_entry_id = pipeline_result.audit_entry_id
        audit_hash = pipeline_result.audit_hash
        prompt_score = pipeline_result.prompt_score
    else:
        # Fallback: inline PII sanitization (no pipeline available)
        try:
            sanitization_result = await app_state.sanitizer.sanitize(request.content)
        except Exception as e:
            logger.error(f"PII sanitization failed: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Content sanitization failed. Request blocked for safety.",
            )
        sanitized_content = sanitization_result.sanitized_content
        sanitized = len(sanitization_result.redactions) > 0
        entity_types_found = sanitization_result.entity_types_found
        redaction_count = len(sanitization_result.redactions)

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
            redaction_count=redaction_count,
            redaction_types=entity_types_found,
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
                f"{redaction_count} PII entities redacted",
                {
                    "types": entity_types_found,
                    "count": redaction_count,
                },
                "warning",
            )
        )

    # Step 5: Return response
    response_data = {
        "id": ledger_entry.id,
        "sanitized": sanitized,
        "redactions": entity_types_found,
        "redaction_count": redaction_count,
        "content_hash": ledger_entry.content_hash,
        "forwarded_to": forwarded_to,
        "timestamp": ledger_entry.timestamp,
        "audit_entry_id": audit_entry_id or None,
        "audit_hash": audit_hash or None,
        "prompt_score": prompt_score if prompt_score > 0.0 else None,
    }

    # Include agent response if available
    if agent_response:
        # Step 5.0: Filter out Claude XML internal blocks and run outbound PII scan
        if pipeline:
            out_result = await pipeline.process_outbound(
                response=agent_response, agent_id="default"
            )
            filtered_response = out_result.sanitized_message
        else:
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
