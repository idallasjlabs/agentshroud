# AgentShroud Documentation

Complete documentation for "One Shroud Over Every Wire" - a secure, isolated OpenClaw deployment.

## Quick Navigation

### Getting Started
- **[Setup Wizard](../setup-wizard.html)** - Interactive web-based setup (START HERE!)
- **[First Time Setup Guide](../FIRST-TIME-SETUP.md)** - Step-by-step manual setup
- **[Connection Guide](./CONNECTION-GUIDE.md)** - Troubleshooting gateway connections
- **[Main README](../README.md)** - Project overview and quick start

### Understanding the Project
- **[Announcement & Philosophy](./ANNOUNCEMENT.md)** - Read this to understand WHY this exists
- **[Security Analysis](./SECURITY-ANALYSIS.md)** - Deep dive into OpenClaw vulnerabilities and our solutions
- **[Future Features Roadmap](./FUTURE-FEATURES.md)** - What's coming next
- **[Session Summary](./SESSION-SUMMARY.md)** - Complete log of development and decisions

### Technical Documentation
- **[Architecture Overview](./ARCHITECTURE.md)** - System design and components
- **[Docker Configuration](./DOCKER-SETUP.md)** - Container hardening details
- **[Network Isolation](./NETWORK-ISOLATION.md)** - How internet-only access works
- **[API Integration](./API-INTEGRATION.md)** - OpenAI/Anthropic setup

### Security
- **[Security Analysis](./SECURITY-ANALYSIS.md)** - Threat model and mitigation strategies
- **[Incident Response Plan](./INCIDENT-RESPONSE.md)** - What to do if compromised
- **[Security Checklist](./SECURITY-CHECKLIST.md)** - Pre-deployment verification

### Usage Guides
- **[Daily Workflow Examples](./WORKFLOW-EXAMPLES.md)** - How to use the agent effectively
- **[Apple Shortcuts Guide](./SHORTCUTS-GUIDE.md)** - iOS/macOS integration (coming soon)
- **[Gmail Forwarding Setup](./GMAIL-FORWARDING.md)** - Email integration guide
- **[Telegram Bot Setup](./TELEGRAM-SETUP.md)** - Quick messaging interface

### Contributing
- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute (coming soon)
- **[Development Setup](./DEVELOPMENT.md)** - Local dev environment
- **[Testing Guide](./TESTING.md)** - How to test changes

## Documentation Status

| Document | Status | Last Updated |
|----------|--------|--------------|
| ANNOUNCEMENT.md | ✅ Complete | Feb 14, 2026 |
| SECURITY-ANALYSIS.md | ✅ Complete | Feb 14, 2026 |
| FUTURE-FEATURES.md | ✅ Complete | Feb 14, 2026 |
| CONNECTION-GUIDE.md | ✅ Complete | Feb 14, 2026 |
| SESSION-SUMMARY.md | ✅ Complete | Feb 14, 2026 |
| ARCHITECTURE.md | 📝 Planned | TBD |
| DOCKER-SETUP.md | 📝 Planned | TBD |
| NETWORK-ISOLATION.md | 📝 Planned | TBD |
| INCIDENT-RESPONSE.md | 📝 Planned | TBD |
| WORKFLOW-EXAMPLES.md | 📝 Planned | TBD |
| SHORTCUTS-GUIDE.md | 📝 Planned | TBD |

## Document Summaries

### ANNOUNCEMENT.md
**Purpose**: Public-facing story explaining the project philosophy and inviting collaborators

**Key Points**:
- The 2026 OpenClaw security crisis (42,900+ exposed instances)
- Why traditional AI assistant setups are dangerous
- The "separate digital environment" philosophy
- How information staging works
- Call for collaborators

**Audience**: General public, potential users, developers

**Length**: ~8,000 words

---

### SECURITY-ANALYSIS.md
**Purpose**: Comprehensive technical security audit and threat modeling

**Key Points**:
- All known OpenClaw vulnerabilities (CVE-2026-25253, etc.)
- How our architecture addresses each vulnerability
- Network isolation diagrams
- Docker hardening measures
- Threat model & attack surface analysis
- Incident response procedures
- Comparison: Traditional vs. Our Approach

**Audience**: Security-conscious users, auditors, technical contributors

**Length**: ~13,000 words

**Sources**: 20+ authoritative security publications and advisories

---

### FUTURE-FEATURES.md
**Purpose**: Product roadmap and feature planning

**Key Points**:
- Priority 0: Apple Shortcuts, Gmail filtering, Telegram enhancements
- Priority 1: Calendar, task management
- Priority 2: Hardware keys, voice interface, PayPal workflows
- Priority 3: Mobile apps, desktop app, multi-agent
- Implementation complexity and ETAs
- Contribution opportunities

**Audience**: Contributors, users interested in roadmap

**Length**: ~7,000 words

---

### CONNECTION-GUIDE.md
**Purpose**: Troubleshooting guide for Control UI connectivity

**Key Points**:
- How to connect Control UI to gateway
- Common WebSocket errors and solutions
- Manual connection testing
- CLI alternatives
- Success checklist

**Audience**: Users experiencing connection issues

**Length**: ~2,000 words

---

### SESSION-SUMMARY.md
**Purpose**: Complete development log and technical decisions

**Key Points**:
- All work completed in this session
- Security research findings
- Files created and modified
- Technical decisions and rationale
- Testing performed
- Next steps

**Audience**: Project maintainers, future developers

**Length**: ~5,000 words

## Project Philosophy

### The Core Problem

Traditional AI assistant deployments grant:
- Full access to your primary email accounts
- Access to your local network and VPN
- OAuth tokens to your real identity
- Ability to execute any command
- Memory of your entire digital life

**When compromised → lose everything.**

### Our Solution: Isolation Layers

1. **Network Isolation**: Internet-only, no LAN/VPN access
2. **Separate Identity**: Dedicated service accounts (therealidallasj@gmail.com)
3. **Information Staging**: You manually forward selected data
4. **Container Hardening**: Non-root, capabilities dropped, resource limits
5. **Defense in Depth**: Multiple overlapping protections

**When compromised → lose a burner email and $40. Rebuild in 10 minutes.**

### The Mantra

> "One Shroud Over Every Wire"
>
> The agent is powerful and useful, but it can only touch what you explicitly hand to it.
> It cannot reach into your digital life and grab things on its own.
>
> One shroud covers every wire. The agent is free to help you.

## Quick Reference

### Essential Commands

```bash
# Start AgentShroud
./start-agentshroud.sh

# Stop AgentShroud
./stop-agentshroud.sh

# View logs
docker logs agentshroud_isaiah -f

# Check status
docker exec agentshroud_isaiah node openclaw.mjs status

# Run security audit
docker exec agentshroud_isaiah node openclaw.mjs security audit
```

### Important Files

```
agentshroud/
├── setup-wizard.html          # Interactive setup (USE THIS FIRST)
├── wizard-deploy.sh           # Automated deployment script
├── start-agentshroud.sh           # Start everything
├── stop-agentshroud.sh            # Stop everything
├── spa-server.py              # Web server for Control UI
├── Dockerfile.secure          # Container build definition
├── agentshroud-container/
│   ├── docker-compose.yml     # Container orchestration
│   ├── config/
│   │   └── openclaw.json      # OpenClaw configuration
│   ├── secrets/
│   │   └── .env              # API keys and tokens
│   ├── workspace/            # Agent workspace
│   └── control-ui/           # Web interface
└── docs/
    ├── SECURITY-ANALYSIS.md
    ├── FUTURE-FEATURES.md
    ├── ANNOUNCEMENT.md
    └── CONNECTION-GUIDE.md
```

### Gateway Authentication

```
Gateway URL: ws://127.0.0.1:18789
Auth Token:  acd0842962070d58c2bb825876aab743c4c45ddbc2eae7e475c4058e0b3f7832
Web UI:      http://localhost:18791
```

### Service Accounts

```
Email:    therealidallasj@gmail.com
Apple ID: therealidallasj@icloud.com (create separately)
Telegram: @therealidallasj (create via @BotFather)
PayPal:   therealidallasj@gmail.com (with $40 limit)
```

## Getting Help

### Common Issues

1. **"Cannot connect to gateway"**
   → See [CONNECTION-GUIDE.md](./CONNECTION-GUIDE.md)

2. **"Container won't start"**
   → Check logs: `docker logs agentshroud_isaiah`

3. **"Security concerns"**
   → Read [SECURITY-ANALYSIS.md](./SECURITY-ANALYSIS.md)

4. **"How do I forward emails?"**
   → Coming soon: [GMAIL-FORWARDING.md](./GMAIL-FORWARDING.md)

### Support Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community support
- **Security Issues**: See SECURITY.md for private disclosure

## Contributing to Documentation

Documentation needs help! See areas marked 📝 Planned above.

**Priority documentation needs**:
1. Architecture diagrams and flowcharts
2. Video tutorials and screencasts
3. Workflow examples with screenshots
4. Apple Shortcuts gallery with .shortcut files
5. Docker networking deep dive
6. Testing and validation procedures

**How to contribute**:
1. Check [CONTRIBUTING.md](../CONTRIBUTING.md)
2. Find a 📝 Planned document above
3. Create draft in Google Docs or Notion
4. Submit PR with markdown version
5. Include screenshots, diagrams, code examples

## Version History

- **v1.0** (Feb 14, 2026) - Initial documentation release
  - Security analysis complete
  - Future features roadmap published
  - Announcement story written
  - Connection guide created

## License

All documentation is licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to:
- Share — copy and redistribute
- Adapt — remix, transform, build upon

Under these terms:
- Attribution — credit "One Shroud Over Every Wire" project
- ShareAlike — distribute under same license

---

**Questions? Open a GitHub Discussion!**

**Found an error? Submit a PR!**

**Want to help? Check the 📝 Planned docs above!**

🦞 One Shroud Over Every Wire
