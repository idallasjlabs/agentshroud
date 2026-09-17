---
source_file: "gateway/tests/test_gateway_email_service.py"
type: "rationale"
community: "GatewayEmailService"
location: "L21"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/GatewayEmailService
---

# Records login/sendmail; usable as a context manager like SMTP_SSL.

## Connections
- [[_FakeSmtp]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/GatewayEmailService