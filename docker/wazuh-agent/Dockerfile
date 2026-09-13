# Wazuh HIDS agent — standalone sidecar container.
#
# Split out of gateway/Dockerfile 2026-09-06: wazuh-agentd's compiled-in
# privilege-drop calls setgroups()+setgid()+setuid() to switch from root to
# the "wazuh" system user at startup — a call that unconditionally requires
# CAP_SETGID/CAP_SETUID as *effective* capabilities. The gateway container
# runs non-root from the moment it boots (no root phase ever exists there)
# under cap_drop: ALL, and three separate mechanisms to hand it that
# capability post-hoc all failed: docker-compose cap_add only reaches the
# bounding set for a non-root process, not its effective set; a matching
# primary GID doesn't help because setgroups() has no same-list exception the
# way setgid() does; and a setcap file capability failed outright with
# "unable to set CAP_SETFCAP effective capability" even under --privileged,
# a Colima/VM-level restriction on security.capability xattrs, not a Docker
# flag problem. Running wazuh-agentd from genuine root — its intended
# deployment model — sidesteps all of that: real root has every capability
# it needs, and it renounces them itself once dropped.
#
# SCRUM-101: 4.9.2 → 4.14.7 (latest 4.x; ships underscore >= 1.13, retiring
# the CVE-2021-23358 .trivyignore suppression, and clears accumulated
# agent-lib CVEs).
FROM python:3.13-slim@sha256:bffeb7bd6a85767587059c6ba23e1e9122078e3aa3fa836099171b9bb5a9bb00

ENV DEBIAN_FRONTEND=noninteractive
ARG WAZUH_VERSION=4.14.7

RUN mkdir -p /apt-dl/partial \
    && sed -i 's/^Signed-By:.*/Trusted: yes/' /etc/apt/sources.list.d/debian.sources \
    && apt-get update \
    && apt-get -o Dir::Cache::archives=/apt-dl install -y --no-install-recommends \
        curl ca-certificates gpg \
    && curl -sSfL https://packages.wazuh.com/key/GPG-KEY-WAZUH \
        | gpg --dearmor -o /usr/share/keyrings/wazuh.gpg \
    && echo "deb [trusted=yes signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" \
        > /etc/apt/sources.list.d/wazuh.list \
    && apt-get update \
    && WAZUH_MANAGER=127.0.0.1 apt-get -o Dir::Cache::archives=/apt-dl install -y --no-install-recommends \
        wazuh-agent=${WAZUH_VERSION}-1 \
    && rm -rf /apt-dl /var/lib/apt/lists/*

# Realign the package-created "wazuh" user/group onto uid/gid 1000 so FIM
# reads land on the same identity that owns the shared host bind mounts and
# named volumes (gateway's "agentshroud" user is also uid 1000) — otherwise
# wazuh-agentd, running as its own dropped "wazuh" user, can't read files
# the gateway container wrote.
RUN usermod -u 1000 wazuh && groupmod -g 1000 wazuh \
    && chown -R wazuh:wazuh /var/ossec

# Bake in ossec.conf (FIM on /app/gateway + Falco alert ingestion + security
# scan reports — see docker-compose.yml's wazuh-agent service for the exact
# shared mounts this expects).
COPY docker/wazuh/ossec.conf /var/ossec/etc/ossec.conf
# Pre-register agent key so wazuh-agentd starts without needing a live manager
RUN echo "001 agentshroud-gateway any c0000000000000000000000000000001" \
        > /var/ossec/etc/client.keys && \
    chmod 640 /var/ossec/etc/client.keys && \
    chown wazuh:wazuh /var/ossec/etc/client.keys

# Strip setuid/setgid bits repo-wide (CIS Docker Benchmark 4.8) — safe here:
# wazuh-agentd's privilege drop is a plain setuid()/setgid() syscall pair
# performed by the process itself while genuinely root, not a setuid-bit
# executable, so this hardening step doesn't interfere with it.
RUN find / -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true

# Deliberately no USER directive — wazuh-agentd must start as root so its
# own internal privilege drop (-u wazuh -g wazuh, both now uid/gid 1000) can
# succeed; it renounces root itself within the first seconds of running.
ENTRYPOINT ["/var/ossec/bin/wazuh-agentd"]
CMD ["-f"]
