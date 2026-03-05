# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Approval system routes.

Human approval system endpoints:
- /approve - Submit approval request
- /approve/{request_id}/decide - Approve or reject request
- /approve/pending - List pending approvals
- /ws/approvals - WebSocket for real-time approval notifications
"""

import hmac
import logging
from typing import Annotated

from fastapi import APIRouter, Request, HTTPException, Query, WebSocket, Depends

from ..models import (
    ApprovalDecision,
    ApprovalQueueItem,
    ApprovalRequest,
)
from ..auth import create_auth_dependency
from ..state import app_state
from ..event_bus import make_event

# Create router
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
@router.post("/approve", response_model=ApprovalQueueItem)
async def submit_approval_request(request: ApprovalRequest, req: Request, auth: AuthRequired):
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


@router.post("/approve/{request_id}/decide", response_model=ApprovalQueueItem)
async def decide_approval(
    request_id: str, decision: ApprovalDecision, req: Request, auth: AuthRequired
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


@router.get("/approve/pending", response_model=list[ApprovalQueueItem])
async def list_pending_approvals(req: Request, auth: AuthRequired):
    """List all pending approval requests

    Authentication required.
    """
    return await app_state.approval_queue.get_pending()


@router.websocket("/ws/approvals")
async def approval_websocket(websocket: WebSocket, token: str | None = Query(None)):
    """WebSocket endpoint for real-time approval notifications

    Protocol:
    1. Client connects with token as query param: /ws/approvals?token=<token>
    2. Server validates token during handshake - rejects before accepting
    3. Server pushes new approval requests and decisions
    4. Client can send decisions: {"type": "decide", "request_id": "...", "approved": true}
    """
    # Access app_state from websocket state
    app_state = websocket.scope["app"].state.app_state
    
    # L5: Accept scoped WS tokens (short-lived, single-use) alongside master token
    from .dashboard import _validate_ws_token
    if not token or (
        not _validate_ws_token(token)
        and not hmac.compare_digest(token, app_state.config.auth_token)
    ):
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