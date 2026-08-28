#!/bin/bash
# omlx-keepwarm.sh — keep the oMLX gemma model resident in memory.
#
# Why: the voice terminal's "direct" path answers via gemma-4-12B-it-4bit on
# the host's oMLX server. The model pages out of memory after a few idle
# minutes; the next voice query then pays a cold reload before the first
# token (measured live 2026-08-28: 5.06s cold vs 0.69s warm for an identical
# tiny completion — the dominant chunk of the user-visible "thinking" delay).
# A 1-token ping every few minutes keeps it hot.
#
# No secret is stored on disk: the API key is read from the running gateway
# container's environment at execution time. If the container is down, the
# ping is skipped silently (nothing to keep warm for anyway).
#
# Install (user crontab):
#   */4 * * * * /Users/ijefferson.admin/Development/agentshroud/scripts/omlx-keepwarm.sh >/dev/null 2>&1

KEY=$(/usr/local/bin/docker exec agentshroud-gateway printenv OMLX_API_KEY 2>/dev/null \
      || docker exec agentshroud-gateway printenv OMLX_API_KEY 2>/dev/null)
[ -z "$KEY" ] && exit 0

curl -s -m 30 -o /dev/null -X POST http://localhost:8000/v1/chat/completions \
  -H "Authorization: Bearer $KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemma-4-12B-it-4bit","messages":[{"role":"user","content":"hi"}],"max_tokens":1}'
