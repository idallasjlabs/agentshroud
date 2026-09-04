#!/usr/bin/env bash
# Smoke test: for every local AGENTSHROUD_MODEL_MODE, OpenClaw's resulting
# main-model reference (config.agents.defaults.model.primary) must resolve
# to a provider that apply-patches.js actually registers under
# config.models.providers.
#
# A mismatch (e.g. primary model "openai-local/x" but only "ollama"
# registered under config.models.providers, because AGENTSHROUD_MODEL_MODE
# is "local" not "local-multi") makes OpenClaw reject every job with
# "FailoverError: Unknown model: openai-local/x" — which in turn floods the
# startup readiness check with retry churn, so OpenClaw never sends its
# "online" + photo notification and silently degrades to "readiness
# delayed" on every restart. Incident: 2026-09-04 — docker-compose.yml's
# openclaw service defaults AGENTSHROUD_LOCAL_MODEL_REF to
# "openai-local/nemotron-3.5-lightning-rapid", but the deployment actually
# runs AGENTSHROUD_MODEL_MODE=local (set at the container's runtime
# environment, outside this repo), under which only "ollama" gets
# registered — the two diverged. AGENTSHROUD_MODEL_MODE=cloud (compose's own
# default) does not exercise this: it routes to AGENTSHROUD_CLOUD_MODEL_REF
# instead, so this test targets the "local" / "local-multi" modes directly
# rather than whatever compose's own top-level default happens to be.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMPOSE="$REPO/docker/docker-compose.yml"
TMP_CONFIG="$(mktemp -u)"
trap 'rm -f "$TMP_CONFIG"' EXIT

echo ""
echo "── OpenClaw model/provider consistency ─────────────────"

# Isolate the openclaw: service block (between its header and the next
# top-level service key) and pull its actual compose-file defaults for the
# local-model ref/name, so this test tracks docker-compose.yml rather than a
# value hardcoded here.
block="$(awk '/^  openclaw:$/{flag=1; next} /^  [a-zA-Z0-9_-]+:$/{flag=0} flag' "$COMPOSE")"

extract_default() {
    local var="$1"
    echo "$block" | grep -oE "${var}:-[^}]+" | head -1 | sed -E "s/^${var}:-//"
}

local_model_ref="$(extract_default AGENTSHROUD_LOCAL_MODEL_REF)"
local_model="$(extract_default AGENTSHROUD_LOCAL_MODEL)"

if [ -z "$local_model_ref" ]; then
    echo "  FAIL: could not extract AGENTSHROUD_LOCAL_MODEL_REF default from openclaw: block in $COMPOSE" >&2
    exit 1
fi
echo "  compose defaults: AGENTSHROUD_LOCAL_MODEL_REF=$local_model_ref AGENTSHROUD_LOCAL_MODEL=$local_model"

fail=0
for mode in local local-multi; do
    rm -f "$TMP_CONFIG"
    AGENTSHROUD_MODEL_MODE="$mode" \
    AGENTSHROUD_LOCAL_MODEL_REF="$local_model_ref" \
    AGENTSHROUD_LOCAL_MODEL="$local_model" \
    node "$REPO/docker/config/openclaw/apply-patches.js" "$TMP_CONFIG" >/dev/null

    primary="$(node -e "console.log(JSON.parse(require('fs').readFileSync(process.argv[1],'utf8')).agents.defaults.model.primary)" "$TMP_CONFIG")"
    provider="${primary%%/*}"

    if node -e "
      const cfg = JSON.parse(require('fs').readFileSync(process.argv[1], 'utf8'));
      process.exit(cfg.models && cfg.models.providers && cfg.models.providers[process.argv[2]] ? 0 : 1);
    " "$TMP_CONFIG" "$provider"; then
        echo "  OK : mode=$mode primary='$primary' — provider '$provider' is registered in config.models.providers"
    else
        echo "  FAIL: mode=$mode primary='$primary' references provider '$provider', but config.models.providers has no '$provider' entry — every OpenClaw job will fail with FailoverError: Unknown model" >&2
        fail=1
    fi
done

exit "$fail"
