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
