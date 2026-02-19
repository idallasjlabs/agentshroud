# SecureClaw Access Control Matrix

## Overview

SecureClaw implements Role-Based Access Control (RBAC) with trust-level progression to provide granular permission management. The system supports five primary roles with trust levels ranging from 0 (untrusted) to 4 (highly trusted), enabling dynamic security controls based on behavioral analysis.

## RBAC Role Definitions

### Administrative Roles

#### Admin (admin)
**Trust Level**: N/A (Administrative)
**Description**: Full system administration capabilities
**Typical Users**: SecureClaw system administrators, security team leads

#### Operator (operator)  
**Trust Level**: N/A (Administrative)
**Description**: Operational management without policy modification
**Typical Users**: SOC analysts, system operators, DevOps engineers

#### Viewer (viewer)
**Trust Level**: N/A (Administrative)
**Description**: Read-only access to logs, metrics, and dashboards
**Typical Users**: Compliance auditors, management, stakeholders

### Agent Trust Levels

#### Trust Level 0 (agent_l0)
**Description**: New or untrusted agents with maximum restrictions
**Characteristics**: All actions require approval, comprehensive monitoring
**Progression Time**: Minimum 7 days of consistent behavior

#### Trust Level 1 (agent_l1)
**Description**: Basic trust with limited tool access
**Characteristics**: High-risk actions require approval, standard monitoring  
**Progression Time**: 14 days of compliant behavior

#### Trust Level 2 (agent_l2)
**Description**: Standard operational trust level
**Characteristics**: Suspicious actions trigger approval, normal monitoring
**Progression Time**: 30 days of consistent performance

#### Trust Level 3 (agent_l3)
**Description**: High trust with advanced capabilities
**Characteristics**: Only clear threats blocked, reduced oversight
**Progression Time**: 60 days of excellent behavior

#### Trust Level 4 (agent_l4)
**Description**: Verified trust with minimal restrictions
**Characteristics**: Monitor-only mode, autonomous operation
**Progression Time**: 90 days of exceptional performance + manual verification

## Permission Matrix

### System Administration

| Permission | Admin | Operator | Viewer | L0 | L1 | L2 | L3 | L4 |
|------------|--------|----------|--------|----|----|----|----|-------|
| **Security Policy Management** |
| Create/Modify Security Policies | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Security Policies | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Apply Emergency Security Updates | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Kill Switch Operations** |
| Activate Global Kill Switch | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Activate Individual Agent Kill Switch | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Kill Switch Status | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **User Management** |
| Create/Delete User Accounts | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Modify User Roles | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View User Accounts | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Reset User Passwords | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

### Agent Management

| Permission | Admin | Operator | Viewer | L0 | L1 | L2 | L3 | L4 |
|------------|--------|----------|--------|----|----|----|----|-------|
| **Trust Level Management** |
| Modify Agent Trust Levels | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Trust Level History | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Override Trust Calculations | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Agent Lifecycle** |
| Deploy New Agent | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Terminate Agent | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Suspend/Resume Agent | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Agent Status | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### Approval Queue Management

| Permission | Admin | Operator | Viewer | L0 | L1 | L2 | L3 | L4 |
|------------|--------|----------|--------|----|----|----|----|-------|
| **Queue Operations** |
| Approve High-Risk Requests | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Approve Medium-Risk Requests | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Approve Low-Risk Requests | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Approval Queue | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Modify Queue Priorities | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Approval Workflows** |
| Create Custom Approval Workflows | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Assign Approval Reviewers | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

### Monitoring and Audit

| Permission | Admin | Operator | Viewer | L0 | L1 | L2 | L3 | L4 |
|------------|--------|----------|--------|----|----|----|----|-------|
| **Log Access** |
| Access Security Logs | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Access Agent Activity Logs | ✓ | ✓ | ✓ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Access System Audit Logs | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Export Log Data | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Metrics and Monitoring** |
| View Security Metrics | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| View Performance Metrics | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Configure Alerting | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Access Real-Time Dashboard | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

*⚠️ = Agents can only access their own activity logs*

## Agent Operational Permissions

### External Service Access

| Service Type | L0 | L1 | L2 | L3 | L4 | Approval Required |
|--------------|----|----|----|----|-------|-------------------|
| **LLM APIs** |
| OpenAI GPT Models | A | A | ✓ | ✓ | ✓ | L0/L1: Yes |
| Anthropic Claude | A | A | ✓ | ✓ | ✓ | L0/L1: Yes |
| Open Source Models | ✗ | A | ✓ | ✓ | ✓ | L0: No, L1: Yes |
| **Search Services** |
| Web Search (Brave/Google) | A | ✓ | ✓ | ✓ | ✓ | L0: Yes |
| Academic Databases | ✗ | A | ✓ | ✓ | ✓ | L1: Yes |
| **Communication** |
| Email Sending | ✗ | A | A | ✓ | ✓ | L1/L2: Yes |
| Social Media Posting | ✗ | ✗ | A | A | ✓ | L2/L3: Yes |
| Messaging Platforms | A | A | ✓ | ✓ | ✓ | L0/L1: Yes |

**Legend**: ✓ = Allowed, ✗ = Blocked, A = Approval Required

### Tool and Capability Access

| Tool Category | L0 | L1 | L2 | L3 | L4 | Special Restrictions |
|---------------|----|----|----|----|-------|---------------------|
| **File System Operations** |
| Read Local Files | A | ✓ | ✓ | ✓ | ✓ | L0: Approval required |
| Write Local Files | A | A | ✓ | ✓ | ✓ | L0/L1: Approval required |
| Execute Scripts | ✗ | A | A | ✓ | ✓ | L1/L2: Sandboxed execution |
| **Network Operations** |
| HTTP GET Requests | ✓ | ✓ | ✓ | ✓ | ✓ | Rate limited |
| HTTP POST Requests | A | A | ✓ | ✓ | ✓ | L0/L1: Content inspection |
| FTP/SFTP Operations | ✗ | A | A | ✓ | ✓ | Destination whitelist |
| **System Integration** |
| Environment Variable Access | ✗ | ✗ | A | ✓ | ✓ | Sensitive vars redacted |
| Process Spawning | ✗ | ✗ | A | A | ✓ | Process restrictions |
| Container Operations | ✗ | ✗ | ✗ | A | A | Admin approval required |

### Data Handling Permissions

| Data Type | L0 | L1 | L2 | L3 | L4 | PII Sanitization |
|-----------|----|----|----|----|-------|------------------|
| **Personal Information** |
| Process User Data | A | A | ✓ | ✓ | ✓ | Always enabled |
| Store User Data | ✗ | A | A | ✓ | ✓ | Required |
| Transmit User Data | ✗ | A | A | A | ✓ | Required + approval |
| **Financial Information** |
| View Financial Data | ✗ | ✗ | A | A | ✓ | Enhanced sanitization |
| Process Transactions | ✗ | ✗ | ✗ | A | A | Multi-approval required |
| **Healthcare Information** |
| Access Medical Records | ✗ | ✗ | A | A | ✓ | HIPAA compliance mode |
| Generate Medical Advice | ✗ | ✗ | ✗ | A | A | Medical professional approval |

## Trust Level Progression Rules

### Automatic Progression Criteria

#### Level 0 → Level 1
```yaml
criteria:
  minimum_duration: 7 days
  successful_operations: 100
  security_violations: 0
  approval_compliance_rate: 95%
  behavioral_consistency_score: 80%
```

#### Level 1 → Level 2  
```yaml
criteria:
  minimum_duration: 14 days
  successful_operations: 500
  security_violations: 0
  approval_compliance_rate: 98%
  behavioral_consistency_score: 85%
  peer_rating: 3.5/5.0
```

#### Level 2 → Level 3
```yaml
criteria:
  minimum_duration: 30 days
  successful_operations: 2000
  security_violations: 0
  approval_compliance_rate: 99%
  behavioral_consistency_score: 90%
  peer_rating: 4.0/5.0
  complexity_handling_score: 85%
```

#### Level 3 → Level 4
```yaml
criteria:
  minimum_duration: 60 days
  successful_operations: 5000
  security_violations: 0
  approval_compliance_rate: 99.5%
  behavioral_consistency_score: 95%
  peer_rating: 4.5/5.0
  complexity_handling_score: 90%
  manual_verification: required
```

### Trust Degradation Rules

#### Security Violation Penalties
```yaml
violation_types:
  prompt_injection_attempt: -20 points, level_cap: 1
  unauthorized_access_attempt: -30 points, level_cap: 0  
  pii_exposure: -25 points, level_cap: 1
  policy_violation: -15 points
  failed_approval_compliance: -10 points
  suspicious_behavior_pattern: -5 points
```

#### Recovery Timeframes
- **Minor Violations** (5-10 points): 7 days clean behavior
- **Moderate Violations** (11-20 points): 14 days clean behavior  
- **Major Violations** (21+ points): 30 days clean behavior + manual review

## MCP Proxy Tool Authorization

### Tool Categories and Trust Requirements

#### Category A: Safe Operations (All Levels)
```yaml
tools:
  - web_search
  - calculator
  - weather_info
  - timezone_converter
  - text_formatter
restrictions: rate_limiting_only
```

#### Category B: Standard Operations (L1+)
```yaml
tools:
  - file_reader
  - image_analyzer  
  - document_generator
  - data_visualizer
restrictions: content_filtering, rate_limiting
```

#### Category C: Privileged Operations (L2+)
```yaml
tools:
  - email_sender
  - file_writer
  - api_client
  - database_query
restrictions: approval_queue, content_inspection
```

#### Category D: Administrative Operations (L3+)
```yaml
tools:
  - system_command
  - process_manager
  - network_scanner
  - security_analyzer
restrictions: approval_queue, audit_logging, sandbox_execution
```

#### Category E: Critical Operations (L4 + Manual Approval)
```yaml
tools:
  - container_manager
  - credential_manager
  - backup_controller
  - security_config_manager
restrictions: multi_approval, full_audit, admin_oversight
```

### Dynamic Permission Adjustment

SecureClaw continuously monitors agent behavior and can dynamically adjust permissions:

```python
def adjust_permissions(agent_id: str, trust_score: float, recent_behavior: Dict):
    adjustments = {}
    
    # Recent security violations reduce permissions
    if recent_behavior.get('security_violations', 0) > 0:
        adjustments['tool_access_level'] = min(current_level - 1, 0)
        adjustments['approval_threshold'] = 'strict'
    
    # Exceptional performance can grant temporary elevated access
    if recent_behavior.get('exceptional_performance', False):
        adjustments['temporary_elevation'] = True
        adjustments['elevation_duration'] = timedelta(hours=24)
    
    # Resource usage patterns affect limitations
    if recent_behavior.get('resource_usage', 0) > 0.8:
        adjustments['rate_limits'] = 'restrictive'
    
    return adjustments
```

This comprehensive access control matrix ensures SecureClaw provides appropriate security boundaries while enabling agent functionality based on demonstrated trustworthiness and operational requirements.