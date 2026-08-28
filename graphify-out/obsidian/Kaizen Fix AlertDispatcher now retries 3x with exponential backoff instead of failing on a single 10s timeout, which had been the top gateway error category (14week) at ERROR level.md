---
source_file: "gateway/tests/test_alert_dispatcher_retry.py"
type: "rationale"
community: "Security Audit & Drift Detection"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Audit__Drift_Detection
---

# Kaizen Fix: AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14/week) at ERROR level

## Connections
- [[AlertDispatcher]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Audit__Drift_Detection