# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the SCRUM-81 Hermes weekly Jira review script.

The script lives in the Hermes image workspace
(docker/config/hermes/workspace/jira_weekly_review.py) and is self-contained
(stdlib only) so it runs inside that image. We load it here by file path and
unit-test its pure functions plus the orchestration with a mocked HTTP transport
— NO real network / Jira calls.
"""

from __future__ import annotations

import base64
import importlib.util
import json
import pathlib
from datetime import datetime, timedelta, timezone

import pytest

_SCRIPT_PATH = (
    pathlib.Path(__file__).resolve().parents[2]
    / "docker"
    / "config"
    / "hermes"
    / "workspace"
    / "jira_weekly_review.py"
)


def _load_module():
    spec = importlib.util.spec_from_file_location("jira_weekly_review", _SCRIPT_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


jwr = _load_module()


# ---------------------------------------------------------------------------
# Basic auth header
# ---------------------------------------------------------------------------


def test_basic_auth_header_is_base64_email_colon_token():
    header = jwr.build_basic_auth_header("agentshroud.ai@gmail.com", "tok123")
    assert header.startswith("Basic ")
    decoded = base64.b64decode(header.split(" ", 1)[1]).decode()
    assert decoded == "agentshroud.ai@gmail.com:tok123"


def test_basic_auth_header_rejects_empty():
    with pytest.raises(ValueError):
        jwr.build_basic_auth_header("", "tok")
    with pytest.raises(ValueError):
        jwr.build_basic_auth_header("e@x.com", "")


# ---------------------------------------------------------------------------
# op-proxy request builder
# ---------------------------------------------------------------------------


def test_op_proxy_request_has_bearer_and_system_header():
    url, body, headers = jwr.build_op_proxy_request(jwr.OP_REF_TOKEN, "gw-tok")
    assert url.endswith("/credentials/op-proxy")
    assert json.loads(body.decode())["reference"] == jwr.OP_REF_TOKEN
    assert headers["Authorization"] == "Bearer gw-tok"
    assert headers["X-AgentShroud-System"] == "1"


def test_op_refs_target_the_atlassian_item():
    assert jwr.OP_REF_TOKEN.endswith("/AgentShroud -Atlassian API Token/token")
    assert jwr.OP_REF_EMAIL.endswith("/AgentShroud -Atlassian API Token/email")
    assert jwr.OP_REF_DOMAIN.endswith("/AgentShroud -Atlassian API Token/domain")


# ---------------------------------------------------------------------------
# Comment URL + ADF payload
# ---------------------------------------------------------------------------

_CLOUD_ID = "7a044ff7-e2cf-40e6-b6f0-e3e080898fbb"


def test_comment_url_targets_scrum_81_rest_v3():
    url = jwr.build_comment_url(_CLOUD_ID)
    assert url == f"https://api.atlassian.com/ex/jira/{_CLOUD_ID}/rest/api/3/issue/SCRUM-81/comment"


def test_comment_url_rejects_empty_cloud_id():
    with pytest.raises(ValueError):
        jwr.build_comment_url("")


def test_tenant_info_url_targets_edge_endpoint():
    assert jwr.build_tenant_info_url("agentshroudai.atlassian.net") == (
        "https://agentshroudai.atlassian.net/_edge/tenant_info"
    )


def test_tenant_info_url_accepts_full_https_domain():
    assert jwr.build_tenant_info_url("https://agentshroudai.atlassian.net/") == (
        "https://agentshroudai.atlassian.net/_edge/tenant_info"
    )


def test_tenant_info_url_rejects_empty_domain():
    with pytest.raises(ValueError):
        jwr.build_tenant_info_url("")


def test_resolve_cloud_id_parses_response():
    def get_fn(url, headers, timeout=30):
        assert url == "https://agentshroudai.atlassian.net/_edge/tenant_info"
        return 200, json.dumps({"cloudId": _CLOUD_ID})

    assert jwr.resolve_cloud_id("agentshroudai.atlassian.net", get_fn=get_fn) == _CLOUD_ID


def test_resolve_cloud_id_raises_on_non_200():
    def get_fn(url, headers, timeout=30):
        return 500, "server error"

    with pytest.raises(RuntimeError):
        jwr.resolve_cloud_id("agentshroudai.atlassian.net", get_fn=get_fn)


def test_resolve_cloud_id_raises_when_field_missing():
    def get_fn(url, headers, timeout=30):
        return 200, json.dumps({})

    with pytest.raises(RuntimeError):
        jwr.resolve_cloud_id("agentshroudai.atlassian.net", get_fn=get_fn)


def test_comment_payload_is_valid_adf_doc():
    payload = jwr.build_comment_payload("line one\nline two")
    body = payload["body"]
    assert body["type"] == "doc"
    assert body["version"] == 1
    assert len(body["content"]) == 2
    assert body["content"][0]["content"][0]["text"] == "line one"


def test_comment_payload_never_empty():
    payload = jwr.build_comment_payload("   \n  \n")
    assert len(payload["body"]["content"]) == 1


# ---------------------------------------------------------------------------
# Summary builder + SCRUM extraction
# ---------------------------------------------------------------------------


def test_extract_scrum_items_from_commits():
    commits = ["abc123 fix(SCRUM-81): wire cron", "def456 chore: bump", "aaa SCRUM-54 done"]
    assert sorted(jwr.extract_scrum_items(commits)) == ["SCRUM-54", "SCRUM-81"]


def test_summary_with_commits_flags_active():
    now = datetime(2026, 7, 12, tzinfo=timezone.utc)
    commits = ["abc123 fix(SCRUM-81): wire cron"]
    summary = jwr.build_weekly_summary(commits, ["SCRUM-81"], now=now, last_activity=now)
    assert "Shipped this week (1 commits)" in summary
    assert "SCRUM items advanced: SCRUM-81" in summary
    assert "Staleness flag: OK" in summary


def test_summary_with_no_commits_flags_stale():
    now = datetime(2026, 7, 12, tzinfo=timezone.utc)
    summary = jwr.build_weekly_summary([], [], now=now)
    assert "no commits in the last 7 days" in summary
    assert "Staleness flag: STALE" in summary


def test_summary_old_activity_flags_stale_even_with_commits():
    now = datetime(2026, 7, 12, tzinfo=timezone.utc)
    old = now - timedelta(days=30)
    summary = jwr.build_weekly_summary(["x done"], [], now=now, last_activity=old)
    assert "Staleness flag: STALE" in summary


# ---------------------------------------------------------------------------
# Orchestration with mocked HTTP transport (no real network)
# ---------------------------------------------------------------------------


class _MockTransport:
    """Records POSTs; returns op-proxy secrets then a 201 for the comment."""

    def __init__(self):
        self.calls = []
        self._secrets = {
            jwr.OP_REF_TOKEN: "atl-token-xyz",
            jwr.OP_REF_EMAIL: "agentshroud.ai@gmail.com",
            jwr.OP_REF_DOMAIN: "agentshroudai.atlassian.net",
        }

    def __call__(self, url, body, headers, timeout=30):
        self.calls.append((url, body, headers))
        if url.endswith("/credentials/op-proxy"):
            ref = json.loads(body.decode())["reference"]
            return 200, json.dumps({"value": self._secrets[ref]})
        # Jira comment endpoint
        return 201, json.dumps({"id": "10001"})


def _get_fn_stub(url, headers, timeout=30):
    return 200, json.dumps({"cloudId": _CLOUD_ID})


def test_run_posts_comment_with_basic_auth(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")
    transport = _MockTransport()
    rc = jwr.run(
        post_fn=transport,
        commits_fn=lambda: ["abc SCRUM-81 wire cron"],
        get_fn=_get_fn_stub,
    )
    assert rc == 0

    # Last call is the Jira comment POST — verify auth + URL + ADF body.
    url, body, headers = transport.calls[-1]
    assert url == f"https://api.atlassian.com/ex/jira/{_CLOUD_ID}/rest/api/3/issue/SCRUM-81/comment"
    expected = "Basic " + base64.b64encode(b"agentshroud.ai@gmail.com:atl-token-xyz").decode()
    assert headers["Authorization"] == expected
    payload = json.loads(body.decode())
    assert payload["body"]["type"] == "doc"
    assert any("SCRUM-81" in c["content"][0]["text"] for c in payload["body"]["content"])


def test_run_aborts_without_gateway_token(monkeypatch):
    monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)
    rc = jwr.run(post_fn=lambda *a, **k: (200, "{}"), commits_fn=lambda: [])
    assert rc == 1


def test_run_returns_1_on_jira_rejection(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")

    def transport(url, body, headers, timeout=30):
        if url.endswith("/credentials/op-proxy"):
            ref = json.loads(body.decode())["reference"]
            val = {
                jwr.OP_REF_TOKEN: "t",
                jwr.OP_REF_EMAIL: "e@x.com",
                jwr.OP_REF_DOMAIN: "agentshroudai.atlassian.net",
            }[ref]
            return 200, json.dumps({"value": val})
        return 401, json.dumps({"errorMessages": ["auth failed"]})

    rc = jwr.run(post_fn=transport, commits_fn=lambda: [], get_fn=_get_fn_stub)
    assert rc == 1


def test_run_returns_1_when_op_proxy_denies(monkeypatch):
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "gw-tok")

    def transport(url, body, headers, timeout=30):
        return 403, json.dumps({"detail": "not allowed"})

    rc = jwr.run(post_fn=transport, commits_fn=lambda: [])
    assert rc == 1
