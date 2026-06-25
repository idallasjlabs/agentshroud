# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Cross-Bot Trust Ledger — Module 27 (v1.2.0)

IEC 62443 FR6 (Audit Log / Accountability): every cross-bot incident is logged
in an append-only in-memory ledger; operators can query propagation history.
IEC 62443 FR3 (System Integrity): an incident on one bot propagates a
configurable fraction of its score penalty to all registered peer bots, so a
compromise on openclaw immediately demotes hermes's effective trust level —
closing the lateral-trust exploitation surface.

Architecture note
-----------------
The ledger owns no TrustManager state; it holds references to externally owned
TrustManager instances. The caller applies the primary penalty (record_violation /
record_failure) on the source bot's manager BEFORE or AFTER calling
``record_incident``; the ledger only drives propagation to *peers*.

Propagation rules
-----------------
1. Only incidents whose severity >= policy.min_severity_to_propagate are
   propagated (LOW is below the default threshold of MEDIUM).
2. Propagation is depth-limited to ``policy.max_propagation_depth``.
3. A bot is never its own peer target (no self-propagation).
4. Peers without a registered TrustManager are silently skipped.
5. Peer decay = abs(score_delta) * policy.decay_fraction.
"""

from __future__ import annotations

import logging
import time
from collections import deque
from dataclasses import dataclass, field
from enum import IntEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.security.trust_manager import TrustManager

logger = logging.getLogger("agentshroud.security.cross_bot_trust_ledger")


# ---------------------------------------------------------------------------
# Severity
# ---------------------------------------------------------------------------


class BotIncidentSeverity(IntEnum):
    """Ordered severity levels for cross-bot incidents.

    Values map to IEC 62443 SLIR taxonomy roughly:
      LOW      → nuisance / policy breach
      MEDIUM   → suspicious pattern / repeated failure
      HIGH     → exploitation attempt
      CRITICAL → active compromise / confirmed attack
    """

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

    @classmethod
    def _missing_(cls, value: object) -> "BotIncidentSeverity | None":
        if isinstance(value, str):
            try:
                return cls[value.upper()]
            except KeyError:
                pass
        return None


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass
class TrustDecayPolicy:
    """Configuration for how incidents decay peer trust scores.

    Attributes:
        decay_fraction: Fraction of abs(score_delta) applied to each peer.
            Must be in (0, 1].  Default 0.3 (30 %).
        max_propagation_depth: Maximum hop distance.  1 = direct peers only;
            2 = peers-of-peers too.  Default 2.
        min_severity_to_propagate: Incidents below this threshold are logged
            but NOT propagated.  Default MEDIUM.
    """

    decay_fraction: float = 0.3
    max_propagation_depth: int = 2
    min_severity_to_propagate: BotIncidentSeverity = BotIncidentSeverity.MEDIUM

    def __post_init__(self) -> None:
        if not (0.0 < self.decay_fraction <= 1.0):
            raise ValueError(
                f"decay_fraction must be in (0, 1]; got {self.decay_fraction}"
            )
        if self.max_propagation_depth < 1:
            raise ValueError(
                f"max_propagation_depth must be >= 1; got {self.max_propagation_depth}"
            )


@dataclass
class IncidentRecord:
    """A single cross-bot incident recorded in the ledger."""

    source_bot: str
    agent_id: str
    severity: BotIncidentSeverity
    score_delta: float  # negative (penalty) applied to source bot
    reason: str
    timestamp: float
    propagated_to: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# CrossBotTrustLedger
# ---------------------------------------------------------------------------


class CrossBotTrustLedger:
    """Shared trust decay channel for multi-bot deployments.

    Usage::

        ledger = CrossBotTrustLedger()
        ledger.register_peer("openclaw", "hermes", bidirectional=True)
        ledger.register_trust_manager("openclaw", openclaw_tm)
        ledger.register_trust_manager("hermes", hermes_tm)

        # After the primary penalty has been applied to openclaw_tm:
        ledger.record_incident(
            source_bot="openclaw",
            agent_id="openclaw",
            severity=BotIncidentSeverity.HIGH,
            score_delta=-50.0,
            reason="prompt injection detected",
        )
    """

    #: Default maximum incidents retained before the oldest are dropped.
    max_incidents: int = 1_000

    def __init__(
        self,
        policy: TrustDecayPolicy | None = None,
        max_incidents: int = 1_000,
    ) -> None:
        self.policy: TrustDecayPolicy = policy or TrustDecayPolicy()
        self.max_incidents = max_incidents

        # Graph: source_bot → set of peer bot names
        self._peers: dict[str, set[str]] = {}
        # Registered TrustManager instances keyed by bot name
        self._trust_managers: dict[str, TrustManager] = {}
        # Append-only incident log (bounded)
        self._incidents: deque[IncidentRecord] = deque(maxlen=max_incidents)

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register_peer(
        self, bot_a: str, bot_b: str, bidirectional: bool = True
    ) -> None:
        """Register bot_b as a peer of bot_a.

        Args:
            bot_a: Source bot name.
            bot_b: Peer bot name.
            bidirectional: If True (default), also register bot_a as a peer
                of bot_b so incidents flow both ways.
        """
        self._peers.setdefault(bot_a, set()).add(bot_b)
        if bidirectional:
            self._peers.setdefault(bot_b, set()).add(bot_a)

    def register_trust_manager(self, bot_name: str, trust_manager: TrustManager) -> None:
        """Attach a TrustManager instance to a bot name."""
        self._trust_managers[bot_name] = trust_manager

    def peers_of(self, bot_name: str) -> list[str]:
        """Return the registered peers for *bot_name* (empty list if none)."""
        return list(self._peers.get(bot_name, []))

    # ------------------------------------------------------------------
    # Incident recording + propagation
    # ------------------------------------------------------------------

    def record_incident(
        self,
        source_bot: str,
        agent_id: str,
        severity: BotIncidentSeverity,
        score_delta: float,
        reason: str,
    ) -> IncidentRecord:
        """Log an incident and propagate trust decay to registered peers.

        Args:
            source_bot: The bot where the incident originated.
            agent_id:   The agent identity within that bot.
            severity:   Incident severity (see BotIncidentSeverity).
            score_delta: Negative score change already applied to the source
                bot's TrustManager by the caller.  The propagation computes
                peer decay as ``abs(score_delta) * policy.decay_fraction``.
            reason:     Human-readable description for audit logs.

        Returns:
            The IncidentRecord appended to the ledger.
        """
        record = IncidentRecord(
            source_bot=source_bot,
            agent_id=agent_id,
            severity=severity,
            score_delta=score_delta,
            reason=reason,
            timestamp=time.time(),
            propagated_to=[],
        )

        if severity >= self.policy.min_severity_to_propagate:
            self._propagate(
                source_bot=source_bot,
                agent_id=agent_id,
                score_delta=score_delta,
                depth=0,
                visited={source_bot},
                propagated_to=record.propagated_to,
            )
        else:
            logger.debug(
                "CrossBotTrustLedger: incident on %s (severity=%s) below propagation threshold — not propagated",
                source_bot,
                severity.name,
            )

        self._incidents.append(record)
        return record

    def _propagate(
        self,
        source_bot: str,
        agent_id: str,
        score_delta: float,
        depth: int,
        visited: set[str],
        propagated_to: list[str],
    ) -> None:
        """Recursive BFS propagation up to max_propagation_depth hops."""
        if depth >= self.policy.max_propagation_depth:
            return

        peer_decay = abs(score_delta) * self.policy.decay_fraction

        for peer in self.peers_of(source_bot):
            if peer in visited:
                continue  # no self-loops or back-edges

            visited.add(peer)
            tm = self._trust_managers.get(peer)
            if tm is None:
                logger.debug(
                    "CrossBotTrustLedger: peer %s has no registered TrustManager — skipping",
                    peer,
                )
                continue

            # Apply decay by recording a failure on the peer's own agent_id.
            # We use record_failure (not record_violation) so the peer's counter
            # state reflects that it was not the primary offender.
            try:
                # Ensure the peer agent is registered before we penalise it
                if tm.get_trust(peer) is None:
                    tm.register_agent(peer)
                # Temporarily override failure_points to apply exact peer_decay
                orig_failure = tm.config.failure_points
                tm.config.failure_points = -peer_decay
                tm.record_failure(
                    peer,
                    details=f"cross-bot decay from {source_bot}: {agent_id} — {self.policy.decay_fraction*100:.0f}% of {abs(score_delta):.1f}pt penalty",
                )
                tm.config.failure_points = orig_failure
                propagated_to.append(peer)
                logger.info(
                    "CrossBotTrustLedger: propagated %.1f-pt decay to peer %s (depth=%d)",
                    peer_decay,
                    peer,
                    depth + 1,
                )
            except Exception as exc:
                logger.error(
                    "CrossBotTrustLedger: failed to apply decay to peer %s: %s",
                    peer,
                    exc,
                )

            # Recurse to the peer's own peers (depth + 1)
            self._propagate(
                source_bot=peer,
                agent_id=agent_id,
                score_delta=peer_decay,
                depth=depth + 1,
                visited=visited,
                propagated_to=propagated_to,
            )

    # ------------------------------------------------------------------
    # Querying
    # ------------------------------------------------------------------

    def incident_count(self) -> int:
        """Return the number of incidents currently in the ledger."""
        return len(self._incidents)

    def get_incidents(
        self,
        source_bot: str | None = None,
        limit: int | None = None,
    ) -> list[IncidentRecord]:
        """Return incidents, optionally filtered by source bot.

        Args:
            source_bot: If provided, return only incidents from this bot.
            limit:      Maximum number of incidents to return (most recent first).

        Returns:
            List of IncidentRecord, newest first.
        """
        items: list[IncidentRecord] = list(self._incidents)
        if source_bot is not None:
            items = [i for i in items if i.source_bot == source_bot]
        items = list(reversed(items))  # newest first
        if limit is not None:
            items = items[:limit]
        return items
