---
source_file: "/Users/ijefferson.admin/Development/agentshroud/docs/vault/03 - Configuration/Dockerfile.gateway.md"
type: "document"
community: "Module Group 345"
location: "gateway/Dockerfile"
tags:
  - graphify/document
  - graphify/EXTRACTED
  - community/Module_Group_345
---

# Dockerfile.gateway

## Connections
- [[All Dependencies (gateway Python + bot Node.js + system packages)]] - `uses` [EXTRACTED]
- [[ClamAV (malware scanning — pre-installed in gateway image)]] - `installs` [EXTRACTED]
- [[Docker Security Hardening (non-root, no setuid, seccomp, read-only rootfs)]] - `implements` [EXTRACTED]
- [[OpenSCAP (compliance scanning — pre-installed in gateway image)]] - `installs` [EXTRACTED]
- [[Python 3.13 Runtime (multi-stage Docker build)]] - `defines` [EXTRACTED]
- [[Trivy (container vulnerability scanning — pre-installed in gateway image)]] - `installs` [EXTRACTED]
- [[docker-compose.yml (primary Docker Compose — services, networks, volumes, secrets)]] - `referenced_by` [EXTRACTED]
- [[spaCy NLP (en_core_web_sm — pre-installed for PII detection)]] - `installs` [EXTRACTED]

#graphify/document #graphify/EXTRACTED #community/Module_Group_345