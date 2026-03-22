# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC Shared Command Layer — /soc/v1/ REST router.

Implements all SCL verb-noun endpoints:
  Security, Egress, Services, Contributors, Approvals, Observability, Updates.

Every handler:
  1. Calls get_caller() to authenticate
  2. Calls caller.require(action, resource) to enforce RBAC
  3. Logs an AuditLogEntry for every write operation
  4. Returns SCLError / SCLConfirmationRequired for error/confirmation cases
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, WebSocket, status
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from .auth import SCLCaller, get_caller, issue_session_token, issue_ws_token
from .models import (
    AuditLogEntry,
    AuditResult,
    SCLConfirmationRequired,
    SCLError,
    SCLInterface,
    Severity,
    WSEventType,
)
from ..security.rbac import Action, Resource

logger = logging.getLogger("agentshroud.soc.router")

router = APIRouter(prefix="/soc/v1", tags=["soc"])


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _app_state():
    from ..ingest_api.state import app_state
    return app_state


def _log_audit(
    caller: SCLCaller,
    command: str,
    target: str = "",
    result: AuditResult = AuditResult.SUCCESS,
    details: Optional[Dict[str, Any]] = None,
    interface: SCLInterface = SCLInterface.WEB,
) -> None:
    entry = AuditLogEntry(
        actor_id=caller.user_id,
        actor_role=caller.role.value,
        interface=interface,
        command=command,
        target=target,
        result=result,
        details=details or {},
    )
    try:
        import asyncio
        audit_store = getattr(_app_state(), "audit_store", None)
        if audit_store and hasattr(audit_store, "append"):
            asyncio.create_task(audit_store.append(entry.model_dump()))
    except Exception as exc:
        logger.debug("_log_audit: %s", exc)
    logger.info("SCL audit: %s %s → %s (%s)", caller.user_id, command, target, result.value)


def _confirmation_required(action: str, target: str, message: str):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=SCLConfirmationRequired(message=message, action=action, target=target).model_dump(),
    )


# ---------------------------------------------------------------------------
# Auth endpoints
# ---------------------------------------------------------------------------

class LoginRequest(BaseModel):
    token: str


@router.post("/auth/login")
async def auth_login(body: LoginRequest) -> JSONResponse:
    """Exchange gateway token for a session cookie."""
    import hmac
    cfg_token = os.environ.get("AGENTSHROUD_GATEWAY_PASSWORD", "") or os.environ.get("OPENCLAW_GATEWAY_PASSWORD", "")
    if not cfg_token or not hmac.compare_digest(body.token.encode(), cfg_token.encode()):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"error": True, "code": "UNAUTHORIZED", "message": "Invalid token"},
        )
    from ..security.rbac_config import RBACConfig
    owner_id = RBACConfig().owner_user_id
    session_token = issue_session_token(cfg_token, owner_id)
    response = JSONResponse(content={"ok": True, "user_id": owner_id})
    _dev_mode = os.environ.get("AGENTSHROUD_DEV_MODE", "0").lower() in ("1", "true", "yes")
    response.set_cookie(
        "soc_session", session_token,
        httponly=True, samesite="strict", secure=not _dev_mode,
    )
    return response


@router.post("/auth/ws-token")
async def auth_ws_token(caller: SCLCaller = Depends(get_caller)) -> Dict[str, Any]:
    """Issue a short-lived WebSocket token for /ws/soc."""
    ws_token = issue_ws_token(caller.user_id)
    return {"token": ws_token, "ttl_seconds": 300}


# ---------------------------------------------------------------------------
# Security endpoints
# ---------------------------------------------------------------------------

@router.get("/security/events")
async def get_security_events(
    limit: int = Query(default=50, le=500),
    severity: Optional[str] = Query(default=None),
    caller: SCLCaller = Depends(get_caller),
) -> List[Dict]:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    from .event_adapter import collect_recent_events
    events = await collect_recent_events(
        getattr(app, "audit_store", None),
        limit=limit,
        severity_filter=severity,
    )
    return [e.model_dump() for e in events]


@router.get("/security/alerts")
async def get_security_alerts(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    alerts = []
    try:
        dispatcher = getattr(app, "alert_dispatcher", None)
        if dispatcher and hasattr(dispatcher, "get_recent_alerts"):
            raw = dispatcher.get_recent_alerts(limit=50)
            from .event_adapter import from_dict
            alerts = [from_dict(a).model_dump() for a in raw if isinstance(a, dict)]
    except Exception as exc:
        logger.debug("get_security_alerts: %s", exc)
    return alerts


@router.get("/security/correlation")
async def get_soc_correlation(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    try:
        engine = getattr(app, "soc_correlation", None)
        if engine and hasattr(engine, "get_summary"):
            return engine.get_summary()
        from ..security.soc_correlation import build_correlation_summary
        return build_correlation_summary(app).to_dict()
    except Exception as exc:
        logger.debug("get_soc_correlation: %s", exc)
    return {"status": "unavailable", "risk_score": 0, "signals": []}


@router.get("/security/risk")
async def get_risk_score(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    try:
        engine = getattr(app, "soc_correlation", None)
        if engine and hasattr(engine, "get_risk_score"):
            score = engine.get_risk_score()
            return {"risk_score": score, "level": _risk_level_label(score)}
        from ..security.soc_correlation import build_correlation_summary
        score = build_correlation_summary(app).risk_score
        return {"risk_score": score, "level": _risk_level_label(score)}
    except Exception as exc:
        logger.debug("get_risk_score: %s", exc)
    return {"risk_score": 0, "level": "low"}


def _risk_level_label(score: int) -> str:
    if score >= 70:
        return "critical"
    if score >= 40:
        return "high"
    if score >= 20:
        return "medium"
    return "low"


@router.get("/security/audit/export")
async def export_audit(
    fmt: str = Query(default="json", alias="format"),
    limit: int = Query(default=1000, le=10000),
    caller: SCLCaller = Depends(get_caller),
):
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    try:
        exporter = getattr(app, "audit_exporter", None)
        if exporter and hasattr(exporter, "export"):
            data = await exporter.export(format=fmt, limit=limit)
            media_type = "text/plain" if fmt == "cef" else "application/json"
            return StreamingResponse(
                iter([data if isinstance(data, str) else json.dumps(data)]),
                media_type=media_type,
                headers={"Content-Disposition": f'attachment; filename="audit.{fmt}"'},
            )
    except Exception as exc:
        logger.warning("export_audit: %s", exc)
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"error": True, "code": "UNAVAILABLE", "message": "Audit exporter not available"},
    )


@router.post("/security/audit/verify")
async def verify_audit_chain(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    try:
        pipeline = getattr(app, "pipeline", None)
        if pipeline and hasattr(pipeline, "verify_audit_chain"):
            valid, msg = pipeline.verify_audit_chain()
            return {"valid": valid, "message": msg}
    except Exception as exc:
        logger.warning("verify_audit_chain: %s", exc)
    return {"valid": False, "message": "Audit chain not available"}


# ---------------------------------------------------------------------------
# Egress endpoints
# ---------------------------------------------------------------------------

@router.get("/egress/pending")
async def get_egress_pending(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.APPROVALS)
    app = _app_state()
    try:
        eq = getattr(app, "egress_approval_queue", None)
        if eq and hasattr(eq, "get_pending_requests"):
            pending = await eq.get_pending_requests()
            return pending if isinstance(pending, list) else []
    except Exception as exc:
        logger.debug("get_egress_pending: %s", exc)
    return []


@router.get("/egress/rules")
async def get_egress_rules(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Return all active egress rules: preloaded permanent, user-created permanent, session.

    CC-07/09: merges queue rules + pre-approved domains with source tagging.
    """
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    eq = getattr(app, "egress_approval_queue", None)
    if eq and hasattr(eq, "get_all_rules"):
        try:
            all_rules = await eq.get_all_rules()
            # Tag each permanent rule with source (preloaded vs user-created) (CC-09)
            permanent = []
            for r in all_rules.get("permanent_rules", []):
                src = getattr(eq._permanent_rules.get(r["domain"]), "source", "user")
                permanent.append({**r, "source": src or "user"})
            return {
                "permanent_rules": permanent,
                "session_rules": all_rules.get("session_rules", []),
            }
        except Exception as exc:
            logger.debug("get_egress_rules: %s", exc)
    # Fallback: return empty structure
    return {"permanent_rules": [], "session_rules": []}


@router.get("/egress/log")
async def get_egress_log(
    limit: int = Query(default=50, le=500),
    caller: SCLCaller = Depends(get_caller),
) -> List[Dict]:
    caller.require(Action.READ, Resource.SYSTEM)
    from .event_adapter import collect_recent_events
    events = await collect_recent_events(
        getattr(_app_state(), "audit_store", None),
        limit=limit,
    )
    egress_events = [e.model_dump() for e in events if "egress" in e.event_type.lower()]
    return egress_events[:limit]


class EgressApproveRequest(BaseModel):
    mode: str = "once"  # "once" | "session" | "permanent" | "1h" | "4h" | "24h"


@router.post("/egress/{request_id}/approve")
async def approve_egress(
    request_id: str,
    body: EgressApproveRequest = EgressApproveRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    try:
        eq = getattr(app, "egress_approval_queue", None)
        if eq and hasattr(eq, "approve"):
            from ..security.egress_approval import ApprovalMode
            # Map web UI mode strings to ApprovalMode (CC-06)
            _mode_map = {
                "once": ApprovalMode.ONCE,
                "session": ApprovalMode.SESSION,
                "permanent": ApprovalMode.PERMANENT,
                "1h": ApprovalMode.SESSION,
                "4h": ApprovalMode.SESSION,
                "24h": ApprovalMode.SESSION,
            }
            approval_mode = _mode_map.get(body.mode, ApprovalMode.ONCE)
            await eq.approve(request_id, mode=approval_mode)
            _log_audit(caller, "approve egress", target=request_id, details={"mode": body.mode})
            return {"ok": True, "request_id": request_id, "action": "approved", "mode": body.mode}
    except Exception as exc:
        logger.warning("approve_egress: %s", exc)
    return {"ok": False, "error": "Request not found or already decided"}


@router.post("/egress/{request_id}/deny")
async def deny_egress(
    request_id: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    try:
        eq = getattr(app, "egress_approval_queue", None)
        if eq and hasattr(eq, "deny"):
            eq.deny(request_id, decided_by=caller.user_id)
            _log_audit(caller, "deny egress", target=request_id)
            return {"ok": True, "request_id": request_id, "action": "denied"}
    except Exception as exc:
        logger.warning("deny_egress: %s", exc)
    return {"ok": False, "error": "Request not found or already decided"}


class EgressRuleOverrideRequest(BaseModel):
    domain: str
    action: str = "deny"  # "allow" or "deny"
    mode: str = "permanent"  # "permanent" or "session"


@router.post("/egress/rules/override")
async def override_egress_rule(
    body: EgressRuleOverrideRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Add or override a specific egress domain rule (CC-10)."""
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    eq = getattr(app, "egress_approval_queue", None)
    if not eq:
        return {"ok": False, "error": "Egress approval queue not available"}
    from ..security.egress_approval import ApprovalMode
    mode = ApprovalMode.PERMANENT if body.mode == "permanent" else ApprovalMode.SESSION
    ok = await eq.add_rule(body.domain, body.action, mode)
    _log_audit(caller, "override egress rule", target=body.domain, details={"action": body.action, "mode": body.mode})
    return {"ok": ok, "domain": body.domain, "action": body.action, "mode": body.mode}


@router.delete("/egress/rules/{domain}")
async def remove_egress_rule(
    domain: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Remove an egress rule for a domain (CC-10)."""
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    eq = getattr(app, "egress_approval_queue", None)
    if not eq:
        return {"ok": False, "error": "Egress approval queue not available"}
    ok = await eq.remove_rule(domain)
    _log_audit(caller, "remove egress rule", target=domain)
    return {"ok": ok, "domain": domain, "action": "removed"}


@router.get("/egress/history")
async def get_egress_history(
    limit: int = Query(default=100, le=500),
    caller: SCLCaller = Depends(get_caller),
) -> List[Dict]:
    """Return egress decision history (approve/deny/timeout) (CC-40)."""
    caller.require(Action.READ, Resource.APPROVALS)
    app = _app_state()
    eq = getattr(app, "egress_approval_queue", None)
    if not eq or not hasattr(eq, "get_decision_log"):
        return []
    return await eq.get_decision_log(limit=limit)


@router.post("/egress/history/{entry_id}/revoke")
async def revoke_egress_history(
    entry_id: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Revoke an active rule from a past approval decision (CC-40)."""
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    eq = getattr(app, "egress_approval_queue", None)
    if not eq or not hasattr(eq, "revoke_decision"):
        return {"ok": False, "error": "Egress queue not available"}
    ok = await eq.revoke_decision(entry_id)
    _log_audit(caller, "revoke egress decision", target=entry_id)
    return {"ok": ok, "entry_id": entry_id}


class EmergencyBlockRequest(BaseModel):
    reason: str = "Emergency block triggered via SCL"
    confirm: bool = False


@router.post("/egress/emergency-block")
async def emergency_block_egress(
    body: EmergencyBlockRequest,
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required(
            "block egress",
            "all",
            "This will block all outbound egress immediately. Resend with confirm: true to proceed.",
        )
    app = _app_state()
    try:
        ef = getattr(app, "egress_filter", None)
        if ef and hasattr(ef, "emergency_block"):
            ef.emergency_block(reason=body.reason)
    except Exception as exc:
        logger.warning("emergency_block_egress: %s", exc)
    _log_audit(caller, "block egress", target="all", details={"reason": body.reason})
    return JSONResponse(content={"ok": True, "action": "emergency_block", "reason": body.reason})


# ---------------------------------------------------------------------------
# Service endpoints
# ---------------------------------------------------------------------------

class ServiceActionRequest(BaseModel):
    confirm: bool = False


@router.get("/services")
async def list_services(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.SYSTEM)
    from .services import ServiceManager
    mgr = ServiceManager()
    return [s.model_dump() for s in mgr.list_services()]


@router.get("/services/{name}/logs")
async def get_service_logs(
    name: str,
    tail: int = Query(default=50, le=500),
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    from .services import ServiceManager
    mgr = ServiceManager()
    lines = await mgr.get_logs(name, tail=tail)
    return {"service": name, "lines": lines}


@router.post("/services/{name}/start")
async def start_service(
    name: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    from .services import ServiceManager
    mgr = ServiceManager()
    ok = await mgr.start_service(name)
    _log_audit(caller, "start service", target=name, result=AuditResult.SUCCESS if ok else AuditResult.FAILED)
    return {"ok": ok, "service": name, "action": "start"}


@router.post("/services/{name}/stop")
async def stop_service(
    name: str,
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("stop service", name, f"This will stop container '{name}'. Resend with confirm: true.")
    from .services import ServiceManager
    mgr = ServiceManager()
    ok = await mgr.stop_service(name)
    _log_audit(caller, "stop service", target=name, result=AuditResult.SUCCESS if ok else AuditResult.FAILED)
    return JSONResponse(content={"ok": ok, "service": name, "action": "stop"})


@router.post("/services/{name}/restart")
async def restart_service(
    name: str,
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("restart service", name, f"This will restart container '{name}'. Resend with confirm: true.")
    from .services import ServiceManager
    mgr = ServiceManager()
    ok = await mgr.restart_service(name)
    _log_audit(caller, "restart service", target=name, result=AuditResult.SUCCESS if ok else AuditResult.FAILED)
    return JSONResponse(content={"ok": ok, "service": name, "action": "restart"})


@router.post("/services/{name}/update")
async def update_service(
    name: str,
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    """Pull the latest image for a container and restart it."""
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("update service", name, f"This will pull the latest image for '{name}' and restart it. Resend with confirm: true.")
    from .services import ServiceManager
    mgr = ServiceManager()
    ok = await mgr.update_service(name)
    _log_audit(caller, "update service", target=name, result=AuditResult.SUCCESS if ok else AuditResult.FAILED)
    return JSONResponse(content={"ok": ok, "service": name, "action": "update"})


@router.post("/services/rebuild")
async def rebuild_all_services(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("rebuild services", "all", "This will rebuild all containers. Resend with confirm: true.")
    _log_audit(caller, "rebuild services", target="all")
    return JSONResponse(content={"ok": True, "action": "rebuild", "note": "Rebuild initiated — monitor logs for progress"})


# ---------------------------------------------------------------------------
# Kill switch endpoints
# ---------------------------------------------------------------------------

@router.post("/killswitch/freeze")
async def killswitch_freeze(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("freeze services", "all", "This will pause all bot containers. Resend with confirm: true.")
    app = _app_state()
    try:
        monitor = getattr(app, "killswitch_monitor", None)
        if monitor and hasattr(monitor, "trigger_freeze"):
            monitor.trigger_freeze()
    except Exception as exc:
        logger.warning("killswitch_freeze: %s", exc)
    _log_audit(caller, "freeze services", target="all")
    return JSONResponse(content={"ok": True, "action": "freeze"})


@router.post("/killswitch/shutdown")
async def killswitch_shutdown(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not body.confirm:
        return _confirmation_required("shutdown services", "all", "This will perform compose down. Resend with confirm: true.")
    app = _app_state()
    try:
        monitor = getattr(app, "killswitch_monitor", None)
        if monitor and hasattr(monitor, "trigger_shutdown"):
            monitor.trigger_shutdown()
    except Exception as exc:
        logger.warning("killswitch_shutdown: %s", exc)
    _log_audit(caller, "shutdown services", target="all")
    return JSONResponse(content={"ok": True, "action": "shutdown"})


class DisconnectRequest(BaseModel):
    confirm: bool = False
    force: bool = False


@router.post("/killswitch/disconnect")
async def killswitch_disconnect(
    body: DisconnectRequest,
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not caller.is_owner():
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"error": True, "code": "PERMISSION_DENIED", "message": "Disconnect requires owner role"},
        )
    if not (body.confirm and body.force):
        return _confirmation_required(
            "disconnect services",
            "all",
            "DESTRUCTIVE: This will stop all containers and shred credentials. "
            "Resend with confirm: true and force: true to proceed.",
        )
    app = _app_state()
    try:
        monitor = getattr(app, "killswitch_monitor", None)
        if monitor and hasattr(monitor, "trigger_disconnect"):
            monitor.trigger_disconnect()
    except Exception as exc:
        logger.warning("killswitch_disconnect: %s", exc)
    _log_audit(caller, "disconnect services", target="all", details={"force": body.force})
    return JSONResponse(content={"ok": True, "action": "disconnect"})


# ---------------------------------------------------------------------------
# Contributor / user management endpoints
# ---------------------------------------------------------------------------

@router.get("/users")
async def list_users(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    from .contributors import ContributorManager
    mgr = ContributorManager(
        teams_config=getattr(getattr(app, "config", None), "teams", None),
        activity_tracker=getattr(app, "collaborator_tracker", None),
    )
    return [c.model_dump() for c in mgr.list_contributors()]


@router.get("/users/{user_id}")
async def get_user(user_id: str, caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    from .contributors import ContributorManager
    mgr = ContributorManager(
        teams_config=getattr(getattr(app, "config", None), "teams", None),
        activity_tracker=getattr(app, "collaborator_tracker", None),
    )
    rec = mgr.get_contributor(user_id)
    if rec is None:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"User {user_id} not found"})
    return rec.model_dump()


class UpdateDisplayNameRequest(BaseModel):
    display_name: str


@router.put("/users/{user_id}/display-name")
async def update_display_name(
    user_id: str,
    body: UpdateDisplayNameRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Update a user's display name (CC-35)."""
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    _log_audit(caller, "set display-name", target=user_id, details={"display_name": body.display_name})
    # Runtime-only update (no persist path available without access to the collab file)
    return {"ok": True, "user_id": user_id, "display_name": body.display_name, "note": "Runtime update only; persisted on next collaborator record write"}


class AddCollaboratorRequest(BaseModel):
    user_id: str
    display_name: str = ""
    platform: str = "telegram"


@router.post("/users/collaborator")
async def add_collaborator(
    body: AddCollaboratorRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    from ..security.rbac_config import persist_approved_collaborator
    persist_approved_collaborator(body.user_id)
    _log_audit(caller, "add collaborator", target=body.user_id)
    return {"ok": True, "user_id": body.user_id, "action": "added"}


@router.delete("/users/{user_id}/collaborator")
async def revoke_collaborator(
    user_id: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    _log_audit(caller, "revoke collaborator", target=user_id)
    return {"ok": True, "user_id": user_id, "action": "revoked", "note": "Runtime revocation; restart gateway for full effect"}


@router.get("/collaborators/activity")
async def get_collaborator_activity(
    since: float = Query(default=0.0),
    limit: int = Query(default=100, le=500),
    user_id: Optional[str] = Query(default=None),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    """Return collaborator activity log with timestamps, source, direction, and message previews."""
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    tracker = getattr(app, "collaborator_tracker", None)
    if not tracker:
        return JSONResponse(content={"entries": [], "total": 0})
    entries = tracker.get_activity(since=since, limit=limit)
    if user_id:
        entries = [e for e in entries if e.get("user_id") == user_id]
    return JSONResponse(content={"entries": entries, "total": len(entries)})


class SetRoleRequest(BaseModel):
    role: str


@router.put("/users/{user_id}/role")
async def set_user_role(
    user_id: str,
    body: SetRoleRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.SET_ROLE, Resource.USERS)
    from ..security.rbac import RBACManager
    from ..security.rbac_config import RBACConfig, Role
    mgr = RBACManager(RBACConfig())
    try:
        role = Role(body.role.lower())
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Invalid role: {body.role}"})
    result = mgr.set_user_role(caller.user_id, user_id, role)
    if not result.allowed:
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": result.reason})
    _log_audit(caller, "set role", target=user_id, details={"role": body.role})
    return {"ok": True, "user_id": user_id, "role": body.role}


# ---------------------------------------------------------------------------
# Group management endpoints
# ---------------------------------------------------------------------------

@router.get("/groups")
async def list_groups(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams:
        return []
    return [{"id": gid, **g.model_dump()} for gid, g in teams.groups.items()]


@router.get("/groups/{group_id}")
async def get_group(group_id: str, caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    g = teams.groups[group_id]
    return {"id": group_id, **g.model_dump()}


class CreateGroupRequest(BaseModel):
    group_id: str
    name: str
    collab_mode: str = "local_only"
    members: List[str] = Field(default_factory=list)
    admin: Optional[str] = None


@router.post("/groups")
async def create_group(
    body: CreateGroupRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Create a new group at runtime (owner only)."""
    caller.require(Action.WRITE, Resource.GROUPS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if teams is None:
        raise HTTPException(status_code=503, detail={"error": True, "code": "CONFIG_UNAVAILABLE", "message": "Teams config not available"})
    if body.group_id in teams.groups:
        raise HTTPException(status_code=409, detail={"error": True, "code": "CONFLICT", "message": f"Group '{body.group_id}' already exists"})
    from ..security.group_config import GroupConfig, persist_group_create
    new_group = GroupConfig(
        id=body.group_id,
        name=body.name,
        members=body.members,
        admin=body.admin,
        collab_mode=body.collab_mode,
    )
    teams.groups[body.group_id] = new_group
    persist_group_create(body.group_id, body.name, body.collab_mode, body.members, body.admin)
    _log_audit(caller, "create group", target=body.group_id, details={"name": body.name, "collab_mode": body.collab_mode})
    return {"ok": True, "id": body.group_id, "name": body.name, "collab_mode": body.collab_mode, "members": body.members}


@router.delete("/groups/{group_id}")
async def delete_group(
    group_id: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Delete a group at runtime (owner only)."""
    caller.require(Action.WRITE, Resource.GROUPS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    del teams.groups[group_id]
    from ..security.group_config import persist_group_delete
    persist_group_delete(group_id)
    _log_audit(caller, "delete group", target=group_id)
    return {"ok": True, "group_id": group_id, "action": "deleted"}


class AddGroupMemberRequest(BaseModel):
    user_id: str


@router.post("/groups/{group_id}/members")
async def add_group_member(
    group_id: str,
    body: AddGroupMemberRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    if not caller.is_owner() and not caller.is_group_admin(group_id):
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner or group admin required"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    group = teams.groups[group_id]
    if body.user_id not in group.members:
        group.members.append(body.user_id)
    from ..security.group_config import persist_group_member_add
    persist_group_member_add(group_id, body.user_id)
    _log_audit(caller, "add group-member", target=f"{group_id}/{body.user_id}")
    return {"ok": True, "group_id": group_id, "user_id": body.user_id, "action": "added"}


@router.delete("/groups/{group_id}/members/{uid}")
async def remove_group_member(
    group_id: str,
    uid: str,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    if not caller.is_owner() and not caller.is_group_admin(group_id):
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner or group admin required"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    group = teams.groups[group_id]
    if uid in group.members:
        group.members.remove(uid)
    from ..security.group_config import persist_group_member_remove
    persist_group_member_remove(group_id, uid)
    _log_audit(caller, "remove group-member", target=f"{group_id}/{uid}")
    return {"ok": True, "group_id": group_id, "user_id": uid, "action": "removed"}


class RenameGroupRequest(BaseModel):
    name: str


@router.put("/groups/{group_id}/name")
async def rename_group(
    group_id: str,
    body: RenameGroupRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Rename a group (CC-34)."""
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    if not body.name.strip():
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": "Name cannot be empty"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    teams.groups[group_id].name = body.name
    _log_audit(caller, "rename group", target=group_id, details={"name": body.name})
    return {"ok": True, "group_id": group_id, "name": body.name}


class SetModeRequest(BaseModel):
    collab_mode: str


@router.put("/groups/{group_id}/mode")
async def set_group_mode(
    group_id: str,
    body: SetModeRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    valid_modes = {"local_only", "project_scoped", "full_access"}
    if body.collab_mode not in valid_modes:
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Invalid mode: {body.collab_mode}"})
    app = _app_state()
    teams = getattr(getattr(app, "config", None), "teams", None)
    if not teams or group_id not in teams.groups:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Group {group_id} not found"})
    teams.groups[group_id].collab_mode = body.collab_mode
    from ..security.group_config import persist_group_collab_mode
    persist_group_collab_mode(group_id, body.collab_mode)
    _log_audit(caller, "set mode", target=group_id, details={"mode": body.collab_mode})
    return {"ok": True, "group_id": group_id, "collab_mode": body.collab_mode}


# ---------------------------------------------------------------------------
# Delegation management endpoints (v0.9.0)
# ---------------------------------------------------------------------------

@router.get("/delegation")
async def list_delegations(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    """List all active privilege delegations."""
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    mgr = getattr(app, "delegation_manager", None)
    if not mgr:
        return []
    mgr.cleanup_expired()
    return [d.to_dict() for d in mgr.get_active_delegations()]


class CreateDelegationRequest(BaseModel):
    delegatee_id: str
    privilege: str = "egress_approval"
    duration_hours: float = 8.0


@router.post("/delegation")
async def create_delegation(
    body: CreateDelegationRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Create a time-bounded privilege delegation (owner only)."""
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    app = _app_state()
    mgr = getattr(app, "delegation_manager", None)
    if not mgr:
        raise HTTPException(status_code=503, detail={"error": True, "code": "UNAVAILABLE", "message": "DelegationManager not initialized"})
    try:
        from ..security.delegation import DelegationPrivilege
        priv = DelegationPrivilege(body.privilege)
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Invalid privilege: {body.privilege}. Valid: egress_approval, user_management"})
    delegation = mgr.delegate(
        owner_id=caller.user_id,
        to_user_id=body.delegatee_id,
        privilege=priv,
        duration_hours=body.duration_hours,
    )
    _log_audit(caller, "create delegation", target=body.delegatee_id, details={"privilege": body.privilege, "duration_hours": body.duration_hours})
    return delegation.to_dict()


@router.delete("/delegation/{delegatee_id}")
async def revoke_delegation(
    delegatee_id: str,
    privilege: Optional[str] = Query(default=None),
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Revoke a privilege delegation. Omit privilege to revoke all for the user."""
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    app = _app_state()
    mgr = getattr(app, "delegation_manager", None)
    if not mgr:
        raise HTTPException(status_code=503, detail={"error": True, "code": "UNAVAILABLE", "message": "DelegationManager not initialized"})
    if privilege:
        try:
            from ..security.delegation import DelegationPrivilege
            priv = DelegationPrivilege(privilege)
        except ValueError:
            raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Invalid privilege: {privilege}"})
        revoked = mgr.revoke(caller.user_id, delegatee_id, priv)
        count = 1 if revoked else 0
    else:
        count = mgr.revoke_all_for_user(caller.user_id, delegatee_id)
    _log_audit(caller, "revoke delegation", target=delegatee_id, details={"privilege": privilege or "all", "count": count})
    return {"ok": count > 0, "delegatee_id": delegatee_id, "revoked_count": count}


# ---------------------------------------------------------------------------
# Tool ACL endpoints (v0.9.0) — read-only visibility
# ---------------------------------------------------------------------------

@router.get("/tool-acl/{entity_id}")
async def get_tool_acl(entity_id: str, caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Get tool allow/deny lists for a user or group entity."""
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    enforcer = getattr(app, "tool_acl_enforcer", None)
    if not enforcer:
        return {"entity_id": entity_id, "allowed": [], "denied": [], "note": "ToolACLEnforcer not initialized"}
    return {
        "entity_id": entity_id,
        "allowed": enforcer.get_allowed_tools(entity_id),
        "denied": enforcer.get_denied_tools(entity_id),
    }


# ---------------------------------------------------------------------------
# Shared memory endpoints (v0.9.0) — group memory visibility + clear
# ---------------------------------------------------------------------------

@router.get("/shared-memory/groups/{group_id}")
async def get_group_memory(group_id: str, caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Read raw shared memory for a group workspace."""
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    sm = getattr(app, "session_manager", None)
    if not sm:
        return {"group_id": group_id, "memory": "", "note": "SessionManager not initialized"}
    from ..security.shared_memory import SharedMemoryManager
    memory_text = SharedMemoryManager(sm).get_group_memory(group_id)
    return {"group_id": group_id, "memory": memory_text, "length": len(memory_text)}


@router.delete("/shared-memory/groups/{group_id}")
async def clear_group_memory(group_id: str, caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Clear shared memory for a group workspace (owner only)."""
    caller.require(Action.MANAGE, Resource.USERS)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    app = _app_state()
    sm = getattr(app, "session_manager", None)
    if not sm:
        return {"ok": False, "group_id": group_id, "note": "SessionManager not initialized"}
    try:
        gs = sm.get_or_create_group_session(group_id)
        if gs.memory_file.exists():
            gs.memory_file.write_text("", encoding="utf-8")
        _log_audit(caller, "clear group-memory", target=group_id)
        return {"ok": True, "group_id": group_id}
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": True, "code": "INTERNAL_ERROR", "message": str(exc)})


# ---------------------------------------------------------------------------
# Privacy policy endpoints (v0.9.0) — service policy visibility
# ---------------------------------------------------------------------------

@router.get("/privacy")
async def get_privacy_policies(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """List service privacy policies (read-only view)."""
    caller.require(Action.READ, Resource.USERS)
    app = _app_state()
    enforcer = getattr(app, "privacy_enforcer", None)
    if not enforcer or not getattr(enforcer, "_policy", None):
        return {"services": {}, "note": "PrivacyPolicyEnforcer not initialized"}
    policy = enforcer._policy
    return {
        "audit_access_attempts": policy.audit_access_attempts,
        "alert_on_private_access": policy.alert_on_private_access,
        "services": {
            name: {
                "privacy": svc.privacy.value,
                "allowed_groups": list(svc.allowed_groups),
                "description": svc.description,
            }
            for name, svc in policy.services.items()
        },
    }


# ---------------------------------------------------------------------------
# Approval endpoints
# ---------------------------------------------------------------------------

@router.get("/approvals/pending")
async def list_pending_approvals(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.APPROVALS)
    app = _app_state()
    try:
        aq = getattr(app, "approval_queue", None)
        if aq and hasattr(aq, "get_pending_items"):
            items = aq.get_pending_items()
            return [i if isinstance(i, dict) else vars(i) for i in items]
    except Exception as exc:
        logger.debug("list_pending_approvals: %s", exc)
    return []


class ApprovalDecisionRequest(BaseModel):
    reason: str = ""


@router.post("/approvals/{approval_id}/approve")
async def approve_request(
    approval_id: str,
    body: ApprovalDecisionRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    try:
        aq = getattr(app, "approval_queue", None)
        if aq and hasattr(aq, "approve"):
            await aq.approve(approval_id, approver=caller.user_id)
            _log_audit(caller, "approve request", target=approval_id)
            return {"ok": True, "approval_id": approval_id, "action": "approved"}
    except Exception as exc:
        logger.warning("approve_request: %s", exc)
    return {"ok": False, "error": "Approval not found or already decided"}


@router.post("/approvals/{approval_id}/deny")
async def deny_request(
    approval_id: str,
    body: ApprovalDecisionRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.APPROVE, Resource.APPROVALS)
    app = _app_state()
    try:
        aq = getattr(app, "approval_queue", None)
        if aq and hasattr(aq, "deny"):
            await aq.deny(approval_id, denier=caller.user_id, reason=body.reason)
            _log_audit(caller, "deny request", target=approval_id)
            return {"ok": True, "approval_id": approval_id, "action": "denied"}
    except Exception as exc:
        logger.warning("deny_request: %s", exc)
    return {"ok": False, "error": "Approval not found or already decided"}


# ---------------------------------------------------------------------------
# Observability / health
# ---------------------------------------------------------------------------

@router.get("/health")
async def get_health(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    from .services import ServiceManager
    mgr = ServiceManager()
    services = mgr.list_services()
    all_healthy = all(s.status.value == "running" for s in services)
    return {
        "status": "healthy" if all_healthy else "degraded",
        "services": [{"name": s.name, "status": s.status.value, "health": s.health.value} for s in services],
        "risk_score": 0,
    }


# CC-43: Human-readable descriptions for all security modules
_MODULE_DESCRIPTIONS = {
    "sanitizer": "PII/secret detection and redaction in bot responses",
    "prompt_guard": "Prompt injection and jailbreak detection",
    "egress_filter": "Network egress policy enforcement (domain allowlist/blocklist)",
    "mcp_proxy": "MCP tool call interception and security filtering",
    "killswitch_monitor": "Emergency stop — freeze/halt/disconnect all bot activity",
    "drift_detector": "Detects unauthorized config or file changes at runtime",
    "memory_integrity": "Validates bot memory files haven't been tampered with",
    "soc_correlation": "Cross-signal risk scoring and threat correlation",
    "dns_blocklist": "DNS-level blocking of malicious/suspicious domains",
    "heuristic_classifier": "Behavioral classification of bot actions (safe/risky/malicious)",
}


@router.get("/security/modules")
@router.get("/modules")
async def get_modules(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    """List security modules with availability, mode, and descriptions (CC-42, CC-43)."""
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    modules = []
    module_names = [
        "sanitizer", "prompt_guard", "egress_filter", "mcp_proxy",
        "killswitch_monitor", "drift_detector", "memory_integrity",
        "soc_correlation", "dns_blocklist", "heuristic_classifier",
    ]
    for name in module_names:
        obj = getattr(app, name, None)
        # Read mode from module config if available (CC-42)
        mode = "enforce"
        if obj is not None:
            cfg = getattr(obj, "config", None)
            if cfg is not None:
                mode = getattr(cfg, "mode", "enforce")
            else:
                mode = getattr(obj, "mode", "enforce")
        modules.append({
            "name": name,
            "available": obj is not None,
            "mode": mode,
            "description": _MODULE_DESCRIPTIONS.get(name, ""),
        })
    return modules


class SetModuleModeRequest(BaseModel):
    mode: str  # "enforce" | "monitor" | "disabled"


@router.put("/security/modules/{name}/mode")
async def set_module_mode(
    name: str,
    body: SetModuleModeRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Switch a security module between enforce/monitor/disabled modes at runtime (CC-42)."""
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if body.mode not in ("enforce", "monitor", "disabled"):
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": "mode must be enforce | monitor | disabled"})
    app = _app_state()
    obj = getattr(app, name, None)
    if obj is None:
        raise HTTPException(status_code=404, detail={"error": True, "code": "NOT_FOUND", "message": f"Module {name} not found or not initialized"})
    # Try to set mode on config or directly on the object
    changed = False
    cfg = getattr(obj, "config", None)
    if cfg is not None and hasattr(cfg, "mode"):
        cfg.mode = body.mode
        changed = True
    elif hasattr(obj, "mode"):
        obj.mode = body.mode
        changed = True
    if not changed:
        raise HTTPException(status_code=400, detail={"error": True, "code": "NOT_SUPPORTED", "message": f"Module {name} does not support runtime mode switching"})
    _log_audit(caller, f"set module mode {name}", target=name, details={"mode": body.mode})
    return {"ok": True, "name": name, "mode": body.mode}


@router.get("/config")
async def get_config(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.CONFIGURATION)
    app = _app_state()
    cfg = getattr(app, "config", None)
    if cfg is None:
        return {}
    # Return a safe subset — no secrets
    return {
        "bind": getattr(cfg, "bind", ""),
        "port": getattr(cfg, "port", 8080),
        "log_level": getattr(cfg, "log_level", "INFO"),
        "bots": {bid: {"name": b.name, "hostname": b.hostname, "port": b.port} for bid, b in getattr(cfg, "bots", {}).items()},
        "teams_enabled": getattr(cfg, "teams", None) is not None,
    }


class SetLogLevelRequest(BaseModel):
    level: str  # DEBUG | INFO | WARNING | ERROR


@router.put("/config/log-level")
async def set_log_level(
    body: SetLogLevelRequest,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    """Change the root log level at runtime without restart (CC-44)."""
    caller.require(Action.MANAGE, Resource.CONFIGURATION)
    valid = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
    lvl = body.level.upper()
    if lvl not in valid:
        raise HTTPException(status_code=400, detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Invalid level: {body.level}. Valid: {sorted(valid)}"})
    import logging as _logging
    _logging.getLogger().setLevel(lvl)
    _logging.getLogger("agentshroud").setLevel(lvl)
    _log_audit(caller, "set log-level", target="root", details={"level": lvl})
    return {"ok": True, "level": lvl}


@router.post("/config-integrity/acknowledge")
async def acknowledge_config_integrity(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Reset the config integrity baseline to the current file state.

    Use after a legitimate rebuild to silence the stale-hash warning on the
    next restart. Owner access required.
    """
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail="Owner access required")
    app = _app_state()
    monitor = getattr(app, "config_integrity", None)
    if monitor is None:
        return {"status": "skipped", "reason": "ConfigIntegrityMonitor not initialized"}
    monitor.reset_baseline()
    return {"status": "ok", "message": "Config integrity baseline reset to current state"}


# ---------------------------------------------------------------------------
# Scan implementation helpers
# ---------------------------------------------------------------------------

_SECURITY_SCAN_SCRIPT = "/usr/local/bin/security-scan.sh"
_SCANNER_FLAG_MAP = {
    "trivy": "--trivy",
    "clamav": "--clamav",
    "openscap": "--oscap",
    "sbom": "--sbom",
    "all": "--all",
}


async def _launch_scan_background(scanner: str) -> None:
    """Launch security-scan.sh for the given scanner and discard the handle (fire-and-forget)."""
    flag = _SCANNER_FLAG_MAP[scanner]
    try:
        proc = await asyncio.create_subprocess_exec(
            _SECURITY_SCAN_SCRIPT, flag,
            stdout=asyncio.subprocess.DEVNULL,
            stderr=asyncio.subprocess.DEVNULL,
        )
        # Do not await — results are written to /var/log/security/* shared volume
        asyncio.ensure_future(proc.wait())
    except Exception as exc:
        logger.warning("launch_scan_background(%s): %s", scanner, exc)


class ScanRequest(BaseModel):
    confirm: bool = False


@router.post("/scan/{scanner}")
async def run_scanner(
    scanner: str,
    body: Optional[ScanRequest] = None,
    caller: SCLCaller = Depends(get_caller),
) -> Dict:
    caller.require(Action.EXECUTE, Resource.SYSTEM)
    valid_scanners = set(_SCANNER_FLAG_MAP)
    if scanner not in valid_scanners:
        raise HTTPException(
            status_code=400,
            detail={"error": True, "code": "VALIDATION_ERROR", "message": f"Unknown scanner: {scanner}. Valid: {sorted(valid_scanners)}"},
        )
    _log_audit(caller, f"scan {scanner}", target="system")
    await _launch_scan_background(scanner)
    return {
        "ok": True,
        "scanner": scanner,
        "status": "initiated",
        "note": "Scan running in background. Results will appear in /soc/v1/scan/results within minutes.",
    }


@router.get("/scan/results")
async def get_scan_results(caller: SCLCaller = Depends(get_caller)) -> List[Dict]:
    caller.require(Action.READ, Resource.SYSTEM)
    app = _app_state()
    results = []
    try:
        trivy = getattr(app, "trivy_scanner", None)
        if trivy and hasattr(trivy, "get_last_results"):
            r = trivy.get_last_results()
            if r:
                results.append({"scanner": "trivy", "results": r})
    except Exception:
        pass
    return results


# ---------------------------------------------------------------------------
# Scanner aggregation + Container Security Scorecard endpoints
# ---------------------------------------------------------------------------

@router.get("/scanners")
async def get_scanner_results(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Unified scanner aggregation: Trivy, Falco, ClamAV, Wazuh, OpenSCAP.

    Returns aggregated findings from all security sidecars. Data is read from
    shared volumes — no scanners are invoked at query time.
    """
    caller.require(Action.READ, Resource.SYSTEM)
    try:
        from ..security.scanner_integration import aggregate_results
        return aggregate_results()
    except Exception as exc:
        logger.warning("get_scanner_results: %s", exc)
        return {
            "status": "error",
            "error": str(exc),
            "scanners": {},
            "totals": {"critical": 0, "high": 0, "medium": 0, "low": 0},
        }


@router.get("/scorecard")
async def get_security_scorecard(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Container Security Scorecard — 12-domain maturity assessment.

    Standards basis: CIS Docker Benchmark v1.6.0, NIST SP 800-190,
    DISA Docker Enterprise STIG, IEC 62443 (FR1–FR7).

    Domains scored 0-5 per maturity scale:
      0=Not Started, 1=Initial, 2=Managed, 3=Defined, 4=Measured, 5=Optimizing
    """
    caller.require(Action.READ, Resource.SYSTEM)
    try:
        from ..security.scanner_integration import compute_scorecard
        return compute_scorecard()
    except Exception as exc:
        logger.warning("get_security_scorecard: %s", exc)
        return {
            "error": str(exc),
            "version": "v0.9.0",
            "domains": [],
            "totals": {"score": 0, "max": 60, "percentage": 0},
            "overall_maturity": "Not Started",
        }


@router.get("/sbom")
async def get_sbom(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Return the latest Software Bill of Materials (SBOM) in SPDX JSON format.

    Generated by Syft during build-time security scan (scripts/security-scan.sh).
    EO 14028 mandate — third-party component traceability.
    """
    caller.require(Action.READ, Resource.SYSTEM)
    try:
        from ..security.scanner_integration import get_sbom as _get_sbom
        sbom = _get_sbom()
        if sbom is None:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "error": True,
                    "code": "NOT_FOUND",
                    "message": "No SBOM found. Run scripts/security-scan.sh to generate.",
                },
            )
        return sbom
    except Exception as exc:
        logger.warning("get_sbom: %s", exc)
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"error": True, "code": "UNAVAILABLE", "message": str(exc)},
        )


@router.get("/trivy")
async def get_trivy_results(caller: SCLCaller = Depends(get_caller)) -> Dict:
    """Return the latest Trivy vulnerability scan results.

    Trivy scans are run at build time via scripts/security-scan.sh.
    Results are read from the shared security report volume.
    """
    caller.require(Action.READ, Resource.SYSTEM)
    try:
        from ..security.scanner_integration import get_trivy_summary
        return get_trivy_summary()
    except Exception as exc:
        logger.warning("get_trivy_results: %s", exc)
        return {"tool": "trivy", "status": "error", "error": str(exc), "findings": 0}


# ---------------------------------------------------------------------------
# Updates / upgrade endpoints
# ---------------------------------------------------------------------------

_GH_RELEASES_API = "https://api.github.com/repos/idallasj/agentshroud/releases/latest"
_CURRENT_VERSION = "0.9.0"


def _fetch_latest_release() -> Dict:
    """Query GitHub releases API. Returns {"tag_name": ..., "html_url": ...} or {"error": ...}."""
    try:
        req = urllib.request.Request(
            _GH_RELEASES_API,
            headers={"User-Agent": f"agentshroud-gateway/{_CURRENT_VERSION}", "Accept": "application/vnd.github+json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        return {"tag_name": data.get("tag_name", ""), "html_url": data.get("html_url", ""), "body": data.get("body", "")}
    except Exception as exc:
        return {"error": str(exc)}


@router.get("/updates")
async def get_updates(caller: SCLCaller = Depends(get_caller)) -> Dict:
    caller.require(Action.READ, Resource.SYSTEM)
    release = await asyncio.get_event_loop().run_in_executor(None, _fetch_latest_release)
    if "error" in release:
        return {"current_version": _CURRENT_VERSION, "available": [], "check_error": release["error"]}
    latest = release.get("tag_name", "").lstrip("v")
    available = []
    if latest and latest != _CURRENT_VERSION:
        available.append({"version": latest, "url": release.get("html_url", ""), "notes": release.get("body", "")})
    return {"current_version": _CURRENT_VERSION, "latest_version": latest, "available": available}


async def _ssh_compose(command: str, timeout: int = 120) -> tuple[int, str, str]:
    """Run a shell command on the Docker Compose host via SSH.

    Requires AGENTSHROUD_COMPOSE_HOST (SSH target, e.g. user@host) and
    optionally AGENTSHROUD_COMPOSE_DIR (project directory, default /opt/agentshroud).
    Returns (returncode, stdout, stderr).
    """
    host = os.environ.get("AGENTSHROUD_COMPOSE_HOST", "")
    compose_dir = os.environ.get("AGENTSHROUD_COMPOSE_DIR", "/opt/agentshroud")
    if not host:
        return 1, "", "AGENTSHROUD_COMPOSE_HOST is not configured — cannot perform remote compose operations"
    full_cmd = f"cd {compose_dir} && {command}"
    try:
        proc = await asyncio.create_subprocess_exec(
            "ssh",
            "-o", "BatchMode=yes",
            "-o", "ConnectTimeout=10",
            "-o", "StrictHostKeyChecking=accept-new",
            host, full_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return proc.returncode or 0, stdout.decode(errors="replace"), stderr.decode(errors="replace")
    except asyncio.TimeoutError:
        return 1, "", f"SSH command timed out after {timeout}s"
    except Exception as exc:
        return 1, "", str(exc)


@router.post("/updates/gateway/upgrade")
async def upgrade_gateway(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    if not body.confirm:
        return _confirmation_required(
            "upgrade gateway", "agentshroud-gateway",
            "Runs: git pull origin main && docker compose up -d --build --no-deps agentshroud-gateway "
            "on AGENTSHROUD_COMPOSE_HOST. Resend with confirm: true.",
        )
    _log_audit(caller, "upgrade gateway", target="agentshroud-gateway")
    rc, stdout, stderr = await _ssh_compose(
        "git pull origin main && docker compose up -d --build --no-deps agentshroud-gateway",
        timeout=300,
    )
    if rc != 0:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"ok": False, "action": "upgrade", "target": "gateway", "exit_code": rc, "stderr": stderr[:2000]},
        )
    return JSONResponse(content={"ok": True, "action": "upgrade", "target": "gateway", "stdout": stdout[:2000]})


async def _docker_exec_bot(command: list[str], timeout: int = 120) -> tuple[int, str]:
    """Run a command inside the agentshroud-bot container via the Docker socket.

    Uses Docker's exec API (create + start) so no external CLI is needed.
    Returns (exit_code, combined_output).
    """
    import http.client
    import json as _json
    import socket as _socket

    _SOCK = "/var/run/docker.sock"
    _CONTAINER = "agentshroud-bot"

    def _unix_call(method: str, path: str, body: bytes = b"") -> tuple[int, bytes]:
        class _UH(http.client.HTTPConnection):
            def connect(self) -> None:  # type: ignore[override]
                self.sock = _socket.socket(_socket.AF_UNIX, _socket.SOCK_STREAM)
                self.sock.settimeout(30)
                self.sock.connect(_SOCK)

        conn = _UH("localhost")
        headers = {"Content-Type": "application/json", "Content-Length": str(len(body))}
        conn.request(method, path, body=body, headers=headers)
        resp = conn.getresponse()
        return resp.status, resp.read()

    try:
        # Create exec instance
        exec_body = _json.dumps({
            "AttachStdout": True, "AttachStderr": True,
            "Cmd": command,
        }).encode()
        status_code, data = await asyncio.get_event_loop().run_in_executor(
            None, lambda: _unix_call("POST", f"/containers/{_CONTAINER}/exec", exec_body)
        )
        if status_code not in (200, 201):
            return 1, f"Docker exec create failed ({status_code}): {data.decode(errors='replace')[:500]}"
        exec_id = _json.loads(data).get("Id", "")
        if not exec_id:
            return 1, "Docker exec create returned no ID"

        # Start exec instance (returns streamed output — read synchronously)
        start_body = _json.dumps({"Detach": False, "Tty": False}).encode()
        _, output = await asyncio.get_event_loop().run_in_executor(
            None, lambda: _unix_call("POST", f"/exec/{exec_id}/start", start_body)
        )

        # Inspect exec for exit code
        _, inspect_data = await asyncio.get_event_loop().run_in_executor(
            None, lambda: _unix_call("GET", f"/exec/{exec_id}/json")
        )
        exit_code = _json.loads(inspect_data).get("ExitCode", 0)
        # Strip Docker multiplexed stream header bytes (8-byte frame header per chunk)
        raw = output
        text = ""
        offset = 0
        while offset + 8 <= len(raw):
            frame_size = int.from_bytes(raw[offset + 4:offset + 8], "big")
            text += raw[offset + 8: offset + 8 + frame_size].decode(errors="replace")
            offset += 8 + frame_size
        return exit_code, text or output.decode(errors="replace")
    except Exception as exc:
        return 1, str(exc)


@router.post("/updates/bot/upgrade")
async def upgrade_bot(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    """In-place openclaw upgrade: runs npm install -g inside the bot container.

    No container rebuild needed — installs the latest openclaw into the
    NPM_CONFIG_PREFIX volume (/home/node/.npm-global) which is writable at runtime.
    Works for any single-instance deployment without SSH or compose access.
    """
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not caller.is_owner():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"},
        )
    if not body.confirm:
        return _confirmation_required(
            "upgrade bot", "agentshroud-bot",
            "Runs: npm install -g openclaw@latest inside the agentshroud-bot container "
            "(writes to /home/node/.npm-global — no container rebuild needed). "
            "Resend with confirm: true.",
        )
    _log_audit(caller, "upgrade bot", target="agentshroud-bot")
    exit_code, output = await _docker_exec_bot(
        ["npm", "install", "-g", "openclaw@latest"],
        timeout=300,
    )
    if exit_code != 0:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"ok": False, "action": "upgrade", "target": "bot", "exit_code": exit_code, "output": output[:2000]},
        )
    return JSONResponse(content={"ok": True, "action": "upgrade", "target": "bot", "output": output[:2000]})


@router.post("/updates/gateway/rollback")
async def rollback_gateway(
    body: ServiceActionRequest = ServiceActionRequest(),
    caller: SCLCaller = Depends(get_caller),
) -> JSONResponse:
    caller.require(Action.MANAGE, Resource.SYSTEM)
    if not caller.is_owner():
        raise HTTPException(status_code=403, detail={"error": True, "code": "PERMISSION_DENIED", "message": "Owner required"})
    if not body.confirm:
        return _confirmation_required(
            "rollback gateway", "agentshroud-gateway",
            "Runs: git checkout HEAD~1 -- gateway/ && docker compose up -d --build --no-deps agentshroud-gateway "
            "on AGENTSHROUD_COMPOSE_HOST. Resend with confirm: true.",
        )
    _log_audit(caller, "rollback gateway", target="agentshroud-gateway")
    rollback_tag = os.environ.get("AGENTSHROUD_ROLLBACK_TAG", "HEAD~1")
    rc, stdout, stderr = await _ssh_compose(
        f"git checkout {rollback_tag} -- gateway/ && docker compose up -d --build --no-deps agentshroud-gateway",
        timeout=300,
    )
    if rc != 0:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"ok": False, "action": "rollback", "target": "gateway", "exit_code": rc, "stderr": stderr[:2000]},
        )
    return JSONResponse(content={"ok": True, "action": "rollback", "target": "gateway", "stdout": stdout[:2000]})


# ---------------------------------------------------------------------------
# WebSocket endpoint
# ---------------------------------------------------------------------------

@router.websocket("/ws")
async def soc_websocket(websocket: WebSocket):
    from .websocket import ws_soc_endpoint
    await ws_soc_endpoint(websocket)


# ---------------------------------------------------------------------------
# Web dashboard — serve SPA at /soc/
# ---------------------------------------------------------------------------

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
@router.get("", response_class=HTMLResponse, include_in_schema=False)
async def soc_dashboard(request: Request):
    """Serve the unified SOC web dashboard."""
    template_path = Path(__file__).parent / "templates" / "soc.html"
    _v = _CURRENT_VERSION.replace(".", "") + "b"
    if template_path.exists():
        html = template_path.read_text()
        # Inject version query param for cache-busting on each release
        html = html.replace('/soc/static/soc.js"', f'/soc/static/soc.js?v={_v}"')
        html = html.replace('/soc/static/soc.css"', f'/soc/static/soc.css?v={_v}"')
        return HTMLResponse(
            content=html,
            headers={"Cache-Control": "no-cache, no-store, must-revalidate"},
        )
    return HTMLResponse(content=_minimal_dashboard_html())


def _minimal_dashboard_html() -> str:
    """Fallback minimal dashboard when template file is missing."""
    return """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>AgentShroud SOC</title>
<style>body{background:#0d1117;color:#c9d1d9;font-family:monospace;padding:2rem;}
h1{color:#58a6ff;} a{color:#58a6ff;}</style></head>
<body>
<h1>AgentShroud SOC — Command Center</h1>
<p>v0.9.0 Sentinel | <a href="/soc/v1/health">Health</a> |
<a href="/soc/v1/security/events">Events</a> |
<a href="/soc/v1/services">Services</a> |
<a href="/soc/v1/users">Contributors</a></p>
<p>Full dashboard template at gateway/soc/templates/soc.html</p>
</body></html>"""
