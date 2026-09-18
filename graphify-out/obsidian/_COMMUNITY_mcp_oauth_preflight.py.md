---
type: community
cohesion: 0.06
members: 55
---

# mcp_oauth_preflight.py

**Cohesion:** 0.06 - loosely connected
**Members:** 55 nodes

## Members
- [[.do_GET()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[.log_message()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[.test_all_whitespace_file_returns_default()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_all_whitespace_returns_empty()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_clean_single_line()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_clean_token_returned()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_crlf_secret_file()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_crlf_stripped()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_empty_string_returns_empty()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_garbled_blob_returns_last_line()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_garbled_blob_returns_real_token()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_label_lines_stripped()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_missing_file_returns_default()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_multiline_interior_blank_lines()]] - code - gateway/tests/test_utils_secrets.py
- [[.test_trailing_newline_stripped()]] - code - gateway/tests/test_utils_secrets.py
- [[An all-whitespace  blank file returns an empty string.]] - rationale - gateway/tests/test_utils_secrets.py
- [[BaseHTTPRequestHandler]] - code
- [[CRLF line endings are handled correctly.]] - rationale - gateway/tests/test_utils_secrets.py
- [[HTTPServer]] - code
- [[Label + masked preview lines before the real token are discarded.]] - rationale - gateway/tests/test_utils_secrets.py
- [[Normal single-line value is returned unchanged (modulo outer whitespace).]] - rationale - gateway/tests/test_utils_secrets.py
- [[OAuthResult (dataclass)]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[Read a Docker secret from runsecretsname. Falls back to `default` if the…]] - rationale - gateway/utils/secrets.py
- [[Read response body. - max_bytes=None - read all bytes - max_bytes=int - read…]] - rationale - .llm_settings/scripts/mcp_oauth_preflight.py
- [[Return the last non-empty line of raw, stripped of surrounding whitespace.…]] - rationale - gateway/utils/secrets.py
- [[Shared secret-reading utilities for gateway components.]] - rationale - gateway/utils/secrets.py
- [[Single-line value with trailing newline is stripped.]] - rationale - gateway/tests/test_utils_secrets.py
- [[TestNormalizeSecret]] - code - gateway/tests/test_utils_secrets.py
- [[TestReadSecret]] - code - gateway/tests/test_utils_secrets.py
- [[The exact garbled blob from the marvin-dev bug returns only the real token.]] - rationale - gateway/tests/test_utils_secrets.py
- [[The exact marvin-dev garbled blob on disk yields only the real token.]] - rationale - gateway/tests/test_utils_secrets.py
- [[Unit tests for gateway.utils.secrets — secret-file reading and normalization.…]] - rationale - gateway/tests/test_utils_secrets.py
- [[When the value has interior blank lines, the last non-empty line is returned.]] - rationale - gateway/tests/test_utils_secrets.py
- [[_CallbackHandler (loopback OAuth callback HTTP handler)]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_dns_lookup()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_http_request()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_normalize_secret()]] - code - gateway/utils/secrets.py
- [[_normalize_url()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_pkce_pair()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_read_body()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_start_callback_server()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_tls_probe()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[_wait_for_callback()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[cmd_oauth()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[cmd_reachability()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[gateway.utils.secrets]] - code - gateway/utils/secrets.py
- [[getenv_required()]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[main() (CLI entrypoint)]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[mcp_oauth_preflight.py]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[mcp_oauth_preflight.py Enterprise-safe OAuth + MCP connectivity preflight.…]] - rationale - .llm_settings/scripts/mcp_oauth_preflight.py
- [[oauth_atlassian() (Atlassian 3LO PKCE flow)]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[oauth_github() (GitHub device flow)]] - code - .llm_settings/scripts/mcp_oauth_preflight.py
- [[perform_mcp_oauth_preflight.sh (reachability wrapper)]] - code - .llm_settings/scripts/perform_mcp_oauth_preflight.sh
- [[read_secret()]] - code - gateway/utils/secrets.py
- [[test_utils_secrets.py]] - code - gateway/tests/test_utils_secrets.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mcp_oauth_preflightpy
SORT file.name ASC
```
