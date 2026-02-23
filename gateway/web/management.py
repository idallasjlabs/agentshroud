# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""AgentShroud Management Dashboard routes.

All /manage/ routes require authentication via the gateway's auth dependency.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from .api import require_auth

logger = logging.getLogger("agentshroud.web.management")

router = APIRouter(
    prefix="/manage",
    tags=["management"],
    dependencies=[Depends(require_auth)],
)


@router.get("/", response_class=HTMLResponse)
async def dashboard():
    """Serve the management dashboard. Authentication required."""
    template = Path(__file__).parent / "templates" / "management.html"
    return HTMLResponse(template.read_text())
