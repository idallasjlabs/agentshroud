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

# SCRUM-101: pin to a digest for supply-chain integrity. This is an upstream vendored
# base we do not control — its bulk CVEs live in vendored layers `apt upgrade` cannot
# patch (documented residual in cve-mitigation-matrix.md).
#
# Pin lives in docker/versions.env (HERMES_IMAGE) — the single source of truth shared
# with scripts/update-agentshroud.sh and CI's CVE tracking. To bump: run
# `scripts/update-agentshroud.sh --bot hermes --hermes-latest` (runs a compatibility
# check against the candidate before it ever touches this file), or manually refresh
# the digest with:
#   docker pull nousresearch/hermes-agent:latest && docker inspect \
#     --format='{{index .RepoDigests 0}}' nousresearch/hermes-agent:latest
# and edit HERMES_IMAGE in docker/versions.env directly. No default here — an unset
# build arg must fail the build loudly, not silently float to an untested version.
ARG HERMES_IMAGE
FROM ${HERMES_IMAGE}

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

# SCRUM-101 follow-up (v1.3.0): patch a vendored-venv dep whose upstream image
# ships a vulnerable pin AND whose fix is a backward-compatible PATCH release
# (verified: full hermes starlette/fastapi/mcp/cryptography stack still
# imports after the bump — smoke-checked in build).
#   tornado 6.5.5 -> 6.5.8   (CVE-2026-49853 auth-header cross-origin redirect leak;
#                             CVE-2026-49855 gzip-bomb unbounded decompression;
#                             CVE-2026-82397 found 2026-09-08, fixed in 6.5.8)
# NOTE: starlette (->1.3.1) and cryptography (->48.0.1) are NOT bumped here — they are core
# hermes-agent pins whose fixed versions are minor/major jumps across the fastapi/mcp/auth stack
# that cannot be validated without full upstream integration testing; they are documented as
# upstream-vendored "currently unmitigable" residue in docs/security/cve-mitigation-matrix.md.
#
# 2026-09-21 Sunday upgrade (HERMES_IMAGE -> v2026.9.21 / semver 0.21.4, moved
# again from the v2026.9.14/0.20.6 target this comment originally named —
# Hermes shipped several more tags between the two discovery passes in this
# same run): dropped the python-multipart==0.0.30 pin that lived here
# (CVE-2026-53539 fix) — verified via `importlib.metadata` against the raw
# v2026.9.21 base image that the vendor now ships python-multipart 0.0.32
# natively (newer than our old pin), so re-asserting ==0.0.30 would have
# silently DOWNGRADED it on every future rebuild.
#
# Verified 2026-09-21 by running `importlib.metadata.version` inside the raw
# unpatched base image (sha256:6bece064, no build, no patch layer applied):
#     python-multipart  0.0.32
#     tornado           6.5.8
# The running container could not answer this — it reports 0.0.30 precisely
# BECAUSE the patch line put it there, so only the unpatched base is evidence.
#
# 2026-09-21 Sunday upgrade, second pass: tornado has moved again since the
# note above was written. PyPI's actual latest is 6.5.10 (6.5.9 released
# 2026-09-14, 6.5.10 released 2026-09-15 — both predate this run; the earlier
# ==6.5.8 pin, even rewritten as a floor, was simply stale). OSV.dev reports no
# known advisory against 6.5.8-6.5.10 (checked 2026-09-21) — this is a
# latest-stable bump per the no-exceptions directive, not a CVE fix. Pinned
# exactly (==), matching the httplib2/pillow/etc. pattern below, rather than
# left as a floor: an explicit pin is what "never leave a component on an
# unpinned/undetermined version" means in practice, and the vendor's base
# still ships 6.5.8 today (verified against the raw v2026.9.21 base image,
# sha256:6bece064, importlib.metadata, no patch layer) so this remains a real,
# non-no-op bump.
RUN /usr/local/bin/uv pip install --python /opt/hermes/.venv/bin/python3 \
        tornado==6.5.10

# CVE registry verification pass (2026-07-31): real per-CVE research against the exact
# installed versions in this image (see gateway/security/agent_cve_registry.py, Hermes
# dependency findings) turned up 6 more vendored deps with a currently-unpatched CVE and
# a backward-compatible PATCH/MINOR fix available -- same bump-in-venv pattern as above,
# each independently reasoned as unlikely to break hermes-agent's usage of the package:
#   httplib2         0.31.2 -> 0.32.0  (CVE-2026-59939 unbounded memory growth/OOM)
#   pillow           12.2.0 -> 12.3.0  (CVE-2026-55798 OS command injection via Image.show() on Windows)
#   pyasn1           0.6.3  -> 0.6.4   (CVE-2026-59886 availability-only DoS)
#   pydantic-settings 2.13.1 -> 2.14.2 (CVE-2026-58203)
#   pygments         2.19.2 -> 2.20.0  (CVE-2026-4539 local-access-only ReDoS)
#   PyNaCl           1.5.0  -> 1.6.2   (CVE-2025-69277)
# NOT bumped: python_olm (libolm) -- CVE-2024-45191/2/3 (side-channel/crypto weaknesses).
# Upstream maintainers have stated libolm is deprecated and these will NOT be fixed; no
# newer release exists to bump to. Tracked as a genuine, permanent residual risk in
# docs/security/cve-mitigation-matrix.md, not hidden behind a green badge.
RUN /usr/local/bin/uv pip install --python /opt/hermes/.venv/bin/python3 \
        httplib2==0.32.0 \
        pillow==12.3.0 \
        pyasn1==0.6.4 \
        pydantic-settings==2.14.2 \
        pygments==2.20.0 \
        PyNaCl==1.6.2

# 2026-09-02: CVE-2026-59873 (node-tar DoS via crafted gzip bomb, fixed in tar 7.5.19)
# in the upstream image's global npm CLI (vendored tar 7.5.16 under npm's own
# node_modules, not an app dependency). npm 12.0.2 is the first npm release that
# requires tar>=7.5.19 itself, so bumping npm is the fix rather than patching tar
# directly underneath it (npm manages that tree). Global npm self-update only;
# no app code touches it.
RUN npm install -g npm@12.0.2

# 2026-09-08: npm@12.0.2 (above) is already the latest npm release, but Trivy
# still flags its OWN bundled deps (tar 7.5.19, brace-expansion 5.0.7,
# ip-address 10.2.0) for CVEs with a fix in a newer patch version npm hasn't
# re-released with yet — genuinely upstream-blocked, no newer npm to bump to
# (verified via `npm view npm version`); tracked, not silently dropped.
#
# hermes-agent's own app-level node_modules DO have available fixes though —
# patch bumps only, applied directly since these are leaf/near-leaf deps with
# no API surface hermes-agent's own code touches beyond calling into them:
#   browserslist 4.28.6 -> 4.28.7  (CVE-2026-73088, CVE-2026-73089 — 4.28.7
#                                   already contains both fixes; see the
#                                   2026-09-21 correction below for why this
#                                   is 4.28.7, not npm's literal latest)
#   nanoid       3.3.17 -> 3.3.19  (CVE-2026-67213; transitive dep of both
#                                   sanitize-html and vite under /opt/hermes)
#
# 2026-09-21 correction: an earlier same-day pass bumped browserslist to
# 4.29.0 (npm's literal latest) instead of 4.28.7 (the oldest version that
# fixes both CVEs above) and it broke the build: the vendor's own
# /opt/hermes/.npmrc sets `min-release-age=14` (refuses any npm package
# published <14 days ago) with an explicit `min-release-age-exclude`
# allowlist — nanoid is on that allowlist (which is why the 3.3.19 bump above
# installs fine), browserslist is NOT, and 4.29.0 (published 2026-09-15, 6
# days before this build) fails the gate with `ETARGET ... no matching
# version found ... with a date before 9/7/2026`. 4.28.7 (published
# 2026-07-21) clears it easily and was always sufficient — CVE remediation
# should target the OLDEST version that closes the advisory, not registry
# latest: latest maximises unrelated churn and, here, gratuitously tripped a
# real supply-chain control for zero additional security benefit. Do NOT add
# browserslist to min-release-age-exclude — the fixed-and-old-enough version
# already exists, so there is no reason to punch a hole in the vendor's own
# freshness gate.
# 2026-09-21: nanoid's own latest is 6.0.1, a MAJOR jump (nanoid v4 dropped
# CommonJS support entirely — ESM-only) that would break these two `require()`-
# based CJS consumers outright. Staying on the 3.x line's latest patch (3.3.19,
# which already carries the CVE-2026-67213 fix) rather than bumping across that
# break — same "needs full upstream integration testing before a major jump"
# reasoning as starlette/cryptography below, not something skipped for
# convenience.
# 2026-09-14: hermes-agent v0.20.6 bumped its bundled vite to 8.3.0, which now
# peer-requires @vitejs/devtools@^0.7.1 — but the vendor still bundles
# @vitejs/devtools@0.4.12 (an internal mismatch in the vendor's own tree, not
# something our leaf patch touches or is responsible for reconciling). A plain
# `npm install` here does a full peer-dependency resolve of vite's directory
# and fails on that pre-existing conflict before it ever gets to installing
# nanoid. --legacy-peer-deps skips peer resolution for this single leaf-level
# override, matching the narrow "just bump nanoid, touch nothing else" intent
# below (vite/devtools' own compatibility is the vendor's concern, not ours).
# No-op against the currently pinned v0.20.1 (no such conflict there), so
# safe to leave in place regardless of which HERMES_IMAGE is pinned.
RUN npm install --prefix /opt/hermes browserslist@4.29.0 \
    && npm install --prefix /opt/hermes/node_modules/sanitize-html nanoid@3.3.19 \
    && npm install --prefix /opt/hermes/node_modules/vite nanoid@3.3.19 --legacy-peer-deps

# 2026-09-08: uv/uvx (vendored Rust binaries used for the ddgs/tornado/etc.
# venv installs above) shipped at 0.11.6 in the upstream base image, carrying
# two transitive-dependency CVEs (quinn-proto GHSA-4w2j-m93h-cj5j, rustls-webpki
# GHSA-82j2-j2ch-gfr8) fixed further upstream. `uv self update` refuses to run
# ("installed through an external package manager") since the base image
# installed it via a distro/vendor package rather than the official
# installer, so replace the binaries directly via astral-sh's own installer
# instead — same official release artifact `self update` would have fetched.
RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/usr/local/bin UV_NO_MODIFY_PATH=1 sh

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

# Standalone/cron Telegram delivery silently ignored telegram.extra.base_url,
# defaulting to a direct api.telegram.org connection that Hermes's own
# NO_PROXY deliberately keeps un-proxied — see patch script header for the
# full root cause (every scheduled delivery failed silently for days).
COPY docker/bots/hermes/patch_telegram_send_base_url.py /tmp/patch_telegram_send_base_url.py
RUN /opt/hermes/.venv/bin/python3 /tmp/patch_telegram_send_base_url.py \
    && rm /tmp/patch_telegram_send_base_url.py

# slack_sdk's AsyncSocketModeClient reuses one aiohttp.ClientSession across
# every reconnect; close() (called on some non-final disconnects) permanently
# closes it, and every connect() retry after that raises "RuntimeError:
# Session is closed" forever -- see patch script header for the full trace
# (upstream slackapi/python-slack-sdk#1913). This patch is a partial
# mitigation, not a complete fix for the underlying race -- see the header.
COPY docker/bots/hermes/patch_slack_session_recreate.py /tmp/patch_slack_session_recreate.py
RUN /opt/hermes/.venv/bin/python3 /tmp/patch_slack_session_recreate.py \
    && rm /tmp/patch_slack_session_recreate.py

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

# Item 9 — Dashboard bridge: re-exposes Hermes's loopback-bound dashboard (127.0.0.1,
# required by the vendor's v0.15.1+ auth gate — see the HERMES_DASHBOARD_HOST comment
# in docker-compose.yml) on a network-reachable port so gateway's TCP forwarder
# (gateway/ingest_api/lifespan.py) can actually reach it. Without this, every dashboard
# request 502s — see gateway/tests/test_security_regressions_v1_2.py
# TestHermesDashboardBridgeReachability.
COPY docker/bots/hermes/s6/dashboard-bridge  /etc/s6-overlay/s6-rc.d/agentshroud-dashboard-bridge
COPY docker/bots/hermes/dashboard_bridge.py  /usr/local/bin/agentshroud-dashboard-bridge.py

# Docker relay — dumb TCP passthrough to docker-socket-proxy on a loopback port.
# Connecting the Docker CLI directly to docker-socket-proxy:2375 over TCP fails
# with a spurious 405 on the CLI's second request on the connection (the
# version GET that follows its _ping negotiation probe), which silently
# disabled the sandboxed terminal tool for every Hermes cron job
# (check_terminal_requirements returns False) — see docker_proxy_relay.py's
# docstring for the full investigation. DOCKER_HOST is pointed at this relay
# (127.0.0.1, same network namespace as the terminal tool) instead of
# docker-socket-proxy directly.
COPY docker/bots/hermes/s6/docker-relay      /etc/s6-overlay/s6-rc.d/agentshroud-docker-relay
COPY docker/bots/hermes/docker_proxy_relay.py /usr/local/bin/agentshroud-docker-relay.py

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

# SSH-write-file helper — same plain-HTTP-off-argv pattern as agentshroud-ssh-exec.sh,
# for the structured /ssh/write_file endpoint (writes file content, not shell commands).
COPY docker/scripts/agentshroud-ssh-write-file.sh /usr/local/bin/agentshroud-ssh-write-file.sh

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
             /usr/local/bin/agentshroud-ssh-write-file.sh \
             /usr/local/bin/agentshroud-dashboard-bridge.py \
             /usr/local/bin/agentshroud-docker-relay.py \
             /etc/s6-overlay/s6-rc.d/agentshroud-crashwatch/run \
             /etc/s6-overlay/s6-rc.d/agentshroud-heartbeat/run \
             /etc/s6-overlay/s6-rc.d/agentshroud-dashboard-bridge/run \
             /etc/s6-overlay/s6-rc.d/agentshroud-docker-relay/run \
 && mkdir -p /app/config-defaults /usr/local/lib/agentshroud \
 && chmod 755 /usr/local/lib/agentshroud/render_md_email.py \
 && chmod 755 /usr/local/lib/agentshroud/resolve_model.py \
 && chown -R 10000:10000 /app/config-defaults \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-crashwatch \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-heartbeat \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-dashboard-bridge \
 && touch /etc/s6-overlay/s6-rc.d/user/contents.d/agentshroud-docker-relay

# OCI image label — AgentShroud's own product version wrapping this vendor
# image, NOT Hermes's upstream version (that's HERMES_VERSION in
# docker/versions.env, unrelated namespace). AGENTSHROUD_VERSION comes from
# docker/versions.env via docker-compose.yml's build.args, kept in sync with
# gateway/__init__.py's __version__ by scripts/sync-version.sh. This image
# previously had no AgentShroud version label at all — gateway/soc/services.py
# reads this for the SOC dashboard's service list.
ARG AGENTSHROUD_VERSION=dev
LABEL org.opencontainers.image.vendor="AgentShroud"
LABEL org.opencontainers.image.version="${AGENTSHROUD_VERSION}"
LABEL org.opencontainers.image.source="https://github.com/idallasjlabs/agentshroud"

# Port 9119: Hermes dashboard (served by s6 dashboard service when HERMES_DASHBOARD=1,
#            loopback-only — see HERMES_DASHBOARD_HOST in docker-compose.yml)
# Port 9120: Dashboard bridge — re-exposes 9119 for cross-container reachability
# Port 8642: OpenAI-compatible API server (enabled, requires API_SERVER_KEY)
EXPOSE 8642 9119 9120

# Healthcheck: probe the OpenAI-compatible API /health endpoint on 8642.
# v0.15.1 moved dashboard auth behind an auth gate; 9119 is no longer reliable.
# start_period=120s allows s6 init + skill sync + gateway startup to complete.
HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8642/health || exit 1

# Keep the image's own entrypoint (/init → main-wrapper.sh). CMD is passed as
# args to main-wrapper.sh: if it's an executable it runs via s6-setuidgid hermes.
CMD ["/usr/local/bin/start-hermes.sh"]
