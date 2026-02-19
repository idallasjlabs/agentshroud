# SecureClaw Sequence Diagrams

This document shows the interaction sequences for key SecureClaw operations using ASCII sequence diagrams.

## 1. Normal Message Flow

Standard user message processing through the SecureClaw gateway.

```
User    Gateway    Sanitizer    Audit     OpenClaw    Audit     User
 │         │           │         │          │         │         │
 │──msg───▶│           │         │          │         │         │
 │         │──────────▶│         │          │         │         │
 │         │           │─clean──▶│          │         │         │
 │         │           │         │──log────▶│         │         │
 │         │           │         │          │◀─resp───│         │
 │         │           │         │          │         │         │
 │         │           │         │◀────audit│         │         │
 │         │           │         │          │         │         │
 │◀─resp──┤           │         │          │         │         │
 │         │           │         │          │         │         │

Timeline:
1. User sends message to Gateway
2. Gateway forwards to PII Sanitizer
3. Sanitizer removes PII, forwards to Audit
4. Audit logs incoming message, forwards to OpenClaw
5. OpenClaw processes and responds
6. Response logged by Audit system
7. Clean response returned to User
```

## 2. MCP Tool Call Flow

AI agent requesting to use an external tool through MCP proxy.

```
Agent    MCPProxy   PermChk    RateLimit   MCPServer   Audit    Agent
  │         │         │          │           │         │        │
  │─tool───▶│         │          │           │         │        │
  │         │──check─▶│          │           │         │        │
  │         │◀──ok───┤          │           │         │        │
  │         │─────────┼─limit───▶│           │         │        │
  │         │◀────────┼───ok────┤           │         │        │
  │         │─────────┼──────────┼─forward──▶│         │        │
  │         │◀────────┼──────────┼─response─┤         │        │
  │         │─────────┼──────────┼───────────┼─audit──▶│        │
  │         │─inspect─┼──────────┼───────────┼─────────│        │
  │◀─result┤         │          │           │         │        │
  │         │         │          │           │         │        │

Error Flow (Permission Denied):
Agent    MCPProxy   PermChk    Audit      Agent
  │         │         │         │          │
  │─tool───▶│         │         │          │
  │         │──check─▶│         │          │
  │         │◀─deny──┤         │          │
  │         │─────────┼─audit──▶│          │
  │◀─error─┤         │         │          │
  │         │         │         │          │

Timeline:
1. Agent requests tool execution
2. MCP Proxy checks permissions
3. Rate limiting validation
4. Forward to MCP Server if allowed
5. Inspect and sanitize response
6. Log all actions to audit
7. Return result (or error) to Agent
```

## 3. Kill Switch Activation Flow

Emergency shutdown sequence when kill switch is triggered.

```
Admin    Dashboard    KillSw    Gateway    Audit    OpenClaw   Notify
  │         │           │         │         │         │         │
  │─PANIC──▶│           │         │         │         │         │
  │         │──trigger─▶│         │         │         │         │
  │         │           │─block──▶│         │         │         │
  │         │           │         │──stop──▶│         │         │
  │         │           │         │         │─audit──▶│         │
  │         │           │         │         │         │──alert─▶│
  │         │           │         │         │         │         │
  │◀─ack───┤           │         │         │         │         │
  │         │           │         │         │         │         │

Cascade Effect:
KillSw   Gateway   MCPProxy   WebProxy   SSHProxy   Audit
  │        │         │          │          │         │
  │─block─▶│         │          │          │         │
  │        │─stop───▶│          │          │         │
  │        │─stop────┼─────────▶│          │         │
  │        │─stop────┼──────────┼─────────▶│         │
  │        │─────────┼──────────┼──────────┼─log────▶│
  │        │         │          │          │         │

States:
- SOFT_KILL: Block new requests, allow existing to complete
- HARD_KILL: Terminate all active connections immediately  
- PANIC: Emergency shutdown with minimal logging

Timeline:
1. Admin triggers kill switch via dashboard
2. Kill switch immediately blocks Gateway
3. All proxy services receive stop signals
4. OpenClaw container is halted
5. Emergency audit entry created
6. Notification system alerts ops team
7. System enters safe state
```

## 4. SSH Command Flow

AI agent executing SSH commands through the SSH proxy with security checks.

```
Agent   SSHProxy   Inject    Approval   Executor   AuditSys   Agent
  │        │        Check      Queue        │         │       │
  │─ssh───▶│         │          │          │         │       │
  │        │──scan──▶│          │          │         │       │
  │        │◀─safe──┤          │          │         │       │
  │        │─────────┼─request─▶│          │         │       │
  │        │◀────────┼─pending─┤          │         │       │
  │        │         │          │          │         │       │
  │        │         │         ... WAIT FOR APPROVAL ...    │
  │        │         │          │          │         │       │
  │        │◀────────┼approved─┤          │         │       │
  │        │─────────┼──────────┼─execute─▶│         │       │
  │        │◀────────┼──────────┼─output──┤         │       │
  │        │─────────┼──────────┼─────────┼─log────▶│       │
  │◀─resp──┤         │          │          │         │       │
  │        │         │          │          │         │       │

High-Risk Command (Injection Detected):
Agent   SSHProxy   Inject    AuditSys   Agent
  │        │        Check        │       │
  │─ssh───▶│         │           │       │
  │        │──scan──▶│           │       │
  │        │◀─BLOCK─┤           │       │
  │        │─────────┼─log──────▶│       │
  │◀─error┤         │           │       │
  │        │         │           │       │

Auto-Approved (Trusted Agent):
Agent   SSHProxy   Inject    TrustMgr   Executor   Agent
  │        │        Check       │         │        │
  │─ssh───▶│         │          │         │        │
  │        │──scan──▶│          │         │        │
  │        │◀─safe──┤          │         │        │
  │        │─────────┼─check───▶│         │        │
  │        │◀────────┼─trusted─┤         │        │
  │        │─────────┼─────────┼─exec───▶│        │
  │◀─resp──┤         │          │         │        │

Timeline:
1. Agent submits SSH command
2. Injection checker scans for malicious patterns
3. Safe commands go to approval queue
4. Manual/auto approval based on trust level
5. Approved commands executed on target system
6. All actions logged to audit system
7. Sanitized output returned to agent
```

## 5. Web Fetch Flow

AI agent fetching web content through the web proxy with URL analysis and content scanning.

```
Agent   WebProxy   URLAnalyz   DNSCheck   WebFetch   ContentScan   Agent
  │        │         │           │          │           │         │
  │─fetch─▶│         │           │          │           │         │
  │        │─analyze▶│           │          │           │         │
  │        │◀─safe──┤           │          │           │         │
  │        │─────────┼─resolve──▶│          │           │         │
  │        │◀────────┼─allowed──┤          │           │         │
  │        │─────────┼───────────┼─request─▶│           │         │
  │        │◀────────┼───────────┼─content─┤           │         │
  │        │─────────┼───────────┼─────────┼─scan─────▶│         │
  │        │◀────────┼───────────┼─────────┼─clean────┤         │
  │◀─data──┤         │           │          │           │         │
  │        │         │           │          │           │         │

Blocked URL Flow:
Agent   WebProxy   URLAnalyz   AuditSys   Agent
  │        │         │           │         │
  │─fetch─▶│         │           │         │
  │        │─analyze▶│           │         │
  │        │◀─BLOCK─┤           │         │
  │        │─────────┼─log──────▶│         │
  │◀─error┤         │           │         │
  │        │         │           │         │

SSRF Protection:
Agent   WebProxy   URLAnalyz   DNSCheck   Agent
  │        │         │           │         │
  │─fetch─▶│         │           │         │
  │        │─analyze▶│           │         │
  │        │◀─check─┤           │         │
  │        │─────────┼─resolve──▶│         │
  │        │◀────────┼─PRIVATE──┤         │
  │◀─error┤         │           │         │
  │        │         │           │         │

Content Scanning:
WebFetch   ContentScan   AuditSys   Result
    │           │          │         │
    │─content──▶│          │         │
    │           │─malware─▶│         │
    │           │─pii─────▶│         │
    │           │─size────▶│         │
    │◀─clean───┤          │         │
    │           │          │         │

Timeline:
1. Agent requests web fetch
2. URL analyzer checks for known threats
3. DNS checker prevents private IP access (SSRF)
4. Web fetcher retrieves content
5. Content scanner removes malware/PII
6. All actions logged to audit
7. Clean content returned to agent

Security Checks:
- URL reputation analysis
- SSRF protection (private IP blocking)
- Content-type validation
- Malware scanning
- PII redaction
- Size limits enforcement
```

These sequence diagrams show how SecureClaw maintains security at every step of the interaction flow, with multiple checkpoints and comprehensive audit logging for all operations.