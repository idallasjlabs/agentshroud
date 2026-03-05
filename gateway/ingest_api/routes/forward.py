# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Message forwarding routes.

Core message forwarding endpoints:
- /webhook/telegram - Telegram inbound webhook
- /email/send - Email sending gateway
- /forward - Main ingest endpoint for content forwarding
"""

import logging
from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Request, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from ..models import (
    ApprovalRequest,
    EmailSendRequest, 
    EmailSendResponse,
    ForwardRequest,
    ForwardResponse,
)
from ..auth import create_auth_dependency
from ..router import ForwardError
from ..event_bus import make_event
from ...proxy.webhook_receiver import WebhookReceiver

# Create router
router = APIRouter()

# Set up logger
logger = logging.getLogger(__name__)

# Configuration constants
_EMAIL_ALLOWED_RECIPIENTS: list[str] = [
    # Fill in trusted addresses; unknown recipients always go to approval queue.
]

# iMessage channel ownership (P5)
_IMESSAGE_SERVER = "mac-messages"
_IMESSAGE_SEND_TOOL = "tool_send_message"


# Authentication dependency
async def auth_dep(request: Request):
    """Auth dependency that uses the app state config."""
    app_state = request.app.state.app_state
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


def _is_imessage_recipient_allowed(recipient: str, allowed: list[str]) -> bool:
    """Return True if the iMessage recipient is on the pre-approved list."""
    return recipient.strip() in {r.strip() for r in allowed}


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
    app_state = request.app.state.app_state

    # Build receiver using available app_state components
    pipeline = getattr(app_state, "pipeline", None)
    forwarder = getattr(app_state, "forwarder", None)
    session_manager = getattr(app_state, "session_manager", None)
    receiver = WebhookReceiver(pipeline=pipeline, forwarder=forwarder, session_manager=session_manager)

    result = await receiver.process_webhook(payload, source="telegram")
    logger.info(f"telegram-webhook: status={result.get('status')}")
    return result


@router.post("/email/send", status_code=status.HTTP_200_OK)
async def email_send(request: EmailSendRequest, req: Request, auth: AuthRequired):
    """Email send gateway (P3: channel ownership).

    The bot submits email send requests here instead of calling Gmail directly.
    Controls:
    - PII scan on body (redacts before logging)
    - Recipient allowlist: known addresses return 200 (approved)
    - Unknown recipients: submitted to approval queue → 202 (queued)

    Authentication required.
    """
    app_state = req.app.state.app_state
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


@router.post(
    "/forward", response_model=ForwardResponse, status_code=status.HTTP_201_CREATED
)
async def forward_content(request: ForwardRequest, req: Request, auth: AuthRequired):
    """Main ingest endpoint

    Receives data from iOS Shortcuts, browser extension, or API.
    Sanitizes PII, logs to ledger, and forwards to agent.

    Authentication required.
    """
    app_state = req.app.state.app_state
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
                "headers": {},  # Add headers if available in request
                "user_id": getattr(request, "user_id", None) or getattr(request, "source", "anonymous")
            }

            # Process through middleware
            middleware_result = await middleware_manager.process_request(request_data, "unknown")

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
            # Get user trust level for outbound filtering
            user_trust_level = "UNTRUSTED"
            if pipeline.trust_manager:
                trust_info = pipeline.trust_manager.get_trust("default")
                if trust_info:
                    trust_levels = ["UNTRUSTED", "BASIC", "STANDARD", "ELEVATED", "FULL"]
                    trust_score = trust_info[0]
                    if trust_score >= 400:
                        user_trust_level = "FULL"
                    elif trust_score >= 300:
                        user_trust_level = "ELEVATED"
                    elif trust_score >= 200:
                        user_trust_level = "STANDARD"
                    elif trust_score >= 100:
                        user_trust_level = "BASIC"
            
            out_result = await pipeline.process_outbound(
                response=agent_response, 
                agent_id="default",
                user_trust_level=user_trust_level,
                source=request.source
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