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
    const DASHBOARD_LINKS = {
        falco_monitor:  '/manage/dashboard/falco',
        wazuh_client:   '/manage/dashboard/wazuh',
        pipeline:       '/manage/dashboard/modules',
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
                const dashLink = DASHBOARD_LINKS[name];
                let actionHtml = '';
                if (act) actionHtml += '<button class="scan-btn" onclick="window._scan(\'' + act.ep + '\')">' + act.label + '</button> ';
                if (dashLink) actionHtml += '<a class="scan-btn" href="' + dashLink + qs2 + '" style="text-decoration:none">View</a>';
                tr.innerHTML =
                    '<td style="font-family:monospace">' + name + '</td>' +
                    '<td><span class="' + tc + '">' + (info.tier||'') + '</span></td>' +
                    '<td><span class="' + sc + '">' + (info.status||'') + '</span></td>' +
                    '<td style="color:#64748b;font-size:0.8rem">' + (info.binary||info.location||'') + '</td>' +
                    '<td>' + (actionHtml || '') + '</td>';
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


@router.get("/dashboard/falco", response_class=HTMLResponse)
async def falco_dashboard():
    """Falco runtime security alerts viewer."""
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Falco Alerts - AgentShroud</title>
    <style>
        body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
        .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
        .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        .summary-bar { display: flex; gap: 2rem; margin-bottom: 1rem; flex-wrap: wrap; }
        .stat { text-align: center; }
        .stat .val { font-size: 2rem; font-weight: 700; }
        .stat .lbl { font-size: 0.8rem; color: #64748b; text-transform: uppercase; }
        .sev-CRITICAL { color: #f87171; } .sev-HIGH { color: #fb923c; }
        .sev-MEDIUM { color: #facc15; } .sev-LOW { color: #94a3b8; }
        table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
        th { text-align: left; padding: 0.5rem 0.75rem; border-bottom: 2px solid #2d3748; color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; }
        td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #1a2235; vertical-align: top; }
        tr:hover td { background: #1a2235; }
        .pill { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 600; }
        .pill-CRITICAL { background: #450a0a; color: #f87171; }
        .pill-HIGH { background: #431407; color: #fb923c; }
        .pill-MEDIUM { background: #422006; color: #facc15; }
        .pill-LOW { background: #1a1a2e; color: #94a3b8; }
        .empty { color: #64748b; text-align: center; padding: 2rem; }
        .status-clean { color: #6ee7b7; } .status-info { color: #93c5fd; }
        .status-warning { color: #fcd34d; } .status-critical { color: #f87171; }
        .no-data-note { background: #0f1219; border: 1px solid #232b3d; border-radius: 6px; padding: 1rem; color: #64748b; font-size: 0.85rem; }
        pre { margin: 0; white-space: pre-wrap; font-size: 0.78rem; color: #94a3b8; }
    </style>
</head>
<body>
<header class="header">
    <h1>AgentShroud - Falco Runtime Monitor</h1>
</header>
<main class="main-content">
    <section class="card" id="summary-card">
        <h2 style="margin-top:0">Summary</h2>
        <div class="summary-bar">
            <div class="stat"><div class="val sev-CRITICAL" id="cnt-critical">-</div><div class="lbl">Critical</div></div>
            <div class="stat"><div class="val sev-HIGH" id="cnt-high">-</div><div class="lbl">High</div></div>
            <div class="stat"><div class="val sev-MEDIUM" id="cnt-medium">-</div><div class="lbl">Medium</div></div>
            <div class="stat"><div class="val sev-LOW" id="cnt-low">-</div><div class="lbl">Low</div></div>
            <div class="stat"><div class="val" id="cnt-total" style="color:#93c5fd">-</div><div class="lbl">Total</div></div>
        </div>
        <p id="status-line" style="margin:0;font-size:0.9rem">Loading...</p>
        <p id="dir-line" style="margin:0.5rem 0 0;font-size:0.8rem;color:#64748b"></p>
    </section>
    <section class="card" id="alerts-card">
        <h2 style="margin-top:0">Recent Alerts</h2>
        <table>
            <thead><tr><th>Time</th><th>Severity</th><th>Rule</th><th>Process</th><th>Output</th></tr></thead>
            <tbody id="alerts-tbody"><tr><td colspan="5" class="empty">Loading...</td></tr></tbody>
        </table>
    </section>
    <section class="card"><p style="margin:0"><a href="/manage/dashboard">&#8592; Back to Dashboard</a></p></section>
</main>
<script>
(async () => {
    const qs = new URLSearchParams(window.location.search);
    const token = qs.get('token') || '';
    const h = token ? {'Authorization': 'Bearer ' + token} : {};
    const qs2 = token ? '?token=' + encodeURIComponent(token) : '';

    function fmtTime(ts) {
        if (!ts) return '-';
        try { return new Date(ts).toLocaleString(); } catch(e) { return ts; }
    }

    try {
        const r = await fetch('/manage/falco/alerts' + qs2, {headers: h});
        if (!r.ok) throw new Error('HTTP ' + r.status);
        const data = await r.json();
        const s = data.summary || {};

        document.getElementById('cnt-critical').textContent = s.critical ?? 0;
        document.getElementById('cnt-high').textContent = s.high ?? 0;
        document.getElementById('cnt-medium').textContent = s.medium ?? 0;
        document.getElementById('cnt-low').textContent = s.low ?? 0;
        document.getElementById('cnt-total').textContent = s.findings ?? 0;

        const statusClass = 'status-' + (s.status || 'clean');
        document.getElementById('status-line').innerHTML =
            'Status: <strong class="' + statusClass + '">' + (s.status || 'clean').toUpperCase() + '</strong>';
        document.getElementById('dir-line').textContent =
            'Alert directory: ' + data.alert_dir + (data.dir_exists ? ' (exists)' : ' (not found — no agent deployed)');

        const alerts = data.alerts || [];
        const tbody = document.getElementById('alerts-tbody');
        if (!alerts.length) {
            const note = data.dir_exists
                ? 'No alerts recorded — system is clean.'
                : 'Falco agent not deployed. This gateway monitors alert files written by an external Falco agent running in the host environment. Deploy the Falco agent to populate this view.';
            tbody.innerHTML = '<tr><td colspan="5" class="empty">' + note + '</td></tr>';
        } else {
            tbody.innerHTML = '';
            for (const a of [...alerts].reverse()) {
                const tr = document.createElement('tr');
                const sev = (a.severity || 'MEDIUM').toUpperCase();
                tr.innerHTML =
                    '<td style="white-space:nowrap;font-size:0.78rem;color:#64748b">' + fmtTime(a.timestamp) + '</td>' +
                    '<td><span class="pill pill-' + sev + '">' + sev + '</span></td>' +
                    '<td style="font-family:monospace;font-size:0.8rem">' + (a.rule || '') + '</td>' +
                    '<td style="font-size:0.8rem;color:#94a3b8">' + (a.process || a.container_name || '') + '</td>' +
                    '<td><pre>' + (a.output || '').substring(0, 200) + '</pre></td>';
                tbody.appendChild(tr);
            }
        }
    } catch(e) {
        document.getElementById('alerts-tbody').innerHTML =
            '<tr><td colspan="5" style="color:#f87171;text-align:center">Failed to load: ' + e + '</td></tr>';
    }
})();
</script>
</body>
</html>""")


@router.get("/dashboard/wazuh", response_class=HTMLResponse)
async def wazuh_dashboard():
    """Wazuh HIDS alerts and FIM events viewer."""
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wazuh HIDS - AgentShroud</title>
    <style>
        body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
        .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; }
        .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        .summary-bar { display: flex; gap: 2rem; margin-bottom: 1rem; flex-wrap: wrap; }
        .stat { text-align: center; }
        .stat .val { font-size: 2rem; font-weight: 700; }
        .stat .lbl { font-size: 0.8rem; color: #64748b; text-transform: uppercase; }
        .tabs { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
        .tab { padding: 0.4rem 1rem; border-radius: 6px 6px 0 0; cursor: pointer; font-size: 0.85rem; background: #0f1219; border: 1px solid #232b3d; border-bottom: none; }
        .tab.active { background: #161c27; color: #93c5fd; border-color: #3b82f6; }
        table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
        th { text-align: left; padding: 0.5rem 0.75rem; border-bottom: 2px solid #2d3748; color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; }
        td { padding: 0.5rem 0.75rem; border-bottom: 1px solid #1a2235; }
        tr:hover td { background: #1a2235; }
        .pill { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 600; }
        .pill-CRITICAL { background: #450a0a; color: #f87171; }
        .pill-HIGH { background: #431407; color: #fb923c; }
        .pill-MEDIUM { background: #422006; color: #facc15; }
        .pill-LOW { background: #1a1a2e; color: #94a3b8; }
        .empty { color: #64748b; text-align: center; padding: 2rem; }
        .status-clean { color: #6ee7b7; } .status-info { color: #93c5fd; }
        .status-warning { color: #fcd34d; } .status-critical { color: #f87171; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body>
<header class="header">
    <h1>AgentShroud - Wazuh HIDS</h1>
</header>
<main class="main-content">
    <section class="card">
        <h2 style="margin-top:0">Summary</h2>
        <div class="summary-bar">
            <div class="stat"><div class="val" id="cnt-critical" style="color:#f87171">-</div><div class="lbl">Critical</div></div>
            <div class="stat"><div class="val" id="cnt-high" style="color:#fb923c">-</div><div class="lbl">High</div></div>
            <div class="stat"><div class="val" id="cnt-fim" style="color:#93c5fd">-</div><div class="lbl">FIM Events</div></div>
            <div class="stat"><div class="val" id="cnt-rootkit" style="color:#f87171">-</div><div class="lbl">Rootkit Events</div></div>
            <div class="stat"><div class="val" id="cnt-total" style="color:#e2e8f0">-</div><div class="lbl">Total</div></div>
        </div>
        <p id="status-line" style="margin:0;font-size:0.9rem">Loading...</p>
        <p id="dir-line" style="margin:0.5rem 0 0;font-size:0.8rem;color:#64748b"></p>
    </section>
    <section class="card">
        <div class="tabs">
            <div class="tab active" onclick="switchTab('all')">All Alerts</div>
            <div class="tab" onclick="switchTab('fim')">FIM Events</div>
            <div class="tab" onclick="switchTab('rootkit')">Rootkit Events</div>
        </div>
        <div id="tab-all" class="tab-content active">
            <table>
                <thead><tr><th>Time</th><th>Severity</th><th>Rule</th><th>Description</th><th>Agent</th></tr></thead>
                <tbody id="all-tbody"><tr><td colspan="5" class="empty">Loading...</td></tr></tbody>
            </table>
        </div>
        <div id="tab-fim" class="tab-content">
            <table>
                <thead><tr><th>Time</th><th>File Path</th><th>Event</th><th>MD5 Before</th><th>MD5 After</th></tr></thead>
                <tbody id="fim-tbody"><tr><td colspan="5" class="empty">Loading...</td></tr></tbody>
            </table>
        </div>
        <div id="tab-rootkit" class="tab-content">
            <table>
                <thead><tr><th>Time</th><th>Severity</th><th>Rule ID</th><th>Description</th><th>Agent</th></tr></thead>
                <tbody id="rootkit-tbody"><tr><td colspan="5" class="empty">Loading...</td></tr></tbody>
            </table>
        </div>
    </section>
    <section class="card"><p style="margin:0"><a href="/manage/dashboard">&#8592; Back to Dashboard</a></p></section>
</main>
<script>
function switchTab(name) {
    document.querySelectorAll('.tab').forEach((t, i) => {
        const names = ['all', 'fim', 'rootkit'];
        t.classList.toggle('active', names[i] === name);
    });
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    document.getElementById('tab-' + name).classList.add('active');
}

(async () => {
    const qs = new URLSearchParams(window.location.search);
    const token = qs.get('token') || '';
    const h = token ? {'Authorization': 'Bearer ' + token} : {};
    const qs2 = token ? '?token=' + encodeURIComponent(token) : '';

    function fmtTime(ts) {
        if (!ts) return '-';
        try { return new Date(ts).toLocaleString(); } catch(e) { return ts; }
    }

    function noDataNote(dirExists) {
        return dirExists
            ? 'No alerts recorded.'
            : 'Wazuh agent not deployed. This gateway reads alert files written by an external Wazuh agent. Deploy the Wazuh agent to populate this view.';
    }

    try {
        const r = await fetch('/manage/wazuh/alerts' + qs2, {headers: h});
        if (!r.ok) throw new Error('HTTP ' + r.status);
        const data = await r.json();
        const s = data.summary || {};

        document.getElementById('cnt-critical').textContent = s.critical ?? 0;
        document.getElementById('cnt-high').textContent = s.high ?? 0;
        document.getElementById('cnt-fim').textContent = (data.fim_events || []).length;
        document.getElementById('cnt-rootkit').textContent = (data.rootkit_events || []).length;
        document.getElementById('cnt-total').textContent = s.findings ?? 0;

        const statusClass = 'status-' + (s.status || 'clean');
        document.getElementById('status-line').innerHTML =
            'Status: <strong class="' + statusClass + '">' + (s.status || 'clean').toUpperCase() + '</strong>';
        document.getElementById('dir-line').textContent =
            'Alert directory: ' + data.alert_dir + (data.dir_exists ? ' (exists)' : ' (not found)');

        // All alerts
        const allAlerts = data.alerts || [];
        const allTbody = document.getElementById('all-tbody');
        if (!allAlerts.length) {
            allTbody.innerHTML = '<tr><td colspan="5" class="empty">' + noDataNote(data.dir_exists) + '</td></tr>';
        } else {
            allTbody.innerHTML = '';
            for (const a of [...allAlerts].reverse()) {
                const sev = (a.severity || 'MEDIUM').toUpperCase();
                const tr = document.createElement('tr');
                tr.innerHTML =
                    '<td style="white-space:nowrap;font-size:0.78rem;color:#64748b">' + fmtTime(a.timestamp) + '</td>' +
                    '<td><span class="pill pill-' + sev + '">' + sev + '</span></td>' +
                    '<td style="font-family:monospace;font-size:0.8rem">' + (a.rule_id || '') + '</td>' +
                    '<td style="font-size:0.85rem">' + (a.rule_description || '') + '</td>' +
                    '<td style="font-size:0.8rem;color:#94a3b8">' + (a.agent || '') + '</td>';
                allTbody.appendChild(tr);
            }
        }

        // FIM events
        const fim = data.fim_events || [];
        const fimTbody = document.getElementById('fim-tbody');
        if (!fim.length) {
            fimTbody.innerHTML = '<tr><td colspan="5" class="empty">' + noDataNote(data.dir_exists) + '</td></tr>';
        } else {
            fimTbody.innerHTML = '';
            for (const a of [...fim].reverse()) {
                const tr = document.createElement('tr');
                tr.innerHTML =
                    '<td style="white-space:nowrap;font-size:0.78rem;color:#64748b">' + fmtTime(a.timestamp) + '</td>' +
                    '<td style="font-family:monospace;font-size:0.78rem">' + (a.file_path || '') + '</td>' +
                    '<td><span class="pill pill-MEDIUM">' + (a.file_event || '') + '</span></td>' +
                    '<td style="font-family:monospace;font-size:0.78rem;color:#64748b">' + (a.file_md5_before || '-') + '</td>' +
                    '<td style="font-family:monospace;font-size:0.78rem;color:#94a3b8">' + (a.file_md5_after || '-') + '</td>';
                fimTbody.appendChild(tr);
            }
        }

        // Rootkit events
        const rootkit = data.rootkit_events || [];
        const rkTbody = document.getElementById('rootkit-tbody');
        if (!rootkit.length) {
            rkTbody.innerHTML = '<tr><td colspan="5" class="empty">' + noDataNote(data.dir_exists) + '</td></tr>';
        } else {
            rkTbody.innerHTML = '';
            for (const a of [...rootkit].reverse()) {
                const sev = (a.severity || 'HIGH').toUpperCase();
                const tr = document.createElement('tr');
                tr.innerHTML =
                    '<td style="white-space:nowrap;font-size:0.78rem;color:#64748b">' + fmtTime(a.timestamp) + '</td>' +
                    '<td><span class="pill pill-' + sev + '">' + sev + '</span></td>' +
                    '<td style="font-family:monospace;font-size:0.8rem">' + (a.rule_id || '') + '</td>' +
                    '<td style="font-size:0.85rem">' + (a.rule_description || '') + '</td>' +
                    '<td style="font-size:0.8rem;color:#94a3b8">' + (a.agent || '') + '</td>';
                rkTbody.appendChild(tr);
            }
        }
    } catch(e) {
        document.getElementById('all-tbody').innerHTML =
            '<tr><td colspan="5" style="color:#f87171;text-align:center">Failed to load: ' + e + '</td></tr>';
    }
})();
</script>
</body>
</html>""")


@router.get("/dashboard/security", response_class=HTMLResponse)
async def security_overview():
    """Security tools overview — links to all tool-specific dashboards."""
    return HTMLResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Security Overview - AgentShroud</title>
    <style>
        body { background: #08090b; color: #e2e8f0; font-family: system-ui; margin: 0; padding: 0; }
        .header { background: #0f1219; padding: 1rem 2rem; border-bottom: 1px solid #232b3d; display: flex; align-items: center; gap: 1rem; }
        .main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }
        .card { background: #161c27; border: 1px solid #232b3d; border-radius: 8px; padding: 1.5rem; margin-bottom: 1.5rem; }
        .tool-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem; }
        .tool-card { background: #0f1219; border: 1px solid #232b3d; border-radius: 8px; padding: 1.25rem; display: flex; flex-direction: column; gap: 0.5rem; }
        .tool-card:hover { border-color: #3b82f6; }
        .tool-name { font-weight: 600; font-size: 1rem; }
        .tool-desc { font-size: 0.82rem; color: #64748b; flex: 1; }
        .tool-actions { display: flex; gap: 0.5rem; margin-top: 0.5rem; flex-wrap: wrap; }
        .btn { padding: 0.3rem 0.85rem; border-radius: 5px; font-size: 0.8rem; cursor: pointer; text-decoration: none; display: inline-block; border: 1px solid; }
        .btn-view { background: #1e3a5f; color: #93c5fd; border-color: #3b82f6; }
        .btn-view:hover { background: #1d4ed8; }
        .btn-scan { background: #064e3b; color: #6ee7b7; border-color: #059669; }
        .btn-scan:hover { background: #065f46; }
        .pill { display: inline-block; padding: 0.15rem 0.55rem; border-radius: 9999px; font-size: 0.72rem; font-weight: 600; }
        .pill-active { background: #064e3b; color: #6ee7b7; }
        .pill-degraded { background: #78350f; color: #fcd34d; }
        .pill-unavailable { background: #1a1a2e; color: #64748b; }
        .grade-badge { font-size: 2rem; font-weight: bold; width: 55px; height: 55px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; }
        .grade-A { background: #064e3b; color: #6ee7b7; } .grade-B { background: #1e3a5f; color: #93c5fd; }
        .grade-C { background: #78350f; color: #fcd34d; } .grade-D { background: #7c2d12; color: #fdba74; }
        .grade-F { background: #450a0a; color: #fca5a5; }
        #scan-out { display: none; margin-top: 1rem; padding: 0.75rem; background: #0a0b0e; border-radius: 6px; font-family: monospace; font-size: 0.78rem; white-space: pre-wrap; max-height: 300px; overflow-y: auto; }
    </style>
</head>
<body>
<header class="header">
    <h1>AgentShroud - Security Overview</h1>
    <span id="grade-badge" class="grade-badge" title="Overall security grade">?</span>
</header>
<main class="main-content">
    <section class="card">
        <h2 style="margin-top:0">Security Tool Status</h2>
        <div id="tool-grid" class="tool-grid"><p style="color:#64748b">Loading...</p></div>
        <div id="scan-out"></div>
    </section>
    <section class="card"><p style="margin:0"><a href="/manage/dashboard">&#8592; Back to Dashboard</a></p></section>
</main>
<script>
(async () => {
    const qs = new URLSearchParams(window.location.search);
    const token = qs.get('token') || '';
    const h = token ? {'Authorization': 'Bearer ' + token} : {};
    const qs2 = token ? '?token=' + encodeURIComponent(token) : '';

    async function fetchJ(url) {
        const r = await fetch(url, {headers: h});
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
    }

    window._runScan = (ep, label) => {
        const el = document.getElementById('scan-out');
        el.style.display = 'block'; el.textContent = label + ': Running...';
        fetch(ep + qs2, {method: 'POST', headers: h})
            .then(r => r.json())
            .then(d => { el.textContent = label + ':\\n' + JSON.stringify(d, null, 2); })
            .catch(e => { el.textContent = label + ' Error: ' + e; });
    };

    const TOOLS = [
        { key: 'clamav_scanner',   name: 'ClamAV',        tier: 'P3', desc: 'Antivirus — scans container filesystem for malware',
          dashboard: null, scan: '/manage/scan/clamav', scanLabel: 'Run AV Scan' },
        { key: 'trivy_scanner',    name: 'Trivy',         tier: 'P3', desc: 'Vulnerability scanner — CVEs and misconfigurations',
          dashboard: null, scan: '/manage/scan/trivy', scanLabel: 'Run Vuln Scan' },
        { key: 'falco_monitor',    name: 'Falco',         tier: 'P3', desc: 'Runtime security monitor — syscall anomaly detection',
          dashboard: '/manage/dashboard/falco', scan: null },
        { key: 'wazuh_client',     name: 'Wazuh HIDS',    tier: 'P3', desc: 'Host intrusion detection — FIM and rootkit monitoring',
          dashboard: '/manage/dashboard/wazuh', scan: null },
        { key: 'drift_detector',   name: 'Drift Detector',tier: 'P2', desc: 'Detects configuration and filesystem drift',
          dashboard: null, scan: null },
        { key: 'encrypted_store',  name: 'Encrypted Store',tier:'P2', desc: 'Encrypted at-rest storage for sensitive gateway data',
          dashboard: null, scan: null },
        { key: 'key_vault',        name: 'Key Vault',     tier: 'P2', desc: 'Secure in-memory key management',
          dashboard: null, scan: null },
        { key: 'alert_dispatcher', name: 'Alert Dispatcher',tier:'P1',desc: 'Routes security alerts to Telegram and audit log',
          dashboard: null, scan: null },
        { key: 'killswitch_monitor',name:'Kill Switch',   tier: 'P1', desc: 'Docker/Colima health monitor — auto-shutdown on failure',
          dashboard: '/manage/dashboard/killswitch', scan: null },
        { key: 'canary',           name: 'Canary',        tier: 'P2', desc: 'Integrity trip-wires for prompt injection detection',
          dashboard: null, scan: '/manage/canary', scanLabel: 'Check Integrity' },
        { key: 'network_validator',name: 'Network Validator',tier:'P2',desc:'DNS blocklist and egress domain enforcement',
          dashboard: null, scan: null },
        { key: 'pipeline',         name: 'Security Pipeline',tier:'P0',desc:'Core request/response security pipeline (PromptGuard, ContextGuard, PII)',
          dashboard: '/manage/dashboard/modules', scan: null },
    ];

    const OPENCLAW_URL = 'http://localhost:18789';

    try {
        const [modRes, repRes] = await Promise.allSettled([
            fetchJ('/manage/modules' + qs2),
            fetchJ('/manage/security-report' + qs2),
        ]);

        const mods = modRes.status === 'fulfilled' ? modRes.value : null;
        const rep  = repRes.status  === 'fulfilled' ? repRes.value  : null;

        if (rep) {
            const grade = rep.grade || '?';
            const badge = document.getElementById('grade-badge');
            badge.textContent = grade;
            badge.className = 'grade-badge grade-' + grade;
        }

        const statusMap = {};
        if (mods && mods.modules) {
            for (const [k, v] of Object.entries(mods.modules)) {
                statusMap[k] = v.status || 'unavailable';
            }
        }

        const grid = document.getElementById('tool-grid');
        grid.innerHTML = '';
        for (const tool of TOOLS) {
            const status = statusMap[tool.key] || (mods ? 'unavailable' : 'unknown');
            const pillCls = status === 'active' ? 'pill-active' : status === 'degraded' ? 'pill-degraded' : 'pill-unavailable';
            let actions = '';
            if (tool.dashboard) {
                actions += '<a class="btn btn-view" href="' + tool.dashboard + qs2 + '">View Dashboard</a> ';
            }
            if (tool.scan) {
                actions += '<button class="btn btn-scan" onclick="window._runScan(\'' + tool.scan + '\',\'' + tool.name + '\')">' + (tool.scanLabel||'Run') + '</button>';
            }
            const div = document.createElement('div');
            div.className = 'tool-card';
            div.innerHTML =
                '<div style="display:flex;justify-content:space-between;align-items:center">' +
                    '<span class="tool-name">' + tool.name + '</span>' +
                    '<span class="pill ' + pillCls + '">' + status + '</span>' +
                '</div>' +
                '<div style="font-size:0.72rem;color:#64748b">Tier: ' + tool.tier + '</div>' +
                '<div class="tool-desc">' + tool.desc + '</div>' +
                '<div class="tool-actions">' + actions + '</div>';
            grid.appendChild(div);
        }
    } catch(e) {
        document.getElementById('tool-grid').innerHTML =
            '<p style="color:#f87171">Failed to load: ' + e + '</p>';
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
