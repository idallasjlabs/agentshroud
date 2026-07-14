# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for MFAGuard — second factor for high-risk owner operations.

SCRUM-93 — IEC 62443 FR1 (Identification & Authentication Control).

Covers:
  * MFA disabled (default) leaves behavior unchanged (fail-open by policy: no factor required).
  * Valid TOTP code allows a high-risk op.
  * Missing / invalid / expired-window / replayed code denies (fail-closed).
  * Constant-time verification path is used (monkeypatched to prove it is invoked).
  * High-risk classification gate (only high-risk ops require a factor).
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import struct
import time

import pytest

from gateway.security.mfa_guard import MFAGuard, MFAResult

# ---------------------------------------------------------------------------
# Deterministic reference TOTP generator (RFC 6238) for test vectors.
# ---------------------------------------------------------------------------
_SECRET_B32 = "JBSWY3DPEHPK3PXP"  # RFC 4648 base32, arbitrary test secret


def _ref_totp(secret_b32: str, at: int, step: int = 30, digits: int = 6) -> str:
    key = base64.b32decode(secret_b32.upper() + "=" * ((8 - len(secret_b32) % 8) % 8))
    counter = int(at // step)
    msg = struct.pack(">Q", counter)
    digest = hmac.new(key, msg, hashlib.sha1).digest()
    offset = digest[-1] & 0x0F
    binary = struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF
    return str(binary % (10**digits)).zfill(digits)


@pytest.fixture()
def now() -> int:
    return 1_700_000_000  # fixed, deterministic — no real clock/sleep


# ---------------------------------------------------------------------------
# Disabled (default) — behavior unchanged
# ---------------------------------------------------------------------------


def test_disabled_by_default_allows_without_factor():
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=False)
    res = guard.verify(action_type="email_sending", code=None, now=1_700_000_000)
    assert isinstance(res, MFAResult)
    assert res.allowed is True
    assert res.required is False


def test_disabled_allows_even_high_risk_with_no_code():
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=False)
    res = guard.verify(action_type="file_deletion", code=None, now=1_700_000_000)
    assert res.allowed is True


# ---------------------------------------------------------------------------
# Enabled — valid factor allows a high-risk op
# ---------------------------------------------------------------------------


def test_valid_totp_allows_high_risk(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    code = _ref_totp(_SECRET_B32, now)
    res = guard.verify(action_type="email_sending", code=code, now=now)
    assert res.required is True
    assert res.allowed is True


def test_valid_totp_prev_window_allowed(now):
    # Code from the previous 30s window must still validate (clock skew tolerance).
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True, window=1)
    code = _ref_totp(_SECRET_B32, now - 30)
    res = guard.verify(action_type="skill_installation", code=code, now=now)
    assert res.allowed is True


# ---------------------------------------------------------------------------
# Enabled — missing / invalid / expired / replay deny (fail-closed)
# ---------------------------------------------------------------------------


def test_missing_code_denies_high_risk(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    res = guard.verify(action_type="email_sending", code=None, now=now)
    assert res.required is True
    assert res.allowed is False
    assert "missing" in res.reason.lower()


def test_empty_code_denies(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    res = guard.verify(action_type="file_deletion", code="   ", now=now)
    assert res.allowed is False


def test_invalid_code_denies(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    res = guard.verify(action_type="external_api_calls", code="000000", now=now)
    # 000000 is astronomically unlikely to be the real code for this vector.
    assert res.allowed is False
    assert "invalid" in res.reason.lower()


def test_wrong_length_code_denies(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    res = guard.verify(action_type="email_sending", code="12345", now=now)
    assert res.allowed is False


def test_expired_window_code_denies(now):
    # Code from 5 windows ago (150s) is outside the ±1 window tolerance.
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True, window=1)
    old = _ref_totp(_SECRET_B32, now - 150)
    res = guard.verify(action_type="email_sending", code=old, now=now)
    assert res.allowed is False


def test_replayed_code_denies(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    code = _ref_totp(_SECRET_B32, now)
    first = guard.verify(action_type="email_sending", code=code, now=now)
    assert first.allowed is True
    # Same code, same guard — replay must be rejected.
    second = guard.verify(action_type="email_sending", code=code, now=now + 1)
    assert second.allowed is False
    assert "replay" in second.reason.lower()


# ---------------------------------------------------------------------------
# High-risk classification gate
# ---------------------------------------------------------------------------


def test_non_high_risk_action_not_required(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    res = guard.verify(action_type="status_read", code=None, now=now)
    assert res.required is False
    assert res.allowed is True


def test_custom_high_risk_action_types(now):
    guard = MFAGuard(
        secret_b32=_SECRET_B32,
        enabled=True,
        high_risk_actions={"custom_destruct"},
    )
    # Not in the custom set -> not required.
    assert guard.verify(action_type="email_sending", code=None, now=now).required is False
    # In the custom set -> required and denied without code.
    r = guard.verify(action_type="custom_destruct", code=None, now=now)
    assert r.required is True
    assert r.allowed is False


# ---------------------------------------------------------------------------
# Constant-time verification is used
# ---------------------------------------------------------------------------


def test_uses_constant_time_compare(monkeypatch, now):
    calls = {"n": 0}
    real = hmac.compare_digest

    def spy(a, b):
        calls["n"] += 1
        return real(a, b)

    monkeypatch.setattr("gateway.security.mfa_guard.hmac.compare_digest", spy)
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    code = _ref_totp(_SECRET_B32, now)
    guard.verify(action_type="email_sending", code=code, now=now)
    assert calls["n"] >= 1


# ---------------------------------------------------------------------------
# Secret loading & construction
# ---------------------------------------------------------------------------


def test_enabled_without_secret_denies_fail_closed(now):
    # Enabled but no secret configured -> cannot verify anything -> deny high-risk.
    guard = MFAGuard(secret_b32="", enabled=True)
    res = guard.verify(action_type="email_sending", code="123456", now=now)
    assert res.allowed is False
    assert "not configured" in res.reason.lower()


def test_from_env_disabled_when_flag_unset(monkeypatch):
    monkeypatch.delenv("AGENTSHROUD_MFA_ENABLED", raising=False)
    monkeypatch.delenv("AGENTSHROUD_MFA_SECRET", raising=False)
    guard = MFAGuard.from_env()
    assert guard.enabled is False
    assert guard.verify(action_type="email_sending", code=None, now=1_700_000_000).allowed is True


def test_from_env_reads_secret_and_flag(monkeypatch, tmp_path, now):
    monkeypatch.setenv("AGENTSHROUD_MFA_ENABLED", "true")
    monkeypatch.setenv("AGENTSHROUD_MFA_SECRET", _SECRET_B32)
    monkeypatch.delenv("AGENTSHROUD_MFA_SECRET_FILE", raising=False)
    guard = MFAGuard.from_env()
    assert guard.enabled is True
    code = _ref_totp(_SECRET_B32, now)
    assert guard.verify(action_type="email_sending", code=code, now=now).allowed is True


def test_from_env_reads_secret_file(monkeypatch, tmp_path, now):
    secret_file = tmp_path / "mfa_secret"
    secret_file.write_text(_SECRET_B32 + "\n")
    monkeypatch.setenv("AGENTSHROUD_MFA_ENABLED", "1")
    monkeypatch.delenv("AGENTSHROUD_MFA_SECRET", raising=False)
    monkeypatch.setenv("AGENTSHROUD_MFA_SECRET_FILE", str(secret_file))
    guard = MFAGuard.from_env()
    assert guard.enabled is True
    code = _ref_totp(_SECRET_B32, now)
    assert guard.verify(action_type="email_sending", code=code, now=now).allowed is True


def test_invalid_base32_secret_treated_as_unconfigured(now):
    guard = MFAGuard(secret_b32="not!valid!base32!", enabled=True)
    res = guard.verify(action_type="email_sending", code="123456", now=now)
    assert res.allowed is False
    assert "not configured" in res.reason.lower()


def test_counter_below_zero_skipped():
    # now near unix epoch with a window forces expected_counter < 0 branch.
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True, window=2)
    res = guard.verify(action_type="email_sending", code="000000", now=0)
    assert res.allowed is False


def test_prune_used_drops_stale_entries(now):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True, window=0)
    old_code = _ref_totp(_SECRET_B32, now)
    assert guard.verify(action_type="email_sending", code=old_code, now=now).allowed is True
    # A verification far in the future must prune the stale replay record.
    future = now + 10_000
    future_code = _ref_totp(_SECRET_B32, future)
    assert guard.verify(action_type="email_sending", code=future_code, now=future).allowed is True
    # Internal replay set should not retain the ancient entry.
    assert all(counter >= (future // 30) - 1 for counter, _ in guard._used)


def test_from_env_enabled_no_secret_warns(monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_MFA_ENABLED", "true")
    monkeypatch.delenv("AGENTSHROUD_MFA_SECRET", raising=False)
    monkeypatch.delenv("AGENTSHROUD_MFA_SECRET_FILE", raising=False)
    guard = MFAGuard.from_env()
    assert guard.enabled is True
    # Fail-closed: no secret -> high-risk denied.
    assert guard.verify(action_type="email_sending", code="123456").allowed is False


def test_from_env_bad_window_defaults_to_one(monkeypatch):
    monkeypatch.setenv("AGENTSHROUD_MFA_ENABLED", "true")
    monkeypatch.setenv("AGENTSHROUD_MFA_SECRET", _SECRET_B32)
    monkeypatch.setenv("AGENTSHROUD_MFA_WINDOW", "not-an-int")
    guard = MFAGuard.from_env()
    assert guard._window == 1


def test_from_env_unreadable_secret_file(monkeypatch, tmp_path):
    missing = tmp_path / "does_not_exist"
    monkeypatch.setenv("AGENTSHROUD_MFA_ENABLED", "true")
    monkeypatch.setenv("AGENTSHROUD_MFA_SECRET", _SECRET_B32)
    monkeypatch.setenv("AGENTSHROUD_MFA_SECRET_FILE", str(missing))
    guard = MFAGuard.from_env()
    # Falls back to inline secret when file is unreadable.
    code = _ref_totp(_SECRET_B32, int(time.time()))
    assert guard.verify(action_type="email_sending", code=code).allowed is True


def test_real_time_default_now(monkeypatch):
    # When now is omitted, real time is used — verify it does not crash and
    # that a freshly generated code validates.
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    at = int(time.time())
    code = _ref_totp(_SECRET_B32, at)
    res = guard.verify(action_type="email_sending", code=code)
    assert res.allowed is True


# ===========================================================================
# Integration: MFAGuard wired into ApprovalQueue.decide (the chokepoint)
# ===========================================================================

from gateway.approval_queue.queue import ApprovalQueue  # noqa: E402
from gateway.ingest_api.config import ApprovalQueueConfig  # noqa: E402
from gateway.ingest_api.models import ApprovalRequest  # noqa: E402


def _queue(mfa_enabled: bool) -> ApprovalQueue:
    config = ApprovalQueueConfig(enabled=True, actions=["email_sending"], timeout_seconds=300)
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=mfa_enabled)
    return ApprovalQueue(config, mfa_guard=guard)


async def _submit_high_risk(q: ApprovalQueue) -> str:
    item = await q.submit(
        ApprovalRequest(
            action_type="email_sending",
            description="Send email to owner",
            details={"to": "x@example.com"},
            agent_id="agent-1",
        )
    )
    return item.request_id


@pytest.mark.asyncio
async def test_decide_mfa_disabled_approves_without_code():
    q = _queue(mfa_enabled=False)
    rid = await _submit_high_risk(q)
    item = await q.decide(rid, approved=True)
    assert item.status == "approved"


@pytest.mark.asyncio
async def test_decide_mfa_enabled_valid_code_approves():
    q = _queue(mfa_enabled=True)
    rid = await _submit_high_risk(q)
    code = _ref_totp(_SECRET_B32, int(time.time()))
    item = await q.decide(rid, approved=True, mfa_code=code)
    assert item.status == "approved"


@pytest.mark.asyncio
async def test_decide_mfa_enabled_missing_code_denied():
    q = _queue(mfa_enabled=True)
    rid = await _submit_high_risk(q)
    with pytest.raises(PermissionError):
        await q.decide(rid, approved=True)
    # Fail-closed: item must remain pending, not approved.
    still = await q.get_item(rid)
    assert still.status == "pending"


@pytest.mark.asyncio
async def test_decide_mfa_enabled_invalid_code_denied():
    q = _queue(mfa_enabled=True)
    rid = await _submit_high_risk(q)
    with pytest.raises(PermissionError):
        await q.decide(rid, approved=True, mfa_code="000000")
    still = await q.get_item(rid)
    assert still.status == "pending"


@pytest.mark.asyncio
async def test_decide_mfa_enabled_replayed_code_denied():
    q = _queue(mfa_enabled=True)
    rid1 = await _submit_high_risk(q)
    code = _ref_totp(_SECRET_B32, int(time.time()))
    item = await q.decide(rid1, approved=True, mfa_code=code)
    assert item.status == "approved"
    # Reuse same code on a second high-risk approval -> replay denied.
    rid2 = await _submit_high_risk(q)
    with pytest.raises(PermissionError):
        await q.decide(rid2, approved=True, mfa_code=code)


@pytest.mark.asyncio
async def test_decide_reject_never_requires_mfa():
    q = _queue(mfa_enabled=True)
    rid = await _submit_high_risk(q)
    # Rejecting a high-risk action must always work without a second factor.
    item = await q.decide(rid, approved=False, reason="not now")
    assert item.status == "rejected"


# ===========================================================================
# Integration: MFAGuard wired into EnhancedApprovalQueue.decide (production path)
# ===========================================================================

import tempfile  # noqa: E402

import pytest_asyncio  # noqa: E402

from gateway.approval_queue.enhanced_queue import EnhancedApprovalQueue  # noqa: E402
from gateway.approval_queue.store import ApprovalStore  # noqa: E402
from gateway.ingest_api.config import ToolRiskConfig  # noqa: E402


@pytest_asyncio.fixture
async def enhanced_mfa_queue():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as fh:
        store = ApprovalStore(fh.name)
    await store.initialize()
    q = EnhancedApprovalQueue(
        config=ApprovalQueueConfig(enabled=True, timeout_seconds=300),
        tool_risk_config=ToolRiskConfig(enforce_mode=True),
        store=store,
        mfa_guard=MFAGuard(secret_b32=_SECRET_B32, enabled=True),
    )
    yield q
    await store.close()


async def _submit_enhanced_high_risk(q: EnhancedApprovalQueue) -> str:
    item = await q.submit(
        ApprovalRequest(
            action_type="email_sending",
            description="Send email",
            details={"to": "x@example.com"},
            agent_id="agent-1",
        )
    )
    return item.request_id


@pytest.mark.asyncio
async def test_enhanced_decide_valid_code_approves(enhanced_mfa_queue):
    rid = await _submit_enhanced_high_risk(enhanced_mfa_queue)
    code = _ref_totp(_SECRET_B32, int(time.time()))
    item = await enhanced_mfa_queue.decide(rid, approved=True, mfa_code=code)
    assert item.status == "approved"


@pytest.mark.asyncio
async def test_enhanced_decide_missing_code_denied(enhanced_mfa_queue):
    rid = await _submit_enhanced_high_risk(enhanced_mfa_queue)
    with pytest.raises(PermissionError):
        await enhanced_mfa_queue.decide(rid, approved=True)
    still = await enhanced_mfa_queue.get_item(rid)
    assert still.status == "pending"


@pytest.mark.asyncio
async def test_enhanced_decide_reject_no_mfa(enhanced_mfa_queue):
    rid = await _submit_enhanced_high_risk(enhanced_mfa_queue)
    item = await enhanced_mfa_queue.decide(rid, approved=False, reason="no")
    assert item.status == "rejected"


# ===========================================================================
# Regression: the PRODUCTION high-risk channel is `tool_call_<tier>`.
#
# EnhancedApprovalQueue.submit_tool_request(...) enqueues MCP tool-call
# approvals with action_type=f"tool_call_{tier}" (enhanced_queue.py:176,196,
# driven by mcp_policy.py). Prior to the SCRUM-93 fix, MFAGuard.is_required()
# only matched the named DEFAULT_HIGH_RISK_ACTIONS set, so `tool_call_high` /
# `tool_call_critical` returned False and a destructive MCP tool call was
# APPROVED with NO second factor even when MFA was enabled (HIGH fail-open).
# These tests FAIL on the pre-fix code and PASS after.
# ===========================================================================


async def _submit_tool_call(q: EnhancedApprovalQueue, tier: str) -> str:
    """Submit via the real tool-call path -> action_type == f'tool_call_{tier}'."""
    request_id, requires_wait = await q.submit_tool_request(
        tool_name="exec",
        parameters={"cmd": "rm -rf /"},
        agent_id="agent-1",
        force_tier=tier,
    )
    assert requires_wait is True
    return request_id


@pytest.mark.asyncio
async def test_enhanced_tool_call_high_blocked_without_mfa(enhanced_mfa_queue):
    # HIGH fail-open regression: a high-tier MCP tool call must be BLOCKED
    # without a valid second factor when MFA is enabled.
    rid = await _submit_tool_call(enhanced_mfa_queue, "high")
    item = await enhanced_mfa_queue.get_item(rid)
    assert item.action_type == "tool_call_high"
    with pytest.raises(PermissionError):
        await enhanced_mfa_queue.decide(rid, approved=True)
    still = await enhanced_mfa_queue.get_item(rid)
    assert still.status == "pending"


@pytest.mark.asyncio
async def test_enhanced_tool_call_high_allowed_with_mfa(enhanced_mfa_queue):
    rid = await _submit_tool_call(enhanced_mfa_queue, "high")
    code = _ref_totp(_SECRET_B32, int(time.time()))
    item = await enhanced_mfa_queue.decide(rid, approved=True, mfa_code=code)
    assert item.status == "approved"


@pytest.mark.asyncio
async def test_enhanced_tool_call_critical_blocked_without_mfa(enhanced_mfa_queue):
    rid = await _submit_tool_call(enhanced_mfa_queue, "critical")
    item = await enhanced_mfa_queue.get_item(rid)
    assert item.action_type == "tool_call_critical"
    with pytest.raises(PermissionError):
        await enhanced_mfa_queue.decide(rid, approved=True, mfa_code="000000")
    still = await enhanced_mfa_queue.get_item(rid)
    assert still.status == "pending"


@pytest.mark.asyncio
async def test_enhanced_tool_call_critical_allowed_with_mfa(enhanced_mfa_queue):
    rid = await _submit_tool_call(enhanced_mfa_queue, "critical")
    code = _ref_totp(_SECRET_B32, int(time.time()))
    item = await enhanced_mfa_queue.decide(rid, approved=True, mfa_code=code)
    assert item.status == "approved"


@pytest.mark.asyncio
async def test_enhanced_tool_call_medium_not_gated(enhanced_mfa_queue):
    # Only high/critical tiers are second-factor gated. A medium-tier tool-call
    # action_type must NOT require a code (boundary check). Submitted directly
    # because the medium tier policy does not itself require approval.
    item = await enhanced_mfa_queue.submit(
        ApprovalRequest(
            action_type="tool_call_medium",
            description="Execute medium-tier tool: grep",
            details={"tool_name": "grep", "risk_tier": "medium"},
            agent_id="agent-1",
        )
    )
    decided = await enhanced_mfa_queue.decide(item.request_id, approved=True)
    assert decided.status == "approved"


@pytest.mark.asyncio
async def test_enhanced_decide_missing_item_fail_closed(enhanced_mfa_queue, monkeypatch):
    # LOW edge: if the item is missing on an approved+MFA-enabled decision, the
    # gate must FAIL CLOSED (raise PermissionError), never degrade to action_type
    # "" and skip MFA. Simulate a store race where get_item returns None but the
    # pending future still exists.
    rid = await _submit_tool_call(enhanced_mfa_queue, "high")

    async def _none(_request_id):
        return None

    monkeypatch.setattr(enhanced_mfa_queue, "get_item", _none)
    with pytest.raises(PermissionError):
        await enhanced_mfa_queue.decide(rid, approved=True, mfa_code="000000")


# ---------------------------------------------------------------------------
# Unit: is_required() tier parsing
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "action_type,expected",
    [
        ("tool_call_high", True),
        ("tool_call_critical", True),
        ("TOOL_CALL_HIGH", True),
        ("  tool_call_critical  ", True),
        ("tool_call_medium", False),
        ("tool_call_low", False),
        ("tool_call_", False),
        ("tool_call_unknown", False),
        ("email_sending", True),
        ("status_read", False),
    ],
)
def test_is_required_tool_call_tier_parsing(action_type, expected):
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=True)
    assert guard.is_required(action_type) is expected


def test_is_required_tool_call_disabled_never_required():
    guard = MFAGuard(secret_b32=_SECRET_B32, enabled=False)
    assert guard.is_required("tool_call_critical") is False
