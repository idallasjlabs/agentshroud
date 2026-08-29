#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud startup wrapper - exports API keys from Docker secrets

set -euo pipefail

# ---------------------------------------------------------------------------
# Security agents — start before main process (non-fatal, background)
# ---------------------------------------------------------------------------

# ClamAV daemon — malware scanning for bot workspace
# Bot has ClamAV installed; clamd.conf uses /tmp for socket (read_only rootfs safe).
if command -v clamd >/dev/null 2>&1 && [ -f /var/lib/clamav/main.cvd -o -f /var/lib/clamav/main.cld ]; then
    clamd --config-file=/etc/clamav/clamd.conf 2>/tmp/clamd-start.log &
    echo "[startup] clamd launched (pid=$!)"
else
    echo "[startup] clamd: skipping (binary or virus DB not ready)"
fi

# Wazuh agent — FIM on /home/node/agentshroud/workspace
# /var/ossec is owned by node (chowned at build time); runs without root.
if [ -x /var/ossec/bin/wazuh-agentd ]; then
    mkdir -p /var/ossec/var/run /var/ossec/queue/sockets /var/ossec/tmp 2>/dev/null || true
    /var/ossec/bin/wazuh-agentd 2>/tmp/wazuh-start.log &
    echo "[startup] wazuh-agentd launched (pid=$!)"
fi

# AGENTSHROUD_HEALTHCHECKS_URL — openclaw_healthchecks_url Docker secret.
# This script is OpenClaw's actual container entrypoint (confirmed via its
# own boot logs). Gateway's real entrypoint is docker/scripts/gateway-start.sh
# — it never runs this file (it's staged into the gateway image but unused
# there), so it has its own copy of this same heartbeat block reading
# gateway_healthchecks_url instead. Inlined (not _read_secret_file, defined
# later in this script) since this block runs before that function exists.
_read_hc_secret() { awk 'NF {last=$0} END {printf "%s", last}' "$1"; }
if [ -f "/run/secrets/openclaw_healthchecks_url" ] && [ -s "/run/secrets/openclaw_healthchecks_url" ]; then
    export AGENTSHROUD_HEALTHCHECKS_URL="$(_read_hc_secret /run/secrets/openclaw_healthchecks_url)"
fi

# Healthchecks.io dead-man's-switch heartbeat. Pings AGENTSHROUD_HEALTHCHECKS_URL
# every 60s once OpenClaw's own health endpoint (127.0.0.1:18789/) responds.
# Added 2026-08-24 — Hermes has had this since Healthchecks.io was set up;
# OpenClaw never did, so a real outage was silent.
# No-op (once-per-hour log line) if AGENTSHROUD_HEALTHCHECKS_URL is unset.
(
    _tick=60
    _last_disabled_log=0
    while true; do
        _url="${AGENTSHROUD_HEALTHCHECKS_URL:-}"
        if [ -z "${_url}" ]; then
            _now="$(date +%s)"
            if [ "$(( _now - _last_disabled_log ))" -ge 3600 ]; then
                echo "[heartbeat] disabled: AGENTSHROUD_HEALTHCHECKS_URL not set"
                _last_disabled_log="${_now}"
            fi
            sleep "${_tick}"
            continue
        fi
        if curl -fsS --max-time 5 -o /dev/null "http://127.0.0.1:18789/" 2>/dev/null; then
            curl -fsS --max-time 10 "${_url}" -o /dev/null 2>/dev/null \
                && echo "[heartbeat] Pinged Healthchecks.io OK" \
                || echo "[heartbeat] WARN: Healthchecks.io ping failed (will retry in ${_tick}s)"
        else
            echo "[heartbeat] Health gate not ready — skipping ping"
        fi
        sleep "${_tick}"
    done
) &
echo "[startup] healthcheck heartbeat launched (pid=$!)"

# ---------------------------------------------------------------------------
# OpenClaw sandbox reaper — root cause fix for "sandbox abandonment"
# ---------------------------------------------------------------------------
# OpenClaw's own sandbox backend (agents.defaults.sandbox.scope=session,
# .openclaw/openclaw.json) starts one persistent `sleep infinity` container
# per cron job / collaborator chat and re-execs into it on every subsequent
# run — a deliberate warm-start design. It never stops or removes that
# container itself; there is no vendor-side TTL, idle timeout, or session-end
# hook. Found 2026-08-24: 10 `openclaw-sbx-agent-*` containers had
# accumulated, all `Up`, oldest ~13h with zero exec activity. Manually
# killing orphans (done earlier) doesn't fix the leak going forward — this
# does. Each sandbox's /workspace is a bind mount back to this container's
# own `.openclaw/workspace` (verified via `docker inspect` .Mounts), so
# removing an idle sandbox container loses no data — only the warm exec
# cache, rebuilt automatically on the sandbox's next use.
# Gated on `command -v docker`: only OpenClaw's image installs the Docker
# CLI (agents.defaults.sandbox.backend=docker requires it — see this repo's
# docker/bots/openclaw/Dockerfile); gateway shares this script but has no
# `docker` binary, so this block is a natural no-op there.
# Since this reaper already needs full-host Docker access, it also covers
# two sibling abandonment classes discovered 2026-08-24 alongside it:
#   - Hermes's own per-task code-execution sandboxes (nikolaik/python-nodejs
#     image, named hermes-<hex>, same "sleep infinity" warm-cache pattern as
#     OpenClaw's — found 21h+ old with nothing ever reaping them).
#   - GitHub MCP server sidecars (ghcr.io/github/github-mcp-server image,
#     Docker-random names since nothing names them explicitly) spawned per
#     agent session and never stopped when the session ends. These have
#     AutoRemove=true set at creation, so a plain `docker stop` (not `rm -f`)
#     is enough — Docker removes the container itself once it exits. Unlike
#     the two sandbox classes, an MCP server has no idle-vs-busy signal (it's
#     a single long-lived stdio process regardless of use), so this pass is
#     age-only with a longer, more conservative TTL to reduce the chance of
#     stopping a session that's still genuinely active.
if command -v docker >/dev/null 2>&1 && [ -n "${DOCKER_HOST:-}" ]; then
(
    # Background loop — never let one failed `docker` call (a container
    # removed between listing and inspecting, a transient proxy hiccup)
    # propagate via the parent script's `set -euo pipefail` and kill this
    # loop. Every command below is also individually guarded regardless.
    set +e +o pipefail
    _reap_tick=1800   # 30 min
    _reap_ttl=21600   # 6h — well past any single cron run or active chat turn
    _mcp_reap_ttl=43200   # 12h — no idle signal available, stay conservative

    _container_age_seconds() {
        # $1 = container id; prints age in seconds, or empty on failure.
        local _created _epoch
        _created="$(docker inspect --format '{{.Created}}' "$1" 2>/dev/null || true)"
        [ -z "${_created}" ] && return 1
        _epoch="$(date -d "${_created}" +%s 2>/dev/null || date -j -f '%Y-%m-%dT%H:%M:%S' "${_created%%.*}" +%s 2>/dev/null || echo 0)"
        [ "${_epoch}" -eq 0 ] && return 1
        echo $(( $(date +%s) - _epoch ))
    }

    # Concurrency cap — preventative, distinct from the TTL-based reaping
    # below. TTL only cleans up AFTER a sandbox has sat idle for 6h; nothing
    # stops the count climbing unbounded before that (found 2026-08-26: 13
    # openclaw-sbx + 4 mcp-github concurrently on the interactive/production
    # account, none old enough yet to hit the TTL — legitimate usage, not a
    # bug, but nothing was bounding it either). Same-image reaper runs on
    # both the interactive and automated-dev accounts, so this cap protects
    # both without needing to know which account it's running under.
    # Eviction only ever targets the OLDEST sandboxes that are ALSO idle
    # (same _proc_lines<=2 check as _reap_idle_sandboxes) — a busy sandbox is
    # never killed to satisfy the cap, even if that means staying over it
    # temporarily. Set with headroom above the highest observed count so far
    # (13), not the observed count itself — raise if legitimate concurrent
    # usage grows past this.
    _sbx_cap=20
    _mcp_cap=8

    _enforce_sandbox_cap() {
        # $1 = docker ps --filter args, $2 = cap
        local _ids _count _over
        _ids="$(docker ps -a --filter "$1" --format '{{.ID}}' 2>/dev/null)"
        [ -z "${_ids}" ] && return 0
        _count="$(echo "${_ids}" | wc -l | tr -d ' ')"
        _over=$(( _count - $2 ))
        [ "${_over}" -le 0 ] && return 0
        # Oldest first (CreatedAt sorts lexically fine — RFC3339 timestamps).
        docker ps -a --filter "$1" --format '{{.CreatedAt}} {{.ID}} {{.Names}}' 2>/dev/null \
          | sort \
          | while read -r _created _cid _cname; do
            [ "${_over}" -le 0 ] && break
            _proc_lines="$(docker top "${_cid}" 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')"
            if [ -n "${_proc_lines}" ] && [ "${_proc_lines}" -le 2 ]; then
                docker rm -f "${_cid}" >/dev/null 2>&1 \
                  && { echo "[sandbox-reaper] removed ${_cname} (over cap, idle)"; _over=$(( _over - 1 )); } \
                  || echo "[sandbox-reaper] WARN: failed to remove ${_cname}"
            fi
        done
    }

    _reap_idle_sandboxes() {
        # $1 = docker ps --filter args (as a single string, name-filter only)
        docker ps -a --filter "$1" --format '{{.ID}} {{.Names}}' 2>/dev/null \
          | while read -r _cid _cname; do
            [ -z "${_cid:-}" ] && continue
            _age="$(_container_age_seconds "${_cid}")" || continue
            [ "${_age}" -lt "${_reap_ttl}" ] && continue
            _proc_lines="$(docker top "${_cid}" 2>/dev/null | tail -n +2 | wc -l | tr -d ' ')"
            if [ -n "${_proc_lines}" ] && [ "${_proc_lines}" -le 2 ]; then
                docker rm -f "${_cid}" >/dev/null 2>&1 \
                  && echo "[sandbox-reaper] removed ${_cname} (idle $(( _age / 3600 ))h)" \
                  || echo "[sandbox-reaper] WARN: failed to remove ${_cname}"
            fi
        done
    }

    # Exited-container pass — separate from the idle-running check above.
    # Found 2026-08-25: `docker top` errors out on a container that isn't
    # running ("container ... is not running", exit 1), so `_proc_lines`
    # comes back empty and `_reap_idle_sandboxes`'s guard never fires for a
    # crashed/killed container — it only ever reaps containers that are
    # idle but still *running*. A host reboot or Colima restart kills every
    # sandbox at once (RestartPolicy is "no", so Docker never revives them),
    # and those then sit as dead weight forever regardless of TTL. No
    # age gate needed here: an exited container with no restart policy will
    # never do anything useful again by staying around.
    _reap_exited_sandboxes() {
        # $1 = docker ps --filter args (as a single string, name-filter only)
        docker ps -a --filter "$1" --filter "status=exited" --format '{{.ID}} {{.Names}}' 2>/dev/null \
          | while read -r _cid _cname; do
            [ -z "${_cid:-}" ] && continue
            docker rm -f "${_cid}" >/dev/null 2>&1 \
              && echo "[sandbox-reaper] removed ${_cname} (exited)" \
              || echo "[sandbox-reaper] WARN: failed to remove ${_cname}"
        done
    }

    # Rename pass — separate from reaping. Neither Hermes's own sandbox code
    # nor OpenClaw's MCP-server spawning exposes any container-naming config
    # (checked openclaw.json 2026-08-24, no docker/name/prefix keys under any
    # mcp/sandbox section), so containers land with Docker's random
    # adjective_scientist names (github-mcp-server sidecars) or a bare
    # hermes-<hex> that's easy to mistake for the main agentshroud-hermes-v2
    # container. `docker rename` doesn't touch the running process — safe to
    # run on an active container. Runs once immediately (covers whatever
    # already exists) and every tick after (covers newly-spawned ones); the
    # name-prefix check makes repeat runs a no-op for already-renamed ones.
    _rename_to_meaningful() {
        # $1 = docker ps --filter args, $2 = desired name prefix
        docker ps -a --filter "$1" --format '{{.ID}} {{.Names}}' 2>/dev/null \
          | while read -r _cid _cname; do
            [ -z "${_cid:-}" ] && continue
            case "${_cname}" in
                "$2"-*) continue ;;   # already renamed
            esac
            docker rename "${_cid}" "$2-${_cid}" >/dev/null 2>&1 \
              && echo "[sandbox-reaper] renamed ${_cname} -> $2-${_cid}" \
              || echo "[sandbox-reaper] WARN: failed to rename ${_cname}"
        done
    }
    _rename_to_meaningful "ancestor=ghcr.io/github/github-mcp-server:latest" "openclaw-mcp-github"
    _rename_to_meaningful "name=^/hermes-" "hermes-sandbox"
    _reap_exited_sandboxes "name=^/openclaw-sbx-"
    _reap_exited_sandboxes "name=^/hermes-sandbox-"
    _enforce_sandbox_cap "name=^/openclaw-sbx-" "${_sbx_cap}"
    _enforce_sandbox_cap "name=^/hermes-sandbox-" "${_sbx_cap}"
    _enforce_sandbox_cap "ancestor=ghcr.io/github/github-mcp-server:latest" "${_mcp_cap}"

    while true; do
        sleep "${_reap_tick}"
        _reap_idle_sandboxes "name=^/openclaw-sbx-"
        _reap_idle_sandboxes "name=^/hermes-sandbox-"
        _reap_exited_sandboxes "name=^/openclaw-sbx-"
        _reap_exited_sandboxes "name=^/hermes-sandbox-"
        _enforce_sandbox_cap "name=^/openclaw-sbx-" "${_sbx_cap}"
        _enforce_sandbox_cap "name=^/hermes-sandbox-" "${_sbx_cap}"

        docker ps -a --filter "ancestor=ghcr.io/github/github-mcp-server:latest" --format '{{.ID}} {{.Names}}' 2>/dev/null \
          | while read -r _cid _cname; do
            [ -z "${_cid:-}" ] && continue
            _age="$(_container_age_seconds "${_cid}")" || continue
            [ "${_age}" -lt "${_mcp_reap_ttl}" ] && continue
            docker stop "${_cid}" >/dev/null 2>&1 \
              && echo "[sandbox-reaper] stopped ${_cname} (idle $(( _age / 3600 ))h, AutoRemove will clean up)" \
              || echo "[sandbox-reaper] WARN: failed to stop ${_cname}"
        done
        _enforce_sandbox_cap "ancestor=ghcr.io/github/github-mcp-server:latest" "${_mcp_cap}"

        _rename_to_meaningful "ancestor=ghcr.io/github/github-mcp-server:latest" "openclaw-mcp-github"
        _rename_to_meaningful "name=^/hermes-" "hermes-sandbox"
    done
) &
echo "[startup] sandbox reaper launched (pid=$!)"
fi

# ---------------------------------------------------------------------------
# OpenClaw cron session-store cleanup — root cause fix for
# CronSessionLifecycleClaimError ("Session ... changed while starting
# work. Retry.")
# ---------------------------------------------------------------------------
# Found 2026-08-24 diagnosing a stuck "Collaborator Report - Morning" job:
# every isolated cron session's claim lease lives in a store file
# (agents/<id>/sessions/sessions.json) keyed by session ID. When a run's
# isolated-agent setup fails or times out before it ever produces a
# transcript file, OpenClaw leaves that claim entry behind -- there is no
# vendor-side reaper for it, the same gap class as the sandbox containers
# above. A live audit found 15 of 19 stored session entries system-wide
# (not just this one job) were stale in exactly this way. `openclaw
# sessions cleanup --fix-missing` is OpenClaw's own sanctioned maintenance
# command for this (prunes entries whose transcript file is missing) --
# confirmed safe and effective live: cleared the stuck entry, the job's
# next run then claimed a fresh session and completed normally.
if command -v openclaw >/dev/null 2>&1; then
(
    set +e +o pipefail
    _cleanup_tick=1800   # 30 min -- independent of the sandbox reaper's cadence
    while true; do
        sleep "${_cleanup_tick}"
        _out="$(openclaw sessions cleanup --all-agents --fix-missing --enforce 2>&1)"
        echo "[session-cleanup] ${_out}" | tr '\n' ' '
        echo ""
    done
) &
echo "[startup] openclaw session-store cleanup reaper launched (pid=$!)"
fi

# ---------------------------------------------------------------------------
# Env-split cron reconciliation: prod disables, dev enables (all jobs)
# ---------------------------------------------------------------------------
# Owner directive 2026-08-29 (REVERSES 2026-08-24): the cron quality work now
# lives in DEV -- jobs must run on their schedules there so local-model
# output can be iterated against golden baselines -- while PROD carries zero
# scheduled LLM load. Same blanket pass over the live cron store (covers
# static seed, `cron add`, and `cron edit` alike), gate inverted, plus the
# dev side now ENABLES so a store disabled under the old regime self-heals
# on the next dev boot. AGENTSHROUD_PROJECT threading is unchanged
# ("agentshroud-bot" on dev, "agentshroud" on prod; unset fails safe to
# prod, which under the new regime means jobs stay disabled -- still the
# conservative direction for the shared local-model backends).
if command -v openclaw >/dev/null 2>&1; then
    if [ "${AGENTSHROUD_PROJECT:-agentshroud}" != "agentshroud" ]; then
        _cron_action="enable"
        _cron_tag="dev-cron-enable"
    else
        _cron_action="disable"
        _cron_tag="prod-cron-disable"
    fi
(
    set +e +o pipefail
    _gw_wait=0
    while [ "${_gw_wait}" -lt 120 ]; do
        curl -fsS --max-time 3 -o /dev/null "http://127.0.0.1:18789/" 2>/dev/null && break
        sleep 5
        _gw_wait=$(( _gw_wait + 5 ))
    done
    _ids="$(openclaw cron list --json --all 2>/dev/null | python3 -c 'import json,sys; d=json.load(sys.stdin); [print(j["id"]) for j in d.get("jobs",[])]' 2>/dev/null)"
    if [ -z "${_ids}" ]; then
        echo "[${_cron_tag}] WARN: could not list cron jobs (gateway not ready in time?) -- nothing changed"
    else
        echo "${_ids}" | while read -r _id; do
            [ -z "${_id}" ] && continue
            openclaw cron "${_cron_action}" "${_id}" >/dev/null 2>&1
        done
        _n="$(echo "${_ids}" | grep -c .)"
        echo "[${_cron_tag}] ${_cron_action}d ${_n} cron job(s) (AGENTSHROUD_PROJECT=${AGENTSHROUD_PROJECT:-unset}, env-split 2026-08-29)"
    fi
) &
echo "[startup] env-split cron ${_cron_action}-all launched (pid=$!)"
fi

# ---------------------------------------------------------------------------
# Read the last non-empty line from a secret file.
# Handles garbled multi-line blobs (label + asterisks + real value) written to
# the secret backend before the 017e7bd write-path fix. For clean single-line
# values the result is identical to a raw cat + strip.
_read_secret_file() { awk 'NF {last=$0} END {printf "%s", last}' "$1"; }

# ---------------------------------------------------------------------------
# Export Gateway password from secret file
# Note: OpenClaw CLI expects OPENCLAW_GATEWAY_PASSWORD env var
if [ -f "/run/secrets/gateway_password" ]; then
    export OPENCLAW_GATEWAY_PASSWORD="$(_read_secret_file /run/secrets/gateway_password)"
    # FINAL: also set GATEWAY_AUTH_TOKEN so op-wrapper.sh routes through gateway
    export GATEWAY_AUTH_TOKEN="$OPENCLAW_GATEWAY_PASSWORD"
    # SECURITY (H3): Strip DNS architecture info from resolv.conf comments
# Docker adds internal network details that leak infrastructure topology
sed -i /^#.*ExtServers/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Overrides/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Based on host/d /etc/resolv.conf 2>/dev/null || true
sed -i /^#.*Option ndots/d /etc/resolv.conf 2>/dev/null || true

echo "[startup] Loaded Gateway password"
else
    echo "[startup] Warning: Gateway password file not found"
fi

# Export Telegram bot token from secret file (per-host token injection)
# The apply-patches.js script reads TELEGRAM_BOT_TOKEN and injects it into openclaw.json
if [ -f "/run/secrets/telegram_bot_token" ]; then
    export TELEGRAM_BOT_TOKEN="$(_read_secret_file /run/secrets/telegram_bot_token)"
    echo "[startup] Loaded Telegram bot token"
elif [ -n "${TELEGRAM_BOT_TOKEN_FILE:-}" ] && [ -f "$TELEGRAM_BOT_TOKEN_FILE" ]; then
    export TELEGRAM_BOT_TOKEN="$(_read_secret_file "$TELEGRAM_BOT_TOKEN_FILE")"
    echo "[startup] Loaded Telegram bot token from $TELEGRAM_BOT_TOKEN_FILE"
fi

# Export OpenAI API key from secret file (optional)
if [ -f "/run/secrets/openai_api_key" ] && [ -s "/run/secrets/openai_api_key" ]; then
    export OPENAI_API_KEY="$(_read_secret_file /run/secrets/openai_api_key)"
    echo "[startup] Loaded OpenAI API key"
else
    echo "[startup] OpenAI API key not configured (optional)"
fi

# Export Google Gemini API key from secret file (optional)
if [ -f "/run/secrets/google_api_key" ] && [ -s "/run/secrets/google_api_key" ]; then
    export GOOGLE_API_KEY="$(_read_secret_file /run/secrets/google_api_key)"
    echo "[startup] Loaded Google API key"
else
    echo "[startup] Google API key not configured (optional)"
fi

_LOCAL_ONLY_MODEL=false
_MODEL_MODE="$(echo "${AGENTSHROUD_MODEL_MODE:-local}" | tr '[:upper:]' '[:lower:]')"
if [[ "${_MODEL_MODE}" != "cloud" ]]; then
    _LOCAL_ONLY_MODEL=true
fi
if [[ "${OPENCLAW_MAIN_MODEL:-}" == ollama/* ]]; then
    _LOCAL_ONLY_MODEL=true
fi
if $_LOCAL_ONLY_MODEL && [ -z "${OLLAMA_API_KEY:-}" ]; then
    export OLLAMA_API_KEY="ollama-local"
    echo "[startup] Set default OLLAMA_API_KEY for local provider registration"
fi

# Load Claude OAuth token only when running non-local model backends.
if ! $_LOCAL_ONLY_MODEL; then
    if [ -f "/run/secrets/anthropic_oauth_token" ] && [ -s "/run/secrets/anthropic_oauth_token" ]; then
        export ANTHROPIC_OAUTH_TOKEN="$(_read_secret_file /run/secrets/anthropic_oauth_token)"
        echo "[startup] Loaded Claude OAuth token (from secret file)"
    fi
else
    echo "[startup] Local Ollama model selected — skipping Claude token load"
fi

# FINAL: Load secrets via gateway op-proxy (bot has no direct 1Password access).
# op-wrapper.sh routes "op read" through POST /credentials/op-proxy when
# GATEWAY_AUTH_TOKEN and GATEWAY_OP_PROXY_URL are set.

# Retry wrapper for op-proxy reads — handles race condition where the bot
# restarts before the gateway's 1Password connection is fully ready.
# Usage: op_proxy_read_with_retry <label> <op-reference>
# Returns the secret value on stdout; exits non-zero only if all retries fail.
op_proxy_read_with_retry() {
    local label="$1"
    local reference="$2"
    # Cascading waits: 5s, 10s, 15s, 30s, 60s — total patience: 2 minutes before final attempt
    local delays=(5 10 15 30 60)
    local value=""

    for i in "${!delays[@]}"; do
        local attempt=$((i + 1))
        local total=$(( ${#delays[@]} + 1 ))
        value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
        if [ -n "$value" ]; then
            printf '%s' "$value"
            return 0
        fi
        local wait="${delays[$i]}"
        echo "[startup] ⚠ ${label}: attempt ${attempt}/${total} failed — retrying in ${wait}s" >&2
        sleep "$wait"
    done

    # Final attempt after all waits exhausted
    value="$(/usr/local/bin/op-wrapper.sh read "$reference" 2>/dev/null)" || true
    if [ -n "$value" ]; then
        printf '%s' "$value"
        return 0
    fi

    echo "[startup] ✗ ${label}: all ${total} attempts failed after 2 minutes" >&2
    return 1
}

# Only attempt op-proxy reads if 1Password credentials are present and non-empty
_OP_AVAILABLE=false
if [ -f "/run/secrets/1password_bot_email" ] && [ -s "/run/secrets/1password_bot_email" ]; then
    _OP_AVAILABLE=true
fi

if [ -n "${GATEWAY_AUTH_TOKEN:-}" ] && [ -n "${GATEWAY_OP_PROXY_URL:-}" ] && $_OP_AVAILABLE; then
    echo "[startup] Loading secrets via gateway op-proxy (${GATEWAY_OP_PROXY_URL})"

    # Load Claude OAuth token via op-proxy only when not pinned to local Ollama models.
    if ! $_LOCAL_ONLY_MODEL; then
        if [ -z "${ANTHROPIC_OAUTH_TOKEN:-}" ]; then
            ANTHROPIC_OAUTH_TOKEN="$(op_proxy_read_with_retry "Claude OAuth token" \
                "op://Agent Shroud Bot Credentials/AgentShroud - Anthropic Claude OAuth Token/claude oath token")" || true
            if [ -n "$ANTHROPIC_OAUTH_TOKEN" ]; then
                export ANTHROPIC_OAUTH_TOKEN
                echo "[startup] ✓ Loaded Claude OAuth token (via op-proxy)"
            else
                echo "[startup] ⚠ Could not load Claude OAuth token after retries"
            fi
        else
            echo "[startup] ✓ Claude OAuth token already loaded (from secret file)"
        fi
    else
        echo "[startup] Local Ollama model selected — skipping Claude op-proxy fetch"
    fi

    # Load Brave Search API key (non-blocking single attempt).
    # This key is optional; do not delay bot startup for retry backoff loops.
    # Brief delay gives the gateway op-proxy time to authenticate before the first attempt.
    # Item ID: 6j6ij5tzld6kobvit5tk6ufrhq (Brave Search API - agentshroud.ai@gmail.com)
    sleep 5
    BRAVE_API_KEY="${BRAVE_API_KEY:-$(/usr/local/bin/op-wrapper.sh read \
        "op://Agent Shroud Bot Credentials/6j6ij5tzld6kobvit5tk6ufrhq/brave search api key" \
        2>/dev/null || true)}"
    if [ -n "$BRAVE_API_KEY" ]; then
        export BRAVE_API_KEY
        echo "[startup] ✓ Loaded Brave Search API key"
    else
        echo "[startup] ⚠ Brave Search API key unavailable (continuing without web search key)"
    fi

else
    echo "[startup] Warning: Gateway op-proxy not configured, 1Password secrets unavailable"
fi

# Apply OpenClaw config defaults (SSH allowlist, cron jobs, agent patches, workspace brand files)
echo "[startup] Bootstrapping OpenClaw config..."
/usr/local/bin/init-openclaw-config.sh

# CVE-2021-23358: upgrade underscore in bot workspace if pinned to vulnerable version (<1.12.1)
# underscore@1.7.0 allows arbitrary code execution via _.template(); fixed in >=1.12.1
_WORKSPACE_PKG="/home/node/agentshroud/workspace/package-lock.json"
if [ -f "$_WORKSPACE_PKG" ] && grep -q '"underscore"' "$_WORKSPACE_PKG" 2>/dev/null; then
    _US_VER=$(node -e "try{console.log(require('/home/node/agentshroud/workspace/node_modules/underscore/package.json').version)}catch(e){console.log('0')}" 2>/dev/null || echo "0")
    # Skip npm update if already patched (>= 1.12.1)
    if [ "$_US_VER" = "0" ] || [ "$(printf '%s\n' "1.12.1" "$_US_VER" | sort -V | head -n1)" != "1.12.1" ]; then
        cd /home/node/agentshroud/workspace && npm update underscore --no-fund --no-audit 2>/dev/null || true
        cd /home/node
        echo "[startup] underscore upgraded from $_US_VER (CVE-2021-23358)"
    else
        echo "[startup] underscore $_US_VER already patched — skipping update (CVE-2021-23358)"
    fi
fi

# DNS warmup probe — prevents EAI_AGAIN on first user message.
# Docker's internal resolver (127.0.0.11) takes ~20-30s to route to the Pi-hole
# after container restart. Poll until external DNS resolves before starting OpenClaw.
_dns_warmup_probe() {
    local target="${1:-api.github.com}"
    local max_wait="${2:-30}"
    local elapsed=0
    while [ "${elapsed}" -lt "${max_wait}" ]; do
        if curl -sf --max-time 3 "https://${target}" -o /dev/null 2>/dev/null; then
            return 0
        fi
        sleep 2
        elapsed=$(( elapsed + 2 ))
    done
    return 1  # Non-fatal — OpenClaw starts regardless; warning only
}
echo "[startup] DNS warmup check..."
if _dns_warmup_probe "api.github.com" 30; then
    echo "[startup] ✓ External DNS ready"
else
    echo "[startup] ⚠ External DNS probe timed out — OpenClaw will start anyway (tools may retry)"
fi

# Start AgentShroud gateway (powered by OpenClaw CLI)
echo "[startup] Starting AgentShroud gateway..."
OPENCLAW_BIND_MODE="${OPENCLAW_GATEWAY_BIND:-loopback}"
UV_THREADPOOL_SIZE="${UV_THREADPOOL_SIZE:-16}" node --stack-size=65536 "$(command -v openclaw)" gateway --allow-unconfigured --bind "${OPENCLAW_BIND_MODE}" &
OPENCLAW_PID=$!

# Telegram notification helpers — ALL traffic routes through AgentShroud gateway
# No direct api.telegram.org calls. No hardcoded bot tokens.
_OWNER_CHAT_ID="8096968754"
_GATEWAY_TELEGRAM_BASE="${GATEWAY_OP_PROXY_URL:-http://gateway:8080}/telegram-api"

_telegram_bot_token() {
    # Try env var first (exported from Docker secret at line ~31)
    if [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
        printf '%s' "$TELEGRAM_BOT_TOKEN"
        return 0
    fi
    # Fall back to reading from OpenClaw config file (try both known paths)
    node -e "
        const paths = [
            '/home/node/.agentshroud/openclaw.json',
            '/home/node/.openclaw/openclaw.json',
        ];
        for (const p of paths) {
            try {
                const c = JSON.parse(require('fs').readFileSync(p, 'utf8'));
                const t = c.channels && c.channels.telegram && c.channels.telegram.botToken;
                if (t) { process.stdout.write(t); process.exit(0); }
            } catch(e) {}
        }
    " 2>/dev/null
}

_telegram_send() {
    local text="$1"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        echo "[startup] ⚠ No Telegram bot token available — cannot send notification" >&2
        return 1
    fi
    # Route through AgentShroud gateway Telegram proxy (never direct to api.telegram.org)
    curl -sf --max-time 10 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"chat_id\":\"${_OWNER_CHAT_ID}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

# Slack notification helpers — token injected by gateway proxy, same security model as Telegram.
# SLACK_API_BASE_URL is set by docker-compose.yml to http://gateway:8080/slack-api so all
# outbound Slack API calls are intercepted by the gateway for content scanning.
_GATEWAY_SLACK_BASE="${SLACK_API_BASE_URL:-http://gateway:8080/slack-api}"

_slack_channel_id() {
    # Prefer env override, then Docker secret, then empty (disabled)
    if [ -n "${AGENTSHROUD_SLACK_CHANNEL_ID:-}" ]; then
        printf '%s' "$AGENTSHROUD_SLACK_CHANNEL_ID"
        return 0
    fi
    if [ -f "/run/secrets/slack_bot_token" ]; then
        # Channel ID must be configured via env — no way to derive it from the token
        return 1
    fi
    return 1
}

_slack_send() {
    local text="$1"
    local channel
    channel="${AGENTSHROUD_SLACK_CHANNEL_ID:-}"
    if [ -z "$channel" ]; then
        return 0  # Slack notifications not configured — skip silently
    fi
    # Route through AgentShroud gateway Slack proxy (never direct to slack.com)
    curl -sf --max-time 10 -X POST "${_GATEWAY_SLACK_BASE}/chat.postMessage" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -d "{\"channel\":\"${channel}\",\"text\":\"${text}\"}" \
        >/dev/null 2>&1
}

_telegram_send_photo() {
    local caption="$1"
    local photo_path="${2:-/app/branding/logo.png}"
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        echo "[startup] ⚠ Photo notification: no bot token available" >&2
        return 1
    fi
    if [ ! -f "$photo_path" ]; then
        echo "[startup] ⚠ Photo notification: logo file not found at ${photo_path}" >&2
        return 1
    fi
    # Logo PNG is ~300 KB; on a VPN link the upload can take up to 30s.
    local resp exit_code
    resp=$(curl -s --max-time 45 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/sendPhoto" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        -F "chat_id=${_OWNER_CHAT_ID}" \
        -F "caption=${caption}" \
        -F "photo=@${photo_path}" \
        2>/dev/null)
    exit_code=$?
    if [ "$exit_code" -ne 0 ]; then
        echo "[startup] ⚠ Photo notification: curl failed (exit=${exit_code})" >&2
        return 1
    fi
    if ! echo "$resp" | /usr/bin/grep -q '"ok":true'; then
        echo "[startup] ⚠ Photo notification: gateway error: ${resp:0:200}" >&2
        return 1
    fi
    return 0
}

_telegram_get_me_ready() {
    local token
    token="$(_telegram_bot_token)"
    if [ -z "$token" ]; then
        return 1
    fi
    curl -sf --max-time 8 -X POST "${_GATEWAY_TELEGRAM_BASE}/bot${token}/getMe" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN:-}" \
        -H "X-AgentShroud-System: 1" \
        >/dev/null 2>&1
}

_model_runtime_ready() {
    if [ "${AGENTSHROUD_MODEL_MODE:-cloud}" != "local" ]; then
        return 0
    fi
    local model_name="${AGENTSHROUD_LOCAL_MODEL:-}"
    if [ -z "${model_name}" ]; then
        model_name="${AGENTSHROUD_LOCAL_MODEL_REF#ollama/}"
    fi
    if [ -z "${model_name}" ]; then
        return 1
    fi
    curl -sf --max-time 8 "${OLLAMA_BASE_URL:-http://gateway:8080/v1}/../api/tags" \
        | grep -F "\"name\":\"${model_name}\"" >/dev/null 2>&1
}

# ── Security-critical cron reconciliation ────────────────────────────────────
# init-openclaw-config.sh's cron seeding (see comments there) only replaces
# cron/jobs.json ON DISK when the whole-file image-default checksum changes,
# and only propagates into OpenClaw's own sqlite-backed live cron store on the
# very first boot. An already-existing live job is intentionally left alone so
# a user's real `openclaw cron edit` customizations survive restarts — but
# that same protection means a live job seeded before a security fix (e.g. the
# raw-ssh-to-lab-hosts bug fixed in PR #321) never gets corrected by any later
# fix to the seed file, because the fix only ever touches the file, not the
# already-existing live job. Confirmed 2026-08-03: the "AgentShroud Daily
# Check-in" job's live payload had reverted to raw `ssh -l agentshroud-bot
# host.docker.internal` / `raspberrypi.tail240ea8.ts.net` months after PR #321,
# invisible to every prior fix.
#
# For a short, explicit list of security-critical job IDs, force-correct the
# LIVE job (via the CLI, not the file) whenever its content still matches a
# known-dangerous pattern. This runs once the gateway is confirmed responsive
# (inside the readiness block below) and never touches jobs outside this list,
# so ordinary live cron customizations are unaffected.
_SECURITY_CRITICAL_CRON_JOB_IDS="a16ccca0-e953-48f3-9ebe-430e1085dea3"  # AgentShroud Daily Check-in
_CRON_DANGER_PATTERN='ssh (marvin|raspberrypi|trillian|pi)\b|agentshroud-bot@|tail[0-9a-f]+\.ts\.net'
_CRON_SEED_FILE="/app/config-defaults/openclaw/cron/jobs.json"

_reconcile_security_critical_cron() {
    local job_id live_msg seed_msg
    for job_id in ${_SECURITY_CRITICAL_CRON_JOB_IDS}; do
        live_msg="$(openclaw cron get "${job_id}" 2>/dev/null | node -e '
            let d = "";
            process.stdin.on("data", c => d += c);
            process.stdin.on("end", () => {
                try {
                    const j = JSON.parse(d);
                    process.stdout.write((j.payload && j.payload.message) || "");
                } catch (e) {}
            });
        ' 2>/dev/null)"
        if [ -z "${live_msg}" ]; then
            continue  # job not found or CLI not ready yet — never block startup on this
        fi
        if printf '%s' "${live_msg}" | grep -qE "${_CRON_DANGER_PATTERN}"; then
            echo "[startup] ⚠ Live cron job ${job_id} contains a raw-ssh/Tailscale-hostname pattern — force-correcting from seed"
            seed_msg="$(node -e "
                const jobs = JSON.parse(require('fs').readFileSync('${_CRON_SEED_FILE}', 'utf8')).jobs;
                const j = jobs.find(x => x.id === '${job_id}');
                if (j && j.payload && j.payload.message) process.stdout.write(j.payload.message);
            " 2>/dev/null)"
            if [ -n "${seed_msg}" ]; then
                if openclaw cron edit "${job_id}" --message "${seed_msg}" >/dev/null 2>&1; then
                    echo "[startup] ✓ Force-corrected live cron job ${job_id} from seed"
                else
                    echo "[startup] ⚠ Failed to force-correct live cron job ${job_id} — leaving as-is"
                fi
            else
                echo "[startup] ⚠ No seed message found for job ${job_id} in ${_CRON_SEED_FILE} — skipping force-correct"
            fi
        fi
    done
}

# Instance identity for notifications
# _INSTANCE_LABEL removed 2026-08-27 — was only used to suffix the Telegram
# startup message ("OpenClaw online — <label>"); owner asked for the plain
# Hermes-style message instead, leaving it with no remaining consumers.
_BOT_NAME="${OPENCLAW_BOT_NAME:-agentshroud-openclaw}"
_STARTUP_NOTICE_STAMP="${OPENCLAW_STARTUP_NOTICE_STAMP:-/home/node/.openclaw/workspace/.startup_notice_at}"
_STARTUP_NOTICE_COOLDOWN_SECONDS="${OPENCLAW_STARTUP_NOTICE_COOLDOWN_SECONDS:-300}"

# Forward TERM/INT to openclaw, backup memory, send shutdown notification
trap '
    echo "[startup] Shutdown signal received — backing up memory..."
    MEMORY_BACKUP_DIR="/app/memory-backups"
    WORKSPACE_DIR="/home/node/.openclaw/workspace"
    if [ -d "${MEMORY_BACKUP_DIR}" ]; then
        [ -f "${WORKSPACE_DIR}/MEMORY.md" ] && cp "${WORKSPACE_DIR}/MEMORY.md" "${MEMORY_BACKUP_DIR}/MEMORY.md"
        if [ -d "${WORKSPACE_DIR}/memory" ]; then
            mkdir -p "${MEMORY_BACKUP_DIR}/memory"
            cp -r "${WORKSPACE_DIR}/memory/"* "${MEMORY_BACKUP_DIR}/memory/" 2>/dev/null || true
        fi
        for f in USER.md TOOLS.md HEARTBEAT.md; do
            [ -f "${WORKSPACE_DIR}/${f}" ] && cp "${WORKSPACE_DIR}/${f}" "${MEMORY_BACKUP_DIR}/${f}"
        done
        echo "[startup] ✓ Memory backed up before shutdown"
    fi
    echo "[startup] Sending shutdown notifications..."
    _telegram_send "🔴 OpenClaw shutting down" \
        && echo "[startup] ✓ Sent Telegram shutdown notification" \
        || echo "[startup] ⚠ Could not send Telegram shutdown notification"
    _slack_send "OpenClaw shutting down" \
        && echo "[startup] ✓ Sent Slack shutdown notification" \
        || true
    kill $OPENCLAW_PID 2>/dev/null
' TERM INT

# Wait for gateway/model/telegram readiness, then send startup notifications
(
    # Isolate from parent set -euo pipefail so transient failures never kill the subshell
    set +euo pipefail 2>/dev/null || true

    now_epoch="$(date +%s)"
    last_notice_epoch=""
    if [ -f "${_STARTUP_NOTICE_STAMP}" ]; then
        last_notice_epoch="$(cat "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true)"
    fi
    should_notify="yes"
    if [ -n "${last_notice_epoch}" ] && [ "${last_notice_epoch}" -eq "${last_notice_epoch}" ] 2>/dev/null; then
        age="$(( now_epoch - last_notice_epoch ))"
        if [ "${age}" -lt "${_STARTUP_NOTICE_COOLDOWN_SECONDS}" ]; then
            should_notify="no"
        fi
    fi

    if [ "${should_notify}" != "yes" ]; then
        echo "[startup] Startup notification suppressed (cooldown active)"
        exit 0
    fi

    mkdir -p "$(dirname "${_STARTUP_NOTICE_STAMP}")" 2>/dev/null || true
    printf '%s\n' "${now_epoch}" > "${_STARTUP_NOTICE_STAMP}" 2>/dev/null || true
    _telegram_send "🟡 OpenClaw starting" \
        && echo "[startup] ✓ Sent Telegram starting notification" \
        || echo "[startup] ⚠ Could not send Telegram starting notification"
    _slack_send "OpenClaw starting" || true

    # Poll OpenClaw HTTP endpoint and Telegram/model readiness — up to 120s
    ready="no"
    for _i in $(seq 1 60); do
        _http_ok=0
        _tg_ok=0
        _model_ok=0
        curl -sf http://localhost:18789/ >/dev/null 2>&1 && _http_ok=1
        _telegram_get_me_ready && _tg_ok=1
        _model_runtime_ready && _model_ok=1
        if [ "${_http_ok}" = "1" ] && [ "${_tg_ok}" = "1" ] && [ "${_model_ok}" = "1" ]; then
            ready="yes"
            break
        fi
        sleep 2
    done

    echo "[startup] Readiness result: ready=${ready}"

    if [ "${ready}" = "yes" ]; then
        # Gateway is confirmed responsive — safe to query/edit live cron jobs now.
        _reconcile_security_critical_cron

        # Give the Telegram provider a moment to finish initialising before the photo upload
        sleep 5
        _photo_sent="no"
        for _attempt in 1 2 3; do
            echo "[startup] Photo attempt ${_attempt}/3..."
            # Instance label dropped 2026-08-27 (owner request): match Hermes's
            # plain "🛡️ Hermes online" style.
            if _telegram_send_photo "🛡️ OpenClaw online" "/app/branding/logo.png"; then
                echo "[startup] ✓ Sent Telegram startup photo notification"
                _photo_sent="yes"
                break
            fi
            echo "[startup] ⚠ Photo attempt ${_attempt}/3 failed — retrying in 5s"
            sleep 5
        done
        if [ "${_photo_sent}" != "yes" ]; then
            echo "[startup] Falling back to text notification"
            _telegram_send "🛡️ OpenClaw online" \
                && echo "[startup] ✓ Sent Telegram startup notification" \
                || echo "[startup] ⚠ Could not send Telegram startup notification"
        fi
        _slack_send "OpenClaw online" \
            && echo "[startup] ✓ Sent Slack startup notification" \
            || true
    else
        _telegram_send "🟠 OpenClaw starting (readiness delayed)" \
            && echo "[startup] ⚠ Sent delayed startup notification" \
            || echo "[startup] ⚠ Could not send delayed startup notification"
        _slack_send "OpenClaw starting (readiness delayed)" || true
    fi
) &

wait $OPENCLAW_PID
