# ADR-002: Default-Allow Security Philosophy

## Status
**Superseded** — see [ADR-009: Enforce-by-Default Security Philosophy](ADR-009-enforce-by-default.md)

*Original status: Accepted — December 2025. Superseded by ADR-009 — March 2026.*

## Context

AgentShroud must balance security protection with agent functionality. Two security philosophies were evaluated:

1. **Default-Deny**: Block all actions unless explicitly permitted (whitelist approach)
2. **Default-Allow**: Allow all actions while logging comprehensively, blocking only clear threats

### Evaluation Criteria
- Agent functionality preservation
- Security threat detection effectiveness
- Operational complexity
- False positive rates
- Compliance requirements

## Decision

We adopt a **Default-Allow with Comprehensive Logging** security philosophy:

- All agent actions are permitted by default
- Every action is logged with full context for audit trails
- Only clear, high-confidence threats are automatically blocked
- Suspicious activities trigger approval queues rather than automatic blocks
- Trust levels progressively restrict permissions based on agent behavior

### Implementation Approach
```
Action → Threat Analysis → Log Everything → Progressive Enforcement
                       ↓
         Clear Threat? ─Yes→ Block + Alert
                       ↓
                      No
                       ↓
         Suspicious? ─Yes→ Approval Queue
                       ↓
                      No
                       ↓
                    Allow + Log
```

## Consequences

### Positive Consequences
- **Preserved Functionality**: Agents maintain full capabilities without unexpected restrictions
- **Learning Phase**: System learns normal vs. suspicious behavior patterns
- **Reduced False Positives**: Human approval for ambiguous cases prevents blocking legitimate actions
- **Comprehensive Audit**: Complete visibility into all agent activities
- **Gradual Hardening**: Security can be progressively tightened based on observed threats

### Negative Consequences
- **Initial Exposure**: Some threats may succeed during learning phase
- **Human Oversight Required**: Approval queues require human intervention
- **Storage Requirements**: Comprehensive logging requires significant storage
- **Alert Fatigue**: High volume of logged events may overwhelm analysts

### Mitigation Strategies
- Implement ML-based threat scoring to improve detection accuracy
- Automated approval for low-risk, repetitive actions
- Log retention policies with automated archiving
- Intelligent alerting with threat prioritization

This philosophy enables AgentShroud to protect against threats while preserving agent capabilities and building intelligence for future enforcement.