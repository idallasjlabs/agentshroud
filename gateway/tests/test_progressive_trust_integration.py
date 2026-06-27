# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""ProgressiveTrustConfig → TrustManager integration tests.

The trust ladder (gateway/security/progressive_trust_config.py) was designed
but never wired. These tests prove the integration: enum mapping, threshold-
gated promotion, typed violation penalties, severe-violation demotion, owner
vouching, per-level tool gating, and the ToolACLEnforcer deny composition —
plus a backward-compat guard that TrustManager without a progressive config
behaves exactly as before.
"""

from __future__ import annotations

from gateway.security.progressive_trust_config import (
    ProgressiveTrustConfig,
    PromotionThreshold,
    ViolationType,
)
from gateway.security.progressive_trust_config import TrustLevel as PLevel
from gateway.security.trust_manager import (
    _MANAGER_BY_PROGRESSIVE,
    _PROGRESSIVE_BY_MANAGER,
    TrustConfig,
    TrustLevel,
    TrustManager,
)


def _fast_ladder() -> ProgressiveTrustConfig:
    """A ladder with thresholds small enough for unit tests."""
    thresholds = {
        PLevel.BASIC: PromotionThreshold(
            min_interactions=0, min_days_since_first=0, max_violations=0
        ),
        PLevel.STANDARD: PromotionThreshold(
            min_interactions=2, min_days_since_first=0, max_violations=0
        ),
        PLevel.TRUSTED: PromotionThreshold(
            min_interactions=4, min_days_since_first=0, max_violations=1
        ),
        PLevel.VERIFIED: PromotionThreshold(
            min_interactions=6,
            min_days_since_first=0,
            max_violations=1,
            requires_owner_vouching=True,
        ),
    }
    return ProgressiveTrustConfig(promotion_thresholds=thresholds)


def _make_tm(progressive=None, **config_overrides) -> TrustManager:
    cfg = TrustConfig(
        decay_rate=0.0,
        max_successes_per_hour=1000,
        **config_overrides,
    )
    return TrustManager(db_path=":memory:", config=cfg, progressive_config=progressive)


def _set_state(tm: TrustManager, agent_id: str, score: float, level: TrustLevel):
    """Seed stored score/level directly (same technique lifespan.py uses)."""
    tm.register_agent(agent_id)
    tm._conn.execute(
        "UPDATE trust_scores SET score = ?, level = ? WHERE agent_id = ?",
        (score, int(level), agent_id),
    )
    tm._conn.commit()


class TestEnumMapping:
    def test_mapping_is_bijective_and_total(self):
        assert set(_PROGRESSIVE_BY_MANAGER.keys()) == set(TrustLevel)
        assert set(_PROGRESSIVE_BY_MANAGER.values()) == set(PLevel)
        for manager_level, p_level in _PROGRESSIVE_BY_MANAGER.items():
            assert _MANAGER_BY_PROGRESSIVE[p_level] == manager_level

    def test_renamed_rungs_map_correctly(self):
        assert _PROGRESSIVE_BY_MANAGER[TrustLevel.ELEVATED] == PLevel.TRUSTED
        assert _PROGRESSIVE_BY_MANAGER[TrustLevel.FULL] == PLevel.VERIFIED


class TestBackwardCompat:
    """TrustManager WITHOUT a progressive config must behave exactly as before."""

    def test_score_alone_promotes_without_config(self):
        tm = _make_tm(progressive=None, success_points=60.0)
        try:
            tm.register_agent("agent")  # BASIC, score 100
            tm.record_success("agent")  # 160 -> STANDARD purely by score
            level, score = tm.get_trust("agent")
            assert level == TrustLevel.STANDARD
            assert score == 160.0
        finally:
            tm.close()

    def test_untyped_violation_uses_legacy_points(self):
        tm = _make_tm(progressive=None)
        try:
            tm.register_agent("agent")  # score 100
            tm.record_violation("agent")  # -50 legacy
            _, score = tm.get_trust("agent")
            assert score == 50.0
        finally:
            tm.close()

    def test_is_tool_allowed_returns_none_without_config(self):
        tm = _make_tm(progressive=None)
        try:
            tm.register_agent("agent")
            assert tm.is_tool_allowed("agent", "web_fetch") is None
        finally:
            tm.close()


class TestGatedPromotion:
    def test_score_alone_cannot_promote_with_ladder(self):
        """High score with too few interactions must NOT climb the ladder."""
        tm = _make_tm(progressive=_fast_ladder(), success_points=200.0)
        try:
            tm.register_agent("agent")  # BASIC, 100, 0 interactions
            tm.record_success("agent")  # score 300 -> ELEVATED by score, but
            # only 0 prior interactions: STANDARD needs 2 -> stays BASIC
            level, score = tm.get_trust("agent")
            assert score == 300.0
            assert level == TrustLevel.BASIC
        finally:
            tm.close()

    def test_promotion_granted_once_thresholds_met(self):
        tm = _make_tm(progressive=_fast_ladder(), success_points=30.0)
        try:
            tm.register_agent("agent")  # BASIC, 100
            tm.record_success("agent")  # 130, prior interactions 0
            tm.record_success("agent")  # 160 >= STANDARD(150), prior 1 < 2 -> BASIC
            assert tm.get_trust("agent")[0] == TrustLevel.BASIC
            tm.record_success("agent")  # 190, prior 2 >= 2 -> STANDARD
            assert tm.get_trust("agent")[0] == TrustLevel.STANDARD
        finally:
            tm.close()

    def test_get_trust_respects_stored_ceiling(self):
        """Stored level is the promotion ceiling when the ladder is active."""
        tm = _make_tm(progressive=_fast_ladder())
        try:
            _set_state(tm, "agent", score=400.0, level=TrustLevel.BASIC)
            level, _ = tm.get_trust("agent")
            assert level == TrustLevel.BASIC
        finally:
            tm.close()

    def test_vouching_required_for_top_rung(self):
        ladder = _fast_ladder()
        tm = _make_tm(progressive=ladder, success_points=100.0)
        try:
            _set_state(tm, "agent", score=450.0, level=TrustLevel.ELEVATED)
            # Seed enough interactions to satisfy VERIFIED's min_interactions=6
            for _ in range(7):
                tm._conn.execute(
                    "UPDATE trust_scores SET total_successes = total_successes + 1 "
                    "WHERE agent_id = ?",
                    ("agent",),
                )
            tm._conn.commit()
            tm.record_success("agent")  # 550 >= FULL(500) but not vouched
            assert tm.get_trust("agent")[0] == TrustLevel.ELEVATED

            tm.vouch_for_agent("agent")
            tm.record_success("agent")
            assert tm.get_trust("agent")[0] == TrustLevel.FULL
        finally:
            tm.close()


class TestTypedViolations:
    def test_typed_penalty_from_config(self):
        tm = _make_tm(progressive=_fast_ladder())
        try:
            tm.register_agent("agent")  # 100
            tm.record_violation(
                "agent", violation_type=ViolationType.RATE_LIMIT_EXCEEDED
            )  # -10 per config, not legacy -50
            _, score = tm.get_trust("agent")
            assert score == 90.0
        finally:
            tm.close()

    def test_severe_violation_forces_demotion(self):
        """MALICIOUS_INTENT drops a level even when the score would not."""
        tm = _make_tm(progressive=_fast_ladder())
        try:
            _set_state(tm, "agent", score=260.0, level=TrustLevel.STANDARD)
            new_level = tm.record_violation("agent", violation_type=ViolationType.MALICIOUS_INTENT)
            # 260 - 100 = 160 would still be STANDARD by score; severe ->
            # forced down one rung with the score clamped to match.
            assert new_level == TrustLevel.BASIC
            level, score = tm.get_trust("agent")
            assert level == TrustLevel.BASIC
            assert score <= tm.config.thresholds[TrustLevel.BASIC]
        finally:
            tm.close()

    def test_non_severe_typed_violation_does_not_force_demotion(self):
        tm = _make_tm(progressive=_fast_ladder())
        try:
            _set_state(tm, "agent", score=260.0, level=TrustLevel.STANDARD)
            new_level = tm.record_violation(
                "agent", violation_type=ViolationType.POLICY_VIOLATION
            )  # -30 -> 230, still STANDARD
            assert new_level == TrustLevel.STANDARD
        finally:
            tm.close()

    def test_demotion_recorded_in_history(self):
        tm = _make_tm(progressive=_fast_ladder())
        try:
            _set_state(tm, "agent", score=260.0, level=TrustLevel.STANDARD)
            tm.record_violation("agent", violation_type=ViolationType.UNAUTHORIZED_ACCESS)
            events = [h["event_type"] for h in tm.get_history("agent")]
            assert "demotion" in events
        finally:
            tm.close()


class TestToolGating:
    def test_tool_allowed_at_level(self):
        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "agent", score=200.0, level=TrustLevel.STANDARD)
            assert tm.is_tool_allowed("agent", "web_fetch") is True
        finally:
            tm.close()

    def test_tool_denied_above_level(self):
        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "agent", score=100.0, level=TrustLevel.BASIC)
            assert tm.is_tool_allowed("agent", "write_file") is False
        finally:
            tm.close()

    def test_full_level_wildcard_allows_everything(self):
        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "agent", score=600.0, level=TrustLevel.FULL)
            assert tm.is_tool_allowed("agent", "write_file") is True
            assert tm.is_tool_allowed("agent", "send_email") is True
        finally:
            tm.close()

    def test_unknown_tool_returns_none(self):
        """Tools outside the ladder vocabulary get no opinion (ACL decides)."""
        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "agent", score=100.0, level=TrustLevel.BASIC)
            assert tm.is_tool_allowed("agent", "some_unrelated_tool") is None
        finally:
            tm.close()

    def test_unregistered_agent_returns_none(self):
        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            assert tm.is_tool_allowed("ghost", "web_fetch") is None
        finally:
            tm.close()


class TestToolACLComposition:
    def test_trust_deny_wins_over_acl(self):
        from gateway.security.tool_acl import ToolACLEnforcer

        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "1234", score=100.0, level=TrustLevel.BASIC)
            enforcer = ToolACLEnforcer(trust_manager=tm)
            allowed, reason = enforcer.can_use_tool("1234", "write_file")
            assert allowed is False
            assert "trust level" in reason
        finally:
            tm.close()

    def test_unknown_tool_falls_through_to_acl(self):
        from gateway.security.tool_acl import ToolACLEnforcer

        tm = _make_tm(progressive=ProgressiveTrustConfig())
        try:
            _set_state(tm, "1234", score=100.0, level=TrustLevel.BASIC)
            enforcer = ToolACLEnforcer(trust_manager=tm)
            _, reason = enforcer.can_use_tool("1234", "completely_unknown_tool")
            # The ladder has no opinion here — whatever the ACL decides, the
            # reason must come from the ACL, not the trust gate.
            assert "trust level" not in reason
        finally:
            tm.close()

    def test_enforcer_without_trust_manager_unchanged(self):
        from gateway.security.tool_acl import ToolACLEnforcer

        enforcer = ToolACLEnforcer()
        _, reason = enforcer.can_use_tool("1234", "write_file")
        assert "trust level" not in reason


class TestProgressiveTrustConfigUnit:
    """First-ever unit tests for the config object itself."""

    def test_level_order(self):
        cfg = ProgressiveTrustConfig()
        order = cfg.get_trust_level_order()
        assert order[0] == PLevel.UNTRUSTED
        assert order[-1] == PLevel.VERIFIED
        assert len(order) == 5

    def test_next_and_previous_levels(self):
        cfg = ProgressiveTrustConfig()
        assert cfg.get_next_trust_level(PLevel.UNTRUSTED) == PLevel.BASIC
        assert cfg.get_next_trust_level(PLevel.VERIFIED) is None
        assert cfg.get_previous_trust_level(PLevel.VERIFIED) == PLevel.TRUSTED
        assert cfg.get_previous_trust_level(PLevel.UNTRUSTED) is None

    def test_is_tool_allowed_wildcard(self):
        cfg = ProgressiveTrustConfig()
        assert cfg.is_tool_allowed(PLevel.VERIFIED, "anything_at_all") is True

    def test_is_tool_allowed_per_level(self):
        cfg = ProgressiveTrustConfig()
        assert cfg.is_tool_allowed(PLevel.UNTRUSTED, "web_search") is False
        assert cfg.is_tool_allowed(PLevel.BASIC, "web_search") is True
        assert cfg.is_tool_allowed(PLevel.STANDARD, "web_fetch") is True
        assert cfg.is_tool_allowed(PLevel.STANDARD, "write_file") is False
        assert cfg.is_tool_allowed(PLevel.TRUSTED, "write_file") is True

    def test_default_penalties_cover_all_violation_types(self):
        cfg = ProgressiveTrustConfig()
        for vtype in ViolationType:
            assert vtype in cfg.violation_penalties
            assert cfg.violation_penalties[vtype] > 0
