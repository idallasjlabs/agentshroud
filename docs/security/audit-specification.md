# AgentShroud Audit Specification

## Overview

AgentShroud implements a comprehensive audit system with cryptographic integrity guarantees through SHA-256 hash chaining. The audit system captures all security-relevant events across the platform, providing complete traceability for compliance, forensic analysis, and security monitoring.

## Audit Event Types and Schema

### Core Event Categories

#### 1. Authentication Events (AUTH)
```json
{
  "event_id": "auth_001_20251219_103045_abc123",
  "category": "AUTH",
  "event_type": "login_attempt",
  "timestamp": "2025-12-19T10:30:45.123Z",
  "user_id": "user_12345",
  "source_ip": "192.168.1.100",
  "user_agent": "AgentShroud-Dashboard/1.0",
  "success": true,
  "failure_reason": null,
  "session_id": "sess_abc123def456",
  "mfa_used": true,
  "geolocation": "US-CA-San Francisco"
}
```

**Sub-types**:
- `login_attempt` - User login attempts (success/failure)
- `logout` - User logout events
- `session_timeout` - Session expiration events
- `password_change` - Password modification events
- `mfa_enrollment` - Multi-factor authentication setup
- `api_key_generated` - API key creation events
- `certificate_issued` - Certificate generation events

#### 2. Authorization Events (AUTHZ)
```json
{
  "event_id": "authz_002_20251219_103046_def456",
  "category": "AUTHZ",
  "event_type": "permission_check",
  "timestamp": "2025-12-19T10:30:46.234Z",
  "user_id": "agent_67890",
  "trust_level": 2,
  "resource": "mcp_tool:file_writer",
  "action": "execute",
  "decision": "allowed",
  "policy_version": "v1.2.3",
  "approval_required": false,
  "approval_id": null
}
```

**Sub-types**:
- `permission_check` - Resource access authorization decisions
- `role_assignment` - Role changes and assignments
- `trust_level_change` - Agent trust level modifications
- `approval_request` - Human approval workflow initiations
- `approval_decision` - Human approval decisions
- `policy_enforcement` - Security policy enforcement actions

#### 3. Security Events (SEC)
```json
{
  "event_id": "sec_003_20251219_103047_ghi789",
  "category": "SEC",
  "event_type": "threat_detected",
  "timestamp": "2025-12-19T10:30:47.345Z",
  "threat_type": "prompt_injection",
  "confidence_score": 0.87,
  "threat_pattern": "ignore_previous_instructions",
  "source_agent": "agent_67890",
  "request_payload_hash": "sha256:a1b2c3d4e5f6...",
  "mitigation_action": "blocked",
  "alert_triggered": true,
  "kill_switch_activated": false
}
```

**Sub-types**:
- `threat_detected` - Security threat identification
- `vulnerability_scan` - System vulnerability assessments
- `intrusion_attempt` - Unauthorized access attempts
- `malware_detected` - Malicious code identification
- `data_exfiltration` - Suspicious data egress patterns
- `kill_switch_activation` - Emergency response activations
- `security_policy_violation` - Policy compliance violations

#### 4. Data Events (DATA)
```json
{
  "event_id": "data_004_20251219_103048_jkl012",
  "category": "DATA",
  "event_type": "pii_detected",
  "timestamp": "2025-12-19T10:30:48.456Z",
  "pii_types": ["email", "phone_number"],
  "confidence_scores": {"email": 0.95, "phone_number": 0.89},
  "source_location": "request_body",
  "sanitization_applied": true,
  "original_hash": "sha256:b2c3d4e5f6g7...",
  "sanitized_hash": "sha256:c3d4e5f6g7h8...",
  "retention_policy": "30_days"
}
```

**Sub-types**:
- `pii_detected` - Personally identifiable information detection
- `data_classification` - Automatic data sensitivity classification
- `encryption_applied` - Data encryption operations
- `backup_created` - Data backup operations
- `data_retention` - Data lifecycle management events
- `gdpr_request` - GDPR/privacy regulation compliance events

#### 5. System Events (SYS)
```json
{
  "event_id": "sys_005_20251219_103049_mno345",
  "category": "SYS",
  "event_type": "container_deployed",
  "timestamp": "2025-12-19T10:30:49.567Z",
  "container_id": "cont_abc123",
  "image": "agentshroud/gateway:v1.2.3",
  "runtime": "docker",
  "security_context": {
    "seccomp_profile": "restricted",
    "capabilities": ["NET_BIND_SERVICE"],
    "user_namespace": true
  },
  "network_config": {
    "networks": ["agentshroud_internal"],
    "exposed_ports": []
  }
}
```

**Sub-types**:
- `container_deployed` - Container creation and deployment
- `service_started` - Service initialization events
- `configuration_changed` - System configuration modifications
- `resource_usage` - System resource utilization metrics
- `health_check` - System health monitoring events
- `maintenance_operation` - Scheduled maintenance activities

## Hash Chain Structure

### Chain Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Genesis       │───►│   Block 1       │───►│   Block 2       │
│   Block         │    │                 │    │                 │
│                 │    │ prev_hash: G    │    │ prev_hash: B1   │
│ prev_hash: null │    │ content_hash    │    │ content_hash    │
│ chain_hash: G   │    │ chain_hash: B1  │    │ chain_hash: B2  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Block Structure
```json
{
  "sequence": 12345,
  "timestamp": "2025-12-19T10:30:50.678Z",
  "previous_hash": "sha256:a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6...",
  "events": [
    {
      "event_id": "auth_001_20251219_103045_abc123",
      "category": "AUTH",
      "event_type": "login_attempt",
      "payload": {...}
    }
  ],
  "content_hash": "sha256:b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7...",
  "chain_hash": "sha256:c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8...",
  "signature": {
    "algorithm": "RSA-PSS",
    "public_key_id": "audit_key_001",
    "signature": "base64_encoded_signature"
  }
}
```

### Hash Calculation Algorithm
```python
def calculate_chain_hash(block: AuditBlock) -> str:
    """Calculate cryptographic hash for audit block chain"""
    
    # Step 1: Calculate content hash
    content_data = json.dumps({
        "sequence": block.sequence,
        "timestamp": block.timestamp.isoformat(),
        "events": block.events
    }, sort_keys=True, separators=(',', ':'))
    
    content_hash = hashlib.sha256(content_data.encode('utf-8')).hexdigest()
    
    # Step 2: Calculate chain hash
    chain_data = f"{block.previous_hash}:{content_hash}:{block.sequence}:{block.timestamp.isoformat()}"
    chain_hash = hashlib.sha256(chain_data.encode('utf-8')).hexdigest()
    
    return chain_hash

def verify_chain_integrity(blocks: List[AuditBlock]) -> bool:
    """Verify complete audit chain integrity"""
    
    for i, block in enumerate(blocks):
        # Verify content hash
        calculated_content_hash = calculate_content_hash(block)
        if calculated_content_hash != block.content_hash:
            logger.error(f"Content hash mismatch at block {block.sequence}")
            return False
        
        # Verify chain linkage
        if i > 0:
            if block.previous_hash != blocks[i-1].chain_hash:
                logger.error(f"Chain linkage broken at block {block.sequence}")
                return False
        
        # Verify digital signature
        if not verify_block_signature(block):
            logger.error(f"Signature verification failed at block {block.sequence}")
            return False
    
    return True
```

### Genesis Block Specification
```json
{
  "sequence": 0,
  "timestamp": "2025-12-01T00:00:00.000Z",
  "previous_hash": null,
  "events": [
    {
      "event_id": "genesis_000_20251201_000000_000000",
      "category": "SYS",
      "event_type": "audit_system_initialized",
      "payload": {
        "version": "1.0.0",
        "hash_algorithm": "SHA-256",
        "signature_algorithm": "RSA-PSS",
        "random_seed": "base64_encoded_entropy"
      }
    }
  ],
  "content_hash": "sha256:genesis_content_hash",
  "chain_hash": "sha256:genesis_chain_hash"
}
```

## Retention Policies

### Tier-Based Retention Strategy

#### Tier 1: Critical Security Events (7 Years)
- Authentication failures and successes
- Authorization violations
- Security threats and incidents  
- Privacy regulation compliance events
- Administrative actions and policy changes

#### Tier 2: Operational Events (3 Years)
- Agent trust level changes
- Approval workflow decisions
- System configuration modifications
- Data processing activities
- Performance monitoring metrics

#### Tier 3: Debug and Diagnostic Events (1 Year)
- Detailed request/response logging
- System health check results
- Resource utilization metrics
- Development and testing activities

#### Tier 4: High-Volume Events (90 Days)
- Successful routine operations
- Heartbeat and status updates
- Automated system maintenance
- Non-security related diagnostic data

### Archival Process
```python
class AuditRetentionManager:
    def __init__(self):
        self.retention_policies = {
            'CRITICAL': timedelta(days=2555),  # 7 years
            'OPERATIONAL': timedelta(days=1095),  # 3 years
            'DIAGNOSTIC': timedelta(days=365),   # 1 year
            'HIGH_VOLUME': timedelta(days=90)    # 90 days
        }
    
    def archive_expired_events(self):
        """Archive events based on retention policies"""
        for tier, retention_period in self.retention_policies.items():
            cutoff_date = datetime.utcnow() - retention_period
            
            # Move to cold storage
            expired_events = self.query_events_before(cutoff_date, tier)
            self.archive_to_cold_storage(expired_events, tier)
            
            # Update hash chain references
            self.update_chain_metadata(expired_events)
            
            # Compliance notification
            self.notify_compliance_team(tier, len(expired_events))
```

## Query Capabilities

### Query API Specification

#### Basic Event Query
```http
GET /api/v1/audit/events
  ?category=AUTH
  &event_type=login_attempt
  &start_time=2025-12-01T00:00:00Z
  &end_time=2025-12-19T23:59:59Z
  &limit=100
  &offset=0
```

#### Advanced Search Query
```http
POST /api/v1/audit/search
Content-Type: application/json

{
  "query": {
    "bool": {
      "must": [
        {"term": {"category": "SEC"}},
        {"range": {"confidence_score": {"gte": 0.8}}},
        {"terms": {"threat_type": ["prompt_injection", "data_exfiltration"]}}
      ]
    }
  },
  "aggregations": {
    "threats_by_type": {
      "terms": {"field": "threat_type"}
    }
  },
  "sort": [{"timestamp": {"order": "desc"}}]
}
```

#### Chain Verification Query
```http
GET /api/v1/audit/verify
  ?start_sequence=1000
  &end_sequence=2000
  &include_signatures=true
```

### Query Response Format
```json
{
  "total": 1337,
  "offset": 0,
  "limit": 100,
  "events": [...],
  "aggregations": {...},
  "chain_verification": {
    "verified": true,
    "blocks_checked": 1000,
    "integrity_score": 1.0,
    "last_verified": "2025-12-19T10:30:50Z"
  },
  "query_metadata": {
    "execution_time_ms": 45,
    "cache_hit": false,
    "query_id": "query_abc123"
  }
}
```

### Real-Time Event Streaming
```python
# WebSocket connection for real-time audit events
ws://api.agentshroud.local/audit/stream
  ?categories=SEC,AUTH
  &threat_levels=HIGH,CRITICAL
  &agents=agent_12345,agent_67890

# Event stream format
{
  "stream_id": "stream_abc123",
  "event": {
    "event_id": "sec_006_20251219_103050_pqr678",
    "category": "SEC",
    "event_type": "threat_detected",
    "timestamp": "2025-12-19T10:30:50.789Z",
    "payload": {...}
  },
  "sequence": 12346
}
```

## Compliance Mapping

### IEC 62443 Industrial Security Framework

#### Security Levels Mapping
```yaml
IEC_62443_Mapping:
  SL1_Protection_Against_Casual_Violation:
    - basic_authentication_logging
    - network_segmentation_audit
    - access_control_monitoring
    
  SL2_Protection_Against_Intentional_Violation:
    - failed_authentication_detection
    - authorization_violation_logging
    - security_event_correlation
    
  SL3_Protection_Against_Sophisticated_Attacks:
    - advanced_threat_detection
    - behavioral_anomaly_monitoring
    - cryptographic_integrity_verification
    
  SL4_Protection_Against_State_Sponsored_Attacks:
    - complete_audit_trail_preservation
    - tamper_evident_logging
    - real_time_threat_intelligence
```

#### Functional Requirements Coverage
```yaml
Identification_and_Authentication_Control:
  - FR1: All authentication attempts logged
  - FR2: Multi-factor authentication events captured
  - FR3: Session management fully audited
  
Use_Control:
  - FR1: All resource access attempts logged
  - FR2: Privilege escalation detection
  - FR3: Role-based access enforcement auditing

System_Integrity:
  - FR1: Configuration change detection
  - FR2: Software integrity monitoring
  - FR3: Cryptographic verification logging

Data_Confidentiality:
  - FR1: Encryption operation logging
  - FR2: Data access audit trails
  - FR3: PII handling compliance tracking
```

### GDPR Article 30 Record Keeping

#### Processing Activities Register
```json
{
  "processing_activity": "AI_Agent_Security_Monitoring",
  "controller": {
    "name": "AgentShroud Security System",
    "contact": "privacy@agentshroud.com"
  },
  "purposes": [
    "Security monitoring and threat detection",
    "Compliance with legal obligations",
    "Legitimate interests in system protection"
  ],
  "categories_of_personal_data": [
    "IP addresses",
    "User identifiers", 
    "Authentication credentials",
    "System access logs"
  ],
  "categories_of_recipients": [
    "Security operations team",
    "System administrators",
    "Authorized third-party auditors"
  ],
  "retention_periods": {
    "security_events": "7 years",
    "access_logs": "3 years",
    "diagnostic_data": "1 year"
  },
  "technical_safeguards": [
    "Encryption at rest and in transit",
    "Access controls and authentication",
    "Audit logging and monitoring"
  ]
}
```

### SOX Compliance (Section 404)

#### Internal Controls Documentation
```yaml
SOX_Section_404_Controls:
  Access_Controls:
    - "AC-001: User access provisioning and deprovisioning"
    - "AC-002: Privileged access management"
    - "AC-003: Segregation of duties enforcement"
    
  Change_Management:
    - "CM-001: Configuration change authorization"
    - "CM-002: Emergency change procedures"
    - "CM-003: Change success validation"
    
  Monitoring_Controls:
    - "MC-001: Continuous security monitoring"
    - "MC-002: Exception reporting and escalation"
    - "MC-003: Management review and oversight"
```

### ISO 27001 Control Objectives

#### A.12.4 Logging and Monitoring
```yaml
Control_A.12.4.1_Event_Logging:
  implementation: "Complete audit event capture with hash chain integrity"
  evidence: "Daily audit log verification reports"
  
Control_A.12.4.2_Log_Information_Protection:
  implementation: "Encrypted audit logs with access controls"
  evidence: "Cryptographic integrity verification"
  
Control_A.12.4.3_Administrator_Logs:
  implementation: "All administrative actions logged and monitored"
  evidence: "Administrative activity reports"
  
Control_A.12.4.4_Clock_Synchronization:
  implementation: "NTP-synchronized timestamps across all systems"
  evidence: "Time synchronization verification logs"
```

## Performance and Scalability

### Audit System Performance Metrics
```yaml
Performance_Targets:
  event_ingestion_rate: "10,000 events/second"
  query_response_time: "< 100ms (95th percentile)"
  chain_verification_time: "< 1 second per 1,000 blocks"
  storage_efficiency: "< 500 bytes per event"
  
Scalability_Limits:
  max_events_per_block: 1000
  max_block_size: "1MB"
  chain_segment_size: "10,000 blocks"
  archive_threshold: "100GB active storage"
```

This comprehensive audit specification ensures AgentShroud provides enterprise-grade audit capabilities meeting international compliance standards while maintaining high performance and scalability.