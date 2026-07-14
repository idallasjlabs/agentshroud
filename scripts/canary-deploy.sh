#!/usr/bin/env bash
# scripts/canary-deploy.sh — Blue/green canary deploy with auto-rollback (SCRUM-62)
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#
# Deploys a new git ref to the GREEN (canary) instance — the `agentshroud-bot`
# UNIX account's stack on marvin (gateway :9080, containers agentshroud-marvin-*)
# — validates it with scripts/post-deploy-check.sh, and AUTO-ROLLS-BACK to the
# previously-deployed ref on any failure.  The BLUE (production) instance
# (`ijefferson.admin`, gateway :8080) is NEVER touched, so a bad deploy can
# never take down the only production instance.
#
# The canary is validated first; only after GREEN is proven healthy should BLUE
# be promoted to the same ref (a separate, human-gated step).
#
# Usage:
#   scripts/canary-deploy.sh [--ref <git-ref>] [--dry-run] [--repo <path>]
#     --ref      git ref to deploy to GREEN (default: origin/main)
#     --dry-run  print every action, change nothing (safe to run anywhere)
#     --repo     GREEN checkout path (default: $HOME/agentshroud)
#
# Safety:
#   * refuses to run unless USER=agentshroud-bot (the GREEN account) OR --dry-run
#   * tags pre-deploy-<UTC> on the pre-deploy ref before touching anything
#   * on post-deploy-check failure, restores the previous ref and re-deploys GREEN
#
# Cross-platform: POSIX bash, works on macOS (Colima) and Linux.

set -euo pipefail

# ── Args ──────────────────────────────────────────────────────────────────
REF="origin/main"
DRY_RUN=0
REPO="${HOME}/agentshroud"
REPO_URL="${AGENTSHROUD_REPO_URL:-git@github.com:idallasjlabs/agentshroud.git}"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --ref) REF="$2"; shift 2 ;;
        --dry-run) DRY_RUN=1; shift ;;
        --repo) REPO="$2"; shift 2 ;;
        -h|--help) sed -n '2,40p' "$0"; exit 0 ;;
        *) echo "unknown arg: $1" >&2; exit 2 ;;
    esac
done

log() { echo "  [canary-deploy] $*"; }
die() { echo "  [canary-deploy] ERROR: $*" >&2; exit 1; }

# Execute a command array directly (NO eval — no injection surface from --ref).
# Honors --dry-run by printing a shell-quoted preview and changing nothing.
run() {
    if [[ "$DRY_RUN" == "1" ]]; then
        printf '  [dry-run]'
        printf ' %q' "$@"
        printf '\n'
    else
        "$@"
    fi
}

# Run a command with the GREEN repo as cwd (for `asb`, which resolves its
# compose override from the working tree). Subshell keeps our cwd unchanged.
run_in_repo() {
    if [[ "$DRY_RUN" == "1" ]]; then
        printf '  [dry-run] (cd %q &&' "$REPO"
        printf ' %q' "$@"
        printf ')\n'
    else
        ( cd "$REPO" && "$@" )
    fi
}

# ── Guards ────────────────────────────────────────────────────────────────
# GREEN only.  Never deploy through this script as the BLUE (prod) user.
if [[ "$DRY_RUN" != "1" && "${USER:-}" != "agentshroud-bot" ]]; then
    die "must run as the GREEN account 'agentshroud-bot' (got '${USER:-?}'). Blue/prod is off-limits to this script. Use --dry-run to preview."
fi

command -v git >/dev/null || die "git not found"
command -v docker >/dev/null || die "docker not found"

UTC="$(date -u +%Y%m%dT%H%M%SZ)"
TAG="pre-deploy-${UTC}"

log "GREEN canary deploy — ref=${REF}, repo=${REPO}, dry_run=${DRY_RUN}"

# ── First-run: clone GREEN checkout if absent ─────────────────────────────
if [[ ! -d "${REPO}/.git" ]]; then
    log "no checkout at ${REPO} — first-run clone"
    run git clone "${REPO_URL}" "${REPO}"
fi

if [[ "$DRY_RUN" == "1" && ! -d "${REPO}/.git" ]]; then
    log "dry-run: would operate in freshly-cloned ${REPO}; skipping git state inspection"
    ROLLBACK_REF="<current-green-HEAD>"
else
    # Record the ref GREEN is currently on, so we can roll back to it.
    ROLLBACK_REF="$(git -C "${REPO}" rev-parse HEAD 2>/dev/null || echo '')"
    [[ -n "$ROLLBACK_REF" ]] || ROLLBACK_REF="origin/main"
fi
log "rollback anchor (current GREEN ref): ${ROLLBACK_REF}"

# ── Fetch + tag the rollback anchor ───────────────────────────────────────
run git -C "${REPO}" fetch --tags --prune origin
run git -C "${REPO}" tag -f "${TAG}" "${ROLLBACK_REF}"
run git -C "${REPO}" push -f origin "${TAG}" || log "note: could not push tag ${TAG} (continuing)"
log "tagged rollback anchor ${TAG} -> ${ROLLBACK_REF}"

# ── Deploy the new ref to GREEN ───────────────────────────────────────────
deploy_ref() {
    local ref="$1"
    run git -C "${REPO}" checkout -f "${ref}"
    # `asb rebuild` builds + brings the stack up AND auto-runs post-deploy-check
    # (see scripts/post-deploy-check.sh docstring). It exits non-zero on failure.
    run_in_repo scripts/asb rebuild
}

log "deploying ${REF} to GREEN…"
if deploy_ref "${REF}"; then
    log "✅ GREEN canary healthy on ${REF} — post-deploy-check passed."
    log "Next (human-gated): promote BLUE/prod to ${REF} once you're satisfied with the canary."
    exit 0
fi

# ── Auto-rollback ─────────────────────────────────────────────────────────
log "❌ GREEN canary FAILED post-deploy-check on ${REF} — rolling back to ${ROLLBACK_REF}"
if deploy_ref "${ROLLBACK_REF}"; then
    log "↩️  GREEN restored to ${ROLLBACK_REF}. BLUE/prod was never touched."
else
    die "ROLLBACK ALSO FAILED — GREEN may be down. BLUE/prod is still untouched (:8080). Investigate manually; rollback anchor tag=${TAG}."
fi
exit 1
