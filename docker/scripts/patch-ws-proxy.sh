#!/bin/sh
# patch-ws-proxy.sh — Patch ws/lib/websocket.js on disk to route wss:// through HTTPS_PROXY.
#
# ROOT CAUSE: openclaw uses Node.js Compile Cache (module.enableCompileCache).
# The cache persists compiled bytecode across restarts. Our runtime require.cache
# patch (setup-https-proxy.js) is never seen because Node loads ws from bytecode,
# not from source. The patched exports are never used.
#
# FIX: Modify ws/lib/websocket.js on disk. When the source changes, Node regenerates
# the compile cache from the new source. This works for ALL loaders: CJS require,
# ESM createRequire, and bundled __require. Same pattern as patch-telegram-sdk.sh.
#
# The patch wraps tlsConnect() to tunnel through an HTTP CONNECT proxy when
# HTTPS_PROXY is set. Falls back to direct tls.connect() when unset or host is
# in NO_PROXY — so the same image works on isolated (bot) and non-isolated networks.

set -e

OPENCLAW_ROOT="$(npm root -g)/openclaw"

# Find all copies of ws/lib/websocket.js under the openclaw tree
WS_FILES="$(find "$OPENCLAW_ROOT" -path '*/ws/lib/websocket.js' -type f 2>/dev/null || true)"

if [ -z "$WS_FILES" ]; then
    echo "WARNING: no ws/lib/websocket.js found under $OPENCLAW_ROOT — skipping ws proxy patch"
    exit 0
fi

printf '%s\n' "$WS_FILES" | while IFS= read -r WS_FILE; do
    node -e "
const fs = require('fs');
const wsFile = process.argv[1];
let src = fs.readFileSync(wsFile, 'utf8');

if (src.includes('AGENTSHROUD_WS_PROXY_PATCHED')) {
    console.log('Already patched: ' + wsFile);
    process.exit(0);
}

// Target: the tlsConnect function used by initAsClient for wss:// connections.
// We inject a proxy-aware version that tunnels through HTTPS_PROXY when set,
// using the same async callback pattern Node's http.Agent machinery expects.
// The original tls.connect() path is preserved as fallback.
const OLD = \`function tlsConnect(options) {
  options.path = undefined;

  if (!options.servername && options.servername !== '') {
    options.servername = net.isIP(options.host) ? '' : options.host;
  }

  return tls.connect(options);
}\`;

const NEW = \`function tlsConnect(options, callback) { // AGENTSHROUD_WS_PROXY_PATCHED
  options.path = undefined;

  if (!options.servername && options.servername !== '') {
    options.servername = net.isIP(options.host) ? '' : options.host;
  }

  var _proxyUrl = process.env.HTTPS_PROXY || process.env.https_proxy;
  if (_proxyUrl) {
    var _noProxy = (process.env.NO_PROXY || process.env.no_proxy || '')
      .split(',').map(function(h) { return h.trim().toLowerCase(); }).filter(Boolean);
    var _host = (options.host || '').toLowerCase();
    var _bypass = _host === 'localhost' || _host === '127.0.0.1' || _host === '::1'
      || _noProxy.indexOf(_host) !== -1
      || _noProxy.some(function(p) {
           return p.charAt(0) === '.' && (_host === p.slice(1) || _host.slice(-p.length) === p);
         });
    if (!_bypass) {
      try { var _pu = new URL(_proxyUrl); } catch (e) { /* fall through */ }
      if (_pu) {
        var _ph = _pu.hostname;
        var _pp = parseInt(_pu.port, 10) || 8181;
        var _port = parseInt(options.port, 10) || 443;
        var _connectReq = http.request({
          host: _ph, port: _pp, method: 'CONNECT',
          path: _host + ':' + _port,
          headers: { Host: _host + ':' + _port }
        });
        _connectReq.on('connect', function(res, socket) {
          if (res.statusCode !== 200) {
            socket.destroy();
            var err = new Error('CONNECT proxy rejected: ' + res.statusCode + ' for ' + _host + ':' + _port);
            if (typeof callback === 'function') callback(err); else socket.emit('error', err);
            return;
          }
          var tlsSock = tls.connect(Object.assign({}, options, {
            socket: socket,
            rejectUnauthorized: options.rejectUnauthorized !== false
          }), function() {
            if (typeof callback === 'function') callback(null, tlsSock);
          });
          tlsSock.on('error', function(e) {
            if (typeof callback === 'function') callback(e); else tlsSock.emit('error', e);
          });
        });
        _connectReq.on('error', function(e) {
          if (typeof callback === 'function') callback(e);
        });
        _connectReq.end();
        return; // async — callback delivers the socket
      }
    }
  }

  // No proxy or bypassed: direct TLS (original behaviour)
  var sock = tls.connect(options);
  if (typeof callback === 'function') {
    sock.once('secureConnect', function() { callback(null, sock); });
    sock.once('error', callback);
  }
  return sock;
}\`;

if (!src.includes('function tlsConnect(options)')) {
    console.log('WARNING: tlsConnect not found in ' + wsFile + ' — skipping (different ws version?)');
    process.exit(0);
}

src = src.replace(OLD, NEW);

if (!src.includes('AGENTSHROUD_WS_PROXY_PATCHED')) {
    // Exact whitespace mismatch — try a more tolerant replace
    src = fs.readFileSync(wsFile, 'utf8');
    // Find function body bounds
    var fnIdx = src.indexOf('function tlsConnect(options)');
    var braceIdx = src.indexOf('{', fnIdx);
    var depth = 0, endIdx = -1;
    for (var i = braceIdx; i < src.length; i++) {
        if (src[i] === '{') depth++;
        else if (src[i] === '}') { if (--depth === 0) { endIdx = i + 1; break; } }
    }
    if (endIdx < 0) {
        console.log('ERROR: could not locate tlsConnect body in ' + wsFile);
        process.exit(1);
    }
    src = src.slice(0, fnIdx) + NEW + src.slice(endIdx);
    if (!src.includes('AGENTSHROUD_WS_PROXY_PATCHED')) {
        console.log('ERROR: patch failed for ' + wsFile);
        process.exit(1);
    }
}

fs.writeFileSync(wsFile, src);
console.log('Patched: ' + wsFile);
" "$WS_FILE"
done

echo "ws proxy patch complete."
