---
type: community
cohesion: 0.13
members: 22
---

# Container Runtime (smoke.d)

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[AgentShroud Tagline]] - concept - BRAND.md
- [[AgentShroud Taglines List]] - document - branding/taglines.json
- [[check()_2]] - code - scripts/smoke.d/test-container-runtime.sh
- [[check()_6]] - code - tests/startup_smoke/test_hermes_chown_coverage.sh
- [[check()_7]] - code - tests/startup_smoke/test_hermes_cron_html_email.sh
- [[check()_9]] - code - tests/startup_smoke/test_openclaw_photo.sh
- [[container-runtime.sh (detection shim)]] - code - scripts/lib/container-runtime.sh
- [[email_helper.sh]] - code - docker/bots/hermes/email_helper.sh
- [[email_helper.sh script]] - code - docker/bots/hermes/email_helper.sh
- [[make_fake_bin()]] - code - scripts/smoke.d/test-container-runtime.sh
- [[run_detect()]] - code - scripts/smoke.d/test-container-runtime.sh
- [[run_test()]] - code - scripts/smoke.sh
- [[smoke.sh]] - code - scripts/smoke.sh
- [[smoke.sh script]] - code - scripts/smoke.sh
- [[test-container-runtime.sh]] - code - scripts/smoke.d/test-container-runtime.sh
- [[test-container-runtime.sh script]] - code - scripts/smoke.d/test-container-runtime.sh
- [[test_hermes_chown_coverage.sh]] - code - tests/startup_smoke/test_hermes_chown_coverage.sh
- [[test_hermes_chown_coverage.sh script]] - code - tests/startup_smoke/test_hermes_chown_coverage.sh
- [[test_hermes_cron_html_email.sh]] - code - tests/startup_smoke/test_hermes_cron_html_email.sh
- [[test_hermes_cron_html_email.sh script]] - code - tests/startup_smoke/test_hermes_cron_html_email.sh
- [[test_openclaw_photo.sh]] - code - tests/startup_smoke/test_openclaw_photo.sh
- [[test_openclaw_photo.sh script]] - code - tests/startup_smoke/test_openclaw_photo.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Container_Runtime_smoked
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Render Email (hermes)]]
- 1 edge to [[_COMMUNITY_Start (hermes)]]
- 1 edge to [[_COMMUNITY_Start Agentshroud (scripts)]]
- 1 edge to [[_COMMUNITY_Collaborator Greeter]]
- 1 edge to [[_COMMUNITY_Sync Llm Settings (scripts)]]
- 1 edge to [[_COMMUNITY_Jobs (cron)]]
- 1 edge to [[_COMMUNITY_Deployment (runbooks)]]
- 1 edge to [[_COMMUNITY_Readme (branding)]]

## Top bridge nodes
- [[test_openclaw_photo.sh]] - degree 10, connects to 4 communities
- [[test_hermes_cron_html_email.sh]] - degree 8, connects to 2 communities
- [[smoke.sh]] - degree 7, connects to 1 community
- [[AgentShroud Tagline]] - degree 2, connects to 1 community