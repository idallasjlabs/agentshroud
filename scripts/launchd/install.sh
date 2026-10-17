#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/launchd/install.sh — install this host's AgentShroud schedulers from
# the repo. Idempotent: re-running with nothing changed changes nothing.
#
# Why it exists (2026-10-17 drift audit): nothing tracked installed either
# host's scheduler, so both drifted from main. Prod's Sunday job was loaded
# from a stale backup plist with the same Label and no SUNDAY_UPGRADE_AUTON=1,
# which would have stalled the unattended run on permission prompts. Dev's
# crontab was hand-typed. Dev's colima plist had per-account log paths while
# the repo copy had regressed to /tmp.
#
# The account picks the role (`whoami`):
#   ijefferson.admin  prod — copy com.agentshroud.{sunday-upgrade,colima-
#                     autostart}.plist into ~/Library/LaunchAgents, archive any
#                     other file there carrying the same Label, and
#                     bootout/bootstrap a job only when its file changed or it
#                     is not loaded.
#   agentshroud-bot   dev  — this account never gets a GUI login, so launchd
#                     never bootstraps its agents (see the colima plist). Its
#                     schedule is cron: a managed block for the Colima health
#                     check and the Sunday run + retries replaces any hand-typed
#                     copies of those lines; every other crontab line is kept.
#                     The colima plist is still placed for the GUI-login case.
#   anyone else       refused, nothing changed.
#
# Plists are written with prod's home; the account's $HOME is substituted on
# install (a no-op on prod, so prod's copy stays byte-identical to the repo).
#
# Usage: scripts/launchd/install.sh [--dry-run]
#   LAUNCHD_INSTALL_USER overrides `whoami` (tests only).

set -euo pipefail

SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROD_HOME_LITERAL="/Users/ijefferson.admin"
AGENTS_DIR="$HOME/Library/LaunchAgents"
ARCHIVE_DIR="$HOME/Library/LaunchAgents-archive"
REPO_DIR="$HOME/Development/agentshroud"
CRON_BEGIN="# BEGIN agentshroud managed (scripts/launchd/install.sh) — edit there, not here"
CRON_END="# END agentshroud managed"

DRY_RUN=0
case "${1:-}" in
  --dry-run) DRY_RUN=1 ;;
  "") ;;
  -h|--help) sed -n '6,33p' "${BASH_SOURCE[0]}"; exit 0 ;;
  *) echo "install.sh: unknown argument: $1" >&2; exit 2 ;;
esac

say() { echo "[launchd-install] $*"; }
act() {
  if [ "$DRY_RUN" -eq 1 ]; then say "[dry-run] $*"; else "$@"; fi
}

plist_label() {
  /usr/libexec/PlistBuddy -c 'Print :Label' "$1" 2>/dev/null || true
}

# install_agent <plist name> <load: 1|0>
install_agent() {
  local name="$1" load="$2" src dest label rendered changed=0 f
  src="$SRC_DIR/$name"
  dest="$AGENTS_DIR/$name"
  label="$(plist_label "$src")"
  [ -n "$label" ] || { echo "install.sh: no Label in $src" >&2; exit 1; }

  act mkdir -p "$AGENTS_DIR"
  # Any OTHER file carrying this Label is a stale copy launchd may load instead
  # of the canonical one. Archive it rather than delete it.
  for f in "$AGENTS_DIR"/*; do
    [ -f "$f" ] && [ "$f" != "$dest" ] || continue
    [ "$(plist_label "$f")" = "$label" ] || continue
    act mkdir -p "$ARCHIVE_DIR"
    act mv "$f" "$ARCHIVE_DIR/"
    say "archived stale copy of ${label}: $(basename "$f")"
    changed=1
  done

  rendered="$(mktemp)"
  sed "s|${PROD_HOME_LITERAL}|${HOME}|g" "$src" > "$rendered"
  if cmp -s "$rendered" "$dest"; then
    say "${name}: up to date"
  else
    act cp "$rendered" "$dest"
    act chmod 644 "$dest"
    say "${name}: installed"
    changed=1
  fi
  rm -f "$rendered"

  [ "$load" -eq 1 ] || return 0
  local domain
  domain="gui/$(id -u)"
  if [ "$changed" -eq 0 ] && launchctl print "$domain/$label" >/dev/null 2>&1; then
    say "${label}: loaded, unchanged"
    return 0
  fi
  act launchctl bootout "$domain/$label" 2>/dev/null || true
  act launchctl bootstrap "$domain" "$dest"
  say "${label}: (re)loaded from $dest"
}

install_dev_crontab() {
  local current block new
  current="$(crontab -l 2>/dev/null || true)"
  block="$(cat <<EOF
$CRON_BEGIN
PATH=/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
*/5 * * * * $REPO_DIR/docker/scripts/colima-health-check.sh >> $HOME/Library/Logs/agentshroud-health.log 2>&1
@reboot $REPO_DIR/docker/scripts/colima-health-check.sh >> $HOME/Library/Logs/agentshroud-health.log 2>&1
0 3 * * 0 SUNDAY_UPGRADE_AUTON=1 /bin/bash $REPO_DIR/scripts/sunday-upgrade.sh >> $HOME/Library/Logs/sunday-upgrade.log 2>&1
0 5,8,11,14 * * 0 SUNDAY_UPGRADE_AUTON=1 /bin/bash $REPO_DIR/scripts/sunday-upgrade.sh >> $HOME/Library/Logs/sunday-upgrade.log 2>&1
$CRON_END
EOF
)"
  # Drop the previous managed block and any hand-typed copy of a managed job
  # (left in place, it would fire twice); keep every other line as it was.
  new="$(printf '%s\n' "$current" \
    | awk -v b="$CRON_BEGIN" -v e="$CRON_END" '
        $0 == b { skip = 1; next }
        $0 == e { skip = 0; next }
        skip { next }
        /docker\/scripts\/colima-health-check\.sh/ { next }
        /scripts\/sunday-upgrade\.sh/ { next }
        { print }' \
    | sed -e :a -e '/^\n*$/{$d;N;ba' -e '}')"
  if [ -n "$new" ]; then new="$new"$'\n'"$block"; else new="$block"; fi
  if [ "$new" = "$current" ]; then
    say "crontab: up to date"
    return 0
  fi
  if [ "$DRY_RUN" -eq 1 ]; then
    say "[dry-run] would install crontab:"
    printf '%s\n' "$new"
    return 0
  fi
  printf '%s\n' "$new" | crontab -
  say "crontab: managed block installed"
}

user="${LAUNCHD_INSTALL_USER:-$(whoami)}"
case "$user" in
  ijefferson.admin)
    say "role: prod ($user)"
    install_agent com.agentshroud.sunday-upgrade.plist 1
    install_agent com.agentshroud.colima-autostart.plist 1
    ;;
  agentshroud-bot)
    say "role: dev ($user)"
    install_agent com.agentshroud.colima-autostart.plist 0
    install_dev_crontab
    ;;
  *)
    echo "install.sh: unknown account '$user' — expected ijefferson.admin (prod) or agentshroud-bot (dev); nothing changed" >&2
    exit 2
    ;;
esac
say "done"
