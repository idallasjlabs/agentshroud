---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Community 185"
location: "L582"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_185
---

# TestSMTPIMAPPorts

## Connections
- [[dot-test_connect_proxy_policy_allows_smtp_gmail_465()]] - `method` [EXTRACTED]
- [[dot-test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `method` [EXTRACTED]
- [[dot-test_default_policy_allows_imaps()]] - `method` [EXTRACTED]
- [[dot-test_default_policy_allows_smtp_submission()]] - `method` [EXTRACTED]
- [[dot-test_default_policy_allows_smtps()]] - `method` [EXTRACTED]
- [[dot-test_non_email_port_still_denied_for_unlisted_domain()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_185