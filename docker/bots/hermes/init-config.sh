#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Hermes Agent first-boot config materialisation.
# Merges AgentShroud-managed defaults from /app/config-defaults/hermes/ into
# /opt/data/ (Hermes' persistent data directory, backed by the hermes-config volume).
# This script is idempotent — it only writes files that do not already exist.

set -euo pipefail

# INIT_DEFAULTS_DIR / INIT_DATA_DIR are test-only path overrides (mirrors the
# SKILLGUARD_TEST_DEST_ROOT hook in sync-llm-settings.sh) so the wiring can be
# exercised against sandbox dirs without touching the container paths. Unset in
# production, where the baked/volume paths below are used.
DEFAULTS_DIR="${INIT_DEFAULTS_DIR:-/app/config-defaults/hermes}"
DATA_DIR="${INIT_DATA_DIR:-/opt/data}"

echo "[hermes-init] Checking config..."

# config.yaml — Hermes primary config file
# First-boot: seed from template if absent.
# Upgrade path: if present but missing telegram.extra.base_url (added in v1.1.0
# to route Telegram API calls through AgentShroud gateway:8080/telegram-api/),
# replace it so EgressFilter does not block api.telegram.org CONNECT requests.
if [ ! -f "${DATA_DIR}/config.yaml" ]; then
    cp "${DEFAULTS_DIR}/config.yaml.tmpl" "${DATA_DIR}/config.yaml"
    echo "[hermes-init] Seeded config.yaml from defaults"
elif ! grep -q "telegram-api/bot" "${DATA_DIR}/config.yaml" 2>/dev/null; then
    cp "${DEFAULTS_DIR}/config.yaml.tmpl" "${DATA_DIR}/config.yaml"
    echo "[hermes-init] Upgraded config.yaml: added telegram.extra.base_url for AgentShroud gateway routing"
elif grep -q 'claude-opus-4\.[0-9]' "${DATA_DIR}/config.yaml" 2>/dev/null; then
    # Migration: old template had "claude-opus-4.6" (dot) which Anthropic 404s with
    # "Did you mean claude-opus-4-6?". Rewrite in-place to the current valid name
    # from the template without destroying user-edited fields elsewhere.
    sed -i.bak -E 's|claude-opus-4\.[0-9]+|claude-opus-4-7|g' "${DATA_DIR}/config.yaml"
    rm -f "${DATA_DIR}/config.yaml.bak"
    echo "[hermes-init] Migrated config.yaml: invalid 'claude-opus-4.X' model name → claude-opus-4-7"
else
    echo "[hermes-init] config.yaml already exists and is current — skipping"
fi

# SOUL.md — bot identity file.
# Source of truth is the synced persona ~/.llm_settings/agents/hermes-soul.md
# (baked to ${DEFAULTS_DIR}/agents/hermes-soul.md by sync-llm-settings.sh). This is
# Hermes' OWN identity path — OpenClaw's persona (openclaw-identity.md) is NEVER
# loaded here. Fall back to the legacy ${DEFAULTS_DIR}/SOUL.md only if the synced
# file is absent (image built before the sync ran).
#
# Seeding model: first-boot seeds; on upgrade, re-seed when the IMAGE default changed
# since last seed (checksum stamp) so corrected personas — e.g. the connectivity-fix
# ssh-exec wrapper now in hermes-soul.md — propagate onto pre-existing volumes.
# Between image builds the checksum is stable, so live edits survive plain restarts.
_SOUL_SRC="${DEFAULTS_DIR}/agents/hermes-soul.md"
[ -f "${_SOUL_SRC}" ] || _SOUL_SRC="${DEFAULTS_DIR}/SOUL.md"
_SOUL_STAMP="${DATA_DIR}/.SOUL.md.seed-sha256"
_soul_sha="$(sha256sum "${_SOUL_SRC}" 2>/dev/null | awk '{print $1}')"
if [ ! -f "${DATA_DIR}/SOUL.md" ]; then
    cp "${_SOUL_SRC}" "${DATA_DIR}/SOUL.md"
    printf '%s' "${_soul_sha}" > "${_SOUL_STAMP}" 2>/dev/null || true
    echo "[hermes-init] Seeded SOUL.md from ${_SOUL_SRC##*/} (Hermes identity, first run)"
else
    _soul_prev=""
    [ -f "${_SOUL_STAMP}" ] && _soul_prev="$(cat "${_SOUL_STAMP}" 2>/dev/null || true)"
    if [ -n "${_soul_sha}" ] && [ "${_soul_sha}" != "${_soul_prev}" ]; then
        cp "${_SOUL_SRC}" "${DATA_DIR}/SOUL.md"
        printf '%s' "${_soul_sha}" > "${_SOUL_STAMP}" 2>/dev/null || true
        echo "[hermes-init] Re-seeded SOUL.md — synced persona changed since last seed (stale volume copy replaced)"
    else
        echo "[hermes-init] SOUL.md matches last-seeded synced persona — skipping"
    fi
fi

# Skills — install synced skills into Hermes' skill directory (/opt/data/skills/).
# Source of truth: ~/.llm_settings/skills/ → baked to ${DEFAULTS_DIR}/skills/ by
# sync-llm-settings.sh. Hermes reads skill artefacts from /opt/data/skills/ (see the
# skills/.hub reclaim in agentshroud-secrets.sh). Refresh managed skills on every boot
# so repo edits take effect after rebuild. This is Hermes' OWN skill path.
_SKILLS_SRC="${DEFAULTS_DIR}/skills"
_SKILLS_DEST="${DATA_DIR}/skills"
if [ -d "${_SKILLS_SRC}" ]; then
    mkdir -p "${_SKILLS_DEST}"
    for _skill_path in "${_SKILLS_SRC}"/*/; do
        [ -d "${_skill_path}" ] || continue
        _skill_name="$(basename "${_skill_path}")"
        rm -rf "${_SKILLS_DEST:?}/${_skill_name}"
        cp -r "${_skill_path}" "${_SKILLS_DEST}/${_skill_name}"
    done
    echo "[hermes-init] Installed synced skills into ${_SKILLS_DEST} ($(ls "${_SKILLS_DEST}" 2>/dev/null | wc -l | tr -d ' ') skill(s))"
else
    echo "[hermes-init] No synced skills dir at ${_SKILLS_SRC} — run scripts/sync-llm-settings.sh (skipping)"
fi

# Cron jobs — seed default job set on first boot
if [ ! -f "${DATA_DIR}/cron/jobs.yaml" ]; then
    mkdir -p "${DATA_DIR}/cron"
    cp "${DEFAULTS_DIR}/cron/jobs.yaml" "${DATA_DIR}/cron/jobs.yaml"
    echo "[hermes-init] Seeded cron/jobs.yaml from defaults"
else
    echo "[hermes-init] cron/jobs.yaml already exists — skipping"
fi

# ── Workspace seeding — competitive-intel files ────────────────────────────
# Seeds competitive-analysis.md and reports/ dir into /opt/data/workspace/
# on first boot. Idempotent via separate stamp.
_WS_STAMP="${DATA_DIR}/.hermes-workspace-seeded"
if [ ! -f "${_WS_STAMP}" ]; then
    mkdir -p "${DATA_DIR}/workspace/reports"
    if [ ! -f "${DATA_DIR}/workspace/competitive-analysis.md" ]; then
        cp "${DEFAULTS_DIR}/workspace/competitive-analysis.md" \
           "${DATA_DIR}/workspace/competitive-analysis.md"
        echo "[hermes-init] Seeded workspace/competitive-analysis.md"
    fi
    touch "${_WS_STAMP}"
    echo "[hermes-init] Workspace seeded"
else
    echo "[hermes-init] Workspace already seeded — skipping"
fi

# SCRUM-81: weekly Jira review script — refresh on EVERY boot (not stamp-gated) so
# code fixes ship on upgrade. It reads no persistent state; overwrite is safe.
if [ -f "${DEFAULTS_DIR}/workspace/jira_weekly_review.py" ]; then
    mkdir -p "${DATA_DIR}/workspace"
    cp "${DEFAULTS_DIR}/workspace/jira_weekly_review.py" \
       "${DATA_DIR}/workspace/jira_weekly_review.py"
    chmod 755 "${DATA_DIR}/workspace/jira_weekly_review.py" 2>/dev/null || true
    echo "[hermes-init] Seeded workspace/jira_weekly_review.py"
else
    echo "[hermes-init] WARN: jira_weekly_review.py not found in defaults — skipping"
fi

# ── Native cron jobs — idempotent seed on every boot ───────────────────────
# Uses `hermes cron create` (writes to Hermes's internal db) rather than
# the YAML file, which is not read natively by hermes-agent.
# Idempotent: _seed_cron deletes any existing job with the same name before
# creating, so re-seeds on upgrade never accumulate duplicates.
# (Prior stamp-file gating v1/v2/v3 caused triplication on each version bump
# because hermes cron create has no dedup — removed in favour of this approach.)

_seed_cron() {
    local _name="$1" _deliver="$2" _schedule="$3" _prompt="$4"
    # Remove all pre-existing jobs with this exact name, then create one canonical copy.
    hermes cron list 2>/dev/null \
      | awk -v name="$_name" '
            /^  [a-f0-9]{12} \[/ { id = $1; next }
            index($0, "Name:") && index($0, name) { print id }
          ' \
      | xargs -r -n1 hermes cron delete >/dev/null 2>&1 || true
    hermes cron create --name "$_name" --deliver "$_deliver" "$_schedule" "$_prompt" \
      2>/dev/null \
      && echo "[hermes-init] Seeded: $_name" \
      || echo "[hermes-init] WARN: seed failed: $_name"
}

echo "[hermes-init] Seeding native cron jobs (idempotent)..."

_seed_cron "AgentShroud Daily Check-in" "telegram" "0 14 * * *" \
    "Daily AgentShroud check-in from Hermes. Report current date/time, brief status of active tasks, and anything noteworthy from today. Under 150 words, send via Telegram to Isaiah."

_seed_cron "AgentShroud Weekly Summary" "telegram" "0 18 * * 5" \
    "Weekly summary from Hermes: key topics this week, skills learned or created, and what to focus on next week. Format concisely, deliver via Telegram."

_seed_cron "Weekly Kaizen Review" "telegram" "0 17 * * 5" \
    "Friday 5 PM weekly kaizen review (Hermes). What shipped this week? What caused friction? What process improvements would most help AgentShroud development? Format: SHIPPED / FRICTION / IMPROVE. Be specific and actionable."

_seed_cron "Monthly Chaos Engineering Drill" "telegram" "0 9 1 * *" \
    "First of month chaos engineering drill (Hermes). Simulate one failure scenario for AgentShroud involving Hermes: gateway crash, volume corruption, bot disconnect, or dependency outage. Describe failure mode, detection method, blast radius, and recovery procedure."

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_memory_journal_prompt='Nightly memory consolidation. Summarize today'"'"'s active projects, pending tasks, decisions made, and key facts for continuity. Append your summary to /opt/data/memories/journal-$(date +%Y-%m).md as a new dated section (use today'"'"'s date in YYYY-MM-DD format as the section heading). Create the file if it does not exist. Silent operation — no Telegram delivery.'
_seed_cron "Daily Memory Journal" "local" "55 23 * * *" "$_memory_journal_prompt"

_seed_cron "Weekly Hermes Stability Report" "telegram" "0 9 * * 1" \
    "Read /opt/data/logs/gateway-exit-diag.log (last 7 days entries) and /opt/data/.start-history (one epoch per line). Compute: total restarts this week, crashes per day as a sparkline (e.g. 0 0 2 0 1 0 3), longest stable window in hours, top 3 exit codes by frequency, any backoff pauses triggered (5-minute sleeps). Format as 'Hermes Weekly Stability — <date range>' in under 200 words. Send via Telegram. If log files do not exist, report that Hermes has been stable with no recorded exits this week."

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_competitive_landscape_prompt='Read /opt/data/workspace/competitive-analysis.md for research instructions. Execute the full 4-section competitive intelligence report. CRITICAL RULES: zero hallucinations — every company, product, and statistic must be verified against a live primary source. Exclude anything unverified. Every claim requires a working URL. Research competitors of AgentShroud (autonomous agent security tools — NOT the agents themselves). Verify GitHub star counts from live pages. Save report as /opt/data/workspace/reports/competitive-report-$(date +%Y-%m-%d).md (use today'"'"'s date in YYYY-MM-DD format). Append one-line summary to /opt/data/workspace/reports/trend-log.md. Do NOT send any email — the separate Hermes Competitive Intelligence Email cron job handles delivery. Silence is correct if nothing new is found; hallucination is a critical failure.'
_seed_cron "Hermes Competitive Landscape Update (AM/PM)" "local" "0 6,15 * * *" "$_competitive_landscape_prompt"

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_competitive_email_prompt='Read the most recent competitive-report-*.md from /opt/data/workspace/reports/ (prefer today'"'"'s date in YYYY-MM-DD format). If no report exists, use body '"'"'No significant changes detected today.'"'"' Render as a clean HTML email with inline CSS only (white bg #ffffff, text #111111, links #1a73e8, code bg #f6f8fa). To render: copy the cron-operations skill'"'"'s scripts/render_md_email.py to /opt/data/workspace/render_email.py, set its SRC/DST Path() constants (DST = /tmp/competitive-email.html), then run: python3 /opt/data/workspace/render_email.py. If the skill script is unavailable, write a pure-stdlib renderer to /opt/data/workspace/render_email.py and run it the same way. NEVER use execute_code, python3 -c, pip install, or uv pip install — all are blocked in cron mode. NEVER write_file a .py to /tmp/ — write renderer scripts to /opt/data/workspace/ only. The final .html output at /tmp/ is fine. Then run EXACTLY: /usr/local/bin/agentshroud-email-send.sh --html --subject '"'"'AgentShroud Hermes Competitive Intelligence'"'"' --body-file /tmp/competitive-email.html. The --html flag is mandatory — omitting it delivers raw markdown as plain text. Expect HTTP 200. On failure, report the full error via Telegram.'
_seed_cron "Hermes Competitive Intelligence Email (AM/PM)" "local" "0 7,16 * * *" "$_competitive_email_prompt"

# SCRUM-81: weekly Jira review — post a real authenticated comment on SCRUM-81
# every Sunday 09:00 so the Atlassian bot account never goes idle.
_seed_cron "jira-weekly-review" "local" "0 9 * * 0" \
    "Sunday 09:00 SCRUM-81 weekly Jira review. Run exactly: python3 /opt/data/workspace/jira_weekly_review.py — it fetches the Atlassian token/email/domain from the gateway op-proxy, builds a weekly summary (commits + SCRUM items advanced + staleness flag), and posts a real authenticated comment on SCRUM-81 via the Atlassian REST API to keep the account non-idle. NEVER use execute_code, python3 -c, pip install, or uv pip install — run the committed script only. Do NOT write your own script. Expect exit code 0. If it exits non-zero, report the full stderr via Telegram."

# Ensure memory journal write directory exists on the persistent volume
mkdir -p "${DATA_DIR}/memories"

echo "[hermes-init] Cron jobs seeded"

# ── Tirith trust: competitor + research-source reachability ────────────────
# The hermes URL scanner (tirith) flags `.ai`, `.security`, `.dev`, `.io`
# TLDs under its `lookalike_tld` rule and *blocks* the agent from probing
# them. The competitive cron's "verify-every-source" contract then can't
# reach known-safe sites and the report ends up filled with ⚠️ UNVERIFIED
# markers. Scope-only-to-rule trust entries narrow the bypass to
# lookalike_tld alone — every other tirith rule still fires.
# Idempotent: `tirith trust add` no-ops on already-trusted patterns.
if [ -x /opt/data/bin/tirith ]; then
    # trust.json is written by tirith as hermes user, but may be root-owned
    # if a previous boot ran the add as root. Ensure the hermes user can write it.
    _tirith_cfg="/opt/data/.config/tirith"
    _tirith_json="${_tirith_cfg}/trust.json"
    mkdir -p "${_tirith_cfg}" 2>/dev/null || true
    if [ -f "${_tirith_json}" ] && [ "$(stat -c '%u' "${_tirith_json}" 2>/dev/null || echo 0)" != "10000" ]; then
        chown 10000:10000 "${_tirith_json}" 2>/dev/null || true
    fi
    for _dom in \
        lakera.ai prompt.security calypsoai.com lasso.security \
        cequence.ai arcade.dev cyberark.com gravitee.io maxim.ai \
        adversa.ai o-mega.ai getmaxim.ai; do
        /opt/data/bin/tirith trust add "${_dom}" --rule lookalike_tld \
            >/dev/null 2>&1 || true
    done
    echo "[hermes-init] Tirith trust seeded for 12 competitor/research domains (rule=lookalike_tld)"

    # ── Defense-in-depth: internal gateway control-plane HTTP trust ──────────
    # The primary fix for the "[HIGH] Plain HTTP URL in execution context" flag
    # on gateway /ssh/exec calls is the agentshroud-ssh-exec.sh wrapper (the
    # plain-http URL never reaches the agent's command line). This block is a
    # NARROW belt-and-suspenders: if the agent ever hand-writes a raw curl to
    # the internal control-plane, trust the `gateway` host ONLY for the tirith
    # rule that fires on plain-HTTP-in-exec, so every OTHER rule (and every
    # OTHER host) is still scanned. http://gateway is the internal Docker
    # control-plane (compose network `internal: true`, not internet-exposed).
    #
    # tirith's rule id for this flag is discovered at runtime (its help/list
    # output) rather than hard-coded, so a tirith version bump that renames the
    # rule can't silently create a wrong-rule no-op that looks trusted but isn't.
    _http_rules="$(/opt/data/bin/tirith rules list 2>/dev/null \
        | awk '/[Hh][Tt][Tt][Pp]|execution context|unencrypted|insecure/ {print $1}' \
        | tr -d ':' | sort -u)"
    if [ -n "${_http_rules}" ]; then
        for _rule in ${_http_rules}; do
            for _gw in gateway "gateway:8080"; do
                /opt/data/bin/tirith trust add "${_gw}" --rule "${_rule}" \
                    >/dev/null 2>&1 || true
            done
        done
        echo "[hermes-init] Tirith trust seeded for internal gateway host (rules: ${_http_rules})"
    else
        echo "[hermes-init] Tirith plain-HTTP rule not enumerable — relying on agentshroud-ssh-exec.sh wrapper (primary fix)"
    fi
fi

# ── GitHub MCP server — wire on first boot if PAT is available ─────────────
# Requires github_pat Docker secret (stored in 1Password "Agent Shroud Bot Credentials").
# If the secret is absent or empty, this step is skipped silently.
_MCP_STAMP="${DATA_DIR}/.hermes-mcp-github-added"
if [ ! -f "${_MCP_STAMP}" ]; then
    if [ -f "/run/secrets/github_pat" ] && [ -s "/run/secrets/github_pat" ]; then
        _github_pat="$(cat /run/secrets/github_pat)"
        if hermes mcp list 2>/dev/null | grep -q "github"; then
            echo "[hermes-init] GitHub MCP server already configured — skipping"
            touch "${_MCP_STAMP}"
        else
            echo "[hermes-init] Adding GitHub MCP server..."
            HOME="${DATA_DIR}" hermes mcp add github \
                --command npx \
                --args -y @modelcontextprotocol/server-github \
                --env "GITHUB_PERSONAL_ACCESS_TOKEN=${_github_pat}" \
                2>/dev/null \
                && touch "${_MCP_STAMP}" \
                && echo "[hermes-init] GitHub MCP server added" \
                || echo "[hermes-init] WARN: GitHub MCP add failed (will retry on next boot)"
        fi
    else
        echo "[hermes-init] github_pat secret absent — skipping GitHub MCP setup"
        echo "[hermes-init]   To enable: store github_pat in 1Password 'Agent Shroud Bot Credentials' vault"
        echo "[hermes-init]   and run: asb rebuild full"
    fi
else
    echo "[hermes-init] GitHub MCP already configured — skipping"
fi

# ── Synced MCP servers — register each from mcp/servers.json (idempotent) ───
# Source of truth: ~/.llm_settings/mcp/servers.json → baked to
# ${DEFAULTS_DIR}/mcp/servers.json by sync-llm-settings.sh. Read the server
# name + url from that file (NOT hardcoded) and register each enabled server via
# Hermes' native `hermes mcp add`. Extends the github-MCP idempotent pattern above
# to the declarative server list. No secrets are written here — the servers.json
# comment notes tokens are injected at deploy time; agentshroud-gateway needs none
# (internal Docker control plane). HTTP transport is used because servers.json
# declares "type":"http". Idempotent: skip any server already in `hermes mcp list`.
_MCP_SERVERS_JSON="${DEFAULTS_DIR}/mcp/servers.json"
if [ -f "${_MCP_SERVERS_JSON}" ]; then
    _mcp_rows="$(python3 -c "
import json, sys
try:
    cfg = json.load(open('${_MCP_SERVERS_JSON}'))
except Exception as e:
    sys.stderr.write('mcp parse error: %s\n' % e); sys.exit(0)
for name, s in (cfg.get('servers') or {}).items():
    if not isinstance(s, dict) or s.get('enabled') is False:
        continue
    url = s.get('url') or ''
    if not url:
        continue
    print('%s\t%s\t%s' % (name, s.get('type') or 'http', url))
" 2>/dev/null)"
    if [ -n "${_mcp_rows}" ]; then
        _mcp_existing="$(HOME="${DATA_DIR}" hermes mcp list 2>/dev/null || true)"
        printf '%s\n' "${_mcp_rows}" | while IFS="$(printf '\t')" read -r _name _type _url; do
            [ -n "${_name}" ] && [ -n "${_url}" ] || continue
            if printf '%s' "${_mcp_existing}" | grep -qw "${_name}"; then
                echo "[hermes-init] MCP server '${_name}' already configured — skipping"
                continue
            fi
            # HTTP-transport flag names vary across Hermes releases; try the known
            # forms in order. Non-fatal on failure (retries next boot).
            if HOME="${DATA_DIR}" hermes mcp add "${_name}" --transport http --url "${_url}" >/dev/null 2>&1 \
               || HOME="${DATA_DIR}" hermes mcp add "${_name}" --type http --url "${_url}" >/dev/null 2>&1 \
               || HOME="${DATA_DIR}" hermes mcp add "${_name}" --url "${_url}" >/dev/null 2>&1; then
                echo "[hermes-init] Registered MCP server '${_name}' (${_type}) → ${_url}"
            else
                echo "[hermes-init] WARN: could not add MCP server '${_name}' (will retry on next boot)"
            fi
        done
    else
        echo "[hermes-init] No enabled MCP servers in ${_MCP_SERVERS_JSON} — skipping"
    fi
else
    echo "[hermes-init] No synced mcp/servers.json — run scripts/sync-llm-settings.sh (skipping)"
fi

echo "[hermes-init] Config init complete"
