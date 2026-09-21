#!/bin/bash
# AgentShroud pre-commit hook — runs gitleaks on staged changes
#
# DO NOT INSTALL THIS BY COPYING IT OVER .git/hooks/pre-commit.
# That path has exactly one owner: the pre-commit framework, driven by
# .pre-commit-config.yaml (which already runs gitleaks). Copying this file
# there displaces gitleaks, detect-secrets, ruff, black and semgrep in one
# move — that is precisely how Semgrep SAST came to be enforced nowhere while
# the PR template still asked authors to attest it passed (fixed 2026-09-20).
#
# Install with:  .llm_settings/git-hooks/install.sh   (additive, idempotent)
# This file is kept only as a standalone scanner for environments that have no
# pre-commit available; run it directly: bash scripts/pre-commit-hook.sh

set -e

# Check if gitleaks is installed
if ! command -v gitleaks &> /dev/null; then
    # Was `exit 0` until 2026-09-20: a missing scanner reported the same
    # success as a clean scan, so this hook passed every commit on any machine
    # without gitleaks. A no-op must be distinguishable from a success
    # (CLAUDE.md 0.0 rule 2). Nix, not brew, per CLAUDE.md section 5.
    echo "❌ gitleaks not found — cannot scan for secrets, refusing to pass" >&2
    echo "   Install: nix develop   (or: nix profile install nixpkgs#gitleaks)" >&2
    exit 1
fi

echo "🔐 Running gitleaks on staged changes..."

# Scan only staged changes (not entire history)
gitleaks protect --staged --config gitleaks.toml --verbose

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ BLOCKED: Secrets detected in staged files!"
    echo ""
    echo "Options:"
    echo "  1. Remove the secret and use env vars / 1Password instead"
    echo "  2. Add a false positive to gitleaks.toml [allowlist]"
    echo "  3. Skip this check (NOT recommended): git commit --no-verify"
    echo ""
    exit 1
fi

echo "✅ No secrets found — commit allowed"
