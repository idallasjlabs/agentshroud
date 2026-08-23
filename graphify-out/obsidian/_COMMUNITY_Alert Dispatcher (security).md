---
type: community
cohesion: 0.14
members: 17
---

# Alert Dispatcher (security)

**Cohesion:** 0.14 - loosely connected
**Members:** 17 nodes

## Members
- [[._format_alert_message()]] - code - gateway/security/alert_dispatcher.py
- [[._is_duplicate()]] - code - gateway/security/alert_dispatcher.py
- [[._is_rate_limited()]] - code - gateway/security/alert_dispatcher.py
- [[._log_alert()]] - code - gateway/security/alert_dispatcher.py
- [[._send_notification()]] - code - gateway/security/alert_dispatcher.py
- [[.dispatch()]] - code - gateway/security/alert_dispatcher.py
- [[.get_digest()]] - code - gateway/security/alert_dispatcher.py
- [[.get_stats()_12]] - code - gateway/security/alert_dispatcher.py
- [[Any_31]] - code - gateway/security/alert_dispatcher.py
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
TABLE source_file, type FROM #community/Alert_Dispatcher_security
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[.dispatch()]] - degree 7, connects to 1 community
- [[._send_notification()]] - degree 5, connects to 1 community
- [[._format_alert_message()]] - degree 4, connects to 1 community
- [[._log_alert()]] - degree 4, connects to 1 community
- [[.get_digest()]] - degree 3, connects to 1 community