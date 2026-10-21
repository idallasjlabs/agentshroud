---
name: i-prod-safety
description: "DEPRECATED — use /i-release-gate. Alias for the former production-safety checks (blast radius, rollback path, pre/post-deploy gates). Redirects to the i-release-gate agent and its release-check.sh, smoke.sh and sbom-verify.sh gates."
---

> **[Copilot Standalone Mode]** Complete this task using direct MCP tool calls.
> Do **not** invoke or reference other agents by name — all capabilities are
> available through the MCP tools configured in `.github/mcp.json`.


# Skill: Production Safety (PROD-SAFETY)

> **DEPRECATED (kept as an alias for one release):** use `/i-release-gate` instead.

The production-safety checks now live in the testing agent suite:

| Former check | Replacement |
|---|---|
| Pre/post-deploy checklists, rollback verified | `/i-release-gate` (`scripts/testing/release-check.sh`, `smoke.sh`) |
| Blast radius, rollback path, test isolation, cost guards in review | `/i-code-reviewer` (`scripts/testing/impact-map.sh`) |
| Incident response and severity matrix | `/i-production` (unchanged) |
| Pre/post-deployment gate (backup, smoke) | `/i-ps` (unchanged) |

Invoke `/i-release-gate` and follow its playbook.
