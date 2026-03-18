// AgentShroud™ SOC Command Center — v0.9.0
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// Vanilla JS — no build toolchain required.
'use strict';

const SOC_BASE = '/soc/v1';
let _token = localStorage.getItem('soc_token') || '';
let _ws = null;
let _wsStatus = 'disconnected';
let _eventFeed = [];
const MAX_FEED = 300;

// ---------------------------------------------------------------------------
// API helpers
// ---------------------------------------------------------------------------

async function _api(method, path, body) {
  const opts = {
    method,
    headers: { 'Authorization': `Bearer ${_token}`, 'Content-Type': 'application/json' },
  };
  if (body !== undefined) opts.body = JSON.stringify(body);
  try {
    const resp = await fetch(`${SOC_BASE}${path}`, opts);
    const data = await resp.json().catch(() => ({}));
    return { ok: resp.ok, status: resp.status, data };
  } catch (err) {
    return { ok: false, status: 0, data: { error: String(err) } };
  }
}

const _get    = p       => _api('GET',    p);
const _post   = (p, b) => _api('POST',   p, b);
const _delete = p       => _api('DELETE', p);

// ---------------------------------------------------------------------------
// Utility
// ---------------------------------------------------------------------------

function _esc(s) {
  return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function _ts(iso) {
  if (!iso) return '—';
  try { return new Date(iso).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }); }
  catch { return String(iso).slice(11, 19); }
}

function _ago(iso) {
  if (!iso) return '—';
  const diff = (Date.now() - new Date(iso)) / 1000;
  if (diff < 60)   return `${Math.round(diff)}s ago`;
  if (diff < 3600) return `${Math.round(diff / 60)}m ago`;
  return `${Math.round(diff / 3600)}h ago`;
}

function _uptime(sec) {
  const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60), s = sec % 60;
  return h > 0 ? `${h}h ${m}m` : m > 0 ? `${m}m ${s}s` : `${s}s`;
}

function _sevBadge(sev) {
  const m = { critical: 'critical', high: 'danger', medium: 'warning', low: 'muted', info: 'info' };
  return `<span class="badge badge-${m[sev] || 'muted'}">${(sev || 'info').toUpperCase()}</span>`;
}

// ---------------------------------------------------------------------------
// Toast notifications
// ---------------------------------------------------------------------------

function _toast(msg, type = 'info') {
  const t = document.createElement('div');
  const col = { success: '--success', danger: '--danger', warning: '--warning', info: '--accent' }[type] || '--accent';
  t.style.cssText = `position:fixed;bottom:4.5rem;right:1rem;padding:.5rem 1rem;border-radius:5px;
    font-size:12px;z-index:999;background:var(--surface);border:1px solid var(${col});color:var(${col});
    box-shadow:0 4px 12px rgba(0,0,0,.4);max-width:300px;word-break:break-word;`;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3500);
}

// ---------------------------------------------------------------------------
// Confirmation modal
// ---------------------------------------------------------------------------

function _confirm(title, body, onConfirm, danger = true) {
  const overlay = document.getElementById('confirm-modal');
  document.getElementById('modal-title').textContent = title;
  document.getElementById('modal-title').style.color = danger ? 'var(--danger)' : 'var(--accent)';
  document.getElementById('modal-body').textContent = body;
  const btn = document.getElementById('modal-confirm-btn');
  btn.className = `btn ${danger ? 'btn-danger' : 'btn-primary'}`;
  btn.onclick = () => { _closeModal(); onConfirm(); };
  overlay.classList.add('open');
}

window._closeModal = function() {
  document.getElementById('confirm-modal').classList.remove('open');
};

// ---------------------------------------------------------------------------
// WebSocket
// ---------------------------------------------------------------------------

function _connectWS() {
  if (_ws && _ws.readyState <= 1) return;
  _setWSStatus('connecting');
  const wsBase = location.origin.replace(/^http/, 'ws');
  _ws = new WebSocket(`${wsBase}${SOC_BASE}/ws?token=${encodeURIComponent(_token)}`);
  _ws.addEventListener('open', () => {
    _setWSStatus('connected');
    _ws.send(JSON.stringify({ subscribe: ['security_event', 'egress_event', 'service_event', 'log_event'] }));
  });
  _ws.addEventListener('message', e => {
    try {
      const ev = JSON.parse(e.data);
      if (ev.type === 'keepalive') return;
      _handleWSEvent(ev);
    } catch {}
  });
  _ws.addEventListener('close', () => { _setWSStatus('disconnected'); setTimeout(_connectWS, 5000); });
  _ws.addEventListener('error',  () => _setWSStatus('disconnected'));
}

function _setWSStatus(st) {
  _wsStatus = st;
  const el = document.getElementById('ws-status');
  const lbl = document.getElementById('ws-label');
  if (!el) return;
  el.className = `ws-pill ${st}`;
  if (lbl) lbl.textContent = st === 'connected' ? 'Live' : st === 'connecting' ? 'Connecting…' : 'Disconnected';
}

function _handleWSEvent(ev) {
  _eventFeed.unshift(ev);
  if (_eventFeed.length > MAX_FEED) _eventFeed.length = MAX_FEED;

  const cnt = document.getElementById('feed-count');
  if (cnt) cnt.textContent = _eventFeed.length;
  const kpi = document.getElementById('kpi-events');
  if (kpi) kpi.textContent = _eventFeed.length;

  if (_currentTab === 'overview') _renderOverviewFeed();
  if (_currentTab === 'security') _renderSecurityTable();
  if (_currentTab === 'logs')     _appendLogLine(ev);
}

// ---------------------------------------------------------------------------
// Tab system
// ---------------------------------------------------------------------------

let _currentTab = 'overview';
const _tabLoaders = {};

function _showTab(name) {
  _currentTab = name;
  document.querySelectorAll('.nav-item[data-tab]').forEach(el => {
    el.classList.toggle('active', el.dataset.tab === name);
  });
  document.querySelectorAll('.tab-pane').forEach(el => {
    el.style.display = el.id === `tab-${name}` ? '' : 'none';
  });
  const loader = _tabLoaders[name];
  if (loader) loader();
}

function _registerTab(name, loader) { _tabLoaders[name] = loader; }

// ---------------------------------------------------------------------------
// Overview tab
// ---------------------------------------------------------------------------

async function _loadOverview() {
  const [healthRes, riskRes, usersRes, egressRes] = await Promise.all([
    _get('/health'),
    _get('/security/risk'),
    _get('/users'),
    _get('/egress/pending'),
  ]);
  const health  = healthRes.data  || {};
  const risk    = riskRes.data    || {};
  const users   = usersRes.data   || [];
  const pending = egressRes.data  || [];

  const running = (health.services || []).filter(s => s.status === 'running').length;
  const total   = (health.services || []).length;
  const score   = risk.risk_score ?? '--';
  const level   = risk.level ?? 'low';

  _setText('kpi-risk',        score);
  _setText('kpi-risk-sub',    level.toUpperCase());
  _setText('kpi-services',    `${running}/${total}`);
  _setText('kpi-services-sub', running === total ? 'All running' : 'Degraded');
  _setText('kpi-contribs',    Array.isArray(users) ? users.length : '--');
  _setText('kpi-egress',      Array.isArray(pending) ? pending.length : '--');

  _renderOverviewFeed();
}

function _setText(id, val) {
  const el = document.getElementById(id);
  if (el) el.textContent = val;
}

function _renderOverviewFeed() {
  const el = document.getElementById('overview-feed');
  if (!el) return;
  const items = _eventFeed.slice(0, 50);
  if (!items.length) {
    el.innerHTML = '<div class="feed-item" style="color:var(--text-muted)">No events yet — listening...</div>';
    return;
  }
  el.innerHTML = items.map(ev =>
    `<div class="feed-item">
      <span class="feed-ts">${_ts(ev.timestamp)}</span>
      ${_sevBadge(ev.severity || 'info')}
      <span class="feed-body">${_esc(ev.summary || ev.type || '')}</span>
    </div>`
  ).join('');
}

// ---------------------------------------------------------------------------
// Security tab
// ---------------------------------------------------------------------------

async function _loadSecurity() {
  const [evRes, corrRes, riskRes] = await Promise.all([
    _get('/security/events?limit=100'),
    _get('/security/correlation'),
    _get('/security/risk'),
  ]);
  _renderSecurityTable(evRes.data);
  _renderCorrelation(corrRes.data);
  const risk = riskRes.data || {};
  const score = risk.risk_score ?? '--';
  const level = risk.level ?? 'low';
  const el = document.getElementById('risk-score-big');
  if (el) { el.textContent = score; el.className = `risk-score ${level}`; }
  _setText('risk-level-label', level.toUpperCase());
  _setText('risk-updated', `Updated ${_ago(risk.updated_at)}`);
}

function _renderSecurityTable(events) {
  const data = Array.isArray(events) ? events : _eventFeed.filter(e => e.type === 'security_event');
  const sev   = document.getElementById('sev-filter')?.value || '';
  const rows  = data.filter(ev => !sev || ev.severity === sev).slice(0, 100);
  const tbody = document.getElementById('security-tbody');
  if (!tbody) return;
  if (!rows.length) {
    tbody.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">No events</td></tr>';
    return;
  }
  tbody.innerHTML = rows.map(ev =>
    `<tr>
      <td>${_ts(ev.timestamp)}</td>
      <td>${_sevBadge(ev.severity || 'info')}</td>
      <td>${_esc(ev.event_type || ev.type || '')}</td>
      <td>${_esc(ev.source_module || '')}</td>
      <td>${_esc((ev.summary || '').slice(0, 100))}</td>
    </tr>`
  ).join('');
}

function _renderCorrelation(corr) {
  const el = document.getElementById('correlation-panel');
  if (!el) return;
  el.innerHTML = corr
    ? `<pre style="font-size:11px;white-space:pre-wrap;color:var(--text)">${_esc(JSON.stringify(corr, null, 2))}</pre>`
    : '<span>No correlation data</span>';
}

window._reloadSecurity = _loadSecurity;

// ---------------------------------------------------------------------------
// Scanners tab
// ---------------------------------------------------------------------------

const SCANNER_INFO = {
  trivy:   { label: 'Trivy',     desc: 'CVE / image vulnerability scanning', iec: 'FR3 SR 3.4' },
  clamav:  { label: 'ClamAV',   desc: 'Malware / antivirus scanning',         iec: 'FR3 SR 3.2' },
  falco:   { label: 'Falco',    desc: 'Runtime eBPF syscall detection',        iec: 'FR3 SR 3.5 / FR6' },
  wazuh:   { label: 'Wazuh',    desc: 'HIDS / file integrity monitoring',      iec: 'FR3 SR 3.2 / FR6 SR 6.2' },
  openscap:{ label: 'OpenSCAP', desc: 'CIS Benchmark / DISA STIG compliance',  iec: 'FR3 SR 3.3' },
};

async function _loadScanners() {
  const [scannersRes, sbomRes] = await Promise.all([
    _get('/scanners'),
    _get('/sbom'),
  ]);
  _renderScanners(scannersRes.data);
  _renderSbom(sbomRes.data, sbomRes.status);
  _setText('scanners-updated', `Updated ${new Date().toLocaleTimeString()}`);
}

function _renderScanners(data) {
  const grid = document.getElementById('scanner-grid');
  if (!grid) return;
  if (!data || typeof data !== 'object') {
    grid.innerHTML = '<div style="color:var(--text-muted);font-size:12px">No scanner data available — sidecars may not be running.</div>';
    return;
  }
  grid.innerHTML = Object.entries(SCANNER_INFO).map(([key, info]) => {
    const s = data[key] || {};
    const status  = s.status || 'unknown';
    const findings = s.findings ?? 0;
    const crit = s.critical ?? 0;
    const high = s.high ?? 0;
    const med  = s.medium ?? 0;
    const low  = s.low ?? 0;
    const statusCls = {clean:'success', ok:'success', critical:'critical', error:'error'}[status] || 'unknown';
    const statusBadge = {
      clean:'success', ok:'success', critical:'critical', error:'danger', error2:'danger', unknown:'muted',
    };
    return `
      <div class="scanner-card status-${statusCls}">
        <div class="scanner-header">
          <span class="scanner-name">${_esc(info.label)}</span>
          <span class="badge badge-${statusBadge[status] || 'muted'}">${_esc(status)}</span>
        </div>
        <div class="scanner-body">
          <div class="scanner-row"><span class="scanner-label">Role</span><span class="scanner-val">${_esc(info.desc)}</span></div>
          <div class="scanner-row"><span class="scanner-label">IEC 62443</span><span class="scanner-val" style="color:var(--accent)">${_esc(info.iec)}</span></div>
          <div class="scanner-row"><span class="scanner-label">Total findings</span><span class="scanner-val ${findings > 0 ? 'sev-high' : ''}">${findings}</span></div>
          ${s.timestamp ? `<div class="scanner-row"><span class="scanner-label">Last scan</span><span class="scanner-val">${_ago(s.timestamp)}</span></div>` : ''}
          <div class="finding-pills">
            ${crit ? `<span class="fpill fpill-c">C:${crit}</span>` : ''}
            ${high ? `<span class="fpill fpill-h">H:${high}</span>` : ''}
            ${med  ? `<span class="fpill fpill-m">M:${med}</span>`  : ''}
            ${low  ? `<span class="fpill fpill-l">L:${low}</span>`  : ''}
            ${!crit && !high && !med && !low ? `<span style="font-size:11px;color:var(--text-muted)">No findings</span>` : ''}
          </div>
          ${s.error ? `<div style="margin-top:.5rem;font-size:11px;color:var(--danger)">${_esc(s.error)}</div>` : ''}
        </div>
      </div>`;
  }).join('');
}

function _renderSbom(sbom, status) {
  const el = document.getElementById('sbom-panel');
  if (!el) return;
  if (!sbom || status === 404) {
    el.innerHTML = '<span style="color:var(--text-muted)">No SBOM available — run <code>scripts/security-scan.sh</code> to generate.</span>';
    return;
  }
  const pkg_count = sbom.packages?.length ?? sbom.spdxVersion ? Object.keys(sbom).length : '?';
  el.innerHTML = `
    <div class="sbom-field">Format</div>       <div class="sbom-val">${_esc(sbom.spdxVersion || sbom.bomFormat || 'SPDX')}</div>
    <div class="sbom-field">Document name</div><div class="sbom-val">${_esc(sbom.name || '—')}</div>
    <div class="sbom-field">Created</div>      <div class="sbom-val">${_esc(sbom.creationInfo?.created || sbom.metadata?.timestamp || '—')}</div>
    <div class="sbom-field">Packages</div>     <div class="sbom-val">${pkg_count}</div>
  `;
}

window._reloadScanners = _loadScanners;

window._downloadSbom = async function() {
  const { data, status } = await _get('/sbom');
  if (!data || status === 404) { _toast('No SBOM available', 'warning'); return; }
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = Object.assign(document.createElement('a'), { href: url, download: 'agentshroud-sbom.json' });
  a.click();
  URL.revokeObjectURL(url);
};

// ---------------------------------------------------------------------------
// Scorecard tab
// ---------------------------------------------------------------------------

const MATURITY_LEVELS = ['Not Started', 'Initial', 'Managed', 'Defined', 'Measured', 'Optimizing'];
const MATURITY_DESC = {
  0: 'No tooling or process in place.',
  1: 'Tool exists but not integrated or automated.',
  2: 'Tool integrated, manual execution.',
  3: 'Automated, part of CI/CD or runtime pipeline.',
  4: 'Metrics tracked, SLAs defined, dashboard visibility.',
  5: 'Continuous improvement, anomaly-driven tuning, audit-ready.',
};

async function _loadScorecard() {
  const { data } = await _get('/scorecard');
  _renderScorecard(data);
}

function _renderScorecard(data) {
  if (!data || !data.domains) {
    document.getElementById('scorecard-grid').innerHTML = '<div style="color:var(--text-muted);font-size:12px">Scorecard unavailable — run security scan to populate.</div>';
    return;
  }
  const overall  = data.overall_score ?? 0;
  const level    = data.overall_level || MATURITY_LEVELS[Math.round(overall)] || 'Unknown';
  const scoreFmt = typeof overall === 'number' ? overall.toFixed(1) : '--';

  const scoreEl = document.getElementById('scorecard-score');
  if (scoreEl) {
    scoreEl.textContent = scoreFmt;
    scoreEl.className   = `scorecard-overall-score score-${Math.round(overall)}`;
  }
  _setText('scorecard-level', `${level} Maturity`);
  _setText('scorecard-desc', `${MATURITY_DESC[Math.round(overall)] || ''} — 12-domain IEC 62443 / NIST SP 800-190 / CIS Docker Benchmark assessment.`);

  const grid = document.getElementById('scorecard-grid');
  if (!grid) return;
  grid.innerHTML = data.domains.map((d, i) => {
    const sc    = d.score ?? 0;
    const refs  = (d.standard_refs || []).join(' · ');
    const tools = (d.tools || []);
    return `
      <div class="domain-card">
        <div class="domain-card-header">
          <div>
            <div class="domain-num">DOMAIN ${String(i+1).padStart(2,'0')}</div>
            <div class="domain-name">${_esc(d.name)}</div>
          </div>
          <div class="domain-score-num score-${sc}">${sc}<span style="font-size:12px;opacity:.6">/5</span></div>
        </div>
        <div class="score-bar-track"><div class="score-bar-fill fill-${sc}"></div></div>
        <div class="domain-refs">${_esc(refs)}</div>
        <div class="domain-tools">${tools.map(t => `<span class="tool-tag">${_esc(t)}</span>`).join('')}</div>
        ${d.details ? `<div style="font-size:11px;color:var(--text-muted);margin-top:.4rem">${_esc(d.details)}</div>` : ''}
      </div>`;
  }).join('');
}

window._reloadScorecard = _loadScorecard;

// ---------------------------------------------------------------------------
// Services tab
// ---------------------------------------------------------------------------

async function _loadServices() {
  const { data: services } = await _get('/services');
  _renderServices(services);
  _setText('services-updated', `Updated ${new Date().toLocaleTimeString()}`);
}

function _renderServices(services) {
  const grid = document.getElementById('services-grid');
  if (!grid) return;
  if (!Array.isArray(services) || !services.length) {
    grid.innerHTML = '<div style="color:var(--text-muted);font-size:12px">No services found</div>';
    return;
  }
  grid.innerHTML = services.map(s => {
    const statusCls = s.status === 'running' ? 'running' : s.status === 'unhealthy' ? 'unhealthy' : 'stopped';
    const statusBadge = s.status === 'running' ? 'success' : s.status === 'unhealthy' ? 'danger' : 'muted';
    const healthBadge = s.health === 'healthy' ? 'success' : s.health === 'unhealthy' ? 'danger' : 'muted';
    return `
      <div class="svc-card ${statusCls}">
        <div class="svc-header">
          <span class="svc-name">${_esc(s.name)}</span>
          <span class="badge badge-${statusBadge}">${_esc(s.status)}</span>
        </div>
        <div class="svc-body">
          <div class="svc-row"><span class="svc-label">Health</span>     <span class="badge badge-${healthBadge}">${_esc(s.health || '—')}</span></div>
          <div class="svc-row"><span class="svc-label">Uptime</span>     <span>${s.uptime_seconds != null ? _uptime(s.uptime_seconds) : '—'}</span></div>
          <div class="svc-row"><span class="svc-label">Restarts</span>   <span>${s.restart_count ?? '—'}</span></div>
          ${s.image ? `<div class="svc-row"><span class="svc-label">Image</span><span style="font-size:11px">${_esc(s.image.slice(0,40))}</span></div>` : ''}
          <div class="svc-actions">
            <button class="btn btn-sm" onclick="window._svcAction('restart','${_esc(s.name)}')">Restart</button>
            <button class="btn btn-sm" onclick="window._svcAction('update','${_esc(s.name)}')">Update</button>
            <button class="btn btn-sm btn-danger" onclick="window._svcAction('stop','${_esc(s.name)}')">Stop</button>
            <button class="btn btn-sm" onclick="window._viewSvcLogs('${_esc(s.name)}')">Logs</button>
          </div>
        </div>
      </div>`;
  }).join('');
}

window._reloadServices = _loadServices;

window._svcAction = function(action, name) {
  const labels = { restart: 'Restart', update: 'Pull latest image and restart', stop: 'Stop' };
  _confirm(
    `${labels[action] || action} ${name}`,
    `This will ${(labels[action] || action).toLowerCase()} the container "${name}". Continue?`,
    async () => {
      const { data } = await _post(`/services/${encodeURIComponent(name)}/${action}`, { confirm: true });
      _toast(data?.ok ? `${name}: ${action} initiated` : `Error: ${data?.message || 'failed'}`, data?.ok ? 'success' : 'danger');
      setTimeout(_loadServices, 2000);
    },
    action === 'stop',
  );
};

window._viewSvcLogs = async function(name) {
  const { data } = await _get(`/services/${encodeURIComponent(name)}/logs?tail=200`);
  const el = document.getElementById('log-viewer');
  if (el) { el.textContent = (data?.lines || []).join('\n'); _showTab('logs'); }
};

// ---------------------------------------------------------------------------
// Contributors tab
// ---------------------------------------------------------------------------

async function _loadContributors() {
  const [usersRes, groupsRes] = await Promise.all([_get('/users'), _get('/groups')]);
  _renderUsers(usersRes.data);
  _renderGroups(groupsRes.data);
}

function _renderUsers(users) {
  const tbody = document.getElementById('users-tbody');
  if (!tbody) return;
  if (!Array.isArray(users) || !users.length) {
    tbody.innerHTML = '<tr><td colspan="7" style="color:var(--text-muted);text-align:center;padding:1rem">No contributors</td></tr>';
    return;
  }
  const roleCls = { owner: 'info', operator: 'warning', admin: 'warning', collaborator: 'success', viewer: 'muted' };
  tbody.innerHTML = users.map(u =>
    `<tr>
      <td><code>${_esc(u.user_id)}</code></td>
      <td>${_esc(u.display_name || u.user_id)}</td>
      <td><span class="badge badge-${roleCls[u.role] || 'muted'}">${_esc(u.role)}</span></td>
      <td>${(u.groups || []).join(', ') || '—'}</td>
      <td>${_esc(u.collab_mode || '—')}</td>
      <td>${_esc(u.lockdown_level ?? '—')}</td>
      <td>
        <button class="btn btn-sm btn-danger" onclick="window._removeCollab('${_esc(u.user_id)}')">Remove</button>
      </td>
    </tr>`
  ).join('');
}

function _renderGroups(groups) {
  const tbody = document.getElementById('groups-tbody');
  if (!tbody) return;
  if (!Array.isArray(groups) || !groups.length) {
    tbody.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">No groups configured</td></tr>';
    return;
  }
  tbody.innerHTML = groups.map(g =>
    `<tr>
      <td><code>${_esc(g.id)}</code></td>
      <td><strong>${_esc(g.name)}</strong></td>
      <td>${g.members?.length ?? 0}</td>
      <td><span class="badge badge-info">${_esc(g.collab_mode || '—')}</span></td>
      <td><button class="btn btn-sm" onclick="window._editGroup('${_esc(g.id)}')">Edit</button></td>
    </tr>`
  ).join('');
}

window._showContribTab = function(name, el) {
  document.getElementById('contribs-users').style.display  = name === 'users'  ? '' : 'none';
  document.getElementById('contribs-groups').style.display = name === 'groups' ? '' : 'none';
  document.querySelectorAll('.tab-bar .tab').forEach(t => t.classList.remove('active'));
  if (el) el.classList.add('active');
};

window._showAddCollabForm = function() { _toast('Use /addcollab command in Telegram to add a collaborator', 'info'); };
window._removeCollab = function(uid) {
  _confirm('Remove collaborator', `Remove user "${uid}" from all collaborator lists?`, async () => {
    const { data } = await _delete(`/users/${encodeURIComponent(uid)}`);
    _toast(data?.ok ? 'User removed' : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
    _loadContributors();
  });
};
window._editGroup = function(id) { _toast(`Group editing for "${id}" — use Telegram /addtogroup command`, 'info'); };

// ---------------------------------------------------------------------------
// Egress tab
// ---------------------------------------------------------------------------

async function _loadEgress() {
  const [pendingRes, rulesRes] = await Promise.all([_get('/egress/pending'), _get('/egress/rules')]);
  _renderPendingEgress(pendingRes.data);
  _renderEgressRules(rulesRes.data);
  const cnt = document.getElementById('egress-count');
  if (cnt && Array.isArray(pendingRes.data)) cnt.textContent = pendingRes.data.length;
}

function _renderPendingEgress(items) {
  const tbody = document.getElementById('egress-tbody');
  if (!tbody) return;
  if (!Array.isArray(items) || !items.length) {
    tbody.innerHTML = '<tr><td colspan="8" style="color:var(--text-muted);text-align:center;padding:1rem">No pending requests</td></tr>';
    return;
  }
  tbody.innerHTML = items.map(r =>
    `<tr>
      <td><code>${_esc((r.request_id || '').slice(0, 8))}</code></td>
      <td>${_esc(r.domain || '—')}</td>
      <td>${r.port || '—'}</td>
      <td>${_esc(r.agent_id || '—')}</td>
      <td>${_esc(r.tool_name || '—')}</td>
      <td>${_sevBadge(r.risk_level || 'medium')}</td>
      <td>${_ago(r.submitted_at)}</td>
      <td>
        <button class="btn btn-sm btn-success" onclick="window._egressDecide('approve','${_esc(r.request_id)}')">Allow</button>
        <button class="btn btn-sm btn-danger"  onclick="window._egressDecide('deny','${_esc(r.request_id)}')">Deny</button>
      </td>
    </tr>`
  ).join('');
}

function _renderEgressRules(rules) {
  const el = document.getElementById('egress-rules');
  if (!el || !rules) return;
  el.innerHTML = `<pre style="font-size:11px;white-space:pre-wrap;color:var(--text)">${_esc(JSON.stringify(rules, null, 2))}</pre>`;
}

window._reloadEgress = _loadEgress;

window._egressDecide = async function(action, id) {
  const { data } = await _post(`/egress/${encodeURIComponent(id)}/${action}`);
  _toast(data?.ok ? `Egress ${action}d` : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
  setTimeout(_loadEgress, 1000);
};

window._emergencyBlock = function() {
  _confirm('Emergency Egress Block', 'This will immediately block ALL outbound egress from all agents. Active connections will be dropped.', async () => {
    const { data } = await _post('/egress/emergency-block', { confirm: true, reason: 'Manual emergency block from SOC' });
    _toast(data?.ok ? 'All egress blocked' : `Error: ${data?.message}`, data?.ok ? 'danger' : 'warning');
    _loadEgress();
  });
};

// ---------------------------------------------------------------------------
// Logs tab
// ---------------------------------------------------------------------------

function _appendLogLine(ev) {
  const liveEl = document.getElementById('log-live');
  if (liveEl && !liveEl.checked) return;
  const el = document.getElementById('log-viewer');
  if (!el) return;
  const svc  = document.getElementById('log-service-filter')?.value || '';
  if (svc && ev.service !== svc) return;
  const line = `[${_ts(ev.timestamp)}] [${(ev.severity || 'info').toUpperCase().padEnd(8)}] ${ev.summary || ev.type}\n`;
  if (el.textContent === 'Waiting for events...') el.textContent = '';
  el.textContent += line;
  if (el.scrollTop + el.clientHeight >= el.scrollHeight - 40) el.scrollTop = el.scrollHeight;
}

window._clearLogs = function() {
  const el = document.getElementById('log-viewer');
  if (el) el.textContent = 'Log cleared.';
};

// ---------------------------------------------------------------------------
// Config tab
// ---------------------------------------------------------------------------

async function _loadConfig() {
  const { data } = await _get('/config');
  const el = document.getElementById('config-view');
  if (el) el.textContent = JSON.stringify(data, null, 2);

  const { data: modules } = await _get('/security/modules').catch(() => ({ data: null }));
  const mEl = document.getElementById('modules-view');
  if (mEl && modules) {
    mEl.innerHTML = Object.entries(modules).map(([k, v]) =>
      `<div style="display:flex;justify-content:space-between;margin-bottom:.4rem;font-size:12px">
        <span>${_esc(k)}</span>
        <span class="badge badge-${v.enabled ? 'success' : 'muted'}">${v.enabled ? 'enabled' : 'disabled'}</span>
      </div>`
    ).join('');
  }
}

window._reloadConfig = _loadConfig;

// ---------------------------------------------------------------------------
// Kill switch (E-Stop)
// ---------------------------------------------------------------------------

window._ksFreeze = function() {
  _confirm(
    '⏸ Freeze All Containers',
    'This will pause all AgentShroud™ containers (bot, gateway, security sidecars). No data will be lost. Resume by restarting services.',
    async () => {
      const { data } = await _post('/killswitch/freeze', { confirm: true });
      _toast(data?.ok ? 'System frozen — all containers paused' : `Error: ${data?.message || 'failed'}`, data?.ok ? 'warning' : 'danger');
    },
    false,
  );
};

window._ksHalt = function() {
  _confirm(
    '■ Halt System',
    'This will perform a full compose-down, stopping all containers. The system will be offline until manually restarted. Are you certain?',
    async () => {
      const { data } = await _post('/killswitch/shutdown', { confirm: true });
      _toast(data?.ok ? 'Shutdown initiated — system going offline' : `Error: ${data?.message || 'failed'}`, data?.ok ? 'danger' : 'warning');
    },
    true,
  );
};

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
  // Token prompt
  if (!_token) {
    _token = prompt('AgentShroud™ SOC — Enter gateway token:') || '';
    if (_token) localStorage.setItem('soc_token', _token);
  }

  // Register tab loaders
  _registerTab('overview',     _loadOverview);
  _registerTab('security',     _loadSecurity);
  _registerTab('scanners',     _loadScanners);
  _registerTab('scorecard',    _loadScorecard);
  _registerTab('services',     _loadServices);
  _registerTab('contributors', _loadContributors);
  _registerTab('egress',       _loadEgress);
  _registerTab('logs',         () => {});
  _registerTab('config',       _loadConfig);

  // Wire nav items
  document.querySelectorAll('.nav-item[data-tab]').forEach(el => {
    el.addEventListener('click', e => { e.preventDefault(); _showTab(el.dataset.tab); });
  });

  // Severity filter change handler
  const sevFilter = document.getElementById('sev-filter');
  if (sevFilter) sevFilter.addEventListener('change', () => _renderSecurityTable());

  // Show overview
  _showTab('overview');

  // Connect WebSocket
  if (_token) _connectWS();
  else _setWSStatus('disconnected');
});
