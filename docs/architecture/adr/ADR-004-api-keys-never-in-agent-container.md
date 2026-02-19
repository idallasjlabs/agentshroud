# ADR-004: API Keys Never in Agent Container

## Status
**Accepted** - December 2025

## Context

OpenClaw agents require API keys for external services (LLM providers, search APIs, etc.). Key management approaches:

1. **Agent-Side Storage**: Store API keys directly in agent containers
2. **Proxy-Side Storage**: Store keys in AgentShroud, proxy adds them to requests
3. **External Secrets Manager**: Use vault systems for key retrieval

## Decision

Implement **Proxy-Side API Key Management**:
- All API keys stored only in AgentShroud containers
- Agent containers never have direct access to production API keys  
- AgentShroud automatically injects appropriate keys based on request destination
- Key rotation handled transparently without agent updates

### Implementation
```yaml
# AgentShroud Configuration
api_keys:
  openai: ${VAULT_SECRET_OPENAI_KEY}
  anthropic: ${VAULT_SECRET_ANTHROPIC_KEY}
  brave_search: ${VAULT_SECRET_BRAVE_KEY}

key_injection_rules:
  - pattern: "api.openai.com/*"
    key: openai
    header: "Authorization: Bearer {key}"
  - pattern: "api.anthropic.com/*"  
    key: anthropic
    header: "x-api-key: {key}"
```

## Consequences

### Positive Consequences
- **Credential Isolation**: Compromised agents cannot access API keys
- **Centralized Key Management**: Single point for key rotation and auditing
- **Audit Trail**: All API key usage logged with full context
- **Zero-Trust Model**: Agents operate with minimal privileges

### Negative Consequences
- **Proxy Dependency**: Agents cannot function without AgentShroud for external API calls
- **Key Mapping Complexity**: Must maintain mappings between services and keys
- **Performance Overhead**: Additional processing for key injection

### Mitigation
- High-availability proxy deployment
- Automated key rotation with rollback capability
- Optimized key injection with minimal latency impact