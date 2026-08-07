# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Message forwarding routes.

Core message forwarding endpoints:
- /webhook/telegram - Telegram inbound webhook
- /email/send - Email sending gateway
- /forward - Main ingest endpoint for content forwarding
"""

import json
import logging
import os
import re
import smtplib
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated, AsyncIterator, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from ...proxy.webhook_receiver import WebhookReceiver
from ..auth import create_auth_dependency
from ..email_service import GatewayEmailService
from ..event_bus import make_event
from ..models import (
    AgentTarget,
    ApprovalRequest,
    EmailSendRequest,
    EmailSendResponse,
    ForwardRequest,
    ForwardResponse,
)
from ..router import ForwardError
from ..state import app_state

# Create router
router = APIRouter()

# Set up logger
logger = logging.getLogger(__name__)

# Email configuration
_EMAIL_ALLOWED_RECIPIENTS: list[str] = [
    "idallasj@gmail.com",
]
_EMAIL_SENDER = "agentshroud.ai@gmail.com"
_EMAIL_OP_REF = "op://Agent Shroud Bot Credentials/AgentShroud - Google/gmail app password"
_EMAIL_SMTP_HOST = "smtp.gmail.com"
_EMAIL_SMTP_PORT = 465

# Single owner-comms email transport (SCRUM-77).  Injectable in tests so no test
# opens a real SMTP connection; policy (allowlist/PII/approval/credentials) stays
# in the endpoint below.
_email_service = GatewayEmailService(_EMAIL_SENDER, _EMAIL_SMTP_HOST, _EMAIL_SMTP_PORT)


def _get_gmail_app_password() -> "str | None":
    """Read Gmail app password from 1Password using the gateway's cached session."""
    session = os.environ.get("OP_SESSION", "")

    def _run(sess: str) -> "subprocess.CompletedProcess[str]":
        return subprocess.run(
            ["op", "read", "--session", sess, _EMAIL_OP_REF],
            capture_output=True,
            text=True,
            timeout=30,
        )

    result = _run(session) if session else None
    if not result or result.returncode != 0:
        secrets = "/run/secrets"
        try:
            email = Path(f"{secrets}/1password_bot_email").read_text().strip()
            password = Path(f"{secrets}/1password_bot_master_password").read_text().strip()
            key_path = Path(f"{secrets}/1password_bot_secret_key")
            key = key_path.read_text().strip() if key_path.exists() else ""
        except OSError:
            return None
        if key:
            r = subprocess.run(
                [
                    "op",
                    "account",
                    "add",
                    "--address",
                    "my.1password.com",
                    "--email",
                    email,
                    "--secret-key",
                    key,
                    "--signin",
                    "--raw",
                ],
                input=password,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if r.returncode == 0 and r.stdout.strip():
                os.environ["OP_SESSION"] = r.stdout.strip()
                result = _run(r.stdout.strip())
        if not result or result.returncode != 0:
            r = subprocess.run(
                ["op", "signin", "--raw"],
                input=password,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if r.returncode == 0 and r.stdout.strip():
                os.environ["OP_SESSION"] = r.stdout.strip()
                result = _run(r.stdout.strip())

    return (
        result.stdout.strip()
        if result and result.returncode == 0 and result.stdout.strip()
        else None
    )


# Authentication dependency
async def auth_dep(request: Request):
    """Auth dependency that uses the app state config."""
    if not hasattr(app_state, "config"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Service not initialized",
        )
    dep = create_auth_dependency(app_state.config)
    await dep(request)


AuthRequired = Annotated[None, Depends(auth_dep)]


# Helper functions
def _is_email_recipient_allowed(address: str) -> bool:
    """Return True if the email address is on the pre-approved recipient list."""
    return address.lower().strip() in {r.lower() for r in _EMAIL_ALLOWED_RECIPIENTS}


# Route endpoints
@router.post("/webhook/telegram")
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

    # Access app_state via request.app.state.app_state

    # Build receiver using available app_state components
    pipeline = getattr(app_state, "pipeline", None)
    forwarder = getattr(app_state, "forwarder", None)
    session_manager = getattr(app_state, "session_manager", None)
    receiver = WebhookReceiver(
        pipeline=pipeline, forwarder=forwarder, session_manager=session_manager
    )

    result = await receiver.process_webhook(payload, source="telegram")
    logger.info(f"telegram-webhook: status={result.get('status')}")
    return result


@router.post("/email/send", status_code=status.HTTP_200_OK)
async def email_send(request: EmailSendRequest, req: Request, auth: AuthRequired):
    """Email send gateway (P3: channel ownership).

    The bot submits email send requests here instead of calling Gmail directly.
    The bot container has no internet access; this endpoint sends via SMTP_SSL
    on the gateway. Controls:
    - PII scan on body (redacts before sending)
    - Recipient allowlist: known addresses are sent immediately
    - Unknown recipients: submitted to approval queue → 202 (queued)

    Authentication required.
    """
    import asyncio

    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Recipient allowlist check — run BEFORE PII scan.
    # Owner-bound mail (allowlisted recipients) is trusted: the owner is allowed to see
    # their own report content verbatim.  PII redaction on a competitive-intel / CVE report
    # addressed to the operator would collapse the body into <PERSON>/<ORGANIZATION>/<US_SSN>
    # tags (CVE-YYYY-NNNN matches the US_SSN regex) and produce an empty email.
    # Non-allowlisted recipients still get the full Presidio+regex scrub before the
    # approval queue, which is the correct trust boundary.
    recipient_allowed = _is_email_recipient_allowed(request.to)
    pii_redacted = False
    sanitized_body = request.body
    if not recipient_allowed:
        sanitizer = getattr(app_state, "sanitizer", None)
        if sanitizer:
            try:
                scan = await sanitizer.sanitize(request.body)
                sanitized_body = scan.sanitized_content
                pii_redacted = len(scan.redactions) > 0
                if pii_redacted:
                    logger.warning(
                        "email-send: PII redacted from body (%d items)",
                        len(scan.redactions),
                    )
            except Exception as e:
                logger.error("email-send: PII scan failed (%s), blocking email (fail-closed)", e)
                sanitized_body = "[EMAIL BLOCKED: PII scan failed — content withheld]"
                pii_redacted = True

    if not recipient_allowed:
        # Unknown recipient → queue for approval
        approval_queue = getattr(app_state, "approval_queue", None)
        if approval_queue:
            approval_req = ApprovalRequest(
                action_type="email_sending",
                description=f"Send email to {request.to}: {request.subject}",
                details={
                    "to": request.to,
                    "subject": request.subject,
                    "body": sanitized_body[:500],
                    "pii_redacted": pii_redacted,
                },
                agent_id=request.agent_id,
            )
            item = await approval_queue.submit(approval_req)
            logger.info("email-send: queued for approval (id=%s)", item.request_id)
            return JSONResponse(
                status_code=status.HTTP_202_ACCEPTED,
                content=EmailSendResponse(
                    status="queued",
                    sanitized_body=sanitized_body,
                    pii_redacted=pii_redacted,
                    approval_id=item.request_id,
                    timestamp=now,
                ).model_dump(),
            )
        logger.warning("email-send: unknown recipient blocked (no approval queue available)")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Recipient not in allowlist and no approval queue available",
        )

    # Retrieve Gmail app password from 1Password
    loop = asyncio.get_event_loop()
    try:
        app_password = await loop.run_in_executor(None, _get_gmail_app_password)
    except Exception as e:
        logger.error("email-send: credential retrieval error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Failed to retrieve email credentials",
        )
    if not app_password:
        logger.error("email-send: Gmail app password not available")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Email credentials not available",
        )

    # Send via the consolidated owner-comms transport (SCRUM-77).  MIME build +
    # SMTP login/sendmail live in GatewayEmailService; the transport is
    # injectable so tests never open a real connection.
    is_html = getattr(request, "is_html", False)
    try:
        await loop.run_in_executor(
            None,
            _email_service.send,
            request.to,
            request.subject,
            sanitized_body,
            is_html,
            app_password,
        )
        logger.info("email-send: sent to %s subject=%r", request.to, request.subject)
    except smtplib.SMTPAuthenticationError as e:
        logger.error("email-send: SMTP auth failed: %s", e)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"SMTP authentication failed: {e}",
        )
    except Exception as e:
        logger.error("email-send: SMTP error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Failed to send email: {e}",
        )

    return EmailSendResponse(
        status="approved",
        sanitized_body=sanitized_body if pii_redacted else None,
        pii_redacted=pii_redacted,
        approval_id=None,
        timestamp=now,
    )


class OwnerEmailRequest(BaseModel):
    subject: str = Field(..., max_length=998)
    body: str = Field(..., max_length=100_000)
    is_html: bool = Field(False)


@router.post("/email/send-owner", status_code=status.HTTP_200_OK)
async def email_send_owner(request: OwnerEmailRequest, req: Request, auth: AuthRequired):
    """Send an email to the owner without exposing the recipient address in the request.

    Identical to /email/send but the recipient is always _EMAIL_ALLOWED_RECIPIENTS[0]
    (currently idallasj@gmail.com). Use this from cron jobs so the owner's email
    never appears in the LLM prompt where the PII scanner would redact it.

    Authentication required.
    """
    inner = EmailSendRequest(
        to=_EMAIL_ALLOWED_RECIPIENTS[0],
        subject=request.subject,
        body=request.body,
        is_html=request.is_html,
    )
    # Delegate to the existing handler — reuse all SMTP + PII logic
    return await email_send(inner, req, auth)


def _resolve_user_trust_level(pipeline, target: AgentTarget, request: ForwardRequest) -> str:
    """Resolve the outbound trust level for `request`, shared by the blocking
    and streaming forward paths so both apply identical redaction behavior.

    Security: request.user_id is trusted here because /forward (and
    /forward/stream) require gateway auth (AuthRequired) and the user_id
    field is set by the authenticated bot/voice-gateway, not by an
    untrusted end user. FULL trust still keeps credential:False
    (outbound_filter.py:96) and block_credentials() still runs downstream
    of every caller, so raw secrets are never delivered regardless of
    trust level.
    """
    user_trust_level = "UNTRUSTED"
    if pipeline.trust_manager:
        trust_info = pipeline.trust_manager.get_trust(target.name)
        if trust_info:
            trust_score = trust_info[0]
            if trust_score >= 400:
                user_trust_level = "FULL"
            elif trust_score >= 300:
                user_trust_level = "ELEVATED"
            elif trust_score >= 200:
                user_trust_level = "STANDARD"
            elif trust_score >= 100:
                user_trust_level = "BASIC"

    # Owner-authenticated requests (voice admin interface, owner DMs, API calls
    # carrying the owner's user_id) receive FULL trust so operational detail
    # such as hostnames and ports is spoken/shown rather than redacted.
    if user_trust_level != "FULL":
        _owner_uid = getattr(pipeline, "_owner_user_id", None)
        if _owner_uid and str(getattr(request, "user_id", "") or "") == str(_owner_uid):
            user_trust_level = "FULL"
    return user_trust_level


@dataclass
class _InboundResult:
    """Everything the post-routing forwarding steps (blocking or streaming)
    need, once inbound target resolution + security processing has run."""

    target: AgentTarget
    sanitized_content: str
    sanitized: bool
    entity_types_found: list
    redaction_count: int
    audit_entry_id: str
    audit_hash: str
    prompt_score: float
    early_response: Optional[JSONResponse] = None
    """Set (non-None) when the pipeline queued the request for approval —
    the caller MUST return this immediately and skip forwarding."""


async def _process_inbound(request: ForwardRequest, req: Request) -> _InboundResult:
    """Target resolution + P1 middleware + inbound security pipeline —
    shared by the blocking `/forward` and streaming `/forward/stream` routes
    so both get identical routing/anti-spoof/PII/audit behavior. Pure
    extraction from the original single-endpoint `forward_content` body;
    do not change behavior here without updating both callers' tests.
    """
    logger.info(
        f"Ingest request: source={request.source}, "
        f"type={request.content_type}, size={len(request.content)}"
    )

    # Resolve routing target before the security pipeline so the correct bot's
    # agent_id flows into TrustManager, EgressFilter, and audit logs.
    try:
        target = await app_state.router.resolve_target(request)
    except Exception as e:
        logger.error(f"Routing failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to resolve routing target",
        )

    # WS-E SCRUM-73/74 — owner-identity anti-spoof.
    # /forward authenticates only a single shared Bearer token; the token proves
    # possession, NOT owner identity.  The body ``user_id`` field is therefore
    # attacker-controlled: any token holder could set it to the owner's (public,
    # guessable) Telegram ID and receive the pipeline's owner exemption
    # (PromptGuard / ContextGuard / injection-scanner / PII bypass) plus FULL
    # outbound trust (below at forward.py FULL-trust resolution).
    #
    # Mirror the existing /mcp/proxy defence
    # (gateway/ingest_api/main.py::_resolve_effective_agent_id): a body ``user_id``
    # is only allowed to CLAIM the owner identity when a trusted
    # ``X-AgentShroud-User-Id`` header corroborates it (set by the voice-gateway
    # at voice_gateway/server.py and by trusted internal callers).  Without a
    # matching trusted header, an owner-ID claim is dropped to "anonymous" so the
    # pipeline never grants owner privileges.  Non-owner user_ids are unaffected
    # (they grant no exemption regardless).
    _owner_id = None
    _pipeline_for_owner = getattr(app_state, "pipeline", None)
    if _pipeline_for_owner is not None:
        _owner_id = getattr(_pipeline_for_owner, "_owner_user_id", None)
    if _owner_id is None:
        try:
            from gateway.security.rbac_config import RBACConfig

            _owner_id = RBACConfig().owner_user_id
        except Exception:
            _owner_id = None
    _body_user_id = getattr(request, "user_id", None)
    if _owner_id and _body_user_id is not None and str(_body_user_id) == str(_owner_id):
        _trusted_header = (req.headers.get("x-agentshroud-user-id") or "").strip()
        if str(_trusted_header) != str(_owner_id):
            logger.warning(
                "Owner-identity spoof rejected on /forward: body user_id claimed owner "
                "without a matching X-AgentShroud-User-Id header (source=%s)",
                request.source,
            )
            request.user_id = None

    # Step 0: P1 Middleware Security Processing
    middleware_manager = getattr(app_state, "middleware_manager", None)
    if middleware_manager:
        try:
            # bot_id: use the routing target's logical name (e.g. "openclaw", "hermes")
            # so that session isolation and audit logs are scoped per-bot.
            bot_id = getattr(target, "name", "openclaw") or "openclaw"

            # Prepare request data for middleware processing
            request_data = {
                "message": request.content,
                "content_type": request.content_type,
                "source": request.source,
                "headers": {},  # Add headers if available in request
                "user_id": getattr(request, "user_id", None)
                or getattr(request, "source", "anonymous"),
                # bot_id scopes the session workspace and audit log entry to the
                # correct bot so that OpenClaw and Hermes data never merge.
                "bot_id": bot_id,
            }

            # Process through middleware
            middleware_result = await middleware_manager.process_request(request_data, bot_id)

            if not middleware_result.allowed:
                logger.warning(f"Middleware blocked request: {middleware_result.reason}")
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Request blocked by middleware: {middleware_result.reason}",
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
                detail="Middleware processing failed. Request blocked for safety.",
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
                agent_id=target.name,
                action="send_message",
                source=request.source,
                # Pass the caller's user_id so process_inbound can resolve is_owner
                # and exempt the authenticated owner from PII redaction.  The accessor
                # mirrors forward.py:382 where the same field is already read for
                # middleware.  When user_id is absent (anonymous API calls) this is
                # None → is_owner stays False → PII sanitization runs as normal.
                metadata={"user_id": getattr(request, "user_id", None)},
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
            return _InboundResult(
                target=target,
                sanitized_content="",
                sanitized=False,
                entity_types_found=[],
                redaction_count=0,
                audit_entry_id="",
                audit_hash="",
                prompt_score=0.0,
                early_response=JSONResponse(
                    status_code=status.HTTP_202_ACCEPTED,
                    content={
                        "status": "queued",
                        "approval_id": pipeline_result.approval_id,
                    },
                ),
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
        audit_entry_id = ""
        audit_hash = ""
        prompt_score = 0.0

    return _InboundResult(
        target=target,
        sanitized_content=sanitized_content,
        sanitized=sanitized,
        entity_types_found=entity_types_found,
        redaction_count=redaction_count,
        audit_entry_id=audit_entry_id,
        audit_hash=audit_hash,
        prompt_score=prompt_score,
    )


@router.post("/forward", response_model=ForwardResponse, status_code=status.HTTP_201_CREATED)
async def forward_content(request: ForwardRequest, req: Request, auth: AuthRequired):
    """Main ingest endpoint

    Receives data from iOS Shortcuts, browser extension, or API.
    Sanitizes PII, logs to ledger, and forwards to agent.

    Authentication required.
    """
    inbound = await _process_inbound(request, req)
    if inbound.early_response is not None:
        return inbound.early_response
    target = inbound.target
    sanitized_content = inbound.sanitized_content
    sanitized = inbound.sanitized
    entity_types_found = inbound.entity_types_found
    redaction_count = inbound.redaction_count
    audit_entry_id = inbound.audit_entry_id
    audit_hash = inbound.audit_hash
    prompt_score = inbound.prompt_score

    # Step 2 (routing target already resolved above)
    # Re-fetch pipeline here — _process_inbound() uses its own local reference
    # for inbound processing; the outbound-filtering step below (Step 5) needs
    # the same object. getattr is cheap/side-effect-free, safe to call twice.
    pipeline = getattr(app_state, "pipeline", None)

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
        logger.debug(f"agent_response type={type(agent_response).__name__}")

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
        # Non-critical - content was already forwarded successfully.
        # Returning 500 would cause callers to retry, duplicating delivery.
        # Use a sentinel so downstream code can build a degraded response.
        ledger_entry = None

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
        "id": ledger_entry.id if ledger_entry else "ledger-unavailable",
        "sanitized": sanitized,
        "redactions": entity_types_found,
        "redaction_count": redaction_count,
        "content_hash": ledger_entry.content_hash if ledger_entry else "",
        "forwarded_to": forwarded_to,
        "timestamp": ledger_entry.timestamp if ledger_entry else "",
        "audit_entry_id": audit_entry_id or None,
        "audit_hash": audit_hash or None,
        "prompt_score": prompt_score if prompt_score > 0.0 else None,
    }

    # Include agent response if available
    if agent_response:
        # Step 5.0: Filter out Claude XML internal blocks and run outbound PII scan
        if pipeline:
            user_trust_level = _resolve_user_trust_level(pipeline, target, request)

            # agent_response may be dict (non-OpenAI targets) or str (OpenAI);
            # process_outbound expects str, so coerce to avoid AttributeError.
            _response_text = (
                agent_response if isinstance(agent_response, str) else str(agent_response)
            )
            out_result = await pipeline.process_outbound(
                response=_response_text,
                agent_id=target.name,
                user_trust_level=user_trust_level,
                source=request.source,
            )
            if out_result.blocked:
                # Never deliver content the pipeline blocked — sanitized_message
                # may still carry the original text for audit purposes.
                logger.warning(
                    "Outbound agent response blocked by pipeline for source=%s: %s",
                    request.source,
                    out_result.block_reason,
                )
                filtered_response = "[Response blocked by AgentShroud security policy]"
            else:
                filtered_response = out_result.sanitized_message
        else:
            _response_text_fallback = (
                agent_response if isinstance(agent_response, str) else str(agent_response)
            )
            filtered_response, xml_was_filtered = app_state.sanitizer.filter_xml_blocks(
                _response_text_fallback
            )
            if xml_was_filtered:
                logger.info(f"Filtered XML blocks from agent response for source={request.source}")

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
                original_content=str(agent_response)[:100],  # First 100 chars for audit
                sanitized=True,
                redaction_count=1,
                redaction_types=["CREDENTIALS"],
                forwarded_to="blocked",
                content_type="security_event",
                metadata={"original_ledger_id": ledger_entry.id},
            )

        response_data["agent_response"] = blocked_response

    return response_data


# ── /forward/stream — streaming voice pipeline ──────────────────────────────
# Lets voice_gateway start TTS on the FIRST sentence of an agent reply instead
# of waiting for the entire response. Security parity with the blocking
# /forward path is maintained by running the SAME process_outbound() +
# block_credentials() checks — just per sliding sentence-window instead of
# once on the complete text. See SCRUM ticket / owner conversation 2026-08-06
# for why: voice was "nearly unusable" waiting for full-response generation
# before any audio began.

_SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+")
# A control-picture character, not valid in normal spoken text — used to mark
# the join point between the two sentences in a filter window so the result
# can be split back apart after process_outbound() has run on the combined
# text (giving the filter cross-sentence context without losing the ability
# to release only the OLDER half of the window).
_WINDOW_SENTINEL = "␞"


async def _sentences_from_deltas(deltas: AsyncIterator[str]) -> AsyncIterator[str]:
    """Buffer streamed text deltas and yield each complete sentence as soon as
    its boundary is crossed. Any trailing fragment with no terminal
    punctuation is flushed once the delta stream ends."""
    buf = ""
    async for delta in deltas:
        buf += delta
        parts = _SENTENCE_BOUNDARY_RE.split(buf)
        for complete in parts[:-1]:
            complete = complete.strip()
            if complete:
                yield complete
        buf = parts[-1]
    tail = buf.strip()
    if tail:
        yield tail


async def _filtered_sentence_stream(
    sentences: AsyncIterator[str],
    pipeline,
    agent_id: str,
    user_trust_level: str,
    source: str,
) -> AsyncIterator[str]:
    """2-sentence sliding window over `sentences`: each window (previous +
    current, joined by a sentinel) is filtered through process_outbound()
    together — giving the filter context to catch patterns split across a
    naive sentence boundary — then the sentinel is used to split the
    (possibly redacted) result back apart, releasing only the older half.
    The final buffered sentence is filtered and flushed alone once the
    source stream ends. Blocked windows yield nothing for that window.
    """
    pending: Optional[str] = None
    async for sentence in sentences:
        if pending is None:
            pending = sentence
            continue
        window = f"{pending}{_WINDOW_SENTINEL}{sentence}"
        result = await pipeline.process_outbound(
            response=window,
            agent_id=agent_id,
            user_trust_level=user_trust_level,
            source=source,
        )
        if result.blocked:
            logger.warning("Streamed sentence window blocked: %s", result.block_reason)
            pending = sentence
            continue
        filtered = result.sanitized_message
        if _WINDOW_SENTINEL in filtered:
            released, pending = filtered.split(_WINDOW_SENTINEL, 1)
        else:
            # Filtering altered/stripped the sentinel (shouldn't normally
            # happen) — fail safe by releasing everything the filter already
            # approved rather than silently dropping it.
            released, pending = filtered, ""
        released = released.strip()
        if released:
            yield released
    if pending:
        result = await pipeline.process_outbound(
            response=pending,
            agent_id=agent_id,
            user_trust_level=user_trust_level,
            source=source,
        )
        if result.blocked:
            logger.warning("Final streamed sentence blocked: %s", result.block_reason)
            return
        final = result.sanitized_message.strip()
        if final:
            yield final


@router.post("/forward/stream")
async def forward_content_stream(request: ForwardRequest, req: Request, auth: AuthRequired):
    """Streaming variant of /forward for OpenAI-compat agents (Hermes).

    Same inbound routing/anti-spoof/PII/audit processing as /forward
    (_process_inbound), but instead of blocking for the complete agent
    reply, relays Hermes's real token stream and releases each sentence
    (through the same security filters, per sliding window) as soon as it
    is ready — so voice_gateway can start TTS immediately instead of
    waiting for the whole response to finish generating.

    Response is `text/event-stream`: one `data: {"sentence": "..."}` event
    per released sentence, followed by a single terminal `data: {"done":
    true, ...ledger fields...}` event. Not used by non-voice callers
    (Telegram, Shortcuts, etc.) — they keep using /forward.
    """
    inbound = await _process_inbound(request, req)
    if inbound.early_response is not None:
        return inbound.early_response
    target = inbound.target
    sanitized_content = inbound.sanitized_content

    if "chat/completions" not in target.chat_path:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Agent {target.name} does not support streaming",
        )

    pipeline = getattr(app_state, "pipeline", None)
    if pipeline is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Streaming requires the security pipeline; none is configured",
        )
    user_trust_level = _resolve_user_trust_level(pipeline, target, request)

    async def _event_stream() -> AsyncIterator[bytes]:
        forwarded_to = target.name
        assembled: list[str] = []
        try:
            deltas = app_state.router.forward_to_agent_stream(
                target=target,
                sanitized_content=sanitized_content,
                ledger_id="pending",
                metadata={
                    "source": request.source,
                    "content_type": request.content_type,
                    **request.metadata,
                },
            )
            sentences = _sentences_from_deltas(deltas)
            filtered = _filtered_sentence_stream(
                sentences, pipeline, target.name, user_trust_level, request.source
            )
            async for sentence in filtered:
                # Step 5.1 parity with /forward: block raw credentials even
                # from an otherwise-approved sentence.
                blocked_sentence, was_blocked = await app_state.sanitizer.block_credentials(
                    content=sentence, source=request.source
                )
                if was_blocked:
                    logger.warning(
                        f"Blocked credential display (streamed) from source={request.source}"
                    )
                    continue
                assembled.append(blocked_sentence)
                yield b"data: " + json.dumps({"sentence": blocked_sentence}).encode() + b"\n\n"
        except ForwardError as e:
            logger.warning(f"Streaming forward failed: {e}. Content logged but not delivered.")
            forwarded_to = f"{target.name} (offline)"
        except Exception as exc:
            logger.error(f"Unhandled error in streaming forward: {exc}", exc_info=True)
            forwarded_to = f"{target.name} (error)"

        full_text = " ".join(assembled)
        try:
            ledger_entry = await app_state.ledger.record(
                source=request.source,
                content=sanitized_content,
                original_content=request.content,
                sanitized=False,
                redaction_count=0,
                redaction_types=[],
                forwarded_to=forwarded_to,
                content_type=request.content_type,
                metadata=request.metadata,
            )
        except Exception as e:
            logger.error(f"Ledger recording failed: {e}")
            ledger_entry = None

        await app_state.event_bus.emit(
            make_event(
                "forward",
                f"Content forwarded from {request.source} to {forwarded_to}",
                {
                    "source": request.source,
                    "content_type": request.content_type,
                    "forwarded_to": forwarded_to,
                },
                "info",
            )
        )

        done_event = {
            "done": True,
            "id": ledger_entry.id if ledger_entry else "ledger-unavailable",
            "forwarded_to": forwarded_to,
            "agent_response": full_text,
        }
        yield b"data: " + json.dumps(done_event).encode() + b"\n\n"

    return StreamingResponse(_event_stream(), media_type="text/event-stream")
