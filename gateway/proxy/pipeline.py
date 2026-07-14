# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Proxy Pipeline — all messages flow through security checks.

Inbound: prompt guard → PII sanitizer → trust check → audit → forward
Outbound: PII sanitizer → outbound info filter → canary tripwire → encoding detector → egress filter → audit → return
"""


import hashlib
import logging
import time
from collections import deque
from dataclasses import dataclass, field
from enum import Enum
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from gateway.security.outbound_filter import FilterResult

logger = logging.getLogger("agentshroud.proxy.pipeline")

try:
    from gateway.security.rbac_config import RBACConfig
except ImportError:
    RBACConfig = None


class PipelineAction(str, Enum):
    FORWARD = "forward"
    BLOCK = "block"
    QUEUE_APPROVAL = "queue_approval"


@dataclass
class PipelineResult:
    """Result of running a message through the security pipeline."""

    original_message: str
    sanitized_message: str
    action: PipelineAction = PipelineAction.FORWARD
    blocked: bool = False
    block_reason: str = ""
    prompt_score: float = 0.0
    prompt_patterns: list[str] = field(default_factory=list)
    pii_redactions: list[str] = field(default_factory=list)
    pii_redaction_count: int = 0
    trust_allowed: bool = True
    trust_level: Optional[int] = None
    audit_entry_id: str = ""
    audit_hash: str = ""
    queued_for_approval: bool = False
    approval_id: str = ""
    direction: str = "inbound"
    timestamp: float = 0.0
    processing_time_ms: float = 0.0
    # New fields for outbound info filter
    info_filter_redactions: list[str] = field(default_factory=list)
    info_filter_redaction_count: int = 0
    info_disclosure_risk: str = ""
    # New fields for canary tripwire and encoding detection
    canary_detections: list[str] = field(default_factory=list)
    canary_blocked: bool = False
    encoding_detections: list[str] = field(default_factory=list)
    encoding_decoded_segments: int = 0
    # C21 context integrity (-1.0 = not scored; real scores are 0.0–1.0)
    integrity_score: float = -1.0
    integrity_factors: list[str] = field(default_factory=list)
    # C46 signed instruction envelope attestation (outbound)
    envelope_id: str = ""
    envelope_signature: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "action": self.action.value,
            "blocked": self.blocked,
            "block_reason": self.block_reason,
            "prompt_score": self.prompt_score,
            "prompt_patterns": self.prompt_patterns,
            "pii_redactions": self.pii_redactions,
            "pii_redaction_count": self.pii_redaction_count,
            "trust_allowed": self.trust_allowed,
            "trust_level": self.trust_level,
            "audit_entry_id": self.audit_entry_id,
            "audit_hash": self.audit_hash,
            "queued_for_approval": self.queued_for_approval,
            "direction": self.direction,
            "processing_time_ms": self.processing_time_ms,
            "info_filter_redactions": self.info_filter_redactions,
            "info_filter_redaction_count": self.info_filter_redaction_count,
            "info_disclosure_risk": self.info_disclosure_risk,
            "canary_detections": self.canary_detections,
            "canary_blocked": self.canary_blocked,
            "encoding_detections": self.encoding_detections,
            "encoding_decoded_segments": self.encoding_decoded_segments,
            "integrity_score": self.integrity_score,
            "integrity_factors": self.integrity_factors,
            "envelope_id": self.envelope_id,
            "envelope_signature": self.envelope_signature,
        }


@dataclass
class AuditChainEntry:
    """An entry in the SHA-256 hash chain audit ledger."""

    id: str
    timestamp: float
    direction: str
    content_hash: str
    previous_hash: str
    chain_hash: str  # SHA-256(previous_hash + content_hash + direction + timestamp)
    metadata: dict[str, Any] = field(default_factory=dict)


class AuditChain:
    """SHA-256 hash chain for tamper-evident audit logging."""

    GENESIS_HASH = "0" * 64

    def __init__(self, audit_store=None, max_entries: int = 10_000):
        # Bounded in-memory window: full history is durably persisted to the
        # SQLite audit store; only the most recent entries stay resident.
        self._entries: deque[AuditChainEntry] = deque(maxlen=max_entries)
        self._total_appended: int = 0
        self._last_hash: str = self.GENESIS_HASH
        self._audit_store = audit_store  # Optional AuditStore for persistence

    def append(
        self,
        content: str,
        direction: str,
        metadata: dict[str, Any] | None = None,
        _skip_task: bool = False,
    ) -> AuditChainEntry:
        import asyncio
        import uuid

        now = time.time()
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        chain_input = f"{self._last_hash}:{content_hash}:{direction}:{now}"
        chain_hash = hashlib.sha256(chain_input.encode()).hexdigest()
        entry = AuditChainEntry(
            id=str(uuid.uuid4()),
            timestamp=now,
            direction=direction,
            content_hash=content_hash,
            previous_hash=self._last_hash,
            chain_hash=chain_hash,
            metadata=metadata or {},
        )
        self._entries.append(entry)
        self._total_appended += 1
        self._last_hash = chain_hash

        # Persist to SQLite audit store if configured (fire-and-forget).
        # _skip_task=True suppresses this for block events, which are persisted
        # synchronously via append_block() instead.
        if self._audit_store is not None and not _skip_task:
            try:
                loop = asyncio.get_running_loop()
                loop.create_task(
                    self._audit_store.log_event(
                        event_type=f"audit_chain.{direction}",
                        severity="INFO",
                        details={
                            "chain_hash": chain_hash,
                            "content_hash": content_hash,
                            "previous_hash": entry.previous_hash,
                            **(metadata or {}),
                        },
                        source_module="pipeline.audit_chain",
                        event_id=entry.id,
                    )
                )
            except RuntimeError:
                pass  # No running event loop (e.g. sync test context)

        return entry

    async def append_block(
        self,
        content: str,
        direction: str,
        metadata: dict[str, Any] | None = None,
    ) -> AuditChainEntry:
        """Append to the chain with guaranteed SQLite persistence.

        Used exclusively for BLOCK events.  Unlike append(), which uses
        fire-and-forget create_task(), this method awaits the SQLite write
        directly so that security-critical block events are never silently
        lost under load.  The in-memory chain entry is created first (via
        append() with _skip_task=True) so the hash chain stays consistent
        even if the DB write fails.
        """
        entry = self.append(content, direction, metadata, _skip_task=True)
        if self._audit_store is not None:
            try:
                await self._audit_store.log_event(
                    event_type=f"audit_chain.{direction}",
                    severity="CRITICAL",
                    details={
                        "chain_hash": entry.chain_hash,
                        "content_hash": entry.content_hash,
                        "previous_hash": entry.previous_hash,
                        **(metadata or {}),
                    },
                    source_module="pipeline.audit_chain.block",
                    event_id=entry.id,
                )
            except Exception as exc:
                logger.error("Block event guaranteed audit persistence failed: %s", exc)
        return entry

    async def append_owner_bypass(
        self,
        content: str,
        guard: str,
        reason: str,
        metadata: dict[str, Any] | None = None,
    ) -> AuditChainEntry:
        """Record an owner guard-bypass in the tamper-evident chain (SCRUM-95).

        The owner is exempt from inbound security guards, but that exemption
        must itself be accountable: IEC 62443 FR6 requires a tamper-evident
        record of *every* security-relevant decision, including when a guard
        that WOULD have blocked is bypassed because the request carries the
        owner's identity.  Without this, an owner-account compromise would leave
        no hash-chain evidence of which guards were bypassed.

        Like append_block, this awaits the SQLite write so the record is never
        lost under load, and appends to the in-memory hash chain first so chain
        integrity holds even if the DB write fails.  Persisted at HIGH severity
        (a bypass is not a block, but is security-relevant).
        """
        meta = {"guard": guard, "would_block_reason": reason, **(metadata or {})}
        entry = self.append(content, "inbound_owner_bypass", meta, _skip_task=True)
        if self._audit_store is not None:
            try:
                await self._audit_store.log_event(
                    event_type="audit_chain.owner_bypass",
                    severity="HIGH",
                    details={
                        "chain_hash": entry.chain_hash,
                        "content_hash": entry.content_hash,
                        "previous_hash": entry.previous_hash,
                        **meta,
                    },
                    source_module="pipeline.audit_chain.owner_bypass",
                    event_id=entry.id,
                )
            except Exception as exc:
                logger.error("Owner-bypass audit persistence failed: %s", exc)
        return entry

    def verify_chain(self) -> tuple[bool, str]:
        """Verify the integrity of the retained hash-chain window.

        When the bounded window has wrapped, verification anchors at the
        first retained entry's previous_hash (full-history verification is
        done against the SQLite audit store).  When it has not wrapped, the
        anchor must be the genesis hash.
        Returns (valid, error_message)."""
        if not self._entries:
            return True, "Empty chain"
        first = self._entries[0]
        wrapped = self._total_appended > len(self._entries)
        if not wrapped and first.previous_hash != self.GENESIS_HASH:
            return (
                False,
                f"Entry 0 ({first.id}): anchor mismatch (unwrapped chain must anchor at genesis)",
            )
        prev_hash = first.previous_hash
        for i, entry in enumerate(self._entries):
            if entry.previous_hash != prev_hash:
                return False, f"Entry {i} ({entry.id}): previous_hash mismatch"
            expected_input = (
                f"{entry.previous_hash}:{entry.content_hash}:{entry.direction}:{entry.timestamp}"
            )
            expected_hash = hashlib.sha256(expected_input.encode()).hexdigest()
            if entry.chain_hash != expected_hash:
                return False, f"Entry {i} ({entry.id}): chain_hash mismatch (tampered)"
            prev_hash = entry.chain_hash
        return True, f"Chain valid ({len(self._entries)} entries, {self._total_appended} total)"

    @property
    def entries(self) -> list[AuditChainEntry]:
        return list(self._entries)

    @property
    def last_hash(self) -> str:
        return self._last_hash

    @property
    def total_appended(self) -> int:
        return self._total_appended

    def __len__(self) -> int:
        return len(self._entries)


class SecurityPipeline:
    """Main security pipeline that all messages pass through.

    Wires together: PromptGuard, PIISanitizer, TrustManager,
    EgressFilter, ApprovalQueue, OutboundInfoFilter, CanaryTripwire,
    EncodingDetector, KeyLeakDetector, AuditChain, CrossBotTrustLedger
    (Module 27), and DifferentialPIIDetector (Module 28).
    """

    def __init__(
        self,
        prompt_guard=None,
        pii_sanitizer=None,
        trust_manager=None,
        egress_filter=None,
        approval_queue=None,
        outbound_filter=None,
        canary_tripwire=None,
        encoding_detector=None,
        context_guard=None,
        output_canary=None,
        enhanced_tool_sanitizer=None,
        key_leak_detector=None,
        prompt_block_threshold: float = 0.8,
        approval_actions: list[str] | None = None,
        audit_store=None,
        prompt_protection=None,
        heuristic_classifier=None,
        clamav_scanner=None,
        # C21 / C25 / C46 optional guards
        context_integrity_scorer=None,
        output_schema_enforcer=None,
        envelope_signer=None,
        # CVE-2026-30741: inbound injection scanner (reuses ToolResultInjectionScanner)
        tool_result_injection_scanner=None,
        # CVE-2026-34425: inbound command injection scanner (reuses XMLLeakFilter C32 patterns)
        xml_leak_filter=None,
        # Module 27 (v1.2.0): Cross-Bot Trust Ledger
        # IEC 62443 FR3/FR6 — propagates trust decay across bot peers on incident
        cross_bot_trust_ledger=None,
        # Module 28 (v1.2.0): Differential PII Detector for Tool Results
        # IEC 62443 FR3 — lower-floor PII pass on tool results to catch adversarial exfil
        differential_pii_detector=None,
    ):
        self.prompt_guard = prompt_guard
        self.pii_sanitizer = pii_sanitizer
        self.trust_manager = trust_manager
        self.egress_filter = egress_filter
        self.approval_queue = approval_queue
        self.outbound_filter = outbound_filter
        self.canary_tripwire = canary_tripwire
        self.encoding_detector = encoding_detector
        self.context_guard = context_guard
        self.output_canary = output_canary
        self.enhanced_tool_sanitizer = enhanced_tool_sanitizer
        self.key_leak_detector = key_leak_detector
        self.prompt_protection = prompt_protection
        self.heuristic_classifier = heuristic_classifier
        self.clamav_scanner = clamav_scanner
        self.tool_result_injection_scanner = tool_result_injection_scanner
        self.xml_leak_filter = xml_leak_filter
        # C21 / C25 / C46
        self.context_integrity_scorer = context_integrity_scorer
        self.output_schema_enforcer = output_schema_enforcer
        self.envelope_signer = envelope_signer
        # Module 27: Cross-Bot Trust Ledger (v1.2.0)
        self.cross_bot_trust_ledger = cross_bot_trust_ledger
        # Module 28: Differential PII Detector (v1.2.0)
        self.differential_pii_detector = differential_pii_detector
        self.prompt_block_threshold = prompt_block_threshold
        # Owner exemption: owner messages are logged but never blocked
        self._owner_user_id = None
        if RBACConfig:
            try:
                self._owner_user_id = RBACConfig().owner_user_id
            except Exception:
                pass
        self.approval_actions = approval_actions or [
            "execute_command",
            "delete_file",
            "admin_action",
            "install_package",
        ]
        self.audit_chain = AuditChain(audit_store=audit_store)
        self._stats = {
            "inbound_total": 0,
            "inbound_blocked": 0,
            "inbound_sanitized": 0,
            "inbound_queued": 0,
            "outbound_total": 0,
            "outbound_sanitized": 0,
            "outbound_blocked": 0,
            "outbound_info_filtered": 0,
            "canary_blocked": 0,
            "encoding_detected": 0,
            "pii_redactions_total": 0,
            "info_redactions_total": 0,
        }

        # Fail-closed: raise immediately if a required guard is missing.
        # Without PII sanitization, the pipeline would pass raw PII through
        # to agents — that's unacceptable.
        _REQUIRED_GUARDS = ("pii_sanitizer",)
        missing_required = [g for g in _REQUIRED_GUARDS if getattr(self, g) is None]
        if missing_required:
            raise RuntimeError(
                f"SecurityPipeline cannot start: required guards missing: "
                f"{missing_required}. Refusing to operate in fail-open mode."
            )

        # Warn loudly about recommended guards that are absent.
        # These don't block startup but produce CRITICAL logs so operators
        # notice the degraded security posture immediately.
        _RECOMMENDED_GUARDS = (
            "context_guard",
            "prompt_guard",
            "egress_filter",
            "outbound_filter",
            "canary_tripwire",
            "encoding_detector",
            "clamav_scanner",
            "context_integrity_scorer",
            "envelope_signer",
        )
        for guard_name in _RECOMMENDED_GUARDS:
            if getattr(self, guard_name) is None:
                logger.critical(
                    "SecurityPipeline: recommended guard %r is not configured. "
                    "Security checks for this guard will be SKIPPED. "
                    "This degrades protection -- configure it before production use.",
                    guard_name,
                )

    async def process_inbound(
        self,
        message: str,
        agent_id: str = "default",
        action: str = "send_message",
        source: str = "api",
        metadata: dict[str, Any] | None = None,
        skip_context_guard: bool = False,
    ) -> PipelineResult:
        """Process an inbound message through the full security pipeline."""
        start = time.time()
        self._stats["inbound_total"] += 1
        result = PipelineResult(
            original_message=message,
            sanitized_message=message,
            direction="inbound",
            timestamp=start,
        )

        # Resolve owner status early — used by both ContextGuard and PromptGuard.
        user_id = (metadata or {}).get("user_id", "")
        is_owner = bool(self._owner_user_id and str(user_id) == str(self._owner_user_id))

        # Step 0: ContextGuard — cross-turn injection and repetition detection.
        # Runs before PromptGuard to catch session-level attacks.  Repetition
        # attacks are logged but not blocked (they fire on legitimate structured
        # output).  Only critical/high instruction-injection findings block.
        # Owner messages are logged but never blocked.
        if self.context_guard and not skip_context_guard:
            try:
                attacks = self.context_guard.analyze_message(agent_id, message)
                for attack in attacks:
                    if attack.attack_type == "repetition_attack":
                        logger.info(
                            "ContextGuard: repetition noted (not blocking): %s", attack.description
                        )
                        continue
                    if attack.severity in ("critical", "high"):
                        if is_owner:
                            logger.info(
                                "ContextGuard: owner message would be blocked (%s — %s) — allowing",
                                attack.attack_type,
                                attack.description,
                            )
                            await self.audit_chain.append_owner_bypass(
                                message,
                                "ContextGuard",
                                f"{attack.attack_type} — {attack.description}",
                                metadata,
                            )
                            continue
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = (
                            f"ContextGuard: {attack.attack_type} — {attack.description}"
                        )
                        self._stats["inbound_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            message, "inbound_context_blocked", metadata
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
            except Exception as exc:
                logger.error("ContextGuard error in pipeline: %s", exc)
                if is_owner:
                    logger.warning("ContextGuard error on owner message — allowing through")
                    await self.audit_chain.append_owner_bypass(
                        message, "ContextGuard", f"guard-error: {exc}", metadata
                    )
                else:
                    # Fail closed — block non-owner on error to maintain security posture
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"ContextGuard error: {exc}"
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 0.5: Context Integrity Scoring (C21) — rolling 0.0–1.0 score over
        # the session's segment provenance.  Score < 0.3 blocks non-owner
        # (lockdown threshold); < 0.6 warns but forwards.  Owner exempt,
        # mirroring the ContextGuard policy above.
        if self.context_integrity_scorer and self.context_guard:
            try:
                segments = self.context_guard.get_segment_provenance(agent_id)
                integrity = self.context_integrity_scorer.score_context(
                    session_id=agent_id, segments=segments
                )
                result.integrity_score = integrity.score
                result.integrity_factors = list(integrity.factors)
                if integrity.score < 0.3:
                    if is_owner:
                        logger.info(
                            "ContextIntegrity: owner session %s below lockdown threshold "
                            "(score=%.3f) — allowing",
                            agent_id,
                            integrity.score,
                        )
                        await self.audit_chain.append_owner_bypass(
                            message,
                            "ContextIntegrity",
                            f"score={integrity.score:.3f}, factors={integrity.factors}",
                            metadata,
                        )
                    else:
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = (
                            f"Context integrity critical (score={integrity.score:.3f}, "
                            f"factors={integrity.factors})"
                        )
                        self._stats["inbound_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            message, "inbound_integrity_blocked", metadata
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
                elif integrity.score < 0.6:
                    logger.warning(
                        "ContextIntegrity: low score %.3f for session %s — forwarding",
                        integrity.score,
                        agent_id,
                    )
            except Exception as exc:
                logger.error("ContextIntegrityScorer error in pipeline: %s", exc)
                if is_owner:
                    logger.warning(
                        "ContextIntegrityScorer error on owner message — allowing through"
                    )
                    await self.audit_chain.append_owner_bypass(
                        message, "ContextIntegrity", f"guard-error: {exc}", metadata
                    )
                else:
                    # Fail closed — block non-owner on error
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"ContextIntegrityScorer error: {exc}"
                    self._stats["inbound_blocked"] += 1
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 0.6: Inbound Encoding Bypass Detection (RT-2 mitigation).
        # Runs the EncodingDetector on the INBOUND path — previously it ran
        # outbound-only (Step 1.6 below), so an attacker could encode an
        # injection (base64/hex/rot13/url/unicode + nested layers) to slip past
        # PromptGuard and the injection scanners, then have it decoded
        # downstream.  Here we decode-and-rescan: if the detector surfaces a
        # hidden encoding layer, the fully-decoded text is re-run through
        # PromptGuard and the ToolResultInjectionScanner.  A detected
        # obfuscated injection fails closed (block non-owner); the owner is
        # audited and allowed, mirroring every other inbound guard.
        if self.encoding_detector and not result.blocked:
            try:
                enc = self.encoding_detector.analyze(text=message)
                if enc.detected and enc.cleaned_text and enc.cleaned_text != message:
                    encodings_found = [layer.encoding for layer in enc.layers]
                    result.encoding_detections = encodings_found
                    result.encoding_decoded_segments = len(enc.layers)
                    self._stats["encoding_detected"] += 1
                    decoded_text = enc.cleaned_text

                    injection_patterns: list[str] = []
                    if self.prompt_guard:
                        decoded_scan = self.prompt_guard.scan(decoded_text)
                        if (
                            decoded_scan.blocked
                            or decoded_scan.score >= self.prompt_block_threshold
                        ):
                            injection_patterns.extend(
                                f"decoded_prompt:{p}" for p in decoded_scan.patterns
                            )
                    if self.tool_result_injection_scanner:
                        from gateway.security.tool_result_injection import InjectionAction

                        decoded_inj = self.tool_result_injection_scanner.scan_tool_result(
                            "user_input", decoded_text
                        )
                        if decoded_inj.action == InjectionAction.STRIP:
                            injection_patterns.extend(
                                f"decoded_injection:{p}" for p in decoded_inj.patterns
                            )

                    if injection_patterns:
                        if is_owner:
                            logger.info(
                                "InboundEncoding: owner message hides injection under "
                                "%s (patterns=%s) — allowing",
                                encodings_found,
                                injection_patterns,
                            )
                            await self.audit_chain.append_owner_bypass(
                                message,
                                "InboundEncoding",
                                f"encodings={encodings_found}, patterns={injection_patterns}",
                                metadata,
                            )
                        else:
                            result.action = PipelineAction.BLOCK
                            result.blocked = True
                            result.block_reason = (
                                f"Obfuscated injection detected inbound "
                                f"(encodings={encodings_found}, patterns={injection_patterns})"
                            )
                            self._stats["inbound_blocked"] += 1
                            entry = await self.audit_chain.append_block(
                                message, "inbound_encoded_injection_blocked", metadata
                            )
                            result.audit_entry_id = entry.id
                            result.audit_hash = entry.chain_hash
                            result.processing_time_ms = (time.time() - start) * 1000
                            return result
                    else:
                        logger.info(
                            "InboundEncoding: %d encoding layer(s) decoded from %s "
                            "with no injection payload — forwarding",
                            len(enc.layers),
                            source,
                        )
            except Exception as exc:
                logger.error("InboundEncoding error in pipeline: %s", exc)
                if not is_owner:
                    # Fail closed — block non-owner on detector error.
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"InboundEncoding error: {exc}"
                    self._stats["inbound_blocked"] += 1
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 1: Prompt injection scan
        # user_id / is_owner already resolved above
        if self.prompt_guard:
            scan = self.prompt_guard.scan(message)
            result.prompt_score = scan.score
            result.prompt_patterns = scan.patterns
            if scan.blocked or scan.score >= self.prompt_block_threshold:
                if is_owner:
                    logger.info(
                        f"PromptGuard: owner message would be blocked "
                        f"(score={scan.score}, patterns={scan.patterns}) — allowing"
                    )
                    await self.audit_chain.append_owner_bypass(
                        message,
                        "PromptGuard",
                        f"score={scan.score}, patterns={scan.patterns}",
                        metadata,
                    )
                    # Owner messages continue through the pipeline
                else:
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = (
                        f"Prompt injection detected (score={scan.score}, patterns={scan.patterns})"
                    )
                    self._stats["inbound_blocked"] += 1
                    # Still audit blocked messages
                    entry = await self.audit_chain.append_block(
                        message, "inbound_blocked", metadata
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 1.1: HeuristicClassifier — secondary signal in the uncertain zone (0.3–0.8).
        # Only invoked when PromptGuard score is uncertain; never the sole blocking signal.
        if self.heuristic_classifier and not result.blocked:
            if 0.3 <= result.prompt_score <= 0.8:
                try:
                    hc_result = self.heuristic_classifier.classify(message)
                    if hc_result.is_injection:
                        if is_owner:
                            logger.info(
                                "HeuristicClassifier: owner injection (prob=%.2f) — allowing",
                                hc_result.probability,
                            )
                            await self.audit_chain.append_owner_bypass(
                                message,
                                "HeuristicClassifier",
                                f"prob={hc_result.probability:.2f}",
                                metadata,
                            )
                        else:
                            result.action = PipelineAction.BLOCK
                            result.blocked = True
                            result.block_reason = (
                                f"HeuristicClassifier: injection detected "
                                f"(prob={hc_result.probability:.2f})"
                            )
                            self._stats["inbound_blocked"] += 1
                            entry = await self.audit_chain.append_block(
                                message, "inbound_heuristic_blocked", metadata
                            )
                            result.audit_entry_id = entry.id
                            result.audit_hash = entry.chain_hash
                            result.processing_time_ms = (time.time() - start) * 1000
                            return result
                    elif hc_result.is_uncertain:
                        logger.warning(
                            "HeuristicClassifier: uncertain (prob=%.2f) from %s — allowing with log",
                            hc_result.probability,
                            source,
                        )
                except Exception as exc:
                    logger.error("HeuristicClassifier error: %s", exc)

        # Step 1.5: Inbound injection scan — CVE-2026-30741 mitigation.
        # Applies the ToolResultInjectionScanner pattern set (12 rules + encoded injection
        # + unicode obfuscation) to inbound messages, closing the asymmetry where only
        # tool results were scanned for these attack classes.
        if self.tool_result_injection_scanner and not result.blocked:
            try:
                inj_result = self.tool_result_injection_scanner.scan_tool_result(
                    "user_input", result.sanitized_message
                )
                from gateway.security.tool_result_injection import InjectionAction

                if inj_result.action == InjectionAction.STRIP:
                    if is_owner:
                        logger.info(
                            "InboundInjectionScanner: owner message flagged (patterns=%s) — allowing",
                            inj_result.patterns,
                        )
                        await self.audit_chain.append_owner_bypass(
                            message,
                            "InboundInjectionScanner",
                            f"patterns={inj_result.patterns}",
                            metadata,
                        )
                    else:
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = (
                            f"Inbound injection detected (patterns={inj_result.patterns})"
                        )
                        self._stats["inbound_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            message, "inbound_injection_blocked", metadata
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
                elif inj_result.action == InjectionAction.WARN:
                    logger.warning(
                        "InboundInjectionScanner: warning-level patterns in inbound from %s: %s",
                        source,
                        inj_result.patterns,
                    )
            except Exception as exc:
                logger.error("InboundInjectionScanner error: %s", exc)

        # Step 1.6: Inbound command injection scan — CVE-2026-34425 mitigation.
        # Applies XMLLeakFilter C32 shell metachar patterns to inbound messages so
        # piped/subshell constructs are caught on the way in, not only on outbound.
        if self.xml_leak_filter and not result.blocked:
            try:
                c32_result = self.xml_leak_filter.scan_command_injection(result.sanitized_message)
                if c32_result.filter_applied:
                    if is_owner:
                        logger.info(
                            "C32InboundScan: owner message contains shell patterns (%s) — allowing",
                            c32_result.removed_items,
                        )
                        await self.audit_chain.append_owner_bypass(
                            message,
                            "C32InboundScan",
                            f"patterns={c32_result.removed_items}",
                            metadata,
                        )
                    else:
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = f"Command injection pattern detected inbound: {c32_result.removed_items}"
                        self._stats["inbound_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            message, "inbound_cmd_injection_blocked", metadata
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
            except Exception as exc:
                logger.error("C32InboundScan error: %s", exc)

        # Step 2: PII sanitization — owner (FULL-trust) queries are exempt so the
        # owner's own spoken/typed request is not garbled before the agent can act on it.
        # Non-owner traffic is still scrubbed at the 0.9 Presidio confidence floor;
        # the detector and threshold are untouched (gateway/ingest_api/config.py:39-40).
        # Mirrors the is_owner exemption already present on every other inbound guard
        # (ContextGuard :434, ContextIntegrity :479, PromptGuard :529, etc.).
        if self.pii_sanitizer and not is_owner:
            sanitize_result = await self.pii_sanitizer.sanitize(message)
            result.sanitized_message = sanitize_result.sanitized_content
            result.pii_redactions = sanitize_result.entity_types_found
            result.pii_redaction_count = len(sanitize_result.redactions)
            if sanitize_result.redactions:
                self._stats["inbound_sanitized"] += 1
                self._stats["pii_redactions_total"] += len(sanitize_result.redactions)
        elif self.pii_sanitizer and is_owner:
            logger.info(
                "PII sanitize: owner inbound query exempt — not redacting (source=%s agent=%s)",
                source,
                agent_id,
            )

        # Step 2.5: ClamAV inline scan — check base64-encoded binary content for malware.
        # Only triggered when message contains a plausible base64 payload (>256 decoded bytes).
        # Fail-open: if clamd is unavailable, log CRITICAL and allow (availability > detection here).
        if self.clamav_scanner and not result.blocked:
            import base64
            import re as _re

            _b64_chunks = _re.findall(
                r"(?:[A-Za-z0-9+/]{4}){64,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?",
                result.sanitized_message,
            )
            for _chunk in _b64_chunks:
                try:
                    _decoded = base64.b64decode(_chunk)
                    if len(_decoded) >= 256:
                        _scan = await self.clamav_scanner(_decoded)
                        if _scan.get("error"):
                            logger.critical(
                                "ClamAV scan_bytes failed (fail-open): %s", _scan["error"]
                            )
                        elif _scan.get("infected_count", 0) > 0:
                            _sigs = [f["signature"] for f in _scan.get("infected_files", [])]
                            result.action = PipelineAction.BLOCK
                            result.blocked = True
                            result.block_reason = f"ClamAV: malware detected — {_sigs}"
                            self._stats["inbound_blocked"] += 1
                            entry = await self.audit_chain.append_block(
                                message,
                                "inbound_clamav_blocked",
                                {**(metadata or {}), "signatures": _sigs},
                            )
                            result.audit_entry_id = entry.id
                            result.audit_hash = entry.chain_hash
                            result.processing_time_ms = (time.time() - start) * 1000
                            logger.critical(
                                "ClamAV BLOCKED inbound from agent=%s: signatures=%s",
                                agent_id,
                                _sigs,
                            )
                            return result
                except Exception:
                    pass  # Bad base64 or scan error — skip this chunk

        # Step 3: Trust level check
        if self.trust_manager:
            allowed = self.trust_manager.is_action_allowed(agent_id, action)
            trust_info = self.trust_manager.get_trust(agent_id)
            result.trust_allowed = allowed
            if trust_info:
                result.trust_level = int(trust_info[0])
            if not allowed:
                result.action = PipelineAction.BLOCK
                result.blocked = True
                result.block_reason = f"Trust level insufficient for action {action}"
                self._stats["inbound_blocked"] += 1
                entry = await self.audit_chain.append_block(
                    result.sanitized_message, "inbound_trust_denied", metadata
                )
                result.audit_entry_id = entry.id
                result.audit_hash = entry.chain_hash
                result.processing_time_ms = (time.time() - start) * 1000
                return result

        # Step 4: Approval queue check
        if self.approval_queue and action in self.approval_actions:
            result.action = PipelineAction.QUEUE_APPROVAL
            result.queued_for_approval = True
            self._stats["inbound_queued"] += 1
            entry = self.audit_chain.append(result.sanitized_message, "inbound_queued", metadata)
            result.audit_entry_id = entry.id
            result.audit_hash = entry.chain_hash
            result.processing_time_ms = (time.time() - start) * 1000
            return result

        # Step 5: Audit log and forward
        result.action = PipelineAction.FORWARD
        entry = self.audit_chain.append(result.sanitized_message, "inbound", metadata)
        result.audit_entry_id = entry.id
        result.audit_hash = entry.chain_hash
        result.processing_time_ms = (time.time() - start) * 1000
        return result

    async def process_outbound(
        self,
        response: str,
        agent_id: str = "default",
        destination_urls: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        user_trust_level: str = "UNTRUSTED",
        source: str = "api",
    ) -> PipelineResult:
        """Process an outbound response through the security pipeline."""
        start = time.time()
        self._stats["outbound_total"] += 1
        result = PipelineResult(
            original_message=response,
            sanitized_message=response,
            direction="outbound",
            timestamp=start,
        )

        # Step 0: Strip Claude XML internal blocks
        if self.pii_sanitizer:
            filtered_response, xml_filtered = self.pii_sanitizer.filter_xml_blocks(response)
            if xml_filtered:
                result.sanitized_message = filtered_response
                response = filtered_response

        # Step 1: PII sanitization on outbound
        if self.pii_sanitizer:
            sanitize_result = await self.pii_sanitizer.sanitize(response)
            result.sanitized_message = sanitize_result.sanitized_content
            result.pii_redactions = sanitize_result.entity_types_found
            result.pii_redaction_count = len(sanitize_result.redactions)
            if sanitize_result.redactions:
                self._stats["outbound_sanitized"] += 1
                self._stats["pii_redactions_total"] += len(sanitize_result.redactions)

        # Step 1.5: Outbound Information Filter (NEW)
        filter_result: Optional[FilterResult] = None
        if self.outbound_filter:
            filter_result = self.outbound_filter.filter_response(
                response_text=result.sanitized_message,
                user_trust_level=user_trust_level,
                source=source,
            )

            result.sanitized_message = filter_result.filtered_text
            result.info_filter_redactions = filter_result.categories_found
            result.info_filter_redaction_count = filter_result.redaction_count
            result.info_disclosure_risk = filter_result.risk_level

            if filter_result.matches:
                self._stats["outbound_info_filtered"] += 1
                self._stats["info_redactions_total"] += filter_result.redaction_count

                # Log high-risk responses for additional review
                if filter_result.risk_level == "high":
                    logger.warning(
                        f"High-density information disclosure blocked: "
                        f"{len(filter_result.matches)} matches, categories={filter_result.categories_found}, "
                        f"trust={user_trust_level}, source={source}"
                    )

        # Escalate fabricated security notices: REDACT → BLOCK.
        # If the bot hallucinated a fake "AGENTSHROUD blocked X" message, redacting
        # the substring is insufficient — the surrounding context is still deceptive.
        # Replace the entire response with a clean fallback and block delivery.
        if filter_result is not None and filter_result.matches:
            fabricated = [
                m for m in filter_result.matches if m.pattern_name == "fabricated_security_notice"
            ]
            if fabricated:
                result.action = PipelineAction.BLOCK
                result.blocked = True
                result.block_reason = "Fabricated security notice detected in agent response"
                result.sanitized_message = (
                    "I'm sorry, I wasn't able to process that request. "
                    "Could you rephrase your question?"
                )
                self._stats["outbound_blocked"] += 1
                entry = await self.audit_chain.append_block(
                    response, "outbound_fabricated_blocked", metadata
                )
                result.audit_entry_id = entry.id
                result.audit_hash = entry.chain_hash
                result.processing_time_ms = (time.time() - start) * 1000
                logger.warning(
                    "Fabricated security notice blocked from %s: %d match(es)",
                    source,
                    len(fabricated),
                )
                return result

        # Step 1.55: PromptProtection — system prompt / architecture disclosure prevention.
        # Applied after OutboundInfoFilter. Redacts additional sensitive content;
        # blocks response if risk_score is critically high (>100) for non-owners.
        if self.prompt_protection:
            user_id_pp = (metadata or {}).get("user_id", "")
            is_owner_pp = bool(
                user_trust_level == "FULL"
                or (self._owner_user_id and str(user_id_pp) == str(self._owner_user_id))
            )
            if not is_owner_pp:
                try:
                    pp_result = self.prompt_protection.scan_response(result.sanitized_message)
                    if pp_result.redactions_made:
                        result.sanitized_message = pp_result.redacted_text
                        logger.info(
                            "PromptProtection: %d redaction(s) applied, risk_score=%.1f (source=%s)",
                            len(pp_result.redactions_made),
                            pp_result.risk_score,
                            source,
                        )
                    if pp_result.risk_score > 100:
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = f"PromptProtection: critical disclosure risk_score={pp_result.risk_score}"
                        self._stats["outbound_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            result.sanitized_message, "outbound_pp_blocked", metadata
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
                except Exception as exc:
                    logger.error("PromptProtection error: %s", exc)

        # Step 1.6: Encoding Bypass Detection
        if self.encoding_detector:
            encoding_result = self.encoding_detector.analyze(
                text=result.sanitized_message,
            )

            # Re-scan decoded content with previous filters if encoding was detected
            if encoding_result.detected:
                encodings_found = [layer.encoding for layer in encoding_result.layers]
                result.encoding_detections = encodings_found
                result.encoding_decoded_segments = len(encoding_result.layers)
                self._stats["encoding_detected"] += 1

                # Update the message to the fully decoded version for further processing
                result.sanitized_message = encoding_result.cleaned_text

                logger.info(
                    f"Encoding bypass detected: {len(encodings_found)} methods, "
                    f"{len(encoding_result.layers)} segments decoded from {source}"
                )

        # Step 1.7: Canary Tripwire (Final Defense)
        if self.canary_tripwire:
            tripwire_result = self.canary_tripwire.scan_response(
                response_text=result.sanitized_message, source=source
            )

            if tripwire_result.is_blocked:
                # BLOCK the entire response - no redaction, complete block
                result.action = PipelineAction.BLOCK
                result.blocked = True
                result.canary_blocked = True
                result.block_reason = (
                    f"Canary tripwire triggered: {len(tripwire_result.detections)} detections"
                )
                result.canary_detections = tripwire_result.detections
                self._stats["canary_blocked"] += 1

                # Audit the block (guaranteed persistence — canary triggers are critical)
                entry = await self.audit_chain.append_block(
                    f"CANARY_BLOCKED: {len(tripwire_result.detections)} detections",
                    "outbound_canary_blocked",
                    {**(metadata or {}), "canary_methods": tripwire_result.scan_methods_used},
                )
                result.audit_entry_id = entry.id
                result.audit_hash = entry.chain_hash
                result.processing_time_ms = (time.time() - start) * 1000

                # Log critical alert
                logger.critical(
                    f"CANARY TRIPWIRE BLOCKED RESPONSE from {source}: "
                    f"{len(tripwire_result.detections)} canary detections, "
                    f"methods={tripwire_result.scan_methods_used}"
                )

                return result

        # Step 1.75: Enhanced tool result sanitizer — strip exfil patterns from outbound content
        if self.enhanced_tool_sanitizer:
            try:
                sanitized = self.enhanced_tool_sanitizer.sanitize(result.sanitized_message)
                if sanitized != result.sanitized_message:
                    logger.info(
                        "EnhancedToolResultSanitizer: content modified (exfil/leak patterns stripped)"
                    )
                    result.sanitized_message = sanitized
            except Exception as exc:
                logger.error("EnhancedToolResultSanitizer error: %s", exc)
                # Fail-closed for non-owner: block if security module crashes
                is_owner_outbound = bool(
                    self._owner_user_id
                    and metadata
                    and str(metadata.get("user_id", "")) == str(self._owner_user_id)
                )
                if not is_owner_outbound:
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = (
                        f"Security module error (EnhancedToolResultSanitizer): {exc}"
                    )
                    self._stats["outbound_blocked"] += 1
                    entry = self.audit_chain.append(
                        f"MODULE_ERROR: EnhancedToolResultSanitizer: {exc}",
                        "outbound_module_error",
                        metadata,
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 1.755: Module 28 — Differential PII Detection on tool results.
        # IEC 62443 FR3: a lower confidence floor (0.7) is applied when the
        # outbound message originates from a tool result, catching adversarially
        # formatted exfiltration that evades the standard 0.9-floor PII pass.
        # Runs only when a tool_name is present in metadata (i.e. this is a
        # tool-result response, not a direct LLM reply).
        if self.differential_pii_detector and not result.blocked:
            tool_name = (metadata or {}).get("tool_name", "")
            if tool_name:
                try:
                    diff_pii_report = self.differential_pii_detector.scan_tool_result(
                        tool_name=tool_name,
                        content=result.sanitized_message,
                    )
                    if diff_pii_report.has_pii:
                        result.sanitized_message = diff_pii_report.redacted_content
                        self._stats["outbound_sanitized"] += 1
                        self._stats["pii_redactions_total"] += len(diff_pii_report.hits)
                        logger.info(
                            "DifferentialPIIDetector: %d hit(s) at floor=%.2f in tool=%r — redacted",
                            len(diff_pii_report.hits),
                            diff_pii_report.confidence_floor_used,
                            tool_name,
                        )
                    if diff_pii_report.adversarial_patterns_detected > 0:
                        logger.warning(
                            "DifferentialPIIDetector: %d adversarial pattern(s) normalized in tool=%r",
                            diff_pii_report.adversarial_patterns_detected,
                            tool_name,
                        )
                        self.audit_chain.append(
                            f"ADVERSARIAL_PII: tool={tool_name} patterns={diff_pii_report.adversarial_patterns_detected}",
                            "outbound_adversarial_pii",
                            metadata,
                        )
                except Exception as exc:
                    logger.error("DifferentialPIIDetector error: %s", exc)

        # Step 1.76: PromptGuard tool-result scan — block indirect prompt injection
        # embedded in tool outputs (web pages, file reads, API responses).
        # CVE-2026-31045 fix: tool results are a request-side injection vector.
        #
        # Trust gate: FULL-trust (owner-authenticated) responses are audited but
        # NOT hard-blocked. The consumer is the owner (voice/chat), not a downstream
        # LLM tool-loop, so the CVE-2026-31045 injection threat model does not apply.
        # All non-FULL trust levels keep the hard block. Detection and audit chain
        # entries run for everyone — forensics are never suppressed.
        if self.prompt_guard:
            try:
                tool_result_scan = self.prompt_guard.scan_tool_result(result.sanitized_message)
                if tool_result_scan.blocked:
                    # Always audit — detection is recorded regardless of trust level.
                    entry = self.audit_chain.append(
                        f"TOOL_RESULT_INJECTION: score={tool_result_scan.score:.2f} "
                        f"patterns={tool_result_scan.patterns[:3]}",
                        "outbound_tool_result_injection",
                        metadata,
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    if user_trust_level == "FULL":
                        logger.warning(
                            "PromptGuard tool_result injection detected but allowed "
                            "for FULL-trust source %s: score=%.2f patterns=%s",
                            source,
                            tool_result_scan.score,
                            tool_result_scan.patterns[:3],
                        )
                    else:
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = (
                            f"PromptGuard(tool_result): indirect injection detected "
                            f"(score={tool_result_scan.score:.2f}, "
                            f"patterns={tool_result_scan.patterns[:3]})"
                        )
                        self._stats["outbound_blocked"] += 1
                        result.processing_time_ms = (time.time() - start) * 1000
                        logger.warning(
                            "PromptGuard blocked tool result injection from %s: "
                            "score=%.2f patterns=%s",
                            source,
                            tool_result_scan.score,
                            tool_result_scan.patterns[:3],
                        )
                        return result
                elif tool_result_scan.score > 0:
                    logger.debug(
                        "PromptGuard tool_result scan: score=%.2f patterns=%s (allowed)",
                        tool_result_scan.score,
                        tool_result_scan.patterns,
                    )
            except Exception as exc:
                logger.error("PromptGuard tool_result scan error: %s", exc)

        # Step 1.8: OutputCanary — check for leaked canary tokens in responses
        if self.output_canary:
            try:
                canary_result = self.output_canary.check_response(
                    agent_id, result.sanitized_message
                )
                if canary_result.canary_detected:
                    logger.critical(
                        "OutputCanary: canary token detected in response from %s — "
                        "method=%s risk=%s incident=%s",
                        source,
                        canary_result.detection_method,
                        canary_result.risk_level,
                        canary_result.incident_id,
                    )
                    # High risk detections block; medium/low are logged only
                    if canary_result.risk_level in ("high", "critical"):
                        result.action = PipelineAction.BLOCK
                        result.blocked = True
                        result.block_reason = (
                            f"OutputCanary: leaked canary token (risk={canary_result.risk_level})"
                        )
                        self._stats["canary_blocked"] += 1
                        entry = await self.audit_chain.append_block(
                            f"CANARY_DETECTED: {canary_result.incident_id}",
                            "outbound_canary_leak",
                            metadata,
                        )
                        result.audit_entry_id = entry.id
                        result.audit_hash = entry.chain_hash
                        result.processing_time_ms = (time.time() - start) * 1000
                        return result
            except Exception as exc:
                logger.error("OutputCanary error: %s", exc)
                # Fail-closed for non-owner: block if security module crashes
                is_owner_outbound = bool(
                    self._owner_user_id
                    and metadata
                    and str(metadata.get("user_id", "")) == str(self._owner_user_id)
                )
                if not is_owner_outbound:
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"Security module error (OutputCanary): {exc}"
                    self._stats["outbound_blocked"] += 1
                    entry = self.audit_chain.append(
                        f"MODULE_ERROR: OutputCanary: {exc}",
                        "outbound_module_error",
                        metadata,
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 1.85: KeyLeakDetector — stored credential values must never
        # leave the gateway. Leaks are redacted (vault design), audited, and
        # surfaced in the final audit entry metadata.
        if self.key_leak_detector and not result.blocked:
            try:
                leak_scan = self.key_leak_detector.scan_outbound(result.sanitized_message)
                if leak_scan.leak_detected:
                    result.sanitized_message = self.key_leak_detector.vault.redact(
                        result.sanitized_message
                    )
                    self._stats["outbound_sanitized"] += 1
                    metadata = {
                        **(metadata or {}),
                        "key_leak_names": leak_scan.leaked_key_names,
                    }
                    logger.critical(
                        "KeyLeakDetector: credential value(s) %s detected in outbound "
                        "response from %s — redacted",
                        leak_scan.leaked_key_names,
                        source,
                    )
                    self.audit_chain.append(
                        f"KEY_LEAK: {leak_scan.leaked_key_names}",
                        "outbound_key_leak",
                        metadata,
                    )
            except Exception as exc:
                logger.error("KeyLeakDetector error: %s", exc)
                # Fail-closed for non-owner: block if security module crashes
                is_owner_outbound = bool(
                    self._owner_user_id
                    and metadata
                    and str(metadata.get("user_id", "")) == str(self._owner_user_id)
                )
                if not is_owner_outbound:
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"Security module error (KeyLeakDetector): {exc}"
                    self._stats["outbound_blocked"] += 1
                    entry = self.audit_chain.append(
                        f"MODULE_ERROR: KeyLeakDetector: {exc}",
                        "outbound_module_error",
                        metadata,
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 1.9: Output Schema Enforcement (C25)
        if self.output_schema_enforcer and not result.blocked:
            try:
                schema_result = self.output_schema_enforcer.validate(result.sanitized_message)
                if schema_result.violations:
                    result.sanitized_message = schema_result.sanitized_output
                    logger.info(
                        "OutputSchemaEnforcer: %d violation(s) redacted from response",
                        len(schema_result.violations),
                    )
            except Exception as exc:
                logger.error("OutputSchemaEnforcer error: %s", exc)

        # Step 2: Egress filter
        if self.egress_filter and destination_urls:
            for url in destination_urls:
                if hasattr(self.egress_filter, "check_async"):
                    attempt = await self.egress_filter.check_async(
                        agent_id, url, tool_name="outbound_response"
                    )
                else:
                    attempt = self.egress_filter.check(agent_id, url)
                if attempt.action.value == "deny":
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"Egress blocked: {url} — {attempt.rule}"
                    self._stats["outbound_blocked"] += 1
                    entry = await self.audit_chain.append_block(
                        result.sanitized_message, "outbound_blocked", metadata
                    )
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 2.5: Envelope signing (C46) — HMAC attestation of the final
        # sanitized response.  Attestation, not a gate: signing failure logs an
        # error but never blocks delivery.
        envelope_timestamp = 0.0
        if self.envelope_signer:
            try:
                tool_name = (metadata or {}).get("tool_name", "")
                if tool_name:
                    envelope = self.envelope_signer.wrap_tool_result(
                        result.sanitized_message, tool_name
                    )
                else:
                    envelope = self.envelope_signer.sign(
                        result.sanitized_message, issuer=f"agent:{agent_id}"
                    )
                result.envelope_id = envelope.instruction_id
                result.envelope_signature = envelope.signature
                envelope_timestamp = envelope.timestamp
            except Exception as exc:
                logger.error("EnvelopeSigner error (non-blocking): %s", exc)

        # Step 3: Audit and return
        result.action = PipelineAction.FORWARD
        audit_metadata = metadata
        if result.envelope_id:
            audit_metadata = dict(metadata or {})
            audit_metadata["envelope_id"] = result.envelope_id
            audit_metadata["envelope_signature"] = result.envelope_signature
            audit_metadata["envelope_timestamp"] = envelope_timestamp
        entry = self.audit_chain.append(result.sanitized_message, "outbound", audit_metadata)
        result.audit_entry_id = entry.id
        result.audit_hash = entry.chain_hash
        result.processing_time_ms = (time.time() - start) * 1000
        return result

    def get_stats(self) -> dict[str, Any]:
        return {
            **self._stats,
            "audit_chain_length": len(self.audit_chain),
            "audit_chain_valid": self.audit_chain.verify_chain()[0],
        }

    def verify_audit_chain(self) -> tuple[bool, str]:
        return self.audit_chain.verify_chain()

    def set_global_mode(self, mode: str) -> None:
        """Set global observatory mode for all security modules.

        Args:
            mode: "monitor" or "enforce"
        """
        # Update components that support mode switching
        if hasattr(self.pii_sanitizer, "set_mode"):
            self.pii_sanitizer.set_mode(mode)

        if hasattr(self.prompt_guard, "set_mode"):
            self.prompt_guard.set_mode(mode)

        if hasattr(self.egress_filter, "set_mode"):
            self.egress_filter.set_mode(mode)

        # Update prompt guard thresholds based on mode.
        # Original thresholds are saved on first monitor switch so they can be
        # restored exactly when returning to enforce — avoids overwriting any
        # custom values set at PromptGuard initialization time.
        if self.prompt_guard:
            if mode == "monitor":
                if not hasattr(self, "_pg_orig_block_threshold"):
                    self._pg_orig_block_threshold = self.prompt_guard.block_threshold
                    self._pg_orig_warn_threshold = self.prompt_guard.warn_threshold
                self.prompt_guard.block_threshold = 999.0
                self.prompt_guard.warn_threshold = 999.0
            else:
                # Restore originals if saved; fall back to defaults if not
                self.prompt_guard.block_threshold = getattr(self, "_pg_orig_block_threshold", 0.8)
                self.prompt_guard.warn_threshold = getattr(self, "_pg_orig_warn_threshold", 0.4)
