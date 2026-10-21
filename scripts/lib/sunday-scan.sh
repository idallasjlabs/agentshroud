# shellcheck shell=bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/lib/sunday-scan.sh — Sunday-upgrade CVE scan-gate logic.
#
# Extracted out of sunday-upgrade-apply.sh's phase_scan so it can be sourced
# and unit-tested with a controlled PATH (scripts/smoke.d/test-sunday-upgrade-scan.sh)
# — the top-level script hardens its own PATH to `/opt/homebrew/bin:...`
# ahead of everything (sunday-upgrade-apply.sh:59, deliberately, to survive a
# launchd PATH that lacks Homebrew), which is exactly what a test double
# needs to NOT be shadowed by. This file has no such hardening and produces
# no side effects on source — callers explicitly invoke the functions below.
#
# Bug this exists to prevent regressing (phantom-tag false pass): the scan
# gate used to look up images by AGENTSHROUD_VERSION (docker/versions.env),
# but that pin is bumped by session judgement BEFORE the corresponding image
# is rebuilt, and scan runs BEFORE apply/build. So the pinned tag routinely
# doesn't exist yet at scan time — `docker image inspect` fails for every
# image, every image gets skipped, and the old code still printed
# "scan: PASS" with 0 CRITICAL. That is a fake green, not a real CVE
# baseline: no image was ever actually scanned.
#
# Public API:
#   sunday_ensure_trivy                 - populate TRIVY_CMD; provisions via
#                                          `nix shell nixpkgs#trivy` if trivy
#                                          isn't already on PATH (repo policy
#                                          is Nix-first, never apt/brew).
#   sunday_resolve_scan_image <target>  - echo a `repo:tag` that actually
#                                          exists locally for the given
#                                          pinned target, falling back to
#                                          whatever tag IS present for that
#                                          repo so the gate scans the real,
#                                          currently-deployed image instead
#                                          of silently skipping it.
#   sunday_run_scan_gate <scan_json_path> <max_critical> <image>...
#                                        - run the full gate. Writes the
#                                          per-image findings to
#                                          scan_json_path. Calls `die` (must
#                                          already be defined by the caller,
#                                          or the fallback below) on a real
#                                          gate failure; never reports PASS
#                                          without at least one image having
#                                          actually been scanned.
#   sunday_handoff_status <status> <scanned> <failed>
#                                        - downgrade a PASS to SCAN_INCOMPLETE
#                                          when no image scanned or any failed.
#   sunday_dev_handoff_gate <dir> <today>
#                                        - prod's gate: today's dev PASS only.
#
# Callers are expected to already define log/warn/die (sunday-upgrade-apply.sh
# does); fallbacks are provided below so this file is independently testable.

if ! declare -f log >/dev/null 2>&1; then
  log() { printf '[scan] %s\n' "$*"; }
fi
if ! declare -f warn >/dev/null 2>&1; then
  warn() { printf '[scan] WARN: %s\n' "$*" >&2; }
fi
if ! declare -f die >/dev/null 2>&1; then
  die() { local code="$1"; shift; printf '[scan] ERROR: %s\n' "$*" >&2; exit "$code"; }
fi

TRIVY_CMD=(trivy)

sunday_ensure_trivy() {
  command -v trivy >/dev/null 2>&1 && { TRIVY_CMD=(trivy); return 0; }
  if ! command -v nix >/dev/null 2>&1; then
    return 1
  fi
  warn "scan: trivy not on PATH — provisioning via 'nix shell nixpkgs#trivy' (repo policy: Nix-first, never apt/brew)"
  if nix shell nixpkgs#trivy --command trivy --version >/dev/null 2>&1; then
    TRIVY_CMD=(nix shell nixpkgs#trivy --command trivy)
    return 0
  fi
  warn "scan: 'nix shell nixpkgs#trivy' failed to provision a working trivy"
  return 1
}

sunday_resolve_scan_image() {
  local target="$1" repo fallback
  if docker image inspect "$target" >/dev/null 2>&1; then
    printf '%s\n' "$target"
    return 0
  fi
  repo="${target%:*}"
  fallback="$(docker images --format '{{.Repository}}:{{.Tag}}' "$repo" 2>/dev/null | grep -v ':<none>$' | head -1)"
  if [ -n "$fallback" ]; then
    warn "scan: $target not built yet — scanning currently-deployed $fallback instead"
    printf '%s\n' "$fallback"
    return 0
  fi
  return 1
}

# Warn while there is still time to act. Trivy silently stops honouring an entry
# the moment it expires, so without this an acceptance lapses as a surprise —
# and under the current policy (dev warns, prod enforces) the surprise would
# land in a Sunday prod window with no lead time. Daily dev runs now flag it for
# SUNDAY_IGNORE_WARN_DAYS beforehand.
_sunday_warn_expiring_acceptances() {
  local file="$1" days="${SUNDAY_IGNORE_WARN_DAYS:-30}" line
  command -v python3 >/dev/null 2>&1 || return 0
  # Piped through warn() when it's defined, not printed straight to stdout:
  # sunday_run_scan_gate's stdout is machine-consumed elsewhere (tests capture
  # it expecting only the gate's own accounting output), so this diagnostic
  # must honour the same log-routing contract as every other message in this
  # library rather than bypass it. Falls back to echo when this function is
  # sourced/eval'd standalone (outside sunday-upgrade-apply.sh, where warn()
  # isn't defined) so the warning is never silently swallowed either way.
  while IFS= read -r line; do
    if declare -f warn >/dev/null 2>&1; then
      warn "$line"
    else
      echo "$line"
    fi
  done < <(python3 - "$file" "$days" <<'PYEOF' 2>/dev/null || true
import sys, datetime, re
path, days = sys.argv[1], int(sys.argv[2])
try:
    text = open(path, encoding="utf-8").read()
except OSError:
    sys.exit(0)
today = datetime.date.today()
# Deliberately regex, not a YAML parser: this must never be the reason a scan
# fails, and PyYAML is not guaranteed present on the host.
ids = re.findall(r"-\s*id:\s*(\S+)", text)
exps = re.findall(r"expiredAt:\s*(\d{4}-\d{2}-\d{2})", text)
for cve, exp in zip(ids, exps):
    try:
        d = datetime.date.fromisoformat(exp)
    except ValueError:
        continue
    left = (d - today).days
    if left < 0:
        print(f"scan: accepted-risk entry {cve} EXPIRED {-left}d ago ({exp}) — it now counts against the gate")
    elif left <= days:
        print(f"scan: accepted-risk entry {cve} expires in {left}d ({exp}) — re-review before it lapses")
PYEOF
  )
}

sunday_run_scan_gate() {
  local scan_json="$1" max_critical="$2"
  shift 2
  local images=("$@")

  # Scan INTEGRITY enforcement is separate from the --max-critical threshold.
  # --max-critical asks "are there too many findings"; this asks the prior
  # question, "did the scanner actually run". Owner decision 2026-09-25: prod
  # fails closed, dev warns — prod can never ship an image nothing scanned,
  # while a scanner outage does not halt dev iteration.
  local enforce="${SUNDAY_SCAN_ENFORCE:-0}"

  # Accepted-risk register. Entries carry a justification, the arm-2 control
  # covering the class, and an expiry that trivy honours natively — on that date
  # the CVE counts again and the gate fails, forcing re-review instead of
  # permanent amnesty. Two CRITICALs live here because they have no fixed
  # version in ANY Debian release (libxml2, openssh-client): without a register
  # a zero-CRITICAL gate could never pass and prod would be blocked forever.
  local ignore_args=() ignore_file="${SUNDAY_IGNORE_FILE:-${REPO:-.}/.trivyignore.yaml}"
  if [ -f "$ignore_file" ]; then
    ignore_args=(--ignorefile "$ignore_file")
    log "scan: applying accepted-risk register $ignore_file"
    _sunday_warn_expiring_acceptances "$ignore_file"
  else
    warn "scan: no accepted-risk register at $ignore_file — findings with no upstream fix will count against the gate"
  fi

  if ! sunday_ensure_trivy; then
    if [ -n "$max_critical" ] || [ "$enforce" = "1" ]; then
      die 20 "trivy not installed and could not be provisioned via 'nix shell nixpkgs#trivy', but --max-critical=$max_critical was requested — cannot enforce a CVE gate without a scanner. Refusing to report a pass."
    fi
    warn "scan: trivy not installed and could not be provisioned via Nix — SKIPPED. No CVE claim can be made from this run."
    printf '{"scanner": "absent", "images": {}}\n' > "$scan_json"
    return 0
  fi

  # Built up in a variable, not inside a `{ ... } > "$scan_json"` group: `log`
  # writes to stdout, and a redirected group redirects EVERYTHING printed
  # inside it, `log` included — which silently spliced each per-image log
  # line into the middle of the JSON, corrupting it. Dormant in the original
  # code because the phantom-tag bug meant every image was always skipped
  # before reaching that log call; fixing the fallback here means real scans
  # actually reach it, which is what surfaced this.
  local total_crit=0 first=1 scanned=0 failed=0 body=""
  local img resolved out crit high trc errf
  for img in "${images[@]}"; do
    if ! resolved="$(sunday_resolve_scan_image "$img")"; then
      warn "scan: no local image found at all for $img — nothing to scan"
      continue
    fi
    # stderr is CAPTURED, never discarded. Until 2026-09-24 this line ended in
    # `2>/dev/null || true`, so a crashing scanner and a clean image produced
    # the identical observable: an empty string, logged as "trivy returned
    # nothing". Three images were "scanned" that way for weeks. The real error,
    # once anybody looked at it, was one line long:
    #   unable to initialize a scan service: ... docker error: unable to get
    #   history (...docker.sock...); remote error: UNAUTHORIZED
    # trivy reaches local images THROUGH the docker socket, and when that socket
    # is down it falls back to a registry that 401s on local-only tags. A gate
    # that cannot tell "no vulnerabilities" from "the scanner never ran" is the
    # exact defect class CLAUDE.md 0.0 exists to forbid.
    # Retried, not single-shot. The vulnerability-DB download is the one part
    # of this call that's genuinely flaky on this host -- a transient network
    # hiccup fetching from the DB mirror (observed live 2026-10-04 and again
    # 2026-10-11, same symptom both times: image scan 0/3, scans FAILED 3,
    # recovered a few hours later by re-running --phase scan standalone once
    # the network had recovered) has, until now, had zero retry protection,
    # unlike the git-fetch hang fix from 2026-09-27. A single transient DB
    # fetch failure should not need a human to notice the handoff's stale
    # 0-images-scanned snapshot and re-run the scan by hand every week.
    errf=""
    trc=0
    out=""
    for _scan_try in 1 2 3; do
      errf="$(mktemp)"
      trc=0
      out="$(timeout 300 "${TRIVY_CMD[@]}" image --quiet --scanners vuln --severity CRITICAL,HIGH \
              "${ignore_args[@]}" --format json "$resolved" 2>"$errf")" || trc=$?
      if [ "$trc" -eq 0 ] && [ -n "$out" ]; then
        break
      fi
      if [ "$_scan_try" -lt 3 ]; then
        # SUNDAY_SCAN_RETRY_SLEEP overrides the per-attempt backoff unit
        # (default 60s, real runs); tests set it to 0 so this loop's retry
        # logic is exercised without three real minutes of sleeping.
        warn "scan: trivy failed for $resolved (attempt ${_scan_try}/3, exit ${trc}) — retrying in $((_scan_try * ${SUNDAY_SCAN_RETRY_SLEEP:-60}))s:"
        sed -n '1,6p' "$errf" | sed 's/^/      /' >&2
        sleep $((_scan_try * ${SUNDAY_SCAN_RETRY_SLEEP:-60}))
      fi
    done
    if [ "$trc" -ne 0 ] || [ -z "$out" ]; then
      failed=$((failed + 1))
      err "scan: trivy FAILED for $resolved after 3 attempts (exit ${trc}) — this is NOT a clean result:"
      sed -n '1,6p' "$errf" | sed 's/^/      /' >&2
      rm -f "$errf"
      continue
    fi
    rm -f "$errf"
    # grep exits 1 on zero matches (a clean image legitimately has 0 CRITICAL
    # findings), and under this file's `set -euo pipefail` caller that would
    # otherwise kill the whole run on the exact outcome a scan is supposed to
    # report cleanly. `|| true` inside the group keeps the pipeline's real
    # exit status at 0 for that case; `wc -l` still counts correctly on the
    # resulting empty input.
    crit="$(printf '%s' "$out" | { grep -o '"Severity": *"CRITICAL"' || true; } | wc -l | tr -d ' ')"
    high="$(printf '%s' "$out" | { grep -o '"Severity": *"HIGH"'     || true; } | wc -l | tr -d ' ')"
    total_crit=$((total_crit + crit))
    scanned=$((scanned + 1))
    if [ "$first" -eq 1 ]; then
      first=0
    else
      body="${body},"$'\n'
    fi
    body="${body}    \"${resolved}\": {\"critical\": ${crit}, \"high\": ${high}, \"resolved_from\": \"${img}\"}"
    log "scan: $resolved -> ${crit} CRITICAL / ${high} HIGH"
  done
  printf '{\n  "scanner": "trivy",\n  "scanned": %s,\n  "failed": %s,\n  "images": {\n%s\n  }\n}\n' \
    "$scanned" "$failed" "$body" > "$scan_json"

  log "scan: wrote $scan_json (total CRITICAL across images: ${total_crit}, images scanned: ${scanned}, scans FAILED: ${failed})"

  # A scanner that errored is not a clean bill of health. Surface it loudly even
  # when no --max-critical was requested, so a report cannot quietly describe an
  # unscanned image set as a CVE baseline.
  if [ "$failed" -gt 0 ]; then
    if [ -n "$max_critical" ] || [ "$enforce" = "1" ]; then
      die 20 "CVE gate FAILED: ${failed} image scan(s) errored — refusing to report a pass on findings the scanner never produced"
    fi
    warn "scan: ${failed} image scan(s) ERRORED (see the trivy output above). The counts below cover only the ${scanned} image(s) that actually scanned — this is NOT a complete CVE baseline."
  fi

  if [ "$scanned" -eq 0 ]; then
    if [ -n "$max_critical" ] || [ "$enforce" = "1" ]; then
      die 20 "CVE gate FAILED: no image could be scanned for any of: ${images[*]} — refusing to report a pass without a scanner having actually run"
    fi
    warn "scan: no image existed locally for any scan target — SKIPPED, not a real CVE baseline"
    return 0
  fi

  if [ -n "$max_critical" ] && [ "$total_crit" -gt "$max_critical" ]; then
    die 20 "CVE gate FAILED: ${total_crit} CRITICAL findings exceeds --max-critical=${max_critical}"
  fi
  log "scan: PASS (${scanned} image(s) scanned)"
}

# ── Handoff truth (CLAUDE.md §0.0) ───────────────────────────────────────────
# sunday_handoff_status <requested> <images_scanned> <scans_failed>
#   Echo the status the dev->prod handoff may honestly publish. Dev only WARNS
#   on scan failure (owner policy 2026-09-25), so a full run whose scanner never
#   produced a finding still reached `write_handoff PASS`: on 2026-10-11 the
#   handoff read status PASS with images_scanned:0, scans_failed:3. A PASS needs
#   at least one image scanned and none failed; anything else — including
#   "null" (no scan artefact at all) — is SCAN_INCOMPLETE. Non-PASS statuses
#   pass through unchanged.
sunday_handoff_status() {
  local requested="$1" scanned="${2:-null}" failed="${3:-null}"
  if [ "$requested" != "PASS" ]; then
    printf '%s\n' "$requested"
    return 0
  fi
  case "$scanned" in ''|*[!0-9]*) printf 'SCAN_INCOMPLETE\n'; return 0 ;; esac
  case "$failed"  in ''|*[!0-9]*) printf 'SCAN_INCOMPLETE\n'; return 0 ;; esac
  if [ "$scanned" -eq 0 ] || [ "$failed" -ne 0 ]; then
    printf 'SCAN_INCOMPLETE\n'
    return 0
  fi
  printf 'PASS\n'
}

# sunday_dev_handoff_gate <handoff_dir> <today>
#   Return 0 only when dev published a PASS for <today>: the file must be
#   dev-result-<today>.json AND its own "date" field must say <today>, so a
#   previous Sunday's PASS (or a copy of one under today's name) can never
#   unlock a prod apply. Prints the reason on refusal.
sunday_dev_handoff_gate() {
  local dir="$1" today="$2" f date status
  f="${dir}/dev-result-${today}.json"
  if [ ! -f "$f" ]; then
    printf 'dev handoff: %s does not exist — dev has not passed today\n' "$f" >&2
    return 1
  fi
  date="$(grep -oE '"date": *"[^"]*"' "$f" 2>/dev/null | head -1 | sed -E 's/.*"([^"]*)"$/\1/')"
  status="$(grep -oE '"status": *"[^"]*"' "$f" 2>/dev/null | head -1 | sed -E 's/.*"([^"]*)"$/\1/')"
  if [ "$date" != "$today" ]; then
    printf 'dev handoff: %s is dated "%s", not %s — stale, refusing\n' "$f" "$date" "$today" >&2
    return 1
  fi
  if [ "$status" != "PASS" ]; then
    printf 'dev handoff: %s has status "%s", not PASS — refusing\n' "$f" "$status" >&2
    return 1
  fi
  return 0
}

# ── Wall-clock cutoff and stack restore (owner directive 2026-10-18) ─────────
# "Everything is up and usable by 08:00 ET." The wrapper's 170-minute budget is
# relative to launch, so a late or slow run could still be mid-apply at 08:00.
# These give it an absolute stop and a guaranteed-working stack afterwards.

SUNDAY_REPO="${SUNDAY_REPO:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# sunday_deadline_epoch <HH:MM|off>
#   Print the epoch of today's HH:MM local, or nothing when the cutoff is off,
#   malformed, or already past (an 11:00 retry is not cut off at 07:20 — it
#   started after the window and the prompt's own 07:00/07:30 rules stop it
#   from touching prod). Computed as now + (deadline - now) in wall-clock
#   seconds, so it needs no GNU/BSD-specific `date` parsing. SUNDAY_NOW
#   ("<epoch> <HH> <MM> <SS>") pins the clock for tests.
sunday_deadline_epoch() {
  local spec="${1:-}" now h m s dh dm wall target
  case "$spec" in
    off|'') return 0 ;;
    [0-2][0-9]:[0-5][0-9]) ;;
    *) warn "cutoff: '$spec' is not HH:MM — wall-clock cutoff NOT armed"; return 0 ;;
  esac
  dh=$((10#${spec%%:*})); dm=$((10#${spec##*:}))
  if [ "$dh" -gt 23 ]; then
    warn "cutoff: '$spec' is not a time of day — wall-clock cutoff NOT armed"
    return 0
  fi
  # shellcheck disable=SC2046,SC2086  # word-splitting the clock fields is the point
  if [ -n "${SUNDAY_NOW:-}" ]; then set -- $SUNDAY_NOW; else set -- $(date '+%s %H %M %S'); fi
  now="$1"; h=$((10#$2)); m=$((10#$3)); s=$((10#$4))
  wall=$((h * 3600 + m * 60 + s))
  target=$((dh * 3600 + dm * 60))
  [ "$target" -gt "$wall" ] || return 0
  printf '%s\n' $((now + target - wall))
}

# sunday_stop_apply <lock_dir>
#   Killing the tmux session does not reliably take sunday-upgrade-apply.sh
#   with it (it may be mid `docker compose`), and restoring the stack while an
#   apply is still recreating containers corrupts both. Stop the pid recorded
#   in the apply lock: TERM, up to SUNDAY_STOP_WAIT seconds (default 60), then
#   KILL. A lock with no live pid is left for the next apply to reclaim.
sunday_stop_apply() {
  local lock="$1" pid i
  pid="$(head -1 "$lock/pid" 2>/dev/null | tr -cd '0-9')"
  [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null || return 0
  warn "restore: apply run (pid $pid) still alive after the session ended — stopping it"
  kill -TERM "$pid" 2>/dev/null || true
  i=0
  while kill -0 "$pid" 2>/dev/null && [ "$i" -lt "${SUNDAY_STOP_WAIT:-60}" ]; do
    sleep 1; i=$((i + 1))
  done
  if kill -0 "$pid" 2>/dev/null; then
    warn "restore: apply pid $pid ignored TERM — killing it"
    kill -KILL "$pid" 2>/dev/null || true
  fi
}

# Seams for sunday_restore_stack. Tests redefine them after sourcing.
# The check is the deploy gate's --functional mode: container health plus a
# real request through each service (post-deploy-check.sh F1-F4).
sunday_stack_check() {
  bash "$SUNDAY_REPO/scripts/post-deploy-check.sh" --functional
}
# The default stack is `asb up full` on the checkout as it stands. Its own
# post-deploy-check is skipped here because the ladder re-checks with
# --functional right after. Dev must never start Hermes with prod's Telegram
# token (409 conflict, eats owner messages).
sunday_stack_start() {
  local tg=0
  [ "${USER:-}" = "agentshroud-bot" ] && tg=1
  AGENTSHROUD_SKIP_POST_DEPLOY_CHECK=1 \
  AGENTSHROUD_HERMES_DISABLE_TELEGRAM="${AGENTSHROUD_HERMES_DISABLE_TELEGRAM:-$tg}" \
    bash "$SUNDAY_REPO/scripts/asb" up full
}
sunday_stack_rollback() {
  bash "$1"
}

# sunday_restore_stack <rollback_script>
#   Leave the stack working: check it; if that fails, start the default stack
#   and check again; if that fails too, run today's rollback anchor (written by
#   sunday-upgrade-apply.sh's baseline phase) and check once more. Prints one
#   of STACK_OK | STACK_RESTARTED | STACK_ROLLED_BACK | STACK_DEGRADED and
#   returns non-zero only for STACK_DEGRADED, which needs a human.
sunday_restore_stack() {
  local rollback="$1"
  if sunday_stack_check >&2; then echo STACK_OK; return 0; fi
  warn "restore: stack check failed — starting the default stack"
  sunday_stack_start >&2 || warn "restore: starting the default stack exited non-zero"
  if sunday_stack_check >&2; then echo STACK_RESTARTED; return 0; fi
  if [ ! -f "$rollback" ]; then
    warn "restore: no rollback anchor at $rollback — stack is DEGRADED, human required"
    echo STACK_DEGRADED
    return 1
  fi
  warn "restore: stack still failing — rolling back with $rollback"
  sunday_stack_rollback "$rollback" >&2 || warn "restore: rollback script exited non-zero"
  if sunday_stack_check >&2; then echo STACK_ROLLED_BACK; return 0; fi
  warn "restore: stack failing after rollback — DEGRADED, human required"
  echo STACK_DEGRADED
  return 1
}

# ── Direct owner notice (no Hermes) ─────────────────────────────────────────
# The upgrade report reaches the owner through Hermes's 08:30 cron. When the
# run ends DEGRADED, Hermes may be the thing that is down, so the one result
# that needs a human would never arrive. This sends a short notice straight to
# the Bot API from the host, the way docker/scripts/colima-health-check.sh
# does. sendMessage does not poll, so it never conflicts with a running bot.

# Seam: POSTs chat_id/text; reads a curl config line holding the URL (and so
# the token) on stdin — this Mac is shared with prod, and ps shows every
# user's argv. Tests redefine it after sourcing.
sunday_telegram_post() {
  curl -sS --max-time "${SUNDAY_NOTIFY_TIMEOUT:-15}" -K - \
    --data-urlencode "chat_id=$1" --data-urlencode "text=$2"
}

# sunday_notify_direct <token_file> <chat_id> <text>
#   Prints NOTIFY_SENT only when the Bot API answers ok with a message_id;
#   NOTIFY_FAILED (rejected or no answer) and NOTIFY_NO_TOKEN return non-zero.
sunday_notify_direct() {
  local token resp
  token="$(tr -d '[:space:]' < "$1" 2>/dev/null || true)"
  if [ -z "$token" ]; then echo NOTIFY_NO_TOKEN; return 1; fi
  resp="$(printf 'url = "https://api.telegram.org/bot%s/sendMessage"\n' "$token" \
    | sunday_telegram_post "$2" "$3" 2>/dev/null || true)"
  case "$resp" in
    *'"ok":true'*'"message_id"'*) echo NOTIFY_SENT; return 0 ;;
  esac
  echo NOTIFY_FAILED
  return 1
}

# sunday_run_summary <exit_code> <stack_state> <report_staged 0|1> <cut_off 0|1>
#   One plain-text notice for the owner, naming what the exit code means.
sunday_run_summary() {
  local rc="$1" stack="${2:-}" staged="${3:-0}" cut="${4:-0}" what
  case "$rc" in
    0) what="run complete" ;;
    1) what="FAILED (exit 1): the upgrade session died during boot" ;;
    3) what="FAILED (exit 3): git fetch origin main failed" ;;
    4) what="FAILED (exit 4): checkout not on main, or main diverged" ;;
    5) what="DEFERRED (exit 5): host memory pressure critical, next fire retries" ;;
    6) what="TIMED OUT (exit 6): no sentinel, next fire retries" ;;
    7) what="STACK DEGRADED (exit 7): restart and rollback both failed, human required" ;;
    *) what="FAILED (exit ${rc})" ;;
  esac
  printf 'AgentShroud Sunday upgrade %s on %s/%s: %s' \
    "$(date +%F)" "$(hostname -s 2>/dev/null || echo host)" "${USER:-?}" "$what"
  [ -n "$stack" ] && printf '\nStack: %s' "$stack"
  [ "$cut" = 1 ] && printf '\nSession cut off at %s' "${SUNDAY_UPGRADE_DEADLINE:-07:20}"
  [ "$staged" = 1 ] || printf '\nReport not staged for Hermes: see reports/ on the host'
  printf '\n'
}

# sunday_hermes_container — prints the running Hermes container's name, or
# nothing. Hermes is started with `docker run` (run-standalone.sh), so it has
# no compose label; it carries com.agentshroud.role=hermes instead. Same lookup
# as post-deploy-check.sh P3, including its fallback by name for containers
# started before that label existed. Dev is agentshroud-dev-hermes-v2, prod
# agentshroud-hermes-v2.
sunday_hermes_container() {
  local name
  name="$(docker ps --filter 'label=com.agentshroud.role=hermes' --format '{{.Names}}' 2>/dev/null | head -1)"
  [ -n "$name" ] || name="$(docker ps --format '{{.Names}}' 2>/dev/null | grep -E '^agentshroud-(dev-)?hermes' | head -1)"
  printf '%s' "$name"
}
