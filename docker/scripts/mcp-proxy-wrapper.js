#!/usr/bin/env node
// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
// Protected by common law trademark rights. Federal trademark registration pending.
// Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
/**
 * mcp-proxy-wrapper.js — Transparent MCP stdio proxy with AgentShroud gateway inspection.
 *
 * Sits between OpenClaw and the actual MCP server subprocess. Every tools/call
 * is sent to the AgentShroud gateway for security inspection before reaching
 * the real MCP server. Blocked calls are rejected with a JSON-RPC error.
 * Tool results are submitted to the gateway for outbound PII audit (fire-and-forget).
 *
 * Usage:
 *   node mcp-proxy-wrapper.js <server-name> -- <command> [args...]
 *
 * Env vars:
 *   GATEWAY_URL          Gateway base URL (default: http://gateway:8080)
 *   GATEWAY_AUTH_TOKEN   Bearer token for gateway auth (required in production)
 *
 * Fail-open: if the gateway is unreachable, the tool call is forwarded with a
 * warning logged to stderr. This preserves OpenClaw functionality during gateway
 * maintenance, at the cost of unaudited calls.
 */

'use strict';

const http = require('http');
const https = require('https');
const { spawn } = require('child_process');
const readline = require('readline');

// ── Config ────────────────────────────────────────────────────────────────────

const GATEWAY_URL = process.env.GATEWAY_URL || 'http://gateway:8080';
const AUTH_TOKEN = process.env.GATEWAY_AUTH_TOKEN || '';
const AGENT_ID = 'openclaw-bot';

// ── Arg parsing ───────────────────────────────────────────────────────────────

const dashDash = process.argv.indexOf('--');
if (dashDash === -1 || dashDash < 3) {
  process.stderr.write(
    'Usage: mcp-proxy-wrapper.js <server-name> -- <command> [args...]\n'
  );
  process.exit(1);
}

const serverName = process.argv[2];
const [command, ...commandArgs] = process.argv.slice(dashDash + 1);

if (!command) {
  process.stderr.write('[mcp-proxy] No command provided after --\n');
  process.exit(1);
}

// ── Start MCP server subprocess ───────────────────────────────────────────────

const child = spawn(command, commandArgs, {
  stdio: ['pipe', 'pipe', 'inherit'],
  env: process.env,
});

child.on('exit', (code) => {
  process.exit(code || 0);
});

child.on('error', (err) => {
  process.stderr.write(`[mcp-proxy] Failed to start MCP server: ${err.message}\n`);
  process.exit(1);
});

// ── Gateway HTTP helper ───────────────────────────────────────────────────────

/**
 * POST JSON body to a gateway endpoint.
 * Returns { status, body } or throws on network error.
 */
function gatewayPost(path, body) {
  return new Promise((resolve, reject) => {
    const url = new URL(path, GATEWAY_URL);
    const data = JSON.stringify(body);
    const isHttps = url.protocol === 'https:';
    const lib = isHttps ? https : http;

    const req = lib.request(
      {
        hostname: url.hostname,
        port: url.port || (isHttps ? 443 : 80),
        path: url.pathname + (url.search || ''),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(data),
          Authorization: `Bearer ${AUTH_TOKEN}`,
        },
        timeout: 10000,
      },
      (res) => {
        let raw = '';
        res.on('data', (chunk) => { raw += chunk; });
        res.on('end', () => {
          try {
            resolve({ status: res.statusCode, body: JSON.parse(raw) });
          } catch {
            resolve({ status: res.statusCode, body: raw });
          }
        });
      }
    );

    req.on('error', reject);
    req.on('timeout', () => {
      req.destroy();
      reject(new Error('Gateway request timed out'));
    });
    req.write(data);
    req.end();
  });
}

// ── Call inspection ───────────────────────────────────────────────────────────

/**
 * Submit a tools/call to the gateway for inspection.
 *
 * Returns:
 *   - null  → forward to the actual MCP server (msg may have sanitized params)
 *   - object → JSON-RPC error response to return to OpenClaw (call is blocked)
 *
 * Mutates msg.params.arguments if gateway provides sanitized params.
 */
async function inspectCall(msg) {
  const params = msg.params || {};
  const toolName = params.name || '';
  const toolArgs = params.arguments || {};

  let gatewayResult;
  try {
    gatewayResult = await gatewayPost('/mcp/proxy', {
      server_name: serverName,
      tool_name: toolName,
      parameters: toolArgs,
      agent_id: AGENT_ID,
    });
  } catch (err) {
    // Gateway unreachable — fail open, log, forward as-is
    process.stderr.write(
      `[mcp-proxy] Gateway unreachable (${err.message}) — forwarding ${toolName} without inspection\n`
    );
    return null;
  }

  if (gatewayResult.status === 403) {
    const reason =
      (gatewayResult.body && gatewayResult.body.detail) ||
      'Blocked by AgentShroud security gateway';
    process.stderr.write(
      `[mcp-proxy] BLOCKED: ${serverName}/${toolName} — ${reason}\n`
    );
    return {
      jsonrpc: '2.0',
      id: msg.id,
      error: { code: -32600, message: `Blocked by AgentShroud: ${reason}` },
    };
  }

  if (gatewayResult.status !== 200) {
    process.stderr.write(
      `[mcp-proxy] Gateway returned ${gatewayResult.status} for ${toolName} — forwarding anyway\n`
    );
    return null;
  }

  // Replace arguments with gateway-sanitized version (PII redacted)
  const sanitized = gatewayResult.body && gatewayResult.body.sanitized_params;
  if (sanitized && typeof sanitized === 'object') {
    msg = { ...msg, params: { ...params, arguments: sanitized } };
  }

  return null; // null = forward msg (possibly with sanitized params)
}

// ── Result audit ──────────────────────────────────────────────────────────────

/**
 * Submit a tool result to the gateway for outbound PII audit.
 * Fire-and-forget — does not block the response to OpenClaw.
 */
function auditResult(callId, toolName, content) {
  gatewayPost('/mcp/result', {
    server_name: serverName,
    tool_name: toolName,
    call_id: String(callId || ''),
    content: content,
    agent_id: AGENT_ID,
  }).catch((err) => {
    process.stderr.write(
      `[mcp-proxy] Could not submit result to gateway: ${err.message}\n`
    );
  });
}

// ── Message routing ───────────────────────────────────────────────────────────

// Track pending tools/call IDs so we can correlate results for audit
const pendingCalls = new Map(); // id → { toolName }

// Modified message buffer for calls where we swap in sanitized params
let pendingForward = null;

// Inbound from OpenClaw → wrapper stdin
const inboundRl = readline.createInterface({ input: process.stdin });

inboundRl.on('line', async (line) => {
  if (!line.trim()) return;

  let msg;
  try {
    msg = JSON.parse(line);
  } catch {
    // Non-JSON (e.g. debug output) — pass through verbatim
    child.stdin.write(line + '\n');
    return;
  }

  if (msg.method === 'tools/call') {
    // Track call ID for result correlation
    const toolName = (msg.params && msg.params.name) || '';
    pendingCalls.set(msg.id, { toolName });

    const blockResponse = await inspectCall(msg);

    if (blockResponse) {
      // Blocked — return error directly to OpenClaw, never touch subprocess
      process.stdout.write(JSON.stringify(blockResponse) + '\n');
      pendingCalls.delete(msg.id);
    } else {
      // Forward (msg may have sanitized params applied by inspectCall)
      child.stdin.write(JSON.stringify(msg) + '\n');
    }
  } else {
    // All other MCP protocol messages (initialize, tools/list, etc.) pass through unchanged
    child.stdin.write(JSON.stringify(msg) + '\n');
  }
});

inboundRl.on('close', () => {
  child.stdin.end();
});

// Outbound from subprocess → wrapper stdout → OpenClaw
const outboundRl = readline.createInterface({ input: child.stdout });

outboundRl.on('line', (line) => {
  if (!line.trim()) {
    process.stdout.write('\n');
    return;
  }

  let msg;
  try {
    msg = JSON.parse(line);
  } catch {
    process.stdout.write(line + '\n');
    return;
  }

  // If this is a JSON-RPC response (has id, no method), check if it correlates
  // to a pending tools/call and submit the result to the gateway for audit
  if (msg.id !== undefined && !msg.method) {
    const pending = pendingCalls.get(msg.id);
    if (pending) {
      pendingCalls.delete(msg.id);
      auditResult(msg.id, pending.toolName, msg.result !== undefined ? msg.result : msg.error);
    }
  }

  process.stdout.write(JSON.stringify(msg) + '\n');
});
