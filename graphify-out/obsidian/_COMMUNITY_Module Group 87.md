---
type: community
cohesion: 0.05
members: 46
---

# Module Group 87

**Cohesion:** 0.05 - loosely connected
**Members:** 46 nodes

## Members
- [[._active_send_token()]] - code - gateway/proxy/telegram_proxy.py
- [[._answer_callback_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._collaborator_rate_limit_retry_after_seconds()]] - code - gateway/proxy/telegram_proxy.py
- [[._edit_telegram_message()]] - code - gateway/proxy/telegram_proxy.py
- [[._forward_to_telegram()]] - code - gateway/proxy/telegram_proxy.py
- [[._queue_collaborator_access_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_display_name()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_collaborator_pending_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_healthcheck_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_help_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_model_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_notice_with_fallback()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_start_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_status_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_local_whoami_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_activity_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_collabs_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_owner_pending_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_rate_limit_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_stranger_rate_limit_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._send_telegram_with_keyboard()]] - code - gateway/proxy/telegram_proxy.py
- [[._telegram_create_invite_link()]] - code - gateway/proxy/telegram_proxy.py
- [[._telegram_kick_member()]] - code - gateway/proxy/telegram_proxy.py
- [[Create a single-use invite link for a Telegram group. Returns URL or None.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Dismiss the Telegram inline button spinner with a brief toast.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Edit an existing Telegram message in-place (removes inline keyboard too).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Estimate seconds until collaborator rate limit window opens again.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Forward request to real Telegram API and return parsed response.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Kick (ban + unban) a user from a Telegram group. Returns True on success.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Notify a collaborator they have exceeded the hourly rate limit.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Notify an unknownunapproved user they have exceeded the access request rate lim]] - rationale - gateway/proxy/telegram_proxy.py
- [[Per-request bot token for gateway-originated Telegram sends.          Returns th]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue owner approval request for unknownrevoked users.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve a readable label for user id when available.          Priority user sel]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send a Telegram message with an inline keyboard.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic help command list without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic start notice without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic status summary without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic gateway health status without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic identityrole notice to simplify approval workflows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic model status without model invocation.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic owner pending-approval snapshot.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send deterministic pending-approval notice to unknownrevoked users.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send local command response with deterministic fallback text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send owner a summary of recent collaborator activity (last hour).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send owner-friendly collaborator roster with known labels.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_87
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 4 edges to [[_COMMUNITY_Module Group 160]]
- 1 edge to [[_COMMUNITY_Collaborator Responses]]

## Top bridge nodes
- [[._active_send_token()]] - degree 13, connects to 2 communities
- [[._send_local_notice_with_fallback()]] - degree 13, connects to 2 communities
- [[._queue_collaborator_access_request()]] - degree 6, connects to 2 communities
- [[._resolve_display_name()]] - degree 6, connects to 2 communities
- [[._forward_to_telegram()]] - degree 5, connects to 2 communities