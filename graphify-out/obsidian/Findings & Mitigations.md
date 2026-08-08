---
source_file: "docs/planning/v0.8/container-security-audit-v0.8.0.md"
type: "document"
community: "Planning Docs"
location: "L45"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Planning_Docs
---

# Findings & Mitigations

## Connections
- [[Container Security Audit — AgentShroud v0.8.0]] - `contains` [EXTRACTED]
- [[🔴 C1 SSH Config Bypass (`-F devnull`)]] - `contains` [EXTRACTED]
- [[🔴 C2 Raw TCP to Host Port 22]] - `contains` [EXTRACTED]
- [[🔴 C3 PID1 Environment Readable (`proc1environ`)]] - `contains` [EXTRACTED]
- [[🟠 H1 Writable `~.ssh` Directory]] - `contains` [EXTRACTED]
- [[🟠 H2 Secrets in Environment Variables]] - `contains` [EXTRACTED]
- [[🟠 H3 `resolv.conf` Leaks DNS Architecture]] - `contains` [EXTRACTED]
- [[🟠 H4 All Internal Container Ports Reachable]] - `contains` [EXTRACTED]
- [[🟡 M1 `apt` Available (Permissions Blocked)]] - `contains` [EXTRACTED]
- [[🟡 M2 `perl` and `bash` Available as Interpreters]] - `contains` [EXTRACTED]
- [[🟡 M3 `proc1ns` Namespace Files Visible]] - `contains` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Planning_Docs