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
    echo "ERROR: no ws/lib/websocket.js found under $OPENCLAW_ROOT — wss:// traffic would bypass the gateway proxy." >&2
    echo "Vendor package layout may have changed; update patch-ws-proxy.sh." >&2
    exit 1
fi

# Iterate via a `for` loop (not `printf | while read`) so per-file failures are
# actually visible to `set -e`: a piped `while read` runs in a subshell under
# POSIX sh (dash), so a variable set inside the loop to record a failure is lost
# the instant the pipe closes — a failure on an earlier file could silently be
# masked by a later file succeeding. IFS is switched to newline-only so paths
# with spaces still split correctly on one file per line.
_FAILED=0
_OLD_IFS="$IFS"
IFS='
'
for WS_FILE in $WS_FILES; do
    IFS="$_OLD_IFS"
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
    console.error('ERROR: tlsConnect not found in ' + wsFile + ' — wss:// traffic would bypass the gateway proxy.');
    console.error('Vendor ws package version likely changed shape; update patch-ws-proxy.sh.');
    process.exit(1);
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
" "$WS_FILE" || _FAILED=1
    IFS='
'
done
IFS="$_OLD_IFS"

if [ "$_FAILED" -eq 1 ]; then
    echo "ERROR: ws proxy patch failed for one or more files (see above) — wss:// traffic would bypass the gateway proxy." >&2
    exit 1
fi

echo "ws proxy patch complete."
