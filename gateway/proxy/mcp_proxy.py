"""MCP Proxy — transparent security layer for MCP tool calls.

Intercepts all MCP tool_use requests and responses, routes them through
the security pipeline, and forwards to the actual MCP server.

Design: transparent drop-in. Default-allow. Log everything, block only clear threats.
Supports stdio and HTTP/SSE transports with connection pooling.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional

from .mcp_audit import MCPAuditTrail
from .mcp_config import MCPProxyConfig, MCPServerConfig, MCPTransport
from .mcp_inspector import MCPInspector, ThreatLevel
from .mcp_permissions import MCPPermissionManager

logger = logging.getLogger("secureclaw.proxy.mcp_proxy")


@dataclass
class MCPToolCall:
    """Represents an MCP tool_use request."""
    id: str
    server_name: str
    tool_name: str
    parameters: dict[str, Any]
    agent_id: str = "default"
    timestamp: float = 0.0

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = time.time()
        if not self.id:
            self.id = str(uuid.uuid4())


@dataclass
class MCPToolResult:
    """Represents an MCP tool result."""
    call_id: str
    server_name: str
    tool_name: str
    content: Any = None
    is_error: bool = False
    error_message: str = ""
    timestamp: float = 0.0

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = time.time()


@dataclass
class ProxyResult:
    """Result of proxying an MCP tool call."""
    allowed: bool = True
    blocked: bool = False
    block_reason: str = ""
    call_id: str = ""
    # Sanitized versions
    sanitized_params: Optional[dict[str, Any]] = None
    sanitized_result: Optional[Any] = None
    # The actual result from the MCP server (after sanitization)
    tool_result: Optional[MCPToolResult] = None
    # Audit info
    audit_entry_id: str = ""
    findings_count: int = 0
    threat_level: str = "none"
    processing_time_ms: float = 0.0
    passthrough: bool = False  # True if bypass mode


class StdioConnection:
    """Manages a stdio connection to an MCP server process."""

    def __init__(self, config: MCPServerConfig):
        self.config = config
        self.process: Optional[asyncio.subprocess.Process] = None
        self._lock = asyncio.Lock()
        self._request_id = 0

    async def start(self) -> None:
        """Start the MCP server process."""
        if self.process and self.process.returncode is None:
            return
        env = None
        if self.config.env:
            import os
            env = {**os.environ, **self.config.env}
        self.process = await asyncio.create_subprocess_exec(
            self.config.command, *self.config.args,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

    async def send_request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        """Send a JSON-RPC request and read the response."""
        if not self.process or self.process.returncode is not None:
            await self.start()

        async with self._lock:
            self._request_id += 1
            request = {
                "jsonrpc": "2.0",
                "id": self._request_id,
                "method": method,
                "params": params,
            }
            data = json.dumps(request) + "\n"
            self.process.stdin.write(data.encode())
            await self.process.stdin.drain()

            # Read response line
            line = await asyncio.wait_for(
                self.process.stdout.readline(),
                timeout=self.config.timeout_seconds,
            )
            return json.loads(line.decode())

    async def stop(self) -> None:
        """Stop the MCP server process."""
        if self.process and self.process.returncode is None:
            self.process.terminate()
            try:
                await asyncio.wait_for(self.process.wait(), timeout=5)
            except asyncio.TimeoutError:
                self.process.kill()
            self.process = None

    @property
    def is_running(self) -> bool:
        return self.process is not None and self.process.returncode is None


class HttpSseConnection:
    """Manages an HTTP/SSE connection to an MCP server."""

    def __init__(self, config: MCPServerConfig):
        self.config = config
        self._session = None

    async def send_request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        """Send an HTTP request to the MCP server."""
        # We use aiohttp if available, but keep it optional
        try:
            import aiohttp
        except ImportError:
            raise RuntimeError("aiohttp required for HTTP/SSE transport. Install with: pip install aiohttp")

        if not self._session:
            self._session = aiohttp.ClientSession()

        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": method,
            "params": params,
        }

        async with self._session.post(
            self.config.url,
            json=request,
            timeout=aiohttp.ClientTimeout(total=self.config.timeout_seconds),
        ) as resp:
            return await resp.json()

    async def stop(self) -> None:
        if self._session:
            await self._session.close()
            self._session = None


class ConnectionPool:
    """Pool of connections to MCP servers."""

    def __init__(self):
        self._connections: dict[str, StdioConnection | HttpSseConnection] = {}

    def get_or_create(self, server_name: str, config: MCPServerConfig) -> StdioConnection | HttpSseConnection:
        """Get existing connection or create a new one."""
        if server_name not in self._connections:
            if config.transport == MCPTransport.STDIO:
                self._connections[server_name] = StdioConnection(config)
            else:
                self._connections[server_name] = HttpSseConnection(config)
        return self._connections[server_name]

    async def stop_all(self) -> None:
        for conn in self._connections.values():
            await conn.stop()
        self._connections.clear()

    def remove(self, server_name: str) -> None:
        self._connections.pop(server_name, None)


class MCPProxy:
    """Main MCP proxy that intercepts tool calls and routes through security.
    
    Transparent by default: all calls pass through unless a clear threat is detected.
    """

    def __init__(
        self,
        config: Optional[MCPProxyConfig] = None,
        permission_manager: Optional[MCPPermissionManager] = None,
        inspector: Optional[MCPInspector] = None,
        audit_trail: Optional[MCPAuditTrail] = None,
        passthrough: bool = False,
    ):
        self.config = config or MCPProxyConfig()
        self.permissions = permission_manager or MCPPermissionManager(self.config)
        self.inspector = inspector or MCPInspector()
        self.audit = audit_trail or MCPAuditTrail()
        self.pool = ConnectionPool()
        self.passthrough = passthrough  # Bypass mode for debugging
        self._stats = {
            "total_calls": 0,
            "allowed": 0,
            "blocked": 0,
            "errors": 0,
            "total_duration_ms": 0.0,
        }

    async def process_tool_call(
        self,
        tool_call: MCPToolCall,
        execute: bool = False,
    ) -> ProxyResult:
        """Process an MCP tool call through the security pipeline.
        
        Args:
            tool_call: The tool call to process.
            execute: If True, actually forward to the MCP server. If False, just inspect.
        
        Returns:
            ProxyResult with security findings and optionally the tool result.
        """
        start = time.time()
        self._stats["total_calls"] += 1

        # Passthrough mode — log minimal, allow everything
        if self.passthrough:
            entry = self.audit.log_tool_call(
                agent_id=tool_call.agent_id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                parameters=tool_call.parameters,
                call_id=tool_call.id,
            )
            self._stats["allowed"] += 1
            result = ProxyResult(
                allowed=True,
                call_id=tool_call.id,
                sanitized_params=tool_call.parameters,
                audit_entry_id=entry.id,
                passthrough=True,
                processing_time_ms=(time.time() - start) * 1000,
            )
            if execute:
                tool_result = await self._execute_tool_call(tool_call)
                result.tool_result = tool_result
                self.audit.log_tool_result(
                    call_id=tool_call.id,
                    agent_id=tool_call.agent_id,
                    server_name=tool_call.server_name,
                    tool_name=tool_call.tool_name,
                    success=not tool_result.is_error,
                    error_message=tool_result.error_message,
                    result_summary=str(tool_result.content)[:200] if tool_result.content else "",
                )
            return result

        # === Security Pipeline ===

        # 1. Permission check
        perm_result = self.permissions.check_all(
            tool_call.agent_id, tool_call.server_name, tool_call.tool_name
        )
        if not perm_result.allowed:
            self._stats["blocked"] += 1
            entry = self.audit.log_tool_call(
                agent_id=tool_call.agent_id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                parameters=tool_call.parameters,
                blocked=True,
                block_reason=perm_result.reason,
                call_id=tool_call.id,
            )
            return ProxyResult(
                allowed=False,
                blocked=True,
                block_reason=perm_result.reason,
                call_id=tool_call.id,
                audit_entry_id=entry.id,
                processing_time_ms=(time.time() - start) * 1000,
            )

        # 2. Inspect tool call parameters
        inspection = self.inspector.inspect_tool_call(
            tool_call.tool_name,
            tool_call.parameters,
            check_injection=self.config.injection_scan_enabled,
            check_pii=self.config.pii_scan_enabled,
        )

        if inspection.blocked:
            self._stats["blocked"] += 1
            entry = self.audit.log_tool_call(
                agent_id=tool_call.agent_id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                parameters=inspection.sanitized_params or tool_call.parameters,
                findings_count=len(inspection.findings),
                threat_level=inspection.threat_level.value,
                blocked=True,
                block_reason=inspection.block_reason,
                pii_redacted=any(f.finding_type.value == "pii_leak" for f in inspection.findings),
                call_id=tool_call.id,
            )
            return ProxyResult(
                allowed=False,
                blocked=True,
                block_reason=inspection.block_reason,
                call_id=tool_call.id,
                sanitized_params=inspection.sanitized_params,
                findings_count=len(inspection.findings),
                threat_level=inspection.threat_level.value,
                audit_entry_id=entry.id,
                processing_time_ms=(time.time() - start) * 1000,
            )

        # 3. Log allowed call
        self._stats["allowed"] += 1
        pii_redacted = any(f.finding_type.value == "pii_leak" for f in inspection.findings)
        entry = self.audit.log_tool_call(
            agent_id=tool_call.agent_id,
            server_name=tool_call.server_name,
            tool_name=tool_call.tool_name,
            parameters=inspection.sanitized_params or tool_call.parameters,
            findings_count=len(inspection.findings),
            threat_level=inspection.threat_level.value,
            pii_redacted=pii_redacted,
            call_id=tool_call.id,
        )

        result = ProxyResult(
            allowed=True,
            call_id=tool_call.id,
            sanitized_params=inspection.sanitized_params,
            findings_count=len(inspection.findings),
            threat_level=inspection.threat_level.value,
            audit_entry_id=entry.id,
        )

        # 4. Execute if requested
        if execute:
            tool_result = await self._execute_tool_call(
                tool_call, sanitized_params=inspection.sanitized_params
            )
            result.tool_result = tool_result

            # 5. Inspect result
            if tool_result.content is not None:
                result_inspection = self.inspector.inspect_tool_result(
                    tool_call.tool_name,
                    tool_result.content,
                    check_pii=self.config.pii_scan_enabled,
                )
                result.sanitized_result = result_inspection.sanitized_result
                result_pii = any(f.finding_type.value == "pii_leak" for f in result_inspection.findings)
            else:
                result_pii = False

            self.audit.log_tool_result(
                call_id=tool_call.id,
                agent_id=tool_call.agent_id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                success=not tool_result.is_error,
                error_message=tool_result.error_message,
                result_summary=str(tool_result.content)[:200] if tool_result.content else "",
                findings_count=len(result_inspection.findings) if tool_result.content is not None else 0,
                threat_level=result_inspection.threat_level.value if tool_result.content is not None else "none",
                pii_redacted=result_pii,
            )

        result.processing_time_ms = (time.time() - start) * 1000
        self._stats["total_duration_ms"] += result.processing_time_ms
        return result

    async def _execute_tool_call(
        self,
        tool_call: MCPToolCall,
        sanitized_params: Optional[dict[str, Any]] = None,
    ) -> MCPToolResult:
        """Actually execute the tool call against the MCP server."""
        server_config = self.config.servers.get(tool_call.server_name)
        if not server_config:
            return MCPToolResult(
                call_id=tool_call.id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                is_error=True,
                error_message=f"Unknown server: {tool_call.server_name}",
            )

        conn = self.pool.get_or_create(tool_call.server_name, server_config)
        params_to_send = sanitized_params or tool_call.parameters

        try:
            response = await conn.send_request(
                "tools/call",
                {"name": tool_call.tool_name, "arguments": params_to_send},
            )

            if "error" in response:
                return MCPToolResult(
                    call_id=tool_call.id,
                    server_name=tool_call.server_name,
                    tool_name=tool_call.tool_name,
                    is_error=True,
                    error_message=response["error"].get("message", str(response["error"])),
                )

            return MCPToolResult(
                call_id=tool_call.id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                content=response.get("result"),
            )

        except asyncio.TimeoutError:
            self._stats["errors"] += 1
            return MCPToolResult(
                call_id=tool_call.id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                is_error=True,
                error_message=f"Timeout after {server_config.timeout_seconds}s",
            )
        except Exception as e:
            self._stats["errors"] += 1
            return MCPToolResult(
                call_id=tool_call.id,
                server_name=tool_call.server_name,
                tool_name=tool_call.tool_name,
                is_error=True,
                error_message=str(e),
            )

    async def process_tool_result(
        self,
        tool_result: MCPToolResult,
        agent_id: str = "default",
    ) -> ProxyResult:
        """Process a tool result coming back (for cases where execution happens externally).
        
        Inspects for PII and logs to audit trail.
        """
        start = time.time()

        if self.passthrough:
            self.audit.log_tool_result(
                call_id=tool_result.call_id,
                agent_id=agent_id,
                server_name=tool_result.server_name,
                tool_name=tool_result.tool_name,
                success=not tool_result.is_error,
                error_message=tool_result.error_message,
                result_summary=str(tool_result.content)[:200] if tool_result.content else "",
            )
            return ProxyResult(
                allowed=True,
                call_id=tool_result.call_id,
                sanitized_result=tool_result.content,
                passthrough=True,
                processing_time_ms=(time.time() - start) * 1000,
            )

        inspection = self.inspector.inspect_tool_result(
            tool_result.tool_name,
            tool_result.content if tool_result.content is not None else {},
            check_pii=self.config.pii_scan_enabled,
        )

        pii_redacted = any(f.finding_type.value == "pii_leak" for f in inspection.findings)

        self.audit.log_tool_result(
            call_id=tool_result.call_id,
            agent_id=agent_id,
            server_name=tool_result.server_name,
            tool_name=tool_result.tool_name,
            success=not tool_result.is_error,
            error_message=tool_result.error_message,
            result_summary=str(tool_result.content)[:200] if tool_result.content else "",
            findings_count=len(inspection.findings),
            threat_level=inspection.threat_level.value,
            pii_redacted=pii_redacted,
        )

        return ProxyResult(
            allowed=True,  # Never block responses, just redact
            call_id=tool_result.call_id,
            sanitized_result=inspection.sanitized_result,
            findings_count=len(inspection.findings),
            threat_level=inspection.threat_level.value,
            processing_time_ms=(time.time() - start) * 1000,
        )

    def get_stats(self) -> dict[str, Any]:
        """Get proxy statistics."""
        avg_ms = (
            self._stats["total_duration_ms"] / self._stats["total_calls"]
            if self._stats["total_calls"] > 0 else 0
        )
        return {
            **self._stats,
            "avg_processing_time_ms": round(avg_ms, 1),
            "audit_entries": len(self.audit),
            "audit_chain_valid": self.audit.verify_chain()[0],
            "passthrough_mode": self.passthrough,
        }

    async def shutdown(self) -> None:
        """Clean shutdown — close all connections."""
        await self.pool.stop_all()
