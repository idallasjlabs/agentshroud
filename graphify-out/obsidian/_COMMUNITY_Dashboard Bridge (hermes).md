---
type: community
cohesion: 0.19
members: 18
---

# Dashboard Bridge (hermes)

**Cohesion:** 0.19 - loosely connected
**Members:** 18 nodes

## Members
- [[Read up to the end of the request's header block (rnrn).      Returns (h]] - rationale - docker/bots/hermes/dashboard_bridge.py
- [[Rewrite the Host header to `new_host` and normalize Connection framing.      `he]] - rationale - docker/bots/hermes/dashboard_bridge.py
- [[StreamReader]] - code - docker/bots/hermes/dashboard_bridge.py
- [[StreamReader_1]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[StreamReader_4]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[StreamWriter]] - code - docker/bots/hermes/dashboard_bridge.py
- [[StreamWriter_1]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[StreamWriter_3]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[_handle()]] - code - docker/bots/hermes/dashboard_bridge.py
- [[_handle()_1]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[_pipe()]] - code - docker/bots/hermes/dashboard_bridge.py
- [[_pump()]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[_read_request_headers()]] - code - docker/bots/hermes/dashboard_bridge.py
- [[dashboard_bridge.py]] - code - docker/bots/hermes/dashboard_bridge.py
- [[docker_proxy_relay.py]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[main()_2]] - code - docker/bots/hermes/dashboard_bridge.py
- [[main()_3]] - code - docker/bots/hermes/docker_proxy_relay.py
- [[rewrite_request_headers()]] - code - docker/bots/hermes/dashboard_bridge.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Dashboard_Bridge_hermes
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Apply Patches (openclaw)]]
- 1 edge to [[_COMMUNITY_Run Standalone (hermes)]]
- 1 edge to [[_COMMUNITY_Start (hermes)]]

## Top bridge nodes
- [[docker_proxy_relay.py]] - degree 7, connects to 3 communities