---
type: community
members: 40
---

# DataExfilVolumeGuard

**Members:** 40 nodes

## Members
- [[2026-03 TeamPCP supply-chain attack on trivy tags]] - concept - .github/workflows/security-scan.yml
- [[AGENTSHROUD_HERMES_DISABLE_TELEGRAM flag for dev Hermes]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[CI DAST scan job (Nuclei)]] - code - .github/workflows/ci.yml
- [[CI SOUL.md freshness check (90 days)]] - code - .github/workflows/ci.yml
- [[CI Workflow]] - code - .github/workflows/ci.yml
- [[CI benchmark regression job]] - code - .github/workflows/ci.yml
- [[CI docs drift  version consistency check]] - code - .github/workflows/ci.yml
- [[CI gitleaks secret scanning job]] - code - .github/workflows/ci.yml
- [[CI lint job (pinned blackisortflake8)]] - code - .github/workflows/ci.yml
- [[CI security-scan job (pip-audit)]] - code - .github/workflows/ci.yml
- [[CI startup smoke tests (static)]] - code - .github/workflows/ci.yml
- [[CI test job (pytest matrix, coverage gate 84%)]] - code - .github/workflows/ci.yml
- [[Colima sizing (prod 8 CPU12 GiB, dev 4 CPU9 GiB, from colima.yaml)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Compose version label mismatch forces network recreate + stale endpoints]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Conduit root-relative ws-ticket fetch vs hermes Funnel path]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Decision no blanket revert to 2026-10-10 commit]] - rationale - INCIDENT_2026-10-16_conduit-outage.md
- [[Dev 2026-10-11 handoff false green (PASS with 0 images scanned)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Drift PR (result gate, prod gate, wrapper, launchd install.sh)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Duplicate Telegram bot polling (dev vs prod getUpdates 409)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Fieldflare shim (strip parallel_tool_callstool_choice, flatten schema unions)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Image signing & provenance (cosign keyless + syft SBOM attest)]] - code - .github/workflows/security-scan.yml
- [[Incident ConduitHermes instability 2026-10-16]] - document - INCIDENT_2026-10-16_conduit-outage.md
- [[Leak gate fatal only on ubuntu+py3.11]] - rationale - .github/workflows/ci.yml
- [[Nemotron in-band reasoning + Qwen-only no_think suffix bug]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[OpenClaw per-container memcg OOM kills]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[OpenClaw sandbox mode all-off stopgap (named volume vs bind-mount)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Per-bot Telegram token fallback to OpenClaw bot (egress notify  lifespan)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Prod Colima VM egress loss (root cause of 7.5h Hermes outage)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Python dependency audit job]] - code - .github/workflows/security-scan.yml
- [[Security Scan workflow (security-scan.yml)]] - code - .github/workflows/security-scan.yml
- [[Semgrep --baseline-commit fail only on new findings]] - rationale - .github/workflows/security-scan.yml
- [[Semgrep SAST baselined gate]] - code - .github/workflows/security-scan.yml
- [[StreamHead status propagation for streaming LLM proxy]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[Trivy filesystem scan (SHA-pinned action)]] - code - .github/workflows/security-scan.yml
- [[asb setup_ephemeral_secrets clobber on killed extract (preserve-nonempty fix)]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[check_benchmark_regression.py]] - code - scripts/check_benchmark_regression.py
- [[lazydocker docker.sock connection leak via Colima ssh forward]] - concept - INCIDENT_2026-10-16_conduit-outage.md
- [[main()_9]] - code - scripts/check_benchmark_regression.py
- [[patch_telegram_edit_message_date.py (KeyError 'date' on editMessageText)]] - code - INCIDENT_2026-10-16_conduit-outage.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/DataExfilVolumeGuard
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY__wrap_response() (2)]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY__make_sanitizer()]]
- 1 edge to [[_COMMUNITY_Sunday Upgrade prompt]]

## Top bridge nodes
- [[Incident ConduitHermes instability 2026-10-16]] - degree 23, connects to 2 communities
- [[Drift PR (result gate, prod gate, wrapper, launchd install.sh)]] - degree 4, connects to 2 communities
- [[CI DAST scan job (Nuclei)]] - degree 2, connects to 1 community
- [[CI startup smoke tests (static)]] - degree 2, connects to 1 community
- [[Hermes pin silent no-op (0.21.5 while upstream 0.22.2)]] - degree 2, connects to 1 community
