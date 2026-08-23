---
type: community
cohesion: 0.33
members: 7
---

# Gemini Review (scripts)

**Cohesion:** 0.33 - loosely connected
**Members:** 7 nodes

## Members
- [[Call Gemini API and return the review text and exit code.      Returns]] - rationale - scripts/gemini-review.py
- [[PATH_4]] - code - scripts/peer-review.sh
- [[call_gemini()]] - code - scripts/gemini-review.py
- [[gemini-review.py]] - code - scripts/gemini-review.py
- [[main()_18]] - code - scripts/gemini-review.py
- [[peer-review.sh]] - code - scripts/peer-review.sh
- [[peer-review.sh script]] - code - scripts/peer-review.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gemini_Review_scripts
SORT file.name ASC
```
