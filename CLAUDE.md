# CLAUDE.md
#
# Guidance for Claude Code (claude.ai/code) when working in this repository.
# These instructions are authoritative. Follow them strictly.
# Keep actions deterministic, minimal, and aligned with how this repo is actually run.

──────────────────────────────────────────────────────────────────────────────
## 0) PRIME DIRECTIVE (NON-NEGOTIABLE)
──────────────────────────────────────────────────────────────────────────────

- **Do NOT create new files** unless absolutely required to satisfy the request.
- **Prefer modifying existing files** over adding new ones.
- **Never create documentation files** (`*.md`, README, design docs) unless the
  **user explicitly asks** for documentation.
- If a new file is genuinely required:
  - Explain **why**
  - Propose the **minimum viable file**
  - Wait for confirmation before creating it
- Never broaden scope beyond the explicit request.
- Never perform opportunistic refactors.

If instructions conflict, follow this file over all other guidance.

──────────────────────────────────────────────────────────────────────────────
## 0.1) MULTI-AGENT HIERARCHY (CLAUDE CODE IS PRIMARY)
──────────────────────────────────────────────────────────────────────────────

**YOU (Claude Code) are the PRIMARY developer in this repository.**

This repository uses a multi-agent development approach with clear role separation:

### PRIMARY Developer: Claude Code (You)
**Responsibilities:**
- Architectural decisions
- Feature implementation
- Schema and API design
- Complex refactors
- Documentation strategy
- Code ownership

**Configuration:** `.claude/` directory
- Advanced agents, skills, and hooks enabled
- Full development permissions
- Plan mode for safety

### SECONDARY/TERTIARY Developers: Gemini CLI & ChatGPT Codex
**Responsibilities:**
- Test augmentation (add missing tests, edge cases)
- Validation runs (execute commands, report results)
- Safe refactors ONLY (after tests pass, local changes only)

**What they CANNOT do:**
- Make architectural decisions (defer to you)
- Implement new features (your job)
- Perform large refactors (your job)
- Create documentation (unless explicitly requested)

**Configuration:**
- Gemini CLI: `.gemini/` directory with `settings.json` (MCP servers) and `GEMINI.md` (context)
- ChatGPT Codex: `.codex/` directory with `config.toml` (MCP servers, feature flags) and `AGENTS.md` (context)
- Neither has agents, skills, or hooks (Claude Code exclusive features)
- Both enforce secondary/tertiary agent role via their context files

### When to Use Each Agent

**Use Claude Code (you) for:**
- New features
- Bug fixes
- Refactoring
- Architecture changes
- Documentation
- PRs and commits

**Use Gemini/Codex for:**
- Adding test coverage after Claude implements changes
- Running validation scripts
- Small, safe refactors (variable naming, helper extraction)
- Test result reporting

**Never delegate primary development to Gemini or Codex.**

──────────────────────────────────────────────────────────────────────────────
## 1) PROJECT OVERVIEW (SCOPE AWARENESS)
──────────────────────────────────────────────────────────────────────────────

**AgentShroud** is an open-source, enterprise-grade **transparent proxy
framework** for the safe, auditable, and governed deployment of autonomous
AI agents in real-world production environments.

It sits as an intermediary layer between AI agents (Claude Code, Gemini CLI,
OpenAI Codex, OpenClaw, and others) and the systems they interact with —
intercepting, inspecting, logging, and enforcing policy on every action
without disrupting the agent's native workflow.

### Primary Components

**Gateway (FastAPI — `gateway/`)**
- Ingest API: forwards data between users and agents with PII filtering,
  approval queue, and audit logging
- Security modules: 14+ modules covering prompt injection, egress, SSH
  proxy, container hardening, kill switch, MCP proxy, HTTP CONNECT proxy,
  credential isolation, and more
- Authentication: HMAC/JWT shared-secret for the bot; human approval queue
  for dangerous actions

**Bot Container (`docker/`)**
- OpenClaw-based autonomous agent (therealidallasj bot, runs on macOS Docker)
- Cron jobs, Telegram channel, 1Password credential integration
- Baked-in config bootstrapped by init script on every startup

**Infrastructure**
- Docker Compose (macOS host), Tailscale for secure remote access
- Raspberry Pi node (`raspberrypi.tail240ea8.ts.net`) for SSH experiments
- 1Password service account for credential isolation (P2)
- Integrations: GitHub, Atlassian (Jira/Confluence), AWS via MCP servers

### Development Goals (guide scope decisions)

- **Personal mastery through real building** — develop hands-on fluency with
  Claude Code, OpenAI Codex, Gemini CLI, MCP, multi-agent coordination, and
  enterprise integrations (GitHub, Atlassian Jira/Confluence, AWS) by shipping
  production software with these tools — not through courses
- Prove that autonomous agents can be deployed safely in enterprise settings
- Provide a real, working reference implementation — not a whitepaper
- Enable the architect/owner (non-developer) to direct LLM agents to build
  production-quality software
- Demonstrate secure multi-agent collaboration and external contributor access
- Show enterprise colleagues a concrete, deployable example of governed AI work

Do not expand scope beyond explicit requests. When unsure, ask.

──────────────────────────────────────────────────────────────────────────────
## 2) HOW TO WORK IN THIS REPO (SDLC EXPECTATIONS)
──────────────────────────────────────────────────────────────────────────────

### Definition of Done (DoD)

A change is considered **done** only when:

- The change is **strictly scoped** to the request
- Existing behavior is preserved unless explicitly changed
- The impacted workflow runs successfully
- You provide **evidence of validation**, in this priority order:

  1. **Unit tests** (required for code behavior changes)
  2. **Data validation output**
     - Stage 1 / Stage 2 checks
     - Schema verification
     - Controlled reprocess
  3. Script execution output (small scoped run)
  4. Notebook execution (only if that is the established workflow)

- Any change affecting mappings, derivations, schemas, or partitions includes
  **targeted verification examples**

### Preferred Workflow

1. **Plan first**
   - Identify impacted scripts, modules, or pipelines
   - Clarify assumptions and risks
2. **Design the smallest safe change**
   - Inline notes only (PR description or comments)
   - Do not create new documentation unless asked
3. **Implement minimal code**
4. **Validate**
   - Tests first
   - Then data validation as applicable
5. **Summarize**
   - What changed
   - How it was tested
   - Risks and assumptions

──────────────────────────────────────────────────────────────────────────────
## 3) TEST-DRIVEN DEVELOPMENT (DEFAULT EXPECTATION)
──────────────────────────────────────────────────────────────────────────────

For **all code behavior changes**, follow **TDD**.

### Red → Green → Refactor

1. **RED**
   - Write the smallest failing unit test that captures the desired behavior
   - Include edge cases where failure is plausible

2. **GREEN**
   - Implement the **minimum** code required to pass the test
   - Avoid premature abstraction or optimization

3. **REFACTOR**
   - Improve clarity, naming, and structure
   - Behavior must remain unchanged
   - All tests must stay green

### Test Quality Rules

- Tests must be **fast and isolated**
  - No real network calls
  - No real AWS calls
  - No real databases
  - No sleeps or timing dependencies
- Prefer:
  - Pure functions
  - Dependency injection
  - Small deterministic fixtures
- Assert **behavior**, not internal implementation details

### Data Pipeline Reality (Allowed Supplements)

TDD does **not** replace data validation for pipelines.

For pipeline work:
- Unit tests validate transformation logic
- Data validation confirms:
  - Schema consistency
  - Partition correctness
  - No unintended data loss or duplication

──────────────────────────────────────────────────────────────────────────────
## 4) LANGUAGE & TOOLING STANDARDS
──────────────────────────────────────────────────────────────────────────────

### Python Standards

- Test runner: `pytest`
- Coverage expectation: **≥ 80% on new or modified code**
- Formatting: `black`
- Linting: `ruff`
- Type checking: `mypy` (when applicable)

Preferred commands:
- Unit tests: `pytest -q`
- Full tests: `pytest`
- Lint: `ruff check .`
- Format: `black .`
- Types: `mypy .`

### Next.js / UI Standards (when applicable)

- Test runner: `jest` or `vitest` (pick one per project)
- Testing utilities: React Testing Library
- Type checking: `tsc`
- Linting: project-configured ESLint

Preferred commands:
- Unit tests: `pnpm test` (or npm/yarn)
- Type check: `pnpm typecheck`
- Lint: `pnpm lint`
- Build: `pnpm build`

──────────────────────────────────────────────────────────────────────────────
## 5) SECURITY & SAFETY REQUIREMENTS
──────────────────────────────────────────────────────────────────────────────

Always assume **production impact**.

- Treat all inputs as untrusted
- Validate and sanitize at boundaries
- Use parameterized queries and safe APIs
- Never log secrets or sensitive data
- Never commit credentials
- Use least-privilege assumptions
- Explicitly flag:
  - Schema or query injection risks
  - Path traversal
  - Unsafe deserialization
  - Privilege escalation
  - Cross-tenant or cross-site access issues

When uncertain, **call it out explicitly** and ask before proceeding.

──────────────────────────────────────────────────────────────────────────────
## 6) CLAUDE CODE OPERATIONAL RULES
──────────────────────────────────────────────────────────────────────────────

### Planning

- Use **Plan Mode** for any non-trivial change
- Propose:
  - Change plan
  - Test plan
  - Validation strategy
- Do not execute broad changes without confirmation

### Subagents

If available, use subagents for:
- Running tests
- Writing release notes
- Security review

Subagents must:
- Produce concise, scoped output
- Avoid speculative refactors or design changes

### Skills

When a skill is invoked (e.g. `/tdd`, `/pr`), follow it **exactly**.

### Background Tasks

Long-running commands (tests, builds, scans) may be run in the background.
Report only failures or actionable summaries.

### MCP Tools (External Integrations)

Claude Code has access to MCP servers for external service integration:

| MCP Server | Capabilities |
|------------|--------------|
| **GitHub** | Repos, PRs, issues, code search |
| **Atlassian** | Jira issues, Confluence pages |
| **AWS API** | All AWS CLI commands (readonly by default) |

Use MCP tools when:
- Accessing external services (GitHub, Jira, AWS)
- Querying data from cloud resources
- Reading documentation from Confluence

MCP Skills available:
- `/mcpm-aws-profile` - Configure AWS MCP profile
- `/mcpm-doctor` - Diagnose MCP issues
- `/mcpm-auth-reset` - Reset MCP authentication

──────────────────────────────────────────────────────────────────────────────
## 7) AGENT SECURITY GUARDRAILS
──────────────────────────────────────────────────────────────────────────────

Be explicit about:
- Which agent (main vs collaborator) handles a given action
- Gateway security module impact of any code change
- Credential scope — never widen what the bot can access
- Container isolation assumptions and blast radius

Never:
- Log or expose secrets (API keys, 1Password tokens, passwords)
- Silently remove or disable a security module
- Grant the bot container direct access to production credentials
- Route sensitive actions around the human approval queue

──────────────────────────────────────────────────────────────────────────────
## 8) ENVIRONMENT SETUP
──────────────────────────────────────────────────────────────────────────────

### Gateway (Python)

```bash
# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r gateway/requirements.txt

# Run tests
pytest gateway/tests/ -q

# Lint / format
ruff check .
black .
```

### Bot Container (Docker)

```bash
# Start all services
docker compose -f docker/docker-compose.yml up -d

# Check health
docker ps          # look for (healthy) on both containers
docker logs agentshroud-bot --tail 50

# Execute into bot
docker exec -it agentshroud-bot bash

# Restart after config changes
docker compose -f docker/docker-compose.yml restart agentshroud-bot
```

### MCP Servers (Claude Code)

MCP servers are configured in `.claude/settings.json`. They provide
GitHub, Atlassian (Jira/Confluence), and AWS access to Claude Code.
No additional setup is required if the MCP servers are already running.

──────────────────────────────────────────────────────────────────────────────
## 9) COMMUNICATION STANDARDS (TRADEMARK)
──────────────────────────────────────────────────────────────────────────────

All external communications must include a trademark statement.
Full templates are in [COMMUNICATION-TEMPLATES.md](COMMUNICATION-TEMPLATES.md).

### Quick Reference

| Context | Statement to append |
|---------|---------------------|
| PR descriptions, GitHub issues, Confluence | **Option 1** (default) |
| Telegram, Slack, quick replies | **Option 2** |
| First contact with any new collaborator | **Option 3** |
| README, docs, whitepapers | **Option 4** |

**Option 1 (default):**
> *AgentShroud™ is a trademark of Isaiah Jefferson. All rights reserved. Unauthorized use of the AgentShroud name, brand, or associated intellectual property is prohibited.*

**Option 2 (compact):**
> *AgentShroud™ — Proprietary & Confidential. © 2026 Isaiah Jefferson. All rights reserved.*

**Option 3 (collaborator first contact):**
> *This communication is issued under the AgentShroud™ project. AgentShroud™ is a trademark of Isaiah Jefferson, established February 2026. All project materials, methodologies, architectures, and associated intellectual property are proprietary and confidential. Participation as a collaborator does not transfer ownership, licensing rights, or any claim to the AgentShroud™ brand or codebase without a separate written agreement.*

**Option 4 (docs footer):**
> AgentShroud™ is a trademark of Isaiah Jefferson · First use February 2026 · All rights reserved
> Unauthorized use of the AgentShroud name or brand is strictly prohibited · Federal trademark registration pending

