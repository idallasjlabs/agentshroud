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

This repository implements a **Data Lakehouse platform** for extracting,
processing, validating, and serving operational data from distributed
energy storage systems.

### Primary Focus

**Data Lakehouse Pipelines**
- Extract data from multiple Central DAS (Data Acquisition System) instances
- Normalize, validate, and partition data
- Persist data in an S3-based lakehouse (Parquet + Athena)
- Emphasis on:
  - Schema stability
  - Partition correctness
  - Deterministic transformations
  - Backward compatibility

### Supporting / Optional Integrations (ONLY when explicitly requested)

**CTA API Integration**
- Interactive extraction from Fluence Central Terminal Application (CTA) REST APIs
- Used for real-time monitoring or device resource queries
- Not a primary workflow; treat as auxiliary

Do not assume CTA work unless explicitly requested.

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
- `/aws-mcp-profile` - Configure AWS MCP profile
- `/mcp-doctor` - Diagnose MCP issues
- `/mcp-auth-reset` - Reset MCP authentication

──────────────────────────────────────────────────────────────────────────────
## 7) DATA PLATFORM GUARDRAILS
──────────────────────────────────────────────────────────────────────────────

Be explicit about:
- DAS instances, arrays, and date ranges considered
- Partitioning and schema changes
- Athena table compatibility
- Backward compatibility risks

Never:
- Break schema compatibility silently
- Change partitioning without calling it out
- Reprocess large data ranges unless explicitly requested

──────────────────────────────────────────────────────────────────────────────
## 8) ENVIRONMENT SETUP
──────────────────────────────────────────────────────────────────────────────

### Conda Environment

```bash
conda env create -f environment/environment.yml
conda activate gsdl

# Platform-specific alternatives:
# environment/macos/conda_environment_macos.yml
# environment/linux/conda_environment_linux.yml
# environment/windows/conda_environment_windows.yml
