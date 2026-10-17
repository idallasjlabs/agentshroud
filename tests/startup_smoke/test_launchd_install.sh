#!/usr/bin/env bash
# ok() always succeeds, so `cond && ok ... || bad ...` is a true if/else here.
# shellcheck disable=SC2015
# Behavioral test for scripts/launchd/install.sh — the one tracked way the
# Sunday-upgrade and Colima schedulers reach a host.
#
# Why it exists (2026-10-17 drift audit): nothing in the repo installed either
# host's scheduler, so both drifted. Prod's Sunday job was loaded from a stale
# backup plist (same Label, no SUNDAY_UPGRADE_AUTON=1 — it would have stalled
# on permission prompts); dev's crontab was hand-typed; dev's colima plist had
# per-account log paths while the repo's had regressed to /tmp, which prod's
# job creates first as another user so dev's job could not spawn.
#
# Runs the real installer against a scratch HOME with fake launchctl/crontab.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INSTALL="$REPO_ROOT/scripts/launchd/install.sh"
COLIMA_SRC="$REPO_ROOT/scripts/launchd/com.agentshroud.colima-autostart.plist"
SUNDAY_SRC="$REPO_ROOT/scripts/launchd/com.agentshroud.sunday-upgrade.plist"
fail=0
ok()  { echo "  OK : $*"; }
bad() { echo "  FAIL: $*" >&2; fail=1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Fake launchctl: loaded labels live in $FAKE_STATE/loaded, every call is logged.
# Fake crontab: the table lives in $FAKE_STATE/crontab.
mkdir -p "$TMP/bin"
cat > "$TMP/bin/launchctl" <<'EOF'
#!/usr/bin/env bash
echo "$*" >> "$FAKE_STATE/launchctl.log"
loaded="$FAKE_STATE/loaded"; touch "$loaded"
case "$1" in
  print)     grep -qxF "${2##*/}" "$loaded" ;;
  bootout)   grep -vxF "${2##*/}" "$loaded" > "$loaded.n" || true; mv "$loaded.n" "$loaded" ;;
  bootstrap) /usr/libexec/PlistBuddy -c 'Print :Label' "$3" >> "$loaded" ;;
  *)         exit 0 ;;
esac
EOF
cat > "$TMP/bin/crontab" <<'EOF'
#!/usr/bin/env bash
t="$FAKE_STATE/crontab"
case "$1" in
  -l) [ -f "$t" ] && cat "$t" || { echo "crontab: no crontab for user" >&2; exit 1; } ;;
  -)  cat > "$t" ;;
  *)  cp "$1" "$t" ;;
esac
EOF
chmod +x "$TMP/bin/launchctl" "$TMP/bin/crontab"

run_install() {  # <home> <user> [args...]
  local home="$1" user="$2"; shift 2
  FAKE_STATE="$home/.state" HOME="$home" PATH="$TMP/bin:/usr/bin:/bin" \
    LAUNCHD_INSTALL_USER="$user" bash "$INSTALL" "$@"
}

echo ""
echo "── repo plist ──"
if grep -q '/tmp/colima-autostart' "$COLIMA_SRC"; then
  bad "colima plist still logs to /tmp (prod's job creates those files first as another user)"
elif grep -q '<string>/Users/ijefferson.admin/Library/Logs/colima-autostart.log</string>' "$COLIMA_SRC"; then
  ok "colima plist logs under the account's own ~/Library/Logs"
else
  bad "colima plist log path not under ~/Library/Logs"
fi
if grep -q 'no --cpu/--memory/--disk here' "$COLIMA_SRC"; then
  ok "colima plist keeps the no-sizing-flags note"
else
  bad "colima plist lost the no-sizing-flags note"
fi

echo ""
echo "── dev (agentshroud-bot): crontab block ──"
DH="$TMP/dev"; mkdir -p "$DH/.state" "$DH/Library/LaunchAgents"
# The hand-installed table found on dev 2026-10-17, plus an unrelated line.
cat > "$DH/.state/crontab" <<'EOF'
PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
*/5 * * * * /Users/agentshroud-bot/Development/agentshroud/docker/scripts/colima-health-check.sh >> /Users/agentshroud-bot/Library/Logs/agentshroud-health.log 2>&1
0 3 * * 0 SUNDAY_UPGRADE_AUTON=1 /bin/bash /Users/agentshroud-bot/Development/agentshroud/scripts/sunday-upgrade.sh >> /Users/agentshroud-bot/Library/Logs/sunday-upgrade.log 2>&1
@reboot /Users/agentshroud-bot/Development/agentshroud/docker/scripts/colima-health-check.sh >> /Users/agentshroud-bot/Library/Logs/agentshroud-health.log 2>&1
0 5,8,11,14 * * 0 SUNDAY_UPGRADE_AUTON=1 /bin/bash /Users/agentshroud-bot/Development/agentshroud/scripts/sunday-upgrade.sh >> /Users/agentshroud-bot/Library/Logs/sunday-upgrade.log 2>&1
17 4 * * * /usr/bin/true # unrelated job
EOF
run_install "$DH" agentshroud-bot >"$TMP/dev1.log" 2>&1 || bad "dev install exited non-zero: $(cat "$TMP/dev1.log")"
CT="$DH/.state/crontab"
n_health="$(grep -c 'colima-health-check.sh' "$CT" || true)"
n_sunday="$(grep -c 'scripts/sunday-upgrade.sh' "$CT" || true)"
[ "$n_health" -eq 2 ] && ok "health check scheduled exactly twice (*/5 and @reboot)" || bad "health-check lines: $n_health"
[ "$n_sunday" -eq 2 ] && ok "Sunday upgrade scheduled exactly twice (03:00 and the retries)" || bad "sunday lines: $n_sunday"
grep -q '^0 3 \* \* 0 SUNDAY_UPGRADE_AUTON=1 ' "$CT" && grep -q '^0 5,8,11,14 \* \* 0 SUNDAY_UPGRADE_AUTON=1 ' "$CT" \
  && ok "03:00 run and 05/08/11/14 retries keep SUNDAY_UPGRADE_AUTON=1" || bad "Sunday schedule wrong: $(grep sunday "$CT")"
grep -q "$DH/Development/agentshroud/scripts/sunday-upgrade.sh" "$CT" \
  && ok "paths come from the installing account's HOME" || bad "paths not under $DH"
grep -q 'unrelated job' "$CT" && ok "unrelated crontab lines are preserved" || bad "unrelated line dropped"
[ "$(grep -c '^# BEGIN agentshroud' "$CT")" -eq 1 ] && ok "one managed block" || bad "managed block count wrong"
cp "$CT" "$TMP/ct.first"
run_install "$DH" agentshroud-bot >"$TMP/dev2.log" 2>&1 || bad "second dev install exited non-zero"
cmp -s "$CT" "$TMP/ct.first" && ok "second run leaves the crontab byte-identical (idempotent)" || bad "second run changed the crontab: $(diff "$TMP/ct.first" "$CT")"

echo ""
echo "── dev: colima plist ──"
DP="$DH/Library/LaunchAgents/com.agentshroud.colima-autostart.plist"
if [ -f "$DP" ] && grep -q "<string>$DH/Library/Logs/colima-autostart.log</string>" "$DP" && ! grep -q 'ijefferson.admin' "$DP"; then
  ok "installed with this account's own log paths"
else
  bad "dev colima plist missing or carries another account's paths"
fi
[ ! -f "$DH/Library/LaunchAgents/com.agentshroud.sunday-upgrade.plist" ] \
  && ok "no Sunday LaunchAgent on dev (cron owns dev's schedule)" || bad "Sunday plist installed on dev"

echo ""
echo "── prod (ijefferson.admin): plists ──"
PH="$TMP/prod"; mkdir -p "$PH/.state" "$PH/Library/LaunchAgents"
# The stale backup prod was actually loaded from: same Label, no AUTON.
sed '/SUNDAY_UPGRADE_AUTON/,+1d' "$SUNDAY_SRC" > "$PH/Library/LaunchAgents/com.agentshroud.sunday-upgrade-20260906-0645.plist"
echo "com.agentshroud.sunday-upgrade" > "$PH/.state/loaded"
run_install "$PH" ijefferson.admin >"$TMP/prod1.log" 2>&1 || bad "prod install exited non-zero: $(cat "$TMP/prod1.log")"
PS="$PH/Library/LaunchAgents/com.agentshroud.sunday-upgrade.plist"
if [ -f "$PS" ] && cmp -s "$PS" <(sed "s|/Users/ijefferson.admin|$PH|g" "$SUNDAY_SRC"); then
  ok "Sunday plist installed from the repo at the canonical path"
else
  bad "Sunday plist missing or differs from the repo"
fi
[ ! -e "$PH/Library/LaunchAgents/com.agentshroud.sunday-upgrade-20260906-0645.plist" ] \
  && [ -f "$PH/Library/LaunchAgents-archive/com.agentshroud.sunday-upgrade-20260906-0645.plist" ] \
  && ok "same-Label stale copy moved to ~/Library/LaunchAgents-archive" || bad "stale copy not archived"
grep -q "bootstrap gui/[0-9]* $PS" "$PH/.state/launchctl.log" \
  && ok "bootstrapped from the canonical path" || bad "no bootstrap of $PS: $(cat "$PH/.state/launchctl.log")"
grep -qx 'com.agentshroud.colima-autostart' "$PH/.state/loaded" \
  && ok "colima-autostart loaded too" || bad "colima-autostart not loaded"
[ ! -f "$PH/.state/crontab" ] && ok "prod crontab untouched" || bad "installer wrote a crontab on prod"
: > "$PH/.state/launchctl.log"
run_install "$PH" ijefferson.admin >"$TMP/prod2.log" 2>&1 || bad "second prod install exited non-zero"
if grep -qE '^(bootout|bootstrap)' "$PH/.state/launchctl.log"; then
  bad "second run reloaded unchanged, already-loaded jobs: $(cat "$PH/.state/launchctl.log")"
else
  ok "second run does not reload unchanged jobs (idempotent)"
fi

echo ""
echo "── unknown account ──"
UH="$TMP/other"; mkdir -p "$UH/.state"
if run_install "$UH" someone-else >"$TMP/other.log" 2>&1; then
  bad "installed for an unknown account"
else
  [ ! -d "$UH/Library" ] && [ ! -f "$UH/.state/crontab" ] && ok "refuses an unknown account and changes nothing" || bad "changed state for an unknown account"
fi

echo ""
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASSED"; else echo "SOME CHECKS FAILED" >&2; fi
exit "$fail"
