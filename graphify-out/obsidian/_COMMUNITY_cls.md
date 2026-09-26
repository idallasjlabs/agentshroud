---
type: community
cohesion: 0.17
members: 18
---

# cls

**Cohesion:** 0.17 - loosely connected
**Members:** 18 nodes

## Members
- [[._scan_encoded_payloads()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_hidden_content()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_pii()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_prompt_injection()]] - code - gateway/proxy/web_content_scanner.py
- [[._scan_zero_width()]] - code - gateway/proxy/web_content_scanner.py
- [[.finding_summary()]] - code - gateway/proxy/web_content_scanner.py
- [[.flagged()_1]] - code - gateway/proxy/web_content_scanner.py
- [[.scan()_1]] - code - gateway/proxy/web_content_scanner.py
- [[A single finding from content scanning.]] - rationale - gateway/proxy/web_content_scanner.py
- [[ContentFinding]] - code - gateway/proxy/web_content_scanner.py
- [[Detect zero-width character sequences (steganographic attacks).]] - rationale - gateway/proxy/web_content_scanner.py
- [[Result of scanning web content.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan HTML for hidden instructions in comments, invisible elements, meta tags.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan content for security issues.          Args             content The web co]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for base64-encoded or otherwise obfuscated payloads.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan for prompt injection patterns.]] - rationale - gateway/proxy/web_content_scanner.py
- [[Scan response content for PII.]] - rationale - gateway/proxy/web_content_scanner.py
- [[ScanResult]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/cls
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[ScanResult]] - degree 10, connects to 1 community
- [[.scan()_1]] - degree 8, connects to 1 community
- [[ContentFinding]] - degree 7, connects to 1 community
- [[._scan_encoded_payloads()]] - degree 5, connects to 1 community
- [[._scan_hidden_content()]] - degree 5, connects to 1 community