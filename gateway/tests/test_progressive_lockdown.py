# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for progressive lockdown UX fixes.

Covers:
  1. ProgressiveLockdown unit tests — reset(), all_statuses(), block thresholds
  2. Collaborator notifications at each lockdown threshold (3, 5, 10 blocks)
  3. Suspended-drop notice with cooldown via _filter_inbound_updates
  4. /locked owner command returns formatted lockdown status
  5. /unlock owner command calls reset() and confirms success
"""

from __future__ import annotations

import asyncio
import json
import time
from dataclasses import dataclass, field
from typing import Any
from unittest.mock import patch

import pytest

from gateway.proxy.telegram_proxy import TelegramAPIProxy
from gateway.security.progressive_lockdown import (
    LockdownLevel,
    ProgressiveLockdown,
)

# ── Shared stubs ─────────────────────────────────────────────────────────────

OWNER_ID = "8096968754"
COLLAB_ID = "7614658040"
OWNER_CHAT = int(OWNER_ID)
COLLAB_CHAT = int(COLLAB_ID)


class FakeRBAC:
    def __init__(self, owner_id: str = OWNER_ID, collaborators: list | None = None):
        self.owner_user_id = owner_id
        self.collaborator_user_ids = collaborators or []

    def is_owner(self, user_id: str) -> bool:
        return str(user_id) == self.owner_user_id


@dataclass
class FakePipelineResult:
    original_message: str = ""
    sanitized_message: str = ""
    blocked: bool = False
    block_reason: str = ""
    prompt_score: float = 0.0
    prompt_patterns: list = field(default_factory=list)
    pii_redaction_count: int = 0
    queued_for_approval: bool = False
    approval_id: str = ""


class PassthroughPipeline:
    async def process_inbound(self, message: str, **kwargs) -> FakePipelineResult:
        return FakePipelineResult(
            original_message=message,
            sanitized_message=message,
        )


def _make_update(
    text: str,
    user_id: str = COLLAB_ID,
    chat_id: int | None = None,
    update_id: int = 1,
) -> dict:
    cid = chat_id if chat_id is not None else int(user_id)
    return {
        "update_id": update_id,
        "message": {
            "message_id": 1,
            "from": {"id": int(user_id), "is_bot": False, "first_name": "Test"},
            "chat": {"id": cid, "type": "private"},
            "date": 1700000000,
            "text": text,
        },
    }


def _wrap(*updates: dict) -> dict:
    return {"ok": True, "result": list(updates)}


def _make_proxy(owner_id: str = OWNER_ID, collab_ids: list | None = None) -> TelegramAPIProxy:
    """Return a TelegramAPIProxy wired with fake deps (no real HTTP)."""
    proxy = TelegramAPIProxy(pipeline=PassthroughPipeline())
    proxy._rbac = FakeRBAC(owner_id=owner_id, collaborators=collab_ids or [COLLAB_ID])
    proxy._bot_token = ""  # disable real Telegram HTTP calls
    return proxy


# ── Section 1: ProgressiveLockdown unit tests ────────────────────────────────


class TestProgressiveLockdownUnit:
    def test_reset_true_for_known_user(self):
        ld = ProgressiveLockdown()
        ld.record_block("u1", "test")
        assert ld.reset("u1") is True

    def test_reset_false_for_unknown_user(self):
        ld = ProgressiveLockdown()
        assert ld.reset("nobody") is False

    def test_reset_removes_suspended_state(self):
        ld = ProgressiveLockdown()
        for _ in range(10):
            ld.record_block("u1", "r")
        assert ld.is_suspended("u1")
        ld.reset("u1")
        assert not ld.is_suspended("u1")

    def test_all_statuses_empty_initially(self):
        ld = ProgressiveLockdown()
        assert ld.all_statuses() == []

    def test_all_statuses_tracks_all_users(self):
        ld = ProgressiveLockdown()
        ld.record_block("alice", "r1")
        ld.record_block("bob", "r2")
        ids = {s["user_id"] for s in ld.all_statuses()}
        assert ids == {"alice", "bob"}

    def test_all_statuses_excludes_reset_users(self):
        ld = ProgressiveLockdown()
        ld.record_block("alice", "r")
        ld.reset("alice")
        assert ld.all_statuses() == []

    def test_alert_level_at_3_blocks(self):
        ld = ProgressiveLockdown()
        for _ in range(2):
            ld.record_block("u1", "r")
        action = ld.record_block("u1", "r")  # 3rd
        assert action.level == LockdownLevel.ALERT
        assert action.notify_owner is True
        assert action.suspended is False

    def test_escalated_level_at_5_blocks(self):
        ld = ProgressiveLockdown()
        for _ in range(4):
            ld.record_block("u1", "r")
        action = ld.record_block("u1", "r")  # 5th
        assert action.level == LockdownLevel.ESCALATED
        assert action.notify_owner is True
        assert action.rate_limit_multiplier == 2.0
        assert action.suspended is False

    def test_suspended_level_at_10_blocks(self):
        ld = ProgressiveLockdown()
        for _ in range(9):
            ld.record_block("u1", "r")
        action = ld.record_block("u1", "r")  # 10th
        assert action.level == LockdownLevel.SUSPENDED
        assert action.notify_owner is True
        assert action.suspended is True
        assert ld.is_suspended("u1")

    def test_notify_owner_fires_once_per_level(self):
        ld = ProgressiveLockdown()
        for _ in range(2):
            ld.record_block("u1", "r")
        a3 = ld.record_block("u1", "r")  # 3rd: alert, first time
        a4 = ld.record_block("u1", "r")  # 4th: still alert, no re-notify
        assert a3.notify_owner is True
        assert a4.notify_owner is False

    def test_no_notify_below_alert_threshold(self):
        ld = ProgressiveLockdown()
        a1 = ld.record_block("u1", "r")
        a2 = ld.record_block("u1", "r")
        assert a1.level == LockdownLevel.NORMAL
        assert a2.level == LockdownLevel.NORMAL
        assert a1.notify_owner is False
        assert a2.notify_owner is False


# ── Section 2: Collaborator notifications via _quarantine_blocked_message ────


class TestCollabLockdownNotifications:
    """Verify _quarantine_blocked_message sends threshold warnings to the collaborator."""

    def _setup_proxy_with_capture(self):
        proxy = _make_proxy()
        sent: list[tuple[Any, str]] = []

        async def capture(chat_id, text, **kw):
            sent.append((chat_id, text))
            return True

        proxy._send_telegram_text = capture
        return proxy, sent

    async def test_no_collab_notice_below_alert(self):
        proxy, sent = self._setup_proxy_with_capture()
        # 2 blocks — below threshold
        for _ in range(2):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        collab_msgs = [t for _, t in sent if _ == COLLAB_CHAT]
        assert not any("security block" in m.lower() for m in collab_msgs)

    async def test_collab_notified_at_alert_threshold(self):
        proxy, sent = self._setup_proxy_with_capture()
        for _ in range(3):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        collab_msgs = [t for cid, t in sent if cid == COLLAB_CHAT]
        assert any("multiple security blocks" in m for m in collab_msgs)

    async def test_collab_notified_at_escalated_threshold(self):
        proxy, sent = self._setup_proxy_with_capture()
        for _ in range(5):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        collab_msgs = [t for cid, t in sent if cid == COLLAB_CHAT]
        assert any("approaching suspension" in m for m in collab_msgs)

    async def test_collab_notified_at_suspended_threshold(self):
        proxy, sent = self._setup_proxy_with_capture()
        for _ in range(10):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        collab_msgs = [t for cid, t in sent if cid == COLLAB_CHAT]
        assert any("suspended" in m.lower() for m in collab_msgs)

    async def test_collab_notified_only_once_per_level(self):
        """The 4th block stays at ALERT but must NOT fire a second notification."""
        proxy, sent = self._setup_proxy_with_capture()
        for _ in range(4):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        alert_msgs = [
            t for cid, t in sent if cid == COLLAB_CHAT and "multiple security blocks" in t
        ]
        assert len(alert_msgs) == 1

    async def test_owner_also_notified_on_threshold(self):
        """Owner should receive an escalation notice on the 3rd block."""
        proxy, sent = self._setup_proxy_with_capture()
        # owner_user_id is a string; _send_telegram_text receives it as str(owner_chat)
        for _ in range(3):
            proxy._quarantine_blocked_message(COLLAB_ID, COLLAB_CHAT, "bad text", "reason", "test")
        await asyncio.sleep(0)
        owner_msgs = [t for cid, t in sent if str(cid) == OWNER_ID]
        assert len(owner_msgs) >= 1
        assert any("Lockdown Alert" in m or "security blocks" in m.lower() for m in owner_msgs)


# ── Section 3: Suspended-drop notice with cooldown ───────────────────────────


class TestSuspendedDropNotice:
    """Verify suspended users get a drop notice (rate-limited to avoid spam)."""

    async def test_suspended_user_gets_drop_notice(self):
        proxy = _make_proxy()
        sent: list[tuple[Any, str]] = []

        async def capture(chat_id, text, **kw):
            sent.append((chat_id, text))
            return True

        proxy._send_telegram_text = capture
        # Suspend the collaborator first
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")

        response = _wrap(_make_update("anything", user_id=COLLAB_ID, chat_id=COLLAB_CHAT))
        await proxy._filter_inbound_updates(response)
        await asyncio.sleep(0)

        collab_msgs = [t for cid, t in sent if cid == COLLAB_CHAT]
        assert any("suspended" in m.lower() for m in collab_msgs)

    async def test_suspended_drop_notice_respects_cooldown(self):
        proxy = _make_proxy()
        sent: list[tuple[Any, str]] = []

        async def capture(chat_id, text, **kw):
            sent.append((chat_id, text))
            return True

        proxy._send_telegram_text = capture
        # Suspend the collaborator
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")
        # Set cooldown so next notice is blocked
        proxy._suspended_drop_notice_until[COLLAB_ID] = time.time() + 9999.0

        for _ in range(3):
            response = _wrap(
                _make_update("anything", user_id=COLLAB_ID, chat_id=COLLAB_CHAT, update_id=_)
            )
            await proxy._filter_inbound_updates(response)
        await asyncio.sleep(0)

        collab_msgs = [t for cid, t in sent if cid == COLLAB_CHAT and "suspended" in t.lower()]
        assert len(collab_msgs) == 0  # cooldown active — no notice sent

    async def test_owner_messages_pass_despite_collab_suspension(self):
        """Owner messages must never be blocked by the suspension logic."""
        proxy = _make_proxy()
        # Suspend the collaborator
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")

        response = _wrap(_make_update("hello owner", user_id=OWNER_ID, chat_id=OWNER_CHAT))
        result = await proxy._filter_inbound_updates(response)
        # Owner update should pass through (not dropped)
        forwarded = [u for u in result.get("result", []) if u.get("message")]
        assert len(forwarded) == 1


# ── Section 4: /locked owner command ─────────────────────────────────────────


class TestLockedCommand:
    async def _run_owner_cmd(self, text: str, proxy: TelegramAPIProxy) -> list[str]:
        """Drive a single owner command through the proxy and capture admin notices."""
        notices: list[str] = []

        async def capture_notice(chat_id, message):
            notices.append(message)

        proxy._send_owner_admin_notice = capture_notice
        response = _wrap(_make_update(text, user_id=OWNER_ID, chat_id=OWNER_CHAT))
        await proxy._filter_inbound_updates(response)
        await asyncio.sleep(0)
        return notices

    async def test_locked_no_active_lockdowns(self):
        proxy = _make_proxy()
        notices = await self._run_owner_cmd("/locked", proxy)
        assert any("No active lockdowns" in n for n in notices)

    async def test_locked_lists_suspended_user(self):
        proxy = _make_proxy()
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")

        notices = await self._run_owner_cmd("/locked", proxy)
        assert any(COLLAB_ID in n for n in notices)
        assert any("SUSPENDED" in n for n in notices)

    async def test_locked_includes_unlock_hint(self):
        proxy = _make_proxy()
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")

        notices = await self._run_owner_cmd("/locked", proxy)
        combined = "\n".join(notices)
        assert "/unlock" in combined

    async def test_locked_shows_all_non_normal_users(self):
        proxy = _make_proxy(collab_ids=[COLLAB_ID, "1111111111"])
        for _ in range(3):
            proxy._lockdown.record_block(COLLAB_ID, "r")
        for _ in range(5):
            proxy._lockdown.record_block("1111111111", "r")

        notices = await self._run_owner_cmd("/locked", proxy)
        combined = "\n".join(notices)
        assert COLLAB_ID in combined
        assert "1111111111" in combined


# ── Section 5: /unlock owner command ─────────────────────────────────────────


class TestUnlockCommand:
    async def _run_owner_cmd(self, text: str, proxy: TelegramAPIProxy) -> list[str]:
        notices: list[str] = []

        async def capture_notice(chat_id, message):
            notices.append(message)

        proxy._send_owner_admin_notice = capture_notice
        response = _wrap(_make_update(text, user_id=OWNER_ID, chat_id=OWNER_CHAT))
        await proxy._filter_inbound_updates(response)
        await asyncio.sleep(0)
        return notices

    async def test_unlock_known_user_succeeds(self):
        proxy = _make_proxy()
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")
        assert proxy._lockdown.is_suspended(COLLAB_ID)

        notices = await self._run_owner_cmd(f"/unlock {COLLAB_ID}", proxy)
        assert any("unlocked" in n.lower() for n in notices)
        assert not proxy._lockdown.is_suspended(COLLAB_ID)

    async def test_unlock_unknown_user_reports_no_state(self):
        proxy = _make_proxy()
        notices = await self._run_owner_cmd(f"/unlock {COLLAB_ID}", proxy)
        assert any("no active lockdown" in n.lower() for n in notices)

    async def test_unlock_clears_suspended_drop_cooldown(self):
        proxy = _make_proxy()
        for _ in range(10):
            proxy._lockdown.record_block(COLLAB_ID, "attack")
        proxy._suspended_drop_notice_until[COLLAB_ID] = time.time() + 9999.0

        await self._run_owner_cmd(f"/unlock {COLLAB_ID}", proxy)
        assert COLLAB_ID not in proxy._suspended_drop_notice_until

    async def test_unlock_without_user_id_shows_usage(self):
        proxy = _make_proxy()
        notices = await self._run_owner_cmd("/unlock", proxy)
        assert any("usage" in n.lower() or "/unlock" in n.lower() for n in notices)


# ── Section 6: SCRUM-203 — one app-wide, principal-keyed lockdown ────────────


class FakeClock:
    def __init__(self, start: float = 1_000_000.0):
        self.now = start

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


class TestPrincipalKeys:
    def test_arbitrary_string_principals_are_isolated(self):
        ld = ProgressiveLockdown()
        for _ in range(3):
            ld.record_block("edge:cloudflare:client-a", "probe")
        ld.record_block(COLLAB_ID, "probe")
        assert ld.level_of("edge:cloudflare:client-a") == LockdownLevel.ALERT
        assert ld.level_of(COLLAB_ID) == LockdownLevel.NORMAL
        assert ld.level_of("edge:never-seen") == LockdownLevel.NORMAL


class TestEscalateTo:
    def test_jumps_directly_to_requested_level(self):
        ld = ProgressiveLockdown()
        action = ld.escalate_to("edge:x:y", LockdownLevel.SUSPENDED, "Falco CRITICAL")
        assert action.level == LockdownLevel.SUSPENDED
        assert action.suspended is True
        assert action.notify_owner is True
        assert "Falco CRITICAL" in action.notify_text
        assert ld.is_suspended("edge:x:y")
        assert ld.level_of("edge:x:y") == LockdownLevel.SUSPENDED

    def test_accepts_string_level(self):
        ld = ProgressiveLockdown()
        action = ld.escalate_to("p", "escalated", "r")
        assert action.level == LockdownLevel.ESCALATED
        assert action.rate_limit_multiplier == 2.0

    def test_never_lowers_level(self):
        ld = ProgressiveLockdown()
        ld.escalate_to("p", LockdownLevel.ESCALATED, "first")
        action = ld.escalate_to("p", LockdownLevel.ALERT, "lower")
        assert action.level == LockdownLevel.ESCALATED
        assert action.notify_owner is False
        assert ld.level_of("p") == LockdownLevel.ESCALATED

    def test_same_level_does_not_renotify(self):
        ld = ProgressiveLockdown()
        assert ld.escalate_to("p", LockdownLevel.ALERT, "a").notify_owner is True
        assert ld.escalate_to("p", LockdownLevel.ALERT, "b").notify_owner is False

    def test_escalated_floor_holds_against_later_low_block_counts(self):
        ld = ProgressiveLockdown()
        ld.escalate_to("p", LockdownLevel.ESCALATED, "falco")
        action = ld.record_block("p", "one block")
        assert action.level == LockdownLevel.ESCALATED
        assert action.notify_owner is False  # already notified at this level

    def test_reset_clears_escalation(self):
        ld = ProgressiveLockdown()
        ld.escalate_to("p", LockdownLevel.SUSPENDED, "falco")
        assert ld.reset("p") is True
        assert ld.level_of("p") == LockdownLevel.NORMAL
        assert not ld.is_suspended("p")

    def test_rejects_unknown_level(self):
        ld = ProgressiveLockdown()
        with pytest.raises(ValueError):
            ld.escalate_to("p", "nuclear", "r")


class TestDecay:
    def test_decay_off_by_default_blocks_never_age_out(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(clock=clock)
        for _ in range(4):
            ld.record_block("p", "r")
            clock.advance(10 * 365 * 86400)  # a decade between blocks
        assert ld.get_status("p")["block_count"] == 4
        assert ld.level_of("p") == LockdownLevel.ALERT

    def test_old_blocks_age_out_when_window_set(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(decay_window_seconds=60.0, clock=clock)
        ld.record_block("p", "r")
        ld.record_block("p", "r")
        clock.advance(61)
        action = ld.record_block("p", "r")
        assert action.level == LockdownLevel.NORMAL
        assert ld.get_status("p")["block_count"] == 1

    def test_blocks_inside_window_still_escalate(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(decay_window_seconds=60.0, clock=clock)
        for _ in range(3):
            ld.record_block("p", "r")
            clock.advance(10)
        assert ld.level_of("p") == LockdownLevel.ALERT

    def test_level_of_reflects_decay_without_new_blocks(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(decay_window_seconds=60.0, clock=clock)
        for _ in range(3):
            ld.record_block("p", "r")
        assert ld.level_of("p") == LockdownLevel.ALERT
        clock.advance(120)
        assert ld.level_of("p") == LockdownLevel.NORMAL

    def test_suspension_is_sticky_under_decay(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(decay_window_seconds=60.0, clock=clock)
        for _ in range(10):
            ld.record_block("p", "r")
        clock.advance(3600)
        assert ld.is_suspended("p")  # only an explicit reset() lifts suspension

    def test_realert_after_full_decay(self):
        clock = FakeClock()
        ld = ProgressiveLockdown(decay_window_seconds=60.0, clock=clock)
        actions = [ld.record_block("p", "r") for _ in range(3)]
        assert actions[-1].notify_owner is True
        clock.advance(120)
        actions = [ld.record_block("p", "r") for _ in range(3)]
        assert actions[-1].notify_owner is True

    def test_rejects_non_positive_window(self):
        with pytest.raises(ValueError):
            ProgressiveLockdown(decay_window_seconds=0)


class TestConcurrency:
    def test_threaded_record_block_counts_exactly(self):
        from concurrent.futures import ThreadPoolExecutor

        ld = ProgressiveLockdown()
        principals = [f"edge:v:c{i}" for i in range(8)]
        per_call = 250

        def hammer(p: str) -> int:
            n_notified = 0
            for _ in range(per_call):
                if ld.record_block(p, "r").notify_owner:
                    n_notified += 1
            return n_notified

        with ThreadPoolExecutor(max_workers=32) as ex:
            results = list(ex.map(hammer, principals * 4))

        for p in principals:
            assert ld.get_status(p)["block_count"] == per_call * 4
            assert ld.is_suspended(p)
        # Exactly three owner notifications (alert, escalate, suspend) per principal.
        assert sum(results) == 3 * len(principals)

    async def test_async_gather_record_block_counts_exactly(self):
        ld = ProgressiveLockdown()

        async def one() -> None:
            await asyncio.to_thread(ld.record_block, "shared", "r")

        await asyncio.gather(*(one() for _ in range(500)))
        assert ld.get_status("shared")["block_count"] == 500


class TestTelegramProxyInjection:
    def test_proxy_uses_injected_instance(self):
        shared = ProgressiveLockdown()
        proxy = TelegramAPIProxy(pipeline=PassthroughPipeline(), lockdown=shared)
        assert proxy._lockdown is shared

    def test_proxy_falls_back_to_private_instance_when_standalone(self):
        proxy = TelegramAPIProxy(pipeline=PassthroughPipeline())
        assert isinstance(proxy._lockdown, ProgressiveLockdown)

    def test_attach_lockdown_replaces_instance(self):
        proxy = TelegramAPIProxy(pipeline=PassthroughPipeline())
        shared = ProgressiveLockdown()
        proxy.attach_lockdown(shared)
        assert proxy._lockdown is shared


class TestLifespanWiring:
    @pytest.mark.asyncio
    async def test_lifespan_sets_one_shared_instance_for_telegram_and_falco(self, test_config):
        import gateway.security.falco_monitor as falco_monitor
        from gateway.ingest_api import main as main_mod

        captured: dict = {}

        class CapturingWatcher:
            def __init__(self, *args, **kwargs):
                captured.update(kwargs)

            async def run(self) -> None:
                return None

        with (
            patch("gateway.ingest_api.lifespan.load_config", return_value=test_config),
            patch.object(falco_monitor, "FalcoAlertWatcher", CapturingWatcher),
        ):
            async with main_mod.lifespan(main_mod.app):
                shared = getattr(main_mod.app_state, "progressive_lockdown", None)
                assert isinstance(shared, ProgressiveLockdown)
                assert main_mod._telegram_proxy._lockdown is shared
                assert captured.get("progressive_lockdown") is shared

    @pytest.mark.asyncio
    async def test_falco_critical_escalates_instance_shared_with_telegram(self, tmp_path):
        from gateway.security.falco_monitor import FalcoAlertWatcher

        shared = ProgressiveLockdown()
        proxy = TelegramAPIProxy(pipeline=PassthroughPipeline(), lockdown=shared)
        watcher = FalcoAlertWatcher(alert_dir=tmp_path, progressive_lockdown=shared)
        alert = {
            "priority": "Critical",
            "rule": "Terminal shell in container",
            "output": "shell spawned",
            "output_fields": {"container.name": "openclaw"},
        }
        (tmp_path / "alerts.json").write_text(json.dumps(alert) + "\n")
        await watcher._process_new_alerts()
        assert proxy._lockdown.get_status("openclaw")["block_count"] == 1
