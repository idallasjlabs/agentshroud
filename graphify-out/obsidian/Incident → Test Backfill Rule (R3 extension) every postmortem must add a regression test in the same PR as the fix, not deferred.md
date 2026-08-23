---
source_file: "docs/governance/TEST_STRATEGY.md"
type: "rationale"
community: "Strategy (governance)"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Strategy_governance
---

# Incident → Test Backfill Rule (R3 extension): every postmortem must add a regression test in the same PR as the fix, not deferred

## Connections
- [[Bug ARM64 V8 stack overflow → S1 --stack-size=65536 in start-agentshroud.sh (v1.0.38)]] - `rationale_for` [EXTRACTED]
- [[Bug Dockerfile COPY path drift → S4 COPY from dockerconfigopenclaw (v1.0.39)]] - `rationale_for` [EXTRACTED]
- [[Bug Gateway binding on 0.0.0.0 → S5 no 0.0.0.08080 in compose (v1.0.39)]] - `rationale_for` [EXTRACTED]
- [[Bug Slack invalid_auth with empty tokens → A3-A5S3 xoxb-xapp- prefix guard (v1.0.39)]] - `rationale_for` [EXTRACTED]
- [[Bug Telegram photo download via wrong apiRoot → A1S2 channels.telegram.apiRoot set (v1.0.39)]] - `rationale_for` [EXTRACTED]
- [[Bug read_secret_masked stdout pollution → S6 routing to devtty (v1.0.39)]] - `rationale_for` [EXTRACTED]
- [[Bug stale Slack block on restart → A6S7 delete config.channels.slack when no tokens (v1.0.40)]] - `rationale_for` [EXTRACTED]
- [[Test Strategy (docsgovernanceTEST_STRATEGY.md)]] - `conceptually_related_to` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Strategy_governance