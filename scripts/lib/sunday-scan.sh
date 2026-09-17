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

sunday_run_scan_gate() {
  local scan_json="$1" max_critical="$2"
  shift 2
  local images=("$@")

  if ! sunday_ensure_trivy; then
    if [ -n "$max_critical" ]; then
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
  local total_crit=0 first=1 scanned=0 body=""
  local img resolved out crit high
  for img in "${images[@]}"; do
    if ! resolved="$(sunday_resolve_scan_image "$img")"; then
      warn "scan: no local image found at all for $img — nothing to scan"
      continue
    fi
    out="$("${TRIVY_CMD[@]}" image --quiet --scanners vuln --severity CRITICAL,HIGH \
            --format json "$resolved" 2>/dev/null || true)"
    if [ -z "$out" ]; then
      warn "scan: trivy returned nothing for $resolved"
      continue
    fi
    crit="$(printf '%s' "$out" | grep -o '"Severity": *"CRITICAL"' | wc -l | tr -d ' ')"
    high="$(printf '%s' "$out" | grep -o '"Severity": *"HIGH"'     | wc -l | tr -d ' ')"
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
  printf '{\n  "scanner": "trivy",\n  "images": {\n%s\n  }\n}\n' "$body" > "$scan_json"

  log "scan: wrote $scan_json (total CRITICAL across images: ${total_crit}, images scanned: ${scanned})"

  if [ "$scanned" -eq 0 ]; then
    if [ -n "$max_critical" ]; then
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
