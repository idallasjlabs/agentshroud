"""
Proxy Pipeline — all messages flow through security checks.

Inbound: prompt guard → PII sanitizer → trust check → audit → forward
Outbound: PII sanitizer → egress filter → audit → return
"""
from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

logger = logging.getLogger("secureclaw.proxy.pipeline")


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

    def __init__(self):
        self._entries: list[AuditChainEntry] = []
        self._last_hash: str = self.GENESIS_HASH

    def append(self, content: str, direction: str, metadata: dict[str, Any] | None = None) -> AuditChainEntry:
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
        self._last_hash = chain_hash
        return entry

    def verify_chain(self) -> tuple[bool, str]:
        """Verify the integrity of the entire hash chain.
        Returns (valid, error_message)."""
        if not self._entries:
            return True, "Empty chain"
        prev_hash = self.GENESIS_HASH
        for i, entry in enumerate(self._entries):
            if entry.previous_hash != prev_hash:
                return False, f"Entry {i} ({entry.id}): previous_hash mismatch"
            expected_input = f"{entry.previous_hash}:{entry.content_hash}:{entry.direction}:{entry.timestamp}"
            expected_hash = hashlib.sha256(expected_input.encode()).hexdigest()
            if entry.chain_hash != expected_hash:
                return False, f"Entry {i} ({entry.id}): chain_hash mismatch (tampered)"
            prev_hash = entry.chain_hash
        return True, f"Chain valid ({len(self._entries)} entries)"

    @property
    def entries(self) -> list[AuditChainEntry]:
        return list(self._entries)

    @property
    def last_hash(self) -> str:
        return self._last_hash

    def __len__(self) -> int:
        return len(self._entries)


class SecurityPipeline:
    """Main security pipeline that all messages pass through.

    Wires together: PromptGuard, PIISanitizer, TrustManager,
    EgressFilter, ApprovalQueue, and AuditChain.
    """

    def __init__(
        self,
        prompt_guard=None,
        pii_sanitizer=None,
        trust_manager=None,
        egress_filter=None,
        approval_queue=None,
        prompt_block_threshold: float = 0.8,
        approval_actions: list[str] | None = None,
    ):
        self.prompt_guard = prompt_guard
        self.pii_sanitizer = pii_sanitizer
        self.trust_manager = trust_manager
        self.egress_filter = egress_filter
        self.approval_queue = approval_queue
        self.prompt_block_threshold = prompt_block_threshold
        self.approval_actions = approval_actions or [
            "execute_command", "delete_file", "admin_action", "install_package"
        ]
        self.audit_chain = AuditChain()
        self._stats = {
            "inbound_total": 0,
            "inbound_blocked": 0,
            "inbound_sanitized": 0,
            "inbound_queued": 0,
            "outbound_total": 0,
            "outbound_sanitized": 0,
            "outbound_blocked": 0,
            "pii_redactions_total": 0,
        }

    async def process_inbound(
        self,
        message: str,
        agent_id: str = "default",
        action: str = "send_message",
        source: str = "api",
        metadata: dict[str, Any] | None = None,
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

        # Step 1: Prompt injection scan
        if self.prompt_guard:
            scan = self.prompt_guard.scan(message)
            result.prompt_score = scan.score
            result.prompt_patterns = scan.patterns
            if scan.blocked or scan.score >= self.prompt_block_threshold:
                result.action = PipelineAction.BLOCK
                result.blocked = True
                result.block_reason = f"Prompt injection detected (score={scan.score}, patterns={scan.patterns})"
                self._stats["inbound_blocked"] += 1
                # Still audit blocked messages
                entry = self.audit_chain.append(message, "inbound_blocked", metadata)
                result.audit_entry_id = entry.id
                result.audit_hash = entry.chain_hash
                result.processing_time_ms = (time.time() - start) * 1000
                return result

        # Step 2: PII sanitization
        if self.pii_sanitizer:
            sanitize_result = await self.pii_sanitizer.sanitize(message)
            result.sanitized_message = sanitize_result.sanitized_content
            result.pii_redactions = sanitize_result.entity_types_found
            result.pii_redaction_count = len(sanitize_result.redactions)
            if sanitize_result.redactions:
                self._stats["inbound_sanitized"] += 1
                self._stats["pii_redactions_total"] += len(sanitize_result.redactions)

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
                entry = self.audit_chain.append(result.sanitized_message, "inbound_trust_denied", metadata)
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

        # Step 1: PII sanitization on outbound
        if self.pii_sanitizer:
            sanitize_result = await self.pii_sanitizer.sanitize(response)
            result.sanitized_message = sanitize_result.sanitized_content
            result.pii_redactions = sanitize_result.entity_types_found
            result.pii_redaction_count = len(sanitize_result.redactions)
            if sanitize_result.redactions:
                self._stats["outbound_sanitized"] += 1
                self._stats["pii_redactions_total"] += len(sanitize_result.redactions)

        # Step 2: Egress filter
        if self.egress_filter and destination_urls:
            for url in destination_urls:
                attempt = self.egress_filter.check(agent_id, url)
                if attempt.action.value == "deny":
                    result.action = PipelineAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"Egress blocked: {url} — {attempt.rule}"
                    self._stats["outbound_blocked"] += 1
                    entry = self.audit_chain.append(result.sanitized_message, "outbound_blocked", metadata)
                    result.audit_entry_id = entry.id
                    result.audit_hash = entry.chain_hash
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result

        # Step 3: Audit and return
        result.action = PipelineAction.FORWARD
        entry = self.audit_chain.append(result.sanitized_message, "outbound", metadata)
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
