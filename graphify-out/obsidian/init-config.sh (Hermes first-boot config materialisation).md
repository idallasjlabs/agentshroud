---
source_file: "docker/bots/hermes/init-config.sh"
type: "code"
community: "_seed_cron"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_seed_cron
---

# init-config.sh (Hermes first-boot config materialisation)

## Connections
- [[Env-split cron reconciliation — dev resumes all jobs, prod pauses except keep-list]] - `implements` [EXTRACTED]
- [[GitHub MCP server wiring — first-boot add from github_pat secret]] - `implements` [EXTRACTED]
- [[MCP servers reconciliation — writes config.yaml mcp_servers from servers.json (not `hermes mcp add`, which is interactive)]] - `implements` [EXTRACTED]
- [[Runtime facts writer — AGENTS.md AgentShroud version line (fixes hallucinated version)]] - `implements` [EXTRACTED]
- [[Skills sync — installs ~.llm_settingsskills into optdataskills every boot]] - `implements` [EXTRACTED]
- [[Tirith trust seeding — competitorresearch TLD lookalike bypass]] - `implements` [EXTRACTED]
- [[_write_soul]] - `calls` [EXTRACTED]
- [[config.yaml seedupgrade — adds telegram.extra.base_url for gateway routing]] - `implements` [EXTRACTED]
- [[gateway-default first-boot auto-start fix (removes stale down sentinel)]] - `implements` [EXTRACTED]
- [[hermes service (prod, profiles hermesfull — service block is dead code, see run-standalone.sh)]] - `shares_data_with` [INFERRED]
- [[start.sh — Hermes s6-overlay startup wrapper (main program)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_seed_cron