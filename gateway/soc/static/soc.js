// AgentShroud SOC — Unified Dashboard JavaScript
// Connects to /soc/v1/ REST API and /soc/v1/ws WebSocket stream.
// No build toolchain required — vanilla JS.

'use strict';

const SOC_BASE = '/soc/v1';
let _token = localStorage.getItem('soc_token') || '';
let _ws = null;
let _wsStatus = 'disconnected';
let _eventFeed = [];
const MAX_FEED = 200;

// ---------------------------------------------------------------------------
// Auth helpers
// ---------------------------------------------------------------------------

async function _api(method, path, body) {
  const opts = {
    method,
    headers: {
      'Authorization': `Bearer ${_token}`,
      'Content-Type': 'application/json',
    },
  };
  if (body !== undefined) opts.body = JSON.stringify(body);
  const resp = await fetch(`${SOC_BASE}${path}`, opts);
  const data = await resp.json().catch(() => ({}));
  return { ok: resp.ok, status: resp.status, data };
}

function _get(path)        { return _api('GET',    path); }
function _post(path, body) { return _api('POST',   path, body); }
function _put(path, body)  { return _api('PUT',    path, body); }
function _delete(path)     { return _api('DELETE', path); }

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
  _ws.addEventListener('close', () => {
    _setWSStatus('disconnected');
    setTimeout(_connectWS, 5000);
  });
  _ws.addEventListener('error', () => _setWSStatus('disconnected'));
}

function _setWSStatus(st) {
  _wsStatus = st;
  const el = document.getElementById('ws-status');
  if (!el) return;
  el.textContent = st === 'connected' ? '● Live' : st === 'connecting' ? '● Connecting' : '○ Disconnected';
  el.className = `ws-status ${st}`;
}

function _handleWSEvent(ev) {
  _eventFeed.unshift(ev);
  if (_eventFeed.length > MAX_FEED) _eventFeed.length = MAX_FEED;
  // Re-render feed on active tabs
  if (_currentTab === 'overview') _renderOverviewFeed();
  if (_currentTab === 'security') _renderSecurityTable();
  if (_currentTab === 'logs')     _appendLogLine(ev);
  _updateKPIs();
}

// ---------------------------------------------------------------------------
// Tab navigation
// ---------------------------------------------------------------------------

let _currentTab = 'overview';
const _tabLoaders = {};

function _showTab(name) {
  _currentTab = name;
  document.querySelectorAll('.tab').forEach(t => t.classList.toggle('active', t.dataset.tab === name));
  document.querySelectorAll('.tab-pane').forEach(p => p.style.display = p.id === `tab-${name}` ? '' : 'none');
  const loader = _tabLoaders[name];
  if (loader) loader();
}

function _registerTab(name, loader) {
  _tabLoaders[name] = loader;
}

// ---------------------------------------------------------------------------
// Severity helpers
// ---------------------------------------------------------------------------

function _sevBadge(sev) {
  const cls = { critical: 'danger', high: 'danger', medium: 'warning', low: 'muted', info: 'info' };
  return `<span class="badge badge-${cls[sev] || 'muted'} sev-${sev}">${sev.toUpperCase()}</span>`;
}

function _ts(iso) {
  if (!iso) return '';
  try { return new Date(iso).toLocaleTimeString(); } catch { return iso.slice(11, 19); }
}

// ---------------------------------------------------------------------------
// Overview tab
// ---------------------------------------------------------------------------

async function _loadOverview() {
  // KPIs
  const [health, risk, events] = await Promise.all([
    _get('/health').then(r => r.data),
    _get('/security/risk').then(r => r.data),
    _get('/security/events?limit=20').then(r => r.data),
  ]);
  _renderKPIs(health, risk, events);
  _renderOverviewFeed();
}

function _renderKPIs(health, risk, events) {
  const score = risk?.risk_score ?? 0;
  const level = risk?.level ?? 'low';
  const running = (health?.services || []).filter(s => s.status === 'running').length;
  const total   = (health?.services || []).length;
  const evCount = Array.isArray(events) ? events.length : 0;

  const el = document.getElementById('kpi-strip');
  if (!el) return;
  el.innerHTML = `
    <div class="kpi-card">
      <div class="kpi-label">Risk Score</div>
      <div class="kpi-value risk-score ${level}">${score}</div>
      <div class="kpi-sub">${level.toUpperCase()}</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">Services</div>
      <div class="kpi-value">${running}/${total}</div>
      <div class="kpi-sub">${running === total ? 'All running' : 'Check services'}</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">Recent Events</div>
      <div class="kpi-value">${evCount}</div>
      <div class="kpi-sub">Last hour</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">Stream</div>
      <div class="kpi-value" id="kpi-stream-count">${_eventFeed.length}</div>
      <div class="kpi-sub" id="ws-status" class="ws-status ${_wsStatus}">● ${_wsStatus}</div>
    </div>
  `;
}

function _updateKPIs() {
  const el = document.getElementById('kpi-stream-count');
  if (el) el.textContent = _eventFeed.length;
}

function _renderOverviewFeed() {
  const el = document.getElementById('overview-feed');
  if (!el) return;
  const items = _eventFeed.slice(0, 40);
  if (!items.length) { el.innerHTML = '<div class="feed-item" style="color:var(--text-muted)">No events yet — listening...</div>'; return; }
  el.innerHTML = items.map(ev =>
    `<div class="feed-item">
      <span class="feed-ts">${_ts(ev.timestamp)}</span>
      <span class="feed-sev">${_sevBadge(ev.severity || 'info')}</span>
      <span class="feed-body">${_esc(ev.summary || ev.type)}</span>
    </div>`
  ).join('');
}

// ---------------------------------------------------------------------------
// Security tab
// ---------------------------------------------------------------------------

async function _loadSecurity() {
  const { data: events } = await _get('/security/events?limit=100');
  const { data: corr }   = await _get('/security/correlation');
  _renderSecurityTable(events);
  _renderCorrelation(corr);
}

function _renderSecurityTable(events) {
  const data = events || _eventFeed.filter(e => e.type === 'security_event');
  const el = document.getElementById('security-events-table');
  if (!el) return;
  if (!data.length) { el.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);padding:1rem">No events</td></tr>'; return; }
  el.innerHTML = data.slice(0, 100).map(ev =>
    `<tr>
      <td>${_ts(ev.timestamp)}</td>
      <td>${_sevBadge(ev.severity || 'info')}</td>
      <td>${_esc(ev.event_type || ev.type || '')}</td>
      <td>${_esc(ev.source_module || '')}</td>
      <td>${_esc((ev.summary || '').slice(0, 80))}</td>
    </tr>`
  ).join('');
}

function _renderCorrelation(corr) {
  const el = document.getElementById('correlation-panel');
  if (!el || !corr) return;
  el.innerHTML = `<pre style="font-size:12px;white-space:pre-wrap">${JSON.stringify(corr, null, 2)}</pre>`;
}

// ---------------------------------------------------------------------------
// Services tab
// ---------------------------------------------------------------------------

async function _loadServices() {
  const { data: services } = await _get('/services');
  _renderServicesTable(services);
}

function _renderServicesTable(services) {
  const el = document.getElementById('services-table');
  if (!el) return;
  if (!Array.isArray(services) || !services.length) {
    el.innerHTML = '<tr><td colspan="6" style="color:var(--text-muted);padding:1rem">No services found</td></tr>';
    return;
  }
  el.innerHTML = services.map(s => {
    const cls = s.status === 'running' ? 'success' : s.status === 'unhealthy' ? 'danger' : 'muted';
    return `<tr>
      <td><strong>${_esc(s.name)}</strong></td>
      <td><span class="badge badge-${cls}">${s.status}</span></td>
      <td><span class="badge badge-${s.health === 'healthy' ? 'success' : 'muted'}">${s.health}</span></td>
      <td>${s.uptime_seconds ? _uptime(s.uptime_seconds) : '—'}</td>
      <td>${s.restart_count}</td>
      <td>
        <button class="btn btn-sm" onclick="svcAction('restart','${_esc(s.name)}')">Restart</button>
        <button class="btn btn-sm btn-danger" onclick="svcAction('stop','${_esc(s.name)}')">Stop</button>
        <button class="btn btn-sm" onclick="viewLogs('${_esc(s.name)}')">Logs</button>
      </td>
    </tr>`;
  }).join('');
}

function _uptime(sec) {
  const h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60);
  return h > 0 ? `${h}h ${m}m` : `${m}m`;
}

window.svcAction = async function(action, name) {
  if (!confirm(`${action} ${name}?`)) return;
  const { data } = await _post(`/services/${encodeURIComponent(name)}/${action}`, { confirm: true });
  _toast(data?.ok ? `${name}: ${action} initiated` : `Error: ${data?.message || 'failed'}`, data?.ok ? 'success' : 'danger');
  setTimeout(_loadServices, 2000);
};

window.viewLogs = async function(name) {
  const { data } = await _get(`/services/${encodeURIComponent(name)}/logs?tail=100`);
  const el = document.getElementById('log-viewer');
  if (el) {
    el.textContent = (data?.lines || []).join('\n');
    _showTab('logs');
  }
};

// ---------------------------------------------------------------------------
// Contributors tab
// ---------------------------------------------------------------------------

async function _loadContributors() {
  const { data: users } = await _get('/users');
  const { data: groups } = await _get('/groups');
  _renderUsersTable(users);
  _renderGroupsTable(groups);
}

function _renderUsersTable(users) {
  const el = document.getElementById('users-table');
  if (!el) return;
  if (!Array.isArray(users) || !users.length) {
    el.innerHTML = '<tr><td colspan="6" style="color:var(--text-muted);padding:1rem">No contributors</td></tr>';
    return;
  }
  el.innerHTML = users.map(u => {
    const roleCls = { owner: 'info', admin: 'warning', collaborator: 'success', viewer: 'muted' };
    return `<tr>
      <td>${_esc(u.user_id)}</td>
      <td>${_esc(u.display_name || u.user_id)}</td>
      <td><span class="badge badge-${roleCls[u.role] || 'muted'}">${u.role}</span></td>
      <td>${(u.groups || []).join(', ') || '—'}</td>
      <td>${u.collab_mode}</td>
      <td>${u.lockdown_level}</td>
    </tr>`;
  }).join('');
}

function _renderGroupsTable(groups) {
  const el = document.getElementById('groups-table');
  if (!el) return;
  if (!Array.isArray(groups) || !groups.length) {
    el.innerHTML = '<tr><td colspan="4" style="color:var(--text-muted);padding:1rem">No groups configured</td></tr>';
    return;
  }
  el.innerHTML = groups.map(g =>
    `<tr>
      <td><strong>${_esc(g.id)}</strong></td>
      <td>${_esc(g.name)}</td>
      <td>${g.members?.length ?? 0}</td>
      <td><span class="badge badge-info">${g.collab_mode}</span></td>
    </tr>`
  ).join('');
}

// ---------------------------------------------------------------------------
// Egress tab
// ---------------------------------------------------------------------------

async function _loadEgress() {
  const [pending, rules] = await Promise.all([
    _get('/egress/pending').then(r => r.data),
    _get('/egress/rules').then(r => r.data),
  ]);
  _renderPendingEgress(pending);
  _renderEgressRules(rules);
}

function _renderPendingEgress(items) {
  const el = document.getElementById('egress-pending-table');
  if (!el) return;
  if (!Array.isArray(items) || !items.length) {
    el.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);padding:1rem">No pending requests</td></tr>';
    return;
  }
  el.innerHTML = items.map(r =>
    `<tr>
      <td>${_esc(r.domain || r.request_id)}</td>
      <td>${_esc(r.agent_id || '')}</td>
      <td><span class="badge badge-warning">${r.risk_level || ''}</span></td>
      <td>${_ts(r.submitted_at)}</td>
      <td>
        <button class="btn btn-sm btn-success" onclick="egressDecide('approve','${_esc(r.request_id)}')">Approve</button>
        <button class="btn btn-sm btn-danger"  onclick="egressDecide('deny','${_esc(r.request_id)}')">Deny</button>
      </td>
    </tr>`
  ).join('');
}

function _renderEgressRules(rules) {
  const el = document.getElementById('egress-rules');
  if (!el || !rules) return;
  el.innerHTML = `<pre style="font-size:12px;white-space:pre-wrap">${JSON.stringify(rules, null, 2)}</pre>`;
}

window.egressDecide = async function(action, id) {
  const { data } = await _post(`/egress/${encodeURIComponent(id)}/${action}`);
  _toast(data?.ok ? `Egress ${action}d` : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
  setTimeout(_loadEgress, 1000);
};

window.emergencyBlock = async function() {
  if (!confirm('Block ALL outbound egress immediately?')) return;
  const { data } = await _post('/egress/emergency-block', { confirm: true, reason: 'Manual emergency block' });
  _toast(data?.ok ? 'Egress blocked' : 'Error', data?.ok ? 'danger' : 'warning');
};

// ---------------------------------------------------------------------------
// Logs tab
// ---------------------------------------------------------------------------

function _appendLogLine(ev) {
  const el = document.getElementById('log-viewer');
  if (!el) return;
  const line = `[${_ts(ev.timestamp)}] [${(ev.severity || 'info').toUpperCase()}] ${ev.summary || ev.type}\n`;
  el.textContent += line;
  if (el.scrollTop + el.clientHeight >= el.scrollHeight - 40) {
    el.scrollTop = el.scrollHeight;
  }
}

// ---------------------------------------------------------------------------
// Config tab
// ---------------------------------------------------------------------------

async function _loadConfig() {
  const { data } = await _get('/config');
  const el = document.getElementById('config-view');
  if (el) el.textContent = JSON.stringify(data, null, 2);
}

// ---------------------------------------------------------------------------
// Kill switch buttons
// ---------------------------------------------------------------------------

window.ksFreeze = async function() {
  if (!confirm('FREEZE: Pause all bot containers?')) return;
  const { data } = await _post('/killswitch/freeze', { confirm: true });
  _toast(data?.ok ? 'Containers frozen' : 'Error', data?.ok ? 'warning' : 'danger');
};

window.ksShutdown = async function() {
  if (!confirm('SHUTDOWN: Perform compose down?')) return;
  const { data } = await _post('/killswitch/shutdown', { confirm: true });
  _toast(data?.ok ? 'Shutdown initiated' : 'Error', data?.ok ? 'warning' : 'danger');
};

// ---------------------------------------------------------------------------
// Toast
// ---------------------------------------------------------------------------

function _toast(msg, type = 'info') {
  const t = document.createElement('div');
  t.style.cssText = `
    position:fixed;bottom:4rem;right:1rem;padding:.5rem 1rem;
    border-radius:4px;font-size:12px;z-index:999;
    background:var(--surface);border:1px solid var(--border);
    color:var(${type === 'success' ? '--success' : type === 'danger' ? '--danger' : '--accent'});
  `;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3000);
}

// ---------------------------------------------------------------------------
// Utility
// ---------------------------------------------------------------------------

function _esc(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', () => {
  // Prompt for token if not set
  if (!_token) {
    _token = prompt('Enter gateway token (AGENTSHROUD_GATEWAY_PASSWORD):') || '';
    if (_token) localStorage.setItem('soc_token', _token);
  }

  // Register tab loaders
  _registerTab('overview',     _loadOverview);
  _registerTab('security',     _loadSecurity);
  _registerTab('services',     _loadServices);
  _registerTab('contributors', _loadContributors);
  _registerTab('egress',       _loadEgress);
  _registerTab('logs',         () => {});
  _registerTab('config',       _loadConfig);

  // Wire tab clicks
  document.querySelectorAll('.tab').forEach(t => {
    t.addEventListener('click', () => _showTab(t.dataset.tab));
  });

  // Show overview by default
  _showTab('overview');

  // Connect WebSocket
  if (_token) _connectWS();
});
