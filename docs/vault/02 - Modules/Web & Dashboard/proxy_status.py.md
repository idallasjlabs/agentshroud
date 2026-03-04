---
title: proxy_status.py
type: module
file_path: gateway/dashboard/proxy_status.py
tags: [dashboard, status, monitoring]
related: [Web & Dashboard/api.py, Security Modules/health_report.py, Architecture Overview]
status: documented
---

# proxy_status.py

**Location:** `gateway/dashboard/proxy_status.py`
**Lines:** ~148

## Purpose

Proxy status reporting module for the AgentShroud dashboard. Aggregates status information from all active proxy components and returns a consolidated status report.

## Responsibilities

- Collect status from MCP proxy, LLM proxy, Telegram proxy, HTTP proxy, Web proxy
- Report active connections, request counts, error rates
- Provide data for the dashboard status panel

## Key Output

Status report structure (inferred from context):
```json
{
  "proxies": {
    "mcp": {"status": "active", "requests": 42, "errors": 0},
    "llm": {"status": "active", "requests": 18, "errors": 0},
    "telegram": {"status": "active", "requests": 5, "errors": 0},
    "http": {"status": "active", "requests": 7, "errors": 0}
  },
  "last_updated": "2026-03-03T10:00:00Z"
}
```

## Related Notes

- [[Web & Dashboard/api.py|api.py]] — Management API that calls this
- [[Security Modules/health_report.py|health_report.py]] — System-wide health report
- [[Runbooks/Health Checks]] — How to use health data
