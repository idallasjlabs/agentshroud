---
source_file: "docker/config/hermes/workspace/jira_weekly_review.py"
type: "code"
community: "jira_weekly_review.py"
location: "L281"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/jira_weekly_reviewpy
---

# run()

## Connections
- [[Fetch creds, build summary, post the comment. Returns a process exit code.]] - `rationale_for` [EXTRACTED]
- [[_git_commits_last_week()]] - `calls` [EXTRACTED]
- [[build_comment_payload()_2]] - `calls` [EXTRACTED]
- [[build_weekly_summary()]] - `calls` [EXTRACTED]
- [[extract_scrum_items()]] - `calls` [EXTRACTED]
- [[fetch_op_secret()_2]] - `calls` [EXTRACTED]
- [[jira_dev_ticket run()]] - `semantically_similar_to` [INFERRED]
- [[jira_weekly_review.py]] - `contains` [EXTRACTED]
- [[post_comment()]] - `calls` [EXTRACTED]
- [[resolve_cloud_id()_2]] - `calls` [EXTRACTED]
- [[test_jira_weekly_review.py]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/jira_weekly_reviewpy