# AgentShroud Data Dictionary

This document defines all data entities and their structures within the AgentShroud system.

## Core Audit Entities

### AuditEntry
Base audit record for all system interactions.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Unique identifier for audit entry | Primary key, auto-generated |
| `timestamp` | DateTime | UTC timestamp of the event | ISO 8601 format, required |
| `direction` | Enum | Traffic direction: INBOUND, OUTBOUND | Required, validated against enum |
| `content` | Text | Sanitized content of the interaction | PII redacted, max 64KB |
| `content_hash` | String | SHA-256 hash of original content | 64 hex characters, immutable |
| `previous_hash` | String | Hash of previous audit entry | 64 hex characters, null for first entry |
| `chain_hash` | String | Cumulative hash for integrity | SHA-256(previous_hash + content_hash) |
| `agent_id` | String | Identifier of the AI agent | Required, foreign key to agent registry |
| `threat_level` | Enum | Security risk assessment | LOW, MEDIUM, HIGH, CRITICAL |
| `pii_redacted` | Boolean | Whether PII was removed | True if sanitization occurred |

**Indexes:**
- Primary: `id`
- Secondary: `agent_id, timestamp`
- Integrity: `chain_hash`

**Business Rules:**
- All entries are immutable once created
- Chain integrity must be maintained
- PII redaction is irreversible

### MCPAuditEntry
Extended audit record for MCP (Model Context Protocol) tool calls.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| *[Inherits all AuditEntry fields]* | | | |
| `server_name` | String | Name of the MCP server | Required, max 255 chars |
| `tool_name` | String | Name of the tool being called | Required, max 255 chars |
| `parameters` | JSON | Sanitized tool parameters | JSON object, max 32KB |
| `duration_ms` | Integer | Execution time in milliseconds | Non-negative, null if blocked |
| `blocked` | Boolean | Whether the call was blocked | Required, default false |
| `block_reason` | String | Reason for blocking the call | Required if blocked=true |

**Additional Indexes:**
- `server_name, tool_name`
- `blocked, timestamp`

**Business Rules:**
- Duration is null for blocked calls
- Block reason required when blocked=true
- Parameters are sanitized but structure preserved

## Security Management Entities

### ApprovalRequest
Requests requiring human approval before execution.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Unique request identifier | Primary key, auto-generated |
| `agent_id` | String | Requesting agent identifier | Required, foreign key |
| `action` | JSON | Action details requiring approval | Required, structured object |
| `status` | Enum | Current approval status | PENDING, APPROVED, DENIED, EXPIRED |
| `priority` | Enum | Request priority level | LOW, MEDIUM, HIGH, CRITICAL |
| `created_at` | DateTime | Request creation timestamp | ISO 8601, auto-generated |
| `reviewed_at` | DateTime | Review completion timestamp | Null until reviewed |
| `reviewer` | String | Identifier of reviewing admin | Required when status != PENDING |
| `review_notes` | Text | Admin notes on the decision | Optional, max 2KB |
| `expiry_at` | DateTime | Automatic expiry timestamp | Calculated based on priority |

**Indexes:**
- Primary: `id`
- Secondary: `status, priority, created_at`
- Foreign key: `agent_id`

**Business Rules:**
- Status transitions: PENDING → (APPROVED|DENIED|EXPIRED)
- Expiry calculated: LOW=4h, MEDIUM=2h, HIGH=1h, CRITICAL=30min
- Reviewer required for non-PENDING status

### TrustLevel
Agent trust level tracking and management.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `agent_id` | String | Agent identifier | Primary key |
| `level` | Integer | Current trust level (0-4) | 0=Untrusted, 4=Admin |
| `last_promoted` | DateTime | Last promotion timestamp | Null if never promoted |
| `total_actions` | Integer | Lifetime action count | Non-negative, auto-incremented |
| `violations` | Integer | Security violation count | Non-negative, manual increment |
| `violation_rate` | Decimal | Violations / total_actions | Calculated field, 0.0-1.0 |
| `last_violation` | DateTime | Most recent violation | Null if no violations |
| `promotion_eligible` | Boolean | Eligible for next level | Calculated based on criteria |

**Indexes:**
- Primary: `agent_id`
- Secondary: `level, last_promoted`

**Business Rules:**
- Level 0→1: Initial assessment
- Level 1→2: 100+ actions, 0 violations, 7+ days
- Level 2→3: 1000+ actions, <5% violation rate
- Level 3→4: Manual promotion only
- Any violation can reset to level 0

## Network Security Entities

### DNSQuery
DNS resolution requests and security analysis.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Query identifier | Primary key, auto-generated |
| `timestamp` | DateTime | Query timestamp | ISO 8601, required |
| `agent_id` | String | Requesting agent | Required, foreign key |
| `domain` | String | Requested domain name | Required, max 253 chars |
| `allowed` | Boolean | Whether query was permitted | Required, default true |
| `flagged` | Boolean | Security flag raised | Default false |
| `reason` | String | Block/flag reason | Required if allowed=false or flagged=true |
| `resolved_ip` | String | IP address resolved to | Null if blocked |
| `response_time_ms` | Integer | DNS resolution time | Non-negative |

**Indexes:**
- Primary: `id`
- Secondary: `domain, timestamp`
- Security: `flagged, agent_id`

**Business Rules:**
- Blocked domains return null IP
- Flagged queries require investigation
- Resolution time tracked for performance

### URLAnalysisResult
URL safety analysis and SSRF protection.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Analysis identifier | Primary key, auto-generated |
| `url` | String | Full URL being analyzed | Required, max 2048 chars |
| `verdict` | Enum | Safety assessment | SAFE, SUSPICIOUS, MALICIOUS, BLOCKED |
| `findings` | JSON | Detailed analysis results | Array of finding objects |
| `resolved_ip` | String | IP address URL resolves to | IPv4/IPv6 format |
| `is_ssrf` | Boolean | Server-Side Request Forgery risk | True if private/internal IP |
| `analyzed_at` | DateTime | Analysis timestamp | ISO 8601, auto-generated |
| `reputation_score` | Integer | URL reputation (0-100) | Higher = more trustworthy |
| `category` | String | Content category | News, Social, Tech, etc. |

**Indexes:**
- Primary: `id`
- Secondary: `url, analyzed_at`
- Security: `verdict, is_ssrf`

**Business Rules:**
- SSRF protection blocks private IPs (10.x, 192.168.x, 127.x)
- Reputation scores below 30 flagged as suspicious
- Analysis results cached for 1 hour

### InspectionResult
Content and parameter inspection results.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Inspection identifier | Primary key, auto-generated |
| `blocked` | Boolean | Content blocked | Required, default false |
| `block_reason` | String | Reason for blocking | Required if blocked=true |
| `findings` | JSON | Security findings array | Array of SecurityFinding objects |
| `sanitized_params` | JSON | Cleaned parameters | Original structure preserved |
| `threat_level` | Enum | Overall threat assessment | LOW, MEDIUM, HIGH, CRITICAL |
| `inspection_time_ms` | Integer | Processing time | Performance metric |
| `rules_triggered` | Array | Security rules that matched | Rule ID array |

**Indexes:**
- Primary: `id`
- Performance: `inspection_time_ms`
- Security: `threat_level, blocked`

**Business Rules:**
- Block reason mandatory for blocked content
- Sanitization preserves parameter structure
- Performance metrics tracked for optimization

### SecurityFinding
Individual security findings within inspections.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | UUID | Finding identifier | Primary key, auto-generated |
| `file_path` | String | File path (if applicable) | Optional, max 1024 chars |
| `threat_level` | Enum | Severity of finding | LOW, MEDIUM, HIGH, CRITICAL |
| `category` | String | Type of security issue | INJECTION, XSS, TRAVERSAL, etc. |
| `description` | Text | Human-readable description | Required, max 1KB |
| `matched_pattern` | String | Security rule pattern matched | Optional, max 512 chars |
| `confidence` | Integer | Confidence in finding (0-100) | Higher = more certain |
| `remediation` | Text | Suggested remediation | Optional, max 2KB |

**Indexes:**
- Primary: `id`
- Secondary: `category, threat_level`
- Performance: `confidence DESC`

**Business Rules:**
- Critical findings require immediate attention
- Confidence below 70% may be false positives
- Remediation guidance helps ops teams

## Configuration Entities

### ConfigurationSetting
System configuration parameters.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `key` | String | Configuration key | Primary key, max 255 chars |
| `value` | Text | Configuration value | JSON or string format |
| `type` | Enum | Value type | STRING, INTEGER, BOOLEAN, JSON |
| `description` | Text | Setting description | Max 1KB |
| `updated_at` | DateTime | Last modification time | Auto-updated |
| `updated_by` | String | Admin who made change | Required for audit |
| `requires_restart` | Boolean | Service restart needed | Default false |

**Indexes:**
- Primary: `key`
- Audit: `updated_at DESC`

**Business Rules:**
- Type validation enforced
- Audit trail for all changes
- Restart flag helps ops teams

## Runtime State Entities

### RateLimitBucket
Rate limiting state per agent/resource.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `agent_id` | String | Agent identifier | Part of composite key |
| `resource` | String | Resource type (MCP, web, ssh) | Part of composite key |
| `tokens` | Integer | Current token count | Non-negative |
| `max_tokens` | Integer | Maximum tokens allowed | Positive integer |
| `refill_rate` | Integer | Tokens per second | Positive integer |
| `last_refill` | DateTime | Last refill timestamp | Auto-updated |
| `blocked_until` | DateTime | Block expiry time | Null if not blocked |

**Indexes:**
- Primary: `agent_id, resource`
- Cleanup: `last_refill`

**Business Rules:**
- Token bucket algorithm implementation
- Refill rate varies by trust level
- Blocked agents cannot make requests

### SessionState
Active session tracking and management.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `session_id` | UUID | Session identifier | Primary key |
| `agent_id` | String | Associated agent | Required, foreign key |
| `created_at` | DateTime | Session start time | Auto-generated |
| `last_activity` | DateTime | Last request timestamp | Auto-updated |
| `request_count` | Integer | Total requests in session | Auto-incremented |
| `active` | Boolean | Session active status | Default true |
| `ip_address` | String | Client IP address | IPv4/IPv6 format |
| `user_agent` | String | Client user agent | Optional, max 512 chars |

**Indexes:**
- Primary: `session_id`
- Cleanup: `last_activity`
- Security: `ip_address, agent_id`

**Business Rules:**
- Sessions expire after 24h inactivity
- IP tracking for security analysis
- Request count for usage monitoring

## Relationship Diagram

```
AuditEntry
    │
    ├── MCPAuditEntry (extends)
    │
    └── agent_id ──────────┐
                           │
TrustLevel ────────────────┤
    │                     │
    └── agent_id          │
                          │
ApprovalRequest ──────────┤
    │                     │
    ├── agent_id          │
    └── reviewer ─────────┤
                          │
DNSQuery ─────────────────┤
    │                     │
    └── agent_id          │
                          │
SessionState ─────────────┤
    │                     │
    └── agent_id          │
                          │
RateLimitBucket ──────────┘
    │
    └── agent_id

InspectionResult
    │
    └── findings[] ───────▶ SecurityFinding

URLAnalysisResult
    │
    └── findings[] ───────▶ SecurityFinding

ConfigurationSetting (standalone)
```

## Data Retention Policies

| Entity | Retention Period | Archive Strategy |
|--------|------------------|------------------|
| AuditEntry | 7 years | Yearly archive to cold storage |
| MCPAuditEntry | 7 years | Yearly archive to cold storage |
| ApprovalRequest | 3 years | Quarterly archive |
| TrustLevel | Indefinite | Active table |
| DNSQuery | 1 year | Monthly rotation |
| URLAnalysisResult | 6 months | Cache cleanup |
| InspectionResult | 1 year | Monthly rotation |
| SecurityFinding | 1 year | Monthly rotation |
| ConfigurationSetting | Indefinite | Version history |
| RateLimitBucket | 24 hours | Memory/Redis only |
| SessionState | 30 days | Daily cleanup |

## Data Classification

| Level | Entities | Access Control | Encryption |
|-------|----------|----------------|------------|
| **PUBLIC** | ConfigurationSetting (non-sensitive) | Read: All, Write: Admin | None required |
| **INTERNAL** | TrustLevel, RateLimitBucket, SessionState | Read: Ops Team, Write: System | At rest |
| **CONFIDENTIAL** | DNSQuery, URLAnalysisResult, InspectionResult | Read: Security Team, Write: System | At rest + transit |
| **RESTRICTED** | AuditEntry, MCPAuditEntry, ApprovalRequest, SecurityFinding | Read: Admin only, Write: System | At rest + transit + backup |

This data dictionary ensures consistent data handling across all AgentShroud components while maintaining security and compliance requirements.