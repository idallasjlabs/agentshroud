#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# security-report-retention.sh — keep only the newest N scan reports per type.
#
# security-scan.sh writes a fresh timestamped report set (openscap, oscap,
# sbom, trivy, clamav) on every scheduled run with no cleanup, so these
# directories grow unbounded (observed: 4.4GB+2.4GB+1.6GB after ~1 week).
# Called daily by security-scheduler.sh; deterministic, no LLM/agent
# involvement, no host access — pure file retention on this container's own
# /var/log/security volume.

set -e

LOG_DIR="${LOG_DIR:-/var/log/security}"
KEEP="${SECURITY_REPORT_KEEP:-3}"

log() {
    echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] [retention] $*" >> "$LOG_DIR/scheduler.log"
}

for type_dir in openscap oscap sbom trivy clamav; do
    dir="$LOG_DIR/$type_dir"
    [ -d "$dir" ] || continue

    # Distinct timestamps present, newest first.
    timestamps=$(ls "$dir" 2>/dev/null | sed -E 's/^[a-z]+-([0-9]{8}-[0-9]{6}).*/\1/' | sort -ru)
    total=$(printf '%s\n' "$timestamps" | grep -c . || true)
    [ "$total" -le "$KEEP" ] && continue

    to_drop=$(printf '%s\n' "$timestamps" | tail -n +"$((KEEP + 1))")
    dropped_files=0
    for ts in $to_drop; do
        for f in "$dir"/*"$ts"*; do
            [ -e "$f" ] && rm -f "$f" && dropped_files=$((dropped_files + 1))
        done
    done
    log "$type_dir: kept newest $KEEP of $total report sets, removed $dropped_files file(s)"
done
