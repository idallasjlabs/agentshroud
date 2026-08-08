---
type: community
cohesion: 0.27
members: 13
---

# browser-extension/background.js

**Cohesion:** 0.27 - loosely connected
**Members:** 13 nodes

## Members
- [[AgentShroudForwarder.buildClipPayload]] - code - browser-extension/lib/forwarder.js
- [[AgentShroudForwarder.buildClipTarget]] - code - browser-extension/lib/forwarder.js
- [[AgentShroudForwarder.buildUrlPayload]] - code - browser-extension/lib/forwarder.js
- [[AgentShroudForwarder.postForward]] - code - browser-extension/lib/forwarder.js
- [[AgentShroudForwarder.validateConfig]] - code - browser-extension/lib/forwarder.js
- [[background.js]] - code - browser-extension/background.js
- [[clipPage()]] - code - browser-extension/background.js
- [[extractPageContent()]] - code - browser-extension/background.js
- [[forwardUrl()]] - code - browser-extension/background.js
- [[getActiveTab()]] - code - browser-extension/background.js
- [[loadConfig()]] - code - browser-extension/background.js
- [[notify()]] - code - browser-extension/background.js
- [[reportResult()]] - code - browser-extension/background.js

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/browser-extension/backgroundjs
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_browser-extensionpopup.js]]
- 1 edge to [[_COMMUNITY_browser-extensionmanifest.json]]
- 1 edge to [[_COMMUNITY_browser-extensionREADME]]
- 1 edge to [[_COMMUNITY_browser-extensionoptions.js]]

## Top bridge nodes
- [[background.js]] - degree 11, connects to 3 communities
- [[loadConfig()]] - degree 4, connects to 1 community