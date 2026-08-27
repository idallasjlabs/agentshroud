---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "Community 82"
location: "L302"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_82
---

# is_safe_a2a_callback_url()

## Connections
- [[._decide()]] - `calls` [EXTRACTED]
- [[Hardened SSRF guard for A2A push-notification callback URLs.      Independent mi]] - `rationale_for` [EXTRACTED]
- [[_address_is_public()]] - `calls` [EXTRACTED]
- [[_canonicalize_ip_literal()]] - `calls` [EXTRACTED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_callback_url_bare_dot_host_is_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_hostname_resolving_to_a_private_ip_is_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_ipv4_mapped_ipv6_loopback_is_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_legitimate_public_urls_are_allowed()]] - `calls` [EXTRACTED]
- [[test_callback_url_malformed_url_is_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_out_of_range_decimal_literal_is_not_treated_as_a_valid_ip()]] - `calls` [EXTRACTED]
- [[test_callback_url_rejects_non_http_schemes()]] - `calls` [EXTRACTED]
- [[test_callback_url_scheme_only_no_host_is_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_ssrf_bypass_encodings_are_rejected()]] - `calls` [EXTRACTED]
- [[test_callback_url_unresolvable_hostname_fails_closed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_82