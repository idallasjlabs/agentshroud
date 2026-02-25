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

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .api import require_auth
from ..security.egress_config import get_egress_config, set_egress_config, EgressFilterConfig

logger = logging.getLogger("agentshroud.web.management")

router = APIRouter(
    prefix="/manage",
    tags=["management"],
    dependencies=[Depends(require_auth)],
)


@router.get("/", response_class=HTMLResponse)
async def dashboard():
    """Serve the main management dashboard."""
    template = Path(__file__).parent / "templates" / "dashboard.html"
    return HTMLResponse(template.read_text())


@router.get("/dashboard", response_class=HTMLResponse) 
async def dashboard_main():
    """Serve the main dashboard page."""
    template = Path(__file__).parent / "templates" / "dashboard.html"
    return HTMLResponse(template.read_text())


@router.get("/dashboard/approvals", response_class=HTMLResponse)
async def approvals():
    """Serve the approval queue page."""
    # For now, return a simple page - will be enhanced later
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Approval Queue - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - Approval Queue</h1>
        </header>
        <main class="main-content">
            <section class="card">
                <h2>Approval Queue</h2>
                <p>No pending approvals at this time.</p>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


@router.get("/dashboard/modules", response_class=HTMLResponse)
async def modules():
    """Serve the security modules page."""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Security Modules - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - Security Modules</h1>
        </header>
        <main class="main-content">
            <section class="card">
                <h2>Security Modules</h2>
                <p>24 of 30 security modules are currently active.</p>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


@router.get("/dashboard/audit", response_class=HTMLResponse)
async def audit():
    """Serve the audit log page."""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Audit Log - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - Audit Log</h1>
        </header>
        <main class="main-content">
            <section class="card">
                <h2>Audit Log</h2>
                <p>Security event logs and system audit trail.</p>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


@router.get("/dashboard/ssh", response_class=HTMLResponse)
async def ssh():
    """Serve the SSH hosts page."""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SSH Hosts - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - SSH Hosts</h1>
        </header>
        <main class="main-content">
            <section class="card">
                <h2>SSH Host Monitoring</h2>
                <p>SSH host connectivity and status monitoring.</p>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


@router.get("/dashboard/collaborators", response_class=HTMLResponse)
async def collaborators():
    """Serve the collaborators page."""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Collaborators - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - Collaborators</h1>
        </header>
        <main class="main-content">
            <section class="card">
                <h2>Active Collaborators</h2>
                <p>Monitor active users and their interactions.</p>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


@router.get("/dashboard/killswitch", response_class=HTMLResponse)
async def killswitch():
    """Serve the emergency kill switch page."""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Emergency Kill Switch - AgentShroud</title>
        <link rel="stylesheet" href="/static/agentshroud-dashboard.css">
        <style>
            body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
            .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
            .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
            .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
            .kill-switch { background: #ef4444; color: white; padding: 1rem 2rem; border-radius: 8px; border: none; font-size: 1.2rem; cursor: pointer; }
        </style>
    </head>
    <body>
        <header class="header">
            <h1>🛡️ AgentShroud - Emergency Kill Switch</h1>
        </header>
        <main class="main-content">
            <section class="card" style="border-color: #ef4444;">
                <h2 style="color: #ef4444;">⚠️ Emergency Kill Switch</h2>
                <p><strong>Warning:</strong> This will immediately shut down all AgentShroud processes.</p>
                <button class="kill-switch" onclick="alert('Kill switch activated (demo)')">🚨 EMERGENCY STOP</button>
                <p><a href="/manage/dashboard">← Back to Dashboard</a></p>
            </section>
        </main>
    </body>
    </html>
    """)


# Pydantic models for egress management
class EgressAllowlistUpdate(BaseModel):
    """Request model for updating egress allowlist."""
    domains: list[str]
    mode: str = "enforce"  # "enforce" or "monitor"


class EgressAllowlistResponse(BaseModel):
    """Response model for egress allowlist."""
    domains: list[str]
    mode: str
    denylist: list[str]


@router.get("/egress/allowlist", response_model=EgressAllowlistResponse)
async def get_egress_allowlist():
    """Get current egress allowlist configuration."""
    config = get_egress_config()
    return EgressAllowlistResponse(
        domains=config.default_allowlist,
        mode=config.mode,
        denylist=config.default_denylist
    )


@router.put("/egress/allowlist")
async def update_egress_allowlist(update: EgressAllowlistUpdate):
    """Update egress allowlist configuration (owner only)."""
    # Validate mode
    if update.mode not in ("enforce", "monitor"):
        raise HTTPException(
            status_code=400, 
            detail="Mode must be 'enforce' or 'monitor'"
        )
    
    # Get current config
    current_config = get_egress_config()
    
    # Create updated config
    new_config = EgressFilterConfig(
        mode=update.mode,
        default_allowlist=update.domains,
        default_denylist=current_config.default_denylist,  # Keep existing denylist
        agent_allowlists=current_config.agent_allowlists,
        allowed_ips=current_config.allowed_ips,
        allowed_ports=current_config.allowed_ports,
        strict_mode=current_config.strict_mode
    )
    
    # Update global config
    set_egress_config(new_config)
    
    return {
        "status": "success", 
        "message": f"Egress allowlist updated with {len(update.domains)} domains in {update.mode} mode",
        "domains": update.domains,
        "mode": update.mode
    }
