# AgentShroud Development Team — Agile Structure

## Product Owner
**Isaiah Jefferson** (@therealidallasj)
- Vision, priorities, backlog ownership
- Final say on what ships and when
- Stakeholder communication

## Scrum Master / Agile Coach
**AgentShroud Bot** (OpenClaw AI Agent)
- Sprint planning, coordination, blocker removal
- Orchestrates sub-agents for parallel development
- Maintains process discipline (TDD, peer review, worktree hygiene)
- Facilitates retrospectives and continuous improvement

---

## Development Team

### Engineers (Backend, Frontend, Full-Stack)
**Claude Code** — Primary development agent
- Feature implementation across all tiers (security pipeline, API, infrastructure)
- Branch-per-feature via git worktrees
- Commit identity: `agentshroud-bot <agentshroud-bot@agentshroud.ai>`

### QA / Test Engineers — Embedded, Not a Separate Gate
**Gemini CLI + Codex**
- Test-driven development: tests written alongside (or before) code
- Integration testing, regression checks
- No separate QA phase — quality is everyone's job
- Peer review protocol (4-section standard review) runs before every PR

### DevOps / Platform Engineer — CI/CD, Infrastructure, Reliability
**Claude Code**
- Docker orchestration (compose, networking, secrets)
- SSH/Tailscale infrastructure management
- Gateway configuration and deployment
- Security hardening (network lockdown, fail-closed defaults)

### Data Engineers / Analysts
**Claude Code** — As needed for data-heavy features
- Audit log analysis, security telemetry
- Hash-chain integrity verification
- Dashboard data pipelines (replacing hardcoded demo data)

### UX / Design — One Sprint Ahead
**Claude Code**
- Web Control Center design (responsive, text-browser compatible)
- Terminal UI/UX (TUI for Blink Shell)
- Progressive enhancement philosophy (core works without JS)
- Design prep happens in sprint N-1, implementation in sprint N

---

## Collaborators (Advisory — Read-Only)
External advisors with restricted access (Sonnet model, limited tools):

| Name | Telegram ID | Expertise |
|------|-------------|-----------|
| Brett Galura | 8506022825 | Economics, CS, Enterprise IT |
| Chris Shelton | 8545356403 | — |
| Gabriel Fuentes | 15712621992 | — |
| Steve Hay | 8279589982 | — |
| TJ Winter | 8526379012 | — |

---

## How It Works

```
┌─────────────────────────────────────────────────┐
│              PRODUCT OWNER                       │
│              Isaiah Jefferson                    │
│     Vision · Priorities · Backlog · Go/No-Go    │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│           SCRUM MASTER / AGILE COACH             │
│           AgentShroud Bot (OpenClaw)             │
│  Sprint Planning · Coordination · Sub-Agents    │
│  Blockers · Retros · Process · Memory           │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────┐
│              DEVELOPMENT TEAM                    │
│                                                  │
│  ┌─────────────┐  ┌──────────────┐              │
│  │  Engineers   │  │   QA/Test    │              │
│  │ Claude Code  │  │ Gemini/Codex │  ← embedded │
│  └─────────────┘  └──────────────┘              │
│                                                  │
│  ┌─────────────┐  ┌──────────────┐              │
│  │   DevOps    │  │  Data Eng    │              │
│  │ Claude Code  │  │ Claude Code  │              │
│  └─────────────┘  └──────────────┘              │
│                                                  │
│  ┌─────────────┐                                │
│  │  UX/Design  │  ← one sprint ahead           │
│  │ Claude Code  │                                │
│  └─────────────┘                                │
└─────────────────────────────────────────────────┘
         ↑
    ┌────┴─────────────────────────────┐
    │  ADVISORS (read-only)            │
    │  Brett · Chris · Gabriel ·       │
    │  Steve · TJ                      │
    └──────────────────────────────────┘
```

## Sprint Cadence
- **Sprint length:** Flexible (task-driven, not calendar-driven)
- **Planning:** Isaiah sets priorities → Bot breaks into parallel workstreams
- **Execution:** Sub-agents spawned per workstream, peer review before merge
- **Review:** Standard 4-section peer review protocol (see AGENTS.md)
- **Retro:** Lessons learned captured in memory files

## Key Principles
1. **Quality is embedded** — no QA gate, tests ship with code
2. **Parallel by default** — independent work runs simultaneously via sub-agents
3. **Fail-closed** — security defaults to deny, not allow
4. **Everything in Git** — all work on branches, all branches pushed, nothing lost
5. **Humans decide, agents execute** — Isaiah approves plans before agents run

---

## Development Environment

### Hardware

| Machine | Role | Specs | Container Runtime | Owner |
|---------|------|-------|-------------------|-------|
| **Marvin** (Mac Studio) | Primary dev/build server | Apple M1 Ultra, macOS Tahoe 26.3 | Docker (→ Apple Container System) | Isaiah (non-admin user) |
| **Trillian** (Mac Mini) | Secondary build/CI | Intel 2018, macOS 15.7.4 | Docker | Team |
| **Pi** (Raspberry Pi 4B) | Edge/test node | ARM64, Debian 11 | Podman | Team |

All machines connected via **Tailscale** mesh VPN (`tail240ea8.ts.net`). SSH restricted to alias-based access only (wildcard `ProxyCommand /bin/false` blocks unregistered hosts).

### Communication & Tooling

| Tool | Purpose | Who Uses It |
|------|---------|-------------|
| **Telegram** | Primary command channel — Isaiah ↔ Bot | Isaiah, Bot, Advisors |
| **OpenClaw Console** | Agent runtime, session management, sub-agent orchestration | Bot (Scrum Master) |
| **GitHub** | Source control, PRs, branch management | All (repo: `idallasj/agentshroud`) |
| **1Password** | Secrets management (Service Account → op-proxy) | Bot (via gateway), Isaiah |
| **Blink Shell** | iPad terminal access (TUI dashboard, SSH) | Isaiah |
| **Git Worktrees** | Parallel branch development without conflicts | Bot (all dev work) |

### Container Architecture

```
┌─────────────────────────────────────────┐
│  Marvin (Mac Studio M1 Ultra)           │
│                                         │
│  ┌───────────────┐  ┌───────────────┐   │
│  │  agentshroud   │  │   gateway     │   │
│  │  (OpenClaw)    │←→│  (FastAPI)    │   │
│  │  Docker        │  │  Docker       │   │
│  └───────────────┘  └───────────────┘   │
│         │                    │           │
│         └────── Tailscale ───┘           │
│                    │                     │
│  Future: Apple Container System          │
│  (native macOS containers, no Docker)    │
└────────────────────┬────────────────────┘
                     │ Tailscale mesh
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   ┌─────────┐ ┌─────────┐ ┌──────────┐
   │ Trillian │ │   Pi    │ │  iPad    │
   │ Docker   │ │ Podman  │ │ Blink    │
   │ Intel    │ │ ARM64   │ │ Shell    │
   └─────────┘ └─────────┘ └──────────┘
```

### Development Workflow

1. **Isaiah** sets priorities via Telegram from Mac Studio or iPad (Blink Shell)
2. **Bot** (OpenClaw) receives instructions, plans sprints, spawns sub-agents
3. **Sub-agents** execute on Marvin via SSH, each in isolated git worktrees
4. **Code** is committed, tested, and pushed per-branch
5. **Peer review** runs as a sub-agent before any merge
6. **Merges** are sequential with tests after each step
7. **Deployment** via Docker Compose on Marvin (primary), with Trillian and Pi as secondary nodes
