# AgentShroud Security Configuration

AgentShroud v0.7.0 implements **enforce-by-default** security with comprehensive protection against prompt injection, PII exposure, unauthorized tool access, and egress filtering.

## Security Modules

AgentShroud includes four core security modules that **default to enforcement mode**:

1. **PII Sanitizer (#1)** - Detects and redacts personally identifiable information
2. **Prompt Injection Defense (#8)** - Blocks malicious prompt injection attempts  
3. **Egress Filtering (#10)** - Controls outbound network traffic with domain allowlist
4. **MCP Proxy (#19)** - Enforces per-tool permissions for AI agent actions

## Monitor Mode Warning

**⚠️ CRITICAL SECURITY NOTICE**

AgentShroud defaults to **enforce mode** for core security modules. Running in monitor mode (`AGENTSHROUD_MODE=monitor` or per-module `mode: monitor`) disables active protection.

### In Monitor Mode, the following protections are DISABLED:

- **PII Exposure**: Credit cards, SSNs, emails pass through unredacted
- **Prompt Injection**: Malicious prompts are logged but not blocked  
- **Tool Access**: All MCP tool calls are permitted regardless of user trust level
- **Network Traffic**: Outbound requests to any domain are allowed

### When Monitor Mode is Appropriate

Monitor mode is intended for **initial deployment tuning ONLY**:

1. **Initial Setup**: Deploy in monitor mode for 1-2 weeks to establish baselines
2. **Threshold Tuning**: Observe false positive rates in logs
3. **Allowlist Building**: Identify legitimate domains and tools that need access
4. **Testing**: Development and testing environments where security is not required

### Production Requirements

**Never run monitor mode in production with real users.**

For production deployments:
- Remove `AGENTSHROUD_MODE=monitor` from environment variables
- Ensure all core modules have `mode: enforce` in configuration
- Regularly review security logs for blocked attempts
- Update allowlists only after thorough security review

## Development Override

For development environments, you can temporarily disable enforcement:

```bash
export AGENTSHROUD_MODE=monitor
```

Or in `docker-compose.yml`:
```yaml
services:
  gateway:
    environment:
      AGENTSHROUD_MODE: monitor  # Remove for production!
```

## Configuration

Core modules can be individually configured in `agentshroud.yaml`:

```yaml
security_modules:
  pii_sanitizer:
    mode: enforce    # enforce (default) or monitor
    action: redact   # redact (default) or block
  prompt_guard:
    mode: enforce    # enforce (default) or monitor
  egress_filter:
    mode: enforce    # enforce (default) or monitor
  mcp_proxy:
    mode: enforce    # enforce (default) or monitor
```

## Security Verification

To verify enforcement is active:

1. **PII Test**: Send a test credit card number - should be redacted
2. **Injection Test**: Send a known injection payload - should be blocked
3. **Egress Test**: Request a non-allowlisted URL - should be denied  
4. **Tool Test**: Attempt unauthorized tool access - should be blocked

## Monitoring

Security events are logged with structured data:
- All enforcement actions are audited
- Monitor mode generates security warnings at startup
- Failed attempts are logged at WARNING level
- Successful blocks are logged at INFO level

## Emergency Response

If security is compromised:
1. Immediately set `AGENTSHROUD_MODE=enforce` 
2. Restart the gateway service
3. Review audit logs for the breach window
4. Update allowlists to close identified gaps

## Contact

For security issues: security@agentshroud.ai
For documentation: https://github.com/agentshroud/agentshroud/security


## Security Features

- **PII Sanitizer** — Hybrid Presidio + regex detection with redaction
- **Prompt Guard** — Injection and jailbreak detection
- **Egress Filter** — DNS-layer domain allowlist
- **File Sandbox** — Path-based read/write access control
- **Metadata Guard** — Path traversal and injection prevention
- **Outbound Info Filter** — Prevents credential/PII leakage in responses
- **Approval Queue** — Human-in-the-loop for high-risk tool calls
- **Session Isolation** — Per-agent session boundaries
- **Credential Injector** — Gateway-only credential storage
- **Network Validator** — Container network policy enforcement
- **ClamAV Scanner** — Malware detection on file operations
- **Trivy Scanner** — Container vulnerability scanning
- **Drift Detector** — Runtime file integrity monitoring
- **Kill Switch** — Emergency shutdown capability for compromised agents
- **Rate Limiter** — Request throttling per agent/IP
- **Canary System** — Data exfiltration detection via planted tokens

## Supported Versions

| Version | Supported |
|---------|-----------|
| v0.7.x  | ✅ Active  |
| v0.6.x  | ⚠️ Critical fixes only |
| < v0.6  | ❌ Unsupported |
| v0.2-v0.5 | ❌ End of life |


## Responsible Disclosure Policy

If you discover a security vulnerability in AgentShroud, please report it responsibly:

1. **Email:** security@agentshroud.ai
2. **Do not** create public GitHub issues for security vulnerabilities
3. We will acknowledge receipt within 48 hours
4. We aim to provide a fix within 7 business days for critical issues

