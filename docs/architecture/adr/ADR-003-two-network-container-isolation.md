# ADR-003: Two-Network Container Isolation

## Status
**Accepted** - December 2025

## Context

AgentShroud requires network isolation to prevent unauthorized access to OpenClaw agents. Container networking approaches evaluated:

1. **Single Network**: All containers on same Docker network with host-based firewalls
2. **Two-Network Isolation**: External + internal networks with AgentShroud as gateway
3. **Three-Network Architecture**: External + management + internal networks

## Decision

Implement **Two-Network Container Isolation** with:
- **External Network** (`secureclaw_external`): Internet-facing with AgentShroud Gateway
- **Internal Network** (`secureclaw_internal`): Isolated network for OpenClaw agents

### Network Configuration
```
External Network (172.20.0.0/24):
├── AgentShroud Gateway (172.20.0.2) - Dual-homed
├── Dashboard Web UI (172.20.0.3)
└── Metrics Collector (172.20.0.4)

Internal Network (172.21.0.0/24):
├── AgentShroud Gateway (172.21.0.2) - Dual-homed
├── OpenClaw Agent (172.21.0.3)
└── Agent Memory Store (172.21.0.4)
```

## Consequences

### Positive Consequences
- **Attack Surface Reduction**: OpenClaw agents have no direct external connectivity
- **Traffic Inspection**: All communication flows through AgentShroud security controls
- **Lateral Movement Prevention**: Compromised containers cannot reach external networks
- **Network-Level Policy Enforcement**: Docker network policies complement application security

### Negative Consequences
- **Complexity**: Requires careful network configuration and routing
- **Single Point of Failure**: Gateway failure isolates agents from external services
- **Debugging Difficulty**: Network isolation complicates troubleshooting

### Mitigation
- Gateway high availability with failover mechanisms
- Network monitoring and automated recovery
- Dedicated debugging network interfaces for troubleshooting