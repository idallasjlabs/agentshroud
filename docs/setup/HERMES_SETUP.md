<!-- © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved. -->
<!-- AgentShroud™ USPTO Serial No. 99728633 | Patent Pending No. 64/018,744 -->

# Hermes Agent — Connection Setup

Connect AI frontend clients to Hermes's OpenAI-compatible API and access the HCI
(Hermes Control Interface) admin UI through the AgentShroud gateway.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Hermes OpenAI-Compatible API](#hermes-openai-compatible-api)
   - [Network Access](#network-access)
   - [API Key Setup](#api-key-setup)
   - [Tailscale Serve Configuration](#tailscale-serve-configuration)
   - [Frontend Client Setup](#frontend-client-setup)
4. [HCI (Hermes Control Interface)](#hci-hermes-control-interface)
   - [Network Access](#hci-network-access)
   - [Authentication Flow](#authentication-flow)
   - [Tailscale Serve Configuration](#hci-tailscale-serve-configuration)
   - [Starting the HCI Container](#starting-the-hci-container)
5. [Security Model](#security-model)
   - [Inbound Path](#inbound-path)
   - [Outbound Path](#outbound-path)
   - [Mitigations in Place](#mitigations-in-place)
6. [Troubleshooting](#troubleshooting)

---

## Overview

| Component | Port | Protocol | Purpose |
|-----------|------|----------|---------|
| Hermes OpenAI API | 8642 | HTTPS (tailnet) / HTTP (local) | OpenAI-compatible LLM endpoint |
| HCI Admin UI | 9121 | HTTPS (tailnet) / HTTP (local) | Hermes Control Interface |

Both services are accessible over the Tailscale tailnet (`marvin.tail240ea8.ts.net`)
or locally on `127.0.0.1`. The tailnet path requires the client machine to be enrolled
in the same Tailscale network.

---

## Prerequisites

- Docker stack running: `agentshroud-gateway` and `agentshroud-hermes` containers up
- Tailscale installed and authenticated on `marvin` (for tailnet access)
- 1Password CLI (`op`) available and signed in to "Agent Shroud Bot Credentials" vault
- The `hermes_api_key` Docker secret created (see [API Key Setup](#api-key-setup))

---

## Hermes OpenAI-Compatible API

### Network Access

The gateway forwards TCP connections from `127.0.0.1:8642` to `hermes:8642` on the
internal Docker network.

| Access path | Base URL |
|-------------|----------|
| Tailnet (recommended) | `https://marvin.tail240ea8.ts.net:8642/v1` |
| Local only | `http://127.0.0.1:8642/v1` |

### API Key Setup

Generate a key and store it as both a Docker secret and a 1Password item:

```bash
# 1. Generate a 64-character hex key
API_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
echo "Generated: $API_KEY"

# 2. Store in 1Password "Agent Shroud Bot Credentials" vault
op item create \
  --vault "Agent Shroud Bot Credentials" \
  --category "Secure Note" \
  --title "hermes-api-key" \
  "credential[password]=$API_KEY"

# 3. Create the Docker secret
echo "$API_KEY" | docker secret create hermes_api_key -

# 4. Verify the secret exists
docker secret ls | grep hermes_api_key
```

### Tailscale Serve Configuration

The canonical setup script configures all AgentShroud serves (including Hermes API, dashboard,
and HCI) in one shot:

```bash
sudo ./scripts/tailscale-serve.sh start
```

Verify all mappings are active:

```bash
tailscale serve status
# Expected output includes:
#   https://marvin.tail240ea8.ts.net:9119 -> http://127.0.0.1:9119
#   https://marvin.tail240ea8.ts.net:8642 -> http://127.0.0.1:8642
#   https://marvin.tail240ea8.ts.net:9121 -> http://127.0.0.1:9121
```

To set up only the API port manually (without the full script):

```bash
sudo tailscale serve --https=8642 --bg http://localhost:8642
```

### Frontend Client Setup

Use any OpenAI-compatible frontend (Open WebUI, LibreChat, Chatbox, or the OpenAI
Python/JS SDK). Apply these settings:

| Setting | Value |
|---------|-------|
| Base URL | `https://marvin.tail240ea8.ts.net:8642/v1` |
| API Key | Value of the `hermes_api_key` secret |
| Model | `anthropic/claude-opus-4.6` |

**Notes:**
- The client machine must be connected to the Tailscale tailnet to reach
  `marvin.tail240ea8.ts.net`. Local-only clients use `http://127.0.0.1:8642/v1`.
- Model override is disabled (`allow_model_override: false`). The model field will
  show `anthropic/claude-opus-4.6` as the only available option. Some clients
  populate the model list via `GET /v1/models`; select that model if prompted.

#### Open WebUI

1. Settings → Connections → OpenAI API
2. Set API URL to `https://marvin.tail240ea8.ts.net:8642/v1`
3. Set API Key to the `hermes_api_key` value
4. Save and reload — `anthropic/claude-opus-4.6` appears in the model selector

#### LibreChat

In `librechat.yaml` under `endpoints`:

```yaml
endpoints:
  custom:
    - name: "Hermes (AgentShroud)"
      apiKey: "<hermes_api_key value>"
      baseURL: "https://marvin.tail240ea8.ts.net:8642/v1"
      models:
        default: ["anthropic/claude-opus-4.6"]
        fetch: false
```

#### Chatbox

1. Settings → AI Provider → OpenAI API Compatible
2. API Host: `https://marvin.tail240ea8.ts.net:8642`
3. API Key: `<hermes_api_key value>`
4. Model: `anthropic/claude-opus-4.6`

---

## HCI (Hermes Control Interface)

### HCI Network Access

The HCI is gated by `gateway/proxy/hci_proxy.py` (HTTP Basic Auth). After passing
gateway auth, HCI presents its own password login screen.

| Access path | URL |
|-------------|-----|
| Tailnet (recommended) | `https://marvin.tail240ea8.ts.net:9121` |
| Local only | `http://127.0.0.1:9121` |

Container: `agentshroud-hci` (profile `hermes` or `full`)

### Authentication Flow

1. Browser navigates to `https://marvin.tail240ea8.ts.net:9121`
2. Gateway Basic Auth prompt — credentials from `hci_proxy.py` configuration
3. HCI password login screen — HCI's own admin password

### HCI Tailscale Serve Configuration

All Tailscale serves (including HCI on `:9121`) are configured by:

```bash
sudo ./scripts/tailscale-serve.sh start
```

To set up only the HCI port manually:

```bash
sudo tailscale serve --https=9121 --bg http://localhost:9121
```

### Starting the HCI Container

HCI starts as part of the `full` compose profile:

```bash
# Full stack (gateway + OpenClaw + Hermes + HCI)
docker-compose -f docker/docker-compose.yml -p agentshroud --profile full up -d

# Verify HCI is running
docker ps --filter name=agentshroud-hci
```

---

## Security Model

### Inbound Path

Direct API clients on port 8642 reach Hermes without passing through the AgentShroud
inbound PromptGuard pipeline. The Telegram-based inbound path (OpenClaw → gateway →
Hermes) does go through PromptGuard; direct API calls do not.

This is by design: the OpenAI-compatible API is intended for trusted, authenticated
clients on the tailnet.

### Outbound Path

All Hermes outbound traffic routes through the gateway HTTP proxy
(`HTTP_PROXY=gateway:8181`). Regardless of how a request arrives at Hermes, every
LLM call and tool invocation that Hermes makes outbound is subject to:

| Control | Enforced |
|---------|----------|
| Egress filter | Yes — `gateway/security/` EgressFilter module |
| PII redaction | Yes — Presidio engine at ≥ 0.9 confidence |
| Audit log | Yes — all outbound requests logged |
| Approval queue | Yes — `email_sending`, `file_deletion`, `external_api_calls`, `skill_installation` |

### Mitigations in Place

| Risk | Mitigation |
|------|-----------|
| Unauthenticated inbound API access | Required `hermes_api_key` on every request |
| Open internet access to API | Tailnet-only via Tailscale serve; no public port forwarding |
| Prompt injection via API | CORS allowlist; `allow_model_override: false` limits attack surface |
| HCI web terminal / command execution | `agentshroud-isolated` network; gateway Basic Auth gate; HCI own password; tailnet-only |
| Model switching by clients | `allow_model_override: false` in Hermes config — model is fixed to `anthropic/claude-opus-4.6` |

---

## Troubleshooting

| Symptom | Check |
|---------|-------|
| `401 Unauthorized` from API | Confirm API key matches `hermes_api_key` Docker secret value |
| `Connection refused` on port 8642 | `docker ps` — confirm `agentshroud-hermes` is running; check `docker logs agentshroud-hermes` |
| Model list shows "no models" | Some clients require `GET /v1/models` to succeed; confirm Hermes API is reachable, then manually set model to `anthropic/claude-opus-4.6` |
| Cannot reach tailnet URL | Confirm client machine is enrolled in Tailscale and `tailscale serve status` shows the mapping |
| HCI shows blank / 502 | `agentshroud-hci` container may not be running — start with `--profile full`; check `docker logs agentshroud-hci` |
| HCI Basic Auth loop | Gateway `hci_proxy.py` credentials mismatch — check gateway config or logs at `docker logs agentshroud-gateway` |
| Outbound LLM calls failing | Hermes `HTTP_PROXY` env var must be `gateway:8181` — inspect with `docker inspect agentshroud-hermes` |
