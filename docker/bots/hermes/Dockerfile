# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud Hermes Agent runtime container.
# Wraps nousresearch/hermes-agent inside the AgentShroud security envelope:
#  - All egress via HTTP_PROXY=http://gateway:8181 (EgressFilter + PromptGuard + ApprovalQueue)
#  - LLM calls via ANTHROPIC_BASE_URL=http://gateway:8080 (PII redaction + audit chain)
#  - Telegram via TELEGRAM_API_BASE_URL=http://gateway:8080/telegram-api
#  - No published ports — only reachable from gateway over agentshroud-isolated network

FROM nousresearch/hermes-agent:latest

USER root

# Minimal additions: curl for healthcheck, dumb-init for clean signal handling.
# Everything else is already in the upstream image.
RUN apt-get update && apt-get install -y --no-install-recommends \
      curl \
      ca-certificates \
      dumb-init \
    && rm -rf /var/lib/apt/lists/*

# Bake AgentShroud-managed config defaults into the image.
# init-config.sh merges these into /opt/data on first boot (idempotent).
COPY docker/config/hermes/ /app/config-defaults/hermes/
COPY docker/bots/hermes/start.sh /usr/local/bin/start-hermes.sh
COPY docker/bots/hermes/init-config.sh /usr/local/bin/init-hermes-config.sh

RUN chmod +x /usr/local/bin/start-hermes.sh /usr/local/bin/init-hermes-config.sh \
 && mkdir -p /opt/data/cron /opt/data/sessions /opt/data/memories /opt/data/skills \
             /opt/data/home /opt/data/logs /opt/data/hooks /opt/data/skins \
 # Hermes drops to UID 10000 (hermes user created by upstream image)
 && chown -R 10000:10000 /opt/data /app/config-defaults

USER hermes

# Port 8642: Hermes gateway API (OpenAI-compatible + /health)
# Port 9119: Hermes dashboard (HERMES_DASHBOARD=1)
EXPOSE 8642 9119

HEALTHCHECK --interval=30s --timeout=10s --start-period=90s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8642/health || exit 1

ENTRYPOINT ["dumb-init", "--"]
CMD ["/usr/local/bin/start-hermes.sh"]
