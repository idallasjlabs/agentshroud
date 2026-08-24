# Hermes Cron Jobs — Reference & Recreation Guide

Auto-generated snapshot of every Hermes cron job running in production, for
recreating the full job set on a fresh AgentShroud install. These jobs live
only in Hermes's live cron store (`/opt/data/cron/jobs.json` inside the
container) — none of this is baked into `docker/bots/hermes/init-config.sh`,
so a fresh volume starts with zero of them.

## How to recreate a job

Each job below has its full prompt saved as a companion `.txt` file in
`docker/config/hermes/cron/prompts/`. To recreate:

```bash
# 1. Copy the prompt file into the Hermes container
docker exec -i agentshroud-hermes-v2 sh -c 'cat > /tmp/p.txt' < docker/config/hermes/cron/prompts/<slug>.txt

# 2. Create the job, referencing the file via command substitution
docker exec agentshroud-hermes-v2 sh -c 'hermes cron create "<schedule>" "$(cat /tmp/p.txt)" --name "<name>" --deliver <deliver>'

# 3. If the job needs a model pin (see table below), edit it in after creation
docker exec agentshroud-hermes-v2 hermes cron edit <new-job-id> --model gemma-4-26b-a4b-it --provider custom
```

**Do not `docker cp` the prompt file** — this repo's Hermes/OpenClaw containers
run with a read-only rootfs; `docker cp` fails there (a real incident on
2026-08-24 wiped 6 job prompts to empty this way). Always pipe via stdin
(`docker exec -i ... sh -c 'cat > file' < local_file`) as shown above.

**Provider must be `custom`, never `ollama` or `openai-local`.** Confirmed
via `hermes doctor` 2026-08-24: neither `ollama` nor `openai-local` is a
valid provider name in this Hermes version (0.20.1) — every job using either
one fails immediately with `RuntimeError: No LLM provider configured`
(or, once the global `model.provider` default happens to be valid,
`HTTP 401: Missing Authentication header`, since the top-level `model:`
block in `config.yaml` also needs an explicit `api_key: ''` field — without
it Hermes routes to a stale OpenRouter-pointed fallback instead of the
local gateway). `custom` + `base_url: http://gateway:8080/v1` is the
correct, working combination — matches every per-task model slot already
configured that way under `config.yaml`'s `auxiliary:` section.

## Job index

| Name | Schedule | Deliver | Model pin | Mode |
|---|---|---|---|---|
| AgentShroud Daily Check-in | `0 14 * * *` | telegram | gemma-4-26b-a4b-it | agent |
| AgentShroud Weekly Summary | `0 18 * * 5` | telegram | gemma-4-26b-a4b-it | agent |
| Daily Component Health Digest | `30 13 * * *` | telegram | (unpinned) | script:prep-component-health.sh |
| Daily Memory Journal | `55 23 * * *` | local | gemma-4-26b-a4b-it | agent |
| Email: Chat Front-Ends & Search Infra | `15 14 * * *` | local | (unpinned) | script:send-newsletter-frontends-email.sh [no-agent] |
| Email: Coding-Agent CLIs | `20 12 * * *` | local | (unpinned) | script:send-newsletter-coding-clis-email.sh [no-agent] |
| Email: Local Inference Engines | `35 12 * * *` | local | (unpinned) | script:send-newsletter-inference-engines-email.sh [no-agent] |
| Email: Mac Clustering | `15 13 * * *` | local | (unpinned) | script:send-newsletter-clustering-email.sh [no-agent] |
| Email: MoE Streaming & SSD Offload | `55 12 * * *` | local | (unpinned) | script:send-newsletter-moe-streaming-email.sh [no-agent] |
| Email: Model Version Tracker | `55 13 * * *` | local | (unpinned) | script:send-newsletter-model-versions-email.sh [no-agent] |
| Email: Personal AI Assistants | `35 13 * * *` | local | (unpinned) | script:send-newsletter-personal-agents-email.sh [no-agent] |
| Email: Today in AI | `15 12 * * *` | local | (unpinned) | script:send-today-in-ai-email.sh [no-agent] |
| Hermes Competitive Intelligence Email (AM/PM) | `0 7,16 * * *` | local | gemma-4-26b-a4b-it | agent |
| Hermes Competitive Landscape Update (AM/PM) | `0 6,15 * * *` | local | gemma-4-26b-a4b-it | agent |
| Monthly Chaos Engineering Drill | `0 9 1 * *` | telegram | gemma-4-26b-a4b-it | agent |
| Newsletter: Chat Front-Ends & Search Infra | `0 14 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-frontends.sh |
| Newsletter: Coding-Agent CLIs | `0 12 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-coding-clis.sh |
| Newsletter: Local Inference Engines | `20 12 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-inference-engines.sh |
| Newsletter: Mac Clustering | `0 13 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-clustering.sh |
| Newsletter: MoE Streaming & SSD Offload | `40 12 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-moe-streaming.sh |
| Newsletter: Model Version Tracker | `40 13 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-model-versions.sh |
| Newsletter: Personal AI Assistants | `20 13 * * *` | local | gemma-4-26b-a4b-it | script:prep-newsletter-personal-agents.sh |
| OMLX MoE Streaming Health Check | `5 13 * * *` | local | gemma-4-26b-a4b-it | agent |
| Today in AI | `0 12 * * *` | local | (unpinned) | script:prep-today-in-ai.sh |
| Turbo Fieldfare Fix Watch | `0 17 * * *` | local | (unpinned) | agent |
| Weekly Hermes Stability Report | `0 9 * * 1` | telegram | gemma-4-26b-a4b-it | agent |
| Weekly Kaizen Review | `0 17 * * 5` | telegram | gemma-4-26b-a4b-it | agent |
| Weekly job-log cleanup | `0 5 * * 0` | local | (unpinned) | script:cleanup-job-logs.sh [no-agent] |
| jira-weekly-review | `0 9 * * 0` | local | (unpinned) | agent |

## Job details

### AgentShroud Daily Check-in

- **ID (reference only, will differ on recreate):** `abab02e235fd`
- **Schedule:** `0 14 * * *`
- **Deliver:** telegram
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/agentshroud-daily-check-in.txt`
### AgentShroud Weekly Summary

- **ID (reference only, will differ on recreate):** `17e6ee61cb1a`
- **Schedule:** `0 18 * * 5`
- **Deliver:** telegram
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/agentshroud-weekly-summary.txt`
### Daily Component Health Digest

- **ID (reference only, will differ on recreate):** `5b1dca7f3c84`
- **Schedule:** `30 13 * * *`
- **Deliver:** telegram
- **Model pin:** (unpinned)
- **Mode:** script:prep-component-health.sh
- **Prompt file:** `prompts/daily-component-health-digest.txt`
### Daily Memory Journal

- **ID (reference only, will differ on recreate):** `5429226931ee`
- **Schedule:** `55 23 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/daily-memory-journal.txt`
### Email: Chat Front-Ends & Search Infra

- **ID (reference only):** `e6c1b1739734`
- **Schedule:** `15 14 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-frontends-email.sh`
- **Mode:** script:send-newsletter-frontends-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Coding-Agent CLIs

- **ID (reference only):** `8cdd7f10c0f2`
- **Schedule:** `20 12 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-coding-clis-email.sh`
- **Mode:** script:send-newsletter-coding-clis-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Local Inference Engines

- **ID (reference only):** `33a50ee36869`
- **Schedule:** `35 12 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-inference-engines-email.sh`
- **Mode:** script:send-newsletter-inference-engines-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Mac Clustering

- **ID (reference only):** `9b5534b3ee56`
- **Schedule:** `15 13 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-clustering-email.sh`
- **Mode:** script:send-newsletter-clustering-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: MoE Streaming & SSD Offload

- **ID (reference only):** `25e68ef12b55`
- **Schedule:** `55 12 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-moe-streaming-email.sh`
- **Mode:** script:send-newsletter-moe-streaming-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Model Version Tracker

- **ID (reference only):** `c1f6c2b7cc8f`
- **Schedule:** `55 13 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-model-versions-email.sh`
- **Mode:** script:send-newsletter-model-versions-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Personal AI Assistants

- **ID (reference only):** `2019daeaa6c8`
- **Schedule:** `35 13 * * *`
- **Deliver:** local
- **Script:** `send-newsletter-personal-agents-email.sh`
- **Mode:** script:send-newsletter-personal-agents-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Email: Today in AI

- **ID (reference only):** `22e736743780`
- **Schedule:** `15 12 * * *`
- **Deliver:** local
- **Script:** `send-today-in-ai-email.sh`
- **Mode:** script:send-today-in-ai-email.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### Hermes Competitive Intelligence Email (AM/PM)

- **ID (reference only, will differ on recreate):** `91c730578ca5`
- **Schedule:** `0 7,16 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/hermes-competitive-intelligence-email-am-pm.txt`
### Hermes Competitive Landscape Update (AM/PM)

- **ID (reference only, will differ on recreate):** `e968c0ca5758`
- **Schedule:** `0 6,15 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/hermes-competitive-landscape-update-am-pm.txt`
### Monthly Chaos Engineering Drill

- **ID (reference only, will differ on recreate):** `69ac94962be4`
- **Schedule:** `0 9 1 * *`
- **Deliver:** telegram
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/monthly-chaos-engineering-drill.txt`
### Newsletter: Chat Front-Ends & Search Infra

- **ID (reference only, will differ on recreate):** `7c9d722746d3`
- **Schedule:** `0 14 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-frontends.sh
- **Prompt file:** `prompts/newsletter-chat-front-ends-search-infra.txt`
### Newsletter: Coding-Agent CLIs

- **ID (reference only, will differ on recreate):** `7d109898f88a`
- **Schedule:** `0 12 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-coding-clis.sh
- **Prompt file:** `prompts/newsletter-coding-agent-clis.txt`
### Newsletter: Local Inference Engines

- **ID (reference only, will differ on recreate):** `721de11cfd76`
- **Schedule:** `20 12 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-inference-engines.sh
- **Prompt file:** `prompts/newsletter-local-inference-engines.txt`
### Newsletter: Mac Clustering

- **ID (reference only, will differ on recreate):** `fc17041c7d64`
- **Schedule:** `0 13 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-clustering.sh
- **Prompt file:** `prompts/newsletter-mac-clustering.txt`
### Newsletter: MoE Streaming & SSD Offload

- **ID (reference only, will differ on recreate):** `3d05ecbcd6cd`
- **Schedule:** `40 12 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-moe-streaming.sh
- **Prompt file:** `prompts/newsletter-moe-streaming-ssd-offload.txt`
### Newsletter: Model Version Tracker

- **ID (reference only, will differ on recreate):** `67a4195391f2`
- **Schedule:** `40 13 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-model-versions.sh
- **Prompt file:** `prompts/newsletter-model-version-tracker.txt`
### Newsletter: Personal AI Assistants

- **ID (reference only, will differ on recreate):** `b90962ec237e`
- **Schedule:** `20 13 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** script:prep-newsletter-personal-agents.sh
- **Prompt file:** `prompts/newsletter-personal-ai-assistants.txt`
### OMLX MoE Streaming Health Check

- **ID (reference only, will differ on recreate):** `805c9d89f93b`
- **Schedule:** `5 13 * * *`
- **Deliver:** local
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/omlx-moe-streaming-health-check.txt`
### Today in AI

- **ID (reference only, will differ on recreate):** `9a233cf4c959`
- **Schedule:** `0 12 * * *`
- **Deliver:** local
- **Model pin:** (unpinned)
- **Mode:** script:prep-today-in-ai.sh
- **Prompt file:** `prompts/today-in-ai.txt`
### Turbo Fieldfare Fix Watch

- **ID (reference only, will differ on recreate):** `b75e6edea791`
- **Schedule:** `0 17 * * *`
- **Deliver:** local
- **Model pin:** (unpinned)
- **Mode:** agent
- **Prompt file:** `prompts/turbo-fieldfare-fix-watch.txt`
### Weekly Hermes Stability Report

- **ID (reference only, will differ on recreate):** `4bc8f8a61cc0`
- **Schedule:** `0 9 * * 1`
- **Deliver:** telegram
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/weekly-hermes-stability-report.txt`
### Weekly Kaizen Review

- **ID (reference only, will differ on recreate):** `88d713f6be08`
- **Schedule:** `0 17 * * 5`
- **Deliver:** telegram
- **Model pin:** gemma-4-26b-a4b-it
- **Mode:** agent
- **Prompt file:** `prompts/weekly-kaizen-review.txt`
### Weekly job-log cleanup

- **ID (reference only):** `f235b8124d1e`
- **Schedule:** `0 5 * * 0`
- **Deliver:** local
- **Script:** `cleanup-job-logs.sh`
- **Mode:** script:cleanup-job-logs.sh [no-agent]
- (No LLM prompt — script-driven job. Script source lives in the Hermes image / `docker/bots/hermes/init-config.sh`.)
### jira-weekly-review

- **ID (reference only, will differ on recreate):** `1cc0354a6ba3`
- **Schedule:** `0 9 * * 0`
- **Deliver:** local
- **Model pin:** (unpinned)
- **Mode:** agent
- **Prompt file:** `prompts/jira-weekly-review.txt`
