---
title: mcp-proxy-wrapper.js
type: module
file_path: docker/scripts/mcp-proxy-wrapper.js
tags: [javascript, nodejs, mcp, proxy, security]
related: [Proxy Layer/mcp_proxy.py, Architecture Overview, Data Flow]
status: documented
---

# mcp-proxy-wrapper.js

**Location:** `docker/scripts/mcp-proxy-wrapper.js`
**Lines:** 293
**Runtime:** Node.js (inside bot container)
**Installed at:** `/usr/local/bin/mcp-proxy-wrapper.js`

## Purpose

Node.js stdio proxy that sits between OpenClaw and any MCP (Model Context Protocol) server subprocess. Every `tools/call` message is forwarded to the AgentShroud gateway for security inspection before reaching the actual MCP server. **Fail-closed**: if the gateway is unreachable, the tool call is BLOCKED — not passed through.

## How It Works

```
OpenClaw Agent
  → stdio (JSON-RPC)
  → mcp-proxy-wrapper.js
    → tools/call: POST http://gateway:8080/mcp/inspect
      → 200 OK: forward to MCP server subprocess
      → Non-200: return JSON-RPC error to OpenClaw
    → tool results: POST http://gateway:8080/mcp/result (fire-and-forget)
  → MCP Server subprocess (stdin/stdout pipe)
```

## Usage

```bash
node mcp-proxy-wrapper.js <server-name> -- <command> [args...]

# Example:
node mcp-proxy-wrapper.js mac-messages -- npx mac-messages-mcp
```

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `GATEWAY_URL` | `http://gateway:8080` | Gateway base URL |
| `GATEWAY_AUTH_TOKEN` | `''` | Bearer token for gateway auth |

## Key Behavior

### Fail-Closed Design

```javascript
// If gateway is unreachable or returns non-200:
// → Return JSON-RPC error to OpenClaw (tool call blocked)
// → NEVER pass-through unaudited tool calls
```

This is the critical security property: no tool call can bypass the gateway even if the gateway crashes or restarts.

### Message Types Intercepted

| Message Type | Action |
|-------------|--------|
| `tools/call` | Sent to gateway for inspection; blocked if non-200 |
| Tool results (responses) | Sent to gateway for PII audit (fire-and-forget) |
| All other messages | Passed through directly (no inspection) |

### Gateway Endpoints Called

| Endpoint | Method | When |
|----------|--------|------|
| `/mcp/inspect` | POST | Every `tools/call` |
| `/mcp/result` | POST | Every tool result (audit only) |

## Process Architecture

```
┌─────────────────┐
│  OpenClaw       │  stdin/stdout
│  Agent process  │ ←──────────────────┐
└─────────────────┘                    │
                                       │ JSON-RPC
┌─────────────────┐                    │
│  mcp-proxy-     │ ←──────────────────┘
│  wrapper.js     │
│  (this script)  │ ←──── HTTP POST → gateway:8080
└────────┬────────┘
         │ stdin/stdout (pipe)
         ▼
┌─────────────────┐
│  MCP Server     │
│  subprocess     │
└─────────────────┘
```

## Gateway Communication

```javascript
function gatewayPost(path, body) {
  // HTTP POST with Authorization: Bearer $GATEWAY_AUTH_TOKEN
  // Returns { status, body }
  // Throws on network error
}
```

## Fail-Closed Patch

A separate file `mcp-proxy-wrapper-fail-closed-patch.js` (29 lines) provides a minimal patch to ensure fail-closed behavior in edge cases.

## Related Notes

- [[Proxy Layer/mcp_proxy.py|mcp_proxy.py]] — Gateway-side MCP inspection handler
- [[Proxy Layer/mcp_permissions.py|mcp_permissions.py]] — Permission enforcement
- [[Environment Variables/GATEWAY_AUTH_TOKEN]] — Auth token
- [[Configuration/Dockerfile.bot]] — Where this script is installed
- [[Data Flow]] — Full request flow
