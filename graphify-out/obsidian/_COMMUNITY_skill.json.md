---
type: community
cohesion: 0.30
members: 15
---

# skill.json

**Cohesion:** 0.30 - loosely connected
**Members:** 15 nodes

## Members
- [[Unexpected exception in maybe_greet must be caught and return False.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_err_response()]] - code - gateway/tests/test_collaborator_greeter.py
- [[_make_greeter()]] - code - gateway/tests/test_collaborator_greeter.py
- [[_ok_response()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_bot_isolation()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_collaborator_greeter.py]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_exception_in_maybe_greet_returns_false()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_first_call_sends_greeting_and_persists_state()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_first_name_none_uses_there_fallback()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_missing_taglines_falls_back_to_default()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_random_tagline_pulled_from_file()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_repeat_after_24h_greets_again()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_repeat_within_24h_is_suppressed()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_send_failure_does_not_persist_state()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_state_file_corruption_recovers()]] - code - gateway/tests/test_collaborator_greeter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/skilljson
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Validation Runner Specialist]]

## Top bridge nodes
- [[test_collaborator_greeter.py]] - degree 22, connects to 1 community
- [[_make_greeter()]] - degree 10, connects to 1 community
- [[test_missing_taglines_falls_back_to_default()]] - degree 3, connects to 1 community
- [[test_state_file_corruption_recovers()]] - degree 3, connects to 1 community