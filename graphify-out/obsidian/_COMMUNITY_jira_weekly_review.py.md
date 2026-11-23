---
type: community
members: 31
---

# jira_weekly_review.py

**Members:** 31 nodes

## Members
- [[Build (url, body, headers) for a POST to the gateway op-proxy. Mirrors…]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Build the Atlassian Document Format (ADF) body for POST ...comment. The REST…]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Build the REST v3 add-comment URL against the cloud-id gateway.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Compose the human-readable weekly summary posted as the comment. - commits…]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Extract SCRUM-n keys mentioned in commit subjects.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Fetch creds, build summary, post the comment. Returns a process exit code.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Fetch one secret field from the gateway op-proxy. Returns the value.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[GET and return (status_code, response_text). HTTPError is treated as a normal…]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[POST and return (status_code, response_text). Raises urllib errors up.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[POST the ADF comment to Jira with Basic auth. Returns (status, text).]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Resolve a site domain to its Atlassian cloud ID via the public, unauthenticated…]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Return 'shorthash subject' lines for commits in the last 7 days. Degrades to …]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Return the HTTP Basic auth header value base64(emailtoken).]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[Unauthenticated site-to-cloud-ID discovery URL.]] - rationale - docker/config/hermes/workspace/jira_weekly_review.py
- [[_adf_paragraph()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[_git_commits_last_week()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[_http_get()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[_http_post_json()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_basic_auth_header()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_comment_payload()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_comment_url()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_op_proxy_request()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_tenant_info_url()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[build_weekly_summary()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[datetime_6]] - code
- [[extract_scrum_items()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[fetch_op_secret()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[jira_weekly_review.py]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[post_comment()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[resolve_cloud_id()]] - code - docker/config/hermes/workspace/jira_weekly_review.py
- [[run()_2]] - code - docker/config/hermes/workspace/jira_weekly_review.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/jira_weekly_reviewpy
SORT file.name ASC
```
