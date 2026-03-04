---
title: AGENTSHROUD_CONFIG
type: env-var
tags: [configuration, gateway]
related: [Configuration/agentshroud.yaml, Gateway Core/config.py, Configuration/All Environment Variables]
status: documented
---

# AGENTSHROUD_CONFIG

## Description

Explicit path to the `agentshroud.yaml` configuration file. When set, the gateway uses this path directly instead of searching the default locations.

## Default Search Order (when NOT set)

1. Explicit path argument to `load_config()`
2. `$AGENTSHROUD_CONFIG` ← this variable
3. `./agentshroud.yaml` (relative to CWD)
4. `../agentshroud.yaml`

## Usage

```bash
export AGENTSHROUD_CONFIG=/etc/agentshroud/config.yaml
```

## When to Set

- When running the gateway outside the repo directory
- When using a non-standard config file path
- When managing multiple environments with different config files

## Related Notes

- [[Configuration/agentshroud.yaml]] — The config file itself
- [[Gateway Core/config.py|config.py]] — `load_config()` function
- [[Configuration/All Environment Variables]] — All env vars
