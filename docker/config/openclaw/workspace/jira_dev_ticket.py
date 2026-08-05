#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Generalized Jira dev-ticket helper (create / comment / transition).
#
# Reuses the exact op-proxy + Basic-auth wiring already proven by
# jira_weekly_review.py (SCRUM-81 weekly heartbeat) instead of inventing a new
# credential path. Used by the i-hdev/i-odev orchestration skills so every
# autonomous development batch gets a real Jira ticket created and kept up to
# date on the agentshroudai SCRUM board, not just a GitHub PR.
#
# Credential isolation: identical to jira_weekly_review.py — the Atlassian
# token/email/domain are NEVER stored in the bot image. They are fetched at run
# time from the gateway op-proxy (POST /credentials/op-proxy), which reads
# 1Password on the gateway side and returns a single field value per call.
# Auth to Jira is HTTP Basic: base64(email:token) against
# https://agentshroudai.atlassian.net.
#
# This module is self-contained (stdlib only) so it runs inside the Hermes /
# OpenClaw images from their own workspace directory. Pure functions (URL/
# payload builders, transition matching, auth header) are unit-tested with
# mocked HTTP — no real network in tests.
#
# CLI:
#   python3 jira_dev_ticket.py create --project SCRUM --summary "..." \
#       [--description "..."] [--issue-type Task] [--parent SCRUM-65] \
#       [--labels a,b,c]
#   python3 jira_dev_ticket.py comment --issue SCRUM-123 --body "..."
#   python3 jira_dev_ticket.py transition --issue SCRUM-123 --status "In Progress"
#
# Each subcommand prints a single-line JSON result to stdout on success and
# exits 0. On any failure it prints the error to stderr and exits 1 — never a
# silent no-op, so a caller (bot agent loop) can always tell success from
# failure rather than assuming the ticket update landed.

from __future__ import annotations

import argparse
import base64
import json
import logging
import os
import sys
import urllib.error
import urllib.request

# --- Constants ---------------------------------------------------------------

# The op:// reference the gateway allowlist must permit (see
# gateway/ingest_api/main.py ALLOWED_OP_PATHS) — same 1Password item
# jira_weekly_review.py already uses.
OP_ITEM = "op://Agent Shroud Bot Credentials/AgentShroud -Atlassian API Token"
OP_REF_TOKEN = f"{OP_ITEM}/token"
OP_REF_EMAIL = f"{OP_ITEM}/email"
OP_REF_DOMAIN = f"{OP_ITEM}/domain"

# Gateway op-proxy endpoint (same base URL Hermes/OpenClaw use elsewhere).
GATEWAY_BASE = os.environ.get("GATEWAY_OP_PROXY_URL", "http://gateway:8080")
OP_PROXY_PATH = "/credentials/op-proxy"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | jira-dev-ticket | %(message)s",
)
logger = logging.getLogger("jira_dev_ticket")


# --- Pure builders (unit-tested) ---------------------------------------------


def build_op_proxy_request(reference: str, auth_token: str) -> tuple[str, bytes, dict]:
    """Build (url, body, headers) for a POST to the gateway op-proxy."""
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


def _base_url(domain: str) -> str:
    clean = domain.strip().rstrip("/")
    if not clean:
        raise ValueError("domain is required")
    if not clean.startswith("http"):
        clean = f"https://{clean}"
    return clean


def build_issue_url(domain: str) -> str:
    """REST v3 URL for creating an issue."""
    return f"{_base_url(domain)}/rest/api/3/issue"


def build_comment_url(domain: str, issue_key: str) -> str:
    """REST v3 add-comment URL for an arbitrary issue key."""
    if not issue_key:
        raise ValueError("issue_key is required")
    return f"{_base_url(domain)}/rest/api/3/issue/{issue_key}/comment"


def build_transitions_url(domain: str, issue_key: str) -> str:
    """REST v3 transitions URL (GET to list, POST to apply) for an issue."""
    if not issue_key:
        raise ValueError("issue_key is required")
    return f"{_base_url(domain)}/rest/api/3/issue/{issue_key}/transitions"


def _adf_doc(text: str) -> dict:
    lines = [ln for ln in text.splitlines() if ln.strip()] or ["(no content)"]
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": ln}]}
            for ln in lines
        ],
    }


def build_comment_payload(body_text: str) -> dict:
    """Build the ADF (Atlassian Document Format) body for POST .../comment."""
    return {"body": _adf_doc(body_text)}


def build_create_issue_payload(
    project_key: str,
    summary: str,
    description: str = "",
    issue_type: str = "Task",
    parent_key: str | None = None,
    labels: list[str] | None = None,
) -> dict:
    """Build the REST v3 create-issue request body."""
    if not project_key:
        raise ValueError("project_key is required")
    if not summary:
        raise ValueError("summary is required")
    fields: dict = {
        "project": {"key": project_key},
        "summary": summary,
        "issuetype": {"name": issue_type},
    }
    if description:
        fields["description"] = _adf_doc(description)
    if labels:
        fields["labels"] = list(labels)
    if parent_key:
        fields["parent"] = {"key": parent_key}
    return {"fields": fields}


def find_transition_id(transitions: list[dict], status_name: str) -> str | None:
    """Match a transition by its own name or its destination status name."""
    target = status_name.strip().lower()
    for t in transitions:
        name = str(t.get("name", "")).strip().lower()
        to_name = str(t.get("to", {}).get("name", "")).strip().lower()
        if target in (name, to_name):
            return str(t.get("id"))
    return None


# --- Impure I/O (thin, not unit-tested; exercised via injection in tests) -----


def _http_request(
    url: str,
    body: bytes | None,
    headers: dict,
    method: str = "GET",
    timeout: int = 30,
) -> tuple[int, str]:
    """Issue one HTTP request and return (status_code, response_text).

    HTTPError is treated as a normal (status, body) response so callers can
    inspect Jira's error payload instead of unwinding via an exception.
    """
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(
            req, timeout=timeout
        ) as resp:  # noqa: S310 (fixed scheme)
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="replace")


def fetch_op_secret(reference: str, auth_token: str, request_fn=_http_request) -> str:
    """Fetch one secret field from the gateway op-proxy. Returns the value."""
    url, body, headers = build_op_proxy_request(reference, auth_token)
    status, text = request_fn(url, body, headers, "POST")
    if status != 200:
        raise RuntimeError(f"op-proxy returned HTTP {status} for a credential fetch")
    return json.loads(text)["value"]


def fetch_credentials(request_fn=_http_request) -> tuple[str, str, str]:
    """Resolve (token, email, domain) via the gateway op-proxy."""
    gateway_token = os.environ.get("GATEWAY_AUTH_TOKEN", "")
    if not gateway_token:
        raise RuntimeError("GATEWAY_AUTH_TOKEN not set — cannot reach op-proxy")
    token = fetch_op_secret(OP_REF_TOKEN, gateway_token, request_fn=request_fn)
    email = fetch_op_secret(OP_REF_EMAIL, gateway_token, request_fn=request_fn)
    domain = fetch_op_secret(OP_REF_DOMAIN, gateway_token, request_fn=request_fn)
    return token, email, domain


def _auth_headers(email: str, token: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": build_basic_auth_header(email, token),
    }


def create_issue(
    domain: str,
    email: str,
    token: str,
    project_key: str,
    summary: str,
    description: str = "",
    issue_type: str = "Task",
    parent_key: str | None = None,
    labels: list[str] | None = None,
    request_fn=_http_request,
) -> str:
    """Create a Jira issue. Returns the new issue key (e.g. 'SCRUM-124')."""
    payload = build_create_issue_payload(
        project_key, summary, description, issue_type, parent_key, labels
    )
    url = build_issue_url(domain)
    status, text = request_fn(
        url, json.dumps(payload).encode("utf-8"), _auth_headers(email, token), "POST"
    )
    if not (200 <= status < 300):
        raise RuntimeError(f"Jira create-issue rejected: HTTP {status} — {text[:300]}")
    return json.loads(text)["key"]


def add_comment(
    domain: str,
    email: str,
    token: str,
    issue_key: str,
    body_text: str,
    request_fn=_http_request,
) -> None:
    """Add a comment to an existing Jira issue."""
    payload = build_comment_payload(body_text)
    url = build_comment_url(domain, issue_key)
    status, text = request_fn(
        url, json.dumps(payload).encode("utf-8"), _auth_headers(email, token), "POST"
    )
    if not (200 <= status < 300):
        raise RuntimeError(f"Jira add-comment rejected: HTTP {status} — {text[:300]}")


def transition_issue(
    domain: str,
    email: str,
    token: str,
    issue_key: str,
    status_name: str,
    request_fn=_http_request,
) -> None:
    """Move an issue to the named status (matched against available transitions)."""
    url = build_transitions_url(domain, issue_key)
    status, text = request_fn(url, None, _auth_headers(email, token), "GET")
    if status != 200:
        raise RuntimeError(f"Jira get-transitions failed: HTTP {status} — {text[:300]}")
    transitions = json.loads(text).get("transitions", [])
    transition_id = find_transition_id(transitions, status_name)
    if transition_id is None:
        available = ", ".join(sorted({t.get("name", "?") for t in transitions}))
        raise RuntimeError(
            f"No transition named {status_name!r} available (have: {available})"
        )
    payload = {"transition": {"id": transition_id}}
    status, text = request_fn(
        url, json.dumps(payload).encode("utf-8"), _auth_headers(email, token), "POST"
    )
    if not (200 <= status < 300):
        raise RuntimeError(f"Jira transition rejected: HTTP {status} — {text[:300]}")


# --- Orchestration -------------------------------------------------------------


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="jira_dev_ticket")
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="Create a new Jira issue")
    p_create.add_argument("--project", required=True)
    p_create.add_argument("--summary", required=True)
    p_create.add_argument("--description", default="")
    p_create.add_argument("--issue-type", default="Task")
    p_create.add_argument("--parent", default=None)
    p_create.add_argument("--labels", default=None, help="comma-separated")

    p_comment = sub.add_parser("comment", help="Add a comment to an existing issue")
    p_comment.add_argument("--issue", required=True)
    p_comment.add_argument("--body", required=True)

    p_transition = sub.add_parser("transition", help="Move an issue to a named status")
    p_transition.add_argument("--issue", required=True)
    p_transition.add_argument("--status", required=True)

    return parser


def run(argv: list[str], request_fn=_http_request) -> int:
    """Parse argv, resolve credentials, dispatch the subcommand. Returns exit code."""
    args = _build_arg_parser().parse_args(argv)

    try:
        token, email, domain = fetch_credentials(request_fn=request_fn)
    except RuntimeError as exc:
        logger.error("Credential fetch failed: %s", exc)
        print(str(exc), file=sys.stderr)
        return 1

    try:
        if args.command == "create":
            labels = (
                [s.strip() for s in args.labels.split(",")] if args.labels else None
            )
            key = create_issue(
                domain,
                email,
                token,
                args.project,
                args.summary,
                args.description,
                args.issue_type,
                args.parent,
                labels,
                request_fn=request_fn,
            )
            print(json.dumps({"key": key}))
        elif args.command == "comment":
            add_comment(
                domain, email, token, args.issue, args.body, request_fn=request_fn
            )
            print(json.dumps({"ok": True}))
        elif args.command == "transition":
            transition_issue(
                domain, email, token, args.issue, args.status, request_fn=request_fn
            )
            print(json.dumps({"ok": True}))
    except (RuntimeError, ValueError) as exc:
        logger.error("%s failed: %s", args.command, exc)
        print(str(exc), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
