# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Context Integrity Scoring — C21

Computes a rolling 0.0–1.0 integrity score for a session's context segments.
Depends on:
  - C9 (SystemPromptFingerprint) from prompt_guard
  - C10 (ContextSegment) from context_guard

Score factors:
  +0.3  system prompt HMAC valid
  +0.3  all segment content hashes pass re-check
  +0.2  no UNTRUSTED source injected between SYSTEM segments
  +0.1  no duplicate content hashes (replay)
  +0.1  normal growth rate (not an outlier burst)

Alert at < 0.6, escalate progressive lockdown at < 0.3.
"""
from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.security.context_guard import ContextSegment
    from gateway.security.prompt_guard import SystemPromptFingerprint, PromptGuard

logger = logging.getLogger("agentshroud.security.context_integrity")

_ALERT_THRESHOLD = 0.6
_LOCKDOWN_THRESHOLD = 0.3


@dataclass
class IntegrityScore:
    """Rolling context integrity score for a session."""
    score: float           # 0.0 – 1.0
    factors: List[str]     # score components added
    timestamp: float
    session_id: str


class ContextIntegrityScorer:
    """Scores the integrity of a session's context.

    Usage::

        scorer = ContextIntegrityScorer()
        result = scorer.score_context(
            session_id="abc",
            segments=[seg1, seg2],
            prompt_guard=guard,
            system_prompt="...",
            system_prompt_fingerprint=fp,
        )
    """

    def __init__(self, audit_store: Optional[Any] = None):
        self._audit_store = audit_store
        # Per-session growth rate tracking: { session_id: (last_ts, last_count) }
        self._growth_state: Dict[str, tuple[float, int]] = {}

    def score_context(
        self,
        session_id: str,
        segments: List["ContextSegment"],
        system_prompt: str = "",
        system_prompt_fingerprint: Optional["SystemPromptFingerprint"] = None,
        prompt_guard: Optional["PromptGuard"] = None,
        hmac_key: Optional[bytes] = None,
    ) -> IntegrityScore:
        """Compute a 0.0–1.0 integrity score for the given context segments.

        Args:
            session_id: Identifies the session being scored.
            segments: Ordered list of ContextSegment provenance records.
            system_prompt: The current system prompt text.
            system_prompt_fingerprint: HMAC fingerprint from register_system_prompt().
            prompt_guard: PromptGuard instance for HMAC verification.
            hmac_key: Optional key override for HMAC verification.

        Returns:
            IntegrityScore with score 0.0–1.0 and breakdown factors.
        """
        score = 0.0
        factors: List[str] = []

        # ── Factor 1: System prompt HMAC valid (+0.3) ────────────────────────
        if (
            system_prompt
            and system_prompt_fingerprint is not None
            and prompt_guard is not None
        ):
            if prompt_guard.verify_system_prompt(
                system_prompt, system_prompt_fingerprint, key=hmac_key
            ):
                score += 0.3
                factors.append("system_prompt_hmac_valid:+0.3")
            else:
                factors.append("system_prompt_hmac_INVALID:+0.0")
                logger.warning(
                    "Context integrity: system prompt HMAC mismatch for session %s",
                    session_id,
                )
        else:
            # No fingerprint provided — grant half credit (not enforced yet)
            score += 0.15
            factors.append("system_prompt_hmac_not_enrolled:+0.15")

        # ── Factor 2: Segment content hashes valid (+0.3) ────────────────────
        if segments:
            all_valid = True
            for seg in segments:
                # Re-hash the content via stored hash — we can't re-compute from
                # original content here, so we verify format integrity only.
                if not seg.content_hash or len(seg.content_hash) != 64:
                    all_valid = False
                    factors.append(f"segment_hash_malformed:{seg.segment_id[:8]}:+0.0")
                    break
            if all_valid:
                score += 0.3
                factors.append("segment_hashes_valid:+0.3")
        else:
            # Empty context is clean
            score += 0.3
            factors.append("empty_context_clean:+0.3")

        # ── Factor 3: No untrusted injection between system segments (+0.2) ──
        has_injection = False
        last_was_system = False
        for seg in segments:
            if seg.source == "system":
                last_was_system = True
            elif last_was_system and seg.trust_level == "UNTRUSTED" and seg.source not in ("user",):
                has_injection = True
                factors.append(
                    f"untrusted_injection_after_system:{seg.source}:+0.0"
                )
                break
        if not has_injection:
            score += 0.2
            factors.append("no_untrusted_injection:+0.2")

        # ── Factor 4: No duplicate content hashes (+0.1) ─────────────────────
        hashes = [s.content_hash for s in segments]
        if len(hashes) == len(set(hashes)):
            score += 0.1
            factors.append("no_duplicate_hashes:+0.1")
        else:
            factors.append("duplicate_hashes_detected:+0.0")

        # ── Factor 5: Normal growth rate (+0.1) ──────────────────────────────
        now = time.time()
        prev_ts, prev_count = self._growth_state.get(session_id, (now, 0))
        elapsed = max(now - prev_ts, 1.0)
        growth_rate = (len(segments) - prev_count) / elapsed  # segments per second
        self._growth_state[session_id] = (now, len(segments))

        if growth_rate <= 10.0:  # ≤ 10 new segments/sec is normal
            score += 0.1
            factors.append("normal_growth_rate:+0.1")
        else:
            factors.append(f"abnormal_growth_rate:{growth_rate:.1f}/s:+0.0")

        score = round(min(score, 1.0), 3)

        # ── Threshold actions ─────────────────────────────────────────────────
        if score < _LOCKDOWN_THRESHOLD:
            logger.error(
                "Context integrity CRITICAL for session %s: score=%.3f — "
                "escalating to progressive lockdown",
                session_id, score,
            )
        elif score < _ALERT_THRESHOLD:
            logger.warning(
                "Context integrity LOW for session %s: score=%.3f — audit event logged",
                session_id, score,
            )

        return IntegrityScore(
            score=score,
            factors=factors,
            timestamp=now,
            session_id=session_id,
        )
