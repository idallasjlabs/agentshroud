# ADR-007: Zero-Config Security (docker-compose up = fully secured)

## Status
**Accepted** - December 2025

## Context

AgentShroud must be deployable with minimal configuration while achieving full security posture.

## Decision

Implement **Zero-Configuration Security** with intelligent defaults:

```bash
# Complete secure deployment in one command
docker-compose up -d
```

### Auto-Configuration Features
- Network isolation with secure defaults
- Pre-configured security policies for common threats
- Automatic SSL/TLS certificate generation
- Default audit logging and retention policies
- Trust level baseline establishment
- Health monitoring activation

### Configuration Hierarchy
1. **Hardcoded Defaults**: Secure baseline configuration
2. **Environment Detection**: Adapt to runtime environment
3. **Environment Variables**: Optional override mechanism
4. **Config Files**: Advanced customization for experts

## Consequences

### Positive Consequences
- **Ease of Adoption**: Immediate security benefits without expertise
- **Reduced Errors**: Eliminates common configuration mistakes
- **Faster Deployment**: Production-ready in minutes

### Negative Consequences
- **Less Flexibility**: Advanced users may need configuration overrides
- **Magic Behavior**: Auto-configuration may be unclear to operators

### Mitigation
- Comprehensive documentation of auto-configuration decisions
- Configuration discovery endpoints for transparency
- Override mechanisms for advanced use cases