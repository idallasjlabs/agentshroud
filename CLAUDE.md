# CLAUDE.md
#
# Guidance for Claude Code (claude.ai/code) when working in this repository.
# These instructions are authoritative. Follow them strictly.
# Keep actions deterministic, minimal, and aligned with how this repo is actually run.
#
# Applies to: Claude Code (primary) · Gemini CLI (secondary) · Codex CLI (tertiary)

──────────────────────────────────────────────────────────────────────────────
## KNOWLEDGE MAP — READ THIS FIRST
──────────────────────────────────────────────────────────────────────────────

At the start of every session, the knowledge graph for this project lives here:

| Vault | Path | Contents |
|-------|------|----------|
| Code architecture | `.obsidian-vaults/code-architecture/` | Module map, dependency graph, git log, ADRs |
| Business | `.obsidian-vaults/business/` | Roadmap, competitive intel, IP/trademark notes |
| Personal | `.obsidian-personal/` | Session logs, research, AI-CONTEXT notes |

**Entry points:**
- Module index: `.obsidian-vaults/code-architecture/modules/`
- Recent commits: `.obsidian-vaults/code-architecture/git-log/recent-commits.md`
- Current roadmap: `.obsidian-vaults/business/roadmap.md`
- Session context: `.obsidian-personal/AI-CONTEXT/`

Do not ask where files are. Read the module index first.

──────────────────────────────────────────────────────────────────────────────
## 0) PRIME DIRECTIVE (NON-NEGOTIABLE)
──────────────────────────────────────────────────────────────────────────────

- **Do NOT create new files** unless absolutely required to satisfy the request.
- **Prefer modifying existing files** over adding new ones.
- **Never create documentation files** (`*.md`, README, design docs) unless the
  user explicitly asks for documentation.
- If a new file is genuinely required:
  - Explain **why**
  - Propose the **minimum viable file**
  - Wait for confirmation before creating it
- Never broaden scope beyond the explicit request.
- Never perform opportunistic refactors.

If instructions conflict, follow this file over all other guidance.

──────────────────────────────────────────────────────────────────────────────
## 0.1) MULTI-AGENT HIERARCHY
──────────────────────────────────────────────────────────────────────────────

**Claude Code is the PRIMARY developer in this repository.**

| Role | Agent | Owns |
|------|-------|------|
| Primary | Claude Code | Architecture, feature impl, schema/API design, complex refactors, documentation strategy, code ownership |
| Secondary | Gemini CLI | Document analysis, cross-referencing, pattern extraction, research |
| Tertiary | GPT/Codex | Test augmentation, validation runs, safe refactors after tests pass |

**Gemini/Codex defer to Claude on:**
- Architectural questions
- Schema or API changes
- Large refactors
- Feature decisions

**Gemini/Codex may own:**
- Test coverage improvements
- Validation execution
- Bug reproduction
- Small safe refactors (variable naming, helper extraction) after tests pass

Never delegate primary development to Gemini or Codex.

Configuration locations:
- Claude Code: `.claude/`
- Gemini CLI: `.gemini/settings.json` + `.gemini/GEMINI.md`
- Codex CLI: `.codex/config.toml` + `.codex/AGENTS.md`

──────────────────────────────────────────────────────────────────────────────
## 1) PROJECT IDENTITY
──────────────────────────────────────────────────────────────────────────────

| Field | Value |
|-------|-------|
| **Product** | AgentShroud™ — Enterprise Governance Proxy for Autonomous AI Agents |
| **Trademark** | AgentShroud™ — Isaiah Dallas Jefferson, Jr. — Federal registration pending |
| **CIE** | Isaiah Jefferson |
| **Current Branch** | `feat/v1.0.0` ("Fortress") |
| **Current Version** | v1.0.0 |
| **Language** | Python 3.9+ |
| **Test Coverage** | 94% — 3,724+ tests total; maintain or improve |

AgentShroud sits as a transparent proxy between AI agents and the systems they
interact with. Every API call, file write, cloud change, and tool invocation is
intercepted, inspected, logged, and policy-enforced without disrupting the agent's
native workflow.

```
AI Agent → AgentShroud Gateway (76 security modules) → Target System
```

Control surfaces: Telegram, iOS Shortcuts, Browser Extension, SSH, REST API — all over Tailscale.

──────────────────────────────────────────────────────────────────────────────
## 2) ⚠️ NO SECURITY THEATER (NON-NEGOTIABLE)
──────────────────────────────────────────────────────────────────────────────

AgentShroud is a security product. Security theater ships vulnerabilities while
hiding them behind green checkmarks. These rules apply to every task, every session,
every file you touch.

### RULE A — NO STUBS. NO PLACEHOLDERS. NO FAKE GREEN.

Prohibited:
- `pass`, `TODO`, `FIXME`, `raise NotImplementedError`, placeholder returns in
  any file committed to a non-draft branch
- `@pytest.mark.skip`, `xit(`, `test.skip(`, `#TODO: implement` counted as passing
- Hardcoded mock data in a function documented as production logic
- Functions that always return `True` / `None` / `{}` without comment
- Files that import a module but never call it, claimed as integration

If you cannot implement something fully:
1. Say so explicitly: "I cannot implement X because [specific reason]"
2. Leave a `STUB: [reason] — NOT PRODUCTION READY` comment
3. Create a failing test that proves the stub is not production ready
4. Flag in status report as `❌ STUB — NOT PASSING`

### RULE B — VERIFY BEFORE CLAIMING. CITE FILES AND LINES.

Every claim about the codebase requires a file path and line number.
- Do NOT say "the module handles X" — say "`gateway/security/X.py:42` handles X"
- Do NOT declare a feature "integrated" without showing the call chain
- Do NOT report a test as passing without showing actual test output

### RULE C — INTEGRATION PROOF FORMAT

When claiming something is integrated, provide all five lines:

```
1. Entry point:    [file:line] where the call originates
2. Routing:        [file:line] where it is dispatched
3. Handler:        [file:line] where the logic executes
4. Test:           [test_file:line] test name + result
5. Evidence:       pytest output or log snippet showing real execution
```

### RULE D — TEST TABLE FORMAT FOR STATUS REPORTS

| Module | Test File | Test Name | Status | Evidence |
|--------|-----------|-----------|--------|----------|
| PromptGuard | `tests/test_prompt_guard.py` | `test_injection_blocked` | ✅ PASS | `1 passed in 0.03s` |

No row may show ✅ without a real test name and real output. A skip marker is ❌.

### RULE E — DEFINITION OF DONE

Done means ALL of:
- ✓ Real implementation — no stubs
- ✓ Unit tests pass, no skip markers
- ✓ Integration proof (all five lines)
- ✓ Status report: GO with test output
- ✓ No existing tests broken
- ✓ Coverage ≥ 94%

NOT done:
- ✗ "Tests coming next session"
- ✗ "Wired up but not tested end-to-end"
- ✗ "Should work based on the architecture"

──────────────────────────────────────────────────────────────────────────────
## 3) SDLC — HOW TO WORK IN THIS REPO
──────────────────────────────────────────────────────────────────────────────

### Preferred workflow

1. **Plan first** — identify impacted files, state assumptions and risks
2. **Design the smallest safe change** — inline notes only, no new docs unless asked
3. **Implement minimal code**
4. **Validate** — tests first, then integration proof
5. **Summarize** — what changed, how tested, risks and assumptions

### Session start checklist

Before writing any code:
1. List the top-level project structure
2. Read this file (`CLAUDE.md`)
3. Read `AI-CONTEXT/NO-SECURITY-THEATER.md` if present
4. Declare: what you know about the codebase, what you don't
5. State your task and your definition of done for it

──────────────────────────────────────────────────────────────────────────────
## 4) TEST-DRIVEN DEVELOPMENT (DEFAULT)
──────────────────────────────────────────────────────────────────────────────

For all code behavior changes, follow TDD strictly.

### Red → Green → Refactor

1. **RED** — write the smallest failing unit test that captures the desired behavior
2. **GREEN** — implement the minimum code required to pass the test
3. **REFACTOR** — improve clarity; behavior must remain unchanged; all tests stay green

### Test quality rules

- No real network calls, no real AWS calls, no real databases, no sleeps
- Prefer pure functions, dependency injection, small deterministic fixtures
- Assert behavior, not internal implementation details
- Coverage: **≥ 94%** on new or modified code (AgentShroud floor, higher than default 80%)

──────────────────────────────────────────────────────────────────────────────
## 5) LANGUAGE & TOOLING STANDARDS
──────────────────────────────────────────────────────────────────────────────

### Python

- Test runner: `pytest`
- Coverage floor: **94%** on new or modified code
- Formatting: `black`
- Linting: `ruff`
- Type checking: `mypy` where applicable
- SAST: `semgrep` (`.semgrep.yml` — CWE-78, CWE-22, CWE-798, CWE-918, CWE-502, SQL injection)

```bash
pytest -q                        # unit tests
pytest --cov=gateway --cov-report=term-missing  # with coverage
ruff check .                     # lint
black .                          # format
mypy .                           # types
scripts/security-scan.sh         # SAST
```

### Provisioning philosophy

**NEVER suggest:**
- `apt-get install`
- `brew install`
- Manual `export` commands

**ALWAYS provide:**
- Nix expressions
- Home Manager modules
- Flake configurations

### Cross-platform requirement

Bash/zsh scripts must work on macOS and Linux without modification.

──────────────────────────────────────────────────────────────────────────────
## 6) SECURITY & SAFETY REQUIREMENTS
──────────────────────────────────────────────────────────────────────────────

Always assume production impact.

- Treat all inputs as untrusted; validate and sanitize at boundaries
- Use parameterized queries and safe APIs
- Never log secrets or sensitive data
- Never commit credentials — use environment variables and secret managers
- Use least-privilege assumptions throughout
- Explicitly flag: schema injection, query injection, path traversal,
  unsafe deserialization, privilege escalation, cross-tenant access

When uncertain, call it out explicitly and ask before proceeding.

──────────────────────────────────────────────────────────────────────────────
## 7) AGENTSHROUD-SPECIFIC CONSTRAINTS
──────────────────────────────────────────────────────────────────────────────

### 76 Active Security Modules — No Stubs

| Tier | Modules |
|------|---------|
| P0 Core | PromptGuard, TrustManager, EgressFilter, PII Sanitizer, Gateway Binding |
| P1 Middleware | SessionManager, TokenValidator, ConsentFramework, SubagentMonitor, AgentRegistry, Delegation, SharedMemory, ToolACL, PrivacyPolicy, RBAC + others |
| P2 Network | EgressFilter, EgressApproval, DNSFilter, NetworkValidator, WebContentScanner |
| P3 Infrastructure | AlertDispatcher, DriftDetector, EncryptedStore, KeyVault, Canary, ClamAV, Trivy, Falco, Wazuh, HealthReport, ProgressiveLockdown, ConfigIntegrity |

### Hard constraints

1. **Trademark** — Never remove or alter AgentShroud™ trademark notices
2. **Coverage** — Must stay ≥94%; all new code requires tests before merge
3. **No module stubs** — every security module must be fully wired in the pipeline; no dead code
4. **IEC 62443 alignment** — security changes must reference IEC 62443 Foundational Requirements (FRs)
   - FR3 → SL3: Cosign / Trivy / Falco / Semgrep
   - FR6 → SL3: SHA-256 hash chain + Wazuh
   - FR7 → SL2
5. **Semgrep** — new code must pass `.semgrep.yml` SAST rules
6. **Docker sidecar integrity** — do not remove or stub `falco`, `clamav`, `wazuh-agent`, or `fluent-bit`
7. **Approval queue** — any agent action touching `email_sending`, `file_deletion`, `external_api_calls`, or `skill_installation` must route through the approval queue
8. **PII redaction** — presidio engine at 0.9 confidence minimum; do not lower threshold
9. **Performance baseline** — maintain `.benchmarks/baseline-v1.0.0.json`; inbound latency <0.5ms on arm64/macOS

### Key source directories

| Path | Contents |
|------|----------|
| `gateway/` | Core proxy, runtime, approval queue, ingest API, SSH proxy |
| `gateway/security/` | All 76 security modules |
| `gateway/soc/` | SOC collaboration features |
| `gateway/proxy/` | Request interception and routing |
| `gateway/runtime/` | Agent runtime management |
| `gateway/approval_queue/` | Human-in-the-loop approval workflow |
| `gateway/web/` | Web control center (7-page dashboard) |
| `dashboard/` | Terminal control center (TUI + chat console) |
| `cli/` | CLI interface |
| `chatbot/` | Telegram bot |
| `browser-extension/` | Browser extension |
| `docker/` | Container stack (Falco, ClamAV, Wazuh, Fluent Bit) |
| `scripts/` | Build, security scan, deployment scripts |
| `gateway/tests/` | Primary test suite |

### Development commands

```bash
# Full test suite
pytest

# With coverage
pytest --cov=gateway --cov-report=term-missing

# Lint + format
ruff check .
black .

# Security scan
scripts/security-scan.sh

# Start gateway
docker-compose -f docker-compose.secure.yml up

# Start with security sidecars
docker-compose -f docker-compose.sidecar.yml up
```

──────────────────────────────────────────────────────────────────────────────
## 8) OUTPUT FORMATTING CONTRACT
──────────────────────────────────────────────────────────────────────────────

Every response must include:
1. **Executive summary** — 1–3 sentences at the top
2. **Structured breakdown** — tables, lists, code blocks
3. **Acronym expansion** — expand all acronyms on first use
4. **Risk callouts** — security, cost, operational implications
5. **Verification steps** — how to test/validate the output

| Output type | Format |
|-------------|--------|
| Summaries | Markdown tables |
| Scripts | Copy-paste ready with headers |
| Documentation | Clean Markdown (Obsidian-compatible) |
| Code | Production-ready with error handling |
| Commands | bash/zsh compatible on macOS and Linux |

### Avoid

- Conversational filler ("Let me help you with that!")
- Superficial advice without actionable steps
- Unstructured output (walls of text)
- Excessive praise or emotional validation
- Creating new files when editing existing ones would suffice
- Broadening scope beyond the explicit request
- Assuming requirements instead of clarifying

──────────────────────────────────────────────────────────────────────────────
## 9) GOVERNANCE & DECISION-MAKING
──────────────────────────────────────────────────────────────────────────────

Standards in scope: NIST CSF, IEC 62443, OWASP Top 10 for Agentic Applications,
MITRE ATLAS, CSA MAESTRO, NIST AI RMF, CIS Docker Benchmark, NIST SP 800-190.

### When to act

Proceed immediately when: request is clear and scoped, solution is well-established,
change is low-risk and reversible, you have all necessary context.

### When to clarify

Ask when: requirements are ambiguous, multiple valid approaches exist, architectural
decision required, security implications unclear, scope could be interpreted multiple ways.

### When to defer

Escalate to Isaiah when: production data at risk, breaking change proposed,
governance/compliance implications, cross-team coordination required.

**Do not change timelines to hide lateness. Honest status only.**

──────────────────────────────────────────────────────────────────────────────
## 10) CLAUDE CODE OPERATIONAL RULES
──────────────────────────────────────────────────────────────────────────────

- Use **Plan Mode** for any non-trivial change; propose change plan, test plan,
  and validation strategy before executing
- Subagents must produce concise scoped output; no speculative refactors
- When a skill is invoked (e.g. `/tdd`, `/pr`), follow it exactly
- Long-running commands may run in the background; report only failures or
  actionable summaries

### MCP tools available

| MCP Server | Capabilities |
|------------|--------------|
| GitHub | Repos, PRs, issues, code search |
| Atlassian | Jira issues, Confluence pages |

MCP skills: `/mcpm-doctor`, `/mcpm-auth-reset`
