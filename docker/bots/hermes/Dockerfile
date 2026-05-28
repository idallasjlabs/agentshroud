# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud Hermes Agent runtime container.
# Wraps nousresearch/hermes-agent inside the AgentShroud security envelope:
#  - All egress via HTTP_PROXY=http://gateway:8181 (EgressFilter + PromptGuard + ApprovalQueue)
#  - LLM calls via ANTHROPIC_BASE_URL=http://gateway:8080 (PII redaction + audit chain)
#  - Telegram traffic proxied via gateway's telegram_proxy.py (multi-bot registry)
#  - No published ports — only reachable from gateway over agentshroud-isolated network
#
# Architecture note: nousresearch/hermes-agent:latest uses s6-overlay for process supervision.
# Entrypoint is /init (s6) → main-wrapper.sh → CMD. Init runs as root, drops to UID 10000
# (hermes user) via s6-setuidgid. We hook into s6 via /etc/cont-init.d/ for secrets injection
# and first-boot config seeding. Do NOT override ENTRYPOINT or set USER hermes here.

FROM nousresearch/hermes-agent:latest

USER root

# curl for healthcheck; no dumb-init needed (image already uses s6-overlay as PID 1)
RUN apt-get update && apt-get install -y --no-install-recommends \
      curl \
      ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# AgentShroud secrets injector — runs as root during s6 cont-init before any service starts.
# Reads Docker secret files and writes to /run/s6/container_environment/ so all supervised
# processes (dashboard, gateway run) inherit them via with-contenv.
COPY docker/bots/hermes/agentshroud-secrets.sh /etc/cont-init.d/00-agentshroud-secrets.sh
RUN chmod +x /etc/cont-init.d/00-agentshroud-secrets.sh

# Bake AgentShroud-managed config defaults into the image.
# init-config.sh merges these into /opt/data on first boot (idempotent).
COPY docker/config/hermes/ /app/config-defaults/hermes/
COPY docker/bots/hermes/start.sh /usr/local/bin/start-hermes.sh
COPY docker/bots/hermes/init-config.sh /usr/local/bin/init-hermes-config.sh

RUN chmod +x /usr/local/bin/start-hermes.sh /usr/local/bin/init-hermes-config.sh \
 && mkdir -p /app/config-defaults \
 && chown -R 10000:10000 /app/config-defaults

# Port 9119: Hermes dashboard (served by s6 dashboard service when HERMES_DASHBOARD=1)
# Port 8642: reserved for future Hermes API server
EXPOSE 8642 9119

# Healthcheck: probe the dashboard on 9119 (always up when HERMES_DASHBOARD=1).
# start_period=120s allows s6 init + skill sync + gateway startup to complete.
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
  CMD curl -fsS http://127.0.0.1:9119/ || exit 1

# Keep the image's own entrypoint (/init → main-wrapper.sh). CMD is passed as
# args to main-wrapper.sh: if it's an executable it runs via s6-setuidgid hermes.
CMD ["/usr/local/bin/start-hermes.sh"]
