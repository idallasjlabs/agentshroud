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

# SCRUM-101: pin to the current-latest digest (refreshed 2026-07-14) for supply-chain
# integrity. This is an upstream vendored base we do not control — its bulk CVEs live in
# vendored layers `apt upgrade` cannot patch (documented residual in cve-mitigation-matrix.md).
# Refresh with: docker pull nousresearch/hermes-agent:latest && docker inspect \
#   --format='{{index .RepoDigests 0}}' nousresearch/hermes-agent:latest
FROM nousresearch/hermes-agent:latest@sha256:e2adeb75300977c509fa363c64a2b0bddac7b6e02888403cd79dd314d8467061

USER root

# HOME must be /opt/data for uid 10000 so interactive docker exec shells write
# hermes CLI config (qwen creds, mcp config) to the persisted volume, not /root.
ENV HOME=/opt/data

# curl for healthcheck + jq for JSON state files; no dumb-init (s6-overlay is PID 1)
# xxd: hermes terminal_tool shells out to xxd for hex dumps — absent from the
# upstream image (debian trixie ships it as its own package, not vim-common).
RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
      curl \
      ca-certificates \
      jq \
      sqlite3 \
      xxd \
    && rm -rf /var/lib/apt/lists/*

# Pre-install ddgs (DuckDuckGo HTML scraper) into the hermes venv so the keyless
# web_search backend is available at first boot. Without it the cron's verify-
# every-claim contract degrades to "no sources" the first time the cloud LLM
# quota is exhausted and failover routes to local LM Studio. uv is part of the
# upstream image; installing into the venv keeps the system Python clean.
RUN /usr/local/bin/uv pip install --python /opt/hermes/.venv/bin/python3 ddgs==9.14.4

# SCRUM-101 follow-up (v1.3.0): patch two vendored-venv deps whose upstream image ships a
# vulnerable pin AND whose fix is a backward-compatible PATCH release (verified: full hermes
# starlette/fastapi/mcp/cryptography stack still imports after the bump — smoke-checked in build).
#   tornado         6.5.5 -> 6.5.6   (CVE-2026-49853 auth-header cross-origin redirect leak;
#                                     CVE-2026-49855 gzip-bomb unbounded decompression)
#   python-multipart 0.0.27 -> 0.0.30 (CVE-2026-53539 form-urlencoded DoS)
# NOTE: starlette (->1.3.1) and cryptography (->48.0.1) are NOT bumped here — they are core
# hermes-agent pins whose fixed versions are minor/major jumps across the fastapi/mcp/auth stack
# that cannot be validated without full upstream integration testing; they are documented as
# upstream-vendored "currently unmitigable" residue in docs/security/cve-mitigation-matrix.md.
RUN /usr/local/bin/uv pip install --python /opt/hermes/.venv/bin/python3 \
        tornado==6.5.6 \
        python-multipart==0.0.30

# Crash-loop fix (2026-07-17): the Telegram adapter's getUpdates health instrumentation
# does `request.do_request = _do_request` to wrap polling requests, but the vendored
# python-telegram-bot 22.6 makes HTTPXRequest __slots__-based (do_request is a class
# method, not an instance attribute) — the assignment raises "AttributeError:
# 'HTTPXRequest' object attribute 'do_request' is read-only" on EVERY boot. Telegram is
# Hermes's only enabled platform (docker/config/hermes/config.yaml.tmpl `telegram.enabled:
# true`), so the failed connect drops the gateway to 0 connected platforms and it exits;
# `restart: unless-stopped` then crash-loops it forever (observed: 175 restarts in prod).
#
# 2026-07-22: this used to be an inline `RUN <<'PATCH' ... PATCH` Dockerfile heredoc.
# That syntax is BuildKit-only — on a Docker Engine without the buildx component, the
# classic builder silently mishandled it (reported "Using cache" and never actually ran
# the patch), producing an image that looked built successfully but still crash-looped.
# Reproduced live on a real host lacking buildx. Moved to a real .py file + COPY + RUN,
# which is builder-agnostic and works identically either way.
COPY docker/bots/hermes/patch_telegram_do_request.py /tmp/patch_telegram_do_request.py
RUN /opt/hermes/.venv/bin/python3 /tmp/patch_telegram_do_request.py \
    && rm /tmp/patch_telegram_do_request.py

# Give s6 15s grace before SIGKILL so the TERM trap can release the Telegram
# long-poll lock and wait up to 8s for the asyncio daemon to exit cleanly.
# Default is 5000ms which cuts the trap short before lock release completes.
ENV S6_KILL_GRACETIME=15000

# AgentShroud secrets injector — runs as root during s6 cont-init before any service starts.
# Reads Docker secret files and writes to /run/s6/container_environment/ so all supervised
# processes (dashboard, gateway run) inherit them via with-contenv.
COPY docker/bots/hermes/agentshroud-secrets.sh /etc/cont-init.d/00-agentshroud-secrets.sh
RUN chmod +x /etc/cont-init.d/00-agentshroud-secrets.sh

# Item 1 — Crash-rate alerting s6 longrun service
COPY docker/bots/hermes/s6/crashwatch /etc/s6-overlay/s6-rc.d/agentshroud-crashwatch
COPY docker/bots/hermes/crashwatch.sh /usr/local/bin/agentshroud-crashwatch.sh

# Item 2 — Healthchecks.io heartbeat s6 longrun service
COPY docker/bots/hermes/s6/heartbeat  /etc/s6-overlay/s6-rc.d/agentshroud-heartbeat
COPY docker/bots/hermes/heartbeat.sh  /usr/local/bin/agentshroud-heartbeat.sh

# Bake AgentShroud-managed config defaults into the image.
# init-config.sh merges these into /opt/data on first boot (idempotent).
COPY docker/config/hermes/ /app/config-defaults/hermes/
COPY docker/bots/hermes/start.sh /usr/local/bin/start-hermes.sh
COPY docker/bots/hermes/init-config.sh /usr/local/bin/init-hermes-config.sh

# SCRUM-70 (WS-C) — local-model parity resolver. Self-contained (no gateway deps)
# so it runs inside this vendored image. init-config.sh / start.sh call it to set
# model.default + model.provider from AGENTSHROUD_MODEL_MODE / HERMES_MAIN_MODEL,
# so Hermes runs fully local (or cloud) exactly as switch_model.sh selected.
COPY docker/bots/hermes/resolve_model.py /usr/local/lib/agentshroud/resolve_model.py

# Item 8 — Stand-alone email helper for cron use
COPY docker/bots/hermes/email_helper.sh /usr/local/bin/agentshroud-email-send.sh

# SSH-exec helper — wraps the internal gateway /ssh/exec control-plane call so the
# agent never puts a plain-http://gateway URL on its command line (which tirith
# flags as "[HIGH] Plain HTTP URL in execution context" and forces approval every
# call). Same shared script both bot images bake in. See the script header.
COPY docker/scripts/agentshroud-ssh-exec.sh /usr/local/bin/agentshroud-ssh-exec.sh

# Pre-baked Markdown→HTML renderer for the competitive-intel email cron job.
# Placed outside /opt/data (which is a volume mount) so it survives volume resets.
COPY docker/bots/hermes/render_md_email.py /usr/local/lib/agentshroud/render_md_email.py

# Branding assets — logo for Telegram startup photo notifications
COPY branding/logos/png/logo.png /app/branding/logo.png
COPY branding/logos/svg/logo.svg /app/branding/logo.svg

RUN chmod +x /usr/local/bin/start-hermes.sh /usr/local/bin/init-hermes-config.sh \
             /usr/local/bin/agentshroud-crashwatch.sh /usr/local/bin/agentshroud-heartbeat.sh \
             /usr/local/bin/agentshroud-email-send.sh \
             /usr/local/bin/agentshroud-ssh-exec.sh \
             /etc/s6-overlay/s6-rc.d/agentshroud-crashwatch/run \
             /etc/s6-overlay/s6-rc.d/agentshroud-heartbeat/run \
 && mkdir -p /app/config-defaults /usr/local/lib/agentshroud \
 && chmod 755 /usr/local/lib/agentshroud/render_md_email.py \
 && chmod 755 /usr/local/lib/agentshroud/resolve_model.py \
 && chown -R 10000:10000 /app/config-defaults \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-crashwatch \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-heartbeat

# Port 9119: Hermes dashboard (served by s6 dashboard service when HERMES_DASHBOARD=1)
# Port 8642: OpenAI-compatible API server (enabled, requires API_SERVER_KEY)
EXPOSE 8642 9119

# Healthcheck: probe the OpenAI-compatible API /health endpoint on 8642.
# v0.15.1 moved dashboard auth behind an auth gate; 9119 is no longer reliable.
# start_period=120s allows s6 init + skill sync + gateway startup to complete.
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8642/health || exit 1

# Keep the image's own entrypoint (/init → main-wrapper.sh). CMD is passed as
# args to main-wrapper.sh: if it's an executable it runs via s6-setuidgid hermes.
CMD ["/usr/local/bin/start-hermes.sh"]
