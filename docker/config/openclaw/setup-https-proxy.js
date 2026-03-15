'use strict';
/**
 * setup-https-proxy.js
 *
 * Loaded via NODE_OPTIONS=--require before OpenClaw starts.
 * Replaces https.globalAgent with a minimal CONNECT-proxy-aware agent so that
 * ALL HTTPS traffic from this Node.js process (including @slack/bolt, @slack/web-api,
 * node-fetch v2, and the ws WebSocket library) routes through the CONNECT proxy at
 * HTTPS_PROXY instead of attempting direct connections to the internet.
 *
 * This is required because @slack/bolt uses its own HTTP client that does not
 * natively read HTTPS_PROXY from the environment.
 */

const http  = require('http');
const https = require('https');
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
