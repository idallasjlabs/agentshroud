---
type: community
members: 42
---

# SecureBrowser Skill (2)

**Members:** 42 nodes

## Members
- [[2026-03 TeamPCP supply-chain attack on trivy tags]] - concept - .github/workflows/security-scan.yml
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM flag for dev Hermes]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Anti-security-theater value]] - rationale - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Benchmark regression job]] - code - .github/workflows/ci.yml
- [[CI pip-audit security-scan job]] - code - .github/workflows/ci.yml
- [[CI test job (pytest matrix, cov-fail-under 84)]] - code - .github/workflows/ci.yml
- [[CI workflow (ci.yml)]] - code - .github/workflows/ci.yml
- [[Colima sizing (prod 8 CPU12 GiB, dev 4 CPU9 GiB, from colima.yaml)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Collaborator workspace SOUL.md (Isaiah persona)]] - document - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Compose version label mismatch forces network recreate + stale endpoints]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Conduit root-relative ws-ticket fetch vs hermes Funnel path]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Current Focus (AgentShroud v1.7.x)]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[DAST scan job (Nuclei)]] - code - .github/workflows/ci.yml
- [[Decision no blanket revert to 2026-10-10 commit]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Docs drift  version consistency check]] - code - .github/workflows/ci.yml
- [[Duplicate Telegram bot polling (dev vs prod getUpdates 409)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Fieldflare shim (strip parallel_tool_callstool_choice, flatten schema unions)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Image signing & provenance (cosign keyless + syft SBOM attest)]] - code - .github/workflows/security-scan.yml
- [[Incident ConduitHermes instability 2026-10-16]] - document - INCIDENT_2026-10-16_conduit-outage.md
- [[Leak gate (ResourceWarning fatal on ubuntu-3.11 only)]] - rationale - .github/workflows/ci.yml
- [[Lint job (pinned blackisortflake8)]] - code - .github/workflows/ci.yml
- [[Nemotron in-band reasoning + Qwen-only no_think suffix bug]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[OpenClaw per-container memcg OOM kills]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[OpenClaw sandbox mode all-off stopgap (named volume vs bind-mount)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Per-bot Telegram token fallback to OpenClaw bot (egress notify  lifespan)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Prod Colima VM egress loss (root cause of 7.5h Hermes outage)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Proxy-layer inversion pattern]] - concept - docker/bots/openclaw/workspace/collaborator-workspace/SOUL.md
- [[Python dependency audit job]] - code - .github/workflows/security-scan.yml
- [[Run judged on state change, not steps completed]] - rationale - prompts/sunday-upgrade.md
- [[SOUL.md freshness check (90-day soul-updated)]] - code - .github/workflows/ci.yml
- [[Secret scanning job (gitleaks full history)]] - code - .github/workflows/ci.yml
- [[Security Scan workflow (security-scan.yml)]] - code - .github/workflows/security-scan.yml
- [[Semgrep --baseline-commit fail only on new findings]] - rationale - .github/workflows/security-scan.yml
- [[Semgrep SAST baselined gate]] - code - .github/workflows/security-scan.yml
- [[Seven-week no-op upgrade failure (2026-07-29 to 2026-09-15)]] - concept - prompts/sunday-upgrade.md
- [[Startup smoke tests (static)]] - code - .github/workflows/ci.yml
- [[StreamHead status propagation for streaming LLM proxy]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Trivy filesystem scan (SHA-pinned action)]] - code - .github/workflows/security-scan.yml
- [[asb setup_ephemeral_secrets clobber on killed extract (preserve-nonempty fix)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[lazydocker docker.sock connection leak via Colima ssh forward]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[patch_telegram_edit_message_date.py (KeyError 'date' on editMessageText)]] - code - INCIDENT_2026-10-16_conduit-outage.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecureBrowser_Skill_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_sunday-upgrade-apply.sh]]
- 3 edges to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_discover_upstream_versions.py]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]

## Top bridge nodes
- [[Incident ConduitHermes instability 2026-10-16]] - degree 23, connects to 3 communities
- [[Collaborator workspace SOUL.md (Isaiah persona)]] - degree 5, connects to 1 community
- [[Run judged on state change, not steps completed]] - degree 4, connects to 1 community
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - degree 3, connects to 1 community
- [[Startup smoke tests (static)]] - degree 2, connects to 1 community
