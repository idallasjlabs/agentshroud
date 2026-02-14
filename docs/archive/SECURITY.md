# Security Architecture
## One Claw Tied Behind Your Back

This document explains the security measures implemented in this OpenClaw deployment.

## Core Security Principle

**Source code never touches your host system.** All building, compilation, and dependency resolution happens inside isolated Docker containers.

## Build Process Security

### Secure Multi-Stage Docker Build

The deployment uses a multi-stage Dockerfile that:

1. **Stage 1 - Builder Container (Ephemeral)**
   - Clones OpenClaw from GitHub
   - Installs all build dependencies
   - Compiles the source code
   - Builds the UI
   - **This container is discarded after build**

2. **Stage 2 - Runtime Container (Minimal)**
   - Contains ONLY the compiled artifacts
   - No source code
   - No build tools
   - No unnecessary dependencies
   - Minimal attack surface

### What This Means

```
❌ Traditional approach:
  git clone (on host) → build (on host) → docker build → container

✅ Our secure approach:
  docker build → git clone (in container) → build (in container) → minimal runtime container

Host filesystem: Never sees source code or build artifacts
```

## Container Security Layers

### Layer 1: Process Isolation

```yaml
user: "1000:1000"  # Non-root user
```

- Container runs as unprivileged user (UID 1000)
- Cannot escalate to root inside container
- Prevents container escape via privilege escalation

### Layer 2: Filesystem Isolation

```yaml
read_only: true  # Root filesystem is immutable
tmpfs:
  - /tmp
  - /var/tmp
  - /app/.cache
```

- Root filesystem is read-only
- Only specific directories are writable (in memory)
- Prevents malware from modifying binaries
- Prevents persistence of malicious code

### Layer 3: Capability Dropping

```yaml
cap_drop:
  - ALL  # Drop all Linux capabilities
cap_add:
  - CHOWN  # Only add back minimum required
  - DAC_OVERRIDE
  - SETUID
  - SETGID
  - NET_BIND_SERVICE
```

- Removes all Linux capabilities
- Adds back only those strictly required
- Prevents container from performing privileged operations

### Layer 4: Security Options

```yaml
security_opt:
  - no-new-privileges:true  # Cannot gain new privileges
```

- Blocks privilege escalation paths
- Even if vulnerability found, can't escalate

## Network Security Layers

### Layer 1: Docker Network Isolation

```yaml
networks:
  - openclaw_net  # Custom bridge network

ports:
  - "127.0.0.1:18789:18789"  # Localhost only
  - "127.0.0.1:18790:18790"
```

- Custom bridge network isolates from other containers
- Ports bound ONLY to localhost (127.0.0.1)
- Not accessible from LAN or internet

### Layer 2: Network Driver Options

```yaml
driver_opts:
  com.docker.network.bridge.enable_icc: "false"  # No inter-container communication
  com.docker.network.bridge.enable_ip_masquerade: "true"  # NAT for internet access
```

- Blocks container-to-container communication
- Internet access via NAT only

### Layer 3: Application Firewall (Host)

- Little Snitch or Lulu monitors `com.docker.vpnkit`
- Blocks access to private IP ranges:
  - 192.168.0.0/16
  - 172.16.0.0/12
  - 10.0.0.0/8
- Allows internet access only

### Layer 4: Container Firewall (Future)

The deployment includes `container-firewall.sh` for iptables rules inside the container:

```bash
# Block private networks
iptables -A OUTPUT -d 192.168.0.0/16 -j DROP
iptables -A OUTPUT -d 172.16.0.0/12 -j DROP
iptables -A OUTPUT -d 10.0.0.0/8 -j DROP
```

**Note**: This requires elevated privileges to apply. Currently relies on host firewall.

## Application Security

### OpenClaw Security Features

```json
{
  "security": {
    "audit": {
      "enabled": true,
      "logPath": "/workspace/logs/audit.log"
    },
    "exec": {
      "approvals": {
        "enabled": true,
        "timeout": 300
      }
    },
    "sandbox": {
      "enabled": true,
      "allowedTools": ["bash", "read", "write", "sessions"]
    }
  }
}
```

1. **Audit Logging**: All actions logged to audit.log
2. **Execution Approvals**: Dangerous operations require confirmation
3. **Sandbox Mode**: Tool execution in isolated environment
4. **Pairing Required**: New contacts must be explicitly approved

## Secrets Management

### Storage

```bash
~/.oneclaw-secure/secrets/.env
chmod 600 (owner read/write only)
```

- API keys stored in file with strict permissions
- Not committed to git (.gitignore)
- Not visible in docker inspect (loaded from file)

### Best Practices

1. **Never commit** `.env` files
2. **Rotate keys** periodically
3. **Use API keys** with least privilege
4. **Monitor usage** for anomalies
5. **Revoke immediately** if compromised

## Resource Limits

```yaml
mem_limit: 4g
mem_reservation: 2g
cpus: 2
```

- Prevents container from consuming all host resources
- Mitigates DoS attacks
- Ensures host system remains responsive

## Logging and Monitoring

### Container Logs

```yaml
logging:
  driver: "json-file"
  options:
    max-size: "10m"  # Max 10MB per log file
    max-file: "3"    # Keep 3 rotated files
```

- Logs automatically rotated
- Prevents disk space exhaustion
- Easy to review with `./logs.sh`

### Health Monitoring

```bash
~/.oneclaw-secure/monitor.sh
```

- Runs via cron every 5 minutes
- Checks container health
- Checks resource usage
- Auto-restarts on failure
- Sends macOS notifications on issues

### Audit Logging

```
~/.oneclaw-secure/workspace/logs/audit.log
```

- Records all OpenClaw actions
- Includes timestamps, users, commands
- Retention: 30 days (configurable)
- Review regularly for suspicious activity

## macOS Bridge Security

### Minimal Attack Surface

```javascript
// macos-bridge/index.js
app.listen(8765, '127.0.0.1');  // Localhost only
```

- Listens ONLY on localhost
- No network exposure
- Minimal dependencies (express, ws)
- Single purpose: relay BlueBubbles webhooks

### Isolation from Container

- Runs on host (required for macOS Messages.app)
- Connects to container via localhost WebSocket
- Cannot access container filesystem
- Cannot execute commands in container

## Threat Model

### What We Protect Against

✅ **Container escape** - Multiple layers prevent escalation
✅ **Network scanning** - Container cannot access LAN
✅ **Data exfiltration** - Audit logs track all file access
✅ **Supply chain attacks** - Build from source, verify in container
✅ **Resource exhaustion** - Hard limits on CPU/memory
✅ **Unauthorized access** - Pairing required, token authentication

### What We Don't Protect Against

❌ **Compromised API keys** - Rotate keys, monitor usage
❌ **Social engineering** - User must approve pairing/commands
❌ **Zero-day in Docker** - Keep Docker updated
❌ **Malicious AI responses** - Use trusted AI providers
❌ **Physical access** - Encrypt disk, lock screen

## Update Strategy

### Security Updates

```bash
# Update OpenClaw to latest version
cd ~/.oneclaw-secure
./stop.sh

# Rebuild with latest source
docker build -t oneclaw-secure:latest -f Dockerfile .

./start.sh
```

### Verify Updates

```bash
# Check for security advisories
docker exec oneclaw_gateway openclaw security audit

# Review audit log
tail -100 ~/.oneclaw-secure/workspace/logs/audit.log
```

## Incident Response

### If Compromise Suspected

1. **Stop services immediately**
   ```bash
   cd ~/.oneclaw-secure
   ./stop.sh
   ```

2. **Review logs**
   ```bash
   ./logs.sh
   cat workspace/logs/audit.log
   ```

3. **Check for persistence**
   ```bash
   docker inspect oneclaw_gateway
   launchctl list | grep openclaw
   ```

4. **Rotate all secrets**
   ```bash
   nano secrets/.env  # Change all API keys
   ```

5. **Rebuild from scratch**
   ```bash
   docker rmi oneclaw-secure:latest
   docker build -t oneclaw-secure:latest -f Dockerfile .
   ```

6. **Report to OpenClaw team**
   - GitHub: https://github.com/openclaw/openclaw/security
   - Discord: https://discord.gg/openclaw

## Security Checklist

Before deployment:
- [ ] Application firewall installed (Little Snitch/Lulu)
- [ ] Strong API keys generated
- [ ] Secrets file has chmod 600 permissions
- [ ] Understand pairing process
- [ ] Review audit log retention policy

After deployment:
- [ ] Test network isolation
- [ ] Verify container is non-root
- [ ] Confirm read-only root filesystem
- [ ] Set up monitoring cron job
- [ ] Create first backup
- [ ] Review firewall rules

Ongoing:
- [ ] Check logs weekly
- [ ] Rotate API keys quarterly
- [ ] Update OpenClaw monthly
- [ ] Review audit log monthly
- [ ] Test backup restore annually

## Questions?

- OpenClaw Security: https://docs.oneclaw.ai/gateway/security
- Docker Security: https://docs.docker.com/engine/security/
- Report Issues: https://github.com/openclaw/openclaw/security

---

**Remember**: Security is a process, not a destination. Stay vigilant!
