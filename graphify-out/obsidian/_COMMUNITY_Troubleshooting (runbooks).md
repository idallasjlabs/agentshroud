---
type: community
cohesion: 0.11
members: 18
---

# Troubleshooting (runbooks)

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[ClamAV `SelfCheck Database status OK.`]] - document - docs/runbooks/troubleshooting.md
- [[ClamAV `Socket for clamd not found yet, retrying (N1800)...`]] - document - docs/runbooks/troubleshooting.md
- [[ClamAV `WARNING Can't query current.cvd.clamav.net`  `ERROR Database update process failed`]] - document - docs/runbooks/troubleshooting.md
- [[Gateway `CONNECT tunnel established wss-primary.slack.com443`]] - document - docs/runbooks/troubleshooting.md
- [[Gateway `GET status - 200 (0.000s)` every 30 seconds]] - document - docs/runbooks/troubleshooting.md
- [[Gateway `POST telegram-apibotgetUpdates - 200 (30–32s)`]] - document - docs/runbooks/troubleshooting.md
- [[Gateway duplicate access log lines for every request]] - document - docs/runbooks/troubleshooting.md
- [[Known Log Messages]] - document - docs/runbooks/troubleshooting.md
- [[`POST apialerts - 404 (Nms)` (resolved in v0.9.0)]] - document - docs/runbooks/troubleshooting.md
- [[`ERROR socket-modeSocketModeClientN Failed to retrieve a new WSS URL`]] - document - docs/runbooks/troubleshooting.md
- [[`WARN bolt-app http request failed connect ECONNREFUSED 10.254.110.28181`]] - document - docs/runbooks/troubleshooting.md
- [[`WARN bolt-app http request failed getaddrinfo ENOTFOUND gateway`]] - document - docs/runbooks/troubleshooting.md
- [[`WARN socket-modeSlackWebSocketN A pong wasn't received from the server before the timeout of 5000ms!`]] - document - docs/runbooks/troubleshooting.md
- [[`agentembedded embedded run agent end isError=true error=Ollama API stream ended without a final response`]] - document - docs/runbooks/troubleshooting.md
- [[`gateway ⚠️ Gateway is binding to a non-loopback address`]] - document - docs/runbooks/troubleshooting.md
- [[`health-monitor slackdefault health-monitor restarting (reason stale-socket)`]] - document - docs/runbooks/troubleshooting.md
- [[`openclaw Non-fatal unhandled rejection (continuing) Error A request error occurred`]] - document - docs/runbooks/troubleshooting.md
- [[`telegram autoSelectFamily=false (config)`  `fetch fallback forcing autoSelectFamily=false + dnsResultOrder=ipv4first`]] - document - docs/runbooks/troubleshooting.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Troubleshooting_runbooks
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Troubleshooting (runbooks)]]

## Top bridge nodes
- [[Known Log Messages]] - degree 19, connects to 1 community