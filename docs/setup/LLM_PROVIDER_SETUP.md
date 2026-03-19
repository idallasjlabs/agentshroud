# AgentShroud™ LLM Provider Setup & Switching Guide
**Generated:** 2026-03-09
**Scope:** Multi-provider support for Claude, ChatGPT, Gemini, and local Ollama.

This guide provides instructions for configuring and switching between different LLM providers using the AgentShroud Gateway as a secure proxy.

---

## 1. Provision Your Secrets (API Keys & Tokens)

The AgentShroud Gateway is configured to automatically inject credentials into outbound requests based on the destination domain. You must provide these secrets as files in the `docker/secrets/` directory.

| Provider | Secret File | Header Injected |
| :--- | :--- | :--- |
| **Claude** | `anthropic_oauth_token.txt` | `x-api-key` or `Authorization: Bearer` |
| **ChatGPT** | `openai_api_key.txt` | `Authorization: Bearer` |
| **Gemini** | `google_api_key.txt` | `x-goog-api-key` |

### Setup Commands:
```bash
# From the project root:
echo "your-openai-key-here" > docker/secrets/openai_api_key.txt
echo "your-gemini-key-here" > docker/secrets/google_api_key.txt

# Ensure permissions are restrictive
chmod 600 docker/secrets/*.txt
```

---

## 2. Apply Configuration & Restart

The `docker/docker-compose.yml` file has been updated to include the necessary environment variables and secret mappings. To apply these changes and mount the new secrets:

```bash
docker compose -f docker/docker-compose.yml -p agentshroud up -d --force-recreate
```

---

## 3. Switching Models in OpenClaw

You can switch between providers by changing the model name in your OpenClaw configuration. This can be done via the Telegram bot or the Web UI (default: `http://localhost:18790`).

### Provider Model Strings:

| Provider | Example Model String | Gateway Routing |
| :--- | :--- | :--- |
| **Claude** | `anthropic/claude-3-5-sonnet-20240620` | `https://api.anthropic.com` |
| **ChatGPT** | `openai/gpt-4o` | `https://api.openai.com` |
| **Gemini** | `google/gemini-1.5-pro` | `https://generativelanguage.googleapis.com` |
| **Ollama** | `qwen2.5-coder:7b` | `http://host.docker.internal:11434` |

### How to Switch via Telegram:
Simply tell the bot:
> "Switch to model openai/gpt-4o"
*or*
> "Switch to model qwen2.5-coder:7b"

---

## 4. Local Ollama Integration

To use local models without spending API credits:

1.  **Ensure Ollama is running** on your host machine (Mac/PC).
2.  **Pull the desired model:**
    ```bash
    ollama run qwen2.5-coder:7b
    ```
3.  **Switch the bot** to the local model name. The Gateway detects local keywords (qwen, llama, mistral, deepseek, phi, ollama) and automatically routes traffic to your host instead of the internet.

---

## 5. Verification & Troubleshooting

*   **Credential Injection:** If a provider returns a 401/403 error, verify the secret file exists in `docker/secrets/` and is correctly mapped in `docker-compose.yml`.
*   **Gateway Logs:** Monitor the gateway logs to see real-time routing and injection:
    ```bash
    docker logs -f agentshroud-gateway
    ```
*   **Audit Trail:** All requests, regardless of provider, are logged to the security ledger in `data/ledger.db` and redacted for PII by the `PIISanitizer`.
