#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
COMPOSE_FILE="${REPO_ROOT}/docker/docker-compose.yml"
MODEL_ENV_FILE="${REPO_ROOT}/docker/.env"

usage() {
  cat <<'EOF'
Usage: scripts/switch_model.sh <target> [model_ref] [--wait]

Targets:
  local       Use local Ollama model (qwen3:14b)
  local-multi Use 3 local LLMs: Anchor (LM Studio:1234) + Coding (LM Studio:1234) + Reasoning (mlx_lm:8234)
  gemini      Use Google Gemini cloud model (gemini-2.5-flash)
  anthropic   Use Anthropic cloud model (claude-opus-4-6)
  openai      Use OpenAI cloud model (gpt-4o-mini)

Examples:
  scripts/switch_model.sh local
  scripts/switch_model.sh local qwen3:14b
  scripts/switch_model.sh local qwen3:14b --wait
  scripts/switch_model.sh local-multi
  scripts/switch_model.sh gemini
  scripts/switch_model.sh openai openai/gpt-4.1-mini
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

if [[ $# -lt 1 || $# -gt 3 ]]; then
  usage
  exit 2
fi

TARGET="$(echo "$1" | tr '[:upper:]' '[:lower:]')"
CUSTOM_MODEL_REF="${2:-}"
WAIT_FOR_MODEL="false"
if [[ "${3:-}" == "--wait" ]] || [[ "${2:-}" == "--wait" ]]; then
  WAIT_FOR_MODEL="true"
  if [[ "${2:-}" == "--wait" ]]; then
    CUSTOM_MODEL_REF=""
  fi
fi
MODEL_MODE="local"
LOCAL_REF="ollama/qwen3:14b"
CLOUD_REF="anthropic/claude-opus-4-6"
OPENCLAW_MAIN_MODEL=""
LOCAL_MODEL_NAME="qwen3:14b"
OLLAMA_PROVIDER_API="ollama"  # overridden to openai-completions for local-multi below
LMSTUDIO_API_BASE="${LMSTUDIO_API_BASE:-http://host.docker.internal:1234}"
MLXLM_API_BASE="${MLXLM_API_BASE:-http://host.docker.internal:8234}"
ANCHOR_MODEL="${AGENTSHROUD_ANCHOR_MODEL:-qwen3.6-27b}"
CODING_MODEL="${AGENTSHROUD_CODING_MODEL:-qwen2.5-coder:32b}"

case "$TARGET" in
  local)
    MODEL_MODE="local"
    LOCAL_REF="ollama/qwen3:14b"
    CLOUD_REF="anthropic/claude-opus-4-6"
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
  local-multi)
    MODEL_MODE="local-multi"
    # All models route through gateway to LM Studio (OpenAI-compatible).
    # Provider key is "openai-local" to avoid Ollama stream parser.
    LOCAL_REF="openai-local/${ANCHOR_MODEL}"
    OPENCLAW_MAIN_MODEL="openai-local/${ANCHOR_MODEL}"
    LOCAL_MODEL_NAME="${ANCHOR_MODEL}"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      LOCAL_MODEL_NAME="${CUSTOM_MODEL_REF#*/}"  # strip any provider/ prefix
      LOCAL_REF="openai-local/${LOCAL_MODEL_NAME}"
      OPENCLAW_MAIN_MODEL="${LOCAL_REF}"
    fi
    # LM Studio speaks OpenAI format, not Ollama native format.
    OLLAMA_PROVIDER_API="openai-completions"
    ;;
  gemini)
    MODEL_MODE="cloud"
    CLOUD_REF="google/gemini-2.5-flash"
    OPENCLAW_MAIN_MODEL="google/gemini-2.5-flash"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "google" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  anthropic)
    MODEL_MODE="cloud"
    CLOUD_REF="anthropic/claude-opus-4-6"
    OPENCLAW_MAIN_MODEL="anthropic/claude-opus-4-6"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "anthropic" "${CUSTOM_MODEL_REF}")"
      OPENCLAW_MAIN_MODEL="${CLOUD_REF}"
    fi
    ;;
  openai)
    MODEL_MODE="cloud"
    CLOUD_REF="openai/gpt-4o-mini"
    OPENCLAW_MAIN_MODEL="openai/gpt-4o-mini"
    if [[ -n "${CUSTOM_MODEL_REF}" ]]; then
      CLOUD_REF="$(normalize_cloud_ref "openai" "${CUSTOM_MODEL_REF}")"
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

if [[ "${MODEL_MODE}" == "local" ]]; then
  ensure_local_model_available "${LOCAL_MODEL_NAME}"
elif [[ "${MODEL_MODE}" == "local-multi" ]]; then
  echo "[switch-model] local-multi: verify LM Studio is running on ${LMSTUDIO_API_BASE} and mlx_lm on ${MLXLM_API_BASE}"
fi

echo "[switch-model] target=${TARGET} mode=${MODEL_MODE} model=${OPENCLAW_MAIN_MODEL}"

touch "${MODEL_ENV_FILE}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_MODEL_MODE" "${MODEL_MODE}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_LOCAL_MODEL_REF" "${LOCAL_REF}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_CLOUD_MODEL_REF" "${CLOUD_REF}"
upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_LOCAL_MODEL" "${LOCAL_MODEL_NAME}"
upsert_env_value "${MODEL_ENV_FILE}" "OPENCLAW_MAIN_MODEL" "${OPENCLAW_MAIN_MODEL}"
upsert_env_value "${MODEL_ENV_FILE}" "OPENCLAW_OLLAMA_API" "${OLLAMA_PROVIDER_API}"
if [[ "${MODEL_MODE}" == "local" ]]; then
  upsert_env_value "${MODEL_ENV_FILE}" "OLLAMA_API_KEY" "${OLLAMA_API_KEY:-ollama-local}"
fi
if [[ "${MODEL_MODE}" == "local-multi" ]]; then
  upsert_env_value "${MODEL_ENV_FILE}" "LMSTUDIO_API_BASE" "${LMSTUDIO_API_BASE}"
  upsert_env_value "${MODEL_ENV_FILE}" "MLXLM_API_BASE" "${MLXLM_API_BASE}"
  upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_ANCHOR_MODEL" "${ANCHOR_MODEL}"
  upsert_env_value "${MODEL_ENV_FILE}" "AGENTSHROUD_CODING_MODEL" "${CODING_MODEL}"
fi
echo "[switch-model] persisted model profile to ${MODEL_ENV_FILE}"

cd "${REPO_ROOT}"
AGENTSHROUD_MODEL_MODE="${MODEL_MODE}" \
AGENTSHROUD_LOCAL_MODEL_REF="${LOCAL_REF}" \
AGENTSHROUD_CLOUD_MODEL_REF="${CLOUD_REF}" \
AGENTSHROUD_LOCAL_MODEL="${LOCAL_MODEL_NAME}" \
OPENCLAW_MAIN_MODEL="${OPENCLAW_MAIN_MODEL}" \
OPENCLAW_OLLAMA_API="${OLLAMA_PROVIDER_API}" \
OLLAMA_API_KEY="${OLLAMA_API_KEY:-ollama-local}" \
LMSTUDIO_API_BASE="${LMSTUDIO_API_BASE}" \
MLXLM_API_BASE="${MLXLM_API_BASE}" \
AGENTSHROUD_ANCHOR_MODEL="${ANCHOR_MODEL}" \
AGENTSHROUD_CODING_MODEL="${CODING_MODEL}" \
OPENCLAW_GATEWAY_BIND="${OPENCLAW_GATEWAY_BIND:-lan}" \
docker compose -f "${COMPOSE_FILE}" up -d --force-recreate gateway bot

echo "[switch-model] complete"
