---
title: PROXY_ALLOWED_NETWORKS
type: env-var
tags: [#type/env-var, #status/critical]
required: false
default: "172.11.0.0/16"
related: ["[[main]]", "[[agentshroud-gateway]]", "[[docker-compose.yml]]", "[[Architecture Overview]]"]
status: active
last_reviewed: 2026-03-09
---

# PROXY_ALLOWED_NETWORKS

## What It Controls

Defines which IP address ranges (CIDRs) are allowed to make requests to the gateway's proxy endpoints: `/v1/`, `/mcp/`, `/credentials/`, `/ssh/`. Requests from outside these ranges receive `403 Forbidden`.

## Expected Format

Comma-separated CIDR strings:
```
172.11.0.0/16,172.12.0.0/16
```

## Default

`172.11.0.0/16` (the `agentshroud-isolated` network subnet)

Loopback (`127.0.0.0/8`) is always included regardless of this variable.

## Where It Is Set

`docker/docker-compose.yml` gateway service:
```yaml
environment:
  - PROXY_ALLOWED_NETWORKS=172.11.0.0/16,172.12.0.0/16
```

The `172.12.0.0/16` (`agentshroud-console`) is included so the bot can reach the gateway through the console network.

## How It Is Used

```python
# main.py
_PROXY_ALLOWED_NETWORKS = [
    ipaddress.ip_network(cidr.strip())
    for cidr in os.environ.get("PROXY_ALLOWED_NETWORKS", "172.11.0.0/16").split(",")
    if cidr.strip()
] + [ipaddress.ip_network("127.0.0.0/8")]
```

Checked on every request to protected endpoints. If the request source IP is not in any of these networks, the request is rejected.

## Effect If Wrong

If the bot's IP is not in this range (e.g., after Docker network reconfiguration), all LLM calls, MCP calls, and SSH calls will fail with 403.

> [!TIP] Optional — has safe default. Only needs to change if Docker network subnets are customized.

## Used In

- [[main]] — `_PROXY_ALLOWED_NETWORKS` IP allowlist check
