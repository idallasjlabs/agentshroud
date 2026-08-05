#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/update-bot-agents.sh — push repo skills/agents/MCP edits into the
# LIVE running bots, without a rebuild and (for skills) without even a restart.
#
# Workflow this supports: edit .llm_settings/{skills,agents,mcp}/ in the repo,
# run this script, done. No full `asb rebuild` (which took every bot offline
# for ~40 minutes during a real incident this session) is needed just to pick
# up a skill/agent/MCP-config change.
#
# What it does, in order:
#   1. Copies repo .llm_settings/{skills,agents,mcp}/ -> ~/.llm_settings/ (the
#      actual source scripts/sync-llm-settings.sh reads from), only where
#      content differs.
#   2. Runs scripts/sync-llm-settings.sh (SkillGuard preflight + writes into
#      docker/config/{openclaw,hermes}/ + manifest.json) — unchanged, existing
#      security gate.
#   3. For each bot container that is currently running:
#      - skills: docker cp the updated tree into the container's baked
#        config-defaults path (so a FUTURE rebuild still has it) AND directly
#        into the bot's live skill-discovery path (same copy semantics the
#        bot's own init script uses at boot) — takes effect immediately, zero
#        restart, zero downtime.
#      - agents/mcp: docker cp into the config-defaults path (durable for next
#        rebuild); since MCP registration and agent-file loading don't have as
#        uniform a "live" path as skills, a container RESTART (a few seconds,
#        not a rebuild) is used to apply these — offered, not forced, unless
#        --restart-for-agents-mcp is passed.
#
# USAGE:
#   bash scripts/update-bot-agents.sh [--dry-run] [--restart-for-agents-mcp]
#
# Works on whichever host currently runs the target containers — the same
# command applies on this machine or on a separate dev host (e.g. marvin),
# since it only ever inspects/acts on containers actually running locally.
#
# EXIT CODES: 0 success, 1 sync-llm-settings.sh failed (incl. SkillGuard
# block), 2 argument error.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"

DRY_RUN=0
RESTART_FOR_AGENTS_MCP=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --restart-for-agents-mcp) RESTART_FOR_AGENTS_MCP=1; shift ;;
    *)
      echo "ERROR: Unknown argument: $1" >&2
      echo "Usage: $0 [--dry-run] [--restart-for-agents-mcp]" >&2
      exit 2 ;;
  esac
done

REPO_LLM_SETTINGS="${REPO}/.llm_settings"
HOME_LLM_SETTINGS="${HOME}/.llm_settings"

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║  AgentShroud™ — Update Bot Agents (no-rebuild refresh) ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

# ── Step 1: repo .llm_settings/ -> ~/.llm_settings/ (the real sync source) ───
if [[ ! -d "${REPO_LLM_SETTINGS}" ]]; then
  echo "ERROR: ${REPO_LLM_SETTINGS} not found — nothing to sync from." >&2
  exit 1
fi

echo "── Step 1: repo .llm_settings/ → ${HOME_LLM_SETTINGS}"
mkdir -p "${HOME_LLM_SETTINGS}"
step1_copied=0
for subdir in skills mcp agents; do
  src="${REPO_LLM_SETTINGS}/${subdir}"
  [[ -d "${src}" ]] || continue
  dst="${HOME_LLM_SETTINGS}/${subdir}"
  mkdir -p "${dst}"
  while IFS= read -r -d '' f; do
    rel="${f#"${src}"/}"
    dst_file="${dst}/${rel}"
    if [[ -f "${dst_file}" ]] && cmp -s "${f}" "${dst_file}"; then
      continue
    fi
    if [[ "${DRY_RUN}" -eq 1 ]]; then
      echo "    [DRY-RUN] would copy: ${subdir}/${rel}"
    else
      mkdir -p "$(dirname "${dst_file}")"
      cp "${f}" "${dst_file}"
      echo "    copied: ${subdir}/${rel}"
    fi
    step1_copied=$((step1_copied + 1))
  done < <(find "${src}" -type f -print0 2>/dev/null)
done
echo "   ${step1_copied} file(s) synced to ${HOME_LLM_SETTINGS}"
echo ""

# ── Step 2: existing SkillGuard-gated sync into docker/config/{bot}/ ─────────
echo "── Step 2: scripts/sync-llm-settings.sh (SkillGuard preflight + docker/config/)"
SYNC_ARGS=()
[[ "${DRY_RUN}" -eq 1 ]] && SYNC_ARGS+=(--dry-run)
if ! bash "${SCRIPT_DIR}/sync-llm-settings.sh" "${SYNC_ARGS[@]}"; then
  echo "" >&2
  echo "ERROR: sync-llm-settings.sh failed — aborting before touching any running container." >&2
  exit 1
fi
echo ""

if [[ "${DRY_RUN}" -eq 1 ]]; then
  echo "Dry-run complete — no containers touched."
  exit 0
fi

# ── Step 3: live-refresh running containers ──────────────────────────────────
# Per-bot: container name, config-defaults path (baked at build), live
# skill-discovery path (what the bot actually reads from).
declare -A BOT_CONTAINER=(
  [openclaw]="agentshroud-openclaw"
  [hermes]="agentshroud-hermes-v2"
)
declare -A BOT_DEFAULTS_DIR=(
  [openclaw]="/app/config-defaults/openclaw"
  [hermes]="/app/config-defaults/hermes"
)
declare -A BOT_LIVE_SKILLS_DIR=(
  [openclaw]="/home/node/.openclaw/skills"
  [hermes]="/opt/data/skills"
)

echo "── Step 3: live-refresh running bot containers"
for bot in openclaw hermes; do
  container="${BOT_CONTAINER[${bot}]}"
  if ! docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "${container}"; then
    echo "  [skip] ${container} is not running — nothing to refresh live (will pick up on next start/rebuild)"
    continue
  fi

  defaults_dir="${BOT_DEFAULTS_DIR[${bot}]}"
  live_skills_dir="${BOT_LIVE_SKILLS_DIR[${bot}]}"
  repo_bot_dir="${REPO}/docker/config/${bot}"

  # Some bots (openclaw) run with a read-only rootfs and no config volume —
  # a deliberate security hardening, not a bug. `docker cp` into them always
  # fails ("container rootfs is marked read-only"); the only way to update
  # their skills is a rebuild + recreate that re-bakes docker/config/<bot>/
  # via the Dockerfile COPY. Detect this per-container so one read-only bot
  # can't abort the whole loop (and skip hermes's live refresh) under set -e.
  readonly_rootfs="$(docker inspect "${container}" --format '{{.HostConfig.ReadonlyRootfs}}' 2>/dev/null || echo "false")"
  if [[ "${readonly_rootfs}" == "true" ]]; then
    echo "  [read-only] ${container}: rootfs is read-only (security hardening) — live docker-cp is not possible."
    echo "  [read-only] ${container}: config staged in docker/config/${bot}/ for the next rebuild. To apply now:"
    echo "  [read-only]   docker-compose -f ${REPO}/docker/docker-compose.yml build ${bot} && docker-compose -f ${REPO}/docker/docker-compose.yml up -d --force-recreate ${bot}"
    continue
  fi

  # -- skills: push into config-defaults (durable) AND live workspace (immediate, zero restart) --
  if [[ -d "${repo_bot_dir}/skills" ]]; then
    if docker cp "${repo_bot_dir}/skills/." "${container}:${defaults_dir}/skills/" >/dev/null 2>&1; then
      docker exec "${container}" sh -c "
        mkdir -p '${live_skills_dir}'
        for d in '${defaults_dir}'/skills/*/; do
          [ -d \"\${d}\" ] || continue
          name=\$(basename \"\${d}\")
          rm -rf \"${live_skills_dir}/\${name:?}\"
          cp -r \"\${d}\" \"${live_skills_dir}/\${name}\"
        done
      "
      # docker cp always writes as the host UID (macOS/Colima), never the
      # container's own user — confirmed 2026-08-04: this left hermes's
      # /opt/data/skills tree root-owned, which crash-looped the container
      # because hermes-init (running as its own unprivileged user) couldn't
      # rm/reseed its own root-owned files on next boot. Restore ownership
      # to match the pre-existing owner of the live skills dir's parent
      # immediately after every copy so this can't regress.
      owner="$(docker exec "${container}" sh -c "stat -c '%u:%g' \"\$(dirname '${live_skills_dir}')\"" 2>/dev/null || true)"
      if [[ -n "${owner}" ]]; then
        docker exec "${container}" chown -R "${owner}" "${live_skills_dir}" 2>/dev/null || \
          echo "  [warn] ${container}: chown of ${live_skills_dir} to ${owner} failed — check ownership manually"
      else
        echo "  [warn] ${container}: could not determine expected owner of ${live_skills_dir} — skipping chown (verify manually)"
      fi
      echo "  [live] ${container}: skills refreshed, no restart needed"
    else
      echo "  [warn] ${container}: docker cp of skills failed — see above; config still staged in docker/config/${bot}/ for next rebuild"
    fi
  fi

  # -- agents/mcp: push into config-defaults (durable); live application needs a restart --
  agents_mcp_touched=0
  for subdir in agents mcp; do
    if [[ -d "${repo_bot_dir}/${subdir}" ]]; then
      if docker cp "${repo_bot_dir}/${subdir}/." "${container}:${defaults_dir}/${subdir}/" >/dev/null 2>&1; then
        agents_mcp_touched=1
      else
        echo "  [warn] ${container}: docker cp of ${subdir} failed — config still staged in docker/config/${bot}/ for next rebuild"
      fi
    fi
  done
  if [[ "${agents_mcp_touched}" -eq 1 ]]; then
    if [[ "${RESTART_FOR_AGENTS_MCP}" -eq 1 ]]; then
      echo "  [restart] ${container}: applying agents/mcp changes (--restart-for-agents-mcp)"
      docker restart "${container}" >/dev/null
      echo "  [restart] ${container}: restarted"
    else
      echo "  [pending] ${container}: agents/mcp files updated in the container, but need a restart to take effect (re-run with --restart-for-agents-mcp, or 'docker restart ${container}' yourself when convenient)"
    fi
  fi
done

echo ""
echo "══════════════════════════════════════════════════════"
echo "Update complete."
echo "══════════════════════════════════════════════════════"
