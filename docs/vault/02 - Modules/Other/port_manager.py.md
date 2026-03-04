---
title: port_manager.py
type: module
file_path: gateway/tools/port_manager.py
tags: [utilities, ports, networking]
related: [Architecture Overview, Configuration/docker-compose.yml]
status: documented
---

# port_manager.py

**Location:** `gateway/tools/port_manager.py`
**Lines:** ~288

## Purpose

Detects port conflicts and auto-assigns available ports when running multiple AgentShroud instances on the same machine (e.g., Docker + Apple Containers simultaneously). Checks if configured ports are already in use and automatically increments to find the next available port.

## Default Ports

| Service | Default Port |
|---------|-------------|
| `gateway` | 8080 |
| `dns` | 5353 |
| `dashboard` | 8443 |
| `websocket` | 8081 |
| `metrics` | 9090 |

## Key Class: `PortManager`

### `resolve_ports(desired: dict[str, int]) → dict[str, int]`

Checks each port and returns a mapping with auto-incremented alternatives if conflicts found:
```python
pm = PortManager()
ports = pm.resolve_ports({"gateway": 8080, "dashboard": 8443})
# If 8080 is free: {"gateway": 8080, "dashboard": 8443}
# If 8080 is taken: {"gateway": 8081, "dashboard": 8443}
```

**Search range:** Up to +100 from base port (`PORT_SEARCH_RANGE = 100`).

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `AGENTSHROUD_PORT_OFFSET` | Manual port offset for all services |

## Related Notes

- [[Architecture Overview]] — Port reference
- [[Configuration/docker-compose.yml]] — Container port mappings
