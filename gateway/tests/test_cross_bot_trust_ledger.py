# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Module 27 — Cross-Bot Trust Ledger.

IEC 62443 FR6 (Audit Log / Accountability): cross-bot incident propagation must be
recorded in the ledger so operators can trace the decay chain.
IEC 62443 FR3 (System Integrity): an incident on one bot must provably affect
the effective trust of peered bots to prevent lateral trust exploitation.

TDD — tests are written FIRST.  Implementation must satisfy these before merge.
"""

from __future__ import annotations

import pytest

from gateway.security.cross_bot_trust_ledger import (
    BotIncidentSeverity,
    CrossBotTrustLedger,
    IncidentRecord,
    TrustDecayPolicy,
)
from gateway.security.trust_manager import TrustConfig, TrustManager

# Python 3.13 raises ResourceWarning for unclosed sqlite3.Connection objects
# during GC.  TrustManager uses in-memory SQLite databases that are safely
# discarded when the process exits — suppress the warning in tests to avoid
# false failures from pytest's strict unraisable-exception handling.
pytestmark = pytest.mark.filterwarnings(
    "ignore::ResourceWarning",
)

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def policy() -> TrustDecayPolicy:
    """Default propagation policy."""
    return TrustDecayPolicy(
        decay_fraction=0.3,  # 30 % of the originating bot's score delta
        max_propagation_depth=2,
        min_severity_to_propagate=BotIncidentSeverity.MEDIUM,
    )


@pytest.fixture()
def ledger(policy: TrustDecayPolicy) -> CrossBotTrustLedger:
    return CrossBotTrustLedger(policy=policy)


@pytest.fixture()
def openclaw_tm() -> TrustManager:
    tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
    tm.register_agent("openclaw")
    yield tm
    tm.close()


@pytest.fixture()
def hermes_tm() -> TrustManager:
    tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
    tm.register_agent("hermes")
    yield tm
    tm.close()


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------


class TestCrossBotTrustLedgerConstruction:
    def test_empty_ledger_has_no_incidents(self, ledger: CrossBotTrustLedger) -> None:
        assert ledger.incident_count() == 0

    def test_default_policy_is_sane(self) -> None:
        default = CrossBotTrustLedger()
        p = default.policy
        assert 0.0 < p.decay_fraction <= 1.0
        assert p.max_propagation_depth >= 1
        assert isinstance(p.min_severity_to_propagate, BotIncidentSeverity)

    def test_register_peer(self, ledger: CrossBotTrustLedger) -> None:
        ledger.register_peer("openclaw", "hermes")
        assert "hermes" in ledger.peers_of("openclaw")

    def test_register_peer_is_bidirectional_by_default(self, ledger: CrossBotTrustLedger) -> None:
        ledger.register_peer("openclaw", "hermes", bidirectional=True)
        assert "hermes" in ledger.peers_of("openclaw")
        assert "openclaw" in ledger.peers_of("hermes")

    def test_unregistered_bot_has_no_peers(self, ledger: CrossBotTrustLedger) -> None:
        assert ledger.peers_of("ghost-bot") == []


# ---------------------------------------------------------------------------
# Incident propagation
# ---------------------------------------------------------------------------


class TestIncidentPropagation:
    def test_low_severity_not_propagated(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        hermes_before = hermes_tm.get_trust("hermes")
        assert hermes_before is not None
        score_before = hermes_before[1]

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.LOW,
            score_delta=-10.0,
            reason="minor policy breach",
        )

        hermes_after = hermes_tm.get_trust("hermes")
        assert hermes_after is not None
        # LOW is below the min_severity threshold of MEDIUM → no propagation
        assert abs(hermes_after[1] - score_before) < 0.01

    def test_medium_severity_propagates_to_peer(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        hermes_before = hermes_tm.get_trust("hermes")
        assert hermes_before is not None
        score_before = hermes_before[1]

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.MEDIUM,
            score_delta=-40.0,  # penalty applied by caller already to openclaw_tm
            reason="prompt injection detected",
        )

        hermes_after = hermes_tm.get_trust("hermes")
        assert hermes_after is not None
        # 30 % of 40 = 12 points decay on hermes
        expected_decay = 40.0 * 0.3
        actual_decay = score_before - hermes_after[1]
        assert abs(actual_decay - expected_decay) < 0.5

    def test_high_severity_propagates_full_fraction(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        hermes_before = hermes_tm.get_trust("hermes")
        assert hermes_before is not None
        score_before = hermes_before[1]

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-80.0,
            reason="credential exfil attempt",
        )

        hermes_after = hermes_tm.get_trust("hermes")
        assert hermes_after is not None
        expected_decay = 80.0 * 0.3
        actual_decay = score_before - hermes_after[1]
        assert abs(actual_decay - expected_decay) < 0.5

    def test_critical_severity_propagates_full_fraction(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        hermes_before = hermes_tm.get_trust("hermes")
        assert hermes_before is not None
        score_before = hermes_before[1]

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.CRITICAL,
            score_delta=-100.0,
            reason="active compromise signal",
        )

        hermes_after = hermes_tm.get_trust("hermes")
        assert hermes_after is not None
        expected_decay = 100.0 * 0.3
        actual_decay = score_before - hermes_after[1]
        assert abs(actual_decay - expected_decay) < 0.5

    def test_no_self_propagation(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
    ) -> None:
        """An incident on openclaw should not re-apply to openclaw via the ledger."""
        ledger.register_peer("openclaw", "openclaw")  # pathological edge case
        ledger.register_trust_manager("openclaw", openclaw_tm)

        before = openclaw_tm.get_trust("openclaw")
        assert before is not None

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="test self-loop guard",
        )
        # Ledger should not re-penalize openclaw's trust manager
        after = openclaw_tm.get_trust("openclaw")
        assert after is not None
        # Score should be unchanged by the ledger propagation step
        assert abs(after[1] - before[1]) < 0.01

    def test_bot_without_registered_trust_manager_is_skipped(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
    ) -> None:
        """Propagation to a peer with no registered TrustManager must not raise."""
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        # hermes TrustManager intentionally NOT registered

        # Must not raise
        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-60.0,
            reason="peer TM missing",
        )

    def test_propagation_limited_to_max_depth(self) -> None:
        """Depth-2 propagation: A → B → C but NOT C → D when max_depth=2."""
        policy = TrustDecayPolicy(
            decay_fraction=0.5,
            max_propagation_depth=2,
            min_severity_to_propagate=BotIncidentSeverity.LOW,
        )
        ledger = CrossBotTrustLedger(policy=policy)

        tm_a = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=300.0))
        tm_b = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=300.0))
        tm_c = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=300.0))
        tm_d = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=300.0))

        for bot, tm in [("a", tm_a), ("b", tm_b), ("c", tm_c), ("d", tm_d)]:
            tm.register_agent(bot)
            ledger.register_trust_manager(bot, tm)

        ledger.register_peer("a", "b")
        ledger.register_peer("b", "c")
        ledger.register_peer("c", "d")

        ledger.record_incident(
            source_bot="a",
            agent_id="a",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-100.0,
            reason="depth test",
        )

        b_after = tm_b.get_trust("b")
        c_after = tm_c.get_trust("c")
        d_after = tm_d.get_trust("d")

        assert b_after is not None and c_after is not None and d_after is not None

        # B is depth-1: must decay
        assert b_after[1] < 300.0
        # C is depth-2: must also decay (depth limit is 2)
        assert c_after[1] < 300.0
        # D is depth-3: must NOT decay (exceeds max_propagation_depth=2)
        assert abs(d_after[1] - 300.0) < 0.01


# ---------------------------------------------------------------------------
# Incident record audit
# ---------------------------------------------------------------------------


class TestIncidentAudit:
    def test_incidents_are_recorded(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="audit test",
        )

        assert ledger.incident_count() == 1

    def test_get_incidents_by_source(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="first incident",
        )
        ledger.record_incident(
            source_bot="hermes",
            agent_id="hermes",
            severity=BotIncidentSeverity.MEDIUM,
            score_delta=-20.0,
            reason="second incident",
        )

        openclaw_incidents = ledger.get_incidents(source_bot="openclaw")
        assert len(openclaw_incidents) == 1
        assert openclaw_incidents[0].source_bot == "openclaw"
        assert openclaw_incidents[0].severity == BotIncidentSeverity.HIGH

    def test_incident_record_fields(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
        hermes_tm: TrustManager,
    ) -> None:
        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.CRITICAL,
            score_delta=-75.0,
            reason="field test",
        )

        incidents = ledger.get_incidents()
        assert len(incidents) == 1
        rec: IncidentRecord = incidents[0]
        assert rec.source_bot == "openclaw"
        assert rec.agent_id == "openclaw"
        assert rec.severity == BotIncidentSeverity.CRITICAL
        assert rec.score_delta == -75.0
        assert rec.reason == "field test"
        assert rec.timestamp > 0.0
        assert len(rec.propagated_to) >= 1
        assert "hermes" in rec.propagated_to

    def test_propagated_to_is_empty_for_no_peers(
        self, ledger: CrossBotTrustLedger, openclaw_tm: TrustManager
    ) -> None:
        ledger.register_trust_manager("openclaw", openclaw_tm)

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-30.0,
            reason="no peers",
        )

        incidents = ledger.get_incidents()
        assert incidents[0].propagated_to == []

    def test_incident_limit_retained(
        self, ledger: CrossBotTrustLedger, openclaw_tm: TrustManager
    ) -> None:
        ledger.register_trust_manager("openclaw", openclaw_tm)
        openclaw_tm.register_agent("openclaw")

        # Push past the default retention limit
        for i in range(ledger.max_incidents + 5):
            ledger.record_incident(
                source_bot="openclaw",
                agent_id="openclaw",
                severity=BotIncidentSeverity.LOW,
                score_delta=-1.0,
                reason=f"incident {i}",
            )

        assert ledger.incident_count() <= ledger.max_incidents


# ---------------------------------------------------------------------------
# Severity enumeration
# ---------------------------------------------------------------------------


class TestBotIncidentSeverity:
    def test_ordering(self) -> None:
        assert BotIncidentSeverity.LOW < BotIncidentSeverity.MEDIUM
        assert BotIncidentSeverity.MEDIUM < BotIncidentSeverity.HIGH
        assert BotIncidentSeverity.HIGH < BotIncidentSeverity.CRITICAL

    def test_from_string(self) -> None:
        assert BotIncidentSeverity("medium") == BotIncidentSeverity.MEDIUM
        assert BotIncidentSeverity("critical") == BotIncidentSeverity.CRITICAL

    def test_invalid_string_returns_none(self) -> None:
        assert BotIncidentSeverity._missing_("nosuchseverity") is None

    def test_non_string_returns_none(self) -> None:
        assert BotIncidentSeverity._missing_(999) is None


class TestTrustDecayPolicyValidation:
    def test_zero_decay_fraction_rejected(self) -> None:
        with pytest.raises(ValueError, match="decay_fraction"):
            TrustDecayPolicy(decay_fraction=0.0)

    def test_fraction_above_one_rejected(self) -> None:
        with pytest.raises(ValueError, match="decay_fraction"):
            TrustDecayPolicy(decay_fraction=1.5)

    def test_zero_max_depth_rejected(self) -> None:
        with pytest.raises(ValueError, match="max_propagation_depth"):
            TrustDecayPolicy(max_propagation_depth=0)


class TestGetIncidentsLimit:
    def test_get_incidents_with_limit(
        self, ledger: CrossBotTrustLedger, openclaw_tm: TrustManager
    ) -> None:
        ledger.register_trust_manager("openclaw", openclaw_tm)

        for i in range(5):
            ledger.record_incident(
                source_bot="openclaw",
                agent_id="openclaw",
                severity=BotIncidentSeverity.LOW,
                score_delta=-1.0,
                reason=f"incident {i}",
            )

        limited = ledger.get_incidents(limit=2)
        assert len(limited) == 2

    def test_propagation_registers_unregistered_peer_agent(
        self,
        ledger: CrossBotTrustLedger,
        openclaw_tm: TrustManager,
    ) -> None:
        """Peer agent not registered in TrustManager should be auto-registered."""
        hermes_tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
        # Note: do NOT call hermes_tm.register_agent("hermes") here

        ledger.register_peer("openclaw", "hermes")
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        # Must not raise, and hermes should be auto-registered
        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="auto-register test",
        )
        # After propagation, hermes should have a trust entry
        assert hermes_tm.get_trust("hermes") is not None


class TestBuildFullMesh:
    """build_full_mesh: N-agent-scalable topology construction.

    Adding a 3rd/4th/Nth bot_id to the input list must be the ONLY change
    needed for it to become a full mutual peer of every existing bot — no
    pairwise registration code changes. This is what backs the "add more
    agents and this all works" requirement.
    """

    def _shared_tm(self) -> TrustManager:
        tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
        for bot_id in ("openclaw", "hermes", "thirdbot", "fourthbot"):
            tm.register_agent(bot_id)
        return tm

    def test_two_bots_are_mutual_peers(self) -> None:
        tm = self._shared_tm()
        ledger = CrossBotTrustLedger.build_full_mesh(["openclaw", "hermes"], tm)
        assert ledger.peers_of("openclaw") == ["hermes"]
        assert ledger.peers_of("hermes") == ["openclaw"]

    def test_three_bots_form_a_full_mesh(self) -> None:
        tm = self._shared_tm()
        ledger = CrossBotTrustLedger.build_full_mesh(["openclaw", "hermes", "thirdbot"], tm)
        assert set(ledger.peers_of("openclaw")) == {"hermes", "thirdbot"}
        assert set(ledger.peers_of("hermes")) == {"openclaw", "thirdbot"}
        assert set(ledger.peers_of("thirdbot")) == {"openclaw", "hermes"}

    def test_adding_a_fourth_bot_extends_the_mesh_to_everyone(self) -> None:
        """The exact scenario the user asked for: add a 4th bot and it just works."""
        tm = self._shared_tm()
        bot_ids = ["openclaw", "hermes", "thirdbot", "fourthbot"]
        ledger = CrossBotTrustLedger.build_full_mesh(bot_ids, tm)
        for bot in bot_ids:
            expected_peers = set(bot_ids) - {bot}
            assert (
                set(ledger.peers_of(bot)) == expected_peers
            ), f"{bot} should be peers with everyone else in a full mesh"

    def test_every_bot_shares_the_same_trust_manager(self) -> None:
        tm = self._shared_tm()
        bot_ids = ["openclaw", "hermes", "thirdbot"]
        ledger = CrossBotTrustLedger.build_full_mesh(bot_ids, tm)
        for bot in bot_ids:
            assert ledger._trust_managers[bot] is tm

    def test_single_bot_has_no_peers_and_does_not_raise(self) -> None:
        tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
        tm.register_agent("openclaw")
        ledger = CrossBotTrustLedger.build_full_mesh(["openclaw"], tm)
        assert ledger.peers_of("openclaw") == []

    def test_empty_bot_list_does_not_raise(self) -> None:
        tm = TrustManager(db_path=":memory:", config=TrustConfig(initial_score=200.0))
        ledger = CrossBotTrustLedger.build_full_mesh([], tm)
        assert ledger.incident_count() == 0

    def test_incident_on_one_bot_propagates_to_all_mesh_peers(self) -> None:
        """End-to-end: a real incident on bot A decays trust on bots B and C
        in a 3-bot full mesh — not just a 2-bot pair."""
        tm = self._shared_tm()
        bot_ids = ["openclaw", "hermes", "thirdbot"]
        ledger = CrossBotTrustLedger.build_full_mesh(bot_ids, tm)

        before_hermes = tm.get_trust("hermes")[1]
        before_third = tm.get_trust("thirdbot")[1]

        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="full-mesh propagation test",
        )

        after_hermes = tm.get_trust("hermes")[1]
        after_third = tm.get_trust("thirdbot")[1]

        assert after_hermes < before_hermes, "hermes should decay from openclaw's incident"
        assert after_third < before_third, "thirdbot should decay from openclaw's incident"
