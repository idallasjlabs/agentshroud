---
title: mcp_proxy.py
type: module
file_path: gateway/proxy/mcp_proxy.py
tags: [proxy, mcp, tool-calls, security, permissions, audit, approval-queue]
related: [[mcp_permissions.py]], [[mcp_inspector.py]], [[mcp_audit.py]], [[mcp_config.py]]
status: documented
---

# mcp_proxy.py

## Purpose
Transparent security proxy for Model Context Protocol (MCP) tool calls. Intercepts all `tool_use` requests between an AI agent and MCP servers, routes them through permission checks and parameter inspection, optionally executes them, and audits every call in a cryptographic hash chain.

## Responsibilities
- Provide a transparent default-allow proxy for MCP tool calls
- Enforce agent-level permission checks before forwarding tool calls
- Inspect tool call parameters for prompt injection and PII leaks
- Inspect tool results for PII before returning them to the agent
- Manage stdio and HTTP/SSE connections to MCP servers via a connection pool
- Integrate with `EnhancedApprovalQueue` for human-in-the-loop gating
- Log all calls and results to `MCPAuditTrail`
- Support passthrough (debug) mode that logs everything but blocks nothing

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `MCPToolCall` | Dataclass | Represents an outgoing MCP tool_use request with agent_id, server, tool name, and parameters |
| `MCPToolResult` | Dataclass | Represents a result returned from an MCP server |
| `ProxyResult` | Dataclass | Full outcome of proxy processing: allowed/blocked flags, sanitized params/result, audit info |
| `StdioConnection` | Class | Manages a stdio subprocess connection to an MCP server process; JSON-RPC over stdin/stdout |
| `HttpSseConnection` | Class | Manages an HTTP/SSE connection to an MCP server using aiohttp |
| `ConnectionPool` | Class | Lazy-initializing pool of server connections keyed by server name |
| `MCPProxy` | Class | Main proxy orchestrating security pipeline for MCP tool calls |

## Function Details

### MCPProxy.process_tool_call(tool_call, execute)
**Purpose:** Run a tool call through the full security pipeline: approval check → permission check → parameter inspection → optional execution → result inspection → audit.
**Parameters:** `tool_call` (MCPToolCall); `execute` (bool) — if True, actually forward to the MCP server.
**Returns:** `ProxyResult`. Blocks on approval denial, permission failure, or HIGH injection finding.

### MCPProxy.process_tool_result(tool_result, agent_id)
**Purpose:** Inspect an externally-executed tool result for PII before returning it to the agent. Results are never blocked, only redacted.
**Parameters:** `tool_result` (MCPToolResult); `agent_id` (str).
**Returns:** `ProxyResult` with `sanitized_result` (PII redacted).

### MCPProxy.check_approval_required(tool_call)
**Purpose:** Submit a tool call to the `EnhancedApprovalQueue` and block until a human approves or denies it.
**Parameters:** `tool_call` (MCPToolCall).
**Returns:** `(bool, Optional[str])` — (approved, denial_reason).

### MCPProxy._execute_tool_call(tool_call, sanitized_params)
**Purpose:** Forward a vetted tool call to the appropriate MCP server via the connection pool.
**Parameters:** `tool_call` (MCPToolCall); `sanitized_params` (dict) — PII-scrubbed version of parameters.
**Returns:** `MCPToolResult`. Returns error result on timeout or unknown server.

### MCPProxy.get_stats()
**Purpose:** Return cumulative proxy metrics.
**Returns:** Dict with total/allowed/blocked/error counts, average latency, audit trail size, and chain validity.

### ConnectionPool.get_or_create(server_name, config)
**Purpose:** Return an existing connection or instantiate a new stdio or HTTP/SSE connection based on transport type.
**Returns:** `StdioConnection` or `HttpSseConnection`.

### StdioConnection.send_request(method, params)
**Purpose:** Send a JSON-RPC 2.0 request to the MCP server process over stdin and read the response from stdout.
**Parameters:** `method` (str), `params` (dict).
**Returns:** Parsed JSON dict response. Raises `asyncio.TimeoutError` on timeout.

## Configuration / Environment Variables
- Configuration sourced from `MCPProxyConfig` (see [[mcp_config.py]])
- `passthrough` (bool) — bypass all security checks; audit-log only
- Approval queue configured via `EnhancedApprovalQueue`

## Related
- [[Architecture Overview]]
- [[Data Flow]]
- [[mcp_permissions.py]]
- [[mcp_inspector.py]]
- [[mcp_audit.py]]
- [[mcp_config.py]]
- [[pipeline.py]]
