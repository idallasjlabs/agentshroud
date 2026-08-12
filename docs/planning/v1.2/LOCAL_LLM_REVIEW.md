# Local LLM Support — Implementation Review

> **Status:** v1.2.0 milestone — 3 commits shipped on `feat-v1.2.0-local-llms`
> **Last reviewed:** 2026-08-12 — added Turbo Fieldflare as the default local backend
> **Purpose:** Compile all context before proceeding with further local LLM work.

---

## 1. Architecture Overview

All LLM traffic — cloud and local — passes through a single choke point:

```
OpenClaw bot → gateway:8080/v1 → LLMProxy → Ollama :11434
                                           → LM Studio :1234
                                           → mlx_lm :8234
                                           → Turbo Fieldflare :8238
                                           → Anthropic API
                                           → OpenAI API
                                           → Google API
```

- **Bot never talks to Ollama directly.** `OLLAMA_BASE_URL=http://gateway:8080/v1` means all requests go through the gateway's security pipeline first (PII redaction, injection defense, credential blocking, audit log).
- **Ollama runs on the host machine**, not in a container. Gateway reaches it via `host.docker.internal:11434`.
- No separate Ollama service in `docker-compose.yml`.

---

## 2. Source Files

| File | Role |
|------|------|
| `gateway/proxy/llm_proxy.py` | Central routing engine — provider detection, model interception, prefix stripping, backend URL resolution |
| `scripts/switch_model.sh` | CLI to switch model at runtime; persists to `docker/.env`; force-recreates gateway + bot |
| `docker/docker-compose.yml:73-81` | Gateway env var wiring |
| `docker/docker-compose.yml:206-216` | Bot env var wiring |
| `docker/bots/openclaw/init-config.sh` | Seeds Ollama provider into OpenClaw's `auth-profiles.json` on container start |
| `docker/bots/openclaw/start.sh` | Model mode detection + Ollama key provisioning at bot startup |
| `docker/scripts/start-agentshroud.sh` | Same model mode detection at main stack startup |
| `gateway/proxy/telegram_proxy.py` | Chat commands for local model status (`_LOCAL_MODEL_STATUS_COMMANDS`) |
| `gateway/tests/test_llm_proxy.py` | 6 unit tests covering model routing |
| `docs/setup/LLM_PROVIDER_SETUP.md` | User-facing provider setup guide |
| `docs/planning/RELEASE-PLAN.md:351-363` | v1.2.0 milestone definition |
| `agentshroud.yaml.example:138` | `default_model: "ollama/phi4:14b"` example |

---

## 3. How Provider Detection Works (`llm_proxy.py:95-153`)

Detection runs in order:

1. **Path-based:** `/api/` in path → Ollama native API
2. **Model keyword matching:** `qwen`, `llama`, `mistral`, `deepseek`, `phi`, `ollama`, `lmstudio`, `mlxlm`, `gemma`, `fieldflare`
3. **Prefix matching:** `ollama/` or `lmstudio/` prefix → local
4. **Interception:** If `MODEL_MODE != "cloud"` and model name contains `claude-opus` → force rewrite to `MAIN_MODEL`
5. **Prefix stripping:** `ollama/qwen3:14b` → `qwen3:14b` (local APIs expect bare names)
6. **Backend routing:** `LOCAL_MODEL_ROUTES` dict checked first (for non-Ollama backends), then Ollama fallback

**`LOCAL_MODEL_ROUTES` (current, `gateway/proxy/llm_proxy.py:71-78`):**
```python
LOCAL_MODEL_ROUTES = {
    "mlx-community/deepseek-r1": MLXLM_API_BASE,  # mlx-lm full-ID
    "deepseek-r1": MLXLM_API_BASE,                # Reasoning — mlx_lm :8234 (no tool calling)
    "gemma-4-26b-a4b-it": FIELDFLARE_API_BASE,     # Turbo Fieldflare — MLX Gemma 4 :8238
    "qwen3": LMSTUDIO_API_BASE,                    # Qwen3 family — LM Studio :1234
    "qwen2.5-coder": LMSTUDIO_API_BASE,            # Coding — LM Studio :1234
    "gemma": LMSTUDIO_API_BASE,                    # Other Gemma models — LM Studio :1234
}
```
Matching is **first-prefix-wins** by dict order — this is why the exact
`gemma-4-26b-a4b-it` entry must precede the generic `gemma` entry (otherwise
a Fieldflare request would incorrectly match `gemma` first and route to LM
Studio, which doesn't serve this model). Models not listed here fall through
to Ollama.

---

## 4. Environment Variables

| Variable | Default (docker-compose) | Default (code fallback) | Purpose |
|----------|--------------------------|-------------------------|---------|
| `AGENTSHROUD_MODEL_MODE` | `cloud` | `local` | `local`, `local-multi`, or `cloud` |
| `AGENTSHROUD_LOCAL_MODEL_REF` | `openai-local/gemma-4-26b-a4b-it` | — | Provider-prefixed local model ref (Turbo Fieldflare as of 2026-08) |
| `AGENTSHROUD_LOCAL_MODEL` | `gemma-4-26b-a4b-it` | `qwen2.5-coder:7b` | Bare model name used for failover dispatch |
| `AGENTSHROUD_CLOUD_MODEL_REF` | `anthropic/claude-opus-4-6` | — | Provider-prefixed cloud model ref |
| `AGENTSHROUD_ANCHOR_MODEL` | `qwen3.5:27b` | — | Anchor model (multi-mode) |
| `AGENTSHROUD_CODING_MODEL` | `qwen2.5-coder:32b` | — | Coding model (multi-mode) |
| `AGENTSHROUD_REASONING_MODEL` | `deepseek-r1` | — | Reasoning model (multi-mode, routes to mlx_lm) |
| `OPENCLAW_MAIN_MODEL` | — | — | Model ref passed to bot; set by `switch_model.sh` |
| `OLLAMA_BASE_URL` | `http://gateway:8080/v1` | — | Bot's Ollama endpoint (proxied through gateway) |
| `OLLAMA_API_KEY` | `ollama-local` | — | Auth token for Ollama provider |
| `LMSTUDIO_API_BASE` | — | `http://host.docker.internal:1234` | LM Studio endpoint |
| `MLXLM_API_BASE` | — | `http://host.docker.internal:8234` | mlx_lm endpoint |
| `FIELDFLARE_API_BASE` | `http://host.docker.internal:8238` | `http://host.docker.internal:8238` | Turbo Fieldflare endpoint (gateway service only) |

> **Note:** `docker-compose.yml` defaults `AGENTSHROUD_MODEL_MODE` to `cloud`. The code-level fallback in `llm_proxy.py:33` defaults to `local`. The compose file wins at runtime. Changing the default *model* (Ollama → Fieldflare) did **not** change this mode default — the system still runs cloud-primary (Claude) day to day; Fieldflare is what it now falls back to on manual switch or automatic quota-exhaustion failover, replacing Ollama/qwen3:14b in that role.

---

## 5. Model Switching CLI (`scripts/switch_model.sh`)

```bash
# Switch to local Ollama (qwen3:14b default)
scripts/switch_model.sh local

# Switch with a specific model (must already be pulled)
scripts/switch_model.sh local qwen3:14b

# Switch with model pull wait (polls ollama list until available)
scripts/switch_model.sh local qwen2.5-coder:7b --wait

# Switch to Turbo Fieldflare (gemma-4-26b-a4b-it default, MLX server :8238)
scripts/switch_model.sh local-fieldflare

# Multi-model mode (Anchor + Coding via LM Studio; Reasoning via mlx_lm)
scripts/switch_model.sh local-multi

# Cloud providers
scripts/switch_model.sh anthropic
scripts/switch_model.sh gemini
scripts/switch_model.sh openai openai/gpt-4.1-mini
```

**What it does:**
1. Validates model is available via `ollama list` (local mode only)
2. Writes all env vars to `docker/.env`
3. Runs `docker compose up -d --force-recreate gateway openclaw`

Note: `local-fieldflare` skips the LM Studio JIT-load step that other
`local-multi`-mode targets run — Fieldflare is its own MLX server, not served
by LM Studio, so that step would load the wrong (or no) model.

Hermes deploys separately (`docker/bots/hermes/run-standalone.sh up`, not
part of this script's compose recreate) — after switching, source
`docker/.env` and redeploy Hermes for it to pick up the new model too.

**Persisted keys in `docker/.env`:** `AGENTSHROUD_MODEL_MODE`, `AGENTSHROUD_LOCAL_MODEL_REF`, `AGENTSHROUD_CLOUD_MODEL_REF`, `AGENTSHROUD_LOCAL_MODEL`, `OPENCLAW_MAIN_MODEL`, `HERMES_MAIN_MODEL`, `OPENCLAW_OLLAMA_API`, `OLLAMA_API_KEY`, and (for `local-multi`-mode targets, including `local-fieldflare`) `LMSTUDIO_API_BASE`, `MLXLM_API_BASE`, `FIELDFLARE_API_BASE`

---

## 6. Three Local Backends

| Backend | Port | Protocol | Default Models | Notes |
|---------|------|----------|----------------|-------|
| **Ollama** | 11434 | OpenAI-compat `/v1/chat/completions` | `qwen3:14b` (single), `qwen3.5:27b` (anchor), `qwen2.5-coder:32b` (coding) | Fallback for any model not matched in `LOCAL_MODEL_ROUTES` |
| **LM Studio** | 1234 | OpenAI-compat | Anchor + Coding in multi-mode | Must be running on host |
| **mlx_lm** | 8234 | OpenAI-compat | `deepseek-r1` | No tool calling; routed via `LOCAL_MODEL_ROUTES` |
| **Turbo Fieldflare** | 8238 | OpenAI-compat (`/health`, `/v1/models`, `/v1/chat/completions`) | `gemma-4-26b-a4b-it` (MLX Gemma 4 26B-A4B) | **Default local model as of 2026-08.** Own MLX server (from the separate `agentshroud_mlx`/`local-llms` project, not this repo), started/stopped via `tf-start`/`tf-stop`/`tf-status`/`tf-log` aliases on the host. No auth (server ignores the API key). Also independently exposed via Tailscale Serve on :8238 (tailnet-only) for direct ChatBox/OpenWebUI access from other devices — that path bypasses AgentShroud's gateway pipeline entirely, which is intentional (host-local backends stay ungated only for the AgentShroud-mediated path; direct device access is a separate, explicitly-chosen use case). |

### Multi-model mode (`local-multi`)

Three role-based models run simultaneously:
- **Anchor** — General agent model; `AGENTSHROUD_ANCHOR_MODEL` (default: `qwen3.5:27b`)
- **Coding** — Code tasks; `AGENTSHROUD_CODING_MODEL` (default: `qwen2.5-coder:32b`)
- **Reasoning** — Deep reasoning; `AGENTSHROUD_REASONING_MODEL` (default: `deepseek-r1`) → routes to mlx_lm

> `local-multi` does **not** automatically route different request types to different models. OpenClaw sends all requests to `OPENCLAW_MAIN_MODEL` (the anchor). The `LOCAL_MODEL_ROUTES` dict in `llm_proxy.py` handles backend routing by model name prefix, so a request with `model: "deepseek-r1"` goes to mlx_lm regardless of mode.

---

## 7. Test Coverage (`gateway/tests/test_llm_proxy.py`)

| Test | What It Covers |
|------|----------------|
| `test_scan_request_data_scans_messages_without_name_error` | PII scanning on inbound messages |
| `test_filter_outbound_streaming_filters_openai_delta_content` | XML block filtering in streaming responses |
| `test_filter_outbound_streaming_filters_anthropic_content_text` | Credential blocking in streaming responses |
| `test_proxy_messages_rewrites_claude_opus_to_local_model` | Cloud-to-local model interception (local mode) |
| `test_proxy_messages_cloud_mode_keeps_claude_and_uses_anthropic` | Cloud mode pass-through (no interception) |
| `test_proxy_messages_strips_ollama_prefix_for_openai_compat` | `ollama/model:tag` → `model:tag` normalization |
| `test_proxy_messages_timeout_returns_openai_compatible_fallback` | Timeout returns graceful OpenAI-format error |
| `test_proxy_messages_timeout_returns_anthropic_compatible_fallback` | Timeout returns graceful Anthropic-format error |

---

## 8. Telegram Integration

`gateway/proxy/telegram_proxy.py` exposes chat commands for model status:
- `_LOCAL_MODEL_STATUS_COMMANDS` (line 82) — commands list
- `_send_local_model_notice()` — reports current `MODEL_MODE` and model ref to chat
- Handles `"ollama requires authentication"` error messages with user-friendly guidance

---

## 9. Bot Startup Flow (local mode)

1. `docker/bots/openclaw/start.sh` — detects `AGENTSHROUD_MODEL_MODE`, sets `OLLAMA_API_KEY` if local, probes `OLLAMA_BASE_URL/../api/tags` to confirm model availability
2. `docker/bots/openclaw/init-config.sh` — runs embedded Node.js that writes `auth-profiles.json`; seeds `cfg.providers.ollama` with `AGENTSHROUD_LOCAL_MODEL_REF`; sets `api: 'ollama'`
3. `docker/config/openclaw/apply-patches.js` — applies remaining openclaw.json patches (not model-specific)

---

## 10. Known Gaps / Open Items

| # | Item | Notes |
|---|------|-------|
| 1 | No dedicated ADR for local LLM architecture | `ADR-006` covers container runtime, not model routing. Should create `ADR-007-local-llm-routing.md` if architecture solidifies. |
| 2 | `qwen3-coder` model only in docs | `RELEASE-PLAN.md:359` references `qwen3-coder:30` as an example. Not used in any code or defaults. Actual default (as of 2026-08) is `gemma-4-26b-a4b-it` via Turbo Fieldflare, not `qwen3:14b`. |
| 3 | `local-multi` doesn't auto-route by task type | OpenClaw always sends to anchor model. To use coding/reasoning models, the user must manually set `model:` in requests or wire task-type detection upstream. |
| 4 | ~~No `AGENTSHROUD_LOCAL_MODEL` wired for gateway~~ **Resolved** | `docker-compose.yml`'s gateway service sets both `AGENTSHROUD_LOCAL_MODEL_REF` and `AGENTSHROUD_LOCAL_MODEL` — confirmed populated at runtime as of the 2026-08 Fieldflare switch. |
| 5 | No smoke test for local model path | `scripts/smoke.sh` likely targets cloud endpoints. No automated check that `gateway → Ollama` path works after deploy. |
| 6 | LM Studio not verified in CI | `local-multi` mode requires LM Studio on host. CI has no Ollama/LM Studio runner. Local-only path has no CI coverage. |
| 7 | Context window mismatch on model switch | Turbo Fieldflare/Gemma-4-26B has a smaller context window than some existing long-running bot sessions expect. Switching a bot to it mid-session can trigger a context-overflow error (`livenessState=blocked`) that only clears with a session reset — not something `switch_model.sh` currently checks for or warns about. |
| 8 | **Hermes cannot be force-switched to a custom-named local model like Fieldflare** — confirmed live 2026-08-12 | Hermes's `ollama` provider type (what `resolve_model.py` maps any local-keyword model to, per its own docstring) does a model-catalog lookup for names it doesn't recognize as a real Ollama-served model — unlike OpenClaw's `openai-local` provider, which posts directly to `OLLAMA_BASE_URL` with no catalog step. For a custom-named model like `gemma-4-26b-a4b-it` (Fieldflare's own naming, not a real Ollama/HuggingFace catalog entry), this makes Hermes silently reroute to a cached/stale `openrouter.ai` route with the wrong API key instead of the correct `gateway:8080` path — surfaces as "Provider authentication failed" with no obvious link to the model switch. **Practical implication:** don't set `HERMES_MAIN_MODEL` to force Hermes's own `model.provider` to a local backend for a non-standard-named model. Leave Hermes on its normal cloud-primary config (`AGENTSHROUD_MODEL_MODE=cloud`, `HERMES_MAIN_MODEL` unset) and rely on the gateway's own automatic quota-exhaustion failover (`LOCAL_MODEL_ROUTES` in `llm_proxy.py`) instead — that path routes correctly regardless of what Hermes's own config says, since it intercepts the request before Hermes's provider-catalog logic ever runs. OpenClaw has no such restriction and can be switched directly via `OPENCLAW_MAIN_MODEL=openai-local/gemma-4-26b-a4b-it` (`scripts/switch_model.sh local-fieldflare` does this correctly already). |

---

## 11. Quick Reference — Switching to Local Mode

```bash
# 1. Pull the model on host
ollama pull qwen3:14b

# 2. Switch stack to local mode
scripts/switch_model.sh local qwen3:14b

# 3. Verify gateway health
curl http://localhost:8080/status

# 4. Verify Ollama routing (send a chat message to the bot, check gateway logs)
docker logs agentshroud-gateway | grep "LLMProxy: Intercepted\|host.docker.internal:11434"
```

### Quick Reference — Switching to Turbo Fieldflare

```bash
# 1. Start Fieldflare on the host (separate agentshroud_mlx/local-llms project)
tf-start
tf-status   # confirm it's serving on :8238

# 2. Switch gateway + openclaw (this is enough for BOTH bots — see step 3)
scripts/switch_model.sh local-fieldflare

# 3. Verify end-to-end
curl -s -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $(docker exec agentshroud-gateway cat /run/secrets/gateway_password)" \
  -d '{"model":"gemma-4-26b-a4b-it","messages":[{"role":"user","content":"say OK"}]}'
```

**Do NOT redeploy Hermes with `HERMES_MAIN_MODEL` pointed at Fieldflare** — see Known Gap #8. Hermes stays on its normal cloud-primary config; it still reaches Fieldflare automatically through the gateway's quota-exhaustion failover when needed, it just shouldn't be forced onto it as the primary provider. OpenClaw has no such restriction; step 2 already switches it correctly.
