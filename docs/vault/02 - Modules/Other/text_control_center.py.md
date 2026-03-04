---
title: text_control_center.py
type: module
file_path: gateway/tools/agentshroud_manager.py (or text_control_center)
tags: [cli, management, utilities]
related: [Web & Dashboard/api.py, Gateway Core/main.py]
status: inferred
---

# text_control_center.py / agentshroud_manager.py

> **Note:** Based on the project structure, this corresponds to `gateway/tools/agentshroud_manager.py` (~303 lines), the gateway manager CLI tool.

## Purpose

CLI interface for managing the AgentShroud gateway from the command line. Provides text-based control center operations without requiring the web dashboard.

## Key Operations (Inferred)

- Start/stop/restart gateway services
- Query gateway health and status
- Manage approval queue (approve/deny items)
- View audit ledger entries
- Toggle security module modes
- Run kill switch

## Relationship to Web API

Provides the same management capabilities as `gateway/web/api.py` but as a CLI tool rather than REST endpoints.

## Related Notes

- [[Web & Dashboard/api.py|api.py]] — REST API providing same functionality
- [[Gateway Core/main.py|main.py]] — Gateway being managed
- [[Runbooks/Restart Procedure]] — Operations these tools support
