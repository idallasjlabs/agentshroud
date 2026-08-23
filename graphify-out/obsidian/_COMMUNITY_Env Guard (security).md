---
type: community
cohesion: 0.08
members: 36
---

# Env Guard (security)

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

## Members
- [[._contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[._looks_like_credential()]] - code - gateway/security/env_guard.py
- [[._record_leakage()]] - code - gateway/security/env_guard.py
- [[.check_command_execution()]] - code - gateway/security/env_guard.py
- [[.check_file_access()]] - code - gateway/security/env_guard.py
- [[.scrub_command_output()]] - code - gateway/security/env_guard.py
- [[.test_allows_env_in_name()]] - code - gateway/tests/test_env_guard.py
- [[.test_allows_natural_language_mixed_quotes()]] - code - gateway/tests/test_env_guard.py
- [[.test_allows_natural_language_question()]] - code - gateway/tests/test_env_guard.py
- [[.test_allows_natural_language_social_phrasing()]] - code - gateway/tests/test_env_guard.py
- [[.test_allows_safe_command()]] - code - gateway/tests/test_env_guard.py
- [[.test_blocks_dollar_env()]] - code - gateway/tests/test_env_guard.py
- [[.test_blocks_env_pipe()]] - code - gateway/tests/test_env_guard.py
- [[.test_blocks_printenv()]] - code - gateway/tests/test_env_guard.py
- [[.test_blocks_proc_environ()]] - code - gateway/tests/test_env_guard.py
- [[.test_blocks_proc_star_environ()]] - code - gateway/tests/test_env_guard.py
- [[.test_clean_text_unchanged()]] - code - gateway/tests/test_env_guard.py
- [[.test_scrubs_aws_key()]] - code - gateway/tests/test_env_guard.py
- [[.test_scrubs_github_token()]] - code - gateway/tests/test_env_guard.py
- [[.test_scrubs_multiple_keys()]] - code - gateway/tests/test_env_guard.py
- [[.test_scrubs_openai_key()]] - code - gateway/tests/test_env_guard.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be allowed.      Args         cmd Command to]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub API keys and sensitive patterns from text output.      Args         text]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[TestCheckCommand]] - code - gateway/tests/test_env_guard.py
- [[TestScrubOutput]] - code - gateway/tests/test_env_guard.py
- [[check_command()]] - code - gateway/security/env_guard.py
- [[scrub_output()]] - code - gateway/security/env_guard.py
- [[test_env_guard.py]] - code - gateway/tests/test_env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Env_Guard_security
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Git Guard (security)]]

## Top bridge nodes
- [[check_command()]] - degree 15, connects to 1 community
- [[scrub_output()]] - degree 8, connects to 1 community
- [[._record_leakage()]] - degree 6, connects to 1 community
- [[.check_command_execution()]] - degree 5, connects to 1 community
- [[.scrub_command_output()]] - degree 4, connects to 1 community