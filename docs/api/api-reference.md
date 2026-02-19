# API Reference
## AgentShroud v0.9.0

### Overview

AgentShroud provides a comprehensive REST API for security proxy management and monitoring. All endpoints implement authentication, rate limiting, and comprehensive audit logging. The API follows OpenAPI 3.0 specification and supports JSON content negotiation.

**Base URL**: `https://localhost:8443/api/v1`  
**Authentication**: Bearer token or API key  
**Content Type**: `application/json`  
**API Version**: `v1`

---

## Authentication

All API endpoints require authentication using one of the following methods:

**Bearer Token**:
```
Authorization: Bearer <jwt-token>
```

**API Key**:
```
X-API-Key: <api-key>
```

**Service Account**:
```
Authorization: ServiceAccount <account-id>:<signature>
```

---

## Health and Status

### GET /health

Health check endpoint for monitoring and load balancer configuration.

**Description**: Returns system health status and basic operational metrics.

**Parameters**: None

**Response Codes**:
- `200` - System healthy
- `503` - System degraded or unhealthy

**Response Schema**:
```json
{
  "status": "healthy",
  "timestamp": "2026-02-19T11:16:00Z",
  "version": "0.9.0",
  "uptime": 86400,
  "components": {
    "database": "healthy",
    "audit_system": "healthy",
    "security_modules": "healthy",
    "external_services": "degraded"
  },
  "metrics": {
    "active_agents": 12,
    "requests_per_second": 45.2,
    "memory_usage_mb": 256,
    "cpu_usage_percent": 23.1
  }
}
```

**Example Request**:
```bash
curl -X GET https://localhost:8443/api/v1/health \
  -H "Authorization: Bearer <token>"
```

**Example Response**:
```json
{
  "status": "healthy",
  "timestamp": "2026-02-19T11:16:00Z",
  "version": "0.9.0",
  "uptime": 86400,
  "components": {
    "database": "healthy",
    "audit_system": "healthy", 
    "security_modules": "healthy",
    "external_services": "healthy"
  },
  "metrics": {
    "active_agents": 8,
    "requests_per_second": 23.7,
    "memory_usage_mb": 192,
    "cpu_usage_percent": 15.3
  }
}
```

---

## Message Processing

### POST /ingest

Primary endpoint for AI agent message ingestion with security processing.

**Description**: Processes incoming messages through the complete security pipeline including PII sanitization, prompt injection detection, and audit logging.

**Request Schema**:
```json
{
  "agent_id": "agent-12345",
  "message": "User message content",
  "session_id": "session-abcde",
  "timestamp": "2026-02-19T11:16:00Z",
  "metadata": {
    "user_id": "user-67890",
    "channel": "telegram",
    "trust_level": 5
  }
}
```

**Response Codes**:
- `200` - Message processed successfully
- `400` - Invalid request format
- `403` - Message blocked by security policy
- `429` - Rate limit exceeded
- `500` - Internal processing error

**Response Schema**:
```json
{
  "message_id": "msg-uuid-here",
  "status": "processed",
  "sanitized": true,
  "processing_time_ms": 23,
  "security_actions": [
    {
      "module": "pii_detection",
      "action": "sanitized",
      "details": "Phone number redacted"
    }
  ],
  "audit_id": "audit-uuid-here"
}
```

**Example Request**:
```bash
curl -X POST https://localhost:8443/api/v1/ingest \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "agent-12345",
    "message": "My phone number is 555-123-4567",
    "session_id": "session-abcde",
    "timestamp": "2026-02-19T11:16:00Z",
    "metadata": {
      "user_id": "user-67890",
      "channel": "telegram",
      "trust_level": 3
    }
  }'
```

**Example Response**:
```json
{
  "message_id": "msg-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "status": "processed",
  "sanitized": true,
  "processing_time_ms": 18,
  "security_actions": [
    {
      "module": "pii_detection",
      "action": "sanitized", 
      "details": "Phone number redacted"
    }
  ],
  "audit_id": "audit-f1e2d3c4-b5a6-9870-dcba-fe0987654321"
}
```

---

## Audit and Compliance

### GET /audit

Query audit trail with filtering and pagination support.

**Description**: Retrieves audit log entries with comprehensive filtering options for compliance and security analysis.

**Query Parameters**:
- `start_date` (string, ISO 8601) - Start date for query range
- `end_date` (string, ISO 8601) - End date for query range  
- `agent_id` (string) - Filter by specific agent ID
- `event_type` (string) - Filter by event type
- `severity` (string) - Filter by severity level (low, medium, high, critical)
- `limit` (integer) - Number of results to return (max 1000, default 100)
- `offset` (integer) - Pagination offset (default 0)

**Response Codes**:
- `200` - Query successful
- `400` - Invalid query parameters
- `403` - Insufficient permissions
- `500` - Query processing error

**Response Schema**:
```json
{
  "total": 1524,
  "limit": 100,
  "offset": 0,
  "entries": [
    {
      "audit_id": "audit-uuid-here",
      "timestamp": "2026-02-19T11:16:00Z",
      "event_type": "message_processed",
      "agent_id": "agent-12345",
      "user_id": "user-67890",
      "severity": "medium",
      "details": {
        "message_id": "msg-uuid-here",
        "security_actions": ["pii_sanitized"],
        "processing_time_ms": 23
      },
      "hash": "sha256-hash-value",
      "prev_hash": "sha256-previous-hash"
    }
  ],
  "hash_chain_valid": true
}
```

**Example Request**:
```bash
curl -X GET "https://localhost:8443/api/v1/audit?start_date=2026-02-19T00:00:00Z&event_type=security_violation&limit=50" \
  -H "Authorization: Bearer <token>"
```

---

## Approval System

### POST /approve/{id}

Approve or deny pending operations in the approval queue.

**Description**: Process approval requests for high-risk operations requiring human oversight.

**Path Parameters**:
- `id` (string, required) - Approval request ID

**Request Schema**:
```json
{
  "action": "approve",
  "reason": "Request validated and approved",
  "approver_id": "operator-12345",
  "conditions": {
    "time_limit_minutes": 30,
    "monitoring_required": true
  }
}
```

**Response Codes**:
- `200` - Approval processed successfully
- `400` - Invalid approval action
- `404` - Approval request not found
- `403` - Insufficient approval permissions
- `409` - Request already processed

**Response Schema**:
```json
{
  "approval_id": "approval-uuid-here",
  "status": "approved",
  "processed_at": "2026-02-19T11:16:00Z",
  "approver_id": "operator-12345",
  "conditions_applied": {
    "time_limit_minutes": 30,
    "monitoring_required": true
  },
  "audit_id": "audit-uuid-here"
}
```

### GET /approve

List pending approval requests.

**Description**: Retrieve pending approval requests for operator review.

**Query Parameters**:
- `priority` (string) - Filter by priority (low, medium, high, critical)
- `age_hours` (integer) - Filter requests older than specified hours
- `agent_id` (string) - Filter by specific agent ID
- `limit` (integer) - Number of results (max 100, default 20)

**Response Schema**:
```json
{
  "pending_count": 5,
  "requests": [
    {
      "approval_id": "approval-uuid-here",
      "created_at": "2026-02-19T10:30:00Z",
      "priority": "high",
      "agent_id": "agent-12345",
      "operation": "ssh_access",
      "details": {
        "target_host": "production-server.example.com",
        "requested_commands": ["ls", "grep", "tail"],
        "justification": "Debug production issue #1234"
      },
      "time_remaining_minutes": 25
    }
  ]
}
```

---

## Emergency Controls

### POST /kill

Activate emergency kill switch to shutdown agent operations.

**Description**: Immediately terminate all or specific agent operations in emergency situations.

**Request Schema**:
```json
{
  "scope": "all",
  "reason": "Security incident detected",
  "operator_id": "operator-12345",
  "immediate": true,
  "preserve_state": true
}
```

**Request Parameters**:
- `scope` (string) - "all", "agent", or specific agent ID
- `reason` (string, required) - Reason for kill switch activation
- `operator_id` (string, required) - ID of operator activating kill switch
- `immediate` (boolean) - Skip graceful shutdown (default: false)
- `preserve_state` (boolean) - Preserve system state for investigation

**Response Codes**:
- `200` - Kill switch activated successfully
- `400` - Invalid kill switch parameters
- `403` - Insufficient kill switch permissions
- `409` - Kill switch already active
- `500` - Kill switch activation failed

**Response Schema**:
```json
{
  "kill_switch_id": "kill-uuid-here",
  "activated_at": "2026-02-19T11:16:00Z",
  "scope": "all",
  "affected_agents": ["agent-12345", "agent-67890"],
  "operator_id": "operator-12345",
  "estimated_shutdown_seconds": 30,
  "audit_id": "audit-uuid-here"
}
```

### DELETE /kill/{id}

Deactivate kill switch and restore operations.

**Description**: Restore system operations after emergency kill switch activation.

**Path Parameters**:
- `id` (string, required) - Kill switch activation ID

**Response Schema**:
```json
{
  "kill_switch_id": "kill-uuid-here",
  "deactivated_at": "2026-02-19T11:20:00Z",
  "restored_agents": ["agent-12345", "agent-67890"],
  "operator_id": "operator-12345",
  "audit_id": "audit-uuid-here"
}
```

---

## Security Dashboard

### GET /dashboard

Retrieve security dashboard data and metrics.

**Description**: Comprehensive security metrics and status information for monitoring dashboards.

**Query Parameters**:
- `time_range` (string) - Time range for metrics (1h, 6h, 24h, 7d, 30d)
- `include_details` (boolean) - Include detailed breakdown (default: false)

**Response Codes**:
- `200` - Dashboard data retrieved successfully
- `400` - Invalid time range parameter
- `403` - Insufficient dashboard permissions

**Response Schema**:
```json
{
  "timestamp": "2026-02-19T11:16:00Z",
  "time_range": "24h",
  "security_summary": {
    "total_requests": 15420,
    "blocked_requests": 89,
    "pii_redactions": 234,
    "security_alerts": 12,
    "kill_switch_activations": 0
  },
  "active_agents": {
    "total": 8,
    "trusted": 6,
    "probationary": 2,
    "suspended": 0
  },
  "threat_metrics": {
    "prompt_injections_blocked": 23,
    "ssrf_attempts_blocked": 15,
    "malicious_content_detected": 7,
    "policy_violations": 31
  },
  "performance_metrics": {
    "avg_processing_time_ms": 28.5,
    "p95_processing_time_ms": 45.2,
    "memory_usage_mb": 203,
    "cpu_usage_percent": 18.7
  },
  "approval_queue": {
    "pending": 3,
    "approved_today": 15,
    "denied_today": 2,
    "expired": 1
  }
}
```

---

## Real-time Events

### WebSocket /ws

Real-time event streaming for monitoring and alerting.

**Description**: WebSocket connection for receiving real-time security events, alerts, and system status updates.

**Connection**: `wss://localhost:8443/api/v1/ws`

**Authentication**: Include token in connection query parameter:
```
wss://localhost:8443/api/v1/ws?token=<jwt-token>
```

**Event Types**:
- `security_alert` - High-priority security events
- `agent_status` - Agent connection/disconnection events  
- `approval_request` - New approval requests
- `kill_switch` - Kill switch activation/deactivation
- `system_status` - System health changes
- `audit_event` - Real-time audit entries

**Message Format**:
```json
{
  "event_type": "security_alert",
  "timestamp": "2026-02-19T11:16:00Z",
  "event_id": "event-uuid-here",
  "severity": "high",
  "data": {
    "alert_type": "prompt_injection_detected",
    "agent_id": "agent-12345",
    "details": {
      "confidence": 0.95,
      "pattern": "system_prompt_override",
      "blocked": true
    }
  }
}
```

**Subscription Control**:
```json
{
  "action": "subscribe",
  "event_types": ["security_alert", "approval_request"],
  "filters": {
    "severity": ["high", "critical"],
    "agent_ids": ["agent-12345", "agent-67890"]
  }
}
```

---

## System Information

### GET /version

Retrieve system version and build information.

**Description**: System version, build details, and feature flags for debugging and compatibility verification.

**Response Schema**:
```json
{
  "version": "0.9.0",
  "build": {
    "commit": "a1b2c3d4e5f6789",
    "branch": "main",
    "build_date": "2026-02-15T14:30:00Z",
    "build_number": "1234"
  },
  "features": {
    "pii_detection": true,
    "prompt_injection_protection": true,
    "mcp_proxy": true,
    "web_proxy": true,
    "ssh_proxy": true,
    "kill_switch": true,
    "approval_queue": true,
    "audit_trail": true
  },
  "dependencies": {
    "node_version": "18.19.0",
    "container_runtime": "docker",
    "database": "sqlite3",
    "security_modules": 26
  }
}
```

---

## Error Responses

All API endpoints use consistent error response format:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Request validation failed",
    "details": {
      "field": "agent_id",
      "reason": "Required field missing"
    },
    "timestamp": "2026-02-19T11:16:00Z",
    "request_id": "req-uuid-here"
  }
}
```

**Common Error Codes**:
- `INVALID_REQUEST` - Malformed request data
- `AUTHENTICATION_FAILED` - Invalid or expired token
- `AUTHORIZATION_DENIED` - Insufficient permissions
- `RATE_LIMIT_EXCEEDED` - Too many requests
- `RESOURCE_NOT_FOUND` - Requested resource not found
- `INTERNAL_ERROR` - Server processing error
- `SERVICE_UNAVAILABLE` - System temporarily unavailable

---

## Rate Limiting

API endpoints implement tiered rate limiting:

**Tier 1 (Critical Operations)**:
- Kill switch: 5 requests per minute
- Approval actions: 20 requests per minute

**Tier 2 (Security Operations)**:
- Message ingestion: 1000 requests per minute
- Audit queries: 100 requests per minute

**Tier 3 (Monitoring)**:
- Health checks: Unlimited
- Dashboard: 60 requests per minute
- WebSocket: 1 connection per token

**Rate Limit Headers**:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 995
X-RateLimit-Reset: 1640995200
```

---

## Pagination

Endpoints supporting pagination use cursor-based pagination:

**Request Parameters**:
- `limit` - Maximum results per page (default varies by endpoint)
- `cursor` - Pagination cursor from previous response

**Response Format**:
```json
{
  "data": [...],
  "pagination": {
    "has_next": true,
    "next_cursor": "cursor-string-here",
    "total_count": 1524
  }
}
```

This API reference provides comprehensive documentation for integrating with AgentShroud's security proxy functionality while maintaining security, performance, and reliability standards.