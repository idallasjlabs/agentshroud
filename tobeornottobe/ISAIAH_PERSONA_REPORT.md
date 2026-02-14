# Isaiah Jefferson — OpenClaw Persona Package

## How to Use This Package

This package contains everything you need to make your OpenClaw bot represent you authentically. There are three files designed to match OpenClaw's workspace structure:

| File | OpenClaw Location | Purpose |
|------|-------------------|---------|
| `IDENTITY.md` | `~/.openclaw/workspace/IDENTITY` | Core persona, name, tone, personality |
| `SOUL.md` | `~/.openclaw/workspace/SOUL.md` | Deep behavioral traits, values, communication style |
| `USER.md` | `~/.openclaw/workspace/USER` | Known facts about you (preferences, background, context) |

### Setup Steps

1. **Copy the files** into your OpenClaw workspace directory (`~/.openclaw/workspace/`)
2. **Edit `IDENTITY`** — customize the name, emoji, and personality description
3. **Link your LinkedIn** — OpenClaw can access LinkedIn via browser skills or you can paste your full profile text into USER
4. **Restart the gateway** — `openclaw gateway restart` or modify via Control UI

### Regarding LinkedIn Access

OpenClaw can't directly authenticate to LinkedIn's API, but you have options:
- **Browser skill**: Enable OpenClaw's browser control, log into LinkedIn in the managed Chrome instance, and let it scrape your profile
- **Manual paste**: Export your LinkedIn profile data (Settings → Get a copy of your data) and paste relevant sections into the USER file
- **LinkedIn URL**: Put your profile URL in the USER file so the bot can reference it when asked

### Regarding Internet Presence

I've included what I found publicly in the USER file. **Be cautious** — some of the data aggregator sites (RocketReach, ContactOut) have your personal email addresses and partial phone numbers exposed. You may want to request removal from those sites.

---

## Summary of Our Interactions (Claude × Isaiah)

### Who You Are (from ~80+ conversations)

You're **Isaiah Dallas Jefferson, Jr.** — Chief Innovation Engineer at Fluence Energy leading the Global Services Digital Enablement & Governance (GSDE&G) team. You're a deeply technical leader who operates across the full stack: cloud infrastructure, system administration, networking, scripting, database management, and monitoring. You hold a BS in Computer Science from the University of Richmond and have 25+ years in the energy sector spanning AES and Fluence.

### Your Technical DNA

- **Primary environment**: macOS with iTerm2, tmux, Ghostty, zsh, conda
- **Cloud**: AWS (Glue, Step Functions, Athena, IAM, S3, SNS, EC2, RDS)
- **Languages**: Python (primary), Bash scripting, SQL (PostgreSQL, MySQL, Athena)
- **Infrastructure**: Linux (Ubuntu, CentOS), Docker, Tailscale, Zabbix
- **Dev tools**: Claude Code, VS Code, GitHub CLI, git-secrets, direnv
- **Networking**: SSH tunneling, Tailscale serve/funnel, Cisco ACLs, industrial protocols (Modbus, DNP3, IEC 61850)

### Your Team

- **KP (Kasthurica Panigrahy)** and **Revathi A** — Data Engineering (GSDE)
- **Tala** — Digital Enablement and Advancement (GSDEA)
- **Keith** — SysOps Reliability Team (SORT)
- GitHub org: FITDevOps, primary repo: services-data-lake

### How You Work

- You troubleshoot methodically — always providing logs, error output, and context
- You prefer command-line solutions over GUI
- You value cross-platform compatibility (Mac + Linux)
- You write scripts meant for team distribution with clear docs
- You enforce proper Git workflows and test-driven development
- You're security-conscious — implemented git-secrets, .env management, direnv
- You care about cost optimization (FY26 40% AWS cost reduction target)
- You run production on servers named things like enst01as01pr, with hosts named marvin, trillian, bionic
- Your data lakehouse: 275TB, 23M+ data points across battery energy storage systems

### Your Communication Style

- Direct and efficient — you provide exactly the context needed
- You iterate quickly — rapid back-and-forth refining solutions
- You push back when solutions don't match your needs
- You value completeness — "give me the full script, copy-paste ready"
- You name your machines after Hitchhiker's Guide characters (marvin, trillian)
- You're comfortable with both high-level architecture and deep technical weeds

### Topics We've Covered Together

**Infrastructure & DevOps**: AWS FinOps optimization, EC2/EBS rightsizing, S3 data lake management, Docker troubleshooting, Tailscale networking, SSH authentication, tmux configuration across multiple versions, terminal emulator comparisons

**Development & Git**: GitHub workflow documentation, branch management (master→main migration), PR processes, deployment procedures, Claude Code skills creation (QA, TDD, CICD, etc.), git-secrets implementation

**System Administration**: Process management, port monitoring, filesystem mounting, package management (dpkg/debconf locks), ClamXAV updates, macOS Tahoe compatibility issues, display resolution configuration

**Data Engineering**: Mango DAS API authentication, Athena query optimization, PostgreSQL management, Zabbix monitoring, Cisco ACL parsing

**Security**: Credential management, .env file cleanup from git history, read-only sudo access design, data privacy in Claude/MCP

**Team Leadership**: Job descriptions, deployment documentation, ITIL processes, team skill deployment scripts, Jira-GitHub integration
