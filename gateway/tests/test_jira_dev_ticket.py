# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the generalized Jira dev-ticket helper (create / comment / transition).

The script lives in both bot image workspaces (docker/config/hermes/workspace/
jira_dev_ticket.py and docker/config/openclaw/workspace/jira_dev_ticket.py — the
two files must stay byte-identical) and is self-contained (stdlib only) so it
runs inside those images. We load the canonical (Hermes) copy here by file path
and unit-test its pure functions plus the orchestration with a mocked HTTP
transport — NO real network / Jira calls. A separate test asserts the OpenClaw
copy is byte-identical so the two bots never drift.
"""

from __future__ import annotations

import base64
import importlib.util
import json
import pathlib

import pytest

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
_HERMES_SCRIPT = (
    _REPO_ROOT / "docker" / "config" / "hermes" / "workspace" / "jira_dev_ticket.py"
)
_OPENCLAW_SCRIPT = (
    _REPO_ROOT / "docker" / "config" / "openclaw" / "workspace" / "jira_dev_ticket.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location("jira_dev_ticket", _HERMES_SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


jdt = _load_module()


def test_openclaw_copy_is_byte_identical_to_hermes_copy():
    assert _HERMES_SCRIPT.read_bytes() == _OPENCLAW_SCRIPT.read_bytes()


# ---------------------------------------------------------------------------
# Basic auth header
# ---------------------------------------------------------------------------


def test_basic_auth_header_is_base64_email_colon_token():
    header = jdt.build_basic_auth_header("agentshroud.ai@gmail.com", "tok123")
    assert header.startswith("Basic ")
    decoded = base64.b64decode(header.split(" ", 1)[1]).decode()
    assert decoded == "agentshroud.ai@gmail.com:tok123"


def test_basic_auth_header_rejects_empty():
    with pytest.raises(ValueError):
        jdt.build_basic_auth_header("", "tok")
    with pytest.raises(ValueError):
        jdt.build_basic_auth_header("e@x.com", "")


# ---------------------------------------------------------------------------
# op-proxy request builder
# ---------------------------------------------------------------------------


def test_op_proxy_request_has_bearer_and_system_header():
    url, body, headers = jdt.build_op_proxy_request(jdt.OP_REF_TOKEN, "gw-tok")
    assert url.endswith("/credentials/op-proxy")
    assert json.loads(body.decode())["reference"] == jdt.OP_REF_TOKEN
    assert headers["Authorization"] == "Bearer gw-tok"
    assert headers["X-AgentShroud-System"] == "1"


def test_op_refs_target_the_atlassian_item():
    assert jdt.OP_REF_TOKEN.endswith("/AgentShroud -Atlassian API Token/token")
    assert jdt.OP_REF_EMAIL.endswith("/AgentShroud -Atlassian API Token/email")
    assert jdt.OP_REF_DOMAIN.endswith("/AgentShroud -Atlassian API Token/domain")


# ---------------------------------------------------------------------------
# URL builders
# ---------------------------------------------------------------------------


def test_issue_url_targets_rest_v3():
    assert jdt.build_issue_url("agentshroudai.atlassian.net") == (
        "https://agentshroudai.atlassian.net/rest/api/3/issue"
    )


def test_issue_url_accepts_full_https_domain():
    assert jdt.build_issue_url("https://agentshroudai.atlassian.net/") == (
        "https://agentshroudai.atlassian.net/rest/api/3/issue"
    )


def test_issue_url_rejects_empty_domain():
    with pytest.raises(ValueError):
        jdt.build_issue_url("")


def test_comment_url_targets_arbitrary_issue():
    assert jdt.build_comment_url("agentshroudai.atlassian.net", "SCRUM-123") == (
        "https://agentshroudai.atlassian.net/rest/api/3/issue/SCRUM-123/comment"
    )


def test_comment_url_rejects_empty_issue_key():
    with pytest.raises(ValueError):
        jdt.build_comment_url("agentshroudai.atlassian.net", "")


def test_transitions_url_targets_arbitrary_issue():
    assert jdt.build_transitions_url("agentshroudai.atlassian.net", "SCRUM-123") == (
        "https://agentshroudai.atlassian.net/rest/api/3/issue/SCRUM-123/transitions"
    )


def test_transitions_url_rejects_empty_issue_key():
    with pytest.raises(ValueError):
        jdt.build_transitions_url("agentshroudai.atlassian.net", "")


# ---------------------------------------------------------------------------
# Payload builders
# ---------------------------------------------------------------------------


def test_comment_payload_is_valid_adf_doc():
    payload = jdt.build_comment_payload("line one\nline two")
    body = payload["body"]
    assert body["type"] == "doc"
    assert body["version"] == 1
    assert len(body["content"]) == 2
    assert body["content"][0]["content"][0]["text"] == "line one"


def test_comment_payload_never_empty():
    payload = jdt.build_comment_payload("   \n  \n")
    assert len(payload["body"]["content"]) == 1


def test_create_issue_payload_minimal():
    payload = jdt.build_create_issue_payload("SCRUM", "Do the thing")
    fields = payload["fields"]
    assert fields["project"] == {"key": "SCRUM"}
    assert fields["summary"] == "Do the thing"
    assert fields["issuetype"] == {"name": "Task"}
    assert "description" not in fields
    assert "labels" not in fields
    assert "parent" not in fields


def test_create_issue_payload_full():
    payload = jdt.build_create_issue_payload(
        "SCRUM",
        "Do the thing",
        description="Because reasons",
        issue_type="Story",
        parent_key="SCRUM-65",
        labels=["hermes", "automation"],
    )
    fields = payload["fields"]
    assert fields["issuetype"] == {"name": "Story"}
    assert (
        fields["description"]["content"][0]["content"][0]["text"] == "Because reasons"
    )
    assert fields["labels"] == ["hermes", "automation"]
    assert fields["parent"] == {"key": "SCRUM-65"}


def test_create_issue_payload_rejects_missing_project():
    with pytest.raises(ValueError):
        jdt.build_create_issue_payload("", "summary")


def test_create_issue_payload_rejects_missing_summary():
    with pytest.raises(ValueError):
        jdt.build_create_issue_payload("SCRUM", "")


# ---------------------------------------------------------------------------
# Transition matching
# ---------------------------------------------------------------------------


def test_find_transition_id_matches_transition_name():
    transitions = [
        {"id": "11", "name": "Start Progress", "to": {"name": "In Progress"}},
        {"id": "21", "name": "Done", "to": {"name": "Done"}},
    ]
    assert jdt.find_transition_id(transitions, "Start Progress") == "11"


def test_find_transition_id_matches_destination_status_name():
    transitions = [
        {"id": "11", "name": "Start Progress", "to": {"name": "In Progress"}},
        {"id": "21", "name": "Done", "to": {"name": "Done"}},
    ]
    assert jdt.find_transition_id(transitions, "in progress") == "11"


def test_find_transition_id_returns_none_when_no_match():
    transitions = [
        {"id": "11", "name": "Start Progress", "to": {"name": "In Progress"}}
    ]
    assert jdt.find_transition_id(transitions, "Blocked") is None


# ---------------------------------------------------------------------------
# Orchestration with mocked HTTP transport (no real network)
# ---------------------------------------------------------------------------


class _MockTransport:
    """Records requests; serves op-proxy secrets then a scripted Jira response."""

    def __init__(self, jira_status=201, jira_body=None):
        self.calls = []
        self._secrets = {
            jdt.OP_REF_TOKEN: "atl-token-xyz",
            jdt.OP_REF_EMAIL: "agentshroud.ai@gmail.com",
            jdt.OP_REF_DOMAIN: "agentshroudai.atlassian.net",
        }
        self._jira_status = jira_status
        self._jira_body = (
            jira_body if jira_body is not None else json.dumps({"key": "SCRUM-999"})
        )

    def __call__(self, url, body, headers, method="GET", timeout=30):
        self.calls.append((url, body, headers, method))
        if url.endswith("/credentials/op-proxy"):
            ref = json.loads(body.decode())["reference"]
            return 200, json.dumps({"value": self._secrets[ref]})
        return self._jira_status, self._jira_body


def test_run_create_posts_issue_with_basic_auth(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")
    transport = _MockTransport(
        jira_status=201, jira_body=json.dumps({"key": "SCRUM-124"})
    )
    rc = jdt.run(
        ["create", "--project", "SCRUM", "--summary", "Do the thing"],
        request_fn=transport,
    )
    assert rc == 0

    url, body, headers, method = transport.calls[-1]
    assert url == "https://agentshroudai.atlassian.net/rest/api/3/issue"
    assert method == "POST"
    expected_auth = (
        "Basic " + base64.b64encode(b"agentshroud.ai@gmail.com:atl-token-xyz").decode()
    )
    assert headers["Authorization"] == expected_auth
    payload = json.loads(body.decode())
    assert payload["fields"]["summary"] == "Do the thing"


def test_run_comment_posts_to_correct_issue(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")
    transport = _MockTransport(jira_status=201, jira_body=json.dumps({"id": "10001"}))
    rc = jdt.run(
        ["comment", "--issue", "SCRUM-356", "--body", "batch update"],
        request_fn=transport,
    )
    assert rc == 0

    url, body, headers, method = transport.calls[-1]
    assert (
        url == "https://agentshroudai.atlassian.net/rest/api/3/issue/SCRUM-356/comment"
    )
    assert method == "POST"
    payload = json.loads(body.decode())
    assert payload["body"]["content"][0]["content"][0]["text"] == "batch update"


def test_run_transition_applies_matching_transition(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")

    def transport(url, body, headers, method="GET", timeout=30):
        if url.endswith("/credentials/op-proxy"):
            ref = json.loads(body.decode())["reference"]
            values = {
                jdt.OP_REF_TOKEN: "t",
                jdt.OP_REF_EMAIL: "e@x.com",
                jdt.OP_REF_DOMAIN: "agentshroudai.atlassian.net",
            }
            return 200, json.dumps({"value": values[ref]})
        if method == "GET":
            return 200, json.dumps(
                {"transitions": [{"id": "31", "name": "Done", "to": {"name": "Done"}}]}
            )
        assert json.loads(body.decode()) == {"transition": {"id": "31"}}
        return 204, ""

    rc = jdt.run(
        ["transition", "--issue", "SCRUM-356", "--status", "Done"], request_fn=transport
    )
    assert rc == 0


def test_run_transition_fails_when_no_matching_transition(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")

    def transport(url, body, headers, method="GET", timeout=30):
        if url.endswith("/credentials/op-proxy"):
            ref = json.loads(body.decode())["reference"]
            values = {
                jdt.OP_REF_TOKEN: "t",
                jdt.OP_REF_EMAIL: "e@x.com",
                jdt.OP_REF_DOMAIN: "agentshroudai.atlassian.net",
            }
            return 200, json.dumps({"value": values[ref]})
        return 200, json.dumps(
            {"transitions": [{"id": "31", "name": "Done", "to": {"name": "Done"}}]}
        )

    rc = jdt.run(
        ["transition", "--issue", "SCRUM-356", "--status", "Blocked"],
        request_fn=transport,
    )
    assert rc == 1


def test_run_aborts_without_gateway_token(monkeypatch):
    monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)
    rc = jdt.run(
        ["create", "--project", "SCRUM", "--summary", "x"],
        request_fn=lambda *a, **k: (200, "{}"),
    )
    assert rc == 1


def test_run_returns_1_on_jira_rejection(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")
    transport = _MockTransport(
        jira_status=401, jira_body=json.dumps({"errorMessages": ["auth failed"]})
    )
    rc = jdt.run(
        ["create", "--project", "SCRUM", "--summary", "x"], request_fn=transport
    )
    assert rc == 1


def test_run_returns_1_when_op_proxy_denies(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")

    def transport(url, body, headers, method="GET", timeout=30):
        return 403, json.dumps({"detail": "not allowed"})

    rc = jdt.run(
        ["create", "--project", "SCRUM", "--summary", "x"], request_fn=transport
    )
    assert rc == 1


def test_run_create_with_labels_and_parent(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")
    transport = _MockTransport(
        jira_status=201, jira_body=json.dumps({"key": "SCRUM-125"})
    )
    rc = jdt.run(
        [
            "create",
            "--project",
            "SCRUM",
            "--summary",
            "Batch work",
            "--description",
            "details here",
            "--issue-type",
            "Story",
            "--parent",
            "SCRUM-65",
            "--labels",
            "hermes,automation",
        ],
        request_fn=transport,
    )
    assert rc == 0
    _, body, _, _ = transport.calls[-1]
    payload = json.loads(body.decode())
    assert payload["fields"]["labels"] == ["hermes", "automation"]
    assert payload["fields"]["parent"] == {"key": "SCRUM-65"}
    assert payload["fields"]["issuetype"] == {"name": "Story"}
