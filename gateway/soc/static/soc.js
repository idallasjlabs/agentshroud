// AgentShroud™ SOC Command Center — v0.9.0
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// Vanilla JS — no build toolchain required.
'use strict';

const SOC_BASE = '/soc/v1';
let _token = (localStorage.getItem('soc_token') || '').replace(/[^a-f0-9]/gi, '');
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
const _put    = (p, b) => _api('PUT',    p, b);
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
  const d = new Date(iso);
  if (isNaN(d.getTime())) return '—';
  const diff = (Date.now() - d) / 1000;
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

// ---------------------------------------------------------------------------
// Login modal
// ---------------------------------------------------------------------------

function _showLoginModal(msg) {
  return new Promise(resolve => {
    const overlay = document.getElementById('login-modal');
    const input   = document.getElementById('login-token');
    const msgEl   = document.getElementById('login-msg');
    if (msgEl && msg) msgEl.textContent = msg;
    if (input) { input.value = ''; }
    if (overlay) overlay.classList.add('open');
    window._loginSubmit = () => {
      const val = (input ? input.value : '').trim();
      if (!val) return;
      _token = val;
      localStorage.setItem('soc_token', _token);
      if (overlay) overlay.classList.remove('open');
      resolve();
    };
    // Allow Enter key to submit
    if (input) {
      input.onkeydown = e => { if (e.key === 'Enter') window._loginSubmit(); };
      setTimeout(() => input.focus(), 50);
    }
  });
}

async function _connectWS() {
  if (_ws && _ws.readyState <= 1) return;
  _setWSStatus('connecting');
  // Exchange bearer token for a short-lived one-time WS token
  let wsToken = _token;
  try {
    const r = await _post('/auth/ws-token');
    if (r.ok && r.data.token) {
      wsToken = r.data.token;
    } else if (r.status === 401) {
      // Token rejected — clear and show login modal, then retry WS
      localStorage.removeItem('soc_token');
      _token = '';
      await _showLoginModal('Session expired — re-enter gateway token.');
      _setWSStatus('disconnected');
      setTimeout(_connectWS, 200);
      return;
    }
  } catch (_) {}
  const wsBase = location.origin.replace(/^http/, 'ws');
  _ws = new WebSocket(`${wsBase}${SOC_BASE}/ws?token=${encodeURIComponent(wsToken)}`);
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
  const [healthRes, riskRes, usersRes, egressRes, eventsRes] = await Promise.all([
    _get('/health'),
    _get('/security/risk'),
    _get('/users'),
    _get('/egress/pending'),
    _get('/security/events?limit=50'),  // CC-02: seed events KPI + feed on load
  ]);
  const health  = healthRes.data  || {};
  const risk    = riskRes.data    || {};
  const users   = usersRes.data   || [];
  const pending = Array.isArray(egressRes.data) ? egressRes.data : [];
  const events  = Array.isArray(eventsRes.data) ? eventsRes.data : [];

  // CC-04: seed _eventFeed from REST so feed is populated before WS connects
  if (events.length && _eventFeed.length === 0) {
    _eventFeed = events.slice(0, MAX_FEED);
  }

  const running = (health.services || []).filter(s => s.status === 'running' || s.status === 'standby').length;
  const total   = (health.services || []).length;
  const score   = risk.risk_score ?? '--';
  const level   = risk.level ?? 'low';

  _setText('kpi-risk',        score);
  _setText('kpi-risk-sub',    level.toUpperCase());
  _setText('kpi-services',    `${running}/${total}`);
  _setText('kpi-services-sub', running === total ? 'All running' : 'Degraded');
  _setText('kpi-contribs',    Array.isArray(users) ? users.length : '--');
  _setText('kpi-egress',      Array.isArray(pending) ? pending.length : '--');
  // CC-02: set events KPI from REST count
  _setText('kpi-events', _eventFeed.length);
  const cnt = document.getElementById('feed-count');
  if (cnt) cnt.textContent = _eventFeed.length;

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
  // CC-13: render structured panels instead of raw JSON dump
  const el = document.getElementById('correlation-panel');
  if (!el) return;
  if (!corr || corr.status === 'unavailable') {
    el.innerHTML = '<span style="color:var(--text-muted)">No correlation data available</span>';
    return;
  }
  const signals = Array.isArray(corr.signals) ? corr.signals : [];
  const denied  = Array.isArray(corr.top_denied_destinations) ? corr.top_denied_destinations : [];
  const violators = Array.isArray(corr.top_policy_violators) ? corr.top_policy_violators : [];
  const trend   = corr.egress_trend || {};
  const scanners = corr.scanner_findings || {};

  const sigRows = signals.length
    ? signals.map(s => `<tr><td>${_esc(s.signal||s.name||'')}</td><td style="text-align:center">${s.count??0}</td><td style="text-align:center">${s.weight??1}</td><td style="text-align:right;color:var(--accent)">${(s.count??0)*(s.weight??1)}</td></tr>`).join('')
    : '<tr><td colspan="4" style="color:var(--text-muted);text-align:center">No signals</td></tr>';

  el.innerHTML = `
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem">
      <div>
        <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);margin-bottom:.5rem">Signal Breakdown</div>
        <table class="data-table" style="font-size:11px">
          <thead><tr><th>Signal</th><th>Count</th><th>Weight</th><th>Score</th></tr></thead>
          <tbody>${sigRows}</tbody>
        </table>
      </div>
      <div>
        <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);margin-bottom:.5rem">Egress Trend</div>
        <div style="display:flex;flex-direction:column;gap:.3rem;font-size:12px">
          <div><span style="color:var(--text-muted)">Denied:</span> <strong style="color:var(--danger)">${trend.denied??0}</strong></div>
          <div><span style="color:var(--text-muted)">Allowed:</span> <strong style="color:var(--success)">${trend.allowed??0}</strong></div>
          <div><span style="color:var(--text-muted)">Pending:</span> <strong style="color:var(--warning)">${trend.pending??0}</strong></div>
        </div>
        ${denied.length ? `
        <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);margin:.75rem 0 .3rem">Top Denied Destinations</div>
        ${denied.map(d => `<div style="font-size:11px;display:flex;justify-content:space-between"><code>${_esc(d.destination||d.domain||'unknown')}</code><span style="color:var(--danger)">${d.count??''}</span></div>`).join('')}
        ` : ''}
        ${violators.length ? `
        <div style="font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);margin:.75rem 0 .3rem">Top Policy Violators</div>
        ${violators.map(v => `<div style="font-size:11px;display:flex;justify-content:space-between"><code>${_esc(v.agent_id||v)}</code><span style="color:var(--warning)">${v.count??''}</span></div>`).join('')}
        ` : ''}
      </div>
    </div>`;
}

window._reloadSecurity = _loadSecurity;

// ---------------------------------------------------------------------------
// Scanners tab
// ---------------------------------------------------------------------------

const SCANNER_INFO = {
  trivy:        { label: 'Trivy',      desc: 'CVE / image vulnerability scanning',      iec: 'FR3 SR 3.4' },
  clamav:       { label: 'ClamAV',    desc: 'Malware / antivirus scanning',             iec: 'FR3 SR 3.2' },
  falco:        { label: 'Falco',     desc: 'Runtime eBPF syscall detection',           iec: 'FR3 SR 3.5 / FR6',        noScan: true },
  wazuh:        { label: 'Wazuh',     desc: 'HIDS / file integrity monitoring',         iec: 'FR3 SR 3.2 / FR6 SR 6.2', noScan: true },
  openscap:     { label: 'OpenSCAP',  desc: 'CIS Benchmark / DISA STIG compliance',    iec: 'FR3 SR 3.3' },
  'fluent-bit': { label: 'Fluent Bit',desc: 'Centralized log collection & forwarding', iec: 'FR6 SR 6.2', noScan: true },
};

async function _loadScanners() {
  const [scannersRes, sbomRes] = await Promise.all([
    _get('/scanners'),
    _get('/sbom'),
  ]);
  _renderScanners(scannersRes.data?.scanners ?? scannersRes.data);
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
          ${!info.noScan ? `<div style="margin-top:.75rem">
            <button class="btn btn-sm" onclick="window._runScan('${_esc(key)}', this)">▶ Run Scan</button>
          </div>` : ''}
        </div>
      </div>`;
  }).join('');
}

let _sbomPackagesAll = [];
let _sbomSortCol = 'name';
let _sbomSortAsc = true;
let _sbomTypeFilter = '';

function _renderSbom(sbom, status) {
  const el = document.getElementById('sbom-panel');
  if (!el) return;
  if (!sbom || status === 404) {
    el.innerHTML = '<span style="color:var(--text-muted)">No SBOM available — run <code>scripts/security-scan.sh</code> to generate.</span>';
    const pkgEl = document.getElementById('sbom-packages');
    if (pkgEl) pkgEl.style.display = 'none';
    return;
  }
  const packages = sbom.packages || [];
  const pkg_count = packages.length || '?';
  el.innerHTML = `
    <div class="sbom-field">Format</div>       <div class="sbom-val">${_esc(sbom.spdxVersion || sbom.bomFormat || 'SPDX')}</div>
    <div class="sbom-field">Document name</div><div class="sbom-val">${_esc(sbom.name || '—')}</div>
    <div class="sbom-field">Created</div>      <div class="sbom-val">${_esc(sbom.creationInfo?.created || sbom.metadata?.timestamp || '—')}</div>
    <div class="sbom-field">Packages</div>     <div class="sbom-val">${pkg_count}</div>
  `;
  // CC-19: render package table
  if (packages.length) {
    _sbomPackagesAll = packages.slice().sort((a, b) => (a.name || '').localeCompare(b.name || ''));
    const pkgEl = document.getElementById('sbom-packages');
    if (pkgEl) pkgEl.style.display = '';
    _renderSbomPackageTable(_sbomPackagesAll);
  }
}

function _sbomGetVal(p, col) {
  if (col === 'name')    return (p.name || p.packageName || '').toLowerCase();
  if (col === 'version') return (p.versionInfo || p.version || '').toLowerCase();
  if (col === 'type')    return (p.externalRefs?.[0]?.referenceCategory || p.type || '').toLowerCase();
  if (col === 'loc')     return (p.sourceInfo || p.packageFileName || '').toLowerCase();
  return '';
}

window._sortSbomCol = function(col) {
  if (_sbomSortCol === col) { _sbomSortAsc = !_sbomSortAsc; }
  else { _sbomSortCol = col; _sbomSortAsc = true; }
  _applyAndRenderSbom();
};

window._filterSbomType = function(type) {
  _sbomTypeFilter = type;
  _applyAndRenderSbom();
};

function _applyAndRenderSbom() {
  const searchEl = document.getElementById('sbom-search');
  const query = searchEl ? searchEl.value.trim().toLowerCase() : '';
  let pkgs = _sbomPackagesAll;
  if (query) pkgs = pkgs.filter(p => (p.name || '').toLowerCase().includes(query));
  if (_sbomTypeFilter) pkgs = pkgs.filter(p => (p.externalRefs?.[0]?.referenceCategory || p.type || '') === _sbomTypeFilter);
  pkgs = pkgs.slice().sort((a, b) => {
    const av = _sbomGetVal(a, _sbomSortCol), bv = _sbomGetVal(b, _sbomSortCol);
    return _sbomSortAsc ? av.localeCompare(bv) : bv.localeCompare(av);
  });
  _renderSbomPackageTable(pkgs);
}

function _renderSbomPackageTable(pkgs) {
  const tbl = document.getElementById('sbom-pkg-table');
  if (!tbl) return;
  if (!pkgs.length) {
    tbl.innerHTML = '<span style="color:var(--text-muted);font-size:12px">No packages</span>';
    return;
  }
  const _thStyle = (col) => {
    const active = _sbomSortCol === col;
    const arrow = active ? (_sbomSortAsc ? ' ▲' : ' ▼') : '';
    return `style="cursor:pointer;user-select:none${active ? ';color:var(--accent)' : ''}" onclick="window._sortSbomCol('${col}')"`;
  };
  // Build type filter dropdown options from all packages
  const allTypes = [...new Set(_sbomPackagesAll.map(p => p.externalRefs?.[0]?.referenceCategory || p.type || '').filter(Boolean))].sort();
  const typeOpts = `<option value="">All Types</option>` + allTypes.map(t => `<option value="${_esc(t)}"${_sbomTypeFilter===t?' selected':''}>${_esc(t)}</option>`).join('');
  const typeFilter = allTypes.length > 1
    ? `<select style="font-size:11px;margin-left:8px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:3px" onchange="window._filterSbomType(this.value)">${typeOpts}</select>`
    : '';
  const filterRow = typeFilter ? `<div style="margin-bottom:6px;font-size:11px">Filter by type: ${typeFilter}</div>` : '';
  tbl.innerHTML = filterRow + `<table class="data-table" style="font-size:11px">
    <thead><tr>
      <th ${_thStyle('name')}>Package${_sbomSortCol==='name'?(_sbomSortAsc?' ▲':' ▼'):''}</th>
      <th ${_thStyle('version')}>Version${_sbomSortCol==='version'?(_sbomSortAsc?' ▲':' ▼'):''}</th>
      <th ${_thStyle('type')}>Type${_sbomSortCol==='type'?(_sbomSortAsc?' ▲':' ▼'):''}</th>
      <th ${_thStyle('loc')}>Location${_sbomSortCol==='loc'?(_sbomSortAsc?' ▲':' ▼'):''}</th>
    </tr></thead>
    <tbody>${pkgs.slice(0, 500).map(p => {
      const name    = p.name || p.packageName || '—';
      const version = p.versionInfo || p.version || '—';
      const type    = p.externalRefs?.[0]?.referenceCategory || p.type || '—';
      const loc     = p.sourceInfo || p.packageFileName || '—';
      return `<tr><td><strong>${_esc(name)}</strong></td><td>${_esc(version)}</td><td>${_esc(type)}</td><td style="font-size:10px;color:var(--text-muted)">${_esc(String(loc).slice(0,60))}</td></tr>`;
    }).join('')}</tbody>
  </table>`;
}

window._filterSbomPackages = function(query) {
  _applyAndRenderSbom();
};

window._reloadScanners = _loadScanners;

window._runScan = async function(scanner, btn) {
  // CC-15: poll for scan completion instead of fixed 3s timeout
  if (btn) { btn.disabled = true; btn.textContent = '⏳ Running…'; }
  const { ok, data } = await _post(`/scan/${encodeURIComponent(scanner)}`, {});
  if (!ok) {
    if (btn) { btn.disabled = false; btn.textContent = '▶ Run Scan'; }
    _toast(`Failed to launch ${scanner} scan: ${data?.message || data?.detail || 'unknown error'}`, 'danger');
    return;
  }
  _toast(`${scanner} scan launched — polling for results…`, 'info');
  // Poll every 8s for up to 5 minutes
  let attempts = 0;
  const maxAttempts = 37;
  const poll = setInterval(async () => {
    attempts++;
    const { data: scanners } = await _get('/scanners');
    const s = (scanners?.scanners || {})[scanner];
    if (s && s.status !== 'not_run' && s.timestamp) {
      clearInterval(poll);
      if (btn) { btn.disabled = false; btn.textContent = '▶ Run Scan'; }
      _toast(`${scanner} scan complete`, 'success');
      _loadScanners();
    } else if (attempts >= maxAttempts) {
      clearInterval(poll);
      if (btn) { btn.disabled = false; btn.textContent = '▶ Run Scan'; }
      _toast(`${scanner} scan timed out — check /var/log/security for errors`, 'warning');
      _loadScanners();
    }
  }, 8000);
};

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
    const refs  = d.standard_ref || '';
    const tools = (d.tools || []);
    const nextAction = d.next_action || '';  // CC-21
    const urgency = d.urgency || (sc <= 1 ? 'improvement' : sc <= 3 ? 'attention' : '');
    return `
      <div class="domain-card">
        <div class="domain-card-header">
          <div>
            <div class="domain-num">DOMAIN ${String(i+1).padStart(2,'0')}</div>
            <div class="domain-name">${_esc(d.domain)}</div>
          </div>
          <div class="domain-score-num score-${sc}">${sc}<span style="font-size:12px;opacity:.6">/5</span></div>
        </div>
        <div class="score-bar-track"><div class="score-bar-fill fill-${sc}"></div></div>
        ${d.description ? `<div style="font-size:11px;color:var(--text-muted);margin-top:.4rem;line-height:1.5">${_esc(d.description)}</div>` : ''}
        ${nextAction ? `<div style="font-size:11px;margin-top:.4rem;padding:.3rem .5rem;border-radius:3px;background:var(--accent-dim);color:var(--accent)">→ ${_esc(nextAction)}</div>` : ''}
        <div class="domain-refs">${_esc(refs)}</div>
        <div class="domain-tools">${tools.map(t => `<span class="tool-tag">${_esc(t)}</span>`).join('')}</div>
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
  // CC-25: split container services vs internal gateway modules
  const grid = document.getElementById('services-grid');
  if (!grid) return;
  if (!Array.isArray(services) || !services.length) {
    grid.innerHTML = '<div style="color:var(--text-muted);font-size:12px">No services found</div>';
    return;
  }
  const containers = services.filter(s => !s.is_internal);
  const internals  = services.filter(s => s.is_internal);

  const renderCard = s => {
    const statusCls   = (s.status === 'running' || s.status === 'standby') ? 'running' : s.status === 'unhealthy' ? 'unhealthy' : 'stopped';
    const statusBadge = (s.status === 'running' || s.status === 'standby') ? 'success' : s.status === 'unhealthy' ? 'danger'
                      : s.status === 'not_installed' ? 'muted' : 'warning';
    const healthBadge = s.health === 'healthy' ? 'success' : s.health === 'unhealthy' ? 'danger' : 'muted';
    const statusLabel = s.status === 'not_installed' ? 'not installed' : s.status;
    // CC-26: no Update button (local-only builds, no registry)
    // CC-33: internal services show "Restart Gateway" instead of per-service controls
    // For internal modules, derive a module_filter key so logs are filtered to that module.
    const modFilter = s.is_internal ? s.name.replace(/^agentshroud-/, '').replace(/-/g, '_') : '';
    const actions = s.is_internal
      ? `<button class="btn btn-sm" title="Restart gateway to restart this module" onclick="window._svcAction('restart','agentshroud-gateway')">Restart Gateway</button>
         <button class="btn btn-sm" onclick="window._viewSvcLogs('agentshroud-gateway','${modFilter}')">Logs</button>`
      : `<button class="btn btn-sm" onclick="window._svcAction('restart','${_esc(s.name)}')">Restart</button>
         <button class="btn btn-sm btn-danger" onclick="window._svcAction('stop','${_esc(s.name)}')">Stop</button>
         <button class="btn btn-sm" onclick="window._viewSvcLogs('${_esc(s.name)}')">Logs</button>`;
    return `
      <div class="svc-card ${statusCls}">
        <div class="svc-header">
          <span class="svc-name">${_esc(s.name.replace('agentshroud-', ''))}</span>
          <span class="badge badge-${statusBadge}">${_esc(statusLabel)}</span>
        </div>
        <div class="svc-body">
          <div class="svc-row"><span class="svc-label">Health</span><span class="badge badge-${healthBadge}">${_esc(s.health || '—')}</span></div>
          <div class="svc-row"><span class="svc-label">Uptime</span><span>${s.uptime_seconds != null ? _uptime(Math.round(s.uptime_seconds)) : '—'}</span></div>
          ${!s.is_internal ? `<div class="svc-row"><span class="svc-label">Restarts</span><span>${s.restart_count ?? '—'}</span></div>` : ''}
          ${s.image ? `<div class="svc-row"><span class="svc-label">Image</span><span style="font-size:11px">${_esc(s.image.slice(0,40))}</span></div>` : ''}
          ${s.version ? `<div class="svc-row"><span class="svc-label">Version</span><span>${_esc(s.version)}</span></div>` : ''}
          <div class="svc-actions">${actions}</div>
        </div>
      </div>`;
  };

  let html = '';
  if (containers.length) {
    html += `<div style="grid-column:1/-1;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--text-muted);margin-bottom:-.25rem">Container Services</div>`;
    html += containers.map(renderCard).join('');
  }
  if (internals.length) {
    html += `<div style="grid-column:1/-1;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--text-muted);margin-top:.75rem;margin-bottom:-.25rem">Gateway Modules <span style="font-weight:400;opacity:.6">(restart gateway to restart any module)</span></div>`;
    html += internals.map(renderCard).join('');
  }
  grid.innerHTML = html;
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

// CC-27: show service logs in an inline modal, not by switching tabs
// module_filter: when set, server-side filters gateway logs to lines containing that string
window._viewSvcLogs = async function(name, module_filter) {
  const modal = document.getElementById('log-modal');
  const titleEl = document.getElementById('log-modal-title');
  const bodyEl  = document.getElementById('log-modal-body');
  if (!modal || !bodyEl) { _showTab('logs'); return; }
  if (titleEl) titleEl.textContent = module_filter ? `Logs: ${name} [${module_filter}]` : `Logs: ${name}`;
  bodyEl.textContent = 'Loading…';
  modal.classList.add('open');
  const qs = module_filter ? `?tail=200&filter=${encodeURIComponent(module_filter)}` : '?tail=200';
  const { data } = await _get(`/services/${encodeURIComponent(name)}/logs${qs}`);
  bodyEl.textContent = (data?.lines || []).join('\n') || '(no log output for this module)';
  bodyEl.scrollTop = bodyEl.scrollHeight;
};

window._closeLogModal = function() {
  const modal = document.getElementById('log-modal');
  if (modal) modal.classList.remove('open');
};

// ---------------------------------------------------------------------------
// Contributors tab
// ---------------------------------------------------------------------------

let _allGroups = [];  // cached for group assignment UI

async function _loadContributors() {
  const [usersRes, groupsRes] = await Promise.all([_get('/users'), _get('/groups')]);
  _allGroups = Array.isArray(groupsRes.data) ? groupsRes.data : [];
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
  const roles   = ['owner', 'operator', 'collaborator', 'viewer'];
  tbody.innerHTML = users.map(u =>
    `<tr>
      <td><code style="font-size:11px">${_esc(u.user_id)}</code></td>
      <td>
        <span id="dn-display-${_esc(u.user_id)}" onclick="window._editDisplayName('${_esc(u.user_id)}')" title="Click to edit" style="cursor:pointer;border-bottom:1px dashed var(--text-muted)">${_esc(u.display_name || u.user_id)}</span>
      </td>
      <td>
        <select style="font-size:11px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:3px"
          onchange="window._changeUserRole('${_esc(u.user_id)}',this.value,this)">
          ${roles.map(r => `<option value="${r}"${u.role===r?' selected':''}>${r}</option>`).join('')}
        </select>
      </td>
      <td style="font-size:11px">
        ${(u.groups || []).map(g => `<span class="badge badge-info" style="margin-right:2px">${_esc(g)}</span>`).join('') || '—'}
        <button class="btn btn-sm" style="margin-left:4px;padding:1px 5px" onclick="window._assignGroups('${_esc(u.user_id)}',${JSON.stringify(u.groups||[])})">+</button>
      </td>
      <td style="font-size:11px">
        <select style="font-size:11px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:3px"
          onchange="window._changeUserMode('${_esc(u.user_id)}',this.value,this)">
          <option value="local_only"${u.collab_mode==='local_only'?' selected':''}>Restrictive</option>
          <option value="project_scoped"${u.collab_mode==='project_scoped'?' selected':''}>Project Scoped</option>
          <option value="full_access"${u.collab_mode==='full_access'?' selected':''}>Full Access</option>
        </select>
      </td>
      <td style="font-size:11px">${_esc(u.lockdown_level ?? '—')}</td>
      <td>
        <button class="btn btn-sm btn-danger" onclick="window._removeCollab('${_esc(u.user_id)}')">Remove</button>
      </td>
    </tr>`
  ).join('');
}

// CC-35: inline display name edit
window._editDisplayName = function(uid) {
  const span = document.getElementById(`dn-display-${uid}`);
  if (!span) return;
  const cur = span.textContent;
  const input = document.createElement('input');
  input.type = 'text'; input.value = cur;
  input.style.cssText = 'font-size:11px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--accent);border-radius:3px;width:120px';
  const save = async () => {
    const val = input.value.trim();
    if (val && val !== cur) {
      const { ok, data } = await _put(`/users/${encodeURIComponent(uid)}/display-name`, { display_name: val });
      _toast(ok ? 'Name updated' : `Error: ${data?.message}`, ok ? 'success' : 'danger');
    }
    span.textContent = input.value || cur;
    input.replaceWith(span);
  };
  input.onblur = save;
  input.onkeydown = e => { if (e.key === 'Enter') save(); if (e.key === 'Escape') { input.replaceWith(span); } };
  span.replaceWith(input);
  input.focus(); input.select();
};

// CC-36: role dropdown change
window._changeUserRole = async function(uid, newRole, selectEl) {
  const prev = Array.from(selectEl.options).find(o => o.selected && o.value !== newRole)?.value;
  if (newRole === 'owner') {
    if (!confirm(`Promote ${uid} to OWNER? This grants full administrative control.`)) {
      selectEl.value = prev || 'collaborator'; return;
    }
  }
  const { ok, data } = await _put(`/users/${encodeURIComponent(uid)}/role`, { role: newRole });
  _toast(ok ? `Role changed to ${newRole}` : `Error: ${data?.message}`, ok ? 'success' : 'danger');
  if (!ok) selectEl.value = prev || 'collaborator';
};

// CC-38: collab mode dropdown change
window._changeUserMode = async function(uid, newMode, selectEl) {
  const prev = Array.from(selectEl.options).find(o => o.selected && o.value !== newMode)?.value;
  const labels = { local_only: 'Restrictive', project_scoped: 'Project Scoped', full_access: 'Full Access' };
  const { ok, data } = await _put(`/users/${encodeURIComponent(uid)}/mode`, { mode: newMode });
  if (ok) {
    _toast(`Mode changed to ${labels[newMode] || newMode}`, 'success');
  } else {
    _toast(`Error: ${data?.message || 'failed to set mode'}`, 'danger');
    if (prev) selectEl.value = prev;
  }
};

// CC-37: group assignment modal
window._assignGroups = function(uid, currentGroups) {
  if (!_allGroups.length) { _toast('No groups configured', 'info'); return; }
  const opts = _allGroups.map(g => {
    const checked = currentGroups.includes(g.id) ? 'checked' : '';
    return `<label style="display:flex;align-items:center;gap:.5rem;padding:.25rem 0;font-size:12px">
      <input type="checkbox" data-gid="${_esc(g.id)}" ${checked}> ${_esc(g.name)} <code style="font-size:10px;color:var(--text-muted)">${_esc(g.id)}</code>
    </label>`;
  }).join('');
  _confirm(
    `Assign groups for ${uid}`,
    `__GROUP_ASSIGN_PLACEHOLDER__`,
    async () => {
      const checkboxes = document.querySelectorAll('#modal-body input[type=checkbox]');
      const toAdd = [], toRemove = [];
      checkboxes.forEach(cb => {
        const gid = cb.dataset.gid;
        if (cb.checked && !currentGroups.includes(gid)) toAdd.push(gid);
        if (!cb.checked && currentGroups.includes(gid)) toRemove.push(gid);
      });
      await Promise.all([
        ...toAdd.map(gid => _post(`/groups/${encodeURIComponent(gid)}/members`, { user_id: uid })),
        ...toRemove.map(gid => _delete(`/groups/${encodeURIComponent(gid)}/members/${encodeURIComponent(uid)}`)),
      ]);
      _toast('Group memberships updated', 'success');
      _loadContributors();
    },
    false,
  );
  // Replace modal body with interactive checkboxes
  setTimeout(() => {
    const bodyEl = document.getElementById('modal-body');
    if (bodyEl) bodyEl.innerHTML = `<div style="max-height:200px;overflow-y:auto">${opts}</div>`;
  }, 0);
};

function _renderGroups(groups) {
  const tbody = document.getElementById('groups-tbody');
  if (!tbody) return;
  if (!Array.isArray(groups) || !groups.length) {
    tbody.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">No groups configured — click "+ Create Group" to add one</td></tr>';
    return;
  }
  tbody.innerHTML = groups.map(g =>
    `<tr>
      <td><code>${_esc(g.id)}</code></td>
      <td><strong>${_esc(g.name)}</strong></td>
      <td>${g.members?.length ?? 0}</td>
      <td><span class="badge badge-info">${_esc(g.collab_mode || '—')}</span></td>
      <td><button class="btn btn-sm" onclick="window._openGroupPanel(${JSON.stringify(g)})">Manage</button></td>
    </tr>`
  ).join('');
}

window._showContribTab = function(name, el) {
  document.getElementById('contribs-users').style.display    = name === 'users'    ? '' : 'none';
  document.getElementById('contribs-groups').style.display   = name === 'groups'   ? '' : 'none';
  document.getElementById('contribs-activity').style.display = name === 'activity' ? '' : 'none';
  document.querySelectorAll('.tab-bar .tab').forEach(t => t.classList.remove('active'));
  if (el) el.classList.add('active');
  if (name === 'activity') window._loadActivityLog();
};

// ── Activity log ────────────────────────────────────────────────────────────

// State: all loaded entries (pre-filter), current sort column/dir
window._activityAllEntries = [];
window._activitySortCol = 'timestamp';
window._activitySortAsc = false; // newest first by default

window._loadActivityLog = async function() {
  const userEl = document.getElementById('activity-user-filter');
  const dirEl  = document.getElementById('activity-direction-filter');
  const userId    = userEl ? userEl.value : '';
  const direction = dirEl  ? dirEl.value  : '';

  let url = '/collaborators/activity?limit=0';
  if (userId)    url += `&user_id=${encodeURIComponent(userId)}`;
  if (direction === 'owner') {
    url += '&is_owner=true';
  } else if (direction) {
    url += `&direction=${encodeURIComponent(direction)}`;
  }

  const tbody = document.getElementById('activity-tbody');
  if (tbody) tbody.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">Loading…</td></tr>';

  // Defensive timeout: clear "Loading…" if API takes >12s
  const _loadTimeout = setTimeout(() => {
    const t = document.getElementById('activity-tbody');
    if (t && t.innerHTML.includes('Loading')) {
      t.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">No activity data available — tracker may not be initialised.</td></tr>';
    }
  }, 12000);

  const { ok, data } = await _get(url);
  clearTimeout(_loadTimeout);
  const tbodyEl = document.getElementById('activity-tbody');
  if (!tbodyEl) return;

  if (!ok) {
    tbodyEl.innerHTML = '<tr><td colspan="5" style="color:var(--danger);text-align:center;padding:1rem">Failed to load activity. Check gateway logs.</td></tr>';
    return;
  }
  if (!Array.isArray(data?.entries)) {
    tbodyEl.innerHTML = '<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">No activity recorded yet.</td></tr>';
    return;
  }

  // Use paired_entries (query+response per row) when available; fall back to flat entries
  window._activityAllEntries = Array.isArray(data.paired_entries) ? data.paired_entries : data.entries;
  window._activityPage = 0;

  // Rebuild user filter with display names (username / uid) preserving selection
  if (userEl && !userId) {
    const currentVal = userEl.value;
    const seenUids = [...new Set(data.entries.map(e => e.user_id).filter(Boolean))].sort();
    const nameMap = {};
    data.entries.forEach(e => { if (e.user_id && e.username && e.username !== 'unknown') nameMap[e.user_id] = e.username; });
    userEl.innerHTML = '<option value="">All Users</option>' +
      seenUids.map(uid => {
        const label = nameMap[uid] ? `${nameMap[uid]} (${uid})` : uid;
        return `<option value="${_esc(uid)}"${uid === currentVal ? ' selected' : ''}>${_esc(label)}</option>`;
      }).join('');
  }

  // New-since-last-view badge
  const lastViewed = parseFloat(sessionStorage.getItem('activityLastViewed') || '0');
  const newCount = data.entries.filter(e => (e.timestamp || 0) > lastViewed).length;
  const badge = document.getElementById('activity-new-badge');
  if (badge) {
    if (newCount > 0 && lastViewed > 0) {
      badge.textContent = `${newCount} new`;
      badge.style.display = '';
    } else {
      badge.style.display = 'none';
    }
  }

  // Stats bar
  const statsEl = document.getElementById('activity-stats');
  if (statsEl) {
    const inCount  = data.entries.filter(e => e.direction === 'inbound').length;
    const outCount = data.entries.filter(e => e.direction === 'outbound').length;
    const uniqueUsers = new Set(data.entries.map(e => e.user_id).filter(Boolean)).size;
    const lastTs = data.entries.length ? Math.max(...data.entries.map(e => e.timestamp || 0)) : 0;
    const lastStr = lastTs ? new Date(lastTs * 1000).toLocaleString() : '—';
    statsEl.innerHTML = `<b>${data.total}</b> entries &nbsp;|&nbsp; ${uniqueUsers} user(s) &nbsp;|&nbsp; ↑ ${inCount} inbound &nbsp; ↓ ${outCount} outbound &nbsp;|&nbsp; Last: ${_esc(lastStr)}`;
  }

  window._applyActivitySort();
};

window._filterActivityLocal = function() {
  window._activityPage = 0;
  window._applyActivitySort();
};

const _ACTIVITY_PAGE_SIZE = 100;

window._applyActivitySort = function() {
  const search = (document.getElementById('activity-search')?.value || '').toLowerCase();
  const dirFilter = document.getElementById('activity-direction-filter')?.value || '';
  let entries = window._activityAllEntries.slice();

  // Text search filter — works on both flat entries and paired entries
  if (search) {
    entries = entries.filter(e =>
      (e.user_id || '').toLowerCase().includes(search) ||
      (e.username || '').toLowerCase().includes(search) ||
      (e.message_preview || e.query_preview || e.response_preview || '').toLowerCase().includes(search) ||
      (e.query_preview || '').toLowerCase().includes(search) ||
      (e.response_preview || '').toLowerCase().includes(search) ||
      (e.source || '').toLowerCase().includes(search)
    );
  }

  // Sort
  const col = window._activitySortCol;
  const asc = window._activitySortAsc;
  entries.sort((a, b) => {
    let av = a[col] ?? '', bv = b[col] ?? '';
    if (typeof av === 'number' || typeof bv === 'number') {
      av = parseFloat(av) || 0; bv = parseFloat(bv) || 0;
    } else {
      av = String(av).toLowerCase(); bv = String(bv).toLowerCase();
    }
    if (av < bv) return asc ? -1 : 1;
    if (av > bv) return asc ? 1 : -1;
    return 0;
  });

  window._activityFilteredEntries = entries;
  const page = window._activityPage || 0;
  const start = page * _ACTIVITY_PAGE_SIZE;
  const pageEntries = entries.slice(start, start + _ACTIVITY_PAGE_SIZE);

  _renderActivityLog(pageEntries, search, dirFilter, entries.length);

  const totalPages = Math.max(1, Math.ceil(entries.length / _ACTIVITY_PAGE_SIZE));
  const footer = document.getElementById('activity-footer');
  if (footer) {
    const showing = entries.length === 0 ? 0 : Math.min(start + _ACTIVITY_PAGE_SIZE, entries.length) - start;
    const pageInfo = totalPages > 1
      ? ` &nbsp;|&nbsp; Page ${page + 1} / ${totalPages} &nbsp;`
        + `<button class="btn btn-sm" onclick="window._activityPagePrev()" ${page === 0 ? 'disabled' : ''}>‹ Prev</button> `
        + `<button class="btn btn-sm" onclick="window._activityPageNext()" ${page >= totalPages - 1 ? 'disabled' : ''}>Next ›</button>`
      : '';
    footer.innerHTML = `Showing ${showing} of ${entries.length} (${window._activityAllEntries.length} total)${pageInfo}`;
  }
};

window._activityPagePrev = function() {
  window._activityPage = Math.max(0, (window._activityPage || 0) - 1);
  window._applyActivitySort();
};

window._activityPageNext = function() {
  const total = (window._activityFilteredEntries || []).length;
  const maxPage = Math.max(0, Math.ceil(total / _ACTIVITY_PAGE_SIZE) - 1);
  window._activityPage = Math.min(maxPage, (window._activityPage || 0) + 1);
  window._applyActivitySort();
};

window._sortActivity = function(col) {
  if (window._activitySortCol === col) {
    window._activitySortAsc = !window._activitySortAsc;
  } else {
    window._activitySortCol = col;
    window._activitySortAsc = col !== 'timestamp'; // timestamps default newest-first
  }
  // Update sort indicators
  ['timestamp','user_id','direction'].forEach(c => {
    const el = document.getElementById(`sort-${c}`);
    if (!el) return;
    if (c === col) el.textContent = window._activitySortAsc ? '▲' : '▼';
    else el.textContent = '';
  });
  window._applyActivitySort();
};

window._markActivityViewed = function() {
  sessionStorage.setItem('activityLastViewed', String(Date.now() / 1000));
  const badge = document.getElementById('activity-new-badge');
  if (badge) badge.style.display = 'none';
};

function _renderActivityLog(entries, search, dirFilter, totalFiltered) {
  const tbody = document.getElementById('activity-tbody');
  if (!tbody) return;
  if (!entries || entries.length === 0) {
    let msg;
    if (search) {
      msg = `No entries match "${_esc(search)}".`;
    } else if (dirFilter === 'outbound') {
      msg = 'No outbound (bot response) entries yet.';
    } else if (dirFilter === 'inbound') {
      msg = 'No inbound entries match the current filter.';
    } else if (dirFilter === 'owner') {
      msg = 'No owner activity recorded yet.';
    } else {
      msg = 'No activity recorded yet. Send a message from a collaborator account to generate entries.';
    }
    tbody.innerHTML = `<tr><td colspan="5" style="color:var(--text-muted);text-align:center;padding:1rem">${msg}</td></tr>`;
    return;
  }
  const lastViewed = parseFloat(sessionStorage.getItem('activityLastViewed') || '0');
  tbody.innerHTML = entries.map(e => {
    const ts = e.timestamp ? new Date(e.timestamp * 1000).toLocaleString() : '—';
    const isNew = lastViewed > 0 && (e.timestamp || 0) > lastViewed;
    const rowStyle = e.is_owner ? 'background:rgba(99,255,160,0.05)' : (isNew ? 'background:rgba(99,210,255,0.06)' : '');
    const srcBadge = `<span class="badge badge-info">${_esc(e.source || '—')}</span>`;
    // User cell: show user_id + username + owner badge if applicable
    const ownerBadge = e.is_owner ? ' <span class="badge badge-success" style="font-size:9px">owner</span>' : '';
    const userCell = `<span style="font-size:11px;font-family:monospace">${_esc(e.user_id || '—')}</span><br><span style="font-size:11px;color:var(--text-muted)">${_esc(e.username || '')}</span>${ownerBadge}`;
    // Query/Response columns: support both paired_entries (query_preview/response_preview) and flat entries (message_preview + direction)
    let queryText, responseText;
    if ('query_preview' in e || 'response_preview' in e) {
      queryText = e.query_preview || '';
      responseText = e.response_preview || '';
    } else {
      queryText = e.direction === 'inbound' ? (e.message_preview || '') : '';
      responseText = e.direction === 'outbound' ? (e.message_preview || '') : '';
    }
    const queryCell = queryText
      ? `<span style="font-size:11px" title="${_esc(queryText)}">${_esc(queryText.length > 80 ? queryText.slice(0, 80) + '…' : queryText)}</span>`
      : '<span style="color:var(--text-muted);font-size:11px">—</span>';
    const responseCell = responseText
      ? `<span style="font-size:11px;color:var(--text-muted)" title="${_esc(responseText)}">${_esc(responseText.length > 80 ? responseText.slice(0, 80) + '…' : responseText)}</span>`
      : '<span style="color:var(--text-muted);font-size:11px">—</span>';
    return `<tr style="${rowStyle}">
      <td style="white-space:nowrap;font-size:11px">${isNew ? '<span style="color:var(--accent);font-weight:700">●</span> ' : ''}${_esc(ts)}</td>
      <td>${userCell}</td>
      <td style="max-width:260px;overflow:hidden">${queryCell}</td>
      <td style="max-width:260px;overflow:hidden">${responseCell}</td>
      <td>${srcBadge}</td>
    </tr>`;
  }).join('');
}

// CC-38: real add-collaborator modal instead of Telegram toast
window._showAddCollabForm = function() {
  const modal = document.getElementById('add-collab-modal');
  if (!modal) { _toast('Use /addcollab command in Telegram to add a collaborator', 'info'); return; }
  // reset fields
  ['ac-user-id', 'ac-display-name'].forEach(id => { const el = document.getElementById(id); if (el) el.value = ''; });
  const platEl = document.getElementById('ac-platform');
  if (platEl) platEl.value = 'telegram';
  modal.classList.add('open');
};

window._closeAddCollabModal = function() {
  const modal = document.getElementById('add-collab-modal');
  if (modal) modal.classList.remove('open');
};

window._submitAddCollab = async function() {
  const uid      = (document.getElementById('ac-user-id')?.value      || '').trim();
  const name     = (document.getElementById('ac-display-name')?.value || '').trim();
  const platform = document.getElementById('ac-platform')?.value      || 'telegram';
  if (!uid) { _toast('User ID is required', 'danger'); return; }
  const { ok, data } = await _post('/users/collaborator', { user_id: uid, display_name: name || uid, platform, role: 'collaborator' });
  if (ok) {
    _toast(`Collaborator ${name || uid} added`, 'success');
    window._closeAddCollabModal();
    _loadContributors();
  } else {
    _toast(`Failed: ${data?.message || data?.detail || 'unknown error'}`, 'danger');
  }
};
window._removeCollab = function(uid) {
  _confirm('Remove collaborator', `Remove user "${uid}" from all collaborator lists?`, async () => {
    const { data } = await _delete(`/users/${encodeURIComponent(uid)}/collaborator`);
    _toast(data?.ok ? 'User removed' : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
    _loadContributors();
  });
};

// ── Group management panel ──────────────────────────────────────────────────
let _gpCurrentId = null; // null = create mode, string = edit mode

window._openGroupPanel = function(group) {
  _gpCurrentId = group ? group.id : null;
  const isCreate = _gpCurrentId === null;

  _setText('group-panel-title', isCreate ? 'Create New Group' : `Manage: ${group.name}`);

  const idInput   = document.getElementById('gp-id');
  const nameInput = document.getElementById('gp-name');
  const modeEl    = document.getElementById('gp-mode');
  const adminInput = document.getElementById('gp-admin');

  if (idInput)    { idInput.value   = isCreate ? '' : group.id;    idInput.disabled = !isCreate; }
  if (nameInput)  { nameInput.value = isCreate ? '' : group.name;  /* CC-34: name always editable */ }
  if (modeEl)     { modeEl.value    = (group?.collab_mode) || 'local_only'; }
  if (adminInput) { adminInput.value = (group?.admin) || ''; }

  const createRow   = document.getElementById('gp-create-row');
  const membersSection = document.getElementById('gp-members-section');
  if (createRow)      createRow.style.display      = isCreate ? '' : 'none';
  if (membersSection) membersSection.style.display = isCreate ? 'none' : '';

  if (!isCreate) _renderGroupMembers(group.members || []);

  const panel = document.getElementById('group-panel');
  if (panel) { panel.style.display = ''; panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
};

window._closeGroupPanel = function() {
  const panel = document.getElementById('group-panel');
  if (panel) panel.style.display = 'none';
  _gpCurrentId = null;
};

function _renderGroupMembers(members) {
  const el = document.getElementById('gp-members-list');
  if (!el) return;
  if (!members.length) {
    el.innerHTML = '<div style="color:var(--text-muted);font-size:12px">No members — use "Add Member" below</div>';
    return;
  }
  // CC-39: show display names if available from cached users list
  const userMap = {};
  document.querySelectorAll('#users-tbody tr').forEach(row => {
    const code = row.querySelector('td:first-child code');
    const name = row.querySelector('td:nth-child(2) span');
    if (code && name) userMap[code.textContent] = name.textContent;
  });
  el.innerHTML = members.map(uid => {
    const displayName = userMap[uid] || uid;
    const showName = displayName !== uid ? ` <span style="color:var(--text-muted);font-size:10px">(${_esc(uid)})</span>` : '';
    return `<div style="display:flex;align-items:center;gap:.5rem;padding:.25rem 0;border-bottom:1px solid var(--border)">
      <span style="flex:1;font-size:12px">${_esc(displayName)}${showName}</span>
      <button class="btn btn-sm btn-danger" onclick="window._submitRemoveMember('${_esc(uid)}')">Remove</button>
    </div>`;
  }).join('');
}

window._submitCreateGroup = async function() {
  const group_id    = (document.getElementById('gp-id')?.value    || '').trim();
  const name        = (document.getElementById('gp-name')?.value  || '').trim();
  const collab_mode = document.getElementById('gp-mode')?.value   || 'local_only';
  const admin       = (document.getElementById('gp-admin')?.value || '').trim() || null;

  if (!group_id || !name) { _toast('Group ID and Name are required', 'danger'); return; }

  const { ok, data } = await _post('/groups', { group_id, name, collab_mode, members: [], admin });
  if (ok) {
    _toast(`Group "${name}" created`, 'success');
    _closeGroupPanel();
    _loadContributors();
  } else {
    _toast(`Failed: ${data?.message || data?.detail || 'unknown error'}`, 'danger');
  }
};

window._submitSaveMode = async function() {
  if (!_gpCurrentId) return;
  const collab_mode = document.getElementById('gp-mode')?.value || 'local_only';
  const newName     = (document.getElementById('gp-name')?.value || '').trim();

  const calls = [_put(`/groups/${encodeURIComponent(_gpCurrentId)}/mode`, { collab_mode })];
  // CC-34: save name if it changed
  if (newName) calls.push(_put(`/groups/${encodeURIComponent(_gpCurrentId)}/name`, { name: newName }));

  const results = await Promise.all(calls);
  const allOk = results.every(r => r.ok);
  if (allOk) {
    _toast('Group settings saved', 'success');
    _loadContributors();
  } else {
    const msg = results.find(r => !r.ok)?.data?.message || 'unknown error';
    _toast(`Failed: ${msg}`, 'danger');
  }
};

window._submitAddMember = async function() {
  if (!_gpCurrentId) return;
  const uid = (document.getElementById('gp-add-uid')?.value || '').trim();
  if (!uid) { _toast('Enter a user ID', 'danger'); return; }
  const { ok, data } = await _post(`/groups/${encodeURIComponent(_gpCurrentId)}/members`, { user_id: uid });
  if (ok) {
    _toast(`User ${uid} added to group`, 'success');
    document.getElementById('gp-add-uid').value = '';
    // Refresh members list from server
    const { data: g } = await _get(`/groups/${encodeURIComponent(_gpCurrentId)}`);
    if (g) _renderGroupMembers(g.members || []);
    _loadContributors();
  } else {
    _toast(`Failed: ${data?.message || 'unknown error'}`, 'danger');
  }
};

window._submitRemoveMember = async function(uid) {
  if (!_gpCurrentId) return;
  const { ok, data } = await _delete(`/groups/${encodeURIComponent(_gpCurrentId)}/members/${encodeURIComponent(uid)}`);
  if (ok) {
    _toast(`User ${uid} removed`, 'success');
    const { data: g } = await _get(`/groups/${encodeURIComponent(_gpCurrentId)}`);
    if (g) _renderGroupMembers(g.members || []);
    _loadContributors();
  } else {
    _toast(`Failed: ${data?.message || 'unknown error'}`, 'danger');
  }
};

window._submitDeleteGroup = function() {
  if (!_gpCurrentId) return;
  _confirm('Delete Group', `Permanently delete group "${_gpCurrentId}"? Members will be removed from the group.`, async () => {
    const { ok, data } = await _delete(`/groups/${encodeURIComponent(_gpCurrentId)}`);
    if (ok) {
      _toast(`Group "${_gpCurrentId}" deleted`, 'success');
      _closeGroupPanel();
      _loadContributors();
    } else {
      _toast(`Failed: ${data?.message || 'unknown error'}`, 'danger');
    }
  });
};

// ---------------------------------------------------------------------------
// Egress tab
// ---------------------------------------------------------------------------

async function _loadEgress() {
  const [pendingRes, rulesRes, histRes] = await Promise.all([
    _get('/egress/pending'),
    _get('/egress/rules'),
    _get('/egress/history?limit=50'),
  ]);
  _renderPendingEgress(pendingRes.data);
  _renderEgressRules(rulesRes.data);
  _renderEgressHistory(histRes.data);
  const cnt = document.getElementById('egress-count');
  if (cnt && Array.isArray(pendingRes.data)) cnt.textContent = pendingRes.data.length;
}

// CC-40: Decision history table
function _renderEgressHistory(history) {
  const tbody = document.getElementById('egress-history-tbody');
  if (!tbody) return;
  const list = Array.isArray(history) ? history : [];
  if (!list.length) {
    tbody.innerHTML = '<tr><td colspan="7" style="color:var(--text-muted);text-align:center;padding:1rem">No decision history yet</td></tr>';
    return;
  }
  const decCls = { approved: 'success', denied: 'danger', timed_out: 'muted', revoked: 'warning' };
  tbody.innerHTML = list.map(e =>
    `<tr>
      <td><code style="font-size:11px">${_esc(e.domain || '—')}</code></td>
      <td style="font-size:11px">${_esc(e.agent_id || '—')}</td>
      <td><span class="badge badge-${decCls[e.decision] || 'muted'}">${_esc(e.decision || '—')}</span></td>
      <td style="font-size:11px">${_esc(e.mode || '—')}</td>
      <td style="font-size:11px">${_esc(e.decided_by || 'system')}</td>
      <td style="font-size:11px">${_ago(e.decided_at ? new Date(e.decided_at * 1000).toISOString() : null)}</td>
      <td>
        ${e.decision === 'approved' && e.mode !== 'once'
          ? `<button class="btn btn-sm btn-danger" onclick="window._revokeEgressDecision('${_esc(e.id)}')">Revoke</button>`
          : '—'}
      </td>
    </tr>`
  ).join('');
}

window._revokeEgressDecision = async function(entryId) {
  _confirm('Revoke Approval', 'This will remove the active rule created by this approval. Future requests to this domain will require a new approval.', async () => {
    const { data } = await _post(`/egress/history/${encodeURIComponent(entryId)}/revoke`);
    _toast(data?.ok ? 'Approval revoked' : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
    _loadEgress();
  }, false);
};

function _renderPendingEgress(items) {
  const tbody = document.getElementById('egress-tbody');
  if (!tbody) return;
  if (!Array.isArray(items) || !items.length) {
    tbody.innerHTML = '<tr><td colspan="9" style="color:var(--text-muted);text-align:center;padding:1rem">No pending requests</td></tr>';
    return;
  }
  const now = Date.now();
  tbody.innerHTML = items.map(r =>
    `<tr>
      <td><code>${_esc((r.request_id || '').slice(0, 8))}</code></td>
      <td>${_esc(r.domain || '—')}</td>
      <td>${r.port || '—'}</td>
      <td>${_esc(r.agent_id || '—')}</td>
      <td>${_esc(r.tool_name || '—')}</td>
      <td>${_sevBadge(r.risk_level || 'medium')}</td>
      <td>${_ago(r.timestamp)}</td>
      <td id="egress-countdown-${_esc(r.request_id)}" style="font-size:11px;color:var(--warning)">—</td>
      <td>
        <div style="display:flex;gap:.25rem;flex-wrap:wrap">
          <select id="egress-mode-${_esc(r.request_id)}" style="font-size:11px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:3px">
            <option value="once">Allow Once</option>
            <option value="session">Allow Session</option>
            <option value="1h">Allow 1h</option>
            <option value="4h">Allow 4h</option>
            <option value="24h">Allow 24h</option>
            <option value="permanent">Allow Always</option>
          </select>
          <button class="btn btn-sm btn-success" onclick="window._egressApproveWithMode('${_esc(r.request_id)}')">Allow</button>
          <button class="btn btn-sm btn-danger"  onclick="window._egressDecide('deny','${_esc(r.request_id)}')">Deny</button>
        </div>
      </td>
    </tr>`
  ).join('');

  // CC-05: start countdown timers for each pending request
  items.forEach(r => {
    if (!r.timeout_at) return;
    const cdEl = document.getElementById(`egress-countdown-${r.request_id}`);
    if (!cdEl) return;
    const tick = () => {
      const remaining = Math.max(0, Math.round((new Date(r.timeout_at) - Date.now()) / 1000));
      if (!document.getElementById(`egress-countdown-${r.request_id}`)) return; // removed from DOM
      cdEl.textContent = remaining > 0 ? `${remaining}s` : 'expired';
      cdEl.style.color = remaining <= 30 ? 'var(--danger)' : 'var(--warning)';
      if (remaining > 0) setTimeout(tick, 1000);
    };
    tick();
  });
}

/// CC-06: approve egress with selected mode
window._egressApproveWithMode = async function(id) {
  const sel = document.getElementById(`egress-mode-${id}`);
  const mode = sel ? sel.value : 'once';
  const { data } = await _post(`/egress/${encodeURIComponent(id)}/approve`, { mode });
  _toast(data?.ok ? `Egress approved (${mode})` : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
  setTimeout(_loadEgress, 1000);
};

function _renderEgressRules(rules) {
  const el = document.getElementById('egress-rules');
  if (!el) return;
  const list = Array.isArray(rules) ? rules
    : [...(rules?.permanent_rules || []), ...(rules?.session_rules || [])];
  if (!list.length) {
    el.innerHTML = '<span style="color:var(--text-muted);font-size:12px">No active rules</span>';
    return;
  }
  // Group by source for visual separation
  const preloaded = list.filter(r => r.source === 'preloaded');
  const user      = list.filter(r => r.source !== 'preloaded');

  const renderRow = r => {
    const expiry = r.expires_at ? _ago(r.expires_at) : (r.mode === 'permanent' ? 'permanent' : '—');
    const badgeCls = r.action === 'deny' ? 'danger' : (r.mode === 'permanent' ? 'success' : 'info');
    const canRevoke = r.source !== 'preloaded' || r.action === 'deny';
    return `<tr>
      <td><code style="font-size:11px">${_esc(r.domain)}</code></td>
      <td><span class="badge badge-${badgeCls}">${_esc(r.action || 'allow')}</span></td>
      <td style="font-size:11px">${_esc(r.mode || '—')}</td>
      <td style="font-size:11px">${expiry}</td>
      <td style="font-size:11px;color:var(--text-muted)">${r.source === 'preloaded' ? 'pre-approved' : 'user'}</td>
      <td>
        ${r.action !== 'deny'
          ? `<button class="btn btn-sm btn-danger" title="Deny/pause this domain" onclick="window._egressOverride('${_esc(r.domain)}','deny')">Pause</button>`
          : `<button class="btn btn-sm" title="Remove override and restore default" onclick="window._egressRemoveOverride('${_esc(r.domain)}')">Restore</button>`}
      </td>
    </tr>`;
  };

  const preHtml = preloaded.length ? `
    <tr><td colspan="6" style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);padding:.5rem 0 .25rem;background:transparent">Pre-approved (${preloaded.length})</td></tr>
    ${preloaded.map(renderRow).join('')}` : '';

  const userHtml = user.length ? `
    <tr><td colspan="6" style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--text-muted);padding:.5rem 0 .25rem;background:transparent">User Rules (${user.length})</td></tr>
    ${user.map(renderRow).join('')}` : '';

  el.innerHTML = `
    <table class="data-table" style="font-size:11px">
      <thead><tr><th>Domain</th><th>Action</th><th>Mode</th><th>Expires</th><th>Source</th><th></th></tr></thead>
      <tbody>${preHtml}${userHtml}</tbody>
    </table>`;
}

// CC-10: pause/deny a permanent domain or restore it
window._egressOverride = async function(domain, action) {
  const { data } = await _post('/egress/rules/override', { domain, action });
  _toast(data?.ok ? `Domain ${action === 'deny' ? 'paused' : 'allowed'}` : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
  _loadEgress();
};

window._egressRemoveOverride = async function(domain) {
  const { data } = await _delete(`/egress/rules/${encodeURIComponent(domain)}`);
  _toast(data?.ok ? 'Override removed' : `Error: ${data?.message}`, data?.ok ? 'success' : 'danger');
  _loadEgress();
};

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

// CC-30/41: fetch REST logs on Logs tab load so viewer is pre-populated
async function _loadLogs() {
  const svcFilter = document.getElementById('log-service-filter')?.value || 'agentshroud-gateway';
  const el = document.getElementById('log-viewer');
  if (!el) return;
  el.textContent = 'Loading logs…';
  const { data } = await _get(`/services/${encodeURIComponent(svcFilter || 'agentshroud-gateway')}/logs?tail=300`);
  const lines = data?.lines || [];
  if (lines.length) {
    el.textContent = lines.join('\n');
  } else if (_eventFeed.length) {
    _replayLogsTab();
  } else {
    el.textContent = 'No log data available — waiting for events…';
  }
  el.scrollTop = el.scrollHeight;
}

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

function _replayLogsTab() {
  const el = document.getElementById('log-viewer');
  if (!el) return;
  if (!_eventFeed.length) {
    el.textContent = 'Waiting for events...';
    return;
  }
  const svc = document.getElementById('log-service-filter')?.value || '';
  const lines = _eventFeed
    .filter(ev => !svc || ev.service === svc)
    .map(ev => `[${_ts(ev.timestamp)}] [${(ev.severity || 'info').toUpperCase().padEnd(8)}] ${ev.summary || ev.type}`)
    .join('\n');
  el.textContent = lines || 'Waiting for events...';
  el.scrollTop = el.scrollHeight;
}

window._clearLogs = function() {
  const el = document.getElementById('log-viewer');
  if (el) el.textContent = 'Log cleared.';
};

// ---------------------------------------------------------------------------
// Config tab
// ---------------------------------------------------------------------------

async function _loadConfig() {
  // CC-44: structured config view instead of raw JSON dump
  const { data: cfg } = await _get('/config');
  const el = document.getElementById('config-view');
  if (el && cfg) {
    const rows = [
      { label: 'Bind Address', key: 'bind' },
      { label: 'Port', key: 'port' },
      { label: 'Teams Enabled', key: 'teams_enabled' },
      { label: 'Active Bots', key: 'bots' },
    ];
    el.innerHTML = `
      <table style="width:100%;border-collapse:collapse;font-size:12px">
        ${rows.map(r => {
          const val = cfg[r.key];
          const display = Array.isArray(val) ? val.join(', ') : (val !== undefined ? String(val) : '—');
          return `<tr>
            <td style="padding:.3rem .5rem;color:var(--text-muted);white-space:nowrap;border-bottom:1px solid var(--border)">${_esc(r.label)}</td>
            <td style="padding:.3rem .5rem;border-bottom:1px solid var(--border)">${_esc(display)}</td>
          </tr>`;
        }).join('')}
        <tr>
          <td style="padding:.3rem .5rem;color:var(--text-muted);border-bottom:1px solid var(--border)">Log Level</td>
          <td style="padding:.3rem .5rem;border-bottom:1px solid var(--border)">
            <select id="log-level-sel" style="font-size:11px;padding:2px 4px;background:var(--surface);color:var(--text);border:1px solid var(--border);border-radius:3px"
              onchange="window._setLogLevel(this.value)">
              ${['DEBUG','INFO','WARNING','ERROR'].map(lvl =>
                `<option value="${lvl}"${(cfg.log_level||'INFO')===lvl?' selected':''}>${lvl}</option>`
              ).join('')}
            </select>
          </td>
        </tr>
      </table>`;
  }

  // CC-42/43: module mode toggles + descriptions
  const { data: modules } = await _get('/security/modules').catch(() => ({ data: null }));
  const mEl = document.getElementById('modules-view');
  if (mEl && Array.isArray(modules)) {
    const modes = ['enforce', 'monitor', 'disabled'];
    const modeCls = { enforce: 'mode-enforce', monitor: 'mode-monitor', disabled: 'mode-disabled' };
    mEl.innerHTML = modules.map(m =>
      `<div style="margin-bottom:.75rem;padding:.5rem;border-radius:4px;background:var(--surface-alt, rgba(255,255,255,0.03));border:1px solid var(--border)">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <code style="color:var(--text);font-size:12px">${_esc(m.name)}</code>
            <span class="badge badge-${m.available ? 'success' : 'muted'}" style="margin-left:.5rem">${m.available ? 'loaded' : 'unavailable'}</span>
          </div>
          ${m.available
            ? `<select class="${modeCls[m.mode] || 'mode-enforce'}"
                style="font-size:11px;padding:2px 6px;border-radius:3px;border:1px solid var(--border)"
                onchange="window._setModuleMode('${_esc(m.name)}',this.value,this)">
                ${modes.map(md => `<option value="${md}"${m.mode===md?' selected':''}>${md}</option>`).join('')}
              </select>`
            : '<span style="font-size:11px;color:var(--text-muted)">unavailable</span>'}
        </div>
        ${m.description ? `<div style="font-size:11px;color:var(--text-muted);margin-top:.25rem">${_esc(m.description)}</div>` : ''}
      </div>`
    ).join('');
  }
}

// CC-44: log level change
window._setLogLevel = async function(level) {
  const { ok, data } = await _put('/config/log-level', { level });
  _toast(ok ? `Log level set to ${level}` : `Error: ${data?.message}`, ok ? 'success' : 'danger');
};

// CC-42: module mode toggle
window._setModuleMode = async function(name, mode, selectEl) {
  const { ok, data } = await _put(`/security/modules/${encodeURIComponent(name)}/mode`, { mode });
  if (ok) {
    const modeCls = { enforce: 'mode-enforce', monitor: 'mode-monitor', disabled: 'mode-disabled' };
    selectEl.className = modeCls[mode] || 'mode-enforce';
    _toast(`${name} → ${mode}`, 'success');
  } else {
    _toast(`Error: ${data?.message || 'failed'}`, 'danger');
  }
};

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

// ---------------------------------------------------------------------------
// Theme toggle
// ---------------------------------------------------------------------------

function _initTheme() {
  const btn = document.getElementById('theme-toggle');
  if (!btn) return;
  btn.textContent = document.documentElement.dataset.theme === 'light' ? '☀' : '🌙';
  btn.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
    document.documentElement.dataset.theme = next;
    localStorage.setItem('as_theme', next);
    btn.textContent = next === 'light' ? '☀' : '🌙';
  });
}

document.addEventListener('DOMContentLoaded', async () => {
  _initTheme();

  // If no stored token, or stored token is invalid → show login modal and wait
  const _needsAuth = async () => {
    if (!_token) return true;
    try {
      const chk = await fetch(`${SOC_BASE}/health`, { headers: { Authorization: `Bearer ${_token}` } });
      if (chk.status === 401) { localStorage.removeItem('soc_token'); _token = ''; return true; }
    } catch (_) {}
    return false;
  };
  if (await _needsAuth()) {
    await _showLoginModal();
  }

  // Register tab loaders
  _registerTab('overview',     _loadOverview);
// ---------------------------------------------------------------------------
// CVE Intelligence tab
// ---------------------------------------------------------------------------

const _SEV_ICON = { CRITICAL: '🔴', HIGH: '🟠', MEDIUM: '🟡', LOW: '🟢', UNKNOWN: '⚪' };
const _STATUS_BADGE = {
  fully_mitigated:    '<span style="background:#1a7f37;color:#fff;padding:2px 7px;border-radius:3px;font-size:10px;font-weight:600">✓ MITIGATED</span>',
  partially_mitigated:'<span style="background:#9a6700;color:#fff;padding:2px 7px;border-radius:3px;font-size:10px;font-weight:600">⚠ PARTIAL</span>',
  not_mitigated:      '<span style="background:#cf222e;color:#fff;padding:2px 7px;border-radius:3px;font-size:10px;font-weight:600">✗ OPEN</span>',
};

window._agentCveData = null;
window._trivyCveData = null;

async function _loadAgentCves() {
  const [agentRes, trivyRes] = await Promise.all([
    _get('/agent-cves'),
    _get('/trivy'),
  ]);

  // Agent CVEs
  if (agentRes.ok) {
    const d = agentRes.data;
    window._agentCveData = d;
    document.getElementById('cve-kpi-agent').textContent    = d.wrapped_agent || '--';
    document.getElementById('cve-kpi-total').textContent    = d.total_cves ?? '--';
    document.getElementById('cve-kpi-full').textContent     = d.by_status?.fully_mitigated ?? '--';
    const partial = (d.by_status?.partially_mitigated ?? 0) + (d.by_status?.not_mitigated ?? 0);
    document.getElementById('cve-kpi-partial').textContent  = partial;
    const agentHeader = document.getElementById('cve-agent-header');
    if (agentHeader) agentHeader.textContent = `${d.wrapped_agent} CVEs (${d.total_cves} tracked)`;
    _renderAgentCveTable(d);
  } else {
    document.getElementById('agent-cve-table').innerHTML =
      '<div style="padding:1rem;color:var(--danger);font-size:12px">Failed to load CVE registry.</div>';
  }

  // Container / Trivy CVEs
  if (trivyRes.ok) {
    const d = trivyRes.data;
    window._trivyCveData = d;
    document.getElementById('cve-kpi-container').textContent = d.findings ?? d.total_vulnerabilities ?? '--';
    _renderTrivyCveTable(d);
  } else {
    document.getElementById('trivy-cve-table').innerHTML =
      '<div style="padding:1rem;color:var(--text-muted);font-size:12px">No Trivy scan results. Run a scan above.</div>';
  }
}

function _renderAgentCveTable(data) {
  if (!data) return;
  const statusFilter = document.getElementById('cve-status-filter')?.value || '';
  const sevFilter    = document.getElementById('cve-sev-filter')?.value    || '';

  const rows = (data.cves || []).filter(c =>
    (!statusFilter || c.status === statusFilter) &&
    (!sevFilter    || c.severity === sevFilter)
  );

  if (!rows.length) {
    document.getElementById('agent-cve-table').innerHTML =
      '<div style="padding:1rem;color:var(--text-muted);font-size:12px">No CVEs match filters.</div>';
    return;
  }

  const thead = `<thead><tr>
    <th style="width:130px">CVE ID</th>
    <th style="width:60px">CVSS</th>
    <th style="width:80px">Severity</th>
    <th style="width:110px">Status</th>
    <th>Vulnerability</th>
    <th>AgentShroud Defense</th>
    <th style="width:90px">Fixed In</th>
  </tr></thead>`;

  const tbody = rows.map(c => {
    const icon = _SEV_ICON[c.severity] || '⚪';
    const badge = _STATUS_BADGE[c.status] || c.status;
    const layers = (c.defense_layers || []).map(l =>
      `<code style="background:var(--input-bg,#161b22);padding:1px 4px;border-radius:3px;font-size:10px;margin-right:3px">${l}</code>`
    ).join('');
    return `<tr>
      <td><code style="font-size:11px">${c.id}</code></td>
      <td style="text-align:center;font-weight:600">${c.cvss}</td>
      <td>${icon} ${c.severity}</td>
      <td>${badge}</td>
      <td>
        <div style="font-weight:600;font-size:11px;margin-bottom:2px">${c.title}</div>
        <div style="color:var(--text-muted);font-size:10px;line-height:1.4">${c.description}</div>
      </td>
      <td>
        <div style="color:var(--text-muted);font-size:10px;line-height:1.5;margin-bottom:4px">${c.mitigation}</div>
        <div>${layers}</div>
      </td>
      <td style="font-size:10px;color:var(--text-muted)">${c.fixed_in || '—'}</td>
    </tr>`;
  }).join('');

  document.getElementById('agent-cve-table').innerHTML =
    `<table class="data-table" style="font-size:11px">${thead}<tbody>${tbody}</tbody></table>`;
}

function _renderTrivyCveTable(data) {
  if (!data) return;
  const sevFilter = document.getElementById('trivy-sev-filter')?.value || '';
  const cves = (data.top_cves || []).filter(c => !sevFilter || c.severity === sevFilter);

  if (data.error) {
    document.getElementById('trivy-cve-table').innerHTML =
      `<div style="padding:1rem;color:var(--warning);font-size:12px">Trivy scan error: ${data.error}. Click "Run Scan" to retry.</div>`;
    return;
  }

  if (!cves.length) {
    const ts = data.timestamp ? ` (scan: ${data.timestamp?.slice(0,10)})` : '';
    document.getElementById('trivy-cve-table').innerHTML =
      `<div style="padding:1rem;color:var(--green);font-size:12px">✅ No vulnerabilities found${ts}.</div>`;
    return;
  }

  const bySev = data.by_severity || {};
  const summary = Object.entries(bySev).filter(([,v]) => v > 0)
    .map(([k,v]) => `${_SEV_ICON[k]||'⚪'} ${k}: <strong>${v}</strong>`).join('  ·  ');

  const thead = `<thead><tr>
    <th style="width:130px">CVE ID</th>
    <th style="width:80px">Severity</th>
    <th>Package</th>
    <th>Installed</th>
    <th>Fixed In</th>
    <th>Title</th>
    <th>Target</th>
  </tr></thead>`;

  const tbody = cves.map(c => {
    const icon = _SEV_ICON[c.severity] || '⚪';
    const fix = c.fixed_version
      ? `<span style="color:var(--green)">${c.fixed_version}</span>`
      : '<span style="color:var(--text-muted)">no fix</span>';
    return `<tr>
      <td><code style="font-size:11px">${c.id}</code></td>
      <td>${icon} ${c.severity}</td>
      <td><code style="font-size:11px">${c.package}</code></td>
      <td><code style="font-size:10px;color:var(--text-muted)">${c.installed_version}</code></td>
      <td><code style="font-size:10px">${fix}</code></td>
      <td style="font-size:10px;color:var(--text-muted)">${c.title}</td>
      <td style="font-size:10px;color:var(--text-muted)">${c.target}</td>
    </tr>`;
  }).join('');

  const ts = data.timestamp ? `<div style="font-size:10px;color:var(--text-muted);padding:0.5rem 1rem">Last scan: ${data.timestamp?.slice(0,19).replace('T',' ')} UTC · ${summary}</div>` : '';
  document.getElementById('trivy-cve-table').innerHTML =
    ts + `<table class="data-table" style="font-size:11px">${thead}<tbody>${tbody}</tbody></table>`;
}

window._triggerCveReport = async function() {
  const btn = document.querySelector('[onclick*="_triggerCveReport"]');
  if (btn) { btn.disabled = true; btn.textContent = '⏳ Scanning...'; }
  const res = await fetch(`${SOC_BASE}/cve-report`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${_token}`, 'Content-Type': 'application/json' },
  });
  if (btn) { btn.disabled = false; btn.textContent = '▶ Run Scan & Send Report'; }
  const data = await res.json().catch(() => ({}));
  if (data.status === 'queued') {
    setTimeout(() => _loadAgentCves(), 8000);  // reload after scan completes
  }
};


  _registerTab('security',     _loadSecurity);
  _registerTab('scanners',     _loadScanners);
  _registerTab('scorecard',    _loadScorecard);
  _registerTab('services',     _loadServices);
  _registerTab('contributors', _loadContributors);
  _registerTab('egress',       _loadEgress);
  _registerTab('logs',         _loadLogs);  // CC-30: fetch REST logs on tab open
  _registerTab('config',       _loadConfig);
  _registerTab('agent-cves',   _loadAgentCves);

  // Wire nav items
  document.querySelectorAll('.nav-item[data-tab]').forEach(el => {
    el.addEventListener('click', e => { e.preventDefault(); _showTab(el.dataset.tab); });
  });

  // CVE Intelligence filter change handlers
  const cveStatusFilter = document.getElementById('cve-status-filter');
  if (cveStatusFilter) cveStatusFilter.addEventListener('change', () => _renderAgentCveTable(window._agentCveData));
  const cveSevFilter = document.getElementById('cve-sev-filter');
  if (cveSevFilter) cveSevFilter.addEventListener('change', () => _renderAgentCveTable(window._agentCveData));
  const trivySevFilter = document.getElementById('trivy-sev-filter');
  if (trivySevFilter) trivySevFilter.addEventListener('change', () => _renderTrivyCveTable(window._trivyCveData));

  // Severity filter change handler
  const sevFilter = document.getElementById('sev-filter');
  if (sevFilter) sevFilter.addEventListener('change', () => _renderSecurityTable());

  // Log service filter — reload logs when changed
  const logSvcFilter = document.getElementById('log-service-filter');
  if (logSvcFilter) logSvcFilter.addEventListener('change', () => { if (_currentTab === 'logs') _loadLogs(); });

  // Show overview
  _showTab('overview');

  // Connect WebSocket
  if (_token) _connectWS();
  else _setWSStatus('disconnected');
});
