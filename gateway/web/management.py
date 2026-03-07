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
    """Serve the security modules page (dynamic — fetches live data)."""
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Modules - AgentShroud</title>
    <style>
        body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
        .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; display: flex; align-items: center; gap: 1rem; }
        .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        .grade-badge { font-size: 2.5rem; font-weight: bold; width: 70px; height: 70px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; }
        .grade-A { background: #064e3b; color: #6ee7b7; } .grade-B { background: #1e3a5f; color: #93c5fd; }
        .grade-C { background: #78350f; color: #fcd34d; } .grade-D { background: #7c2d12; color: #fdba74; }
        .grade-F { background: #450a0a; color: #fca5a5; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        th { text-align: left; padding: 0.6rem 0.8rem; border-bottom: 2px solid #2d3748; color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; }
        td { padding: 0.6rem 0.8rem; border-bottom: 1px solid #1a2235; }
        tr:hover td { background: #1a2235; }
        .pill { display: inline-block; padding: 0.2rem 0.6rem; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; }
        .pill-active { background: #064e3b; color: #6ee7b7; } .pill-degraded { background: #78350f; color: #fcd34d; }
        .pill-unavailable { background: #1a1a2e; color: #64748b; } .pill-loaded { background: #1e3a5f; color: #93c5fd; }
        .tier-P0 { color: #f87171; font-weight: 600; } .tier-P1 { color: #fb923c; }
        .tier-P2 { color: #facc15; } .tier-P3 { color: #94a3b8; }
        .scan-btn { background: #1e3a5f; color: #93c5fd; border: 1px solid #3b82f6; border-radius: 4px; padding: 0.25rem 0.75rem; font-size: 0.8rem; cursor: pointer; }
        .scan-btn:hover { background: #1d4ed8; }
        .summary-bar { display: flex; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .summary-stat { text-align: center; }
        .summary-stat .val { font-size: 2rem; font-weight: 700; }
        .summary-stat .lbl { font-size: 0.8rem; color: #64748b; text-transform: uppercase; }
        #scan-result { margin-top: 1rem; padding: 0.75rem; background: #0f1219; border-radius: 6px; font-family: monospace; font-size: 0.8rem; white-space: pre-wrap; display: none; }
        .recs { list-style: none; padding: 0; margin: 0; }
        .recs li { padding: 0.4rem 0; border-bottom: 1px solid #1a2235; }
    </style>
</head>
<body>
<header class="header">
    <h1>AgentShroud - Security Modules</h1>
    <span id="grade-badge" class="grade-badge" title="Security grade">?</span>
</header>
<main class="main-content">
    <section class="card">
        <div class="summary-bar">
            <div class="summary-stat"><div class="val" id="cnt-active" style="color:#6ee7b7">-</div><div class="lbl">Active</div></div>
            <div class="summary-stat"><div class="val" id="cnt-degraded" style="color:#fcd34d">-</div><div class="lbl">Degraded</div></div>
            <div class="summary-stat"><div class="val" id="cnt-unavailable" style="color:#64748b">-</div><div class="lbl">Unavailable</div></div>
            <div class="summary-stat"><div class="val" id="cnt-total">-</div><div class="lbl">Total</div></div>
            <div class="summary-stat"><div class="val" id="overall-score" style="color:#93c5fd">-</div><div class="lbl">Score</div></div>
        </div>
        <table>
            <thead><tr><th>Module</th><th>Tier</th><th>Status</th><th>Binary / Location</th><th>Actions</th></tr></thead>
            <tbody id="modules-tbody"><tr><td colspan="5" style="color:#64748b;text-align:center">Loading...</td></tr></tbody>
        </table>
    </section>
    <section class="card" id="recs-section" style="display:none">
        <h3 style="margin-top:0">Recommendations</h3>
        <ul class="recs" id="recs-list"></ul>
    </section>
    <section class="card"><p style="margin:0"><a href="/manage/dashboard">← Back to Dashboard</a></p></section>
    <div id="scan-result"></div>
</main>
<script>
(async () => {
    const qs = new URLSearchParams(window.location.search);
    const token = qs.get('token') || '';
    const h = token ? {'Authorization': 'Bearer ' + token} : {};
    const qs2 = token ? '?token=' + encodeURIComponent(token) : '';

    const SCAN_ACTIONS = {
        clamav_scanner: {label: 'Run Scan', ep: '/manage/scan/clamav'},
        trivy_scanner:  {label: 'Run Scan', ep: '/manage/scan/trivy'},
        canary:         {label: 'Check', ep: '/manage/canary'},
    };

    async function fetchJ(url) {
        const r = await fetch(url, {headers: h});
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
    }

    window._scan = (ep) => {
        const el = document.getElementById('scan-result');
        el.style.display = 'block'; el.textContent = 'Running...';
        fetch(ep + qs2, {method:'POST', headers:h})
            .then(r => r.json()).then(d => { el.textContent = JSON.stringify(d, null, 2); })
            .catch(e => { el.textContent = 'Error: ' + e; });
    };

    try {
        const [modRes, repRes] = await Promise.allSettled([
            fetchJ('/manage/modules' + qs2),
            fetchJ('/manage/security-report' + qs2),
        ]);

        const mods = modRes.status === 'fulfilled' ? modRes.value : null;
        const rep  = repRes.status  === 'fulfilled' ? repRes.value  : null;

        if (mods) {
            const degraded = Object.values(mods.modules || {}).filter(m => m.status === 'degraded').length;
            document.getElementById('cnt-active').textContent     = mods.active ?? '-';
            document.getElementById('cnt-degraded').textContent   = degraded;
            document.getElementById('cnt-unavailable').textContent = mods.unavailable ?? '-';
            document.getElementById('cnt-total').textContent      = mods.total ?? '-';

            const tbody = document.getElementById('modules-tbody');
            tbody.innerHTML = '';
            for (const [name, info] of Object.entries(mods.modules || {})) {
                const tr = document.createElement('tr');
                const sc = 'pill pill-' + (info.status || 'unavailable');
                const tc = 'tier-' + (info.tier || 'P3');
                const act = SCAN_ACTIONS[name];
                tr.innerHTML =
                    '<td style="font-family:monospace">' + name + '</td>' +
                    '<td><span class="' + tc + '">' + (info.tier||'') + '</span></td>' +
                    '<td><span class="' + sc + '">' + (info.status||'') + '</span></td>' +
                    '<td style="color:#64748b;font-size:0.8rem">' + (info.binary||info.location||'') + '</td>' +
                    '<td>' + (act ? '<button class="scan-btn" onclick="window._scan(\'' + act.ep + '\')">' + act.label + '</button>' : '') + '</td>';
                tbody.appendChild(tr);
            }
        }

        if (rep) {
            const grade = rep.grade || '?';
            const badge = document.getElementById('grade-badge');
            badge.textContent = grade;
            badge.className = 'grade-badge grade-' + grade;
            document.getElementById('overall-score').textContent =
                rep.overall_score != null ? rep.overall_score.toFixed(1) : '-';

            if (rep.recommendations && rep.recommendations.length) {
                document.getElementById('recs-section').style.display = '';
                document.getElementById('recs-list').innerHTML =
                    rep.recommendations.map(r => '<li>' + r + '</li>').join('');
            }
        }
    } catch(e) {
        document.getElementById('modules-tbody').innerHTML =
            '<tr><td colspan="5" style="color:#f87171">Load failed: ' + e + '</td></tr>';
    }
})();
</script>
</body>
</html>""")


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
    """Serve the collaborators page (dynamic — fetches live activity data)."""
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Collaborators - AgentShroud</title>
    <style>
        body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
        .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
        .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        .summary-bar { display: flex; gap: 2rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .summary-stat { text-align: center; }
        .summary-stat .val { font-size: 2rem; font-weight: 700; color: #93c5fd; }
        .summary-stat .lbl { font-size: 0.8rem; color: #64748b; text-transform: uppercase; }
        table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
        th { text-align: left; padding: 0.6rem 0.8rem; border-bottom: 2px solid #2d3748; color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; }
        td { padding: 0.6rem 0.8rem; border-bottom: 1px solid #1a2235; }
        tr:hover td { background: #1a2235; }
        .ts { color: #64748b; font-size: 0.8rem; font-family: monospace; }
        .preview { color: #94a3b8; font-size: 0.85rem; }
        .empty { color: #64748b; text-align: center; padding: 2rem; }
    </style>
</head>
<body>
<header class="header">
    <h1>AgentShroud - Collaborators</h1>
</header>
<main class="main-content">
    <section class="card">
        <h2 style="margin-top:0">Activity Summary</h2>
        <div class="summary-bar">
            <div class="summary-stat"><div class="val" id="total-msgs">-</div><div class="lbl">Total Messages</div></div>
            <div class="summary-stat"><div class="val" id="unique-users">-</div><div class="lbl">Unique Users</div></div>
            <div class="summary-stat"><div class="val" id="last-active" style="font-size:1rem;padding-top:0.5rem">-</div><div class="lbl">Last Activity</div></div>
        </div>
    </section>
    <section class="card">
        <h2 style="margin-top:0">Recent Activity</h2>
        <table>
            <thead>
                <tr><th>Time</th><th>User</th><th>Message Preview</th><th>Source</th></tr>
            </thead>
            <tbody id="activity-tbody"><tr><td colspan="4" class="empty">Loading...</td></tr></tbody>
        </table>
    </section>
    <section class="card"><p style="margin:0"><a href="/manage/dashboard">← Back to Dashboard</a></p></section>
</main>
<script>
(async () => {
    const qs = new URLSearchParams(window.location.search);
    const token = qs.get('token') || '';
    const h = token ? {'Authorization': 'Bearer ' + token} : {};
    const qs2 = token ? '?token=' + encodeURIComponent(token) : '';

    function fmtTime(ts) {
        if (!ts) return '-';
        const d = new Date(ts * 1000);
        return d.toLocaleString();
    }

    try {
        const r = await fetch('/collaborators' + qs2, {headers: h});
        if (!r.ok) throw new Error('HTTP ' + r.status);
        const data = await r.json();

        const summary = data.summary || {};
        document.getElementById('total-msgs').textContent   = summary.total_messages ?? 0;
        document.getElementById('unique-users').textContent = summary.unique_users   ?? 0;
        document.getElementById('last-active').textContent  = summary.last_activity
            ? fmtTime(summary.last_activity) : 'No activity yet';

        const activity = data.activity || [];
        const tbody = document.getElementById('activity-tbody');
        if (!activity.length) {
            tbody.innerHTML = '<tr><td colspan="4" class="empty">No collaborator activity recorded yet.</td></tr>';
        } else {
            tbody.innerHTML = '';
            for (const entry of activity) {
                const tr = document.createElement('tr');
                tr.innerHTML =
                    '<td class="ts">' + fmtTime(entry.timestamp) + '</td>' +
                    '<td>' + (entry.username || entry.user_id || '-') + '</td>' +
                    '<td class="preview">' + (entry.message_preview || '') + '</td>' +
                    '<td style="color:#64748b;font-size:0.8rem">' + (entry.source || '-') + '</td>';
                tbody.appendChild(tr);
            }
        }
    } catch(e) {
        document.getElementById('activity-tbody').innerHTML =
            '<tr><td colspan="4" style="color:#f87171;text-align:center">Failed to load: ' + e + '</td></tr>';
    }
})();
</script>
</body>
</html>""")


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
# =====================================================# Credential Rotation Management (R-22)
# =====================================================
@router.get("/credentials/status")
async def credentials_status():
    """Get status of all managed credentials including age and rotation schedule."""
    from gateway.security.key_rotation import KeyRotationManager
    from gateway.security.key_rotation_config import KeyRotationConfig
    
    # Initialize with default config
    # In production, this would be loaded from persistent storage
    manager = KeyRotationManager(KeyRotationConfig())
    
    return {
        "credentials": manager.get_all_credentials_status(),
        "health": manager.get_health_score()
    }


@router.post("/credentials/rotate/{credential_id}")
async def rotate_credential(credential_id: str, force: bool = False):
    """Trigger manual rotation for a specific credential (owner only)."""
    from gateway.security.key_rotation import KeyRotationManager
    from gateway.security.key_rotation_config import KeyRotationConfig
    
    manager = KeyRotationManager(KeyRotationConfig())
    
    if credential_id not in manager._credentials:
        raise HTTPException(
            status_code=404,
            detail=f"Credential {credential_id} not found"
        )
    
    result = await manager.rotate_credential(credential_id, force=force)
    
    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )
    
    return result


@router.get("/credentials/health")
async def credentials_health():
    """Get overall credential health score and status summary."""
    from gateway.security.key_rotation import KeyRotationManager
    from gateway.security.key_rotation_config import KeyRotationConfig
    
    manager = KeyRotationManager(KeyRotationConfig())
    return manager.get_health_score()
