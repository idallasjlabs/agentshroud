#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# telemetry-check.sh — OT/BESS telemetry range, unit and timestamp validation (i-data-ai-ot gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="telemetry-check"; T_SUMMARY="OT/BESS telemetry range, unit and timestamp validation (i-data-ai-ot gate)"
T_OPTIONS="Usage: telemetry-check.sh --spec <spec.txt> <file.csv>...
  spec lines:  timestamp <column>   |   <column> <min> <max> [unit]   (# comments allowed)"
SPEC=""
t_parse "spec=SPEC" "$@"; t_init
if [ -z "$SPEC" ] || [ "${#T_POS[@]}" -eq 0 ]; then
    t_skip telemetry "need --spec <spec.txt> and at least one CSV file"
elif [ ! -f "$SPEC" ]; then
    t_die "spec file not found: $SPEC"
else
    for f in "${T_POS[@]}"; do
        [ -f "$f" ] || t_die "telemetry file not found: $f"
        out="$(awk -F, -v specfile="$SPEC" '
            BEGIN {
                while ((getline l < specfile) > 0) {
                    sub(/#.*/, "", l); n = split(l, p, " "); if (n == 0) continue
                    if (p[1] == "timestamp") tscol = p[2]
                    else if (n >= 3) { min[p[1]] = p[2]; max[p[1]] = p[3]; has[p[1]] = 1 }
                }
            }
            NR == 1 { for (i = 1; i <= NF; i++) { gsub(/[ \r]/, "", $i); col[i] = $i; if ($i == tscol) tsi = i } next }
            {
                for (i = 1; i <= NF; i++) {
                    c = col[i]; v = $i; gsub(/[ \r]/, "", v)
                    if (c in has) {
                        if (v == "" || v !~ /^-?[0-9.]+([eE]-?[0-9]+)?$/) { bad++; msg = msg "row " NR " " c "=" v " not numeric; "; continue }
                        if (v + 0 < min[c] + 0 || v + 0 > max[c] + 0) { bad++; msg = msg "row " NR " " c "=" v " out of [" min[c] "," max[c] "]; " }
                    }
                }
                if (tsi) {
                    t = $tsi; gsub(/[ \r]/, "", t)
                    if (t !~ /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9:.]+(Z|[+-][0-9:]+)$/) { bad++; msg = msg "row " NR " bad timestamp " t "; " }
                    else if (prev != "" && t < prev) { bad++; msg = msg "row " NR " timestamp goes backwards; " }
                    prev = t
                }
            }
            END { if (bad > 0) { print bad " violation(s): " substr(msg, 1, 300); exit 1 } }
        ' "$f" 2>&1)" && t_record "telemetry-$(basename "$f")" pass "ranges, units and timestamps valid" \
                      || t_record "telemetry-$(basename "$f")" fail "$out"
    done
fi
t_finish
