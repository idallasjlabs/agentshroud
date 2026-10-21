#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# sql-fixtures.sh — SQL lint, fixtures and scan-cost checks (i-data-ai-ot gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="sql-fixtures"; T_SUMMARY="SQL lint, fixtures and scan-cost checks (i-data-ai-ot gate)"
T_OPTIONS="Fixtures: tests/sql/*.sql run with duckdb when installed. Cost guard: SELECT without WHERE/LIMIT/partition filter fails."
t_parse "" "$@"; t_init
files="$(git ls-files '*.sql' 2>/dev/null | /usr/bin/grep -v '^tests/sql/' )"
if [ -z "$files" ]; then
    t_skip sql "no SQL files tracked"
else
    bad=""
    for f in $files; do
        if /usr/bin/grep -qi 'select' "$f" && ! /usr/bin/grep -qiE 'where|limit|partition|dt *=|year *=' "$f"; then bad="$bad $f"; fi
        if /usr/bin/grep -qiE 'select +\*' "$f"; then bad="$bad $f(select*)"; fi
    done
    [ -z "$bad" ] && t_record scan-cost pass "all SQL has a filter/LIMIT and no SELECT *" || t_record scan-cost fail "unbounded or SELECT * queries:$bad"
    if t_have sqlfluff sql-lint; then t_run sql-lint "sqlfluff lint $(echo $files | tr '\n' ' ')"; fi
    fx="$(git ls-files 'tests/sql/*.sql' 2>/dev/null)"
    if [ -n "$fx" ]; then
        if t_have duckdb sql-fixtures; then for f in $fx; do t_run "fixture-$(basename "$f" .sql)" "duckdb :memory: < $f"; done; fi
    else
        t_skip sql-fixtures "no fixtures under tests/sql/"
    fi
fi
t_finish
