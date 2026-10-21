---
source_file: "gateway/security/daily_cve_report.py"
type: "code"
community: "sync-cve-registry.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sync-cve-registrypy
---

# daily_cve_report.py

## Connections
- [[Daily CVE Report — container vulnerability digest + upstream agent CVE watch.…]] - `rationale_for` [EXTRACTED]
- [[_already_checked_upstream_today()]] - `contains` [EXTRACTED]
- [[_already_ingested_ghsa_today()]] - `contains` [EXTRACTED]
- [[_already_sent_today()]] - `contains` [EXTRACTED]
- [[_build_image_targets()]] - `contains` [EXTRACTED]
- [[_load_alerted_ghsa()]] - `contains` [EXTRACTED]
- [[_running_image()]] - `contains` [EXTRACTED]
- [[_save_alerted_ghsa()]] - `contains` [EXTRACTED]
- [[_send_telegram()]] - `contains` [EXTRACTED]
- [[asyncio_3]] - `imports` [EXTRACTED]
- [[check_upstream_cves()]] - `contains` [EXTRACTED]
- [[cve_report_scheduler()]] - `contains` [EXTRACTED]
- [[datetime_8]] - `imports_from` [EXTRACTED]
- [[format_cve_report()]] - `contains` [EXTRACTED]
- [[format_upstream_cve_alert()]] - `contains` [EXTRACTED]
- [[get_agent_cve_source()]] - `imports` [EXTRACTED]
- [[get_agent_ghsa_repo()]] - `imports` [EXTRACTED]
- [[ghsa_ingest_scheduler()]] - `contains` [EXTRACTED]
- [[list_cve_agents()]] - `imports` [EXTRACTED]
- [[run_and_send_cve_report()]] - `contains` [EXTRACTED]
- [[run_upstream_cve_check()]] - `contains` [EXTRACTED]
- [[run_upstream_cve_check_all_agents()]] - `contains` [EXTRACTED]
- [[test_daily_cve_report.py]] - `imports_from` [EXTRACTED]
- [[upstream_cve_check_scheduler()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sync-cve-registrypy
