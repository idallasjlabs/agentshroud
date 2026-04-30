# Multi-Agent Role Matrix

This document is the single source of truth for which AI agent is authorized
to perform which class of task in the AgentShroud repository.

Role gates are enforced in each agent's context file:
- Claude Code: `CLAUDE.md` § 0.1 + `.claude/settings.json` hooks
- Gemini CLI: `.gemini/GEMINI.md` § 0 (PRIME DIRECTIVE)
- Codex: `.codex/AGENTS.md` (role banner)

---

## Authorization Matrix

| Task type | Claude Code | Gemini CLI | Codex |
|-----------|-------------|------------|-------|
| Architecture decisions | **Allowed** | Defer to Claude | Defer to Claude |
| New feature implementation | **Allowed** | Blocked | Blocked |
| Bug fix | **Allowed** | Blocked | Blocked |
| Schema / API design | **Allowed** | Defer to Claude | Defer to Claude |
| Large refactor (>10 lines) | **Allowed** | Blocked | Blocked |
| Small safe refactor (<10 lines, after tests pass) | **Allowed** | **Allowed** | **Allowed** |
| Test augmentation (add edge cases, missing tests) | **Allowed** | **Allowed** | **Allowed** |
| Validation run (execute commands, report results) | **Allowed** | **Allowed** | **Allowed** |
| Documentation (new files) | **Allowed** (only if requested) | Blocked | Blocked |
| Security module changes (`gateway/security/**`) | **Allowed** | Blocked | Blocked |
| Docker / compose changes | **Allowed** | Blocked | Blocked |
| CI/CD workflow changes | **Allowed** | Blocked | Blocked |
| Commit + PR creation | **Allowed** | Blocked | Blocked |
| Secret / credential handling | **Allowed** (R2 enforced) | Blocked | Blocked |

---

## Escalation Path

When Gemini or Codex encounters a task that is outside its authorized scope:

1. **Stop.** Do not attempt the task.
2. **Report** the task type and why it exceeds the secondary/tertiary scope.
3. **Defer:** "This requires Claude Code (primary developer). Please route this
   task to Claude Code."
4. If the user overrides and explicitly asks Gemini/Codex to proceed anyway,
   output a one-line warning before executing:
   `[ROLE OVERRIDE] This task is outside secondary/tertiary scope per AGENT_ROLES.md.`

---

## Security-Sensitive Paths

These paths require Claude Code (primary) regardless of task type:

| Path | Reason |
|------|--------|
| `gateway/security/**` | 76 active security modules — IEC 62443 FR3/FR6 |
| `gateway/approval_queue/**` | Human-in-the-loop routing |
| `docker/setup-secrets.sh` | Secret storage hygiene |
| `docker/config/openclaw/apply-patches.js` | Bot configuration injection |
| `.claude/scripts/claude-hooks/` | Harness enforcement scripts |
| `.claude/settings.json` | Hook registry + deny-list |

---

## Decision Tree for New Tasks

```
Incoming task
├── Is it architecture / schema / feature / large refactor?
│   └── → Claude Code only
├── Is it a security-sensitive path?
│   └── → Claude Code only
├── Is it test augmentation or validation?
│   └── → Gemini or Codex OK
├── Is it a small safe refactor (tests already pass, <10 lines)?
│   └── → Gemini or Codex OK (with user confirmation)
└── Unsure?
    └── → Default to Claude Code, explain why
```

---

## References

- Full role description: `CLAUDE.md` § 0.1 (Multi-Agent Hierarchy)
- Gemini gate: `.gemini/GEMINI.md` § 0 (PRIME DIRECTIVE)
- Codex gate: `.codex/AGENTS.md` (role banner at top)
- Workflow rules: `~/.claude/projects/.../memory/workflow_rules.md`
