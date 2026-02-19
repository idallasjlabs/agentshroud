# ADR-001: Transparent Proxy vs Agent Modification

## Status
**Accepted** - December 2025

## Context

AgentShroud requires a mechanism to provide security controls for OpenClaw AI agents. Two primary approaches were considered:

1. **Agent Modification Approach**: Integrate security controls directly into the OpenClaw agent codebase
2. **Transparent Proxy Approach**: Implement security controls as an external proxy layer

### Key Considerations

#### Agent Modification Pros:
- Direct access to agent internal state and decision processes
- Lower latency due to in-process security checks
- Tighter integration with agent memory and reasoning systems
- Simplified deployment (single container)

#### Agent Modification Cons:
- Requires ongoing maintenance with OpenClaw updates
- Increases agent complexity and potential attack surface
- Difficult to audit security controls independently
- Couples security policy with agent logic
- Requires security expertise from agent developers
- Breaks compatibility with existing OpenClaw deployments

#### Transparent Proxy Pros:
- Zero modification required for existing OpenClaw installations
- Clear separation of concerns between security and agent functionality
- Independent security policy management and updates
- Auditable security controls isolated from agent logic
- Supports multiple OpenClaw versions without modification
- Security team can manage policies without agent expertise

#### Transparent Proxy Cons:
- Additional network hop introduces latency
- Limited visibility into agent internal decision processes
- More complex deployment architecture
- Potential for proxy bypass if misconfigured

## Decision

We choose the **Transparent Proxy** approach for the following reasons:

1. **Compatibility**: Maintains complete compatibility with existing OpenClaw deployments
2. **Separation of Concerns**: Security policies can evolve independently of agent functionality
3. **Maintainability**: Updates to OpenClaw do not require security code modifications
4. **Auditability**: Clear security boundary enables independent security audits
5. **Operational Excellence**: Security teams can manage policies without understanding agent internals
6. **Deployment Flexibility**: Supports gradual rollout and A/B testing of security policies

### Implementation Strategy

The transparent proxy will:
- Intercept all HTTP/HTTPS traffic to and from OpenClaw agents
- Provide protocol-specific proxies for SSH, MCP, and other protocols
- Implement security controls as middleware in the proxy chain
- Maintain complete request/response fidelity to preserve agent functionality
- Use Docker network isolation to ensure all traffic flows through the proxy

## Consequences

### Positive Consequences
- **Rapid Adoption**: Existing OpenClaw users can add AgentShroud without code changes
- **Security Focus**: Security team can focus on security controls without agent domain knowledge
- **Independent Evolution**: Agent and security features can evolve independently
- **Clear Audit Trail**: All security decisions are external to the agent and fully auditable
- **Deployment Flexibility**: Can be deployed as a sidecar or standalone proxy

### Negative Consequences
- **Latency Overhead**: Additional network hop adds 1-3ms per request
- **Operational Complexity**: Requires managing proxy infrastructure and network configuration
- **Limited Agent Visibility**: Cannot directly access agent memory or reasoning processes
- **Potential Single Point of Failure**: Proxy must be highly available to avoid agent downtime

### Mitigation Strategies
- **Latency**: Implement high-performance async proxy with connection pooling
- **High Availability**: Support proxy clustering and failover mechanisms
- **Monitoring**: Comprehensive metrics and alerting for proxy health
- **Network Isolation**: Use Docker networks to prevent proxy bypass

### Risk Assessment
- **Low Risk**: Network latency impact is acceptable for agent workloads
- **Medium Risk**: Proxy availability must be carefully managed
- **Low Risk**: Security policy management is simplified by external implementation

This decision establishes AgentShroud as a transparent security layer that enhances OpenClaw deployments without requiring agent modifications, enabling rapid adoption while maintaining clear security boundaries.