#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# SCRUM-81 — Hermes weekly Jira review cron.
#
# Purpose: post a REAL authenticated comment on SCRUM-81 every 7 days so the
# Atlassian API token / bot account never goes idle. The cron job in
# init-config.sh / cron/jobs.yaml runs this script every Sunday 09:00.
#
# Credential isolation: the Atlassian token/email/domain are NEVER stored in the
# Hermes container. They are fetched at run time from the gateway op-proxy
# (POST /credentials/op-proxy), which reads 1Password on the gateway side and
# returns a single field value per call. Auth to Jira is HTTP Basic:
# base64(email:token) against https://<domain> (agentshroudai.atlassian.net).
#
# This module is self-contained (stdlib only) so it runs inside the Hermes image
# from /opt/data/workspace/. Pure functions (summary builder, ADF comment-payload
# builder, op-proxy request builder, Basic auth header) are unit-tested with mocked
# HTTP — no real network in tests. Failures are logged and the process exits 0 for
# the "flag" path so a transient outage never crashes the cron; a hard exit code 1
# is reserved for a genuine auth/config failure the owner should see.

from __future__ import annotations

import base64
import json
import logging
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

# --- Constants ---------------------------------------------------------------

# The op:// references the gateway allowlist must permit (see
# gateway/ingest_api/main.py ALLOWED_OP_PATHS). One field per op-proxy call.
OP_ITEM = "op://Agent Shroud Bot Credentials/AgentShroud -Atlassian API Token"
OP_REF_TOKEN = f"{OP_ITEM}/token"
OP_REF_EMAIL = f"{OP_ITEM}/email"
OP_REF_DOMAIN = f"{OP_ITEM}/domain"

# Target issue: SCRUM-81 on agentshroudai.atlassian.net.
ISSUE_KEY = "SCRUM-81"

# Gateway op-proxy endpoint (same base URL Hermes uses elsewhere).
GATEWAY_BASE = os.environ.get("GATEWAY_OP_PROXY_URL", "http://gateway:8080")
OP_PROXY_PATH = "/credentials/op-proxy"

# Where the git repo lives inside the Hermes container, if mounted. When absent,
# the summary degrades gracefully to "no local repo" rather than crashing.
REPO_DIR = os.environ.get("AGENTSHROUD_REPO_DIR", "/opt/data/repo")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | jira-weekly-review | %(message)s",
)
logger = logging.getLogger("jira_weekly_review")


# --- Pure builders (unit-tested) ---------------------------------------------


def build_op_proxy_request(reference: str, auth_token: str) -> tuple[str, bytes, dict]:
    """Build (url, body, headers) for a POST to the gateway op-proxy.

    Mirrors email_helper.sh: Bearer gateway auth + X-AgentShroud-System header.
    """
    url = f"{GATEWAY_BASE}{OP_PROXY_PATH}"
    body = json.dumps({"reference": reference}).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}",
        "X-AgentShroud-System": "1",
    }
    return url, body, headers


def build_basic_auth_header(email: str, token: str) -> str:
    """Return the HTTP Basic auth header value: base64(email:token)."""
    if not email or not token:
        raise ValueError("email and token are both required for Basic auth")
    raw = f"{email}:{token}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _adf_paragraph(text: str) -> dict:
    return {
        "type": "paragraph",
        "content": [{"type": "text", "text": text}],
    }


def build_comment_payload(summary_text: str) -> dict:
    """Build the Atlassian Document Format (ADF) body for POST .../comment.

    The REST v3 comment API requires an ADF document, not plain text.
    Each line of the summary becomes its own paragraph so long summaries render.
    """
    lines = [ln for ln in summary_text.splitlines() if ln.strip()]
    if not lines:
        lines = ["(no activity recorded this week)"]
    return {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [_adf_paragraph(ln) for ln in lines],
        }
    }


def build_comment_url(domain: str, issue_key: str = ISSUE_KEY) -> str:
    """Build the REST v3 add-comment URL for the given cloud domain."""
    clean = domain.strip().rstrip("/")
    if not clean:
        raise ValueError("domain is required to build the comment URL")
    if not clean.startswith("http"):
        clean = f"https://{clean}"
    return f"{clean}/rest/api/3/issue/{issue_key}/comment"


def build_weekly_summary(
    commits: list[str],
    scrum_items: list[str],
    now: datetime | None = None,
    last_activity: datetime | None = None,
) -> str:
    """Compose the human-readable weekly summary posted as the comment.

    - commits:      short "hash subject" strings from the last 7 days
    - scrum_items:  SCRUM-* keys referenced in those commits (advanced this week)
    - staleness:    flag if there was no repo activity in the last 7 days, or if
                    the last recorded activity is older than 7 days.
    """
    now = now or datetime.now(timezone.utc)
    week_ago = now - timedelta(days=7)
    header = (
        f"AgentShroud weekly review — {week_ago.date().isoformat()} "
        f"to {now.date().isoformat()} (automated Hermes cron, SCRUM-81)."
    )

    if commits:
        shipped = [f"Shipped this week ({len(commits)} commits):"]
        shipped += [f"- {c}" for c in commits[:20]]
        if len(commits) > 20:
            shipped.append(f"- ...and {len(commits) - 20} more")
    else:
        shipped = ["Shipped this week: no commits in the last 7 days."]

    if scrum_items:
        advanced = ["SCRUM items advanced: " + ", ".join(sorted(set(scrum_items)))]
    else:
        advanced = ["SCRUM items advanced: none referenced in commits this week."]

    stale = not commits or (last_activity is not None and last_activity < week_ago)
    staleness = [
        (
            "Staleness flag: STALE — no development activity detected in the last 7 days."
            if stale
            else "Staleness flag: OK — active development in the last 7 days."
        )
    ]

    return "\n".join([header, "", *shipped, "", *advanced, "", *staleness])


def extract_scrum_items(commits: list[str]) -> list[str]:
    """Extract SCRUM-<n> keys mentioned in commit subjects."""
    import re

    keys: list[str] = []
    for line in commits:
        keys.extend(re.findall(r"SCRUM-\d+", line))
    return keys


# --- Impure I/O (thin, not unit-tested; exercised via injection in tests) -----


def _git_commits_last_week(repo_dir: str = REPO_DIR) -> list[str]:
    """Return 'shorthash subject' lines for commits in the last 7 days.

    Degrades to [] on any failure (no repo mounted, git missing, etc.).
    """
    try:
        result = subprocess.run(
            ["git", "-C", repo_dir, "log", "--since=7.days", "--pretty=format:%h %s"],
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        logger.warning("git log unavailable (%s) — summary will note no local repo", exc)
        return []
    if result.returncode != 0:
        logger.warning("git log returned %s — treating as no commits", result.returncode)
        return []
    return [ln for ln in result.stdout.splitlines() if ln.strip()]


def _http_post_json(url: str, body: bytes, headers: dict, timeout: int = 30) -> tuple[int, str]:
    """POST and return (status_code, response_text). Raises urllib errors up."""
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (fixed scheme)
        return resp.status, resp.read().decode("utf-8", errors="replace")


def fetch_op_secret(reference: str, auth_token: str, post_fn=_http_post_json) -> str:
    """Fetch one secret field from the gateway op-proxy. Returns the value."""
    url, body, headers = build_op_proxy_request(reference, auth_token)
    status, text = post_fn(url, body, headers)
    if status != 200:
        raise RuntimeError(f"op-proxy returned HTTP {status} for a credential fetch")
    return json.loads(text)["value"]


def post_comment(
    domain: str,
    email: str,
    token: str,
    payload: dict,
    post_fn=_http_post_json,
) -> tuple[int, str]:
    """POST the ADF comment to Jira with Basic auth. Returns (status, text)."""
    url = build_comment_url(domain)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": build_basic_auth_header(email, token),
    }
    body = json.dumps(payload).encode("utf-8")
    return post_fn(url, body, headers)


# --- Orchestration -----------------------------------------------------------


def run(post_fn=_http_post_json, commits_fn=_git_commits_last_week) -> int:
    """Fetch creds, build summary, post the comment. Returns a process exit code."""
    gateway_token = os.environ.get("GATEWAY_AUTH_TOKEN", "")
    if not gateway_token:
        logger.error("GATEWAY_AUTH_TOKEN not set — cannot reach op-proxy; aborting")
        return 1

    try:
        token = fetch_op_secret(OP_REF_TOKEN, gateway_token, post_fn=post_fn)
        email = fetch_op_secret(OP_REF_EMAIL, gateway_token, post_fn=post_fn)
        domain = fetch_op_secret(OP_REF_DOMAIN, gateway_token, post_fn=post_fn)
    except (urllib.error.URLError, RuntimeError, KeyError, ValueError) as exc:
        logger.error("Failed to fetch Atlassian credentials from op-proxy: %s", exc)
        return 1

    commits = commits_fn()
    scrum_items = extract_scrum_items(commits)
    summary = build_weekly_summary(commits, scrum_items)
    payload = build_comment_payload(summary)

    try:
        status, text = post_comment(domain, email, token, payload, post_fn=post_fn)
    except urllib.error.URLError as exc:
        logger.error("Jira comment POST failed (network): %s", exc)
        return 1

    if 200 <= status < 300:
        logger.info("Posted weekly review comment on %s (HTTP %s)", ISSUE_KEY, status)
        return 0

    logger.error("Jira comment POST rejected: HTTP %s — %s", status, text[:300])
    return 1


if __name__ == "__main__":
    sys.exit(run())
