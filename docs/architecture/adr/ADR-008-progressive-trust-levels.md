# ADR-008: Progressive Trust Levels for Agents

## Status
**Accepted** - December 2025

## Context

AgentShroud must balance security controls with agent functionality, adapting restrictions based on observed behavior.

## Decision

Implement **Progressive Trust Level System** with behavioral adaptation:

### Trust Levels (0-4)
- **Level 0**: New/untrusted agents - Maximum restrictions
- **Level 1**: Basic trust - Limited tool access, high monitoring
- **Level 2**: Established trust - Standard operations allowed
- **Level 3**: High trust - Advanced capabilities, reduced oversight
- **Level 4**: Verified trust - Minimal restrictions, autonomous operation

### Trust Calculation
```python
trust_score = base_score 
            + behavioral_history_score
            + compliance_score
            - security_violations_penalty
            - anomaly_detection_penalty
```

### Progressive Controls
```
Level 0: All actions → Approval Queue
Level 1: High-risk actions → Approval Queue  
Level 2: Suspicious actions → Approval Queue
Level 3: Clear threats only → Block
Level 4: Monitor only → Log everything
```

## Consequences

### Positive Consequences
- **Adaptive Security**: Controls adjust to agent risk profile
- **Operational Efficiency**: Trusted agents operate with minimal friction
- **Behavioral Learning**: System learns normal vs. anomalous patterns

### Negative Consequences
- **Complexity**: Trust calculation requires sophisticated modeling
- **Gaming Risk**: Malicious agents might try to game trust scores

### Mitigation
- Multi-factor trust calculation with anomaly detection
- Periodic trust level re-evaluation
- Human oversight for trust level promotions