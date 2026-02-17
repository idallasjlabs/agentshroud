# SSH Security Review

This document reviews the attack surface introduced by the SSH proxy module and evaluates the mitigations in place.

## Threat Model

### 1. Command Injection

**Threat:** An attacker crafts a command containing shell metacharacters to execute arbitrary code (e.g., `ls; rm -rf /` or `cat $(whoami)`).

**Mitigations:**
- `INJECTION_PATTERNS` regex blocks `;`, `|`, `&`, `` ` ``, `>`, `<`, `$()`, `${}`, `$VAR`, newlines, and backslash escape sequences
- Validation runs *before* any command reaches the SSH subprocess
- Denied attempts are logged to the audit ledger

**Residual risk:** Low. The regex is comprehensive. Novel Unicode or encoding-based bypasses are theoretically possible but unlikely given the `asyncio.create_subprocess_exec` call (which does not invoke a shell).

### 2. Host Spoofing / Man-in-the-Middle

**Threat:** An attacker intercepts or redirects SSH connections to impersonate a trusted host, capturing credentials or injecting responses.

**Mitigations:**
- SSH uses `StrictHostKeyChecking=accept-new` — accepts a host's key on first connection, rejects if it changes later
- Configurable `known_hosts_file` per host allows pre-populated host keys
- Tailscale network provides encrypted, authenticated tunnels (current deployment)

**Residual risk:** Medium on first connection (TOFU model). If an attacker controls the network during the *first* connection to a new host, they could inject a fraudulent key. After first connection, the key is pinned.

### 3. Credential Theft

**Threat:** An attacker gains access to SSH private keys or the Gateway API auth token.

**Mitigations:**
- SSH keys are stored on the gateway host filesystem with standard Unix permissions
- Gateway API requires `auth_token` for all endpoints
- `BatchMode=yes` prevents interactive password prompts (keys only)

**Residual risk:** Medium. Key theft is a filesystem security concern outside the SSH proxy's scope. No key rotation or HSM/vault integration is currently implemented.

### 4. Privilege Escalation

**Threat:** An attacker uses allowed commands to gain elevated privileges (e.g., using `cat` to read `/etc/shadow`, or exploiting `sudo` if available).

**Mitigations:**
- Allow list constrains which commands can run
- Deny list blocks known dangerous commands
- The SSH user (`secureclaw-bot`) should have minimal OS-level permissions
- `max_session_seconds` limits exposure time

**Residual risk:** Low-Medium. Security depends on OS-level user permissions being properly restricted. The proxy cannot prevent escalation if the SSH user has `sudo` access.

### 5. Denial of Service

**Threat:** An attacker floods the SSH endpoint or submits commands that consume resources on the target host.

**Mitigations:**
- `max_session_seconds` enforces per-command timeout (process killed on expiry)
- Gateway auth token prevents unauthenticated access
- PIDs limit on the container constrains resource consumption

**Residual risk:** Low. Rate limiting is not currently implemented at the endpoint level.

### 6. Audit Log Tampering / PII Leakage

**Threat:** Sensitive data in commands or output leaks into logs, or an attacker tampers with audit records.

**Mitigations:**
- All commands are run through the Presidio PII sanitizer before ledger storage
- Ledger stores content hashes for integrity verification
- Both successful and denied commands are recorded

**Residual risk:** Low. Output (stdout/stderr) is returned to the caller but not stored in the sanitized ledger, so PII in output is the caller's responsibility.

## Risk Summary

| Threat | Severity | Likelihood | Mitigation | Residual Risk |
|--------|----------|------------|------------|---------------|
| Command injection | Critical | Low | Regex + exec (no shell) | Low |
| Host spoofing / MITM | High | Low | TOFU + Tailscale | Medium (first connect) |
| Credential theft | High | Low | Filesystem perms + auth token | Medium |
| Privilege escalation | High | Low | Allow/deny lists + OS perms | Low-Medium |
| Denial of service | Medium | Low | Timeouts + auth | Low |
| Audit log PII leak | Medium | Low | Presidio sanitization | Low |

## Recommendations for Production Deployment

### 1. Pre-populate known_hosts

Eliminate the TOFU risk by pre-populating host keys before the first connection:

```bash
ssh-keyscan -p 22 target-host.example.com >> /etc/secureclaw/known_hosts
```

Then configure each host with `known_hosts_file: "/etc/secureclaw/known_hosts"` and change `StrictHostKeyChecking` from `accept-new` to `yes` (requires code change).

### 2. Network Segmentation

- Run the gateway and target hosts on an isolated network (e.g., Tailscale)
- Block SSH access from any source other than the gateway
- Use firewall rules to restrict the gateway's outbound SSH to known host IPs

### 3. Key Rotation

- Rotate SSH keys periodically (e.g., every 90 days)
- Consider integrating with a secrets manager (e.g., HashiCorp Vault, 1Password) for key storage
- Use short-lived SSH certificates instead of static keys for high-security targets

### 4. Rate Limiting

Add per-IP or per-token rate limiting on `/ssh/exec` to prevent abuse:

```python
# Example: 10 requests per minute per token
@app.middleware
async def rate_limit_ssh(request, call_next): ...
```

### 5. Output Sanitization

Currently, command output (stdout/stderr) is returned raw to the caller. Consider:
- Sanitizing output through Presidio before returning it
- Truncating output to a maximum size
- Optionally storing sanitized output in the ledger for forensics

### 6. Least-Privilege SSH Users

Ensure each SSH user account on target hosts:
- Has no `sudo` access (or `sudo` only for specific, whitelisted commands)
- Owns no sensitive files
- Has a restricted shell if possible (e.g., `rbash`)
- Uses `ForceCommand` in `sshd_config` for an additional layer of restriction

## Comparison: Direct SSH vs. SecureClaw SSH Proxy

| Aspect | Direct SSH | SecureClaw SSH Proxy |
|--------|-----------|---------------------|
| **Access control** | SSH keys / passwords only | Auth token + allow/deny lists + injection detection |
| **Approval workflow** | None | Human approval queue for sensitive commands |
| **Audit trail** | SSH logs on target host | Centralized ledger with PII sanitization |
| **Command restriction** | Requires `ForceCommand` or restricted shell | Built-in allow/deny lists per host |
| **Injection protection** | None (shell interprets everything) | Regex blocks metacharacters; `exec` avoids shell |
| **Timeout enforcement** | `ClientAliveInterval` only | Per-command timeout with process kill |
| **PII in logs** | Raw commands in auth log | Sanitized via Presidio before storage |
| **Blast radius** | Full shell access | Limited to validated, approved commands |

The SSH proxy adds defense-in-depth: even if an attacker obtains the API token, they face injection detection, allow/deny lists, approval requirements, and audit logging before any command executes on the target.
