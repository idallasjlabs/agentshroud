---
title: LOG_LEVEL
type: env-var
tags: [logging, operations]
related: [Configuration/All Environment Variables, Configuration/agentshroud.yaml]
status: documented
---

# LOG_LEVEL

## Description

Controls the verbosity of the gateway's log output.

## Values

| Value | Output |
|-------|--------|
| `DEBUG` | All logs including request/response details |
| `INFO` (default) | Normal operational logs |
| `WARNING` | Only warnings and errors |
| `ERROR` | Only errors |

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - LOG_LEVEL=INFO
```

Also configurable in `agentshroud.yaml`:
```yaml
logging:
  level: INFO
```

The environment variable takes precedence over the config file value.

## Debug Mode

To enable verbose logging for troubleshooting:
```bash
# Update docker-compose.yml or run:
LOG_LEVEL=DEBUG docker compose restart agentshroud-gateway
```

> Note: `DEBUG` logs may include sanitized request content. Never set in production unless actively debugging a specific issue.

## Related Notes

- [[Configuration/agentshroud.yaml]] — `logging.level` config key
- [[Configuration/All Environment Variables]] — All env vars
