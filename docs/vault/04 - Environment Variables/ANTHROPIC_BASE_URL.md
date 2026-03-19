---
title: ANTHROPIC_BASE_URL
type: env-var
tags: [llm, proxy, anthropic, routing]
related: [Proxy Layer/llm_proxy.py, Configuration/All Environment Variables, Configuration/Dockerfile.bot]
status: documented
---

# ANTHROPIC_BASE_URL

## Description

Overrides the base URL for all Anthropic API calls from the OpenClaw bot. By pointing this to the gateway, every LLM API request is intercepted, scanned for PII, and logged before being forwarded to the real Anthropic endpoint.

## Value

```
http://gateway:8080
```

This routes calls to `http://gateway:8080/v1/messages` instead of `https://api.anthropic.com/v1/messages`.

## How It Works

1. OpenClaw sends `POST http://gateway:8080/v1/messages` (due to `ANTHROPIC_BASE_URL`)
2. Gateway receives it → runs PII scan, prompt injection check, egress filter
3. Gateway forwards to real `api.anthropic.com` using the actual API key (from 1Password op-proxy)
4. Gateway scans response → returns to bot

## Why It's Critical

If `ANTHROPIC_BASE_URL` is unset or points elsewhere:
- LLM calls bypass ALL security scanning
- PII can be sent to Anthropic without redaction
- No audit trail of LLM interactions
- The entire security model is broken

## SDK Patch

The Anthropic SDK patch (`docker/scripts/patch-anthropic-sdk.sh`) is applied at Docker image build time to enforce `ANTHROPIC_BASE_URL`. This prevents runtime bypass via SDK configuration.

## Set In

`docker/docker-compose.yml`:
```yaml
environment:
  - ANTHROPIC_BASE_URL=http://gateway:8080
```

## Related Notes

- [[Proxy Layer/llm_proxy.py|llm_proxy.py]] — Gateway-side LLM proxy handler
- [[Configuration/Dockerfile.bot]] — Where SDK patch is applied
- [[Configuration/All Environment Variables]] — All env vars
- [[Data Flow]] — Full request flow
