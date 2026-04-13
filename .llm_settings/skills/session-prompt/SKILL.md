# Skill: Session Prompt Generator (SESSION-PROMPT)

## Role
You are a Project Context Analyst. Your job is to survey a repository,
extract the information that an LLM needs to work effectively in it,
and produce a `SESSION_PROMPT.md` that gets injected into all three
LLM context files (CLAUDE.md, .gemini/GEMINI.md, .codex/AGENTS.md).

## Trigger
Use this skill when the user says any of:
- `/session-prompt`
- "create a session prompt"
- "generate SESSION_PROMPT.md"
- "set up session context for this repo"

## Workflow: Survey → Draft → Inject → Confirm

### Step 1 — Survey the Repo

Read the following in order (skip gracefully if absent):

1. `README.md` — product identity, architecture overview, key features
2. `CHANGELOG.md` — current version, recent additions, active branch context
3. Primary config file (e.g., `*.yaml`, `*.toml`, `pyproject.toml`, `package.json`)
4. Top-level directory listing — identify source structure
5. `CLAUDE.md` — any repo-specific rules already captured
6. `.env.example` or equivalent — environment variable surface

Do **not** read every file. Read enough to answer the six questions below.

### Step 2 — Answer Six Questions

Before writing, resolve:

1. **What is this project?** (1-2 sentences: product, purpose, owner)
2. **What is the current version / active branch?** (version, milestone, release name)
3. **What are the key source directories?** (table of path → contents)
4. **What is actively being built right now?** (current sprint/tranche/feature set)
5. **What are the hard constraints?** (coverage thresholds, security rules, standards, don't-break items)
6. **What are the dev commands?** (test, lint, build, deploy)

### Step 3 — Write SESSION_PROMPT.md

Use the template below. Fill every section from your survey.
Omit sections that genuinely don't apply — do not leave placeholders.
Keep total length under 150 lines.

```markdown
# <Project Name> — Session Context

## Project Identity

| Field | Value |
|-------|-------|
| **Product** | <one-line description> |
| **Current Version** | <version> |
| **Current Branch** | <branch name and milestone if any> |
| **Language** | <primary language and version> |
| **Test Coverage** | <target %>; <total test count if known> |

---

## Architecture Summary

<2-4 sentences describing how the system works end-to-end.>

```
<ASCII diagram if one exists in README, otherwise omit>
```

---

## Key Source Directories

| Path | Contents |
|------|----------|
| `<path>/` | <what lives here> |

---

## Active Work — <Version or Sprint Name>

<Bullet list or table of what is actively being built, with key file references.>

---

## Constraints for This Repository

<Numbered list of hard rules: coverage floors, security standards,
trademark notices, schema compatibility, approval workflows, etc.
Only include rules that are genuinely enforced — not aspirational.>

---

## Development Commands

\`\`\`bash
# <comment>
<command>
\`\`\`

---

## <Optional: Roadmap / Next Milestone>

<1 short paragraph if relevant. Omit if not.>
```

### Step 4 — Write the File

Write `SESSION_PROMPT.md` to the **repo root** (current working directory).

### Step 5 — Inject into All Three LLMs

Run the injection script:

```bash
.llm_settings/scripts/session-prompt-setup.sh
```

If the script is not present, llm-init has not been run yet. Warn the user
and instruct them to run `llm-init` first, then re-run this skill.

### Step 6 — Confirm

Report:
- Path to `SESSION_PROMPT.md`
- Which targets were injected (CLAUDE.md, .gemini/GEMINI.md, .codex/AGENTS.md)
- Any targets that were skipped and why

---

## Rules

- **Survey before writing.** Never generate from assumptions.
- **No placeholders.** Every field must be filled or the section omitted.
- **Under 150 lines.** Dense and accurate beats comprehensive and speculative.
- **Hard constraints only.** If a rule isn't enforced by a tool, test, or team norm, leave it out.
- **Do not commit** SESSION_PROMPT.md unless the user asks. It may contain
  branch-specific context that should not be pushed to all branches.
- **Idempotent.** If SESSION_PROMPT.md already exists, read it first, update
  only what has changed, and re-inject. Do not start from scratch.

---

## Re-injection Command (for reference)

After editing SESSION_PROMPT.md manually, users can re-inject at any time:

```bash
.llm_settings/scripts/session-prompt-setup.sh
```

To remove the injected block from all targets:

```bash
.llm_settings/scripts/session-prompt-setup.sh --remove
```
