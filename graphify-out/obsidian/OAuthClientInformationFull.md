---
source_file: "gateway/inbound_edge/edge_app.py"
type: "code"
community: "Community 31"
location: "L147"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_31
---

# OAuthClientInformationFull

## Connections
- [[.authorize()]] - `references` [EXTRACTED]
- [[.exchange_authorization_code()]] - `references` [EXTRACTED]
- [[.exchange_refresh_token()]] - `references` [EXTRACTED]
- [[.get_client()]] - `references` [EXTRACTED]
- [[.load_authorization_code()]] - `references` [EXTRACTED]
- [[.load_refresh_token()]] - `references` [EXTRACTED]
- [[.register_client()]] - `references` [EXTRACTED]
- [[TokenRejected]] - `uses` [INFERRED]
- [[test_loaders_return_none_and_revoke_passes_token()]] - `calls` [INFERRED]
- [[test_register_and_authorize_errors_map_to_oauth_codes()]] - `calls` [INFERRED]
- [[test_token_errors_and_foreign_resource()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Community_31