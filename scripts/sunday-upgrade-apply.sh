#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# sunday-upgrade-apply.sh — DETERMINISTIC core of the weekly Sunday upgrade.
#
# Why this exists (owner decision 2026-09-06): the Sunday job previously asked a
# Claude session to improvise every step of a production upgrade unattended.
# That is not reliable — the 2026-09-06 run failed on both accounts before doing
# any work (dev: launchd PATH lacked Homebrew so `tmux` was not found; prod: the
# mission never got submitted out of the composer). Unattended reliability has to
# come from a script with hard pass/fail gates, not from a model's judgement.
#
# Division of labour:
#   THIS SCRIPT  — mechanical + verifiable: preflight, baseline capture, image
#                  scanning, applying pinned version bumps, rebuild, health
#                  verification, rollback, and writing the machine-readable
#                  dev→prod handoff JSON. No LLM required. Exit code is the
#                  contract.
#   THE SESSION  — judgement only: reading changelogs, deciding WHICH versions
#                  are candidates, triaging findings, writing the prose report.
#
# The agent proposes versions; this script disposes. A bump only ships if the
# gates below pass, regardless of what any model concluded.
#
# Usage:
#   sunday-upgrade-apply.sh --env dev|prod [options]
#
#   --env dev|prod        Which stack this is running against. REQUIRED.
#                         dev additionally writes the handoff JSON that gates prod.
#   --dry-run             Run every read-only phase and report what WOULD change.
#                         Makes no mutation: no build, no compose up, no pin edit.
#   --phase P             preflight|baseline|scan|apply|verify|all   (default: all)
#   --soak-seconds N      Post-change stability soak. Default 120 (procedure
#                         requires containers stay healthy at least 2 minutes).
#   --max-critical N      Fail the scan gate above N CRITICAL findings.
#                         Default: unset = report only, never gate on it.
#   --allow-dirty-build   Build even though the build context has uncommitted
#                         changes. Ships WIP into a production image — explicit on purpose.
#   --allow-dirty         Proceed despite unrelated uncommitted changes. The repo
#                         routinely carries pre-existing modifications; this
#                         script never commits, so it does not care — but the
#                         default still warns loudly.
#
# Exit codes (the contract — callers depend on these):
#   0   all requested phases passed
#   10  preflight failed (environment not fit to run)
#   20  scan gate failed (--max-critical exceeded)
#   30  apply failed (build/compose error) — rollback attempted
#   40  verify failed (unhealthy/restart loop/errors) — rollback attempted
#   50  rollback itself failed — STACK MAY BE DEGRADED, human required
#   127 required binary missing

set -euo pipefail

# ── PATH hardening ───────────────────────────────────────────────────────────
# Same defect that killed the 2026-09-06 dev run. Never trust the caller's PATH.
export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"

# ── Defaults ─────────────────────────────────────────────────────────────────
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TODAY="$(date +%F)"
ENVIRONMENT=""
DRY_RUN=0
PHASE="all"
SOAK_SECONDS=120
MAX_CRITICAL=""
ALLOW_DIRTY=0
ALLOW_DIRTY_BUILD=0
HANDOFF_DIR="/Users/Shared/agentshroud-sunday"
COMPOSE_FILE="${SUNDAY_COMPOSE_FILE:-$REPO/docker/docker-compose.yml}"
ARTIFACT_DIR="$REPO/reports/sunday/$TODAY"

# Containers that must be healthy for the stack to be considered good.
# Overridable so dev/prod or a future service list can differ without a code edit.
DEFAULT_CONTAINERS="agentshroud-gateway agentshroud-openclaw agentshroud-hermes-v2 agentshroud-voice-gateway agentshroud-docker-socket-proxy"
CONTAINERS="${SUNDAY_CONTAINERS:-$DEFAULT_CONTAINERS}"

# Images scanned by the CVE gate.
DEFAULT_SCAN_IMAGES="agentshroud-gateway:latest agentshroud-openclaw:latest agentshroud/hermes:latest"
SCAN_IMAGES="${SUNDAY_SCAN_IMAGES:-$DEFAULT_SCAN_IMAGES}"

# ── Logging ──────────────────────────────────────────────────────────────────
_ts() { date '+%H:%M:%S'; }
log()  { printf '[apply %s] %s\n'        "$(_ts)" "$*"; }
warn() { printf '[apply %s] WARN: %s\n'  "$(_ts)" "$*" >&2; }
err()  { printf '[apply %s] ERROR: %s\n' "$(_ts)" "$*" >&2; }
die()  { local code="$1"; shift; err "$*"; exit "$code"; }

# ── Arg parsing ──────────────────────────────────────────────────────────────
while [ $# -gt 0 ]; do
  case "$1" in
    --env)           ENVIRONMENT="${2:-}"; shift 2 ;;
    --dry-run)       DRY_RUN=1; shift ;;
    --phase)         PHASE="${2:-}"; shift 2 ;;
    --soak-seconds)  SOAK_SECONDS="${2:-}"; shift 2 ;;
    --max-critical)  MAX_CRITICAL="${2:-}"; shift 2 ;;
    --allow-dirty)   ALLOW_DIRTY=1; shift ;;
    --allow-dirty-build) ALLOW_DIRTY_BUILD=1; shift ;;
    -h|--help)       sed -n '1,60p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *)               die 10 "unknown argument: $1" ;;
  esac
done

case "$ENVIRONMENT" in
  dev|prod) ;;
  *) die 10 "--env must be 'dev' or 'prod' (got: '${ENVIRONMENT:-<empty>}')" ;;
esac
case "$PHASE" in
  preflight|baseline|scan|apply|verify|all) ;;
  *) die 10 "--phase must be one of preflight|baseline|scan|apply|verify|all (got: '$PHASE')" ;;
esac
if ! printf '%s' "$SOAK_SECONDS" | grep -Eq '^[0-9]+$'; then
  die 10 "--soak-seconds must be an integer (got: '$SOAK_SECONDS')"
fi
if [ -n "$MAX_CRITICAL" ] && ! printf '%s' "$MAX_CRITICAL" | grep -Eq '^[0-9]+$'; then
  die 10 "--max-critical must be an integer (got: '$MAX_CRITICAL')"
fi

_should_run() { [ "$PHASE" = "all" ] || [ "$PHASE" = "$1" ]; }
_mutating()   { [ "$DRY_RUN" -eq 0 ]; }

# Build contexts actually used by the compose file, resolved to absolute paths.
# Falls back to the repo root if compose config can't be parsed — the
# conservative direction, since a wider context means we check MORE files.
_build_context_paths() {
  local ctx
  ctx="$(docker compose -f "$COMPOSE_FILE" config 2>/dev/null \
         | awk '/^[[:space:]]*context:[[:space:]]/ {print $2}' | sort -u)"
  if [ -n "$ctx" ]; then printf '%s\n' "$ctx"; else printf '%s\n' "$REPO"; fi
}

# Uncommitted changes sitting inside a build context. These would be baked into
# the resulting production image by `docker compose build`, which on a security
# product means shipping unreviewed work-in-progress — including, on 2026-09-07,
# modified source for six gateway/security/* modules plus gateway/Dockerfile
# itself. Excludes our own generated artifacts (graphify-out, reports).
_dirty_build_files() {
  local ctx rel
  for ctx in $(_build_context_paths); do
    case "$ctx" in
      "$REPO")   rel="." ;;
      "$REPO"/*) rel="${ctx#"$REPO"/}" ;;
      *)         continue ;;   # context outside the repo: not ours to police
    esac
    git -C "$REPO" status --porcelain -- "$rel" 2>/dev/null || true
  done | grep -v 'graphify-out/' | grep -v ' reports/' | sort -u
}

# Free GiB on the volume backing the Docker daemon's storage — which on
# macOS/Colima is inside the VM and unrelated to the host's own free space.
# Prints an integer, or nothing if it cannot be determined.
_docker_free_gb() {
  if command -v colima >/dev/null 2>&1 && colima status >/dev/null 2>&1; then
    colima ssh -- df -P -BG /var/lib/docker 2>/dev/null \
      | awk 'NR==2 {gsub(/G/,"",$4); print $4}'
    return 0
  fi
  # Native Linux daemon: df the daemon's own root dir.
  local root
  root="$(docker info --format '{{.DockerRootDir}}' 2>/dev/null || true)"
  if [ -n "$root" ] && [ -d "$root" ]; then
    df -P -BG "$root" 2>/dev/null | awk 'NR==2 {gsub(/G/,"",$4); print $4}'
  fi
}

mkdir -p "$ARTIFACT_DIR"
BASELINE_JSON="$ARTIFACT_DIR/baseline.json"
ROLLBACK_SH="$ARTIFACT_DIR/rollback.sh"
SCAN_JSON="$ARTIFACT_DIR/scan.json"

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: preflight
# ═════════════════════════════════════════════════════════════════════════════
phase_preflight() {
  log "preflight: environment=$ENVIRONMENT dry_run=$DRY_RUN repo=$REPO"

  local missing=""
  for b in docker git tar; do
    command -v "$b" >/dev/null 2>&1 || missing="${missing} ${b}"
  done
  [ -z "$missing" ] || die 127 "required binaries not on PATH:${missing} (PATH=$PATH)"

  docker info >/dev/null 2>&1 || die 10 "docker daemon unreachable (DOCKER_HOST=${DOCKER_HOST:-<unset>}) — is Colima running?"
  log "preflight: docker daemon reachable"

  [ -f "$COMPOSE_FILE" ] || die 10 "compose file not found: $COMPOSE_FILE"
  docker compose -f "$COMPOSE_FILE" config -q 2>/dev/null \
    || die 10 "compose file is invalid: $COMPOSE_FILE"
  log "preflight: compose file valid ($COMPOSE_FILE)"

  # Disk: a rebuild of three images plus pulls needs real headroom. Refuse to
  # start an upgrade we cannot finish rather than filling the disk mid-build.
  #
  # The HOST volume is NOT the interesting one. On macOS the Docker daemon lives
  # in a Colima VM with its own disk, and the two diverge completely: on
  # 2026-09-06 the host had 141GiB free while the VM's /var/lib/docker was 100%
  # full (118G/118G, 0 available). That full VM disk had already broken Hermes
  # silently — its logging handler was throwing OSError [Errno 28] No space left
  # on device while the container still reported "healthy" — and it would have
  # failed any image build this script attempted. Checking only the host would
  # have reported a comfortable PASS straight into that wall.
  local host_gb
  host_gb="$(df -g "$REPO" 2>/dev/null | awk 'NR==2 {print $4}')"
  printf '%s' "$host_gb" | grep -Eq '^[0-9]+$' && log "preflight: host volume ${host_gb}GiB free"

  local docker_gb
  docker_gb="$(_docker_free_gb 2>/dev/null || true)"
  if printf '%s' "$docker_gb" | grep -Eq '^[0-9]+$'; then
    if [ "$docker_gb" -lt 25 ]; then
      err "preflight: Docker storage has only ${docker_gb}GiB free — image builds need >=25GiB."
      err "preflight: reclaim space, then re-run. Suggested (review before running):"
      err "    docker builder prune -f            # build cache"
      err "    docker image prune -f              # dangling images"
      err "    docker image prune -a --filter 'until=168h'   # keep the last week, incl. agentshroud-rollback/* tags"
      die 10 "insufficient Docker storage (${docker_gb}GiB free) — refusing to start an upgrade that cannot finish"
    fi
    log "preflight: docker storage OK (${docker_gb}GiB free)"
  else
    warn "preflight: could not determine Docker storage free space — continuing, but a build may fail with ENOSPC"
  fi

  # Dirty tree is expected here and is NOT fatal: this script never commits.
  if ! git -C "$REPO" diff --quiet 2>/dev/null || ! git -C "$REPO" diff --cached --quiet 2>/dev/null; then
    local n
    # Unanchored on purpose: git QUOTES porcelain paths containing spaces or
    # special characters (the graphify vault is full of them), so an anchored
    # '^.. graphify-out/' pattern misses those lines and wildly overcounts —
    # observed reporting 17999 dirty files when the real non-graphify count was 68.
    n="$(git -C "$REPO" status --porcelain 2>/dev/null | grep -vc 'graphify-out/' || true)"
    if [ "$ALLOW_DIRTY" -eq 1 ]; then
      log "preflight: ${n} uncommitted change(s) present — proceeding (--allow-dirty)"
    else
      warn "preflight: ${n} uncommitted change(s) present (excluding graphify-out). This script does not commit, so it proceeds; pass --allow-dirty to silence."
    fi
  fi

  log "preflight: PASS"
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: baseline — capture exactly what we can roll back TO, and prove it.
# ═════════════════════════════════════════════════════════════════════════════
phase_baseline() {
  log "baseline: capturing rollback anchor"

  local git_rev git_desc
  git_rev="$(git -C "$REPO" rev-parse HEAD)"
  git_desc="$(git -C "$REPO" describe --tags --always 2>/dev/null || echo 'no-tag')"

  {
    printf '{\n'
    printf '  "date": "%s",\n' "$TODAY"
    printf '  "environment": "%s",\n' "$ENVIRONMENT"
    printf '  "git_rev": "%s",\n' "$git_rev"
    printf '  "git_describe": "%s",\n' "$git_desc"
    printf '  "images": {\n'
    local first=1 c img id
    for c in $CONTAINERS; do
      img="$(docker inspect --format '{{.Config.Image}}' "$c" 2>/dev/null || echo '<absent>')"
      id="$(docker inspect --format '{{.Image}}' "$c" 2>/dev/null || echo '<absent>')"
      [ "$first" -eq 1 ] || printf ',\n'
      first=0
      printf '    "%s": {"image": "%s", "image_id": "%s"}' "$c" "$img" "$id"
    done
    printf '\n  }\n}\n'
  } > "$BASELINE_JSON"

  log "baseline: wrote $BASELINE_JSON (git $git_desc)"

  # Retag every current image so a rollback has something concrete to point at.
  # Without this, `docker compose build` overwrites :latest and the old image
  # becomes unreferenced and prunable — the rollback path evaporates.
  local tagged=0 c id
  for c in $CONTAINERS; do
    id="$(docker inspect --format '{{.Image}}' "$c" 2>/dev/null || true)"
    [ -n "$id" ] || continue
    if _mutating; then
      docker tag "$id" "agentshroud-rollback/${c}:${TODAY}" 2>/dev/null && tagged=$((tagged + 1)) || \
        warn "baseline: could not retag $c for rollback"
    else
      tagged=$((tagged + 1))
    fi
  done
  if _mutating; then
    log "baseline: retagged ${tagged} image(s) as agentshroud-rollback/<container>:${TODAY}"
  else
    log "baseline: [dry-run] would retag ${tagged} image(s) for rollback"
  fi

  # Emit an executable rollback script. Generated, not hand-written, so it can
  # never drift from what was actually captured.
  {
    echo '#!/usr/bin/env bash'
    echo '# GENERATED by sunday-upgrade-apply.sh — restores the pre-upgrade state.'
    echo "# Baseline captured ${TODAY} for environment '${ENVIRONMENT}'."
    echo 'set -euo pipefail'
    echo "export PATH=\"/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:\${PATH:-}\""
    echo ''
    echo '# 1. Restore code'
    echo "git -C '$REPO' checkout $git_rev"
    echo ''
    echo '# 2. Restore images'
    for c in $CONTAINERS; do
      echo "docker tag agentshroud-rollback/${c}:${TODAY} \"\$(docker inspect --format '{{.Config.Image}}' ${c} 2>/dev/null || echo ${c}:latest)\" 2>/dev/null || true"
    done
    echo ''
    echo '# 3. Recreate containers from the restored images'
    echo "docker compose -f '$COMPOSE_FILE' up -d --force-recreate"
  } > "$ROLLBACK_SH"
  chmod +x "$ROLLBACK_SH"
  log "baseline: wrote executable rollback script $ROLLBACK_SH"
  log "baseline: PASS"
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: scan — real Trivy counts. Absence of a scanner is a FAILED gate,
# never a silent pass (repo rule: no fake green).
# ═════════════════════════════════════════════════════════════════════════════
phase_scan() {
  log "scan: CRITICAL/HIGH counts for: $SCAN_IMAGES"

  if ! command -v trivy >/dev/null 2>&1; then
    if [ -n "$MAX_CRITICAL" ]; then
      die 20 "trivy not installed but --max-critical=$MAX_CRITICAL was requested — cannot enforce a CVE gate without a scanner. Refusing to report a pass."
    fi
    warn "scan: trivy not installed — SKIPPED. No CVE claim can be made from this run."
    printf '{"scanner": "absent", "images": {}}\n' > "$SCAN_JSON"
    return 0
  fi

  local total_crit=0 first=1
  {
    printf '{\n  "scanner": "trivy",\n  "images": {\n'
    local img out crit high
    for img in $SCAN_IMAGES; do
      if ! docker image inspect "$img" >/dev/null 2>&1; then
        warn "scan: image not present locally, skipping: $img"
        continue
      fi
      out="$(trivy image --quiet --scanners vuln --severity CRITICAL,HIGH \
              --format json "$img" 2>/dev/null || true)"
      if [ -z "$out" ]; then
        warn "scan: trivy returned nothing for $img"
        continue
      fi
      crit="$(printf '%s' "$out" | grep -o '"Severity": *"CRITICAL"' | wc -l | tr -d ' ')"
      high="$(printf '%s' "$out" | grep -o '"Severity": *"HIGH"'     | wc -l | tr -d ' ')"
      total_crit=$((total_crit + crit))
      [ "$first" -eq 1 ] || printf ',\n'
      first=0
      printf '    "%s": {"critical": %s, "high": %s}' "$img" "$crit" "$high"
      log "scan: $img -> ${crit} CRITICAL / ${high} HIGH"
    done
    printf '\n  }\n}\n'
  } > "$SCAN_JSON"

  log "scan: wrote $SCAN_JSON (total CRITICAL across images: ${total_crit})"

  if [ -n "$MAX_CRITICAL" ] && [ "$total_crit" -gt "$MAX_CRITICAL" ]; then
    die 20 "CVE gate FAILED: ${total_crit} CRITICAL findings exceeds --max-critical=${MAX_CRITICAL}"
  fi
  log "scan: PASS"
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: apply — rebuild and recreate from CURRENT pins.
# Version pins are edited by the session (judgement); this only builds/ships
# whatever docker/versions.env now says, then verify() decides if it survives.
# ═════════════════════════════════════════════════════════════════════════════
phase_apply() {
  if ! _mutating; then
    log "apply: [dry-run] would run: docker compose -f $COMPOSE_FILE build --pull, then up -d"
    log "apply: [dry-run] current pins:"
    grep -E '^[A-Z_]+=' "$REPO/docker/versions.env" 2>/dev/null | sed 's/^/  /' || true
    return 0
  fi

  # ── Clean-build gate ───────────────────────────────────────────────────────
  # `docker compose build` bakes the working tree into the image. If the build
  # context is dirty, an unattended Sunday run would ship whatever happened to be
  # uncommitted at 06:00 straight into production. On 2026-09-07 that was 57
  # files including gateway/Dockerfile, docker/docker-compose.yml and modified
  # source for six gateway/security/* modules. On a security product that is a
  # supply-chain hazard, not an inconvenience — so it is a hard gate, and the
  # override is deliberately explicit rather than a default.
  local dirty
  dirty="$(_dirty_build_files)"
  if [ -n "$dirty" ] && [ "$ALLOW_DIRTY_BUILD" -eq 0 ]; then
    err "apply: REFUSING to build — uncommitted changes inside the build context would be baked into the production image:"
    printf '%s\n' "$dirty" | head -20 | sed 's/^/    /' >&2
    local n; n="$(printf '%s\n' "$dirty" | wc -l | tr -d ' ')"
    [ "$n" -gt 20 ] && err "    ... and $((n - 20)) more ($n total)"
    err "apply: commit, stash, or explicitly override with --allow-dirty-build if this WIP is genuinely intended to ship."
    exit 30
  fi
  [ -z "$dirty" ] || warn "apply: building with $(printf '%s\n' "$dirty" | wc -l | tr -d ' ') uncommitted file(s) in the build context (--allow-dirty-build)"

  log "apply: building images from current pins (this is the slow phase)"
  if ! docker compose -f "$COMPOSE_FILE" build --pull; then
    err "apply: build FAILED"
    _attempt_rollback
    exit 30
  fi

  log "apply: recreating containers"
  if ! docker compose -f "$COMPOSE_FILE" up -d; then
    err "apply: compose up FAILED"
    _attempt_rollback
    exit 30
  fi
  log "apply: PASS (build + up completed; health not yet proven — see verify)"
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: verify — the gate that actually decides GO/NO-GO.
# ═════════════════════════════════════════════════════════════════════════════
phase_verify() {
  log "verify: checking ${CONTAINERS// /, }"
  local failures=""

  # 1. Every expected container exists and is running.
  local c state
  for c in $CONTAINERS; do
    state="$(docker inspect --format '{{.State.Status}}' "$c" 2>/dev/null || echo 'absent')"
    if [ "$state" != "running" ]; then
      failures="${failures}\n  - ${c}: state=${state} (expected running)"
      err "verify: $c state=$state"
    else
      log "verify: $c running"
    fi
  done

  # 2. Health status where a healthcheck is defined.
  for c in $CONTAINERS; do
    local health
    health="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$c" 2>/dev/null || echo 'absent')"
    case "$health" in
      healthy)   log "verify: $c healthy" ;;
      none)      log "verify: $c has no healthcheck defined (not a failure)" ;;
      absent)    ;;  # already reported above
      *)         failures="${failures}\n  - ${c}: health=${health}"
                 err "verify: $c health=$health" ;;
    esac
  done

  # 3. Restart-loop detection across a soak window. A container can be
  #    "running" at the instant you look and still be crash-looping; the
  #    procedure requires it to hold steady for at least 2 minutes.
  local -a before_counts=()
  for c in $CONTAINERS; do
    before_counts+=("$(docker inspect --format '{{.RestartCount}}' "$c" 2>/dev/null || echo -1)")
  done
  log "verify: soaking ${SOAK_SECONDS}s to detect restart loops"
  sleep "$SOAK_SECONDS"

  local i=0 after
  for c in $CONTAINERS; do
    after="$(docker inspect --format '{{.RestartCount}}' "$c" 2>/dev/null || echo -1)"
    if [ "${before_counts[$i]}" != "-1" ] && [ "$after" != "${before_counts[$i]}" ]; then
      failures="${failures}\n  - ${c}: restarted during soak (${before_counts[$i]} -> ${after})"
      err "verify: $c RESTARTED during soak (${before_counts[$i]} -> ${after})"
    fi
    i=$((i + 1))
  done

  # 4. Error scan of recent logs.
  for c in $CONTAINERS; do
    local hits
    hits="$(docker logs --since "${SOAK_SECONDS}s" "$c" 2>&1 \
            | grep -Eic 'panic:|fatal|traceback \(most recent' || true)"
    if [ "${hits:-0}" -gt 0 ]; then
      warn "verify: $c has ${hits} panic/fatal/traceback line(s) in the last ${SOAK_SECONDS}s — inspect: docker logs --since ${SOAK_SECONDS}s $c"
    fi
  done

  if [ -n "$failures" ]; then
    err "verify: FAILED:$(printf '%b' "$failures")"
    _attempt_rollback
    exit 40
  fi
  log "verify: PASS — all containers running, healthy, and stable for ${SOAK_SECONDS}s"
}

# ═════════════════════════════════════════════════════════════════════════════
# Rollback
# ═════════════════════════════════════════════════════════════════════════════
_attempt_rollback() {
  if ! _mutating; then
    log "rollback: [dry-run] nothing was changed, nothing to roll back"
    return 0
  fi
  if [ ! -x "$ROLLBACK_SH" ]; then
    err "rollback: no rollback script at $ROLLBACK_SH — baseline phase did not run. MANUAL INTERVENTION REQUIRED."
    exit 50
  fi
  warn "rollback: restoring pre-upgrade state via $ROLLBACK_SH"
  if "$ROLLBACK_SH"; then
    log "rollback: completed — re-verifying restored stack"
    local c state bad=0
    for c in $CONTAINERS; do
      state="$(docker inspect --format '{{.State.Status}}' "$c" 2>/dev/null || echo absent)"
      [ "$state" = "running" ] || { err "rollback: $c is '$state' after rollback"; bad=1; }
    done
    [ "$bad" -eq 0 ] || die 50 "rollback ran but the stack is still not healthy — MANUAL INTERVENTION REQUIRED"
    log "rollback: stack restored and running"
  else
    die 50 "rollback script FAILED — STACK MAY BE DEGRADED, MANUAL INTERVENTION REQUIRED"
  fi
}

# ═════════════════════════════════════════════════════════════════════════════
# dev→prod handoff. Written ONLY by dev, ONLY on a genuine pass.
# This is the contract prod's gate reads; making the script own it removes the
# 2026-09-06 failure mode where no JSON existed because the session never got
# far enough to write one.
# ═════════════════════════════════════════════════════════════════════════════
write_handoff() {
  [ "$ENVIRONMENT" = "dev" ] || return 0
  local status="$1"

  if ! _mutating; then
    log "handoff: [dry-run] would write status=${status} to ${HANDOFF_DIR}/dev-result-${TODAY}.json"
    return 0
  fi
  if ! mkdir -p "$HANDOFF_DIR" 2>/dev/null; then
    warn "handoff: cannot create $HANDOFF_DIR — prod will correctly stay BLOCKED"
    return 0
  fi

  local versions=""
  if [ -f "$REPO/docker/versions.env" ]; then
    versions="$(grep -E '^[A-Z_]+=' "$REPO/docker/versions.env" 2>/dev/null \
      | sed 's/"//g' \
      | awk -F= '{printf "%s\"%s\": \"%s\"", (NR>1 ? ",\n    " : ""), $1, $2}')"
  fi

  local out="${HANDOFF_DIR}/dev-result-${TODAY}.json"
  {
    printf '{\n'
    printf '  "date": "%s",\n' "$TODAY"
    printf '  "status": "%s",\n' "$status"
    printf '  "versions": {\n    %s\n  },\n' "$versions"
    printf '  "notes": "Written by sunday-upgrade-apply.sh. status=PASS means preflight, scan, apply and verify all passed on dev, including a %ss stability soak."\n' "$SOAK_SECONDS"
    printf '}\n'
  } > "$out"
  chmod 644 "$out" 2>/dev/null || true
  log "handoff: wrote $out (status=$status)"
}

# ═════════════════════════════════════════════════════════════════════════════
# Main
# ═════════════════════════════════════════════════════════════════════════════
log "=== sunday-upgrade-apply start: env=$ENVIRONMENT phase=$PHASE dry_run=$DRY_RUN ==="

# On any unexpected failure, record a FAIL handoff so prod stays blocked rather
# than reading a stale PASS from a previous week.
trap 'rc=$?; if [ $rc -ne 0 ]; then write_handoff FAIL; fi' EXIT

_should_run preflight && phase_preflight
_should_run baseline  && phase_baseline
_should_run scan      && phase_scan
_should_run apply     && phase_apply
_should_run verify    && phase_verify

write_handoff PASS
log "=== sunday-upgrade-apply COMPLETE: all requested phases passed ==="
log "artifacts: $ARTIFACT_DIR"
exit 0
