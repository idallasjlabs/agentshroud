---
source_file: "gateway/ingest_api/routes/forward.py"
type: "code"
community: "create_auth_dependency (2)"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/create_auth_dependency_2
---

# forward.py

## Connections
- [[AgentTarget_2]] - `imports` [EXTRACTED]
- [[ApprovalRequest_4]] - `imports` [EXTRACTED]
- [[EmailSendRequest]] - `imports` [EXTRACTED]
- [[EmailSendResponse]] - `imports` [EXTRACTED]
- [[ForwardError]] - `imports` [EXTRACTED]
- [[ForwardRequest]] - `imports` [EXTRACTED]
- [[ForwardResponse]] - `imports` [EXTRACTED]
- [[GatewayEmailService_1]] - `imports` [EXTRACTED]
- [[OwnerEmailRequest]] - `contains` [EXTRACTED]
- [[RBACConfig_2]] - `imports` [EXTRACTED]
- [[RT-6 — Owner-Identity Spoofing via forward body (FIXED)]] - `rationale_for` [EXTRACTED]
- [[WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)]] - `references` [EXTRACTED]
- [[WebhookReceiver]] - `imports` [EXTRACTED]
- [[_InboundResult]] - `contains` [EXTRACTED]
- [[_filtered_sentence_stream()]] - `contains` [EXTRACTED]
- [[_get_gmail_app_password()]] - `contains` [EXTRACTED]
- [[_is_email_recipient_allowed()]] - `contains` [EXTRACTED]
- [[_process_inbound()]] - `contains` [EXTRACTED]
- [[_resolve_user_trust_level()]] - `contains` [EXTRACTED]
- [[_sentences_from_deltas()]] - `contains` [EXTRACTED]
- [[auth_dep()_1]] - `contains` [EXTRACTED]
- [[create_auth_dependency()]] - `imports` [EXTRACTED]
- [[email_send()]] - `contains` [EXTRACTED]
- [[email_send_owner()]] - `contains` [EXTRACTED]
- [[email_service.py]] - `imports_from` [EXTRACTED]
- [[event_bus.py]] - `imports_from` [EXTRACTED]
- [[forward_content()]] - `contains` [EXTRACTED]
- [[forward_content_stream()]] - `contains` [EXTRACTED]
- [[ingest_apiauth.py]] - `imports_from` [EXTRACTED]
- [[ingest_apimodels.py]] - `imports_from` [EXTRACTED]
- [[ingest_apirouter.py]] - `imports_from` [EXTRACTED]
- [[make_event()]] - `imports` [EXTRACTED]
- [[state.py]] - `imports_from` [EXTRACTED]
- [[telegram_webhook()]] - `contains` [EXTRACTED]
- [[test_channel_ownership.py]] - `calls` [EXTRACTED]
- [[test_forward_routing.py]] - `imports_from` [EXTRACTED]
- [[webhook_receiver.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/create_auth_dependency_2
