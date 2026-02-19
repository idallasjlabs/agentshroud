# AgentShroud State Diagrams

This document illustrates the state machines that govern AgentShroud's security and operational behavior.

## 1. Agent Trust Levels

Agent trust levels determine what actions an AI agent can perform and how much oversight is required.

```
                    ┌─────────────────────────────────────────┐
                    │                                         │
                    ▼                                         │
    ┌───────────────────────┐                                │
    │                       │    violation_detected()        │
    │   Level 0:            │                                │
    │   UNTRUSTED           │◀───────────────────────────────┤
    │                       │                                │
    │   • All actions blocked│                                │
    │   • Manual approval    │                                │
    │   • Heavy monitoring   │                                │
    └───────────────────────┘                                │
                    │                                         │
                    │ initial_assessment()                    │
                    ▼                                         │
    ┌───────────────────────┐                                │
    │                       │                                │
    │   Level 1:            │                                │
    │   BASIC               │                                │
    │                       │                                │
    │   • Read-only access  │                                │
    │   • No external calls │                                │
    │   • All actions logged│                                │
    └───────────────────────┘                                │
                    │                                         │
                    │ trust_earned()                          │
                    │ (100+ safe actions)                     │
                    ▼                                         │
    ┌───────────────────────┐                                │
    │                       │    major_violation()           │
    │   Level 2:            │                                │
    │   STANDARD            │────────────────────────────────┤
    │                       │                                │
    │   • MCP tool access   │                                │
    │   • Web fetch allowed │                                │
    │   • Rate limited      │                                │
    └───────────────────────┘                                │
                    │                                         │
                    │ proven_reliable()                       │
                    │ (1000+ safe actions)                    │
                    ▼                                         │
    ┌───────────────────────┐                                │
    │                       │    security_incident()         │
    │   Level 3:            │                                │
    │   TRUSTED             │────────────────────────────────┤
    │                       │                                │
    │   • SSH access allowed│                                │
    │   • Higher rate limits│                                │
    │   • Auto-approval     │                                │
    └───────────────────────┘                                │
                    │                                         │
                    │ admin_promotion()                       │
                    │ (manual decision)                       │
                    ▼                                         │
    ┌───────────────────────┐                                │
    │                       │    admin_demotion()            │
    │   Level 4:            │                                │
    │   ADMIN               │────────────────────────────────┘
    │                       │
    │   • Full system access│
    │   • Can modify config │
    │   • Kill switch access│
    └───────────────────────┘

State Transitions:
┌─────────────────┬──────────────────────────────────────────┬────────────────┐
│ Trigger         │ Condition                                │ Action         │
├─────────────────┼──────────────────────────────────────────┼────────────────┤
│ initial_assessment() │ New agent deployed                 │ 0 → 1          │
│ trust_earned()  │ 100+ actions, 0 violations, 7+ days     │ 1 → 2          │
│ proven_reliable()│ 1000+ actions, <5% violation rate       │ 2 → 3          │
│ admin_promotion()│ Manual decision by ops team             │ 3 → 4          │
│ violation_detected()│ Any security violation detected      │ Any → 0        │
│ major_violation()│ Serious security breach                 │ 2,3,4 → 0      │
│ security_incident()│ Critical security event               │ 3,4 → 0        │
│ admin_demotion()│ Manual decision or policy violation      │ 4 → 3          │
└─────────────────┴──────────────────────────────────────────┴────────────────┘

Violation Examples:
- Level 0 Reset: Prompt injection, PII leak, malicious tool use
- Major Violation: Attempting privilege escalation, data exfiltration
- Security Incident: Container escape attempt, audit log tampering
```

## 2. Kill Switch States

The kill switch provides emergency shutdown capabilities with different levels of restriction.

```
                           system_start()
                                 │
                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                   ACTIVE                                │
    │                                                         │
    │   • Normal operation                                    │
    │   • All features enabled                                │
    │   • Full traffic processing                             │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                                 │
                                 │ trigger_soft_kill()
                                 │ (suspicious activity)
                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                 SOFT_KILL                               │
    │                                                         │
    │   • Block new connections                               │
    │   • Allow existing requests to complete                 │
    │   • Enable enhanced monitoring                          │
    │   • Queue approval required for all actions             │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                         │                       │
                         │ escalate_to_hard()    │ admin_override()
                         │ (threat confirmed)    │ (false alarm)
                         ▼                       ▼
    ┌─────────────────────────────────┐     ┌─────────────────┐
    │                                 │     │                 │
    │           HARD_KILL             │     │    ACTIVE       │
    │                                 │     │                 │
    │   • Terminate all connections   │     │ (return to      │
    │   • Stop all agent processing   │     │  normal ops)    │
    │   • Block all external access   │     │                 │
    │   • Emergency audit logging     │     │                 │
    │                                 │     │                 │
    └─────────────────────────────────┘     └─────────────────┘
                         │
                         │ panic_mode()
                         │ (critical threat)
                         ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                    PANIC                                │
    │                                                         │
    │   • Immediate container shutdown                        │
    │   • Network isolation                                   │
    │   • Minimal emergency logging                           │
    │   • Requires manual intervention to recover             │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                                 │
                                 │ manual_recovery()
                                 │ (admin intervention)
                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                 RECOVERY                                │
    │                                                         │
    │   • System health checks                                │
    │   • Audit log verification                              │
    │   • Configuration validation                            │
    │   • Gradual service restoration                         │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                                 │
                                 │ system_healthy()
                                 │ (all checks pass)
                                 ▼
                      ┌─────────────────┐
                      │                 │
                      │     ACTIVE      │
                      │                 │
                      │ (normal ops     │
                      │  restored)      │
                      │                 │
                      └─────────────────┘

Trigger Conditions:
┌────────────────────┬─────────────────────────────────────────────────┐
│ Trigger            │ Condition                                       │
├────────────────────┼─────────────────────────────────────────────────┤
│ trigger_soft_kill()│ • Multiple failed auth attempts                │
│                    │ • Suspicious tool usage patterns               │
│                    │ • High volume of blocked requests               │
├────────────────────┼─────────────────────────────────────────────────┤
│ escalate_to_hard() │ • Confirmed security breach                     │
│                    │ • Critical system resource exhaustion          │
│                    │ • Audit log tampering detected                  │
├────────────────────┼─────────────────────────────────────────────────┤
│ panic_mode()       │ • Container escape attempt                      │
│                    │ • Network intrusion detected                    │
│                    │ • Data exfiltration in progress                 │
├────────────────────┼─────────────────────────────────────────────────┤
│ admin_override()   │ • Manual assessment determines false positive   │
│ manual_recovery()  │ • Ops team intervention required                │
│ system_healthy()   │ • All diagnostic checks pass                    │
└────────────────────┴─────────────────────────────────────────────────┘
```

## 3. Approval Queue States

The approval queue manages requests that require human oversight before execution.

```
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                  PENDING                                │
    │                                                         │
    │   • Request queued for review                           │
    │   • Agent blocked waiting for approval                  │
    │   • Timeout timer started                               │
    │   • Notification sent to reviewers                      │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                         │               │               │
            approve()    │               │ deny()        │ timeout()
                         ▼               ▼               ▼
    ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
    │                 │      │                 │      │                 │
    │    APPROVED     │      │     DENIED      │      │   TIMED_OUT     │
    │                 │      │                 │      │                 │
    │ • Execute action│      │ • Block action  │      │ • Auto-deny     │
    │ • Send to exec  │      │ • Log denial    │      │ • Log timeout   │
    │ • Monitor exec  │      │ • Notify agent  │      │ • Notify agent  │
    │                 │      │                 │      │                 │
    └─────────────────┘      └─────────────────┘      └─────────────────┘
                │                      │                      │
                │ execute()            │ archive()            │ archive()
                ▼                      ▼                      ▼
    ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
    │                 │      │                 │      │                 │
    │    EXECUTED     │      │    ARCHIVED     │      │    ARCHIVED     │
    │                 │      │                 │      │                 │
    │ • Action done   │      │ • Permanent     │      │ • Permanent     │
    │ • Result logged │      │   record kept   │      │   record kept   │
    │ • Audit entry   │      │ • Available for │      │ • Available for │
    │                 │      │   compliance    │      │   compliance    │
    └─────────────────┘      └─────────────────┘      └─────────────────┘
                │                      │                      │
                │ audit()              │                      │
                ▼                      │                      │
    ┌─────────────────┐                │                      │
    │                 │                │                      │
    │    AUDITED      │                │                      │
    │                 │                │                      │
    │ • Full audit    │                │                      │
    │   completed     │                │                      │
    │ • Archived      │                │                      │
    │                 │                │                      │
    └─────────────────┘                │                      │
                │                      │                      │
                │ archive()            │                      │
                ▼                      ▼                      ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                   ARCHIVED                              │
    │                                                         │
    │   • Permanent historical record                         │
    │   • Available for compliance audits                     │
    │   • Used for trust level calculations                   │
    │   • Immutable audit trail                               │
    │                                                         │
    └─────────────────────────────────────────────────────────┘

Queue Management Rules:
┌─────────────────────┬───────────────────────────────────────────────┐
│ Priority Level      │ Timeout Period                                │
├─────────────────────┼───────────────────────────────────────────────┤
│ LOW (file read)     │ 4 hours                                       │
│ MEDIUM (web fetch)  │ 2 hours                                       │
│ HIGH (SSH command)  │ 1 hour                                        │
│ CRITICAL (system)   │ 30 minutes                                    │
└─────────────────────┴───────────────────────────────────────────────┘

Auto-Approval Conditions:
- Agent trust level ≥ 3 (TRUSTED)
- Action type in whitelist
- No recent violations
- Within rate limits
- Off-hours exemption not required

Escalation Rules:
- CRITICAL requests: Immediate notification
- HIGH requests: 15-minute notification
- Multiple timeouts: Escalate to senior ops
- Pattern of denials: Review agent trust level
```

## 4. Gateway Operational Modes

The gateway operates in different modes based on threat level and system state.

```
                           system_init()
                                 │
                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                   MONITOR                               │
    │                                                         │
    │   • Log all traffic                                     │
    │   • No blocking (observe only)                          │
    │   • Learning mode for baselines                         │
    │   • Generate alerts but don't act                       │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                                 │
                                 │ enable_enforcement()
                                 │ (sufficient baseline data)
                                 ▼
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │                   ENFORCE                               │
    │                                                         │
    │   • Active security controls                            │
    │   • Block malicious requests                            │
    │   • Rate limiting enforced                              │
    │   • Normal operational mode                             │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
                         │                       │
                         │                       │ return_to_normal()
                         │ threat_detected()     │ (threat cleared)
                         ▼                       │
    ┌─────────────────────────────────┐         │
    │                                 │         │
    │           LOCKDOWN              │         │
    │                                 │         │
    │   • Maximum security posture    │         │
    │   • Block all non-essential     │         │
    │   • Human approval required     │         │
    │   • Emergency response active   │         │
    │                                 │         │
    └─────────────────────────────────┘         │
                         │                      │
                         │ system_compromised() │
                         │ (severe threat)      │
                         ▼                      │
    ┌─────────────────────────────────┐         │
    │                                 │         │
    │         EMERGENCY               │         │
    │                                 │         │
    │   • Kill switch activated       │         │
    │   • All traffic blocked         │         │
    │   • Container isolation         │         │
    │   • Manual recovery required    │         │
    │                                 │         │
    └─────────────────────────────────┘         │
                         │                      │
                         │ manual_recovery()    │
                         │ (admin intervention) │
                         ▼                      │
    ┌─────────────────────────────────┐         │
    │                                 │         │
    │          RECOVERY               │         │
    │                                 │         │
    │   • Gradual system restoration  │         │
    │   • Health check validation     │         │
    │   • Audit log verification      │         │
    │   • Component-by-component      │         │
    │                                 │         │
    └─────────────────────────────────┘         │
                         │                      │
                         │ validation_complete()│
                         │ (system healthy)     │
                         ▼                      │
                    ┌─────────────────┐         │
                    │                 │         │
                    │    ENFORCE      │◀────────┘
                    │                 │
                    │ (return to      │
                    │  normal ops)    │
                    │                 │
                    └─────────────────┘

Mode Characteristics:
┌─────────────┬─────────────────────────────────────────────────────────┐
│ Mode        │ Behavior                                                │
├─────────────┼─────────────────────────────────────────────────────────┤
│ MONITOR     │ • 100% traffic allowed                                  │
│             │ • Comprehensive logging                                 │
│             │ • Baseline establishment                                │
│             │ • No user impact                                        │
├─────────────┼─────────────────────────────────────────────────────────┤
│ ENFORCE     │ • Security policies active                              │
│             │ • Malicious content blocked                             │
│             │ • Performance optimized                                 │
│             │ • Standard operational mode                             │
├─────────────┼─────────────────────────────────────────────────────────┤
│ LOCKDOWN    │ • Strict security posture                               │
│             │ • Only whitelisted actions                              │
│             │ • Human oversight required                              │
│             │ • Reduced performance acceptable                        │
├─────────────┼─────────────────────────────────────────────────────────┤
│ EMERGENCY   │ • Complete traffic blocking                             │
│             │ • System protection priority                            │
│             │ • Manual intervention required                          │
│             │ • Service availability sacrificed                       │
├─────────────┼─────────────────────────────────────────────────────────┤
│ RECOVERY    │ • Controlled restoration                                │
│             │ • Extensive validation                                  │
│             │ • Conservative approach                                 │
│             │ • Monitoring emphasis                                   │
└─────────────┴─────────────────────────────────────────────────────────┘

These state diagrams ensure AgentShroud operates predictably and securely across all operational scenarios, with clear transitions and comprehensive audit trails for compliance and forensic analysis.
```