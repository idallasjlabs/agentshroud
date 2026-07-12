# Plan: Proxying HexStrike AI MCP Agents via AgentShroud

Status: **PLANNING ONLY — no implementation yet.** This document captures the design so it can
be revisited before an implementation branch is opened.

## Context

**Why:** HexStrike AI (https://github.com/0x4m4/hexstrike-ai) is an offensive-security MCP
framework: an AI agent (Claude/GPT/Copilot) drives 150+ pentest tools (nmap, sqlmap,
metasploit, nuclei) through an MCP server that fronts an HTTP backend exposing
`POST /api/command` — **arbitrary shell execution, no authentication**. The goal is to place
AgentShroud as a governance proxy in front of these agents so every tool invocation is
inspected, approved, and tamper-evidently logged **without breaking HexStrike's ability to
actually scan authorized targets**.

Feasibility conclusion: **YES, and ~80% of the machinery already exists** — AgentShroud ships a
production MCP proxy today. The work is configuration + policy + a scoped engagement-network
topology, not a build-from-scratch.

**Decision recorded (from user):** Proxy and inspect all traffic; use a **permanent egress
allowlist scoped to HexStrike's engagement targets** with full logging/monitoring — do NOT
hard-block. The refinement layered in below: the HTTP egress filter inspects HTTP-layer scans;
raw L3/L4 scan packets (nmap SYN/UDP, ICMP, msf) are logged at packet level (pcap/Falco), since
an HTTP CONNECT proxy structurally cannot carry raw packets.

---

## What already exists (no build needed)

AgentShroud has a complete, production-wired MCP proxy. Registering HexStrike is a config task.

| Capability | Location | Notes |
|---|---|---|
| MCP interceptor (stdio + HTTP/SSE) | `gateway/proxy/mcp_proxy.py:357` `process_tool_call` | Intercepts JSON-RPC `tools/call` |
| Transports | `mcp_proxy.py:92` (stdio), `:158` (HTTP/SSE) | `StdioConnection`, `HttpSseConnection` |
| Server registry / config | `gateway/proxy/mcp_config.py:66` `MCPServerConfig`, `:97` `from_dict` | Parsed from `agentshroud.yaml` `mcp_proxy.servers:` |
| Startup wiring | `gateway/ingest_api/lifespan.py:1257-1276` | Loads servers at boot |
| stdio MITM client (**fail-closed**) | `docker/scripts/mcp-proxy-wrapper.js:135,148` | Gateway unreachable → tool call BLOCKED |
| Gateway HTTP endpoints | `gateway/ingest_api/main.py:676` `/mcp/proxy`, `:777` `/mcp/result` | Auth + trusted-identity re-resolve |
| Approval (risk tiers) | `gateway/approval_queue/enhanced_queue.py:111` `requires_approval`; tiers `gateway/ingest_api/config.py:191-265` | `critical`/`high` → human approval + Telegram |
| Permissions engine | `gateway/proxy/mcp_permissions.py:619` `check_all` | ⚠️ **default-allow** posture |
| Injection/PII inspector | `gateway/proxy/mcp_inspector.py:140` `inspect_tool_call` | Scans params + results |
| Tamper-evident audit | `gateway/proxy/mcp_audit.py:55` SHA-256 hash chain | Per tool-call |
| Egress filter | `gateway/security/egress_filter.py:163` `check`; config `egress_config.py` | Default-deny, allowlist-only |
| Existing HTTP/SSE MCP servers (pattern to copy) | `agentshroud.yaml:265-298` (`devonthink`, `mac-messages`) | Same shape HexStrike will use |

---

## The core tension (and its resolution)

AgentShroud is *built to prevent* what HexStrike *does*:
- Egress is **default-deny, allowlist-only**, ports limited to `[80,443,465,587,993]`
  (`egress_config.py:198`); IP-literal + odd-port destinations auto-flagged RED
  (`egress_approval.py:238`).
- The bot's network `agentshroud-isolated` is `internal: true` (`docker/docker-compose.yml:573`)
  — **no internet route at all**. HexStrike cannot run there and scan anything.
- `MCPPermissionManager` is **default-allow** (`mcp_permissions.py:178`) and `ToolACLEnforcer` is
  **not** wired into the MCP path (only the LLM path, `llm_proxy.py:1213`).

**Resolution — separate the two planes:**

1. **Control plane** (which tool, which params, which target) → runs *through* AgentShroud's MCP
   proxy. Fully inspected, approval-gated, hash-chain audited. This is where governance lives.
2. **Data plane** (the actual scan packets) → HexStrike gets its own **engagement network** with a
   real, firewall-scoped egress path to the authorized target CIDRs (the "permanent egress for
   HexStrike"), default-deny to everything else. Logged at packet level.

This preserves functionality (scans work) while making intent inspectable and auditable.

---

## Proposed architecture

```
 Owner-driven AI agent (OpenClaw / Claude)
        │  MCP tools/call  (JSON-RPC)
        ▼
 AgentShroud gateway  ── mcp_proxy.process_tool_call ──► approval → permissions →
        │                   inspector → egress check → SHA-256 audit
        │  (forwarded only if allowed; params PII-sanitized; result injection-scanned)
        ▼
 HexStrike MCP server (hexstrike_mcp.py, stdio)  ──►  hexstrike_server.py :8888  ──►  150+ tools
        │                                                                              │
        └────────────── engagement network (dedicated) ───────────────────────────────┘
                         nftables egress allowlist → authorized target CIDRs ONLY
                         default-deny to internet + agentshroud-internal/isolated
                         pcap + Falco + (optional) Suricata IDS on this network
```

**Traffic-plane matrix:**

| Layer | Carried by | Enforcement / logging |
|---|---|---|
| MCP control plane | `mcp_proxy.py` | approval + permissions + inspector + hash-chain audit |
| HTTP-layer scans (sqlmap, nuclei, HTTP probes) | gateway HTTP CONNECT proxy `http_proxy.py:8181` | permanent egress allowlist (engagement scope) + `WebContentScanner` |
| Raw L3/L4 scans (nmap SYN/UDP, ICMP, msf) | engagement network (not HTTP-proxiable) | nftables scope allowlist + pcap + Falco syscall monitor |

---

## Policy levers to configure (per engagement)

1. **Register HexStrike** under `agentshroud.yaml` `mcp_proxy.servers:` (copy the `devonthink`
   HTTP/SSE block at `:265`, or use `transport: stdio` + `command`/`args` fronted by
   `mcp-proxy-wrapper.js`).
2. **Classify every HexStrike tool `critical`/`high`** in `tool_risk.tool_classifications`
   (`gateway/ingest_api/config.py:191-265`) → forces human approval + Telegram per call.
   Closes the `default-allow` gap for offensive tools.
3. **Scope egress** — set the engagement target CIDRs/ports as the *only* permitted destinations
   for the HexStrike container (nftables on the engagement network), plus optionally
   `AGENTSHROUD_ALLOWED_IPS` / `AGENTSHROUD_ALLOWED_PORTS` for HTTP-layer scan traffic that
   transits the gateway. Default-deny everywhere else.
4. **Human-in-the-loop** — HexStrike is designed around human-in-the-loop via the LLM; keep it.
   Anything that writes/exploits/persists routes through the approval queue.
5. **Result injection scanning stays on** — `PromptGuard.scan_tool_result` (threshold 0.6,
   `prompt_guard.py:782`) + `ToolResultInjectionScanner` (`tool_result_injection.py:243`) protect
   the driving agent from injected instructions in scan output (banners, HTTP responses).
   ⚠️ Note the **FULL-trust owner bypass** (`pipeline.py:1034`) — owner-context tool results are
   audited but not hard-blocked; the plan should evaluate whether to tighten this for the
   offensive-tool path.

---

## Known integration gaps to document (not fix in this planning branch)

- **G1 — ToolACL not on MCP path.** `ToolACLEnforcer` (`tool_acl.py:206`) gates the LLM path only;
  MCP calls use `MCPPermissionManager`. Wiring `can_use_tool` into `MCPProxy.process_tool_call`
  would add rate-limit + private-tool ACL to HexStrike. (Design note only.)
- **G2 — MCP permission posture is default-allow** (`mcp_permissions.py:178`). Mitigated by
  lever #2 (explicit critical/high classification) rather than relying on default.
- **G3 — Owner FULL-trust tool-result bypass** (`pipeline.py:1034`). Decide policy for offensive
  tooling.
- **G4 — Raw-packet visibility.** HTTP egress filter can't see nmap/msf packets; requires
  pcap/Falco/Suricata on the engagement network. Falco is already in the stack (`docker/`).

---

## Deliverable & branch

- **Branch:** `plan/hexstrike-mcp-proxy` off `main` (planning only; no code).
- **Doc:** this file — the full design, to be expanded later with config snippets, an
  engagement-network compose topology sketch, an nftables scope example, and an IEC 62443 FR
  mapping: FR5 restricted data flow → engagement-network segmentation, FR6 timely response →
  hash-chain audit + Falco, FR7 resource availability → rate limits.
- **Jira:** log under the SCRUM board (epics 53/54) as a planning/spike ticket per the active
  tracking rule.

---

## Verification (of the planning deliverable, once implementation begins)

Since this branch produces **no runtime code**, verification is document-level + a dry
feasibility check:

1. **Trace the MCP path end-to-end in code** and confirm each cited file:line still exists
   (`mcp_proxy.py`, `mcp-proxy-wrapper.js`, `enhanced_queue.py`, `egress_filter.py`).
2. **Confirm the `devonthink` HTTP/SSE server block** in `agentshroud.yaml:265` loads at startup
   (`lifespan.py:1257`) — proves the registration mechanism HexStrike will reuse.
3. **Confirm `agentshroud-isolated` is `internal: true`** (`docker-compose.yml:573`) — proves the
   need for a separate engagement network.
4. **Peer review** the doc against the No-Security-Theater rules (every claim file:line-cited) and
   the two-plane separation before any implementation branch is opened.

## Out of scope (explicitly)

- No implementation, no `agentshroud.yaml` edits, no compose/network changes on this branch.
- No live HexStrike deployment; no scans run.
- Closing gaps G1–G3 is future implementation work, tracked but not done here.
