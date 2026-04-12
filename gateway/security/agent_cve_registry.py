# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Upstream Agent CVE Registry — tracks known CVEs in the wrapped agent (OpenClaw).

Each entry records the CVE metadata, AgentShroud mitigation status, and
the specific defense layer that addresses (or fails to address) the issue.
This data powers the SOC "CVE Intelligence" dashboard page and the daily
CVE report comparisons.

To add a new CVE: append to AGENT_CVE_REGISTRY with status and mitigation notes.
"""

from __future__ import annotations

from typing import Any

# Agent identity — the AI agent framework wrapped by AgentShroud.
WRAPPED_AGENT = "OpenClaw"

# Mitigation status values:
#   "fully_mitigated"    — AgentShroud defense-in-depth neutralizes this CVE
#   "partially_mitigated" — containment exists but a gap remains
#   "not_mitigated"       — no specific defense (upstream patch required)
MITIGATION_STATUS = ("fully_mitigated", "partially_mitigated", "not_mitigated")

AGENT_CVE_REGISTRY: list[dict[str, Any]] = [
    {
        "id": "CVE-2026-22171",
        "title": "Path Traversal in Feishu Media Download",
        "cvss": 8.2,
        "severity": "HIGH",
        "disclosed": "2026-03-18",
        "fixed_in": "2026.2.19",
        "description": (
            "Untrusted Feishu media keys are interpolated directly into temp file "
            "paths, enabling path traversal to write arbitrary files."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "Bot container runs read_only:true with noexec tmpfs. "
            "OPENCLAW_DISABLE_HOST_FILESYSTEM=true blocks native file access. "
            "file_sandbox.py validates all file I/O paths. "
            "Feishu extension is not enabled."
        ),
        "defense_layers": [
            "read_only container",
            "file_sandbox",
            "OPENCLAW_DISABLE_HOST_FILESYSTEM",
        ],
    },
    {
        "id": "CVE-2026-28460",
        "title": "Allowlist Bypass via Shell Line-Continuation",
        "cvss": 5.9,
        "severity": "MEDIUM",
        "disclosed": "2026-03-19",
        "fixed_in": "2026.2.22",
        "description": (
            "Shell line-continuation characters bypass the system.run allowlist, "
            "enabling command substitution inside approved wrappers."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "apply-patches.js denies exec/process tools for all non-owner agents. "
            "PromptGuard detects shell injection patterns. "
            "Seccomp default-deny profile blocks unexpected syscalls. "
            "OPENCLAW_SANDBOX_MODE=strict restricts shell execution."
        ),
        "defense_layers": ["tool_acl", "prompt_guard", "seccomp", "sandbox_mode"],
    },
    {
        "id": "CVE-2026-29607",
        "title": "Allow-Always Wrapper Persistence Bypass",
        "cvss": 6.4,
        "severity": "MEDIUM",
        "disclosed": "2026-03-19",
        "fixed_in": "2026.2.22",
        "description": (
            "The 'allow always' feature persists approval at the wrapper level, "
            "not the inner command. Attacker swaps inner payload for RCE."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud's ApprovalQueue binds approvals to exact action payload "
            "(category + target + hash), not wrapper-level. EgressFilter and "
            "EgressApproval re-evaluate every outbound request independently. "
            "ToolACL enforces per-user/per-group tool allowlists server-side."
        ),
        "defense_layers": ["approval_queue", "egress_filter", "tool_acl"],
    },
    {
        "id": "CVE-2026-32032",
        "title": "Arbitrary Shell Execution via SHELL Environment Variable",
        "cvss": 7.0,
        "severity": "HIGH",
        "disclosed": "2026-03-19",
        "fixed_in": "2026.2.22",
        "description": (
            "OpenClaw trusts the unvalidated SHELL env var from the host. "
            "Attacker injects a malicious SHELL path for arbitrary execution."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "Container env is explicitly declared in docker-compose.yml; SHELL is "
            "never set. Container is read_only:true. no-new-privileges:true + "
            "cap_drop:ALL prevents escalation. Bot on isolated network only."
        ),
        "defense_layers": ["container_isolation", "read_only", "no_new_privileges", "cap_drop"],
    },
    {
        "id": "CVE-2026-32025",
        "title": "WebSocket Brute-Force / ClawJacked (No Rate Limiting on Localhost)",
        "cvss": 7.5,
        "severity": "HIGH",
        "disclosed": "2026-03-19",
        "fixed_in": "2026.2.25",
        "description": (
            "Browser-origin WebSocket clients bypass origin checks on localhost. "
            "Attacker brute-forces gateway password at hundreds of guesses/second."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "Gateway binds to 127.0.0.1 only. Remote access via Tailscale VPN. "
            "Constant-time token comparison (hmac.compare_digest). Auth failure "
            "escalation: 3 failures in 60s triggers owner alert. "
            "256-bit gateway password (secrets.token_hex(32)). "
            "dangerouslyAllowHostHeaderOriginFallback=false."
        ),
        "defense_layers": [
            "localhost_binding",
            "tailscale",
            "hmac_auth",
            "auth_failure_escalation",
        ],
    },
    {
        "id": "CVE-2026-22172",
        "title": "WebSocket Scope Self-Declaration",
        "cvss": 9.9,
        "severity": "CRITICAL",
        "disclosed": "2026-03-20",
        "fixed_in": "2026.3.12",
        "description": (
            "Client declares operator.admin scopes during WebSocket handshake; "
            "server honors them without validation. Full admin takeover."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud does not use OpenClaw's native WS auth/scope for admin. "
            "All admin actions route through gateway RBAC (rbac.py + rbac_config.py) "
            "with server-side role assignment from verified Telegram/Slack identity. "
            "OpenClaw WS is internal-only (isolated Docker network)."
        ),
        "defense_layers": ["rbac", "server_side_roles", "network_isolation"],
    },
    {
        "id": "CVE-2026-32048",
        "title": "Sandbox Escape via sessions_spawn",
        "cvss": 7.5,
        "severity": "HIGH",
        "disclosed": "2026-03-21",
        "fixed_in": "2026.3.1",
        "description": (
            "Sandboxed session spawns child process that runs with sandbox.mode:off. "
            "Child escapes confinement entirely."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "apply-patches.js denies sessions_spawn/sessions_send for all "
            "collaborator and group agents. SubagentMonitor tracks spawns. "
            "OS-level container sandbox (read_only, cap_drop:ALL, seccomp, "
            "no-new-privileges, pids_limit:512) is unaffected by OpenClaw escape. "
            "ProgressiveLockdown escalates: 3 blocks=alert, 5=rate limit, 10=suspend."
        ),
        "defense_layers": [
            "tool_acl",
            "subagent_monitor",
            "container_sandbox",
            "progressive_lockdown",
        ],
    },
    {
        "id": "CVE-2026-32049",
        "title": "Oversized Media Payload DoS",
        "cvss": 7.5,
        "severity": "HIGH",
        "disclosed": "2026-03-21",
        "fixed_in": "2026.2.22",
        "description": (
            "Unauthenticated oversized media payloads crash the OpenClaw service. "
            "No authentication required."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "Gateway checks file_size on all inbound media objects and drops "
            "updates exceeding 50MB (AGENTSHROUD_MAX_MEDIA_BYTES). "
            "_forward_file_download streams in 64KB chunks with abort at limit. "
            "limit_request_body middleware enforces 1MB on API requests including "
            "chunked transfers. Container mem_limit + auto-restart as backstop."
        ),
        "defense_layers": [
            "media_size_guard",
            "streaming_download_limit",
            "request_body_limit",
            "mem_limit",
        ],
    },
    {
        "id": "CVE-2026-32922",
        "title": "Token Scope Expansion via device.token.rotate",
        "cvss": 9.9,
        "severity": "CRITICAL",
        "disclosed": "2026-03-29",
        "fixed_in": "2026.3.29",
        "description": (
            "device.token.rotate fails to constrain newly minted token scopes to "
            "the caller's existing scope set, allowing any paired device to self-issue "
            "operator.admin tokens — full admin takeover without credentials."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud does not use OpenClaw's device token system for authorization. "
            "All admin actions require RBAC role from verified Telegram/Slack identity "
            "(rbac.py + rbac_config.py). OpenClaw WS endpoint is on the isolated "
            "internal Docker network unreachable externally."
        ),
        "defense_layers": ["rbac", "server_side_roles", "network_isolation", "verified_identity"],
    },
    {
        "id": "CVE-2026-35660",
        "title": "Insufficient Access Control in Gateway /reset Endpoint",
        "cvss": 8.1,
        "severity": "HIGH",
        "disclosed": "2026-03-30",
        "fixed_in": "2026.3.23",
        "description": (
            "The Gateway agent /reset endpoint accepts operator.write scope where "
            "operator.admin is required, allowing scope-downgraded callers to reset "
            "arbitrary admin sessions."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud RBAC enforces check_permission() on every SOC endpoint "
            "server-side; OpenClaw's internal /reset route is unreachable directly. "
            "ProgressiveLockdown escalates repeated unauthorized access attempts. "
            "Internal Docker network prevents external callers from reaching the route."
        ),
        "defense_layers": ["rbac", "check_permission", "progressive_lockdown", "network_isolation"],
    },
    {
        "id": "CVE-2026-35650",
        "title": "Environment Variable Override Bypass",
        "cvss": 6.3,
        "severity": "MEDIUM",
        "disclosed": "2026-03-30",
        "fixed_in": "2026.3.22",
        "description": (
            "Inconsistent sanitization paths in OpenClaw's env-var handling allow "
            "an attacker to inject environment variable overrides that bypass the "
            "shared host environment policy."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "All container environment variables are explicitly declared in "
            "docker-compose.yml; no host env passthrough. "
            "no-new-privileges:true + cap_drop:ALL + read_only:true prevent "
            "privilege escalation even if env vars are manipulated. "
            "OPENCLAW_SANDBOX_MODE=strict and OPENCLAW_DISABLE_HOST_FILESYSTEM=true "
            "prevent leveraging injected vars for meaningful access."
        ),
        "defense_layers": ["container_isolation", "read_only", "no_new_privileges", "cap_drop"],
    },
    {
        "id": "CVE-2026-35668",
        "title": "Path Traversal in Sandbox Enforcement (unnormalized mediaUrl)",
        "cvss": 7.7,
        "severity": "HIGH",
        "disclosed": "2026-03-31",
        "fixed_in": "2026.3.24",
        "description": (
            "normalizeSandboxMediaParams fails to normalize mediaUrl/fileUrl "
            "before validating against mediaLocalRoots, letting a sandboxed agent "
            "read arbitrary files from other agents' workspaces."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "OPENCLAW_DISABLE_HOST_FILESYSTEM=true prevents native file access. "
            "file_sandbox.py validates and normalizes all file I/O paths independently. "
            "Bot container runs read_only:true with noexec tmpfs; no persistent workspace "
            "writable outside mounted volumes. Collaborator agents cannot reach owner's "
            "workspace (per-collab workspace isolation)."
        ),
        "defense_layers": ["file_sandbox", "OPENCLAW_DISABLE_HOST_FILESYSTEM", "read_only_container", "workspace_isolation"],
    },
    {
        "id": "CVE-2026-35625",
        "title": "Privilege Escalation via Silent Local Auth Reconnect",
        "cvss": 8.5,
        "severity": "HIGH",
        "disclosed": "2026-04-01",
        "fixed_in": "2026.3.25",
        "description": (
            "Silent local shared-auth reconnects auto-approve scope-upgrade requests, "
            "widening a paired device from operator.read to operator.admin without user "
            "confirmation — enabling RCE on the host node."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud RBAC does not use OpenClaw's pairing scope system for access "
            "control; all roles are resolved server-side from verified Telegram/Slack "
            "identity. Local shared-auth is irrelevant as the WS endpoint is on an "
            "isolated Docker network (localhost-only binding). "
            "dangerouslyAllowHostHeaderOriginFallback=false blocks origin bypass."
        ),
        "defense_layers": ["rbac", "verified_identity", "localhost_binding", "network_isolation"],
    },
    {
        "id": "CVE-2026-35629",
        "title": "Server-Side Request Forgery (SSRF) in Channel Extension fetch()",
        "cvss": 7.5,
        "severity": "HIGH",
        "disclosed": "2026-04-01",
        "fixed_in": "2026.3.25",
        "description": (
            "Multiple channel extensions make unguarded fetch() calls to configured "
            "base URLs without SSRF protection, allowing an attacker to rebind "
            "requests to internal destinations."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "All outbound traffic routes through AgentShroud EgressFilter + EgressApproval; "
            "no direct fetch() calls leave the container unproxied. "
            "DNSFilter blocks internal RFC-1918 targets at the resolver. "
            "NetworkValidator checks destination IPs against the allowlist before any "
            "connection is made. HTTP_PROXY/HTTPS_PROXY force all traffic through the "
            "AgentShroud gateway proxy on :8181."
        ),
        "defense_layers": ["egress_filter", "egress_approval", "dns_filter", "network_validator"],
    },
    {
        "id": "CVE-2026-34512",
        "title": "Improper Access Control in Session Kill Endpoint",
        "cvss": 7.3,
        "severity": "HIGH",
        "disclosed": "2026-04-02",
        "fixed_in": "2026.3.25",
        "description": (
            "The HTTP /sessions/:sessionKey/kill route accepts any bearer-authenticated "
            "user and invokes killSubagentRunAdmin without validating caller ownership "
            "or operator scope, allowing session hijacking."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "apply-patches.js denies sessions_spawn/sessions_send for all collaborator "
            "and group agents at the tool-ACL layer. SubagentMonitor tracks and limits "
            "spawn activity. The OpenClaw HTTP routes are on the isolated internal network "
            "and are not reachable from outside the container stack."
        ),
        "defense_layers": ["tool_acl", "subagent_monitor", "network_isolation"],
    },
    {
        "id": "CVE-2026-35669",
        "title": "Privilege Escalation via Plugin HTTP Auth Scope Minting",
        "cvss": 8.0,
        "severity": "HIGH",
        "disclosed": "2026-04-03",
        "fixed_in": "2026.3.25",
        "description": (
            "Gateway-authenticated plugin HTTP routes incorrectly mint operator.admin "
            "runtime scope regardless of the scope granted to the caller, providing a "
            "straightforward privilege escalation path."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud does not use OpenClaw's runtime scope minting for admin "
            "authorization. All admin actions require RBAC role from verified "
            "Telegram/Slack identity. Plugin HTTP routes are on the isolated internal "
            "Docker network; external callers never reach them directly."
        ),
        "defense_layers": ["rbac", "server_side_roles", "network_isolation"],
    },
    {
        "id": "CVE-2026-32051",
        "title": "Privilege Escalation (operator.write reaches owner-only surfaces)",
        "cvss": 8.8,
        "severity": "HIGH",
        "disclosed": "2026-03-21",
        "fixed_in": "2026.3.1",
        "description": (
            "Operator with operator.write scope reaches owner-only admin surfaces, "
            "breaking the trust boundary between operator and owner roles."
        ),
        "status": "fully_mitigated",
        "mitigation": (
            "AgentShroud RBAC defines OWNER > ADMIN > OPERATOR > COLLABORATOR > STRANGER. "
            "check_permission() enforced on every SOC endpoint server-side. "
            "Role assignment from verified platform identity (Telegram UID / Slack ID). "
            "PrivacyPolicy enforces PRIVATE/SHARED/GROUP_ONLY content tiers."
        ),
        "defense_layers": ["rbac", "check_permission", "verified_identity", "privacy_policy"],
    },
]


def get_agent_cve_summary() -> dict[str, Any]:
    """Return a summary of the wrapped agent CVE registry.

    Used by the SOC dashboard and daily report.
    """
    total = len(AGENT_CVE_REGISTRY)
    by_status = {"fully_mitigated": 0, "partially_mitigated": 0, "not_mitigated": 0}
    by_severity = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for cve in AGENT_CVE_REGISTRY:
        by_status[cve["status"]] = by_status.get(cve["status"], 0) + 1
        by_severity[cve["severity"]] = by_severity.get(cve["severity"], 0) + 1

    return {
        "wrapped_agent": WRAPPED_AGENT,
        "total_cves": total,
        "by_status": by_status,
        "by_severity": by_severity,
        "cves": AGENT_CVE_REGISTRY,
    }
