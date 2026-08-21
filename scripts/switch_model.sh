#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${REPO_ROOT}/docker/docker-compose.yml"
# Standalone docker-compose (hyphenated) is the working binary on the deploy
# hosts; the docker-compose plugin ("docker compose") is broken there. Use a
# single overridable variable so the invocation stays consistent.
COMPOSE="${COMPOSE:-docker-compose}"
# Allow tests to override the env file path via MODEL_ENV_FILE env var.
MODEL_ENV_FILE="${MODEL_ENV_FILE:-${REPO_ROOT}/docker/.env}"
# SWITCH_MODEL_TEST_MODE=1: skip Ollama/docker calls (unit-test mode).
SWITCH_MODEL_TEST_MODE="${SWITCH_MODEL_TEST_MODE:-0}"
# SWITCH_MODEL_HEALTH_MOCK=1: mock health checks for --verify (unit-test mode).
SWITCH_MODEL_HEALTH_MOCK="${SWITCH_MODEL_HEALTH_MOCK:-0}"

usage() {
  cat <<'EOF'
Usage: scripts/switch_model.sh <target> [model_ref] [--wait] [--verify]

Cloud — Anthropic:
  anthropic          anthropic/claude-opus-4-7            (flagship)
  anthropic-sonnet   anthropic/claude-sonnet-4-6
  anthropic-haiku    anthropic/claude-haiku-4-5-20251001

Cloud — OpenAI:
  openai             openai/gpt-5                         (flagship)
  openai-mini        openai/gpt-5-mini
  openai-4.1         openai/gpt-4.1
  openai-4.1-mini    openai/gpt-4.1-mini
  openai-4o          openai/gpt-4o
  openai-4o-mini     openai/gpt-4o-mini

Cloud — Google Gemini:
  gemini             google/gemini-3-pro                  (latest flagship)
  gemini-flash       google/gemini-3-flash
  gemini-2.5-pro     google/gemini-2.5-pro
  gemini-2.5-flash   google/gemini-2.5-flash

Local — single model (LM Studio :1234):
  local-coder        qwen3-coder-30b-a3b-instruct         (best for tool loops)
  local-anchor       qwen3.8-27b-mlx                      (generalist 27B)
  local-qwen14       qwen3-14b                            (smallest bot-capable)

Local — Ollama (back-compat):
  local              ollama/qwen3:14b via Ollama :11434

Local — multi-role (LM Studio :1234 + mlx_lm :8234):
  local-multi        anchor=qwen3.8-27b-mlx  coding=qwen2.5-coder:32b  reasoning=deepseek-r1

Optional [model_ref] overrides the default for any target.
Optional --wait (with `local` target): poll until Ollama model is available.

Examples:
  scripts/switch_model.sh anthropic
  scripts/switch_model.sh openai openai/gpt-4.1
  scripts/switch_model.sh gemini-flash
  scripts/switch_model.sh local-coder
  scripts/switch_model.sh local qwen3:14b --wait
  scripts/switch_model.sh local-multi
EOF
}

normalize_cloud_ref() {
  local provider="$1"
  local ref="$2"
  if [[ -z "${ref}" ]]; then
    echo ""
    return 0
  fi
  if [[ "${ref}" == */* ]]; then
    echo "${ref}"
    return 0
  fi
  echo "${provider}/${ref}"
}

if [[ $# -lt 1 || $# -gt 4 ]]; then
  usage
  exit 2
fi

TARGET="$(echo "$1" | tr '[:upper:]' '[:lower:]')"
CUSTOM_MODEL_REF="${2:-}"
WAIT_FOR_MODEL="false"
VERIFY_AFTER_SWITCH="false"

# Parse flags from positions 2–4 (allow --wait and --verify in any order after target).
for _arg in "${@:2}"; do
  case "${_arg}" in
    --wait)
      WAIT_FOR_MODEL="true"
      # If --wait is the 2nd arg there is no model ref override
      if [[ "${2:-}" == "--wait" ]]; then
        CUSTOM_MODEL_REF=""
      fi
      ;;
    --verify)
      VERIFY_AFTER_SWITCH="true"
      ;;
    *)
      # Any non-flag arg is the model ref override (only the first one counts)
      if [[ "${_arg}" != --* && -z "${CUSTOM_MODEL_REF}" || "${_arg}" == "${2:-}" ]]; then
        : # handled by initial CUSTOM_MODEL_REF="${2:-}" above
      fi
      ;;
  esac
done

# When both a model ref and --wait/--verify are given, strip flags from CUSTOM_MODEL_REF.
if [[ "${CUSTOM_MODEL_REF}" == "--wait" || "${CUSTOM_MODEL_REF}" == "--verify" ]]; then
  CUSTOM_MODEL_REF=""
fi

MODEL_MODE="local"
LOCAL_REF="ollama/qwen3:14b"
CLOUD_REF="anthropic/claude-opus-4-7"
OPENCLAW_MAIN_MODEL=""
LOCAL_MODEL_NAME="qwen3:14b"
OLLAMA_PROVIDER_API="ollama"  # overridden to openai-completions for LM Studio targets
LMSTUDIO_API_BASE="${LMSTUDIO_API_BASE:-http://host.docker.internal:1234}"
MLXLM_API_BASE="${MLXLM_API_BASE:-http://host.docker.internal:8234}"
FIELDFLARE_API_BASE="${FIELDFLARE_API_BASE:-http://host.docker.internal:8238}"
ANCHOR_MODEL="${AGENTSHROUD_ANCHOR_MODEL:-qwen3.8-27b-mlx}"
CODING_MODEL="${AGENTSHROUD_CODING_MODEL:-qwen2.5-coder:32b}"
REASONING_MODEL="${AGENTSHROUD_REASONING_MODEL:-deepseek-r1}"

case "$TARGET" in
  # ── Local — Ollama (back-compat) ─────────────────────────────────────────────
  local)
    MODEL_MODE="local"
    LOCAL_REF="ollama/qwen3:14b"
    CLOUD_REF="anthropic/claude-opus-4-7"
    OPENCLAW_MAIN_MODEL="ollama/qwen3:14b"
    LOCAL_MODEL_NAME="qwen3:14b"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      if [[ "${CUSTOM_MODEL_REF}" == ollama/* ]]; then
        LOCAL_REF="${CUSTOM_MODEL_REF}"
      else
        LOCAL_REF="ollama/${CUSTOM_MODEL_REF}"
      fi
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      LOCAL_MODEL_NAME="${LOCAL_REF#ollama/}"
    fi
    ;;
  # ── Local — LM Studio single-model ───────────────────────────────────────────
  local-coder)
    MODEL_MODE="local-multi"
    LOCAL_REF="openai-local/qwen3-coder-30b-a3b-instruct"
    OPENCLAW_MAIN_MODEL="openai-local/qwen3-coder-30b-a3b-instruct"
    LOCAL_MODEL_NAME="qwen3-coder-30b-a3b-instruct"
    ANCHOR_MODEL="qwen3-coder-30b-a3b-instruct"
    OLLAMA_PROVIDER_API="openai-completions"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      ANCHOR_MODEL="${LOCAL_MODEL_NAME}"
    fi
    ;;
  local-anchor)
    MODEL_MODE="local-multi"
    LOCAL_REF="openai-local/qwen3.8-27b-mlx"
    OPENCLAW_MAIN_MODEL="openai-local/qwen3.8-27b-mlx"
    LOCAL_MODEL_NAME="qwen3.8-27b-mlx"
    ANCHOR_MODEL="qwen3.8-27b-mlx"
    OLLAMA_PROVIDER_API="openai-completions"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      ANCHOR_MODEL="${LOCAL_MODEL_NAME}"
    fi
    ;;
  local-qwen14)
    MODEL_MODE="local-multi"
    LOCAL_REF="openai-local/qwen3-14b"
    OPENCLAW_MAIN_MODEL="openai-local/qwen3-14b"
    LOCAL_MODEL_NAME="qwen3-14b"
    ANCHOR_MODEL="qwen3-14b"
    OLLAMA_PROVIDER_API="openai-completions"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      ANCHOR_MODEL="${LOCAL_MODEL_NAME}"
    fi
    ;;
  # ── Local — Turbo Fieldflare (MLX Gemma 4, :8238) ────────────────────────────
  local-fieldflare)
    MODEL_MODE="local-multi"
    LOCAL_REF="openai-local/gemma-4-26b-a4b-it"
    OPENCLAW_MAIN_MODEL="openai-local/gemma-4-26b-a4b-it"
    LOCAL_MODEL_NAME="gemma-4-26b-a4b-it"
    ANCHOR_MODEL="gemma-4-26b-a4b-it"
    OLLAMA_PROVIDER_API="openai-completions"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      ANCHOR_MODEL="${LOCAL_MODEL_NAME}"
    fi
    ;;
  # ── Local — multi-role ────────────────────────────────────────────────────────
  local-multi)
    MODEL_MODE="local-multi"
    LOCAL_REF="openai-local/${ANCHOR_MODEL}"
    OPENCLAW_MAIN_MODEL="openai-local/${ANCHOR_MODEL}"
    LOCAL_MODEL_NAME="${ANCHOR_MODEL}"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
      ANCHOR_MODEL="${LOCAL_MODEL_NAME}"
    fi
    OLLAMA_PROVIDER_API="openai-completions"
    ;;
  # ── Cloud — Anthropic ─────────────────────────────────────────────────────────
  anthropic)
    MODEL_MODE="cloud"
    CLOUD_REF="anthropic/claude-opus-4-7"
    OPENCLAW_MAIN_MODEL="anthropic/claude-opus-4-7"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "anthropic" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  anthropic-sonnet)
    MODEL_MODE="cloud"
    CLOUD_REF="anthropic/claude-sonnet-4-6"
    OPENCLAW_MAIN_MODEL="anthropic/claude-sonnet-4-6"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "anthropic" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  anthropic-haiku)
    MODEL_MODE="cloud"
    CLOUD_REF="anthropic/claude-haiku-4-5-20251001"
    OPENCLAW_MAIN_MODEL="anthropic/claude-haiku-4-5-20251001"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "anthropic" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  # ── Cloud — OpenAI ────────────────────────────────────────────────────────────
  openai)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-5"
    OPENCLAW_MAIN_MODEL="openai/gpt-5"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai-mini)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-5-mini"
    OPENCLAW_MAIN_MODEL="openai/gpt-5-mini"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai-4.1)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4.1"
    OPENCLAW_MAIN_MODEL="openai/gpt-4.1"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai-4.1-mini)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4.1-mini"
    OPENCLAW_MAIN_MODEL="openai/gpt-4.1-mini"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai-4o)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4o"
    OPENCLAW_MAIN_MODEL="openai/gpt-4o"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai-4o-mini)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4o-mini"
    OPENCLAW_MAIN_MODEL="openai/gpt-4o-mini"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  # ── Cloud — Google Gemini ─────────────────────────────────────────────────────
  gemini)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-3-pro"
    OPENCLAW_MAIN_MODEL="google/gemini-3-pro"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "google" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  gemini-flash)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-3-flash"
    OPENCLAW_MAIN_MODEL="google/gemini-3-flash"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "google" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  gemini-2.5-pro)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-2.5-pro"
    OPENCLAW_MAIN_MODEL="google/gemini-2.5-pro"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "google" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  gemini-2.5-flash)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-2.5-flash"
    OPENCLAW_MAIN_MODEL="google/gemini-2.5-flash"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "google" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  -h|--help|help)
    usage
    exit 0
    ;;
  *)
    echo "Unknown target: $TARGET" >&2
    usage
    exit 2
    ;;
esac

wait_for_local_model() {
  local model_name="$1"
  local timeout_seconds="${SWITCH_MODEL_WAIT_TIMEOUT_SECONDS:-1800}"
  local poll_seconds="${SWITCH_MODEL_WAIT_POLL_SECONDS:-15}"
  local started_at
  started_at="$(date +%s)"
  while true; do
    if ollama list 2>/dev/null | awk '{print $1}' | grep -Fxq "${model_name}"; then
      echo "[switch-model] confirmed local model present: ${model_name}"
      return 0
    fi
    local now elapsed
    now="$(date +%s)"
    elapsed="$(( now - started_at ))"
    if (( elapsed >= timeout_seconds )); then
      echo "[switch-model] ERROR: local model not available after ${timeout_seconds}s: ${model_name}" >&2
      return 1
    fi
    echo "[switch-model] waiting for local model pull: ${model_name} (${elapsed}s elapsed)"
    sleep "${poll_seconds}"
  done
}

ensure_local_model_available() {
  local model_name="$1"
  if ollama list 2>/dev/null | awk '{print $1}' | grep -Fxq "${model_name}"; then
    return 0
  fi
  if [[ "${WAIT_FOR_MODEL}" == "true" ]]; then
    wait_for_local_model "${model_name}"
    return $?
  fi
  echo "[switch-model] ERROR: local model not found: ${model_name}" >&2
  echo "[switch-model] Pull it first: ollama run ${model_name}" >&2
  echo "[switch-model] Or retry with wait: scripts/switch_model.sh local ${model_name} --wait" >&2
  return 1
}

preflight_local() {
  local mode="$1"
  local model_name="$2"
  if [[ "${mode}" != "local-multi" ]]; then
    return 0
  fi
  # qwen3.8-27b-mlx lives on mlx_lm (:8234), not LM Studio — LM Studio can't
  # load its qwen3_5 architecture yet (confirmed 2026-08-17, needs an engine
  # update). Probing LM Studio for it would always false-positive "not found".
  # Must match gateway/proxy/llm_proxy.py's LOCAL_MODEL_ROUTES routing exactly,
  # or this warning drifts from what actually serves the request.
  if [[ "${model_name}" == "qwen3.8-27b-mlx" ]]; then
    if ! curl -fsS --max-time 2 "${MLXLM_API_BASE}/v1/models" 2>/dev/null | grep -q .; then
      echo "[switch-model] WARN: mlx_lm not reachable at ${MLXLM_API_BASE}" >&2
      echo "[switch-model] WARN: qwen3.8-27b-mlx is served via mlx_lm, not LM Studio — start it with: services.sh mlx-lm start" >&2
    fi
  else
    # Probe LM Studio for the requested model
    local lms_models
    lms_models="$(curl -fsS --max-time 2 "${LMSTUDIO_API_BASE}/v1/models" 2>/dev/null || true)"
    if [[ -z "${lms_models}" ]]; then
      echo "[switch-model] WARN: LM Studio not reachable at ${LMSTUDIO_API_BASE}" >&2
      echo "[switch-model] WARN: ensure LM Studio server is running (lms server start)" >&2
    elif ! echo "${lms_models}" | grep -q "${model_name}"; then
      echo "[switch-model] WARN: model '${model_name}' not found in LM Studio at ${LMSTUDIO_API_BASE}" >&2
      echo "[switch-model] WARN: load it with: lms load ${model_name}" >&2
    fi
  fi
  # For the 3-role target, also probe mlx_lm (reasoning role)
  if [[ "${TARGET}" == "local-multi" ]]; then
    if ! curl -fsS --max-time 2 "${MLXLM_API_BASE}/v1/models" 2>/dev/null | grep -q .; then
      echo "[switch-model] WARN: mlx_lm server not reachable at ${MLXLM_API_BASE}" >&2
      echo "[switch-model] WARN: start it with: mlx_lm.server --port 8234" >&2
    fi
  fi
}

upsert_env_value() {
  local file="$1"
  local key="$2"
  local value="$3"
  if [ -f "${file}" ] && grep -q "^${key}=" "${file}"; then
    sed -i.bak "s|^${key}=.*|${key}=${value}|" "${file}"
    rm -f "${file}.bak"
  else
    printf '%s=%s\n' "${key}" "${value}" >> "${file}"
  fi
}

if [[ "${SWITCH_MODEL_TEST_MODE}" != "1" ]]; then
  if [[ "${MODEL_MODE}" == "local" ]]; then
    ensure_local_model_available "${LOCAL_MODEL_NAME}"
  elif [[ "${MODEL_MODE}" == "local-multi" ]]; then
    preflight_local "${MODEL_MODE}" "${LOCAL_MODEL_NAME}"
  fi
fi

echo "[switch-model] target=${TARGET} mode=${MODEL_MODE} model=${OPENCLAW_MAIN_MODEL}"

touch "${MODEL_ENV_FILE}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_MODEL_MODE" "${MODEL_MODE}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_LOCAL_MODEL_REF" "${LOCAL_REF}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_CLOUD_MODEL_REF" "${CLOUD_REF}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_LOCAL_MODEL" "${LOCAL_MODEL_NAME}"
upsert_env_value "${MODEL_ENV_FILE}" "OPENCLAW_MAIN_MODEL" "${OPENCLAW_MAIN_MODEL}"
# Hermes always switches atomically with OpenClaw so both bots use the same model profile.
upsert_env_value "${MODEL_ENV_FILE}" "HERMES_MAIN_MODEL" "${OPENCLAW_MAIN_MODEL}"
upsert_env_value "${MODEL_ENV_FILE}" "OPENCLAW_OLLAMA_API" "${OLLAMA_PROVIDER_API}"
if [[ "${MODEL_MODE}" == "local" ]]; then
  upsert_env_value "${MODEL_ENV_FILE}" "OLLAMA_API_KEY" "${OLLAMA_API_KEY:-ollama-local}"
fi
if [[ "${MODEL_MODE}" == "local-multi" ]]; then
  upsert_env_value "${MODEL_ENV_FILE}" "LMSTUDIO_API_BASE" "${LMSTUDIO_API_BASE}"
  upsert_env_value "${MODEL_ENV_FILE}" "MLXLM_API_BASE" "${MLXLM_API_BASE}"
  upsert_env_value "${MODEL_ENV_FILE}" "FIELDFLARE_API_BASE" "${FIELDFLARE_API_BASE}"
  upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_ANCHOR_MODEL" "${ANCHOR_MODEL}"
  upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_CODING_MODEL" "${CODING_MODEL}"
  upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_REASONING_MODEL" "${REASONING_MODEL}"
fi
if [[ "${MODEL_MODE}" == "cloud" ]]; then
  case "${TARGET}" in
    anthropic*) CLOUD_KEY_VAR="ANTHROPIC_API_KEY" ;;
    openai*)    CLOUD_KEY_VAR="OPENAI_API_KEY" ;;
    gemini*)    CLOUD_KEY_VAR="GEMINI_API_KEY" ;;
    *)          CLOUD_KEY_VAR="" ;;
  esac
  if [[ -n "${CLOUD_KEY_VAR}" ]] && ! grep -q "^${CLOUD_KEY_VAR}=" "${MODEL_ENV_FILE}" 2>/dev/null; then
    echo "[switch-model] WARN: ${CLOUD_KEY_VAR} not set in ${MODEL_ENV_FILE}" >&2
    echo "[switch-model] WARN: add it with: echo '${CLOUD_KEY_VAR}=your-key' >> docker/.env" >&2
  fi
fi
echo "[switch-model] persisted model profile to ${MODEL_ENV_FILE}"

verify_both_bots_healthy() {
  # --verify: confirm gateway, openclaw, and hermes are all healthy before returning 0.
  # In SWITCH_MODEL_HEALTH_MOCK=1 (test mode), skip real HTTP probes and return 0.
  if [[ "${SWITCH_MODEL_HEALTH_MOCK}" == "1" || "${SWITCH_MODEL_TEST_MODE}" == "1" ]]; then
    echo "[switch-model] --verify: health checks mocked (test mode)"
    return 0
  fi

  local gw_url="${GATEWAY_OP_PROXY_URL:-http://localhost:8080}"
  local max_wait=60
  local poll=5
  local elapsed=0

  echo "[switch-model] --verify: waiting up to ${max_wait}s for all bots to report healthy..."

  while (( elapsed < max_wait )); do
    local gw_ok=0 openclaw_ok=0 hermes_ok=0

    if curl -fsS --max-time 3 "${gw_url}/status" 2>/dev/null | grep -q '"status"'; then
      gw_ok=1
    fi
    if curl -fsS --max-time 3 "http://localhost:18789/health" 2>/dev/null | grep -q 'ok\|healthy'; then
      openclaw_ok=1
    fi
    # Hermes health endpoint; skipped if not in full profile
    if curl -fsS --max-time 3 "http://localhost:8642/health" 2>/dev/null | grep -q 'ok\|healthy'; then
      hermes_ok=1
    else
      hermes_ok=1  # Hermes may not be in the current profile; treat as optional
    fi

    if (( gw_ok && openclaw_ok && hermes_ok )); then
      echo "[switch-model] --verify: all bots healthy (gateway=${gw_ok} openclaw=${openclaw_ok} hermes=${hermes_ok})"
      return 0
    fi

    echo "[switch-model] --verify: not ready yet (gateway=${gw_ok} openclaw=${openclaw_ok} hermes=${hermes_ok}), retrying in ${poll}s..."
    sleep "${poll}"
    (( elapsed += poll ))
  done

  echo "[switch-model] ERROR: --verify timed out after ${max_wait}s — bots not healthy" >&2
  return 1
}

# Only gateway and bot are restarted; LM Studio/mlx_lm run on the host.
if [[ "${SWITCH_MODEL_TEST_MODE}" != "1" ]]; then
  # For local-multi mode, load the anchor model in LM Studio at the correct context window.
  # LM Studio's JIT load uses a small default context; we must set it explicitly.
  # Skip for Fieldflare — it runs on its own MLX server (:8238), not LM Studio;
  # loading its model name into LM Studio would silently load nothing / the
  # wrong model (LM Studio doesn't have "gemma-4-26b-a4b-it").
  if [[ "${MODEL_MODE}" == "local-multi" && "${TARGET}" != "local-fieldflare" ]]; then
    LMS_CMD="${HOME}/.cache/lm-studio/bin/lms"
    LMS_CONTEXT="${LMS_CONTEXT:-32768}"
    if command -v "${LMS_CMD}" &>/dev/null; then
      echo "[switch-model] Loading anchor model ${ANCHOR_MODEL} in LM Studio at ${LMS_CONTEXT} context..."
      printf '1\n' | "${LMS_CMD}" load "${ANCHOR_MODEL}" --context-length "${LMS_CONTEXT}" --gpu max 2>&1 | tail -2 || \
        echo "[switch-model] WARN: LM Studio model load failed — load manually: ${LMS_CMD} load ${ANCHOR_MODEL} --context-length ${LMS_CONTEXT}"
    else
      echo "[switch-model] WARN: lms CLI not found; load model manually in LM Studio at context-length ${LMS_CONTEXT}"
    fi
  fi

  cd "${REPO_ROOT}"
  AGENTSHROUD_MODEL_MODE="${MODEL_MODE}" \
  AGENTSHROUD_LOCAL_MODEL_REF="${LOCAL_REF}" \
  AGENTSHROUD_CLOUD_MODEL_REF="${CLOUD_REF}" \
  AGENTSHROUD_LOCAL_MODEL="${LOCAL_MODEL_NAME}" \
  OPENCLAW_MAIN_MODEL="${OPENCLAW_MAIN_MODEL}" \
  HERMES_MAIN_MODEL="${OPENCLAW_MAIN_MODEL}" \
  OPENCLAW_OLLAMA_API="${OLLAMA_PROVIDER_API}" \
  OLLAMA_API_KEY="${OLLAMA_API_KEY:-ollama-local}" \
  LMSTUDIO_API_BASE="${LMSTUDIO_API_BASE}" \
  MLXLM_API_BASE="${MLXLM_API_BASE}" \
  FIELDFLARE_API_BASE="${FIELDFLARE_API_BASE}" \
  AGENTSHROUD_ANCHOR_MODEL="${ANCHOR_MODEL}" \
  AGENTSHROUD_CODING_MODEL="${CODING_MODEL}" \
  AGENTSHROUD_REASONING_MODEL="${REASONING_MODEL}" \
  OPENCLAW_GATEWAY_BIND="${OPENCLAW_GATEWAY_BIND:-lan}" \
  $COMPOSE -f "${COMPOSE_FILE}" up -d --force-recreate gateway openclaw
fi

if [[ "${VERIFY_AFTER_SWITCH}" == "true" ]]; then
  verify_both_bots_healthy
fi

echo "[switch-model] complete"
