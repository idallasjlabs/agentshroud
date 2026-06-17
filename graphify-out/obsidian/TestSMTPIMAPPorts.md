---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "Egress Filter & Approval"
location: "L540"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__Approval
---

# TestSMTPIMAPPorts

## Connections
- [[.test_connect_proxy_policy_allows_smtp_gmail_465()]] - `method` [EXTRACTED]
- [[.test_connect_proxy_policy_allows_smtp_mail_me_587()]] - `method` [EXTRACTED]
- [[.test_default_policy_allows_imaps()]] - `method` [EXTRACTED]
- [[.test_default_policy_allows_smtp_submission()]] - `method` [EXTRACTED]
- [[.test_default_policy_allows_smtps()]] - `method` [EXTRACTED]
- [[.test_non_email_port_still_denied_for_unlisted_domain()]] - `method` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed     by the]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__Approval