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

# ── First-boot gateway auto-start ───────────────────────────────────────────
# hermes_cli.container_boot (vendor, /etc/cont-init.d/02-reconcile-profiles)
# only auto-starts a profile's s6 service when its LAST RECORDED state was
# `running` — see that script's own header comment. A genuinely first-ever
# boot has no recorded state, so the vendor reconciler REGISTERS the
# `gateway-default` s6 service slot (creates /run/service/gateway-default/)
# but leaves its `down` sentinel file in place, and never calls `s6-svc -u`.
# The container then reports Docker-healthy (the dashboard/API-server s6
# services DO start) while the actual Telegram/Discord gateway process never
# runs at all — confirmed live on a first-time install (marvin, 2026-07-19):
# 43+ hours "Up", RestartCount=0, zero bytes ever written to
# /opt/data/logs/gateways/default/current. Silent, and easy to miss because
# nothing crashes or restarts — `docker ps` just shows "unhealthy" forever.
# Idempotent: on every boot AFTER the first, the vendor reconciler has
# already removed `down` (prior_state=running), so this is a no-op.
_GW_DOWN_FILE="/run/service/gateway-default/down"
if [ -f "${_GW_DOWN_FILE}" ]; then
    echo "[hermes-init] gateway-default registered but never started (first boot) — starting it"
    rm -f "${_GW_DOWN_FILE}"
    s6-svc -u /run/service/gateway-default 2>/dev/null \
        && echo "[hermes-init] ✓ gateway-default started" \
        || echo "[hermes-init] WARN: could not start gateway-default (will retry next boot)"
fi

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
#
# Ownership-tolerant write (fixes the "cp: cannot create '/opt/data/SOUL.md':
# Permission denied" trap): the volume may hold a STALE SOUL.md owned by a foreign
# uid (e.g. 14664 from an old host `docker cp`). init runs as the non-root hermes
# user, so a plain `cp` over that file fails (cp opens the existing inode for
# writing → EACCES) even though the target file exists. Since ${DATA_DIR} itself is
# hermes-owned, we can DELETE the foreign file (directory write permission) and
# create a fresh hermes-owned copy. We stage into a temp file in the SAME dir first,
# then rm + mv so a crash mid-write never leaves a truncated SOUL.md.
_SOUL_SRC="${DEFAULTS_DIR}/agents/hermes-soul.md"
[ -f "${_SOUL_SRC}" ] || _SOUL_SRC="${DEFAULTS_DIR}/SOUL.md"
_SOUL_DEST="${DATA_DIR}/SOUL.md"
_SOUL_STAMP="${DATA_DIR}/.SOUL.md.seed-sha256"
_soul_sha="$(sha256sum "${_SOUL_SRC}" 2>/dev/null | awk '{print $1}')"

# _write_soul: atomically place ${_SOUL_SRC} at ${_SOUL_DEST}, tolerant of a
# foreign-owned pre-existing file. Returns 0 on success.
_write_soul() {
    _tmp="${DATA_DIR}/.SOUL.md.tmp.$$"
    if cp "${_SOUL_SRC}" "${_tmp}" 2>/dev/null; then
        rm -f "${_SOUL_DEST}" 2>/dev/null || true
        if mv -f "${_tmp}" "${_SOUL_DEST}" 2>/dev/null; then
            return 0
        fi
        rm -f "${_tmp}" 2>/dev/null || true
    fi
    # Last resort: try a plain in-place cp (works if we DO own the file).
    cp "${_SOUL_SRC}" "${_SOUL_DEST}" 2>/dev/null
}

if [ ! -f "${_SOUL_DEST}" ]; then
    if _write_soul; then
        printf '%s' "${_soul_sha}" > "${_SOUL_STAMP}" 2>/dev/null || true
        echo "[hermes-init] Seeded SOUL.md from ${_SOUL_SRC##*/} (Hermes identity, first run)"
    else
        echo "[hermes-init] WARN: could not seed SOUL.md (permission) — will retry next boot"
    fi
else
    _soul_prev=""
    [ -f "${_SOUL_STAMP}" ] && _soul_prev="$(cat "${_SOUL_STAMP}" 2>/dev/null || true)"
    # Also re-seed if the deployed file's content already drifted from the synced
    # persona (covers the stale foreign-owned file whose stamp was never written).
    _soul_dest_sha="$(sha256sum "${_SOUL_DEST}" 2>/dev/null | awk '{print $1}')"
    if [ -n "${_soul_sha}" ] && { [ "${_soul_sha}" != "${_soul_prev}" ] || [ "${_soul_sha}" != "${_soul_dest_sha}" ]; }; then
        if _write_soul; then
            printf '%s' "${_soul_sha}" > "${_SOUL_STAMP}" 2>/dev/null || true
            echo "[hermes-init] Re-seeded SOUL.md — synced persona changed / stale volume copy replaced"
        else
            echo "[hermes-init] WARN: could not re-seed SOUL.md (permission) — will retry next boot"
        fi
    else
        echo "[hermes-init] SOUL.md matches synced persona — skipping"
    fi
fi

# Runtime facts (AGENTSHROUD_VERSION etc.) — separate from SOUL.md's sync-stamped
# persona content so this always reflects the CURRENT boot, not the last time the
# persona changed. Fixes a real 2026-08-24 incident: run-standalone.sh never passed
# AGENTSHROUD_VERSION into the container at all, so when asked its own version
# Hermes had zero real data and hallucinated "1.0.0" — same failure class as the
# 2026-08-08 voice_gateway regression, just never fixed here. Runs on every boot
# (cheap, always accurate) rather than being stamp-gated like SOUL.md itself.
_RUNTIME_FACTS_DEST="${DATA_DIR}/AGENTS.md"
_runtime_facts_line="AgentShroud version: v${AGENTSHROUD_VERSION:-unknown} (from AGENTSHROUD_VERSION env var, set at container start — never guess this)."
if [ -f "${_RUNTIME_FACTS_DEST}" ] && grep -q "^AgentShroud version:" "${_RUNTIME_FACTS_DEST}" 2>/dev/null; then
    _tmp_facts="${DATA_DIR}/.AGENTS.md.tmp.$$"
    sed "s|^AgentShroud version:.*|${_runtime_facts_line}|" "${_RUNTIME_FACTS_DEST}" > "${_tmp_facts}" 2>/dev/null \
      && mv -f "${_tmp_facts}" "${_RUNTIME_FACTS_DEST}" 2>/dev/null \
      || rm -f "${_tmp_facts}" 2>/dev/null
else
    printf '%s\n' "${_runtime_facts_line}" >> "${_RUNTIME_FACTS_DEST}" 2>/dev/null
fi
echo "[hermes-init] Runtime facts: AgentShroud v${AGENTSHROUD_VERSION:-unknown}"

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

# Generalized Jira dev-ticket helper (create/comment/transition) used by the
# i-hdev orchestration skill so every autonomous dev batch gets a real SCRUM
# ticket — refresh on EVERY boot, same rationale as jira_weekly_review.py above.
if [ -f "${DEFAULTS_DIR}/workspace/jira_dev_ticket.py" ]; then
    mkdir -p "${DATA_DIR}/workspace"
    cp "${DEFAULTS_DIR}/workspace/jira_dev_ticket.py" \
       "${DATA_DIR}/workspace/jira_dev_ticket.py"
    chmod 755 "${DATA_DIR}/workspace/jira_dev_ticket.py" 2>/dev/null || true
    echo "[hermes-init] Seeded workspace/jira_dev_ticket.py"
else
    echo "[hermes-init] WARN: jira_dev_ticket.py not found in defaults — skipping"
fi

# ── Native cron jobs — idempotent seed on every boot ───────────────────────
# Uses `hermes cron create` (writes to Hermes's internal db) rather than
# the YAML file, which is not read natively by hermes-agent.
# Idempotent: _seed_cron deletes any existing job with the same name before
# creating, so re-seeds on upgrade never accumulate duplicates.
# (Prior stamp-file gating v1/v2/v3 caused triplication on each version bump
# because hermes cron create has no dedup — removed in favour of this approach.)
#
# Optional $5/$6 (model/provider): per-job-type model pin, added 2026-08-23.
# Every job previously ran on whatever cron.model/model.default resolve_model.py
# set globally (nemotron-3.5-lightning-rapid in prod) — one model for every job
# type regardless of what the job actually does. Live one-shot testing against
# the real gateway (dev host, 2026-08-23) on real job content — a Competitor
# Matrix synthesis task and a strict-format Telegram-HTML digest, both pulled
# verbatim from these jobs' actual prompts — showed nemotron-3.5-lightning-rapid
# consistently exhausts its entire completion budget (tested up to 3000 tokens,
# 3x the newsletter-job fix's max_tokens) on unresolved internal "thinking
# process" monologue and NEVER emits the requested deliverable (finish_reason
# "length" both times, zero usable output), on tasks as small as an 8-line,
# 500-max-token digest — not a token-budget problem, a genuine coherence
# failure under this workload. gemma-4-26b-a4b-it (Turbo Fieldflare) completed
# both tasks correctly: complete, source-faithful output (correctly left
# unstated fields blank rather than inventing values — gemma-4-12b-it-4bit, by
# contrast, hallucinated an unstated "ACTIVE" status on 7 of 12 rows, violating
# the job's own "do not add, guess, or invent" rule) and exact Telegram-HTML
# format/filtering compliance. deepseek-r1-0528-qwen3-8b could not be tested at
# all — confirmed 404 via the gateway before this session's llm_proxy.py OMLX
# alias fix (see gateway/proxy/llm_proxy.py's _normalize_local_model) — so it is
# deliberately NOT assigned here pending a follow-up validation pass once that
# fix ships. Applied to every content-generating job below except
# jira-weekly-review, whose payload is "run this exact script, report exit
# code" — near-zero free-form generation, so the failure mode this fix targets
# doesn't apply.
_seed_cron() {
    local _name="$1" _deliver="$2" _schedule="$3" _prompt="$4" _model="${5:-}" _provider="${6:-}"
    # Remove all pre-existing jobs with this exact name, then create one canonical copy.
    hermes cron list 2>/dev/null \
      | awk -v name="$_name" '
            /^  [a-f0-9]{12} \[/ { id = $1; next }
            index($0, "Name:") && index($0, name) { print id }
          ' \
      | xargs -r -n1 hermes cron delete >/dev/null 2>&1 || true
    if [ -n "$_model" ]; then
        hermes cron create --name "$_name" --deliver "$_deliver" \
          --model "$_model" --provider "${_provider:-ollama}" "$_schedule" "$_prompt" \
          2>/dev/null \
          && echo "[hermes-init] Seeded: $_name (model=$_model)" \
          || echo "[hermes-init] WARN: seed failed: $_name"
    else
        hermes cron create --name "$_name" --deliver "$_deliver" "$_schedule" "$_prompt" \
          2>/dev/null \
          && echo "[hermes-init] Seeded: $_name" \
          || echo "[hermes-init] WARN: seed failed: $_name"
    fi
    # Dev-environment pausing is handled once, comprehensively, at the end
    # of this script (after ALL jobs exist, not just the ones seeded here) —
    # see the "Dev environment: pause every Hermes cron job" block below.
}

echo "[hermes-init] Seeding native cron jobs (idempotent)..."

_seed_cron "AgentShroud Daily Check-in" "telegram" "0 14 * * *" \
    "Daily AgentShroud check-in from Hermes. Report current date/time, brief status of active tasks, and anything noteworthy from today. Under 150 words, send via Telegram to Isaiah." \
    "gemma-4-26b-a4b-it" "ollama"

_seed_cron "AgentShroud Weekly Summary" "telegram" "0 18 * * 5" \
    "Weekly summary from Hermes: key topics this week, skills learned or created, and what to focus on next week. Format concisely, deliver via Telegram." \
    "gemma-4-26b-a4b-it" "ollama"

_seed_cron "Weekly Kaizen Review" "telegram" "0 17 * * 5" \
    "Friday 5 PM weekly kaizen review (Hermes). What shipped this week? What caused friction? What process improvements would most help AgentShroud development? Format: SHIPPED / FRICTION / IMPROVE. Be specific and actionable." \
    "gemma-4-26b-a4b-it" "ollama"

_seed_cron "Monthly Chaos Engineering Drill" "telegram" "0 9 1 * *" \
    "First of month chaos engineering drill (Hermes). Simulate one failure scenario for AgentShroud involving Hermes: gateway crash, volume corruption, bot disconnect, or dependency outage. Describe failure mode, detection method, blast radius, and recovery procedure." \
    "gemma-4-26b-a4b-it" "ollama"

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_memory_journal_prompt='Nightly memory consolidation. Summarize today'"'"'s active projects, pending tasks, decisions made, and key facts for continuity. Append your summary to /opt/data/memories/journal-$(date +%Y-%m).md as a new dated section (use today'"'"'s date in YYYY-MM-DD format as the section heading). Create the file if it does not exist. Silent operation — no Telegram delivery.'
_seed_cron "Daily Memory Journal" "local" "55 23 * * *" "$_memory_journal_prompt" "gemma-4-26b-a4b-it" "ollama"

_seed_cron "Weekly Hermes Stability Report" "telegram" "0 9 * * 1" \
    "Read /opt/data/logs/gateway-exit-diag.log (last 7 days entries) and /opt/data/.start-history (one epoch per line). Compute: total restarts this week, crashes per day as a sparkline (e.g. 0 0 2 0 1 0 3), longest stable window in hours, top 3 exit codes by frequency, any backoff pauses triggered (5-minute sleeps). Format as 'Hermes Weekly Stability — <date range>' in under 200 words. Send via Telegram. If log files do not exist, report that Hermes has been stable with no recorded exits this week." \
    "gemma-4-26b-a4b-it" "ollama"

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_competitive_landscape_prompt='Read /opt/data/workspace/competitive-analysis.md for research instructions. Execute the full 4-section competitive intelligence report. CRITICAL RULES: zero hallucinations — every company, product, and statistic must be verified against a live primary source. Exclude anything unverified. Every claim requires a working URL. Research competitors of AgentShroud (autonomous agent security tools — NOT the agents themselves). Verify GitHub star counts from live pages. Save report as /opt/data/workspace/reports/competitive-report-$(date +%Y-%m-%d).md (use today'"'"'s date in YYYY-MM-DD format). Append one-line summary to /opt/data/workspace/reports/trend-log.md. Do NOT send any email — the separate Hermes Competitive Intelligence Email cron job handles delivery. Silence is correct if nothing new is found; hallucination is a critical failure.'
_seed_cron "Hermes Competitive Landscape Update (AM/PM)" "local" "0 6,15 * * *" "$_competitive_landscape_prompt" "gemma-4-26b-a4b-it" "ollama"

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_competitive_email_prompt='Read the most recent competitive-report-*.md from /opt/data/workspace/reports/ (prefer today'"'"'s date in YYYY-MM-DD format). If no report exists, use body '"'"'No significant changes detected today.'"'"' Render as a clean HTML email with inline CSS only (white bg #ffffff, text #111111, links #1a73e8, code bg #f6f8fa). To render: copy the cron-operations skill'"'"'s scripts/render_md_email.py to /opt/data/workspace/render_email.py, set its SRC/DST Path() constants (DST = /tmp/competitive-email.html), then run: python3 /opt/data/workspace/render_email.py. If the skill script is unavailable, write a pure-stdlib renderer to /opt/data/workspace/render_email.py and run it the same way. NEVER use execute_code, python3 -c, pip install, or uv pip install — all are blocked in cron mode. NEVER write_file a .py to /tmp/ — write renderer scripts to /opt/data/workspace/ only. The final .html output at /tmp/ is fine. Then run EXACTLY: /usr/local/bin/agentshroud-email-send.sh --html --subject '"'"'AgentShroud Hermes Competitive Intelligence'"'"' --body-file /tmp/competitive-email.html. The --html flag is mandatory — omitting it delivers raw markdown as plain text. Expect HTTP 200. On failure, report the full error via Telegram.'
_seed_cron "Hermes Competitive Intelligence Email (AM/PM)" "local" "0 7,16 * * *" "$_competitive_email_prompt" "gemma-4-26b-a4b-it" "ollama"

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
    # tirith's rule id for this flag is discovered at runtime (its `explain --list`
    # output) rather than hard-coded, so a tirith version bump that renames the
    # rule can't silently create a wrong-rule no-op that looks trusted but isn't.
    #
    # CRASH-STORM ROOT CAUSE (2026-07-20): this used to call the nonexistent
    # `tirith rules list` subcommand (real CLI has no `rules` command — see
    # `tirith --help`). That failed with exit 2 on every boot; under this
    # script's `set -euo pipefail`, an unguarded pipeline assignment propagates
    # the failure even though every downstream awk/tr/sort stage succeeds, which
    # aborted this whole script, which aborted start-hermes.sh (the container's
    # s6-overlay "main program"), which took the ENTIRE Hermes container down —
    # every ~25-40s, indistinguishable from a Python-level crash because the
    # actual gateway process was healthy and idle the whole time. `|| true`
    # restores this block's originally-intended graceful degradation (the `else`
    # branch below already existed for exactly this "not enumerable" case).
    _http_rules="$(/opt/data/bin/tirith explain --list --format json 2>/dev/null \
        | python3 -c '
import json, sys
try:
    rules = json.load(sys.stdin)
except Exception:
    rules = []
keywords = ("http", "execution context", "unencrypted", "insecure")
for r in rules:
    blob = " ".join(str(r.get(k, "")) for k in ("id", "title", "description")).lower()
    if any(k in blob for k in keywords):
        print(r.get("id", ""))
' 2>/dev/null | sort -u)" || true
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
# name + url from that file (NOT hardcoded) and register each enabled server into
# Hermes' MCP config.
#
# Why we write config.yaml directly instead of `hermes mcp add`:
# `hermes mcp add <name> --url <url>` (Hermes 0.18.x) is DISCOVERY-FIRST and fully
# INTERACTIVE — it prompts "Does this server require authentication? [Y/n]", then
# connects/probes the endpoint, then prompts "Enable all tools? [Y/n/select]". In a
# non-interactive s6 init those prompts get EOF and the add is cancelled (verified
# live: it also hung/crash-looped the container). Hermes stores MCP servers in
# ${HERMES_HOME}/config.yaml under the `mcp_servers:` key (HERMES_HOME=/opt/data;
# see hermes_cli/mcp_config.py). An HTTP entry is simply {url, enabled: true}.
# Verified live: writing that key makes `hermes mcp list` show the server as
# "✓ enabled". This merges (never clobbers other servers, e.g. github) and is
# idempotent (only writes when the desired entry is missing/changed).
_MCP_SERVERS_JSON="${DEFAULTS_DIR}/mcp/servers.json"
_HERMES_CONFIG="${DATA_DIR}/config.yaml"
if [ -f "${_MCP_SERVERS_JSON}" ]; then
    if HERMES_MCP_SRC="${_MCP_SERVERS_JSON}" HERMES_MCP_CONFIG="${_HERMES_CONFIG}" \
       python3 - <<'PYEOF'
import json, os, re, sys

src = os.environ["HERMES_MCP_SRC"]
cfg_path = os.environ["HERMES_MCP_CONFIG"]

with open(src) as f:
    servers = (json.load(f).get("servers") or {})

# Desired mcp_servers entries from servers.json (url read from file, not hardcoded).
# Servers explicitly marked enabled: false are tracked separately (explicitly_disabled)
# so a stale enabled:true copy already sitting in config.yaml can be actively turned
# off below, not just left alone. Being purely additive here was the root cause of a
# real incident (2026-08-01): docker/config/hermes/mcp/servers.json disabled the
# "agentshroud-gateway" entry on 2026-07-18 (it points at http://gateway:8080/mcp,
# which the gateway has never actually served -- a real 404), but this script only
# ever ADDED/refreshed entries that SHOULD be enabled; it had no code path to turn off
# an entry already sitting in config.yaml from before the servers.json fix. That
# entry's stale enabled:true survived every single boot since, causing ~213 failed
# connection attempts/day indefinitely. Never leave a disabled-in-source-of-truth
# entry enabled in the derived config just because reconciliation only adds.
desired = {}
explicitly_disabled = set()
for name, s in servers.items():
    if not isinstance(s, dict):
        continue
    if s.get("enabled") is False:
        explicitly_disabled.add(name)
        continue
    url = s.get("url")
    if not url:
        continue
    desired[name] = {"url": url, "enabled": True}

if not desired and not explicitly_disabled:
    print("NO_SERVERS")
    sys.exit(0)

# Primary path: PyYAML (present in the Hermes venv). Preserves the full config
# structure and merges operator-added server fields (headers/tools/auth).
try:
    import yaml  # type: ignore

    cfg = {}
    if os.path.exists(cfg_path):
        with open(cfg_path) as f:
            cfg = yaml.safe_load(f) or {}
    mcp = cfg.setdefault("mcp_servers", {})
    changed = []
    for name, entry in desired.items():
        cur = mcp.get(name)
        if not isinstance(cur, dict):
            mcp[name] = dict(entry)
            changed.append(name)
        elif cur.get("url") != entry["url"] or cur.get("enabled") is False:
            cur["url"] = entry["url"]
            cur["enabled"] = True
            changed.append(name)
    # Actively disable any config.yaml entry servers.json marks enabled: false --
    # see the comment above `desired`/`explicitly_disabled` for why this must not
    # be skipped just because the entry "isn't in the desired set".
    for name in explicitly_disabled:
        cur = mcp.get(name)
        if isinstance(cur, dict) and cur.get("enabled") is not False:
            cur["enabled"] = False
            changed.append(name + " (disabled)")
    if changed:
        tmp = cfg_path + ".tmp.%d" % os.getpid()
        with open(tmp, "w") as f:
            yaml.safe_dump(cfg, f, sort_keys=False)
        os.replace(tmp, cfg_path)
        print("CHANGED:" + ",".join(changed))
    else:
        print("UNCHANGED")
    sys.exit(0)
except ImportError:
    pass  # Fall through to the stdlib-only text merge below.

# Fallback: no PyYAML — rewrite ONLY the top-level `mcp_servers:` block textually,
# preserving every other line (comments included). We treat a server as already
# present if a `  <name>:` key exists with a matching `    url: <url>` beneath it.
text = ""
if os.path.exists(cfg_path):
    with open(cfg_path) as f:
        text = f.read()
lines = text.splitlines()

# Locate an existing top-level mcp_servers: block [start, end).
start = end = None
for i, ln in enumerate(lines):
    if re.match(r"^mcp_servers:\s*$", ln):
        start = i
        j = i + 1
        while j < len(lines) and (lines[j].strip() == "" or lines[j].startswith(("  ", "\t"))):
            j += 1
        end = j
        break

existing_block = lines[start:end] if start is not None else []
existing_text = "\n".join(existing_block)

def has_server(name, url):
    # crude but safe: name key present AND its url line present in the block
    return (re.search(r"^ {2}%s:\s*$" % re.escape(name), existing_text, re.M)
            and ("url: %s" % url) in existing_text)

def is_enabled_in_block(name):
    m = re.search(r"^ {2}%s:\s*\n((?: {4}.+\n?)*)" % re.escape(name), existing_text + "\n", re.M)
    if not m:
        return None
    em = re.search(r"^ {4}enabled:\s*(\S+)", m.group(1), re.M)
    return em.group(1).lower() if em else None

changed = [n for n, e in desired.items() if not has_server(n, e["url"])]
# Same fix as the PyYAML path above: actively disable any entry servers.json marks
# enabled: false, not just skip touching it. See the comment on `explicitly_disabled`.
to_disable = [n for n in explicitly_disabled if is_enabled_in_block(n) not in (None, "false")]
changed += [n + " (disabled)" for n in to_disable]

# Build the merged mcp_servers block: keep existing entries, add/refresh desired ones.
merged = {}
# Parse existing simple entries (name -> {key: val}) to preserve unrelated servers.
cur_name = None
for ln in existing_block[1:]:  # skip the "mcp_servers:" header
    m = re.match(r"^ {2}([^\s:]+):\s*$", ln)
    if m:
        cur_name = m.group(1)
        merged[cur_name] = {}
        continue
    kv = re.match(r"^ {4}([^\s:]+):\s*(.+?)\s*$", ln)
    if kv and cur_name:
        merged[cur_name][kv.group(1)] = kv.group(2)
for n, e in desired.items():
    merged.setdefault(n, {})
    merged[n]["url"] = e["url"]
    merged[n]["enabled"] = "true"
for n in explicitly_disabled:
    if n in merged:
        merged[n]["enabled"] = "false"

block = ["mcp_servers:"]
for n in merged:
    block.append("  %s:" % n)
    for k, v in merged[n].items():
        block.append("    %s: %s" % (k, v))

if start is not None:
    new_lines = lines[:start] + block + lines[end:]
else:
    new_lines = lines + ([""] if lines and lines[-1].strip() else []) + block

if changed or start is None:
    tmp = cfg_path + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as f:
        f.write("\n".join(new_lines) + "\n")
    os.replace(tmp, cfg_path)
    print("CHANGED:" + ",".join(changed) if changed else "CHANGED")
else:
    print("UNCHANGED")
PYEOF
    then
        echo "[hermes-init] MCP servers reconciled from ${_MCP_SERVERS_JSON##*/} into config.yaml"
    else
        echo "[hermes-init] WARN: could not reconcile MCP servers (see error above) — will retry next boot"
    fi
else
    echo "[hermes-init] No synced mcp/servers.json — run scripts/sync-llm-settings.sh (skipping)"
fi

# ── Dev environment: pause every Hermes cron job ────────────────────────────
# Owner directive 2026-08-24: prod always runs its full schedule; dev never
# should (jobs are run manually there for testing) so the two stacks never
# double up load on the same shared local-model backends. The earlier
# per-_seed_cron pause (removed above) only covered the ~9 jobs baked into
# this script's _seed_cron calls — most of Hermes's real job set (newsletter
# pipelines, competitive-intel, CVE watch, etc: 27 jobs total as of
# 2026-08-24) was created live via `hermes cron create`/`edit` outside this
# script entirely and was never touched by that narrower fix. This blanket
# pass runs last, after every job that exists on this volume (seeded or
# live-added) is already in the store, and pauses all of them.
if [ "${AGENTSHROUD_ENV:-prod}" = "dev" ]; then
    _all_job_ids="$(hermes cron list --all 2>/dev/null | awk '/^  [a-f0-9]{12} \[/ { print $1 }')"
    if [ -z "${_all_job_ids}" ]; then
        echo "[hermes-init] WARN: dev cron pause-all found no jobs to pause"
    else
        _paused_count=0
        for _jid in ${_all_job_ids}; do
            hermes cron pause "${_jid}" >/dev/null 2>&1 && _paused_count=$(( _paused_count + 1 ))
        done
        echo "[hermes-init] Dev environment: paused ${_paused_count} Hermes cron job(s). Run manually to test: hermes cron run <id>"
    fi
fi

echo "[hermes-init] Config init complete"
