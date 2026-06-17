---
type: community
cohesion: 0.11
members: 35
---

# Module Group 136

**Cohesion:** 0.11 - loosely connected
**Members:** 35 nodes

## Members
- [[.__init__()_11]] - code - gateway/proxy/collaborator_greeter.py
- [[._load_state()]] - code - gateway/proxy/collaborator_greeter.py
- [[._load_taglines()]] - code - gateway/proxy/collaborator_greeter.py
- [[CollaboratorGreeter]] - code - gateway/proxy/collaborator_greeter.py
- [[CollaboratorGreeter creates its own httpx client lazily.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[Sends a branded greeting photo to each (bot, user) pair once per 24 h.]] - rationale - gateway/proxy/collaborator_greeter.py
- [[Unexpected exception in maybe_greet must be caught and return False.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[When state JSON is corrupt AND writing the empty recovery file fails, no excepti]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_err_response()]] - code - gateway/tests/test_collaborator_greeter.py
- [[_load_state reads and returns a pre-existing valid JSON dict.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_load_state returns {} when state file is a JSON list (not a dict).]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_load_taglines falls back to default when JSON is valid but not a list.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_make_greeter()]] - code - gateway/tests/test_collaborator_greeter.py
- [[_ok_response()]] - code - gateway/tests/test_collaborator_greeter.py
- [[_persist_state failure must not raise.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[collaborator_greeter.py]] - code - gateway/proxy/collaborator_greeter.py
- [[test_bot_isolation()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_caption_length_clamped()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_collaborator_greeter.py]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_exception_in_maybe_greet_returns_false()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_first_call_sends_greeting_and_persists_state()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_first_name_none_uses_there_fallback()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_get_client_creates_own_when_not_injected()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_loads_existing_valid_dict()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_non_dict_json_returns_empty()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_write_empty_fails_silently()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_taglines_with_non_list_json_falls_back()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_missing_logo_returns_false()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_missing_taglines_falls_back_to_default()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_persist_state_exception_is_swallowed()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_random_tagline_pulled_from_file()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_repeat_after_24h_greets_again()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_repeat_within_24h_is_suppressed()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_send_failure_does_not_persist_state()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_state_file_corruption_recovers()]] - code - gateway/tests/test_collaborator_greeter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_136
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 311]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[CollaboratorGreeter]] - degree 21, connects to 2 communities
- [[.__init__()_11]] - degree 4, connects to 1 community
- [[collaborator_greeter.py]] - degree 2, connects to 1 community