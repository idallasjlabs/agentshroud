---
source_file: "gateway/tests/test_slack_proxy.py"
type: "code"
community: "Slack Proxy Tests"
location: "L557"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Slack_Proxy_Tests
---

# TestMultiFieldOutboundScanning

## Connections
- [[.test_attachments_scanned()]] - `method` [EXTRACTED]
- [[.test_blocks_scanned_even_when_text_present()]] - `method` [EXTRACTED]
- [[.test_file_upload_initial_comment_scanned()]] - `method` [EXTRACTED]
- [[.test_post_ephemeral_scanned()]] - `method` [EXTRACTED]
- [[.test_structured_field_sanitization_blocks_delivery()]] - `method` [EXTRACTED]
- [[.test_text_sanitization_still_applied()]] - `method` [EXTRACTED]
- [[SlackAPIProxy]] - `uses` [INFERRED]
- [[WebhookReceiver]] - `uses` [INFERRED]
- [[blocksattachments and upload text must be scanned, not just `text`.      Regres]] - `rationale_for` [EXTRACTED]
- [[test_slack_proxy.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Slack_Proxy_Tests
