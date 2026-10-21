---
type: community
members: 17
---

# AgentShroud — Master Feature List (Everything Ever Mentioned)

**Members:** 17 nodes

## Members
- [[dot-_format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[dot-_send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[dot-dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[dot-get_stats()_19]] - code - gateway/security/alert_dispatcher.py
- [[Any_61]] - code - gateway/security/alert_dispatcher.py
- [[Append alert to JSONL log file.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if alert was already seen within dedup window.]] - rationale - gateway/security/alert_dispatcher.py
- [[Check if we've exceeded the rate limit.]] - rationale - gateway/security/alert_dispatcher.py
- [[Dispatch an alert based on severity.          Args             alert Alert dic]] - rationale - gateway/security/alert_dispatcher.py
- [[Format alert as human-readable message.]] - rationale - gateway/security/alert_dispatcher.py
- [[Get buffered alerts for daily digest.          Args             clear Clear bu]] - rationale - gateway/security/alert_dispatcher.py
- [[Get dispatcher statistics.]] - rationale - gateway/security/alert_dispatcher.py
- [[POST alert to apialerts with bounded retry + backoff.          Returns True on]] - rationale - gateway/security/alert_dispatcher.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud__Master_Feature_List_Everything_Ever_Mentioned
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[dot-dispatch()]] - degree 7, connects to 1 community
- [[dot-_send_notification()]] - degree 5, connects to 1 community
- [[dot-_format_alert_message()]] - degree 4, connects to 1 community
- [[dot-_log_alert()]] - degree 4, connects to 1 community
- [[dot-get_digest()]] - degree 3, connects to 1 community
