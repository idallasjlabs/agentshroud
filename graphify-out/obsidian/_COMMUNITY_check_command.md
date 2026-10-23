---
type: community
cohesion: 0.14
members: 25
---

# check_command

**Cohesion:** 0.14 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-test_allows_env_in_name()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_allows_natural_language_mixed_quotes()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_allows_natural_language_question()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_allows_natural_language_social_phrasing()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_allows_safe_command()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_blocks_dollar_env()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_blocks_env_pipe()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_blocks_printenv()_1]] - code - gateway/tests/test_env_guard.py
- [[dot-test_blocks_proc_environ()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_blocks_proc_star_environ()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_clean_text_unchanged()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_aws_key()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_github_token()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_multiple_keys()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_openai_key()]] - code - gateway/tests/test_env_guard.py
- [[Check if command execution should be allowed.      Args         cmd Command to]] - rationale - gateway/security/env_guard.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Scrub API keys and sensitive patterns from text output.      Args         text]] - rationale - gateway/security/env_guard.py
- [[TestCheckCommand]] - code - gateway/tests/test_env_guard.py
- [[TestScrubOutput]] - code - gateway/tests/test_env_guard.py
- [[check_command()]] - code - gateway/security/env_guard.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[scrub_output()]] - code - gateway/security/env_guard.py
- [[test_env_guard.py]] - code - gateway/tests/test_env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check_command
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_dot-_record_leakage()]]
- 1 edge to [[_COMMUNITY_KeyVault]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[env_guard.py]] - degree 10, connects to 6 communities
- [[check_command()]] - degree 15, connects to 1 community
- [[get_env_guard()]] - degree 4, connects to 1 community
