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
  local file="$1" days="${SUNDAY_IGNORE_WARN_DAYS:-30}"
  command -v python3 >/dev/null 2>&1 || return 0
  python3 - "$file" "$days" <<'PYEOF' 2>/dev/null || true
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
    errf="$(mktemp)"
    trc=0
    out="$("${TRIVY_CMD[@]}" image --quiet --scanners vuln --severity CRITICAL,HIGH \
            "${ignore_args[@]}" --format json "$resolved" 2>"$errf")" || trc=$?
    if [ "$trc" -ne 0 ] || [ -z "$out" ]; then
      failed=$((failed + 1))
      err "scan: trivy FAILED for $resolved (exit ${trc}) — this is NOT a clean result:"
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
