---
title: MCP Proxy Errors
type: troubleshooting
tags: [mcp, proxy, errors]
related: [Proxy Layer/mcp_proxy.py, Configuration/agentshroud.yaml, Errors & Troubleshooting/Error Index]
status: documented
---

# MCP Proxy Errors

## HTTP 403 — MCP Tool Permission Denied

**Error:** `MCP tool permission denied: tool_send_message requires write permission`

**Cause:** Tool is configured with `permission_level: read` but the action requires `write`.

**Fix:** Update the tool permission in `agentshroud.yaml`:
```yaml
mcp_proxy:
  servers:
    mac-messages:
      tools:
        tool_send_message:
          permission_level: write   # Change from read to write
```

Then restart the gateway.

---

## HTTP 429 — MCP Rate Limit Exceeded

**Error:** `MCP rate limit exceeded: tool_send_message (limit: 30/min)`

**Cause:** Tool was called more than `rate_limit` times per minute.

**Fix options:**
1. Reduce call frequency in agent behavior
2. Increase `rate_limit` in `agentshroud.yaml`:
```yaml
tools:
  tool_send_message:
    rate_limit: 60   # Increase from 30 to 60
```

---

## HTTP 502 — MCP Server Unreachable

**Error:** `MCP server unreachable: mac-messages (http://host.docker.internal:8200)`

**Cause:** The MCP server at the configured URL is not running or not accessible.

**Diagnosis:**
```bash
# From bot container, check if host is reachable
docker exec agentshroud-bot curl -v http://host.docker.internal:8200
```

**Fixes:**
1. Start the MCP server on the host machine
2. Verify `extra_hosts: host.docker.internal:host-gateway` in docker-compose.yml
3. Check if the MCP server port changed

---

## HTTP 400 — Unknown MCP Server

**Error:** `Unknown MCP server: my-new-server`

**Cause:** The bot is trying to use an MCP server that isn't configured in `agentshroud.yaml`.

**Fix:** Add the server configuration:
```yaml
mcp_proxy:
  servers:
    my-new-server:
      transport: http_sse
      url: "http://host.docker.internal:8300"
      timeout_seconds: 30
      tools: {}   # Empty = all tools get default read permission
```

---

## MCP Proxy Wrapper Issues (Bot Side)

**Symptom:** Tool calls fail with connection errors (not HTTP errors)

**Cause:** `mcp-proxy-wrapper.js` cannot reach the gateway

**Diagnosis:**
```bash
docker logs agentshroud-bot | grep "mcp-proxy"
```

**Fixes:**
1. Verify gateway is healthy: `curl http://localhost:8080/health`
2. Check `ANTHROPIC_BASE_URL` is set correctly in bot container
3. Restart bot container

---

## Related Notes

- [[Proxy Layer/mcp_proxy.py|mcp_proxy.py]] — MCP proxy implementation
- [[Proxy Layer/mcp_permissions.py|mcp_permissions.py]] — Permission enforcement
- [[Configuration/agentshroud.yaml]] — `mcp_proxy` section
- [[JavaScript/mcp-proxy-wrapper.js|mcp-proxy-wrapper.js]] — Bot-side MCP wrapper
- [[Errors & Troubleshooting/Error Index]] — Full error index
