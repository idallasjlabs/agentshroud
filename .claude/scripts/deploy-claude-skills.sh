#!/usr/bin/env bash
# =============================================================================
# deploy-claude-skills.sh
#
# Deploys Claude Code skills for the SecureClaw project.
# Enforces: Test-Driven Development | Security Review | Production Safety
#
# Usage:
#   ./deploy-claude-skills.sh            # deploy
#   ./deploy-claude-skills.sh --dry-run  # preview only
#   ./deploy-claude-skills.sh --clean    # remove and redeploy
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)/skills"
DRY_RUN=false
CLEAN=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --clean)   CLEAN=true; shift ;;
    -h|--help) echo "Usage: $0 [--dry-run] [--clean]"; exit 0 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

write_skill() {
  local dir="$1" content="$2"
  local fpath="$SKILLS_ROOT/$dir/SKILL.md"
  if $DRY_RUN; then echo "[DRY RUN] $fpath"; return; fi
  mkdir -p "$SKILLS_ROOT/$dir"
  printf '%s\n' "$content" > "$fpath"
  echo "  ✓ $dir/SKILL.md"
}

if $CLEAN && ! $DRY_RUN; then
  [ -d "$SKILLS_ROOT" ] && rm -rf "$SKILLS_ROOT"
fi

echo "Deploying SecureClaw skills to $SKILLS_ROOT/"

# TDD Skill
read -r -d '' SKILL_TDD << 'END' || true
# Skill: Test-Driven Development (TDD)

## Core Discipline: Red → Green → Refactor
1. **RED** — Write a failing test first. Confirm it fails for the right reason.
2. **GREEN** — Write the minimum code to pass. No speculative features.
3. **REFACTOR** — Clean up while tests stay green.

## Rules
- Never skip RED. If you wrote implementation first → delete it, write the test.
- One behaviour per test.
- Descriptive names: `test_<unit>_<scenario>_<expected_result>`
- Test the interface, not the implementation.
- Coverage target: ≥ 80% on new code, ≥ 90% on security modules.
END
write_skill "tdd" "$SKILL_TDD"

# Security Review Skill
read -r -d '' SKILL_SEC << 'END' || true
# Skill: Security Review (SEC)

## Role
Senior security reviewer for SecureClaw — a security proxy for AI agents.

## Focus Areas
1. **Credential handling** — no hardcoded secrets, use 1Password/env
2. **Input validation** — injection, traversal, SSRF, XSS
3. **Container security** — least privilege, read-only fs, seccomp
4. **PII protection** — Presidio integration, sanitizer coverage
5. **Audit trail** — all actions logged, tamper-resistant
6. **Network isolation** — containers properly segmented

## Output
For each finding: `[SEVERITY] file:line — Description + Suggested fix`
Severities: CRITICAL, HIGH, MEDIUM, LOW, INFO
END
write_skill "sec" "$SKILL_SEC"

# Code Review Skill
read -r -d '' SKILL_CR << 'END' || true
# Skill: Code Review (CR)

## Review Principles
1. Security-critical areas get extra scrutiny
2. The 400-line rule: flag PRs exceeding 400 LoC
3. Functionality, performance, readability
4. Static analysis: OWASP Top 10

## Output
- Review Summary: Pass / Request Changes
- Security Audit
- Detailed comments with suggested fixes
END
write_skill "cr" "$SKILL_CR"

# Environment Manager Skill
read -r -d '' SKILL_ENV << 'END' || true
# Skill: Environment Manager (ENV)

## Responsibilities
- Docker container configuration and health
- 1Password CLI integration
- Dependency management (conda, pip, npm)
- Pi-specific constraints (ARM64, 8GB RAM, 2GB swap)
- Shell configuration (zsh, env vars)
END
write_skill "env" "$SKILL_ENV"

# Project Manager Skill
read -r -d '' SKILL_PM << 'END' || true
# Skill: Project Manager (PM)

## Responsibilities
- Phase tracking and milestone updates
- Peer review process coordination
- iCloud Calendar/Reminders sync
- Memory and documentation maintenance
- Risk assessment and blocker tracking
END
write_skill "pm" "$SKILL_PM"

if $DRY_RUN; then echo "Dry run complete — no files written."; else echo "✓ All skills deployed"; fi
