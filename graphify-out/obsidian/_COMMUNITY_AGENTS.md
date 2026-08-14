---
type: community
members: 40
---

# AGENTS.md

**Members:** 40 nodes

## Members
- [[CI Workflow]] - code - .github/workflows/ci.yml
- [[DAST Scan (Nuclei) Job]] - code - .github/workflows/ci.yml
- [[Dependabot Configuration]] - code - .github/dependabot.yml
- [[Gateway Service]] - code - docker/docker-compose.yml
- [[Hermes Agent Service]] - code - docker/docker-compose.yml
- [[Hermes Cannot Force-Switch to Custom-Named Local Model (Gap 8)]] - rationale - docs/planning/v1.2/LOCAL_LLM_REVIEW.md
- [[Hermes Dashboard Bridge Port Wiring (9119-9120)]] - rationale - docker/docker-compose.yml
- [[Hermes Dev Workflow Skill (i-hdev)]] - document - docker/config/hermes/skills/i-hdev/SKILL.md
- [[How to start a task]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[Jira Ticket Per Dev Batch (Standing Rule)]] - rationale - docker/config/hermes/skills/i-hdev/SKILL.md
- [[LLMProxy (llm_proxy.py)]] - code - gateway/proxy/llm_proxy.py
- [[LOCAL_MODEL_ROUTES Dict]] - code - gateway/proxy/llm_proxy.py
- [[Leak Gate Scoped to ubuntu+3.11]] - rationale - .github/workflows/ci.yml
- [[Monitoring progress]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[Multi-LLM Review Loop (Codex+Gemini review, Claude fixer)]] - concept - docker/config/hermes/skills/i-hdev/SKILL.md
- [[OpenClaw Bot Service]] - code - docker/docker-compose.yml
- [[OpenClaw Dev Workflow Skill (i-odev)]] - document - docker/config/hermes/skills/i-odev/SKILL.md
- [[Presidio-Anonymizer 2.2.364 Version Pin-Out]] - rationale - .github/dependabot.yml
- [[Release Workflow_1]] - code - .github/workflows/release.yml
- [[Source of truth_2]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[Starting a Development Task via Hermes  OpenClaw]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[Status ready to use, with 4 known gaps (see below)]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[TagVersion Sync Verification]] - rationale - .github/workflows/release.yml
- [[Things that will make a task halt and ask you, not fail silently]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[Three-Tier Network Segmentation (IEC 62443 FR5)]] - rationale - docker/docker-compose.yml
- [[Turbo Fieldflare Local Backend]] - concept - docs/planning/v1.2/LOCAL_LLM_REVIEW.md
- [[What happens automatically (confirmed real, in]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[What is not currently automated (the 4 gaps)]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[cryptography=50.0.0 Security Floor]] - rationale - gateway/requirements.txt
- [[ensure_local_model_available()]] - code - scripts/switch_model.sh
- [[gatewayrequirements.txt Dependency File]] - code - gateway/requirements.txt
- [[hermes-openclaw-dev-workflow]] - document - docs/runbooks/hermes-openclaw-dev-workflow.md
- [[normalize_cloud_ref()]] - code - scripts/switch_model.sh
- [[preflight_local()]] - code - scripts/switch_model.sh
- [[switch_model.sh]] - code - scripts/switch_model.sh
- [[switch_model.sh script]] - code - scripts/switch_model.sh
- [[upsert_env_value()]] - code - scripts/switch_model.sh
- [[usage()_4]] - code - scripts/switch_model.sh
- [[verify_both_bots_healthy()]] - code - scripts/switch_model.sh
- [[wait_for_local_model()]] - code - scripts/switch_model.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AGENTSmd
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_docsuser-guide]]

## Top bridge nodes
- [[hermes-openclaw-dev-workflow]] - degree 5, connects to 1 community