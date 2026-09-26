---
type: community
cohesion: 0.10
members: 24
---

# Validation Runner Specialist

**Cohesion:** 0.10 - loosely connected
**Members:** 24 nodes

## Members
- [[.__init__()_19]] - code - gateway/proxy/collaborator_greeter.py
- [[._get_client()]] - code - gateway/proxy/collaborator_greeter.py
- [[._load_state()]] - code - gateway/proxy/collaborator_greeter.py
- [[._load_taglines()]] - code - gateway/proxy/collaborator_greeter.py
- [[._persist_state()]] - code - gateway/proxy/collaborator_greeter.py
- [[.maybe_greet()]] - code - gateway/proxy/collaborator_greeter.py
- [[CollaboratorGreeter]] - code - gateway/proxy/collaborator_greeter.py
- [[CollaboratorGreeter creates its own httpx client lazily.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[Greet user if cooldown has expired. Returns True when greeting was sent.]] - rationale - gateway/proxy/collaborator_greeter.py
- [[Sends a branded greeting photo to each (bot, user) pair once per 24 h.]] - rationale - gateway/proxy/collaborator_greeter.py
- [[When state JSON is corrupt AND writing the empty recovery file fails, no excepti]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_load_state reads and returns a pre-existing valid JSON dict.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_load_state returns {} when state file is a JSON list (not a dict).]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_load_taglines falls back to default when JSON is valid but not a list.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[_persist_state failure must not raise.]] - rationale - gateway/tests/test_collaborator_greeter.py
- [[collaborator_greeter.py]] - code - gateway/proxy/collaborator_greeter.py
- [[test_caption_length_clamped()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_get_client_creates_own_when_not_injected()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_loads_existing_valid_dict()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_non_dict_json_returns_empty()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_state_write_empty_fails_silently()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_load_taglines_with_non_list_json_falls_back()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_missing_logo_returns_false()]] - code - gateway/tests/test_collaborator_greeter.py
- [[test_persist_state_exception_is_swallowed()]] - code - gateway/tests/test_collaborator_greeter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Validation_Runner_Specialist
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_skill.json]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_AgentShroud v1.0.0 Fortress Release Announcement]]
- 1 edge to [[_COMMUNITY_AgentShroud — Master Feature List (Everything Ev]]

## Top bridge nodes
- [[CollaboratorGreeter]] - degree 22, connects to 3 communities
- [[.__init__()_19]] - degree 4, connects to 1 community
- [[._get_client()]] - degree 3, connects to 1 community
- [[test_get_client_creates_own_when_not_injected()]] - degree 3, connects to 1 community
- [[test_load_state_loads_existing_valid_dict()]] - degree 3, connects to 1 community