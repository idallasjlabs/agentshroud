# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Health check endpoint for the AgentShroud Gateway"""

import time
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request

from gateway import __version__

from ..auth import create_auth_dependency
from ..models import StatusResponse
from ..state import app_state

router = APIRouter()


async def auth_dep(request: Request):
    """Auth dependency that uses the app state config."""
    if not hasattr(app_state, "config"):
        raise HTTPException(status_code=401, detail="Service not initialized")
    dep = create_auth_dependency(app_state.config)
    await dep(request)


AuthRequired = Annotated[None, Depends(auth_dep)]


@router.get("/status")
async def health_check():
    """Minimal health check endpoint — no authentication required.

    Returns only basic liveness info. Detailed status requires auth via /status/detail.
    """
    return {"status": "healthy", "version": __version__}


@router.get("/status/detail", response_model=StatusResponse)
async def health_check_detail(auth: AuthRequired):
    """Detailed health check endpoint — authentication required.

    Returns full system status including security posture.
    """
    uptime = time.time() - app_state.start_time
    stats = await app_state.ledger.get_stats()
    pending = await app_state.approval_queue.get_pending()

    # Observatory mode state
    obs_mode = getattr(
        app_state,
        "observatory_mode",
        {"global_mode": "enforce", "effective_since": None, "auto_revert_at": None},
    )

    # Egress stats
    egress_queue = getattr(app_state, "egress_approval_queue", None)
    egress_pending = 0
    egress_rules = 0
    if egress_queue:
        try:
            egress_pending = len(egress_queue._pending_requests)
            egress_rules = len(egress_queue._rules.get("allow", [])) + len(
                egress_queue._rules.get("deny", [])
            )
        except Exception:
            pass

    # Collaborator activity tracker health
    tracker_health: dict | None = None
    _ct = getattr(app_state, "collaborator_tracker", None)
    if _ct is not None:
        try:
            tracker_health = _ct.get_health()
        except Exception:
            pass
    else:
        _ct_err = getattr(app_state, "collaborator_tracker_init_error", None)
        tracker_health = {"healthy": False, "error": _ct_err or "tracker not initialized"}

    # Per-bot inventory — query Docker for each configured bot container.
    bots_inventory: dict = {}
    if hasattr(app_state, "config") and app_state.config.bots:
        try:
            from ...runtime import get_engine as _get_engine_fn

            _eng = _get_engine_fn()
            _containers = {c.name: c for c in _eng.ps(all=True)}
            for bot_id, _bot_cfg in app_state.config.bots.items():
                cname = _bot_cfg.resolved_container_name
                cinfo = _containers.get(cname)
                bots_inventory[bot_id] = {
                    "container": cname,
                    "healthy": cinfo is not None
                    and ("Up" in cinfo.status or "healthy" in cinfo.status.lower()),
                    "image": cinfo.image if cinfo else None,
                    "status": cinfo.status if cinfo else "not found",
                }
        except Exception as _e:
            bots_inventory = {"error": str(_e)}

    return StatusResponse(
        status="healthy",
        version=__version__,
        uptime_seconds=uptime,
        ledger_entries=stats.get("total_entries", 0),
        pending_approvals=len(pending),
        pii_engine=app_state.sanitizer.get_mode(),
        config_loaded=True,
        observatory_mode={
            "global_mode": obs_mode.get("global_mode", "enforce"),
            "effective_since": obs_mode.get("effective_since"),
            "auto_revert_at": obs_mode.get("auto_revert_at"),
        },
        security_summary={
            "modules_active": 33,
            "modules_enforcing": 33 if obs_mode.get("global_mode") == "enforce" else 0,
            "modules_monitoring": 0 if obs_mode.get("global_mode") == "enforce" else 33,
            "blocked_today": stats.get("blocked_today", 0),
            "canary_status": "green",
        },
        egress={
            "pending_approvals": egress_pending,
            "rules_count": egress_rules,
            "blocked_today": 0,
            "allowed_today": 0,
        },
        proxies={
            "http": (
                "running" if getattr(app_state, "http_proxy", None) is not None else "stopped"
            ),
            "http_error": getattr(app_state, "_http_proxy_start_error", None),
            "dns": (
                "running" if getattr(app_state, "dns_transport", None) is not None else "stopped"
            ),
        },
        tracker=tracker_health,
        bots=bots_inventory or None,
    )
