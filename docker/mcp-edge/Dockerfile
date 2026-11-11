# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# agentshroud-mcp-edge — the internet-facing Inbound MCP Edge (SCRUM-215).
#
# A protocol terminator only: the MCP SDK's Streamable HTTP + OAuth routes, with
# every decision forwarded to the gateway's /edge/v1/rpc door. The image carries
# exactly the five modules that path imports (edge_app -> edge_jwt -> store, plus
# descriptors for the startup manifest check) and config/inbound-edge/. It holds
# no signing key, no gateway policy code and no tool facades — service.py,
# call_pipeline.py and oauth_service.py are deliberately absent.
#
# Build (repo root as context): docker build -f docker/mcp-edge/Dockerfile -t agentshroud-mcp-edge:dev .
#
# Base image pinned to the same python:3.13-slim digest as gateway/Dockerfile
# (SCRUM-100 supply-chain pinning); the Sunday upgrade refreshes both together.
# IEC 62443: FR3 (System Integrity), FR5 (Restricted Data Flow).

# === Build stage: resolve wheels against the gateway lockfile ===
FROM python:3.13-slim@sha256:70729b46c69b4f1e97c4822c1af3df53a1476cf5ddc6c087c0c10bc3a5678c2f AS builder

ENV PIP_ROOT_USER_ACTION=ignore \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build
COPY gateway/requirements.lock /build/requirements.lock

# Direct dependencies of the edge modules, pinned to gateway/requirements.lock;
# the lockfile is also the constraint set for every transitive dependency.
# --only-binary keeps a compiler out of the build. The freeze check fails the
# build if anything installed is not pinned to exactly the locked version.
RUN pip install --only-binary=:all: --prefix=/install -c requirements.lock \
        "mcp==2.3.0" \
        "pyjwt[crypto]==2.15.1" \
        "cryptography==50.0.2" \
        "httpx==0.28.1" \
        "aiosqlite==0.22.1" \
        "uvicorn==0.54.0" \
        "starlette==1.7.0" \
        "jsonschema==4.26.0" \
        "pyyaml==6.0.3" \
    && python -m pip freeze --path /install/lib/python3.13/site-packages \
       | tr 'A-Z_.' 'a-z--' > /build/installed.txt \
    && grep -E '^[a-z0-9]' requirements.lock | tr 'A-Z_.' 'a-z--' > /build/locked.txt \
    && unlocked="$(grep -vxF -f /build/locked.txt /build/installed.txt || true)" \
    && if [ -n "$unlocked" ]; then \
         echo "mcp-edge: installed packages not pinned by gateway/requirements.lock:" >&2; \
         echo "$unlocked" >&2; exit 1; \
       fi

# === Runtime stage ===
FROM python:3.13-slim@sha256:70729b46c69b4f1e97c4822c1af3df53a1476cf5ddc6c087c0c10bc3a5678c2f

LABEL maintainer="Isaiah Dallas Jefferson, Jr. <idallasj@gmail.com>"
LABEL org.agentshroud.component="mcp-edge"
LABEL org.opencontainers.image.title="agentshroud-mcp-edge"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app \
    EDGE_PORT=8443

COPY --from=builder /install /usr/local

# Pick up Debian security fixes newer than the pinned digest (same as
# gateway/Dockerfile; without it Trivy's fixable-HIGH gate fails on base-OS
# packages such as zlib1g and apt). The runtime never installs anything after
# this: drop pip so the image carries no Python package manager for an attacker
# to use, then strip setuid/setgid bits (CIS Docker 4.8).
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && python -m pip uninstall -y pip \
    && find / -xdev -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true

WORKDIR /app
COPY gateway/__init__.py /app/gateway/__init__.py
COPY gateway/inbound_edge/__init__.py \
     gateway/inbound_edge/edge_app.py \
     gateway/inbound_edge/edge_jwt.py \
     gateway/inbound_edge/store.py \
     gateway/inbound_edge/descriptors.py \
     /app/gateway/inbound_edge/
COPY config/inbound-edge/ /app/config/inbound-edge/

# Numeric non-root user; no home directory and no login shell. Code is owned by
# root and read-only to the runtime user.
USER 10001:10001

EXPOSE 8443

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:%s/healthz' % os.environ.get('EDGE_PORT', '8443'), timeout=4).read()"]

ENTRYPOINT ["python", "-m", "gateway.inbound_edge.edge_app"]

# Repo commit this image was built from (compose build arg). Last so the
# per-commit ARG never invalidates cached layers above it.
ARG AGENTSHROUD_GIT_SHA=unknown
LABEL org.opencontainers.image.revision="${AGENTSHROUD_GIT_SHA}"
