# Local LLM Support — Implementation Review

> **Status:** v1.2.0 milestone — 3 commits shipped on `feat-v1.2.0-local-llms`
> **Last reviewed:** 2026-04-26
> **Purpose:** Compile all context before proceeding with further local LLM work.

---

## 1. Architecture Overview

All LLM traffic — cloud and local — passes through a single choke point:

```
OpenClaw bot → gateway:8080/v1 → LLMProxy → Ollama :11434
                                           → LM Studio :1234
                                           → mlx_lm :8234
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
2. **Model keyword matching:** `qwen`, `llama`, `mistral`, `deepseek`, `phi`, `ollama`, `lmstudio`, `mlxlm`
3. **Prefix matching:** `ollama/` or `lmstudio/` prefix → local
4. **Interception:** If `MODEL_MODE != "cloud"` and model name contains `claude-opus` → force rewrite to `MAIN_MODEL`
5. **Prefix stripping:** `ollama/qwen3:14b` → `qwen3:14b` (local APIs expect bare names)
6. **Backend routing:** `LOCAL_MODEL_ROUTES` dict checked first (for non-Ollama backends), then Ollama fallback

**`LOCAL_MODEL_ROUTES` (current):**
```python
LOCAL_MODEL_ROUTES = {
    "deepseek-r1": MLXLM_API_BASE,   # Routes to mlx_lm :8234 (no tool calling)
}
```
All other local models fall through to Ollama.

---

## 4. Environment Variables

| Variable | Default (docker-compose) | Default (code fallback) | Purpose |
|----------|--------------------------|-------------------------|---------|
| `AGENTSHROUD_MODEL_MODE` | `cloud` | `local` | `local`, `local-multi`, or `cloud` |
| `AGENTSHROUD_LOCAL_MODEL_REF` | `ollama/qwen3:14b` | — | Provider-prefixed local model ref |
| `AGENTSHROUD_LOCAL_MODEL` | `qwen3:14b` | `qwen2.5-coder:7b` | Bare model name for Ollama |
| `AGENTSHROUD_CLOUD_MODEL_REF` | `anthropic/claude-opus-4-6` | — | Provider-prefixed cloud model ref |
| `AGENTSHROUD_ANCHOR_MODEL` | `qwen3.5:27b` | — | Anchor model (multi-mode) |
| `AGENTSHROUD_CODING_MODEL` | `qwen2.5-coder:32b` | — | Coding model (multi-mode) |
| `AGENTSHROUD_REASONING_MODEL` | `deepseek-r1` | — | Reasoning model (multi-mode, routes to mlx_lm) |
| `OPENCLAW_MAIN_MODEL` | — | — | Model ref passed to bot; set by `switch_model.sh` |
| `OLLAMA_BASE_URL` | `http://gateway:8080/v1` | — | Bot's Ollama endpoint (proxied through gateway) |
| `OLLAMA_API_KEY` | `ollama-local` | — | Auth token for Ollama provider |
| `LMSTUDIO_API_BASE` | — | `http://host.docker.internal:1234` | LM Studio endpoint |
| `MLXLM_API_BASE` | — | `http://host.docker.internal:8234` | mlx_lm endpoint |

> **Note:** `docker-compose.yml` defaults `AGENTSHROUD_MODEL_MODE` to `cloud`. The code-level fallback in `llm_proxy.py:33` defaults to `local`. The compose file wins at runtime.

---

## 5. Model Switching CLI (`scripts/switch_model.sh`)

```bash
# Switch to local Ollama (qwen3:14b default)
scripts/switch_model.sh local

# Switch with a specific model (must already be pulled)
scripts/switch_model.sh local qwen3:14b

# Switch with model pull wait (polls ollama list until available)
scripts/switch_model.sh local qwen2.5-coder:7b --wait

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
3. Runs `docker compose up -d --force-recreate gateway bot`

**Persisted keys in `docker/.env`:** `AGENTSHROUD_MODEL_MODE`, `AGENTSHROUD_LOCAL_MODEL_REF`, `AGENTSHROUD_CLOUD_MODEL_REF`, `AGENTSHROUD_LOCAL_MODEL`, `OPENCLAW_MAIN_MODEL`, `OPENCLAW_OLLAMA_API`, `OLLAMA_API_KEY`

---

## 6. Three Local Backends

| Backend | Port | Protocol | Default Models | Notes |
|---------|------|----------|----------------|-------|
| **Ollama** | 11434 | OpenAI-compat `/v1/chat/completions` | `qwen3:14b` (single), `qwen3.5:27b` (anchor), `qwen2.5-coder:32b` (coding) | Default for all local models |
| **LM Studio** | 1234 | OpenAI-compat | Anchor + Coding in multi-mode | Must be running on host |
| **mlx_lm** | 8234 | OpenAI-compat | `deepseek-r1` | No tool calling; routed via `LOCAL_MODEL_ROUTES` |

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
| 2 | `qwen3-coder` model only in docs | `RELEASE-PLAN.md:359` references `qwen3-coder:30` as an example. Not used in any code or defaults. Memory was stale — actual default is `qwen3:14b`. |
| 3 | `local-multi` doesn't auto-route by task type | OpenClaw always sends to anchor model. To use coding/reasoning models, the user must manually set `model:` in requests or wire task-type detection upstream. |
| 4 | No `AGENTSHROUD_LOCAL_MODEL` wired for gateway | `docker-compose.yml:73-81` (gateway service) sets `AGENTSHROUD_LOCAL_MODEL_REF` but not `AGENTSHROUD_LOCAL_MODEL`. The code in `llm_proxy.py:32` reads `AGENTSHROUD_LOCAL_MODEL`. Verify this is populated at runtime. |
| 5 | No smoke test for local model path | `scripts/smoke.sh` likely targets cloud endpoints. No automated check that `gateway → Ollama` path works after deploy. |
| 6 | LM Studio not verified in CI | `local-multi` mode requires LM Studio on host. CI has no Ollama/LM Studio runner. Local-only path has no CI coverage. |

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
