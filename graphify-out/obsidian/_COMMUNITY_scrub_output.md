---
type: community
members: 10
---

# scrub_output

**Members:** 10 nodes

## Members
- [[dot-test_clean_text_unchanged()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_aws_key()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_github_token()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_multiple_keys()]] - code - gateway/tests/test_env_guard.py
- [[dot-test_scrubs_openai_key()]] - code - gateway/tests/test_env_guard.py
- [[Scrub API keys and sensitive patterns from text output. Args text Text to…]] - rationale - gateway/security/env_guard.py
- [[Test Environment Leakage Guard.]] - rationale - gateway/tests/test_env_guard.py
- [[TestScrubOutput]] - code - gateway/tests/test_env_guard.py
- [[scrub_output()]] - code - gateway/security/env_guard.py
- [[test_env_guard.py]] - code - gateway/tests/test_env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scrub_output
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_check_command]]
- 2 edges to [[_COMMUNITY_env_guard.py]]

## Top bridge nodes
- [[test_env_guard.py]] - degree 6, connects to 2 communities
- [[scrub_output()]] - degree 8, connects to 1 community
