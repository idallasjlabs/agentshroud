#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# update-conduit-push.sh — install Hermes's conduit_push plugin at the commit
# pinned in docker/versions.env, then prove it.
#
# conduit_push (kaishi00/hermes-conduit-notifier) lives in the hermes-config
# volume at /opt/data/plugins/conduit_push. It was hand-installed unpinned on
# 2026-10-16 and nothing tracked it. Owner policy (2026-10-22): install only the
# pinned commit; moving the pin is a reviewed PR (hook surface + diff), never a
# floating `hermes plugins update`. Upstream has no tags, so the pin is a full
# 40-char SHA plus the plugin.yaml version expected at that SHA.
#
# Proves the outcome (CLAUDE.md §0.0), each read back from Hermes itself:
#   * `hermes plugins show conduit_push` reports the pinned version, enabled
#   * .install-metadata.json records the pinned revision
#   * Hermes is healthy again after the restart that loads the new code
#   * Pulse is off (absent DB, or settings.enabled false) — owner has not
#     opted in, so Pulse on is a regression
# Any failed proof reinstalls the previous revision and exits 1.
#
# Exit: 0 upgraded | 25 already at the pin (nothing to do) | 1 failed (rolled
# back) | 2 bad pin or Hermes unreachable (nothing touched)
#
# Usage: scripts/update-conduit-push.sh
# Env:   AGENTSHROUD_HERMES_CONTAINER (default agentshroud-hermes-v2)
set -uo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VERSIONS_FILE="${CONDUIT_PUSH_VERSIONS_FILE:-$REPO_DIR/docker/versions.env}"
C="${AGENTSHROUD_HERMES_CONTAINER:-agentshroud-hermes-v2}"
HERMES=/opt/hermes/bin/hermes
PY=/opt/hermes/.venv/bin/python3
HEALTH_TIMEOUT="${CONDUIT_PUSH_HEALTH_TIMEOUT:-300}"
POLL="${CONDUIT_PUSH_POLL:-5}"

say() { echo "conduit_push: $*"; }
die() { echo "conduit_push: $*" >&2; exit "${2:-1}"; }

pin() { sed -n "s/^$1=//p" "$VERSIONS_FILE" | tail -1; }
REPO="$(pin CONDUIT_PUSH_REPO)"
REF="$(pin CONDUIT_PUSH_REF)"
WANT="$(pin CONDUIT_PUSH_VERSION)"
[[ "$REF" =~ ^[0-9a-f]{40}$ ]] || die "CONDUIT_PUSH_REF must be a full lowercase 40-char commit SHA, got '${REF}'" 2
[[ "$REPO" =~ ^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$ ]] || die "CONDUIT_PUSH_REPO must be owner/repo, got '${REPO}'" 2
[[ "$WANT" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || die "CONDUIT_PUSH_VERSION must be x.y.z, got '${WANT}'" 2

installed_version() {
  docker exec -u hermes "$C" "$HERMES" plugins show conduit_push 2>/dev/null \
    | sed -n 's/^conduit_push v\([0-9.]*\).*/\1/p' | head -1
}
installed_status() {
  docker exec -u hermes "$C" "$HERMES" plugins show conduit_push 2>/dev/null \
    | sed -n 's/^Status: *//p' | head -1
}
installed_ref() {
  docker exec "$C" "$PY" -c 'import json; print(json.load(open("/opt/data/plugins/.install-metadata.json"))["conduit_push"]["revision"])' 2>/dev/null
}
pulse_state() {
  docker exec "$C" "$PY" -c '
import json, os, sqlite3
p = "/opt/data/conduit-pulse.db"
if not os.path.exists(p):
    print("absent")
else:
    row = sqlite3.connect(p).execute("SELECT value_json FROM settings WHERE key=?", ("enabled",)).fetchone()
    print("true" if row and json.loads(row[0]) else "false")' 2>/dev/null
}
install_ref() {
  docker exec "$C" "$HERMES" plugins install --force --ref "$1" --enable "$REPO" >&2
}
restart_and_wait() {
  docker restart "$C" >/dev/null || return 1
  local waited=0 h
  while [ "$waited" -le "$HEALTH_TIMEOUT" ]; do
    h="$(docker inspect --format '{{.State.Health.Status}}' "$C" 2>/dev/null)"
    [ "$h" = "healthy" ] && return 0
    sleep "$POLL"; waited=$((waited + POLL + 1))
  done
  return 1
}

BEFORE_V="$(installed_version)"
BEFORE_REF="$(installed_ref)"
[ -n "$BEFORE_V" ] || die "cannot read the installed plugin from $C (is Hermes running?)" 2

if [ "$BEFORE_V" = "$WANT" ] && [ "$BEFORE_REF" = "$REF" ]; then
  say "ALREADY_AT_PIN $WANT (${REF:0:10}) — nothing installed, Hermes not restarted"
  exit 25
fi

rollback() {
  echo "conduit_push: $1 — rolling back to ${BEFORE_V} (${BEFORE_REF:0:10})" >&2
  if [[ "$BEFORE_REF" =~ ^[0-9a-f]{40}$ ]] && install_ref "$BEFORE_REF" && restart_and_wait; then
    echo "conduit_push: rolled back to $(installed_version) ($(installed_ref | cut -c1-10))" >&2
  else
    echo "conduit_push: ROLLBACK FAILED — Hermes needs a manual look" >&2
  fi
  exit 1
}

say "installing $REPO@${REF:0:10} (expect $WANT) over $BEFORE_V (${BEFORE_REF:0:10})"
install_ref "$REF" || rollback "install failed"
restart_and_wait || rollback "Hermes not healthy within ${HEALTH_TIMEOUT}s of restart"

AFTER_V="$(installed_version)"
AFTER_REF="$(installed_ref)"
AFTER_STATUS="$(installed_status)"
[ "$AFTER_V" = "$WANT" ] || rollback "installed version is '${AFTER_V}', expected $WANT"
[ "$AFTER_REF" = "$REF" ] || rollback "installed revision is '${AFTER_REF}', expected $REF"
[ "$AFTER_STATUS" = "enabled" ] || rollback "plugin status is '${AFTER_STATUS}', expected enabled"

PULSE="$(pulse_state)"
case "$PULSE" in
  absent|false) ;;
  *) rollback "Pulse is enabled (state '${PULSE}') — the owner has not opted in" ;;
esac

say "UPGRADED ${BEFORE_V} (${BEFORE_REF:0:10}) -> ${AFTER_V} (${AFTER_REF:0:10}); status ${AFTER_STATUS}; Hermes healthy; Pulse: off (${PULSE})"
