# AgentShroud Security Analysis & Hardening

## Overview

This document analyzes the major security vulnerabilities discovered in OpenClaw during 2026 and demonstrates how our "One Claw Tied Behind Your Back" implementation addresses each concern through defense-in-depth architecture.

## Critical Vulnerabilities Identified in OpenClaw (2026)

### CVE-2026-25253: WebSocket Origin Hijacking → Remote Code Execution

**Severity**: CRITICAL
**CVSS Score**: 9.8
**Affected Versions**: All versions prior to 2026.1.29

**Description**: A critical vulnerability allowed remote code execution through a one-click exploit chain via cross-site WebSocket hijacking. OpenClaw's gateway failed to validate the WebSocket origin header, allowing attackers to execute arbitrary code by tricking users into visiting malicious web pages.

**Sources**:
- [OpenClaw Bug Enables One-Click Remote Code Execution](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
- [Critical vulnerability in OpenClaw allows 1‑click RCE](https://ccb.belgium.be/advisories/warning-critical-vulnerability-openclaw-allows-1-click-remote-code-execution-when)
- [The Register: OpenClaw ecosystem still suffering severe security issues](https://www.theregister.com/2026/02/02/openclaw_security_issues/)

**Our Solution**:
- ✅ **Network Isolation**: Our container runs with `--network agentshroud_isolated` preventing direct internet exposure
- ✅ **No Public Access**: Gateway bound to `loopback` only (127.0.0.1), unreachable from external networks
- ✅ **Token Authentication**: OPENCLAW_GATEWAY_TOKEN required for all connections
- ✅ **Separate Digital Environment**: Acts as air-gapped staging area for information forwarding

### Mass Exposure: 42,900+ Publicly Accessible Instances

**Finding**: Security researchers discovered 42,900 unique IP addresses hosting exposed OpenClaw control panels with full system access across 82 countries. 35.4% of these deployments were vulnerable to Remote Code Execution.

**Sources**:
- [Researchers Find 40,000+ Exposed OpenClaw Instances](https://www.infosecurity-magazine.com/news/researchers-40000-exposed-openclaw/)
- [OpenClaw Security: Risks of Exposed AI Agents](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances)
- [Why OpenClaw has security experts on edge](https://fortune.com/2026/02/12/openclaw-ai-agents-security-risks-beware/)

**Statistics**:
- 21,639 exposed instances identified by Censys (January 31, 2026)
- 63% of deployments were vulnerable
- 15,200 instances vulnerable to RCE
- Nearly 1,000 instances running **without any authentication**

**Consequences**:
- Anthropic API keys exposed
- Telegram bot tokens compromised
- Slack account credentials stolen
- Months of complete chat histories accessible
- SSH credentials and browser passwords leaked

**Our Solution**:
- ✅ **Never Exposed to Internet**: Port 18789 bound to localhost only (127.0.0.1)
- ✅ **Docker Network Isolation**: Custom bridge network prevents WAN routing
- ✅ **Optional Tailscale-Only Access**: If remote access needed, secured via Tailscale VPN (user's private network)
- ✅ **Multi-Layer Authentication**: Gateway token + Tailscale authentication
- ✅ **No Default Cloud Deployment**: Runs locally on user's machine only

### Malicious Skills on ClawHub: The Supply Chain Attack

**Finding**: Security audits revealed 900 malicious skills on ClawHub (OpenClaw's official skill repository), representing nearly 20% of all available packages. Between February 1-3, 2026, 386 confirmed malicious skills were identified deploying infostealers.

**Sources**:
- [Malicious crypto skills compromise OpenClaw AI assistant users](https://www.paubox.com/blog/malicious-crypto-skills-compromise-openclaw-ai-assistant-users)
- [Technical Advisory: OpenClaw Exploitation in Enterprise Networks](https://businessinsights.bitdefender.com/technical-advisory-openclaw-exploitation-enterprise-networks)

**Attack Vectors**:
- Crypto exchange API key theft (Binance, Coinbase, Kraken)
- Wallet private key exfiltration
- SSH credential harvesting
- Browser password stealing
- Session token hijacking

**Compromised Accounts**:
- 14 GitHub accounts confirmed compromised
- Accounts had legitimate contribution history to lend credibility
- Malicious skills disguised as productivity tools

**Our Solution**:
- ✅ **No Automatic Skill Installation**: Skills must be manually approved
- ✅ **Sandboxed Execution**: All agent operations run in restricted Docker environment
- ✅ **Network Restrictions**: Skills cannot access LAN or VPN (internet-only egress)
- ✅ **User-Controlled Integration**: Only user-approved data forwarded to agent
- ✅ **Isolated Credentials**: Uses separate service account (therealidallasj@gmail.com), not primary accounts
- ✅ **Audit Logging**: All skill executions logged for review

### The "Lethal Trifecta" - Enterprise Insider Threat

**Assessment**: Palo Alto Networks called OpenClaw the "potential biggest insider threat of 2026" due to three converging risks:

1. **Access to Private Data**: Full filesystem and terminal access
2. **Exposure to Untrusted Content**: Processes external web content, emails, messages
3. **External Communication + Memory**: Can exfiltrate data while maintaining context

**Sources**:
- [Palo Alto: OpenClaw presents lethal trifecta of risks](https://fortune.com/2026/02/12/openclaw-ai-agents-security-risks-beware/)
- [Jamf: OpenClaw AI Agent Insider Threat Analysis](https://www.jamf.com/blog/openclaw-ai-agent-insider-threat-analysis/)
- [CNBC: From Clawdbot to Moltbot to OpenClaw](https://www.cnbc.com/2026/02/02/openclaw-open-source-ai-agent-rise-controversy-clawdbot-moltbot-moltbook.html)

**Shadow AI Phenomenon**:
- Employees deploying hundreds of AI agents via single-line commands
- Agents granted broad terminal and disk access without security review
- Corporate machines compromised through legitimate-looking automation

**Our Solution**:
- ✅ **Principle of Least Privilege**: Agent has NO access to:
  - Your primary email accounts
  - Your main iCloud/Apple ID
  - Your production services
  - Your local network devices
  - Your VPN or corporate network

- ✅ **Information Staging Area**: Operates as separate digital environment
  - Uses dedicated service accounts only
  - User manually forwards selected information via:
    - Email to therealidallasj@gmail.com
    - Apple Shortcuts (future feature)
    - Telegram messages (optional)

- ✅ **No Filesystem Access**: Container has no access to host filesystem
- ✅ **Resource Limits**: CPU and memory capped to prevent resource exhaustion
- ✅ **Capability Dropping**: All unnecessary Linux capabilities removed

### 512 Total Vulnerabilities, 8 Critical

**Audit Results**: Security audit in late January 2026 identified 512 total vulnerabilities, with 8 classified as CRITICAL.

**OpenClaw Response**: Version 2026.2.12 released with fixes for 40+ security issues.

**Sources**:
- [OpenClaw 2026.2.12 Released With Fix for 40+ Security Issues](https://cybersecuritynews.com/openclaw-2026-2-12-released/)
- [Kaspersky: New OpenClaw AI agent found unsafe for use](https://www.kaspersky.com/blog/openclaw-vulnerabilities-exposed/55263/)
- [OpenClaw security 101: Vulnerabilities & hardening (2026)](https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/)

**Our Solution**:
- ✅ **Using Latest Patched Version**: Dockerfile pulls from `main` branch (includes all security patches)
- ✅ **Automatic Updates**: Can rebuild container to get latest security fixes
- ✅ **Defense in Depth**: Even if new vulnerabilities discovered, network isolation limits blast radius

## Our Security Architecture

### Network Isolation (Internet-Only Access)

```
                                    ┌─────────────────────────────┐
                                    │   Internet (ALLOWED)        │
                                    │   - OpenAI API              │
                                    │   - Anthropic API           │
                                    │   - Public web resources    │
                                    └──────────────┬──────────────┘
                                                   │
                                                   │ ✅ Allowed
                                                   │
                   ┌───────────────────────────────┼───────────────────────────────┐
                   │  Docker Container             │                               │
                   │  (agentshroud_isaiah)             │                               │
                   │                                │                               │
                   │  ┌──────────────────────────┐ │                               │
                   │  │  OpenClaw Gateway        │ │                               │
                   │  │  ws://127.0.0.1:18789    │ │                               │
                   │  │  (loopback only)         │ │                               │
                   │  └──────────────────────────┘ │                               │
                   │                                │                               │
                   └────────────────────────────────┘                               │
                                    │                                                │
                                    │ ❌ BLOCKED                                     │
                                    │                                                │
        ┌───────────────────────────┼────────────────────────────────────────────┐  │
        │  Local Network            │                                            │  │
        │  - 192.168.x.x            ❌ No access to:                            │  │
        │  - 10.x.x.x               │  • NAS devices                             │  │
        │  - 172.16.x.x             │  • Printers                                │  │
        │  - VPN networks           │  • Smart home devices                      │  │
        │                           │  • Corporate resources                     │  │
        └───────────────────────────┴────────────────────────────────────────────┘  │
                                                                                     │
        ┌────────────────────────────────────────────────────────────────────────┐  │
        │  Host Filesystem                                                       │  │
        │  - /Users/you/Documents   ❌ No access to:                             │  │
        │  - /Users/you/Desktop     │  • Personal files                          │  │
        │  - /Users/you/Downloads   │  • Source code repositories                │  │
        │  - ~/.ssh                 │  • SSH keys or credentials                 │  │
        │                           │  • Browser data or passwords               │  │
        └───────────────────────────┴────────────────────────────────────────────┘  │
                                                                                     │
                                    User's Mac                                       │
                                    (Host System)                                    │
                                                                                     │
                                                                                     │
                                    ┌─────────────────────────────────────────────┐ │
                                    │  Control UI                                 │ │
                                    │  http://localhost:18791                     │ │
                                    │  (SPA web interface)                        │ │
                                    └─────────────────────────────────────────────┘ │
                                                                                     │
                                                                                     │
        ┌────────────────────────────────────────────────────────────────────────────┘
        │  Optional: Tailscale VPN (User's Choice)
        │  https://yourname.tailXXXXXX.ts.net/
        │  - Authenticated via Tailscale account
        │  - Encrypted WireGuard tunnel
        │  - Access from your other devices only
        └────────────────────────────────────────────────────────────────────────────
```

### Docker Hardening Measures

Our container implements enterprise-grade security hardening:

```yaml
security_opt:
  - no-new-privileges:true    # Prevents privilege escalation
cap_drop:
  - ALL                       # Drop all Linux capabilities
user: "1000:1000"             # Run as non-root user
mem_limit: 4g                 # Limit memory to 4GB
cpus: 2                       # Limit CPU usage
networks:
  - agentshroud_isolated          # Custom isolated bridge network
ports:
  - "127.0.0.1:18789-18790:18789-18790"  # Localhost-only binding
```

**Sources for Best Practices**:
- [How to secure OpenClaw: Docker hardening](https://composio.dev/blog/secure-openclaw-moltbot-clawdbot-setup)
- [OpenClaw Security: Complete 3-Tier Implementation Guide](https://aimaker.substack.com/p/openclaw-security-hardening-guide)
- [Running OpenClaw in Docker: Secure Local Setup](https://aimlapi.com/blog/running-openclaw-in-docker-secure-local-setup-and-practical-workflow-guide)

### The "Separate Digital Environment" Philosophy

**Problem with Traditional Setups**:
Most OpenClaw deployments grant the agent direct access to:
- Primary email accounts (Gmail, Outlook, iCloud)
- Calendar with personal/work events
- Cloud storage (Google Drive, iCloud Drive, Dropbox)
- Messaging apps (Telegram, Slack, Discord connected to main accounts)
- Financial services using primary credentials

**Result**: If agent compromised → entire digital life exposed

**Our Approach**: Agent as "Staging Area"
```
Your Primary Digital Life          Information Flow          Agent's Isolated Environment
======================             ===============           ============================

Primary Gmail                                               therealidallasj@gmail.com
• work@company.com          ─────────────────────►         (dedicated service account)
• personal@gmail.com        User manually forwards
                            selected emails only

Primary Apple ID                                            therealidallasj@icloud.com
• iCloud data               ─────────────────────►         (separate Apple ID)
• iMessages (main)          Via Apple Shortcuts             No access to your:
• Contacts                  (future feature)                • Photos
                                                            • Notes
                                                            • iCloud Drive

Primary Bank Accounts                                       PayPal with $40 limit
• Chase                     ─────────────────────►         • Pre-approved transactions
• Wells Fargo               User approves each              • Budget-constrained
                            transaction

Primary Telegram                                            @therealidallasj
• @yourusername             ─────────────────────►         (dedicated bot account)
                            Optional forwarding
```

**Key Principle**: You control the information valve. The agent only sees what you explicitly forward.

## Threat Model & Attack Surface

### What Can an Attacker Do if They Compromise Our OpenClaw Container?

**Attack Scenario**: Assume worst case - attacker gains remote code execution inside the container.

**What They CAN Access**:
- ✅ therealidallasj@gmail.com emails (only what you've forwarded)
- ✅ OpenAI API usage (within key limits)
- ✅ Telegram bot messages (on dedicated account)
- ✅ Container's workspace files (no sensitive host data)
- ✅ Public internet resources

**What They CANNOT Access** (due to network isolation):
- ❌ Your primary email accounts
- ❌ Your local network (192.168.x.x)
- ❌ Your NAS, printers, smart home devices
- ❌ Your VPN or corporate network
- ❌ Your Mac's filesystem (/Users/you/)
- ❌ Your SSH keys, browser passwords, keychains
- ❌ Your primary iCloud/Apple ID
- ❌ Your main bank accounts
- ❌ Other Docker containers
- ❌ Host Docker daemon (no Docker socket mounted)

**Blast Radius**: Limited to:
- Service account credentials (easily revoked)
- Forwarded messages/emails (you control what's sent)
- OpenAI API charges (set spending limits in OpenAI dashboard)

**Recovery**:
1. Stop container: `./stop-agentshroud.sh`
2. Revoke service account API keys in OpenAI dashboard
3. Change password on therealidallasj@gmail.com
4. Rebuild container from clean image
5. Generate new gateway token
6. Total time: ~10 minutes

## Comparison: Traditional Setup vs. Our Approach

| Security Aspect | Traditional OpenClaw | One Claw Tied Behind Your Back |
|----------------|---------------------|--------------------------------|
| **Network Access** | Full LAN + Internet | Internet-only (RFC1918 blocked) |
| **Email Integration** | Primary Gmail via OAuth | Separate service account |
| **Credentials at Risk** | Your main API keys | Dedicated keys (easily revoked) |
| **Filesystem Access** | Often mounted /home | No host filesystem access |
| **Docker Socket** | Sometimes mounted | Never mounted |
| **Authentication** | Often none | Token + optional Tailscale |
| **Exposure Risk** | Thousands publicly exposed | Localhost-only (never public) |
| **Malicious Skills** | Auto-install from ClawHub | Manual approval required |
| **Data Exfiltration** | Full email, calendar, files | Only forwarded messages |
| **Blast Radius** | Entire digital identity | Service account only |
| **Recovery Time** | Days (compromise investigation) | ~10 minutes (revoke & rebuild) |

## Residual Risks & Limitations

### Risks We Accept (With Mitigations)

1. **OpenAI API Key Exposure**
   - **Risk**: If container compromised, API key can be extracted
   - **Mitigation**:
     - Set spending limits in OpenAI dashboard ($50/month recommended)
     - Use dedicated API key (not shared with other projects)
     - Monitor usage daily
     - Rotate keys monthly

2. **Information You Forward Is Accessible**
   - **Risk**: Anything you send to therealidallasj@gmail.com becomes accessible
   - **Mitigation**:
     - Only forward non-sensitive information
     - Treat it like a public assistant
     - Review before forwarding
     - No passwords, financial data, or PII

3. **Docker Desktop Vulnerabilities**
   - **Risk**: Vulnerability in Docker Desktop itself
   - **Mitigation**:
     - Keep Docker Desktop/OrbStack updated
     - Consider Podman for rootless containers (advanced)
     - Monitor Docker security advisories

4. **macOS Host Compromise**
   - **Risk**: If your Mac is compromised, container can be accessed
   - **Mitigation**:
     - This is true for any local application
     - Use FileVault, strong password, auto-lock
     - Keep macOS updated
     - Use reputable antivirus

### Risks We Eliminate

- ✅ **Mass internet scanning**: Not exposed to public internet
- ✅ **WebSocket hijacking**: Localhost-only binding prevents cross-origin attacks
- ✅ **Lateral movement**: No LAN access prevents attacking other devices
- ✅ **Primary account compromise**: Separate service accounts protect main identity
- ✅ **Malicious skill auto-install**: Manual approval required
- ✅ **Privilege escalation**: Non-root user + capability dropping
- ✅ **Resource exhaustion**: CPU and memory limits enforced

## Security Checklist

Before deploying:

- [ ] Verify Docker version is current (`docker --version`)
- [ ] Confirm container runs as non-root (`docker exec agentshroud_isaiah whoami` → should say "node")
- [ ] Check network isolation (`docker exec agentshroud_isaiah ping -c 1 192.168.1.1` → should fail)
- [ ] Verify internet access (`docker exec agentshroud_isaiah ping -c 1 8.8.8.8` → should succeed)
- [ ] Confirm localhost-only binding (`docker port agentshroud_isaiah` → should show 127.0.0.1)
- [ ] Test gateway authentication (try connecting without token → should fail)
- [ ] Set OpenAI spending limit ($50/month recommended)
- [ ] Enable 2FA on therealidallasj@gmail.com
- [ ] Review OpenClaw audit logs weekly
- [ ] Never mount host filesystem or Docker socket
- [ ] Never expose port 18789 to 0.0.0.0
- [ ] Rotate gateway token monthly

## Monitoring & Incident Response

### Daily Monitoring

```bash
# Check for failed login attempts
docker logs agentshroud_isaiah | grep "auth failed"

# Monitor API usage
docker exec agentshroud_isaiah node openclaw.mjs status

# Check for suspicious connections
docker logs agentshroud_isaiah | grep "connection from"
```

### Weekly Security Audit

```bash
# Run OpenClaw's built-in security audit
docker exec agentshroud_isaiah node openclaw.mjs security audit

# Check for container updates
docker pull openclaw-secure:latest

# Review installed skills
docker exec agentshroud_isaiah node openclaw.mjs skills list
```

### Incident Response Plan

**If you suspect compromise**:

1. **Immediate Actions** (< 5 minutes):
   ```bash
   # Stop container
   ./stop-agentshroud.sh

   # Disconnect from network
   docker network disconnect agentshroud_isolated agentshroud_isaiah
   ```

2. **Investigation** (< 30 minutes):
   ```bash
   # Export logs
   docker logs agentshroud_isaiah > /tmp/incident-logs.txt

   # Check last commands
   docker exec agentshroud_isaiah node openclaw.mjs logs --tail 1000

   # Review audit log
   docker exec agentshroud_isaiah cat /app/logs/audit.log
   ```

3. **Containment** (< 1 hour):
   - Revoke OpenAI API key in dashboard
   - Change password on therealidallasj@gmail.com
   - Review recent emails sent from service account
   - Check API usage for anomalies

4. **Recovery** (< 2 hours):
   ```bash
   # Remove compromised container
   docker compose -f agentshroud-container/docker-compose.yml down
   docker rmi agentshroud-secure:latest

   # Rebuild from source
   docker build -t agentshroud-secure:latest -f Dockerfile.secure .

   # Generate new gateway token
   openssl rand -hex 32 > agentshroud-container/secrets/.env

   # Restart with fresh config
   ./start-agentshroud.sh
   ```

5. **Post-Incident**:
   - Document timeline of events
   - Identify entry vector (malicious skill? vulnerability?)
   - Update security controls
   - Share findings with community

## Future Security Enhancements

Tracked in [FUTURE-FEATURES.md](./FUTURE-FEATURES.md):

- Hardware security key support (YubiKey, etc.)
- SELinux/AppArmor profiles
- Automatic security updates
- Honeypot capabilities for detecting compromise
- Integration with SIEM tools
- mTLS for gateway connections

## Conclusion

The OpenClaw platform faced significant security challenges in early 2026, with critical vulnerabilities affecting tens of thousands of installations worldwide. Our "One Claw Tied Behind Your Back" implementation addresses these concerns through:

1. **Network isolation** (internet-only, no LAN access)
2. **Separate digital environment** (dedicated service accounts)
3. **Information staging** (user controls what agent sees)
4. **Docker hardening** (non-root, capability dropping, resource limits)
5. **Defense in depth** (multiple overlapping security layers)

This creates a secure AI assistant that serves as an information staging area - you forward selected data to it, but your primary digital life remains protected. If compromised, the blast radius is limited to easily-revoked service accounts, not your entire online identity.

**Remember**: Security is a spectrum, not a binary. This setup dramatically reduces risk compared to traditional OpenClaw deployments, but no system is perfectly secure. Stay vigilant, monitor logs, and maintain good security hygiene.

---

## References

- [OpenClaw ecosystem still suffering severe security issues • The Register](https://www.theregister.com/2026/02/02/openclaw_security_issues/)
- [OpenClaw vulnerability notification - University of Toronto](https://security.utoronto.ca/advisories/openclaw-vulnerability-notification/)
- [OpenClaw Bug Enables One-Click Remote Code Execution](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
- [Critical vulnerability in OpenClaw allows 1‑click RCE](https://ccb.belgium.be/advisories/warning-critical-vulnerability-openclaw-allows-1-click-remote-code-execution-when)
- [OpenClaw Security: Risks of Exposed AI Agents](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances)
- [OpenClaw security 101: Vulnerabilities & hardening (2026)](https://adversa.ai/blog/openclaw-security-101-vulnerabilities-hardening-2026/)
- [OpenClaw 2026.2.12 Released With Fix for 40+ Security Issues](https://cybersecuritynews.com/openclaw-2026-2-12-released/)
- [Why OpenClaw has security experts on edge | Fortune](https://fortune.com/2026/02/12/openclaw-ai-agents-security-risks-beware/)
- [Technical Advisory: OpenClaw Exploitation in Enterprise Networks](https://businessinsights.bitdefender.com/technical-advisory-openclaw-exploitation-enterprise-networks)
- [Researchers Find 40,000+ Exposed OpenClaw Instances](https://www.infosecurity-magazine.com/news/researchers-40000-exposed-openclaw/)
- [How to secure OpenClaw: Docker hardening](https://composio.dev/blog/secure-openclaw-moltbot-clawdbot-setup)
- [OpenClaw Security: Complete 3-Tier Implementation Guide](https://aimaker.substack.com/p/openclaw-security-hardening-guide)
- [Running OpenClaw in Docker: Secure Local Setup](https://aimlapi.com/blog/running-openclaw-in-docker-secure-local-setup-and-practical-workflow-guide)

**Last Updated**: February 14, 2026
**Version**: 1.0
