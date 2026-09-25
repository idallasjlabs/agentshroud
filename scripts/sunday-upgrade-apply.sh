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
#   --phase P             preflight|discover|baseline|scan|apply|verify|all
#                         (default: all)
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
#   25  NOTHING WAS UPGRADED although a newer upstream release exists.
#       The run was mechanically green but achieved nothing — see the no-op
#       gate below. This is a job malfunction, not a healthy stack.
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
# Scan-integrity enforcement, set from the environment below once ENVIRONMENT is
# known. prod: a scan that errored or scanned nothing is fatal. dev: loud warning.
SUNDAY_SCAN_ENFORCE="${SUNDAY_SCAN_ENFORCE:-}"
ALLOW_DIRTY=0
ALLOW_DIRTY_BUILD=0
# Overridable (like SUNDAY_COMPOSE_FILE/SUNDAY_CONTAINERS/SUNDAY_SCAN_IMAGES)
# so tests can point the dev->prod gate at a scratch dir instead of writing to
# the real shared one that prod actually reads.
HANDOFF_DIR="${SUNDAY_HANDOFF_DIR:-/Users/Shared/agentshroud-sunday}"
# Advisory lock telling colima-health-check.sh that a build is in flight, so its
# socket-forward repair does not bounce the VM out from under us. A heavy build
# makes the host socket stop answering, which is exactly the health check's
# trigger to restart Colima — on 2026-09-23 that killed an in-flight build at
# 10:20 and wiped the exit-code sentinel with /tmp. The lock carries this PID and
# is re-stamped on every build poll, so if this run dies the guard lapses within
# AGENTSHROUD_UPGRADE_LOCK_MAX_AGE and normal repair resumes.
UPGRADE_LOCK="${SUNDAY_UPGRADE_LOCK:-$HANDOFF_DIR/upgrade-in-progress.lock}"
COMPOSE_FILE="${SUNDAY_COMPOSE_FILE:-$REPO/docker/docker-compose.yml}"
ARTIFACT_DIR="$REPO/reports/sunday/$TODAY"

# docker/docker-compose.yml interpolates OPENCLAW_VERSION / HERMES_IMAGE /
# AGENTSHROUD_VERSION directly, so they must be present in the REAL shell
# environment, not merely passed as --env-file. scripts/asb:30-33 does exactly
# this and it is why builds there work. Omitting it made compose interpolate
# empty strings ("The OPENCLAW_VERSION variable is not set") and the 2026-09-11
# apply failed into a rollback as a result.
if [ -f "$REPO/docker/versions.env" ]; then
  set -a
  # shellcheck source=docker/versions.env
  . "$REPO/docker/versions.env"
  set +a
else
  echo "[apply] FATAL: $REPO/docker/versions.env not found — required for pinned builds" >&2
  exit 10
fi

# Containers that must be healthy for the stack to be considered good. See the
# per-host default resolved below (after account/host detection) for why this
# can't be a single static default — the container_name suffix a compose
# override picks is NOT always the bare hostname (raspberrypi -> "rpi",
# confirmed 2026-09-14), so only the hosts explicitly handled below get a
# correct auto-default; any other bot account/host must pass SUNDAY_CONTAINERS
# explicitly or this script silently checks containers that don't exist.

# Images scanned by the CVE gate. Tagged by AGENTSHROUD_VERSION (from
# docker/versions.env, sourced above), not `:latest` — images are built and
# tagged as e.g. agentshroud-gateway:1.6.0; `:latest` is never pushed by
# `docker compose build`, so a hardcoded `:latest` here always misses the
# real image. Same phantom-tag defect already fixed in the daily CVE scan
# itself (gateway/security/daily_cve_report.py, PR #442) — this script had
# an independent copy of the same bug.
DEFAULT_SCAN_IMAGES="agentshroud-gateway:${AGENTSHROUD_VERSION:-latest} agentshroud-openclaw:${AGENTSHROUD_VERSION:-latest} agentshroud/hermes:${AGENTSHROUD_VERSION:-latest}"
SCAN_IMAGES="${SUNDAY_SCAN_IMAGES:-$DEFAULT_SCAN_IMAGES}"

# ── Logging ──────────────────────────────────────────────────────────────────
_ts() { date '+%H:%M:%S'; }
log()  { printf '[apply %s] %s\n'        "$(_ts)" "$*"; }
warn() { printf '[apply %s] WARN: %s\n'  "$(_ts)" "$*" >&2; }
err()  { printf '[apply %s] ERROR: %s\n' "$(_ts)" "$*" >&2; }
die()  { local code="$1"; shift; err "$*"; exit "$code"; }

# scan-gate logic lives in a sourced lib (like container-runtime.sh below) so
# it can be unit-tested with a controlled PATH — this script's own PATH
# hardening above is deliberately hostile to that (see scripts/lib/sunday-scan.sh).
# shellcheck source=scripts/lib/sunday-scan.sh
. "$REPO/scripts/lib/sunday-scan.sh"

# ── Container-runtime + compose-file resolution (mirrors scripts/asb) ────────
# scripts/asb already solves "which compose binary, which override file, which
# project name" correctly per-account/per-host; this script must resolve the
# same way or it silently targets the wrong stack. Fixed 2026-09-14: this
# script previously hardcoded the `docker compose` plugin form — broken on
# this host's toolchain (~/.docker/cli-plugins/docker-compose points to a
# deleted Docker.app, same defect scripts/update-agentshroud.sh already works
# around) — and only ever pointed at the base compose file, missing the
# per-account override (docker/docker-compose.agentshroud-bot.<host>.yml) that
# renames containers (agentshroud-gateway -> agentshroud-marvin-gateway on
# this host). Every phase below was therefore inspecting/building against
# containers that don't exist under this account.
# shellcheck source=scripts/lib/container-runtime.sh
. "$REPO/scripts/lib/container-runtime.sh"
CE="$(detect_container_runtime)" || die 127 "no usable docker-compose/podman-compose found on PATH"

HOST_SHORT="$(hostname -s)"
if [ "$USER" = "agentshroud-bot" ]; then
  PROJECT="agentshroud-bot"
  OVERRIDE_FILE="$REPO/docker/docker-compose.agentshroud-bot.${HOST_SHORT}.yml"
  if [ -f "$OVERRIDE_FILE" ]; then
    COMPOSE_CMD="$CE -f $COMPOSE_FILE -f $OVERRIDE_FILE -p $PROJECT"
  else
    warn "no compose override for host '${HOST_SHORT}' — proceeding with base compose file only"
    COMPOSE_CMD="$CE -f $COMPOSE_FILE -p $PROJECT"
  fi
else
  PROJECT="agentshroud"
  COMPOSE_CMD="$CE -f $COMPOSE_FILE -p $PROJECT"
fi

# Renamed 2026-09-18 (owner directive: dev containers must be distinguishable
# from prod by name alone) — agentshroud-dev-* is marvin's actual dev naming
# now (docker/docker-compose.agentshroud-bot.marvin.yml,
# docker/bots/hermes/run-standalone.sh). Only marvin is handled automatically;
# any other bot host/account still needs SUNDAY_CONTAINERS passed explicitly.
if [ "$USER" = "agentshroud-bot" ] && [ "$HOST_SHORT" = "marvin" ]; then
  DEFAULT_CONTAINERS="agentshroud-dev-gateway agentshroud-dev-openclaw agentshroud-dev-hermes-v2 agentshroud-dev-voice-gateway agentshroud-dev-docker-socket-proxy"
else
  DEFAULT_CONTAINERS="agentshroud-gateway agentshroud-openclaw agentshroud-hermes-v2 agentshroud-voice-gateway agentshroud-docker-socket-proxy"
fi
CONTAINERS="${SUNDAY_CONTAINERS:-$DEFAULT_CONTAINERS}"

# Default the scan-integrity gate from the environment unless explicitly set.
if [ -z "$SUNDAY_SCAN_ENFORCE" ]; then
  if [ "$ENVIRONMENT" = "prod" ]; then SUNDAY_SCAN_ENFORCE=1; else SUNDAY_SCAN_ENFORCE=0; fi
fi
export SUNDAY_SCAN_ENFORCE
# hermes-v2 and voice-gateway are gated behind compose profiles ("hermes"/
# "voice", both members of "full" — docker/docker-compose.yml:572,728) and are
# invisible to `config`/`build`/`up` without an explicit --profile flag,
# exactly like scripts/asb's `up full` path already accounts for (asb:475).
# Fixed 2026-09-14: this script had no profile flag at all, so `apply` never
# built either service and `up -d` never even considered them — a first run
# reported PASS having silently left both on their pre-cycle images, even
# though DEFAULT_CONTAINERS above has always listed both as required-healthy.
COMPOSE_CMD="$COMPOSE_CMD --profile full"
log "compose: engine='$CE' project='$PROJECT' cmd='$COMPOSE_CMD'"

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
  preflight|discover|baseline|scan|apply|verify|all) ;;
  *) die 10 "--phase must be one of preflight|discover|baseline|scan|apply|verify|all (got: '$PHASE')" ;;
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
  ctx="$($COMPOSE_CMD config 2>/dev/null \
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
  done | grep -v 'graphify-out/' | grep -v ' reports/' | sort -u || true
  # `|| true` is load-bearing, not defensive noise. Under `set -euo pipefail` a
  # `grep -v` that matches nothing exits 1, which propagates through pipefail and
  # kills the caller's `dirty="$(_dirty_build_files)"` assignment. That made this
  # gate fail CLOSED in the worst possible way: it worked while the tree was
  # dirty and killed the whole run the instant the tree became clean — i.e.
  # exactly when the build should have proceeded. Cost two silent failed apply
  # runs (2026-09-09, 2026-09-11) that looked like hung builds. An empty result
  # means "nothing dirty", which is success, not failure.
}

# Services in the compose file that actually have a build context. Parsed from
# the NORMALIZED `docker compose config` output, so it reflects overrides and
# extends rather than the raw file text.
# Build transport. The host reaches dockerd through Colima's docker.sock
# forward, and that forward dies under sustained build load — it killed builds
# at step 34/125 and 118/125 on 2026-09-20/21, and again 4 seconds into the
# gateway build on 2026-09-23. That last one surfaced as "build FAILED" and
# "rollback script FAILED — STACK MAY BE DEGRADED", when both were really just
# "cannot connect to the Docker daemon"; the stack was untouched and all seven
# containers stayed healthy throughout.
#
# lima forwards unix sockets over SSH with no keepalive of any kind, and that is
# not tunable from colima: --port-forwarder grpc governs TCP forwards only, and
# switching to it changed nothing here. Building INSIDE the VM removes the
# forward from the path entirely — verified 2026-09-23, all three images built
# in-VM with zero socket deaths immediately after two host-socket attempts had
# failed mid-build.
#
# OFF BY DEFAULT: the host path stays the default, so this changes nothing for
# environments without the problem. Enable with SUNDAY_BUILD_VIA_VM=1.
#
# Two translations are required, neither optional:
#   * the VM has the compose PLUGIN (`docker compose`) but NOT the standalone
#     `docker-compose` the host uses, so COMPOSE_CMD is rewritten
#   * versions.env must be re-sourced inside the VM. Without it compose warns
#     "OPENCLAW_VERSION is not set, defaulting to a blank string" and bakes
#     empty pins into the image — a silently WRONG build rather than a failed
#     one. Observed live while testing this path.
# The repo is bind-mounted at the same absolute path in the VM, so the compose
# -f arguments resolve unchanged.

# Wait, bounded, for the Docker socket to come back.
#
# The host socket is a Lima SSH forward configured with ControlMaster/
# ControlPersist and NO keepalive (verified 2026-09-23: zero
# ServerAliveInterval/TCPKeepAlive directives in the generated ssh.config,
# which Lima regenerates on every start, so it cannot be durably fixed there).
# The forward therefore dies silently every few minutes — distinct from the
# daemon simply being slow: a dead forward refuses in ~30ms, a busy daemon
# hangs for minutes. colima-health-check.sh repairs it on its 5-minute tick.
#
# Dying instantly on a condition that self-heals inside 5 minutes is what makes
# this job a coin flip unattended. This does NOT weaken the gate: after the
# budget expires the caller still fails exactly as before. It only refuses to
# call a transient outage a permanent one.
# Worst case the health check needs to repair the forward: up to 300s for the
# upgrade lock to go stale, up to 300s until its next 5-minute tick, ~80s to
# bounce. 420s could not cover that — a run was ~2 minutes short of surviving
# on 2026-09-23 and only finished because a human released the lock by hand.
SUNDAY_DOCKER_WAIT="${SUNDAY_DOCKER_WAIT:-900}"

_wait_for_docker() {
  local waited=0
  docker info >/dev/null 2>&1 && return 0
  while [ "$waited" -lt "$SUNDAY_DOCKER_WAIT" ]; do
    log "apply: docker socket unreachable — waiting for repair (${waited}s/${SUNDAY_DOCKER_WAIT}s)"
    sleep 30
    waited=$(( waited + 30 ))
    if docker info >/dev/null 2>&1; then
      log "apply: docker socket recovered after ${waited}s"
      return 0
    fi
  done
  return 1
}

SUNDAY_BUILD_VIA_VM="${SUNDAY_BUILD_VIA_VM:-0}"
SUNDAY_BUILD_VM_TIMEOUT="${SUNDAY_BUILD_VM_TIMEOUT:-5400}"   # per-service ceiling, seconds
SUNDAY_BUILD_VM_POLL="${SUNDAY_BUILD_VM_POLL:-20}"           # sentinel poll interval, seconds

_build_one_service() {
  local svc="$1"
  if [ "$SUNDAY_BUILD_VIA_VM" != "1" ]; then
    $COMPOSE_CMD build --pull "$svc"
    return $?
  fi

  # The VM carries only the compose *plugin*, never the standalone binary.
  local vm_cmd="${COMPOSE_CMD/docker-compose/docker compose}"
  local tag="sunday-build-${svc}-$$"
  local vlog="/tmp/${tag}.log" vrc="/tmp/${tag}.rc"

  # Run the build DETACHED inside the VM and poll for an exit-code sentinel,
  # rather than holding one long SSH channel open for the whole build. On
  # 2026-09-23 07:10 a build that had already reached "naming to ... done"
  # died with ssh's own "exit status 255" when its channel dropped, and the
  # script reported that as a build failure. Detached, a dropped channel costs
  # one poll interval; the build itself never notices. versions.env is
  # re-sourced in the VM because the remote shell inherits nothing from here
  # and compose would otherwise bake blank version pins.
  local remote
  remote=$(printf '%s\n' \
    "cd '$REPO' || exit 90" \
    "set -a; . docker/versions.env || exit 91; set +a" \
    "$vm_cmd build --pull $svc > '$vlog' 2>&1" \
    "echo \$? > '$vrc'")
  # base64 so no quoting of the remote program survives a trip through ssh.
  local b64; b64=$(printf '%s' "$remote" | base64 | tr -d '\n')

  log "apply: building '$svc' INSIDE the VM, detached (SUNDAY_BUILD_VIA_VM=1)"
  if ! colima ssh -- sh -c "rm -f '$vrc'; echo $b64 | base64 -d > '/tmp/${tag}.sh'; nohup sh '/tmp/${tag}.sh' >/dev/null 2>&1 & echo launched" >/dev/null 2>&1; then
    log "ERROR: apply: could not launch the in-VM build for '$svc'"
    return 1
  fi

  local waited=0 rc=""
  while [ "$waited" -lt "$SUNDAY_BUILD_VM_TIMEOUT" ]; do
    sleep "$SUNDAY_BUILD_VM_POLL"
    waited=$(( waited + SUNDAY_BUILD_VM_POLL ))
    # Re-stamp the lock so the health check keeps deferring its VM bounce for
    # as long as this build is genuinely alive, and no longer.
    printf '%s\n' "$$" > "$UPGRADE_LOCK" 2>/dev/null || true
    # An SSH drop reads as empty here; the next tick opens a fresh connection.
    rc=$(colima ssh -- sh -c "cat '$vrc' 2>/dev/null" 2>/dev/null | tr -cd '0-9')
    [ -n "$rc" ] && break
  done

  # Surface the build's own tail so a failure is diagnosable from this log.
  colima ssh -- sh -c "tail -n 40 '$vlog' 2>/dev/null" 2>/dev/null | sed 's/^/    | /'
  colima ssh -- sh -c "rm -f '/tmp/${tag}.sh'" >/dev/null 2>&1 || true

  if [ -z "$rc" ]; then
    log "ERROR: apply: in-VM build for '$svc' did not finish within ${SUNDAY_BUILD_VM_TIMEOUT}s"
    return 1
  fi
  return "$rc"
}

_buildable_services() {
  $COMPOSE_CMD config 2>/dev/null | awk '
    /^  [a-zA-Z0-9_-]+:$/ { svc=$1; sub(/:$/,"",svc) }
    /^    build:/ { if (svc != "") print svc }
  ' | sort -u || true
  # Same pipefail hazard as _dirty_build_files above — never let an empty or
  # partially-failing pipeline take down the caller via a failed assignment.
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

  _wait_for_docker || die 10 "docker daemon unreachable after ${SUNDAY_DOCKER_WAIT}s (DOCKER_HOST=${DOCKER_HOST:-<unset>}) — is Colima running?"
  log "preflight: docker daemon reachable"

  [ -f "$COMPOSE_FILE" ] || die 10 "compose file not found: $COMPOSE_FILE"
  $COMPOSE_CMD config -q 2>/dev/null \
    || die 10 "compose config is invalid: $COMPOSE_CMD config"
  log "preflight: compose config valid ($COMPOSE_CMD)"

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
  local tagged=0 skipped=0 failed=0 c id
  for c in $CONTAINERS; do
    id="$(docker inspect --format '{{.Image}}' "$c" 2>/dev/null || true)"
    if [ -z "$id" ]; then
      # Not running. Legitimate for profile-gated services (hermes-v2,
      # voice-gateway), but it used to `continue` in silence, so a container
      # that was down for a BAD reason left no anchor and no trace of it.
      skipped=$((skipped + 1))
      log "baseline: $c is not running — no rollback anchor captured for it"
      continue
    fi
    if _mutating; then
      if docker tag "$id" "agentshroud-rollback/${c}:${TODAY}" 2>/dev/null; then
        tagged=$((tagged + 1))
      else
        failed=$((failed + 1))
        err "baseline: could not retag $c for rollback"
      fi
    else
      tagged=$((tagged + 1))
    fi
  done
  if _mutating; then
    log "baseline: retagged ${tagged} image(s) as agentshroud-rollback/<container>:${TODAY} (skipped ${skipped} not running, ${failed} FAILED)"
  else
    log "baseline: [dry-run] would retag ${tagged} image(s) for rollback"
  fi

  # A running container we could see but could NOT anchor has no rollback path.
  # Building anyway is how 2026-09-24 went wrong: baseline logged
  #   "WARN: could not retag agentshroud-dev-openclaw for rollback"
  #   "retagged 4 image(s)"        <- four, not five
  #   "baseline: PASS"             <- and passed regardless
  # The run then built, failed on an unrelated service, and rolled back to the
  # PREVIOUS run's stale anchor — an OpenClaw one release older than the config
  # volume it had already migrated. It refused to start, 80 restarts.
  #
  # CLAUDE.md 0.0: a no-op must not be indistinguishable from a success. If we
  # cannot capture an anchor for a container that is right there and running,
  # the safe move is to refuse to build, not to hope nothing fails.
  if [ "$failed" -gt 0 ]; then
    die 10 "baseline: ${failed} running container(s) could not be anchored for rollback — refusing to build. A failed apply would roll back to a stale or absent image; verify the Docker daemon is healthy and re-run."
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
    echo '# 1. Restore code (branch-preserving)'
    echo "# Restores the WORKING TREE to the baseline commit without detaching HEAD."
    echo "# A bare \`git checkout <sha>\` detaches HEAD and silently strips the branch"
    echo "# out from under any later commit — observed 2026-09-11, where a rollback"
    echo "# left the repo detached at the pre-run commit."
    # SCOPED to the version-pin file, deliberately. This used to restore the
    # whole tree (`-- .`), which reverted the repo to the baseline COMMIT —
    # silently discarding anything committed during the run. The Sunday prompt
    # tells the session to commit as it goes ("one commit per logical
    # component"), so a rollback would throw that work away; it did exactly
    # that on 2026-09-15, wiping two commits made while an upgrade was in
    # flight. Rolling back an upgrade means undoing the VERSION BUMP, not
    # rewinding the repository.
    echo "git -C '$REPO' restore --source=$git_rev --staged --worktree -- docker/versions.env 2>/dev/null || \\"
    echo "  git -C '$REPO' checkout $git_rev -- docker/versions.env"
    echo ''
    echo '# Other files differing from the baseline are NOT reverted automatically —'
    echo '# they may be deliberate compat fixes, or unrelated work committed during'
    echo '# the run. Listed here so a human can decide, rather than losing them.'
    echo "_other=\"\$(git -C '$REPO' diff --name-only $git_rev -- . ':(exclude)docker/versions.env' 2>/dev/null)\""
    # shellcheck disable=SC2016  # literal text emitted into the generated script
    echo 'if [ -n "$_other" ]; then'
    echo '  echo "NOTE: these files differ from the upgrade baseline and were left untouched:"'
    # shellcheck disable=SC2016  # literal text emitted into the generated script
    printf '%s\n' '  printf "  %s\n" $_other'
    echo 'fi'
    echo ''
    echo '# 2. Restore images'
    for c in $CONTAINERS; do
      echo "docker tag agentshroud-rollback/${c}:${TODAY} \"\$(docker inspect --format '{{.Config.Image}}' ${c} 2>/dev/null || echo ${c}:latest)\" 2>/dev/null || true"
    done
    echo ''
    echo '# 3. Recreate containers from the restored images'
    echo '# hermes excluded — its container is managed by scripts/asb (run-standalone.sh),'
    # shellcheck disable=SC2016  # backticks are literal text in the generated script's comment
    echo '# not `docker compose up`; see the matching comment in phase_apply above.'
    # The `|| true` inside the generated command substitution is load-bearing:
    # the rollback script runs under `set -euo pipefail` (emitted above), and a
    # `grep -v` matching nothing exits 1, which would abort the ROLLBACK — the
    # one path that must never fail closed. Same hazard already documented on
    # _dirty_build_files/_buildable_services/phase_apply.
    echo "$COMPOSE_CMD up -d --force-recreate \$($COMPOSE_CMD config --services 2>/dev/null | grep -vx 'hermes' || true)"
    echo 'if docker image inspect agentshroud-rollback/agentshroud-hermes-v2:'"$TODAY"' >/dev/null 2>&1; then'
    echo "  docker tag agentshroud-rollback/agentshroud-hermes-v2:${TODAY} agentshroud/hermes:\${AGENTSHROUD_VERSION:-latest} 2>/dev/null || true"
    echo "  [ -x '$REPO/scripts/asb' ] && '$REPO/scripts/asb' up hermes || echo 'WARN: hermes image restored but not redeployed — run scripts/asb up hermes manually'"
    echo 'fi'
  } > "$ROLLBACK_SH"
  chmod +x "$ROLLBACK_SH"
  log "baseline: wrote executable rollback script $ROLLBACK_SH"
  log "baseline: PASS"
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: discover — what is the latest upstream release, really?
#
# For seven weeks this pipeline reported PASS every Sunday while rebuilding the
# SAME upstream version. OPENCLAW_VERSION was introduced as 2026.7.1 on
# 2026-07-29 and moved exactly once since, to the downstream counter 2026.7.1-2,
# while npm shipped 2026.8.1 through 2026.9.4. HERMES_VERSION moved once, in a
# feature PR, never in a Sunday run.
#
# The cause is stated in this script's own header: "the agent proposes versions;
# this script disposes." It builds whatever versions.env already says and never
# asked what was actually available — that was left to an LLM session's
# judgement, and the gates below then verified only that the rebuild worked.
# Rebuilding an identical version passes every one of them.
#
# Discovery is mechanical, so it belongs here rather than in a prompt.
# ═════════════════════════════════════════════════════════════════════════════
DISCOVERED_OPENCLAW_VERSION=""
DISCOVERED_HERMES_TAG=""
UPGRADE_AVAILABLE=0

phase_discover() {
  local discover_py="$REPO/scripts/discover_upstream_versions.py"
  if [ ! -f "$discover_py" ]; then
    warn "discover: $discover_py not found — cannot tell whether this run upgrades anything"
    return 0
  fi

  local out
  if ! out="$(python3 "$discover_py" --shell 2>/dev/null)"; then
    # Unreachable upstream is "unknown", never "already current" — the latter
    # would silently re-introduce the exact no-op this phase exists to catch.
    warn "discover: upstream lookup FAILED — treating latest as UNKNOWN, not as 'already current'"
    return 0
  fi
  eval "$out"

  log "discover: openclaw pinned=${OPENCLAW_VERSION:-<unset>} latest=${DISCOVERED_OPENCLAW_VERSION:-<unknown>}"
  log "discover: hermes   pinned=${HERMES_VERSION:-<unset>} latest_tag=${DISCOVERED_HERMES_TAG:-<unknown>}"

  if [ -n "$DISCOVERED_OPENCLAW_VERSION" ] \
     && [ "$DISCOVERED_OPENCLAW_VERSION" != "${OPENCLAW_VERSION:-}" ]; then
    UPGRADE_AVAILABLE=1
    warn "discover: OpenClaw is BEHIND — pinned ${OPENCLAW_VERSION:-<unset>}, latest ${DISCOVERED_OPENCLAW_VERSION}"
  fi
}

# ═════════════════════════════════════════════════════════════════════════════
# The NO-OP GATE.
#
# A run that rebuilt the same versions it started with upgraded nothing. That is
# a legitimate outcome ONLY when we are already on the latest release; it is a
# malfunction when a newer one exists. Before this gate the two were
# indistinguishable — both printed PASS — which is how seven weeks of "green"
# upgrades shipped no upgrade at all.
# ═════════════════════════════════════════════════════════════════════════════
PINS_BEFORE=""
_capture_pins() {
  grep -E '^(OPENCLAW_VERSION|HERMES_VERSION|HERMES_IMAGE)=' "$REPO/docker/versions.env" 2>/dev/null | sort || true
}

check_noop_gate() {
  local after
  after="$(_capture_pins)"
  if [ "$after" != "$PINS_BEFORE" ]; then
    log "no-op gate: PASS — upstream pins changed this run"
    UPGRADE_HAPPENED=1
    return 0
  fi

  UPGRADE_HAPPENED=0
  if [ "$UPGRADE_AVAILABLE" -eq 1 ]; then
    err "no-op gate: FAILED — this run changed no upstream pin, but a newer release exists."
    err "no-op gate:   OpenClaw pinned=${OPENCLAW_VERSION:-<unset>} latest=${DISCOVERED_OPENCLAW_VERSION:-<unknown>}"
    err "no-op gate: The stack may be healthy, but nothing was upgraded. Reporting this as"
    err "no-op gate: a PASS is what hid seven weeks of no-op Sunday runs."
    return 25
  fi
  log "no-op gate: NO-OP (honest) — already on the latest upstream release; nothing to upgrade"
  return 0
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: scan — real Trivy counts. Absence of a scanner, or of any image to
# point it at, is a FAILED gate, never a silent pass (repo rule: no fake
# green) — but both are provisioning problems to solve first, not reasons to
# skip: see scripts/lib/sunday-scan.sh (sourced above).
# ═════════════════════════════════════════════════════════════════════════════
phase_scan() {
  log "scan: CRITICAL/HIGH counts for: $SCAN_IMAGES"
  # shellcheck disable=SC2086  # word-splitting SCAN_IMAGES into args is intentional
  sunday_run_scan_gate "$SCAN_JSON" "$MAX_CRITICAL" $SCAN_IMAGES
}

# ═════════════════════════════════════════════════════════════════════════════
# PHASE: apply — rebuild and recreate from CURRENT pins.
# Version pins are edited by the session (judgement); this only builds/ships
# whatever docker/versions.env now says, then verify() decides if it survives.
# ═════════════════════════════════════════════════════════════════════════════
# ── Single-run enforcement ───────────────────────────────────────────────────
# Two applies on one stack corrupt each other. 2026-09-24: a launchd run started
# 09:16 and a manual run 09:31; both built images, both recreated containers,
# and both wrote UPGRADE_LOCK, each overwriting the other's pid. UPGRADE_LOCK is
# advisory and single-valued — it tells the health check "a build is live", it
# was never an exclusion mechanism, and it cannot become one without breaking
# that job. This is a separate, exclusive lock.
#
# mkdir is the atomic primitive here: it succeeds for exactly one caller and
# fails for every other, with no window between test and create. A pid file
# written then checked would race precisely when it matters.
#
# It fails SAFE. A crashed run must not block every future run forever, so a
# lock whose recorded pid is dead is reclaimed. Only a lock held by a LIVE
# process refuses the run.
APPLY_LOCK_DIR="${SUNDAY_APPLY_LOCK_DIR:-$HANDOFF_DIR/apply-running.lock.d}"
APPLY_LOCK_HELD=0

_release_apply_lock() {
  # Only ever remove a lock this process actually holds. If ours went stale and
  # another run reclaimed it, that lock is theirs and removing it would hand a
  # third run permission to start alongside them.
  [ "$APPLY_LOCK_HELD" = "1" ] || return 0
  rm -rf "$APPLY_LOCK_DIR" 2>/dev/null || true
  APPLY_LOCK_HELD=0
}

_take_apply_lock() {
  mkdir -p "$(dirname "$APPLY_LOCK_DIR")" 2>/dev/null || true
  if mkdir "$APPLY_LOCK_DIR" 2>/dev/null; then
    printf '%s\n' "$$" > "$APPLY_LOCK_DIR/pid" 2>/dev/null || true
    APPLY_LOCK_HELD=1
    return 0
  fi
  local other
  other="$(head -1 "$APPLY_LOCK_DIR/pid" 2>/dev/null | tr -cd '0-9')"
  if [ -n "$other" ] && kill -0 "$other" 2>/dev/null; then
    err "apply: another sunday-upgrade-apply run is already in progress (pid ${other})."
    err "apply: two runs on one stack build and recreate the same containers and corrupt each other."
    err "apply: wait for it to finish, or stop it deliberately, then re-run."
    return 1
  fi
  warn "apply: reclaiming a stale run lock (recorded pid '${other:-none}' is not running)"
  rm -rf "$APPLY_LOCK_DIR" 2>/dev/null || true
  if mkdir "$APPLY_LOCK_DIR" 2>/dev/null; then
    printf '%s\n' "$$" > "$APPLY_LOCK_DIR/pid" 2>/dev/null || true
    APPLY_LOCK_HELD=1
    return 0
  fi
  err "apply: could not take the run lock at $APPLY_LOCK_DIR"
  return 1
}

# ── Working-tree stability ───────────────────────────────────────────────────
# `docker compose build` bakes the working tree into the image, and this repo is
# checked out ONCE and shared: on 2026-09-24 a second session ran `git checkout`
# in the same directory while a run was live. Nothing crashed — the build simply
# would have shipped whatever files happened to be on disk at the moment each
# COPY ran, with no error and no trace in the image.
#
# So: record the commit at startup and re-assert it before building. This cannot
# make a shared checkout safe, but it turns a silent mis-build into a refusal.
HEAD_AT_START=""

_record_head() {
  HEAD_AT_START="$(git -C "$REPO" rev-parse HEAD 2>/dev/null || true)"
  [ -n "$HEAD_AT_START" ] && log "apply: working tree at $(printf '%.12s' "$HEAD_AT_START") ($(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?'))"
  return 0
}

_assert_head_unchanged() {
  # Not a git repo, or HEAD unreadable at startup: nothing to compare. Do not
  # invent a failure out of a missing baseline.
  [ -n "$HEAD_AT_START" ] || return 0
  local now
  now="$(git -C "$REPO" rev-parse HEAD 2>/dev/null || true)"
  [ -n "$now" ] || return 0
  [ "$now" = "$HEAD_AT_START" ] && return 0
  err "apply: the working tree MOVED mid-run: $(printf '%.12s' "$HEAD_AT_START") -> $(printf '%.12s' "$now")"
  err "apply: refusing to build — the image would contain code this run never preflighted or scanned."
  err "apply: this repo is a single shared checkout; another session or a human ran git checkout/reset here."
  return 1
}

# ── Build-cache hygiene ──────────────────────────────────────────────────────
# Build cache is NOT rollback material. Rollback restores TAGGED images
# (agentshroud-rollback/*), and `docker builder prune` never touches tags — so
# bounding the cache cannot weaken the rollback safety net.
#
# Why this exists: on 2026-09-23 the VM's docker volume hit 236G/236G with ZERO
# bytes free. Build cache alone had regenerated 57GiB in nine hours across five
# builds. The consequences were not subtle — openclaw's build died with
# "You don't have enough free space in /var/cache/apt/archives/", the gateway
# crashed on "sqlite3.OperationalError: disk I/O error" and never bound :8080,
# and openclaw/hermes crash-looped on ENOSPC (12 and 10 restarts). A weekly job
# that adds tens of GiB of cache and never removes any cannot run unattended.
#
# --max-used-space BOUNDS the cache instead of emptying it, so incremental
# builds stay fast (83s vs 8.5min from cold on this host) while growth is capped.
SUNDAY_BUILD_CACHE_MAX_GB="${SUNDAY_BUILD_CACHE_MAX_GB:-20}"
SUNDAY_BUILD_MIN_GB="${SUNDAY_BUILD_MIN_GB:-25}"

# Keep the upgrade lock fresh for the entire run, not only while building.
#
# The lock lapses after AGENTSHROUD_UPGRADE_LOCK_MAX_AGE (300s) so a dead run
# cannot suppress socket repair forever. But only the build poll loop was
# re-stamping it, which left every other phase unprotected — and the scan phase
# alone ran 19 minutes on 2026-09-23. A VM bounce there does not kill a build
# (there isn't one yet) but it does take out the run.
#
# The heartbeat is a child process that stamps the PARENT's pid and stops the
# moment the parent is gone, then drops the lock outright so repair resumes
# immediately rather than waiting out the staleness window. It must never
# outlive the run: that would be a guard that never lapses, which is worse
# than no guard at all.
_start_lock_heartbeat() {
  local parent=$$
  (
    # Detach stdio. A background child that inherits stdout keeps the write end
    # of any pipe open, so a caller capturing this script's output — `$(...)`,
    # a monitor, a log collector — blocks until the child exits, not until the
    # RUN exits. Observed 2026-09-24: a heartbeat that outlived its parent hung
    # a command substitution indefinitely.
    exec >/dev/null 2>&1
    while kill -0 "$parent" 2>/dev/null; do
      printf '%s\n' "$parent" > "$UPGRADE_LOCK" 2>/dev/null || true
      sleep "${SUNDAY_LOCK_HEARTBEAT:-30}"
    done
    rm -f "$UPGRADE_LOCK" 2>/dev/null || true
  ) &
  LOCK_HEARTBEAT_PID=$!
}

_prune_build_cache() {
  if ! _mutating; then
    log "cleanup: [dry-run] would bound build cache to ${SUNDAY_BUILD_CACHE_MAX_GB}GiB"
    return 0
  fi
  local before after bytes
  bytes=$(( SUNDAY_BUILD_CACHE_MAX_GB * 1024 * 1024 * 1024 ))
  before="$(_docker_free_gb 2>/dev/null || true)"
  log "cleanup: bounding build cache to ${SUNDAY_BUILD_CACHE_MAX_GB}GiB (docker storage free before: ${before:-unknown}GiB)"
  # Prune where buildx actually lives. The HOST docker CLI here drives the
  # legacy builder (no buildx component installed), which does not accept
  # --max-used-space at all — so this silently no-opped on its first real run
  # (2026-09-24 06:15:36: "cache NOT bounded this run", failing in the same
  # second rather than timing out). The VM's docker has buildx, and the cache
  # being bounded is the VM's disk anyway. Same colima-first shape as
  # _docker_free_gb above.
  local -a prune_cmd
  if command -v colima >/dev/null 2>&1 && colima status >/dev/null 2>&1; then
    prune_cmd=(colima ssh -- docker builder prune -f --max-used-space "$bytes")
  else
    prune_cmd=(docker builder prune -f --max-used-space "$bytes")
  fi
  # Never fail the run over cleanup: a successful upgrade must not be reported
  # as a failure because a prune timed out or the socket dropped mid-prune.
  if ! timeout "${SUNDAY_PRUNE_TIMEOUT:-1800}" "${prune_cmd[@]}" >/dev/null 2>&1; then
    warn "cleanup: build-cache prune did not complete (timeout or socket drop) — cache NOT bounded this run"
    return 0
  fi
  after="$(_docker_free_gb 2>/dev/null || true)"
  log "cleanup: build cache bounded (docker storage free after: ${after:-unknown}GiB)"
  return 0
}

# Refuse to start a build that cannot finish. The preflight disk gate only runs
# once, at the start; today's exhaustion happened DURING the run, between
# services, which is why openclaw died on ENOSPC after gateway and hermes had
# already built successfully.
_ensure_build_space() {
  local svc="$1" free
  free="$(_docker_free_gb 2>/dev/null || true)"
  printf '%s' "$free" | grep -Eq '^[0-9]+$' || return 0   # unknown: do not block
  [ "$free" -ge "$SUNDAY_BUILD_MIN_GB" ] && return 0
  warn "apply: only ${free}GiB free before building '$svc' (want >=${SUNDAY_BUILD_MIN_GB}GiB) — bounding build cache first"
  _prune_build_cache
  free="$(_docker_free_gb 2>/dev/null || true)"
  if printf '%s' "$free" | grep -Eq '^[0-9]+$' && [ "$free" -lt "$SUNDAY_BUILD_MIN_GB" ]; then
    err "apply: still only ${free}GiB free after bounding the build cache — refusing to start '$svc'"
    err "apply: a build that runs out of disk does not fail cleanly; it corrupts the run (2026-09-23: ENOSPC mid-build, sqlite 'disk I/O error', two containers crash-looping)"
    return 1
  fi
  return 0
}

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

  # Build ONE SERVICE AT A TIME, never all at once.
  # `docker compose build` builds every buildable service concurrently. On this
  # host that means several parallel Go toolchains — the gateway image compiles
  # cosign AND docker-cli from source — inside an 11GiB VM with ZERO swap. The
  # 2026-09-09 run died mid-build having written nothing past its first log line,
  # consuming 26GB of layers on the way; an OOM kill is the leading explanation.
  # Sequential builds cap peak memory at one toolchain and make any failure
  # attributable to a named service instead of a silent stall.
  _assert_head_unchanged || exit 10

  local svc build_list
  build_list="$(_buildable_services)"
  if [ -z "$build_list" ]; then
    warn "apply: no buildable services found in $COMPOSE_FILE — nothing to build"
  fi
  for svc in $build_list; do
    if ! _ensure_build_space "$svc"; then
      _attempt_rollback
      exit 30
    fi
    log "apply: building '$svc' (sequential)"
    if ! _build_one_service "$svc"; then
      err "apply: build FAILED for service '$svc'"
      _attempt_rollback
      exit 30
    fi
    log "apply: built '$svc' OK"
  done

  # The lock exists ONLY to stop the health check bouncing the VM into a live
  # build. Builds are done, so release it now: holding it past this point makes
  # the health check defer the very socket repair the next line waits for, which
  # on 2026-09-23 deadlocked a run until a human intervened.
  rm -f "$UPGRADE_LOCK" 2>/dev/null || true
  log "apply: builds complete — released the upgrade lock so socket repair can resume"

  # Builds run inside the VM and do not touch the host socket, but they take
  # long enough that the forward can die while we are busy. Everything after
  # this point (up, health, rollback) needs it, so wait rather than fail on an
  # outage that repairs itself.
  _wait_for_docker || { err "apply: docker socket did not return after the build"; _attempt_rollback; exit 30; }

  # `hermes` is profile-gated [hermes, full] so `docker compose build` above
  # builds it correctly, but its CONTAINER is deliberately NOT managed by
  # `docker compose up` in this repo — scripts/asb's own `up full` maps to
  # `--profile voice` (asb:475), not `full`, and hands hermes to a dedicated
  # docker/bots/hermes/run-standalone.sh via `_hermes_up` instead. That
  # script resolves secrets from $HOME/.agentshroud/.asb-secrets (ephemeral,
  # extracted per-run) and docker/secrets/, a mechanism `docker compose up`
  # knows nothing about — attempting hermes through compose here fails with
  # "bind source path does not exist" for any secret not present as a literal
  # docker/secrets/*.txt file, and failed while the marvin per-host compose
  # override was also trying to recreate it under a DIFFERENT container name
  # (agentshroud-marvin-hermes) than the one actually running
  # (agentshroud-hermes-v2, started previously via asb without that override)
  # — discovered 2026-09-14 when this exact path took the whole `up`, and
  # then the rollback, down with it (exit 50: manual recovery required).
  # Exclude it explicitly and defer to asb's own working path instead.
  local up_services
  # `|| true` is load-bearing — same pipefail hazard already documented on
  # _dirty_build_files and _buildable_services above. A `grep -v` that emits
  # nothing exits 1, which under `set -euo pipefail` propagates out of the
  # command substitution and kills the whole run at the assignment.
  up_services="$($COMPOSE_CMD config --services 2>/dev/null | grep -vx 'hermes' || true)"
  if [ -z "$up_services" ]; then
    err "apply: compose reported no services to recreate (other than hermes)"
    _attempt_rollback
    exit 30
  fi
  log "apply: recreating containers (excluding hermes — see comment above): ${up_services//$'\n'/ }"
  # shellcheck disable=SC2086  # up_services is a newline-separated list; splitting into args is intended
  if ! $COMPOSE_CMD up -d $up_services; then
    err "apply: compose up FAILED"
    _attempt_rollback
    exit 30
  fi
  if printf '%s\n' "$build_list" | grep -qx 'hermes'; then
    if [ -x "$REPO/scripts/asb" ]; then
      log "apply: hermes was rebuilt — deploying via scripts/asb up hermes (handles secrets correctly)"
      # asb's exit status covers everything it does, INCLUDING a trailing
      # image/build-cache prune. On 2026-09-23 hermes started cleanly and asb's
      # own post-deploy suite reported "11 checks, 11 passed, Stack is healthy"
      # — then the socket died during that prune, asb exited non-zero, and this
      # gate reported hermes as FAILED and triggered a rollback. Assert on the
      # container, per CLAUDE.md 0.0, and let the exit code inform rather than decide.
      local asb_rc=0 hermes_c
      "$REPO/scripts/asb" up hermes || asb_rc=$?
      hermes_c="$(_hermes_container || true)"
      if [ -z "$hermes_c" ]; then
        # No hermes entry in CONTAINERS means we cannot assert on state, so the
        # exit code is all we have — fall back to trusting it rather than
        # silently passing, which would be the 0.0 defect in the other direction.
        if [ "$asb_rc" -ne 0 ]; then
          err "apply: 'scripts/asb up hermes' exited $asb_rc and no hermes container is listed in CONTAINERS to verify against"
          _attempt_rollback
          exit 30
        fi
      elif ! _container_is_up "$hermes_c"; then
        err "apply: hermes did not come up (asb exited $asb_rc)"
        _attempt_rollback
        exit 30
      elif [ "$asb_rc" -ne 0 ]; then
        warn "apply: 'scripts/asb up hermes' exited $asb_rc, but $hermes_c is running and not unhealthy — treating as deployed. asb's status includes its trailing prune, which fails independently of the deploy."
      fi
    else
      warn "apply: hermes image rebuilt but scripts/asb not found/executable — hermes container NOT redeployed; the new image is tagged and ready, redeploy manually with 'scripts/asb up hermes'"
    fi
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

  # Health is sampled AFTER the soak, never before.
  # A container that has just started is legitimately "starting" for the duration
  # of its healthcheck start_period. Sampling at t=0 (as this did until
  # 2026-09-11) made every freshly-restarted stack report FAILED and escalate to
  # an unnecessary rollback — observed live after a Colima restart, where gateway
  # and openclaw read health=starting 11 seconds in and were both fully healthy a
  # couple of minutes later. After a full soak the start_period has elapsed, so
  # "starting" at THIS point is a real failure rather than a normal transient.
  for c in $CONTAINERS; do
    local health
    health="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$c" 2>/dev/null || echo 'absent')"
    case "$health" in
      healthy)   log "verify: $c healthy (post-soak)" ;;
      none)      log "verify: $c has no healthcheck defined (not a failure)" ;;
      absent)    ;;  # already reported by the running check
      starting)  failures="${failures}\n  - ${c}: still health=starting after ${SOAK_SECONDS}s soak"
                 err "verify: $c STILL starting after ${SOAK_SECONDS}s — start_period should have elapsed" ;;
      *)         failures="${failures}\n  - ${c}: health=${health}"
                 err "verify: $c health=$health" ;;
    esac
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
# True when a container is running and not unhealthy, waiting out its start
# period. Used to judge a deploy by the container's STATE rather than by the
# exit status of the tool that deployed it — see the asb call site for why.
# The hermes container name is env-specific (dev carries a "-dev-" infix), so
# take it from CONTAINERS rather than hardcoding either spelling.
_hermes_container() {
  local c
  for c in $CONTAINERS; do
    case "$c" in *hermes*) printf '%s' "$c"; return 0 ;; esac
  done
  return 1
}

_container_is_up() {
  local name="$1" budget="${2:-240}" waited=0 state health
  while :; do
    state="$(docker inspect --format '{{.State.Status}}' "$name" 2>/dev/null || echo absent)"
    health="$(docker inspect --format '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$name" 2>/dev/null || echo none)"
    if [ "$state" = "running" ] && { [ "$health" = "healthy" ] || [ "$health" = "none" ]; }; then
      return 0
    fi
    [ "$waited" -ge "$budget" ] && break
    sleep 10
    waited=$(( waited + 10 ))
  done
  err "apply: container '$name' is state=$state health=$health after ${budget}s"
  return 1
}

# True ONLY when we can prove the rollback anchor predates the config volume it
# would be restored against.
#
# OpenClaw records the version that last wrote its config as
# "lastTouchedVersion" in openclaw.json, and refuses to start when the binary is
# older than that:
#   Refusing to run automatic gateway startup migrations because this OpenClaw
#   binary (2026.9.5) is older than the config last written by OpenClaw 2026.9.6.
# Config migrations are one-way. Restoring an older IMAGE without restoring the
# CONFIG therefore does not restore service — it produces a container that can
# never start. Observed twice on 2026-09-24: 80 restarts, then 52.
#
# Deliberately conservative: it returns false whenever anything cannot be read,
# because refusing a rollback that would have worked strands a stack that could
# have been recovered. Only a proven downgrade blocks.
_rollback_target_predates_config() {
  local c="" cand anchor cfg_ver img_ver older
  for cand in $CONTAINERS; do
    case "$cand" in *openclaw*) c="$cand"; break ;; esac
  done
  [ -n "$c" ] || return 1

  anchor="agentshroud-rollback/${c}:${TODAY}"
  docker image inspect "$anchor" >/dev/null 2>&1 || return 1

  cfg_ver="$(docker exec "$c" sh -c 'grep -oE "\"lastTouchedVersion\": *\"[^\"]+\"" /home/node/.openclaw/openclaw.json 2>/dev/null | head -1' 2>/dev/null \
    | sed -E 's/.*"([^"]+)"$/\1/' || true)"
  img_ver="$(docker run --rm --entrypoint cat "$anchor" /app/.openclaw-image-version 2>/dev/null | tr -d '[:space:]' || true)"
  [ -n "$cfg_ver" ] && [ -n "$img_ver" ] || return 1
  [ "$cfg_ver" = "$img_ver" ] && return 1

  older="$(printf '%s\n%s\n' "$img_ver" "$cfg_ver" | sort -V | head -1)"
  [ "$older" = "$img_ver" ] || return 1
  ROLLBACK_BLOCK_IMG="$img_ver"
  ROLLBACK_BLOCK_CFG="$cfg_ver"
  return 0
}

_attempt_rollback() {
  if ! _mutating; then
    log "rollback: [dry-run] nothing was changed, nothing to roll back"
    return 0
  fi
  if [ ! -x "$ROLLBACK_SH" ]; then
    err "rollback: no rollback script at $ROLLBACK_SH — baseline phase did not run. MANUAL INTERVENTION REQUIRED."
    exit 50
  fi
  # The socket dies on its own every few minutes (Lima SSH forward, no
  # keepalive). Rolling back through a dead socket fails for reasons that have
  # nothing to do with the stack, and on 2026-09-23 that printed "STACK MAY BE
  # DEGRADED" three times over a stack that was entirely healthy. Wait first,
  # and if the daemon never returns say THAT, rather than inventing damage.
  if ! _wait_for_docker; then
    die 50 "rollback: Docker daemon unreachable after ${SUNDAY_DOCKER_WAIT}s — rollback NOT attempted, stack state UNKNOWN. Check 'colima ssh -- docker ps' before assuming damage."
  fi
  # Owner decision 2026-09-25: refuse rather than restore something that cannot
  # run. A rollback that bricks the service is worse than one that declines and
  # says so — the operator still has a running (if un-upgraded) stack to reason
  # about, instead of a crash loop plus a "rollback completed" line.
  if _rollback_target_predates_config; then
    err "rollback: REFUSING to restore openclaw."
    err "rollback: the anchor image is ${ROLLBACK_BLOCK_IMG}, but its config volume was last written by ${ROLLBACK_BLOCK_CFG}."
    err "rollback: OpenClaw refuses to start against a config newer than the binary, so this restore would not recover service — it would leave a container that can never start (2026-09-24: 80 restarts)."
    err "rollback: the stack has been left exactly as it is. Recover by deploying an openclaw image >= ${ROLLBACK_BLOCK_CFG}, or by restoring the config volume alongside the image."
    die 50 "rollback REFUSED: restore target predates its own config — MANUAL INTERVENTION REQUIRED"
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

  # A partial run proves nothing about the phases it never executed. Writing
  # status=PASS after e.g. `--phase scan` published a gate asserting
  # "preflight, scan, apply and verify all passed ... including a 120s
  # stability soak" when only the scan ran — a false green in the one file
  # prod's gate actually reads. Only a full-pipeline run may publish a PASS;
  # a partial run leaves any existing handoff untouched rather than
  # overwriting it with a weaker claim. FAIL is always allowed through: a
  # failure in any single phase is real, and prod staying blocked is the safe
  # direction.
  if [ "$status" = "PASS" ] && [ "$PHASE" != "all" ]; then
    log "handoff: --phase=${PHASE} is a partial run — NOT writing a PASS handoff (only --phase=all may publish one)"
    return 0
  fi

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
    printf '  "phase": "%s",\n' "$PHASE"
    # Whether this run actually moved an upstream pin. A green run that
    # upgraded nothing is exactly what went unnoticed for seven weeks, so the
    # handoff has to record it rather than leaving PASS to imply it.
    printf '  "upgraded": %s,\n' "$([ "${UPGRADE_HAPPENED:-0}" -eq 1 ] && echo true || echo false)"
    printf '  "latest_openclaw_seen": "%s",\n' "${DISCOVERED_OPENCLAW_VERSION:-unknown}"
    printf '  "versions": {\n    %s\n  },\n' "$versions"
    printf '  "notes": "Written by sunday-upgrade-apply.sh with --phase=%s. status=PASS is only ever published by a full --phase=all run, and means preflight, scan, apply and verify all passed on dev, including a %ss stability soak."\n' "$PHASE" "$SOAK_SECONDS"
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
# shellcheck disable=SC2154  # rc is assigned by the trap body itself, immediately before use
# NEVER `kill "${LOCK_HEARTBEAT_PID:-0}"` here: an unset variable makes that
# `kill 0`, which signals the ENTIRE PROCESS GROUP, not "nothing". Written that
# way it killed the test runner that evaluates this line (2026-09-24), and in a
# real run it would have taken down whatever shared the group. Kill only a pid
# we actually recorded.
trap 'rc=$?; if [ -n "${LOCK_HEARTBEAT_PID:-}" ]; then kill "$LOCK_HEARTBEAT_PID" 2>/dev/null || true; fi; rm -f "$UPGRADE_LOCK" 2>/dev/null || true; _release_apply_lock; if [ $rc -ne 0 ]; then write_handoff FAIL; fi' EXIT
mkdir -p "$(dirname "$UPGRADE_LOCK")" 2>/dev/null || true
printf '%s\n' "$$" > "$UPGRADE_LOCK" 2>/dev/null || true
LOCK_HEARTBEAT_PID=""
_start_lock_heartbeat

# Exclusive: refuse to run alongside another apply. Exit 10 = preconditions are
# wrong, nothing has been mutated yet.
_take_apply_lock || exit 10
_record_head

PINS_BEFORE="$(_capture_pins)"

_should_run preflight && phase_preflight
_should_run discover  && phase_discover
_should_run baseline  && phase_baseline
_should_run scan      && phase_scan
_should_run apply     && phase_apply
_should_run verify    && phase_verify

# The no-op gate only judges a FULL run. A partial --phase invocation was never
# trying to upgrade anything, so "no pin changed" says nothing about it.
if [ "$PHASE" = "all" ]; then
  noop_rc=0
  check_noop_gate || noop_rc=$?
  if [ "$noop_rc" -ne 0 ]; then
    write_handoff NOTHING_UPGRADED
    exit "$noop_rc"
  fi
fi

# Bound the cache BEFORE declaring success, so the disk this run consumed is
# given back as part of the run rather than left for the next one to trip over.
_prune_build_cache

write_handoff PASS
log "=== sunday-upgrade-apply COMPLETE: all requested phases passed ==="
log "artifacts: $ARTIFACT_DIR"
exit 0
