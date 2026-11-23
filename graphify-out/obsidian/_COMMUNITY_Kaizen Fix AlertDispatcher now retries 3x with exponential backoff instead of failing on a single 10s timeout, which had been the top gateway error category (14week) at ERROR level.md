---
type: community
members: 1
---

# Kaizen Fix: AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14/week) at ERROR level

**Members:** 1 nodes

## Members
- [[Kaizen Fix AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14week) at ERROR level]] - rationale - gateway/tests/test_alert_dispatcher_retry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Kaizen_Fix_AlertDispatcher_now_retries_3x_with_exponential_backoff_instead_of_failing_on_a_single_10s_timeout_which_had_been_the_top_gateway_error_category_14/week_at_ERROR_level
SORT file.name ASC
```
