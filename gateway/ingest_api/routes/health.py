# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Health check endpoint for the AgentShroud Gateway"""

import time

from fastapi import APIRouter

from ..models import StatusResponse
from ..state import app_state

router = APIRouter()


@router.get("/status", response_model=StatusResponse)
async def health_check():
    """Health check endpoint

    No authentication required.
    """
    uptime = time.time() - app_state.start_time
    stats = await app_state.ledger.get_stats()
    pending = await app_state.approval_queue.get_pending()

    # Observatory mode state
    obs_mode = getattr(app_state, 'observatory_mode', {
        'global_mode': 'enforce', 'effective_since': None, 'auto_revert_at': None
    })

    # Egress stats
    egress_queue = getattr(app_state, 'egress_approval_queue', None)
    egress_pending = 0
    egress_rules = 0
    if egress_queue:
        try:
            egress_pending = len(egress_queue._pending_requests)
            egress_rules = len(egress_queue._rules.get('allow', [])) + len(egress_queue._rules.get('deny', []))
        except Exception:
            pass

    return StatusResponse(
        status="healthy",
        version="0.8.0",
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
    )
