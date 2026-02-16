# Distributed OpenClaw Node Architecture — Raspberry Pi 4

**Status:** 📋 Future Implementation (Phase 7-8)
**Priority:** Medium (after Phase 4-6 complete)
**Security Level:** High (hardened distributed agent)

---

## Concept Overview

Instead of using simple SSH to run commands on the Raspberry Pi, install OpenClaw itself on the Pi and pair it as a distributed node. This creates a **peer-to-peer AI agent network** where the Pi becomes an autonomous agent that can:

- Execute tasks independently
- Run OpenClaw skills locally
- Communicate directly with the main OpenClaw instance
- Participate in distributed workflows
- Maintain its own secure workspace

---

## Architecture Comparison

### Current Approach (Option 1: Direct SSH)
```
┌─────────────────────────┐
│  Mac (OpenClaw Main)    │
│  @therealidallasj_bot   │
│                         │
│  ┌──────────────────┐   │
│  │ OpenClaw Bot     │   │
│  │ (Docker)         │   │
│  └──────┬───────────┘   │
└─────────┼───────────────┘
          │ SSH
          ▼
┌─────────────────────────┐
│  Raspberry Pi 4         │
│  raspberrypi            │
│                         │
│  secureclaw-bot user    │
│  (bash commands)        │
└─────────────────────────┘
```

**Flow:** Bot SSHs to Pi → Runs bash commands → Returns output

---

### Future Approach (Option 2: Distributed Node)
```
┌─────────────────────────┐
│  Mac (OpenClaw Main)    │
│  @therealidallasj_bot   │
│                         │
│  ┌──────────────────┐   │
│  │ OpenClaw Node 1  │   │
│  │ (Primary)        │   │
│  └──────┬───────────┘   │
└─────────┼───────────────┘
          │ OpenClaw Protocol (WebSocket)
          │ (Encrypted, Authenticated)
          ▼
┌─────────────────────────┐
│  Raspberry Pi 4         │
│  raspberrypi            │
│                         │
│  ┌──────────────────┐   │
│  │ OpenClaw Node 2  │   │
│  │ (Paired Worker)  │   │
│  └──────────────────┘   │
└─────────────────────────┘
```

**Flow:**
1. Main node assigns task to Pi node
2. Pi node executes autonomously
3. Pi node can access its own skills, files, APIs
4. Results returned via OpenClaw protocol
5. Both nodes can initiate communication

---

## Key Benefits

### 1. True Distributed AI
- **Task Distribution**: Main node can delegate work to Pi
- **Parallel Execution**: Both agents work simultaneously
- **Load Balancing**: CPU-intensive tasks run on Pi
- **Specialization**: Pi can have unique skills (IoT, GPIO, local sensors)

### 2. Enhanced Security
- **Encrypted Communication**: WebSocket with TLS
- **Mutual Authentication**: Cryptographic node pairing
- **Sandboxed Execution**: Each node has isolated workspace
- **No SSH Credentials**: No need for SSH keys or passwords
- **Audit Trail**: OpenClaw logs all inter-node communication

### 3. Advanced Capabilities
- **Skill Sharing**: Pi can have Pi-specific skills (GPIO, camera, sensors)
- **Local Processing**: Sensitive data never leaves Pi
- **Offline Operation**: Pi node can work independently
- **Resource Management**: OpenClaw handles node health/status

### 4. Better Development Workflow
- **Direct Testing**: Deploy code to Pi node, test immediately
- **CI/CD Integration**: Pi node runs tests autonomously
- **Git Operations**: Pi node clones/pulls/pushes independently
- **Containerization**: Pi can run Docker for isolated testing

---

## Implementation Plan

### Phase 1: Pi Preparation (Prerequisites)

**Complete security hardening from `BOT_DEVELOPMENT_TEAM_RPI_SETUP.md`:**

- [x] SSH hardening (key-only, Tailscale-only)
- [x] UFW firewall configuration
- [x] Dedicated secureclaw-bot user
- [ ] Node.js 20 LTS installation
- [ ] Docker & Docker Compose installation
- [ ] Git configuration
- [ ] 1Password CLI installation
- [ ] System monitoring setup

**Additional hardening for distributed node:**

```bash
# On Raspberry Pi:

# 1. Install OpenClaw globally
sudo npm install -g openclaw@latest

# 2. Create OpenClaw workspace
sudo mkdir -p /home/secureclaw-bot/.openclaw
sudo chown -R secureclaw-bot:secureclaw-bot /home/secureclaw-bot/.openclaw

# 3. Configure OpenClaw for daemon mode
sudo tee /etc/systemd/system/openclaw-node.service > /dev/null <<EOF
[Unit]
Description=OpenClaw Distributed Node
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=secureclaw-bot
Group=secureclaw-bot
WorkingDirectory=/home/secureclaw-bot
ExecStart=/usr/bin/openclaw gateway --bind lan --allow-unconfigured
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal
SyslogIdentifier=openclaw-node

# Security hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/home/secureclaw-bot/.openclaw
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true

[Install]
WantedBy=multi-user.target
EOF

# 4. Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable openclaw-node
sudo systemctl start openclaw-node
```

---

### Phase 2: Node Pairing

**On Raspberry Pi:**

```bash
# Start pairing mode
sudo -u secureclaw-bot openclaw node pair

# This generates a pairing code (e.g., "abc123-def456")
```

**On Mac (Main OpenClaw Instance):**

```bash
# From your main OpenClaw bot (either via Telegram or CLI)
openclaw node pair abc123-def456

# Or via Telegram:
# "Pair with node using code: abc123-def456"
```

**Pairing Process:**
1. Pi generates ephemeral pairing code
2. Main node connects using code
3. Both nodes exchange public keys
4. Secure WebSocket connection established
5. Pairing code expires (one-time use)

**Verification:**

```bash
# On Mac:
openclaw node list
# Should show: raspberrypi (connected)

# On Pi:
sudo -u secureclaw-bot openclaw node status
# Should show: paired with main node
```

---

### Phase 3: Security Configuration

**Configure node permissions and restrictions:**

```yaml
# On Pi: /home/secureclaw-bot/.openclaw/config.yaml

node:
  name: raspberrypi-dev
  role: worker

  # Network restrictions
  bind: lan  # Allow connections from LAN (Tailscale)
  allowed_peers:
    - <main-node-id>  # Only allow main node

  # Execution limits
  max_concurrent_tasks: 3
  task_timeout: 3600  # 1 hour max per task

  # Resource limits
  max_memory: 4G
  max_cpu: 2.0

  # Allowed operations
  allowed_skills:
    - git
    - docker
    - npm
    - pytest
    - bash  # Restricted bash commands only

  # Denied operations
  denied_skills:
    - ssh  # Pi node cannot SSH to other machines
    - sudo  # No privilege escalation

  # Filesystem restrictions
  workspace: /home/secureclaw-bot/.openclaw/workspace
  allow_filesystem_access: false

  # API restrictions
  require_approval:
    - external_api_calls
    - package_installation
    - docker_builds
```

---

### Phase 4: Skill Development

**Create Pi-specific skills:**

```bash
# On Pi: /home/secureclaw-bot/.openclaw/skills/

# 1. GPIO Control (Pi-specific)
skills/
├── gpio/
│   ├── gpio.js           # Read/write GPIO pins
│   └── package.json
│
├── camera/
│   ├── camera.js         # Capture images from Pi Camera
│   └── package.json
│
├── temperature/
│   ├── temp.js           # Monitor Pi temperature
│   └── package.json
│
├── system-health/
│   ├── health.js         # CPU, RAM, disk monitoring
│   └── package.json
│
└── local-dev/
    ├── git-ops.js        # Git clone, pull, push
    ├── test-runner.js    # Run test suites
    └── package.json
```

**Example: Pi Temperature Monitoring Skill**

```javascript
// /home/secureclaw-bot/.openclaw/skills/temperature/temp.js

import { execSync } from 'child_process';

export default async function checkTemperature() {
  try {
    // Get Pi temperature
    const temp = execSync('vcgencmd measure_temp')
      .toString()
      .match(/temp=([0-9.]+)/)[1];

    const tempFloat = parseFloat(temp);

    // Check throttling
    const throttled = execSync('vcgencmd get_throttled')
      .toString()
      .match(/throttled=(0x[0-9a-f]+)/)[1];

    return {
      temperature: tempFloat,
      unit: 'celsius',
      throttled: throttled !== '0x0',
      status: tempFloat > 75 ? 'warning' : 'ok',
      message: tempFloat > 75
        ? `⚠️ Temperature high: ${tempFloat}°C`
        : `✓ Temperature normal: ${tempFloat}°C`
    };
  } catch (error) {
    return { error: error.message };
  }
}
```

---

### Phase 5: Distributed Workflows

**Example workflows enabled by distributed nodes:**

#### Workflow 1: Automated Testing on Pi

```
User → Telegram: "Run the test suite on the Pi"
  ↓
Main Node (Mac):
  ├─ Identifies task requires Pi node
  ├─ Delegates to raspberrypi-dev node
  └─ Monitors progress
  ↓
Pi Node:
  ├─ Pulls latest code from GitHub
  ├─ Installs dependencies
  ├─ Runs pytest with coverage
  ├─ Generates report
  └─ Returns results to main node
  ↓
Main Node → User: "Tests complete: 87 passed, 2 failed"
```

#### Workflow 2: Continuous Development

```
Developer pushes to GitHub
  ↓
GitHub Webhook → Main Node
  ↓
Main Node delegates to Pi Node:
  ├─ Pull latest code
  ├─ Run tests
  ├─ Build Docker image
  ├─ Deploy to staging
  └─ Report status
  ↓
Main Node → Telegram: "Deploy successful ✓"
```

#### Workflow 3: IoT + AI Integration

```
User → Telegram: "What's the temperature in the lab?"
  ↓
Main Node → Pi Node: Execute temperature skill
  ↓
Pi Node:
  ├─ Reads GPIO sensor
  ├─ Reads Pi internal temp
  ├─ Captures camera image (optional)
  └─ Returns data
  ↓
Main Node:
  ├─ Analyzes data with Claude
  └─ Generates response
  ↓
User: "Lab temperature: 22°C, Pi is running at 58°C (normal)"
```

---

## Security Architecture

### Defense in Depth

**Layer 1: Network Isolation**
- Pi only accessible via Tailscale
- UFW firewall: deny all incoming except Tailscale
- OpenClaw listens only on Tailscale interface
- No public internet exposure

**Layer 2: Node Authentication**
- Cryptographic pairing (one-time code)
- Mutual TLS verification
- Node certificates expire after 90 days
- Re-pairing required for certificate renewal

**Layer 3: Execution Sandboxing**
- Each task runs in isolated workspace
- No host filesystem access (except workspace)
- Resource limits enforced (CPU, RAM, time)
- Skill allowlist/denylist

**Layer 4: Audit & Monitoring**
- All inter-node communication logged
- Task execution audit trail
- Real-time alerts on anomalies
- Integration with existing Zabbix monitoring

**Layer 5: Approval Queue**
- High-risk operations require approval
- User confirms via Telegram before execution
- Approval timeout (auto-deny after 5 minutes)
- Full context provided for approval decision

---

## Comparison Matrix

| Feature | Option 1: SSH | Option 2: Distributed Node |
|---------|---------------|----------------------------|
| **Setup Complexity** | ⭐⭐ Low | ⭐⭐⭐⭐ High |
| **Security** | ⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Excellent |
| **Communication** | SSH (text-based) | OpenClaw Protocol (structured) |
| **Authentication** | SSH keys | Cryptographic pairing + TLS |
| **Audit Trail** | SSH logs only | Full OpenClaw audit ledger |
| **Autonomous Operation** | ❌ No | ✅ Yes |
| **Skill Support** | ❌ No | ✅ Yes |
| **Parallel Execution** | ❌ Sequential | ✅ Parallel |
| **Task Distribution** | Manual | Automatic |
| **Resource Management** | Manual | Automatic |
| **Pi-Specific Capabilities** | ❌ No | ✅ Yes (GPIO, camera, etc.) |
| **Offline Operation** | ❌ No | ✅ Yes |
| **Cost** | $0 | $0 |
| **Maintenance** | Low | Medium |

---

## Migration Path (SSH → Distributed Node)

When ready to migrate from Option 1 to Option 2:

### Step 1: Verify Option 1 Working
- [ ] SSH connection established
- [ ] Bot can execute commands on Pi
- [ ] Git operations working
- [ ] Docker commands working

### Step 2: Install OpenClaw on Pi
- [ ] Node.js 20 installed
- [ ] OpenClaw installed globally
- [ ] Systemd service configured
- [ ] Service running and healthy

### Step 3: Pair Nodes
- [ ] Generate pairing code on Pi
- [ ] Pair from main node
- [ ] Verify connection in `openclaw node list`

### Step 4: Test Basic Communication
- [ ] Send simple task to Pi node
- [ ] Verify execution and results
- [ ] Check audit logs on both nodes

### Step 5: Migrate Workflows
- [ ] Identify tasks currently using SSH
- [ ] Create equivalent OpenClaw skills on Pi
- [ ] Test each workflow with distributed node
- [ ] Update bot instructions/prompts

### Step 6: Deprecate SSH (Optional)
- [ ] Remove SSH public key from Pi
- [ ] Disable SSH access for secureclaw-bot
- [ ] Update firewall rules
- [ ] Document changes

---

## Cost-Benefit Analysis

### Additional Costs (Option 2 vs Option 1)

| Item | Cost | Notes |
|------|------|-------|
| Setup Time | +4-6 hours | One-time |
| Maintenance | +1 hour/month | Updates, monitoring |
| Electricity | +$1/month | Pi runs OpenClaw daemon |
| Total Incremental | ~$1-2/month | Minimal |

### Benefits Gained

| Benefit | Value | Impact |
|---------|-------|--------|
| Security | High | Encrypted, authenticated communication |
| Automation | High | Autonomous task execution |
| Scalability | High | Easy to add more nodes |
| Capabilities | Medium | Pi-specific skills (GPIO, camera) |
| Development Speed | Medium | Faster testing/deployment |
| Reliability | Medium | Self-healing, auto-retry |

**ROI:** High value for minimal cost increase, especially for long-term projects.

---

## Use Cases

### Best Use Cases for Distributed Node Approach

1. **Long-Running CI/CD Pipelines**
   - Pi runs tests overnight
   - Main node monitors progress
   - Results ready in the morning

2. **IoT + AI Integration**
   - Pi reads sensors (temperature, humidity, motion)
   - Claude analyzes data and provides insights
   - Automated responses based on conditions

3. **Distributed Development**
   - Pi is dedicated test environment
   - Main node is development environment
   - Isolates testing from main workflow

4. **Multi-Stage Deployments**
   - Pi is staging environment
   - Main node is production environment
   - Safe testing before production deploy

5. **Resource-Intensive Tasks**
   - Offload CPU-heavy builds to Pi
   - Keep main Mac responsive
   - Parallel execution speeds up workflow

### Not Ideal For

- Simple bash commands (use SSH)
- One-off tasks (overhead not worth it)
- Immediate synchronous responses needed
- Tasks requiring Mac-specific tools

---

## Monitoring & Observability

### Metrics to Track

**Node Health:**
- Connection uptime
- Task success/failure rate
- Average task execution time
- Resource utilization (CPU, RAM, disk)
- Temperature (Pi-specific)

**Security:**
- Failed authentication attempts
- Unauthorized skill invocation attempts
- Unusual task patterns
- Certificate expiration warnings

**Integration with Existing Monitoring:**

```yaml
# Add to Zabbix monitoring

Host: raspberrypi-openclaw-node

Items:
  - openclaw.node.status (0=down, 1=up)
  - openclaw.tasks.queued
  - openclaw.tasks.running
  - openclaw.tasks.success_rate
  - openclaw.resources.cpu
  - openclaw.resources.memory
  - openclaw.temperature

Triggers:
  - Node down for >5 minutes
  - Task failure rate >20%
  - Temperature >75°C
  - Memory usage >90%
  - Certificate expires in <7 days
```

---

## Next Steps

### Prerequisites (Before Implementation)
1. ✅ Complete Phase 3A/3B (Security hardening)
2. ⏳ Complete Phase 4 (SSH capability) ← **Current Phase**
3. ⏳ Complete Phase 5 (Live Action Dashboard)
4. ⏳ Complete Phase 6 (Tailscale + Documentation)

### Implementation Timeline
- **Phase 7 (Month 2):** Distributed node foundation
  - Install OpenClaw on Pi
  - Configure security policies
  - Test basic pairing
- **Phase 8 (Month 3):** Advanced features
  - Custom Pi skills (GPIO, camera)
  - Distributed workflow templates
  - Full integration with SecureClaw

### Decision Points
- [ ] Option 1 working satisfactorily?
- [ ] Need for Pi-specific capabilities (GPIO, camera)?
- [ ] Value of distributed architecture outweighs complexity?
- [ ] Team has bandwidth for advanced setup?

---

## Resources

### Documentation
- OpenClaw Node Pairing: https://openclaw.ai/docs/nodes
- OpenClaw Skills: https://openclaw.ai/docs/skills
- Distributed Architecture: https://openclaw.ai/docs/distributed

### Related SecureClaw Docs
- `BOT_DEVELOPMENT_TEAM_RPI_SETUP.md` - Pi preparation
- `OPENCLAW_SSH_SETUP.md` - Current SSH approach (Option 1)
- `SECURITY_SCRIPTS_REFERENCE.md` - Security tooling

### Community
- OpenClaw Discord: https://discord.gg/openclaw
- GitHub Issues: https://github.com/openclaw/openclaw/issues

---

## Conclusion

**Option 2 (Distributed Node)** provides significant advantages for:
- Long-term projects
- Advanced AI automation
- IoT integration
- Security-critical deployments

**Recommendation:**
- Start with **Option 1 (SSH)** to get immediate value
- Plan migration to **Option 2** in Phase 7-8
- Evaluate after 1-2 months of Option 1 usage

---

**Document Version:** 1.0
**Last Updated:** 2026-02-16
**Status:** Future Implementation Plan
**Priority:** Medium (after Phases 4-6)
