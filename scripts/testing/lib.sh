#!/usr/bin/env bash
# shellcheck disable=SC2034
# lib.sh — shared contract for scripts/testing/*.sh (sourced, not executed).
#   --help / -h          usage (exit 0)
#   --json               machine-readable result on stdout
#   I_GATE=report|block  report (default): print findings, exit 0 even on failure
#                        block: any failed check ⇒ exit 1
#   I_REPO=<dir>         repo to inspect (default: git toplevel of the cwd)
# Exit codes: 0 pass (or report-mode failure) · 1 fail in block mode · 2 misconfiguration.
# A missing optional tool is recorded as "skipped" with a WARN on stderr — never a silent pass.
# Bash 3.2 compatible; no jq dependency (scripts may run with a minimal PATH).

T_JSON=false
T_GATE="${I_GATE:-report}"
T_REPO=""
T_POS=()
T_ROWS=""          # newline-separated "id<TAB>status<TAB>detail"
T_NPASS=0; T_NFAIL=0; T_NSKIP=0

t_die() { echo "${T_NAME:-testing}: $*" >&2; exit 2; }

t_help() {
    printf '%s — %s\n\nUsage: %s [options]\n' "$T_NAME" "$T_SUMMARY" "$T_NAME.sh"
    [ -n "${T_OPTIONS:-}" ] && printf '%s\n' "$T_OPTIONS"
    cat <<'HELP'
  --json               machine-readable output
  -h, --help           this help

Environment:
  I_GATE=report|block  report (default) prints findings and exits 0; block exits 1 on failure
  I_REPO=<dir>         repository to inspect (default: git toplevel of the current directory)

Exit codes: 0 pass · 1 fail (block mode) · 2 misconfiguration.
A missing optional tool is reported as "skipped" with a warning, never as a pass.
HELP
}

# t_parse "flag=VAR flag2=VAR2" "$@" — value flags (--flag VALUE) map to variables; the rest are positional.
t_parse() {
    local spec="$1"; shift
    local arg pair flag var matched
    while [ $# -gt 0 ]; do
        arg="$1"; matched=false
        case "$arg" in
            -h|--help) t_help; exit 0 ;;
            --json)    T_JSON=true; shift; continue ;;
        esac
        for pair in $spec; do
            flag="--${pair%%=*}"; var="${pair#*=}"
            if [ "$arg" = "$flag" ]; then
                [ $# -ge 2 ] || t_die "$flag needs a value"
                printf -v "$var" '%s' "$2"; shift 2; matched=true; break
            fi
        done
        $matched && continue
        case "$arg" in
            -*) t_die "unknown option: $arg" ;;
            *)  T_POS+=("$arg"); shift ;;
        esac
    done
}

t_init() {
    case "$T_GATE" in report|block) ;; *) t_die "I_GATE must be 'report' or 'block' (got '$T_GATE')" ;; esac
    T_REPO="${I_REPO:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
    [ -d "$T_REPO" ] || t_die "repository directory not found: $T_REPO"
    cd "$T_REPO" || t_die "cannot cd to $T_REPO"
}

t_json_escape() {
    printf '%s' "$1" | LC_ALL=C tr -d '\000-\010\013-\037' | LC_ALL=C sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' -e "s/$(printf '\t')/\\\\t/g" \
        | awk 'NR>1{printf "\\n"} {printf "%s",$0}'
}

t_record() { # <id> <pass|fail|skipped> <detail>
    local id="$1" st="$2" detail="${3:-}"
    detail="$(printf '%s' "$detail" | LC_ALL=C tail -c 400)"
    T_ROWS="${T_ROWS}${id}$(printf '\t')${st}$(printf '\t')$(printf '%s' "$detail" | LC_ALL=C tr '\n\t' '  ')
"
    case "$st" in pass) T_NPASS=$((T_NPASS+1)) ;; fail) T_NFAIL=$((T_NFAIL+1)) ;; skipped) T_NSKIP=$((T_NSKIP+1)) ;; esac
}

t_skip() { # <id> <reason>
    echo "WARN [$T_NAME] $1 skipped: $2" >&2
    t_record "$1" skipped "$2"
}

# t_have <tool> <check-id> — true if installed, otherwise records a skip.
t_have() {
    if command -v "$1" >/dev/null 2>&1; then return 0; fi
    t_skip "$2" "$1 not installed — skipped"
    return 1
}

# t_run <id> <shell command> — pass on rc 0, fail otherwise (output kept as detail).
t_run() {
    local id="$1" out rc
    shift
    out="$(bash -c "$*" 2>&1)"; rc=$?
    if [ "$rc" -eq 0 ]; then t_record "$id" pass "ok: $*"; else t_record "$id" fail "rc=$rc: $* :: $out"; fi
    return 0
}

t_status() {
    if [ "$T_NFAIL" -gt 0 ]; then echo fail
    elif [ "$T_NPASS" -eq 0 ]; then echo skipped
    elif [ "$T_NSKIP" -gt 0 ]; then echo warn
    else echo pass; fi
}

t_finish() {
    local status id st detail first=true
    status="$(t_status)"
    if $T_JSON; then
        printf '{"script":"%s","gate":"%s","status":"%s","repo":"%s","checks":[' \
            "$(t_json_escape "$T_NAME")" "$T_GATE" "$status" "$(t_json_escape "$T_REPO")"
        while IFS="$(printf '\t')" read -r id st detail; do
            [ -n "$id" ] || continue
            $first || printf ','
            first=false
            printf '{"id":"%s","status":"%s","detail":"%s"}' "$(t_json_escape "$id")" "$st" "$(t_json_escape "$detail")"
        done <<EOF2
$T_ROWS
EOF2
        printf ']}\n'
    else
        printf '== %s (gate=%s) → %s ==\n' "$T_NAME" "$T_GATE" "$status"
        while IFS="$(printf '\t')" read -r id st detail; do
            [ -n "$id" ] || continue
            printf '  [%s] %s%s\n' "$(printf '%s' "$st" | tr '[:lower:]' '[:upper:]')" "$id" "${detail:+ — $detail}"
        done <<EOF3
$T_ROWS
EOF3
    fi
    if [ "$status" = fail ] && [ "$T_GATE" = block ]; then exit 1; fi
    exit 0
}
