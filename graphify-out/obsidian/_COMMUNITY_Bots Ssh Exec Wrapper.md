---
type: community
cohesion: 0.06
members: 44
---

# Bots Ssh Exec Wrapper

**Cohesion:** 0.06 - loosely connected
**Members:** 44 nodes

## Members
- [[--noproxy gateway is required so the call reaches the control-plane directly.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[A command with quotesmetacharacters cannot inject extra JSON fields.      This]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[An explicitly set GATEWAY_AUTH_TOKEN takes priority over the _FILE (back-compat]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Belt-and-suspenders the wrapper must not contain a literal empty Bearer.      T]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[CompletedProcess_1]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Extract the 'Bearer token' value from the captured curl argv.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[GATEWAY_AUTH_TOKEN_FILE contents become the Bearer token (Hermes path).]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Hermes' belt-and-suspenders tirith trust must be scoped, never blanket.      It]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Literal newlinestabsbackslashesquotes round-trip through JSON safely.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[OPENCLAW_GATEWAY_PASSWORD_FILE contents become the Bearer token.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Proof the exemption is NARROW an EXTERNAL http curl is still flaggable.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Pull the _json_escape helper + payload-build block out of the wrapper.      We r]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Return the contents of ``` fenced code blocks (the runnable recipes).]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Run the real wrapper with a fake `curl` that records its argv.      The stub cur]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Run the wrapper's shell payload builder and return the emitted JSON text.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[The documented agent-facing RECIPE (fenced code) must be scanner-clean.      Thi]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[The interpreter-free builder produces valid JSON for a normal command.      PATH]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[The wrapper hard-codes the internal control-plane endpoint and nothing else.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[The wrapper must NOT shell out to python3python for JSON building.      Regress]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[With NO token source the wrapper must fail loudly and NOT call curl.      Guards]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[Wrapper is COPY'd into and chmod'd in BOTH bot Dockerfiles.]] - rationale - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[_bearer_from_argv()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[_build_payload_via_shell()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[_extract_payload_builder()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[_fenced_code_blocks()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[_run_wrapper_capture_bearer()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[agentshroud-ssh-exec.sh (internal-gateway SSH-exec wrapper)]] - code - docker/scripts/agentshroud-ssh-exec.sh
- [[test_both_bot_images_bake_in_the_wrapper()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_bots_ssh_exec_wrapper.py]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_external_http_curl_still_matches_the_flagged_pattern()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_hermes_tirith_trust_is_scoped_not_blanket()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_no_token_source_exits_nonzero_and_sends_no_request()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_shell_payload_builder_emits_valid_json_without_python()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_shell_payload_builder_encodes_newlines_and_tabs()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_shell_payload_builder_escapes_shell_metacharacters_injection_safe()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_token_env_var_wins_over_file()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_token_resolved_from_hermes_auth_token_file()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_token_resolved_from_openclaw_password_file()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_agent_facing_invocation_has_no_plain_http_url()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_exists_and_is_executable()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_forces_noproxy_gateway()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_has_no_python_dependency()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_never_sends_empty_bearer()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py
- [[test_wrapper_targets_only_internal_gateway_endpoint()]] - code - gateway/tests/test_bots_ssh_exec_wrapper.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Bots_Ssh_Exec_Wrapper
SORT file.name ASC
```
