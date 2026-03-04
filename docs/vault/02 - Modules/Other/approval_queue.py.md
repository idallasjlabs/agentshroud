---
title: approval_queue.py (EnhancedApprovalQueue)
type: module
file_path: gateway/approval_queue/enhanced_queue.py
tags: [approval, queue, human-in-the-loop, security]
related: [Gateway Core/main.py, Gateway Core/models.py, Runbooks/Kill Switch Procedure]
status: documented
---

# EnhancedApprovalQueue (`enhanced_queue.py`)

**Location:** `gateway/approval_queue/enhanced_queue.py`
**Lines:** ~357

## Purpose

Human-in-the-loop approval queue that holds risky agent actions pending operator review. Implements tool risk tier policies (critical/high/medium/low), SQLite persistence, WebSocket notifications, and timeout-based auto-deny.

## Responsibilities

- Hold pending approvals for actions in configured `require_approval_for` list
- Enforce tool risk tier policies (critical tools require approval; low tools auto-approve)
- Notify connected dashboard clients via WebSocket when new items arrive
- Send Telegram notifications for critical-tier actions
- Auto-deny (or auto-approve) after `timeout_seconds` expires
- Support "owner bypass" — designated owner can approve without waiting

## Key Class: `EnhancedApprovalQueue`

| Method | Purpose |
|--------|---------|
| `__init__(config, tool_risk_config, store)` | Initialize queue with configs and persistence store |
| `enqueue(request)` | Add action to queue; returns `ApprovalQueueItem` |
| `approve(item_id, user_id)` | Approve pending item |
| `deny(item_id, user_id, reason)` | Deny pending item |
| `get_pending()` | List all pending items |
| `register_websocket(ws)` | Register WebSocket client for notifications |
| `unregister_websocket(ws)` | Remove WebSocket client |

## Tool Risk Tiers

| Tier | Tools | Requires Approval | Timeout Action |
|------|-------|------------------|---------------|
| Critical | `exec`, `cron`, `sessions_send` | Yes | deny |
| High | `nodes`, `browser`, `apply_patch`, `subagents` | Yes | deny |
| Medium | `grep`, `find`, `sessions_*` | No | deny |
| Low | `ls`, `canvas`, `process` | No | deny |

Configured in `agentshroud.yaml` `tool_risk` section and `GatewayConfig.tool_risk`.

## Persistence

Uses `ApprovalStore` (SQLite at `/tmp/approvals.db`) for persistence across restarts.
> **TODO in code:** Hardcoded path `/tmp/approvals.db` — should use configurable path.

## WebSocket Notifications

When a new item is enqueued, all connected WebSocket clients receive a notification:
```json
{
  "type": "approval_request",
  "item": {...}
}
```

## Timeout Behavior

Each item has a timeout task. If not approved/denied within `timeout_seconds` (default: 5 minutes for critical/high):
- `timeout_action: deny` → item is auto-denied
- `timeout_action: allow` → item is auto-approved

## Environment Variables Used

None directly — configuration comes from `ApprovalQueueConfig` and `ToolRiskConfig`.

## Related Notes

- [[Gateway Core/main.py|main.py]] — Creates and manages the queue instance
- [[Gateway Core/config.py|config.py]] — `ApprovalQueueConfig` and `ToolRiskConfig`
- [[Gateway Core/models.py|models.py]] — `ApprovalQueueItem`, `ApprovalRequest`
- [[Configuration/agentshroud.yaml]] — `tool_risk` and `approval_queue` configuration
