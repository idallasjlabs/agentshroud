'use strict';
// Suppress known transient unhandled rejections that occur during CONNECT proxy
// startup and Slack SocketModeClient WSS URL fetching. These are harmless network
// hiccups (gateway not yet ready, DNS transient, VPN reconnect) that should not
// crash the Node.js process. Unknown rejections are re-thrown so genuine bugs still
// surface as crashes (preserving fail-fast behavior for unexpected errors).
process.on('unhandledRejection', (reason, _promise) => {
  const msg = (reason && (reason.message || String(reason))) || '';
  const TRANSIENT = [
    'CONNECT proxy rejected',
    'ECONNREFUSED',
    'ENOTFOUND',
    'ETIMEDOUT',
    'ECONNRESET',
    'socket hang up',
  ];
  if (TRANSIENT.some((pat) => msg.includes(pat))) {
    // Transient proxy/DNS rejection — log at debug level and suppress
    if (process.env.NODE_DEBUG) {
      process.stderr.write(`[setup-https-proxy] transient rejection suppressed: ${msg}\n`);
    }
    return;
  }
  // Unknown rejection — re-throw so Node.js default crash behavior is preserved
  throw reason;
});

/**
 * setup-https-proxy.js
 *
 * Loaded via NODE_OPTIONS=--require before OpenClaw starts.
 * Routes ALL outbound HTTPS/WSS traffic through the CONNECT proxy at HTTPS_PROXY.
 *
 * Two layers of patching are needed:
 *
 * 1. https.globalAgent replacement (ConnectProxyAgent)
 *    Covers node-fetch v2, @slack/web-api REST calls, and any code that
 *    uses https.request without a custom createConnection.
 *
 * 2. ws WebSocket monkey-patch (patchWsForProxy)
 *    ws v8 sets opts.createConnection = tlsConnect (direct tls.connect) on
 *    every WebSocket, which takes priority over https.globalAgent in Node.js's
 *    agent machinery. We wrap the WebSocket class to inject a proxy-aware
 *    createConnection before ws can set tlsConnect, routing wss:// through
 *    the CONNECT proxy as well.
 */

const http  = require('http');
const https = require('https');
const net   = require('net');
const tls   = require('tls');

const PROXY = process.env.HTTPS_PROXY || process.env.https_proxy;
if (!PROXY) return;

let proxyHost, proxyPort;
try {
  const u = new URL(PROXY);
  proxyHost = u.hostname;
  proxyPort = parseInt(u.port, 10) || 8181;
} catch (e) {
  return;
}

// Domains that must NOT go through the proxy (loop-back and internal services)
const NO_PROXY_HOSTS = new Set(
  (process.env.NO_PROXY || process.env.no_proxy || '')
    .split(',')
    .map((h) => h.trim().toLowerCase())
    .filter(Boolean)
);

function shouldBypass(host) {
  const h = (host || '').toLowerCase();
  if (h === 'localhost' || h === '127.0.0.1' || h === '::1') return true;
  if (NO_PROXY_HOSTS.has(h)) return true;
  for (const pattern of NO_PROXY_HOSTS) {
    if (pattern.startsWith('.') && (h === pattern.slice(1) || h.endsWith(pattern))) return true;
  }
  return false;
}

class ConnectProxyAgent extends https.Agent {
  createConnection(options, callback) {
    const host = options.host || options.hostname || 'localhost';
    const port = options.port || 443;

    if (shouldBypass(host)) {
      // Fall back to default TLS connection for NO_PROXY hosts
      return super.createConnection(options, callback);
    }

    const req = http.request({
      host: proxyHost,
      port: proxyPort,
      method: 'CONNECT',
      path: `${host}:${port}`,
      headers: { Host: `${host}:${port}` },
    });

    req.on('connect', (res, socket) => {
      if (res.statusCode !== 200) {
        socket.destroy();
        callback(new Error(`CONNECT proxy rejected: ${res.statusCode} for ${host}:${port}`));
        return;
      }
      const tlsSocket = tls.connect(
        {
          socket,
          host,
          servername: options.servername || host,
          rejectUnauthorized: options.rejectUnauthorized !== false,
        },
        () => callback(null, tlsSocket)
      );
      tlsSocket.on('error', callback);
    });

    req.on('error', callback);
    req.end();
  }
}

https.globalAgent = new ConnectProxyAgent({ keepAlive: true });

// ── ws WebSocket proxy patch ───────────────────────────────────────────────
// ws v8 sets opts.createConnection = tlsConnect (direct tls.connect) in
// initAsClient, which takes priority over https.globalAgent in Node.js's
// agent.createSocket machinery. The ConnectProxyAgent above is therefore
// never reached for wss:// connections.
//
// Fix: wrap the WebSocket class so every new instance gets a proxy-aware
// createConnection injected before initAsClient can install tlsConnect.
(function patchWsForProxy() {
  // Resolve 'ws' dynamically: check openclaw's own node_modules first, then
  // fall back to global paths.  Avoids hard-coding a version-specific path.
  let WS_PATH;
  const _WS_SEARCH = [
    '/usr/local/lib/node_modules/openclaw/node_modules',
    '/usr/local/lib/node_modules/openclaw',
  ].concat((require.resolve.paths && require.resolve.paths('ws')) || []);
  for (const searchDir of _WS_SEARCH) {
    try {
      WS_PATH = require.resolve('ws', { paths: [searchDir] });
      break;
    } catch (_) { /* try next */ }
  }
  if (!WS_PATH) return; // ws not found — skip

  let wsExports;
  try {
    wsExports = require(WS_PATH);
  } catch (e) {
    return; // ws not loadable — skip
  }

  const OrigWebSocket = wsExports.WebSocket || wsExports;
  if (!OrigWebSocket || typeof OrigWebSocket !== 'function') return;

  // createConnection(options, callback) — called by Node.js HTTP agent machinery.
  // For bypass hosts: direct TLS (same as ws's built-in tlsConnect).
  // For all others: HTTP CONNECT tunnel through the gateway proxy, then TLS.
  function proxyCreateConnection(options, callback) {
    const host    = options.host || options.hostname || 'localhost';
    const port    = parseInt(options.port, 10) || 443;

    // Mirror ws tlsConnect: fix servername for SNI and clear path
    if (!options.servername && options.servername !== '') {
      options.servername = net.isIP(host) ? '' : host;
    }
    options.path = undefined;

    if (shouldBypass(host)) {
      // Direct TLS — identical to ws's default tlsConnect
      return tls.connect(options);
    }

    // Async HTTP CONNECT tunnel — no return value; callback called when ready
    const connectReq = http.request({
      host:    proxyHost,
      port:    proxyPort,
      method:  'CONNECT',
      path:    `${host}:${port}`,
      headers: { Host: `${host}:${port}` },
    });

    connectReq.on('connect', (res, socket) => {
      if (res.statusCode !== 200) {
        socket.destroy();
        callback(new Error(`Proxy CONNECT rejected: ${res.statusCode} for ${host}:${port}`));
        return;
      }
      const tlsOpts = {
        ...options,
        socket,
        rejectUnauthorized: options.rejectUnauthorized !== false,
      };
      const tlsSocket = tls.connect(tlsOpts, () => callback(null, tlsSocket));
      tlsSocket.on('error', callback);
    });

    connectReq.on('error', callback);
    connectReq.end();
    // Intentionally no return value — callback called asynchronously above
  }

  class PatchedWebSocket extends OrigWebSocket {
    constructor(url, protocolsOrOptions, options) {
      let protocols = protocolsOrOptions;
      let opts      = options;

      // Normalize (url, opts) call form — same detection logic as ws internals
      if (
        protocols !== undefined &&
        !Array.isArray(protocols) &&
        typeof protocols === 'object' &&
        opts === undefined
      ) {
        opts      = protocols;
        protocols = undefined;
      }

      // Inject proxyCreateConnection before ws's initAsClient sets tlsConnect
      if (!opts) opts = {};
      if (!opts.createConnection) {
        opts = { ...opts, createConnection: proxyCreateConnection };
      }

      if (protocols !== undefined) {
        super(url, protocols, opts);
      } else {
        super(url, opts);
      }
    }
  }

  // PatchedWebSocket extends OrigWebSocket — static constants (CONNECTING=0, OPEN=1,
  // CLOSING=2, CLOSED=3) are already accessible via prototype chain inheritance.
  // Only override the .WebSocket self-reference so require('ws').WebSocket returns
  // PatchedWebSocket (mirrors the self-reference set in ws/index.js).
  PatchedWebSocket.WebSocket = PatchedWebSocket;

  // Replace in the require cache so all subsequent require('ws') calls —
  // including @slack/socket-mode — receive PatchedWebSocket.
  const resolved = require.resolve(WS_PATH);
  const cached   = require.cache[resolved];
  if (cached) {
    cached.exports             = PatchedWebSocket;
    PatchedWebSocket.WebSocket = PatchedWebSocket;
  }
}());
