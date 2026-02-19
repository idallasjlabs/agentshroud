# Use Cases
## AgentShroud Security Proxy

### Overview
This document describes the primary use cases for AgentShroud, detailing how the system protects AI agents through various security scenarios. Each use case includes actors, preconditions, main flow, alternate flows, and postconditions.

---

## UC-001: User Sends Message to Agent (PII Sanitization Flow)

**Actors**: End User, AgentShroud Proxy, AI Agent, Security Operator

**Preconditions**:
- AgentShroud proxy is running and configured
- AI agent is connected through proxy
- PII detection patterns are loaded
- User has valid session

**Main Flow**:
1. User submits message containing PII (e.g., "My SSN is 123-45-6789")
2. AgentShroud intercepts the message at ingestion endpoint
3. PII detection module scans message content
4. System identifies SSN pattern and flags for redaction
5. PII is replaced with placeholder: "My SSN is [REDACTED:SSN]"
6. Original message hash is stored in audit trail
7. Sanitized message is forwarded to AI agent
8. AI agent processes sanitized message and responds
9. Response is scanned for PII leakage
10. Clean response is returned to user

**Alternate Flows**:
- **A1**: No PII detected - message passes through without modification
- **A2**: Multiple PII types detected - all patterns redacted with appropriate labels
- **A3**: PII detection fails - message is quarantined for manual review

**Postconditions**:
- User message is processed safely without PII exposure
- Audit record created with sanitization details
- AI agent remains unaware of original PII content

---

## UC-002: Agent Calls MCP Tool (Inspection + Permission Check)

**Actors**: AI Agent, AgentShroud Proxy, MCP Server, Security Operator

**Preconditions**:
- MCP proxy is active and configured
- AI agent has established MCP connection
- Tool permissions policy is loaded
- Agent trust level is established

**Main Flow**:
1. AI agent requests to call file system tool via MCP
2. AgentShroud MCP proxy intercepts the tool call
3. System validates tool permissions against agent trust level
4. Tool parameters are inspected for malicious patterns
5. Path traversal detection scans file path parameters
6. Approval required check evaluates tool risk level
7. Tool call is logged to audit trail
8. Validated tool call is forwarded to MCP server
9. MCP server executes tool and returns results
10. Results are scanned for sensitive information
11. Sanitized results returned to AI agent

**Alternate Flows**:
- **A1**: Tool call denied - agent receives permission error
- **A2**: Approval required - tool call queued for human approval
- **A3**: Malicious parameters detected - tool call blocked and alert generated
- **A4**: Tool execution fails - error logged and propagated to agent

**Postconditions**:
- Tool execution completed safely within policy boundaries
- Complete audit trail of tool usage maintained
- Security violations prevented and documented

---

## UC-003: Agent Fetches Web Content (SSRF Check + Content Scan)

**Actors**: AI Agent, AgentShroud Proxy, Web Server, Security Analyst

**Preconditions**:
- Web proxy module is enabled
- SSRF protection rules are loaded
- Content scanning engines are active
- Agent has web access permissions

**Main Flow**:
1. AI agent requests web content from external URL
2. AgentShroud web proxy receives the request
3. URL is validated against SSRF protection rules
4. Domain reputation check performed against threat feeds
5. DNS resolution validated to prevent internal network access
6. HTTP request forwarded to target server
7. Response content received and buffered
8. Content scanning for malware and suspicious patterns
9. Response headers sanitized to remove sensitive information
10. Validated content delivered to AI agent

**Alternate Flows**:
- **A1**: SSRF attempt detected - request blocked and security alert generated
- **A2**: Malicious content detected - response quarantined and notification sent
- **A3**: Rate limit exceeded - request throttled with appropriate error
- **A4**: Domain on blocklist - access denied with policy violation logged

**Postconditions**:
- Safe web content delivered to agent
- Security threats blocked and documented
- Network security maintained

---

## UC-004: Admin Activates Kill Switch

**Actors**: Security Administrator, AgentShroud Proxy, AI Agent, Monitoring System

**Preconditions**:
- Administrator has kill switch privileges
- AgentShroud is in operational state
- Monitoring systems are active
- Emergency notification channels configured

**Main Flow**:
1. Administrator detects security incident requiring immediate shutdown
2. Kill switch endpoint is activated via API or dashboard
3. AgentShroud immediately blocks all new agent requests
4. Active agent sessions are terminated gracefully
5. All proxy modules enter shutdown mode
6. Emergency notifications sent to configured channels
7. System state is persisted for post-incident analysis
8. Audit entry created with kill switch activation details
9. System enters safe mode awaiting manual intervention

**Alternate Flows**:
- **A1**: Automated kill switch triggered by threat detection
- **A2**: Partial kill switch affecting specific agents only
- **A3**: Kill switch fails - fallback to hard shutdown procedures

**Postconditions**:
- All agent operations safely terminated
- System in secure shutdown state
- Incident response team notified
- Complete audit trail preserved

---

## UC-005: Agent Requests SSH Access (Approval Queue)

**Actors**: AI Agent, AgentShroud Proxy, Security Operator, Target SSH Server

**Preconditions**:
- SSH proxy module is configured
- Approval queue system is active
- Security operators are available
- Agent has conditional SSH permissions

**Main Flow**:
1. AI agent requests SSH connection to remote server
2. AgentShroud SSH proxy receives connection request
3. Agent trust level and SSH permissions evaluated
4. Request requires human approval based on policy
5. SSH request queued in approval system
6. Notification sent to security operators
7. Operator reviews request details and context
8. Approval granted with time-limited session
9. SSH connection established with full logging
10. All SSH commands and outputs recorded
11. Session terminated at policy timeout

**Alternate Flows**:
- **A1**: Request automatically approved for high-trust agents
- **A2**: Request denied by operator with reason documented
- **A3**: Request times out without approval - automatically denied
- **A4**: SSH connection fails - failure logged and reported

**Postconditions**:
- SSH access controlled through approval process
- Complete session recording maintained
- Security policies enforced consistently

---

## UC-006: Security Alert Triggers Notification

**Actors**: AgentShroud Monitoring System, Security Operations Center, AI Agent, Threat Detection Engine

**Preconditions**:
- Threat detection engines are active
- Notification channels configured
- Alert severity thresholds defined
- On-call personnel identified

**Main Flow**:
1. Threat detection engine identifies suspicious agent behavior
2. Alert severity calculated based on threat indicators
3. Alert details compiled including context and evidence
4. Notification routing determined by severity and time
5. Immediate notification sent via configured channels
6. Alert details logged to security incident system
7. Automated response actions triggered if configured
8. Security team acknowledges and begins investigation
9. Alert status updated as investigation progresses

**Alternate Flows**:
- **A1**: False positive detected - alert suppressed and pattern updated
- **A2**: Critical alert - escalation to senior security staff
- **A3**: Notification delivery fails - retry with backup channels

**Postconditions**:
- Security team aware of potential threats
- Investigation initiated and documented
- System response actions completed

---

## UC-007: New Agent Onboarding (Trust Level 0)

**Actors**: New AI Agent, AgentShroud Proxy, System Administrator, Trust Management System

**Preconditions**:
- AgentShroud proxy is operational
- Trust management policies configured
- New agent authentication credentials prepared
- Onboarding procedures documented

**Main Flow**:
1. New AI agent connects to AgentShroud proxy
2. Agent authentication and identity verification
3. Trust level initialized to 0 (untrusted)
4. Restrictive security policies applied automatically
5. Agent limited to basic operations requiring approval
6. All agent actions monitored with enhanced logging
7. Trust score gradually increases based on behavior
8. Security restrictions relaxed as trust improves
9. Full operational status achieved at sufficient trust level

**Alternate Flows**:
- **A1**: Agent authentication fails - connection rejected
- **A2**: Agent exhibits suspicious behavior - trust level decreased
- **A3**: Manual trust override by administrator

**Postconditions**:
- New agent safely integrated with appropriate restrictions
- Trust trajectory established for future operations
- Security posture maintained during onboarding

---

## UC-008: Operator Reviews Audit Trail

**Actors**: Security Operator, AgentShroud Audit System, Compliance Officer

**Preconditions**:
- Audit trail system operational
- Operator has audit access permissions
- Audit data integrity verified
- Search and filtering tools available

**Main Flow**:
1. Operator accesses audit trail dashboard
2. Time range and filter criteria specified
3. Audit records retrieved and displayed
4. Hash chain integrity verification performed
5. Suspicious patterns and anomalies highlighted
6. Detailed investigation of flagged events
7. Export audit data for compliance reporting
8. Summary report generated for management

**Alternate Flows**:
- **A1**: Audit integrity violation detected - investigation initiated
- **A2**: Large dataset - results paginated for performance
- **A3**: Export fails - data integrity check and retry

**Postconditions**:
- Audit review completed and documented
- Compliance requirements satisfied
- Security posture assessed and improved

---

## UC-009: System Detects Prompt Injection

**Actors**: AI Agent, AgentShroud Proxy, Threat Detection Engine, Security Analyst

**Preconditions**:
- Prompt injection detection models loaded
- AI agent actively communicating
- Security policies configured
- Alert systems operational

**Main Flow**:
1. User submits message with embedded prompt injection
2. AgentShroud ingestion process receives message
3. Prompt injection detection engine analyzes content
4. Malicious prompt patterns identified with confidence score
5. Message blocked before reaching AI agent
6. Security alert generated with attack details
7. User receives generic error message
8. Incident logged for security analysis
9. Detection models updated based on new pattern

**Alternate Flows**:
- **A1**: Borderline detection - message flagged for manual review
- **A2**: Sophisticated injection bypasses detection - post-processing analysis
- **A3**: False positive - whitelist pattern added after review

**Postconditions**:
- Prompt injection attack blocked successfully
- AI agent protected from manipulation
- Security intelligence improved

---

## UC-010: Multi-Instance Deployment with Port Auto-Detection

**Actors**: DevOps Engineer, Container Orchestrator, AgentShroud Instances, Load Balancer

**Preconditions**:
- Container platform operational
- AgentShroud container images available
- Network configuration supports multi-instance
- Service discovery mechanism configured

**Main Flow**:
1. DevOps engineer initiates multi-instance deployment
2. Container orchestrator creates multiple AgentShroud instances
3. Each instance performs port availability scan
4. Unique ports automatically assigned to avoid conflicts
5. Service discovery registration with assigned ports
6. Load balancer configuration updated automatically
7. Health checks verify all instances operational
8. Traffic distribution begins across instances
9. Monitoring confirms successful scaling

**Alternate Flows**:
- **A1**: Port conflicts detected - automatic reassignment
- **A2**: Instance startup fails - health check triggers restart
- **A3**: Load balancer update fails - manual intervention required

**Postconditions**:
- Multiple AgentShroud instances operational
- Traffic distributed evenly across instances
- High availability and scalability achieved
- Configuration consistency maintained across instances