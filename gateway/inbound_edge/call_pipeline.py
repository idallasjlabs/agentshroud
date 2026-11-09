# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""The gateway-side pipeline every hosted-agent tool call runs through (SCRUM-212).

Order (docs/inbound-mcp-edge/01-plan.md §5)::

    authN → profile + tool ACL → JSON Schema → P3 limits/lockdown → P0 injection
    → approval (writes) → dispatch → P2 canaries → DLP + credential scrub
    → size cap → audit + event

Deviation from the brief, deliberately: rate limits, budgets and concurrency (P3)
run *before* P0, so a flood of junk costs a counter increment, not a PromptGuard
scan of every string. Lockdown state is read at the same point. Denials are
audited either way.

Everything that can fail closed does: an exception anywhere returns a denial,
never a partial result. Monitor mode (per vendor, needs ``monitor_ack``) relaxes
only the P0 verdict and DLP blocking — authN, ACL, schema, limits and approvals
are always enforced.

The principal is ``edge:<vendor>:<client>`` and is never resolved to the owner,
so the pipeline's owner exemption cannot apply to a hosted agent.

IEC 62443 alignment: FR1 (authN), FR2 (use control, approvals), FR3 (integrity of
inputs), FR4 (confidentiality of outputs: DLP, canaries), FR6 (audit + timely
alerting), FR7 (availability: limits and lockdown).
"""

import hashlib
import json
import logging
import time
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Awaitable, Callable, Deque, Dict, List, Optional, Protocol, Set, Tuple

import jsonschema

from gateway.inbound_edge.approvals import (
    ApprovalContext,
    ApprovalDenied,
    ApprovalPending,
    EdgeApprovals,
)
from gateway.inbound_edge.descriptors import TOOL_DESCRIPTORS, canonical_bytes, mcp_tool
from gateway.inbound_edge.edge_jwt import EdgePrincipal, TokenRejected, TokenService
from gateway.inbound_edge.profiles import VendorProfile
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.event_bus import make_event
from gateway.security.input_normalizer import normalize_input
from gateway.security.progressive_lockdown import LockdownLevel

logger = logging.getLogger("agentshroud.inbound_edge.call_pipeline")

# Per-tool response caps on top of the vendor's max_response_bytes.
TOOL_RESPONSE_CAPS = {"lab_search": 65_536}
VENDOR_DISABLE_AFTER_SUSPENDED_CLIENTS = 2
# Denials that count towards the principal's lockdown level.
_STRIKES = {"prompt_injection", "schema", "tool_not_permitted", "rate_limited", "canary", "dlp"}
_LADDER = {
    LockdownLevel.ALERT: "throttle",
    LockdownLevel.ESCALATED: "writes_disabled",
    LockdownLevel.SUSPENDED: "client_revoked",
}


class Facade(Protocol):
    name: str
    target: str
    requires_local_agent: Optional[str]

    async def run(self, args: Dict[str, Any], call: "CallContext") -> Dict[str, Any]: ...


@dataclass
class CallContext:
    request_id: str
    principal: EdgePrincipal
    profile: VendorProfile


@dataclass
class EdgeDeps:
    profiles: Dict[str, VendorProfile]
    tokens: TokenService
    store: EdgeStore
    approvals: EdgeApprovals
    audit: Any  # gateway.security.audit_store.AuditStore
    emit: Callable[[Any], Awaitable[None]]
    prompt_guard: Any
    encoding_detector: Any
    lockdown: Any  # gateway.security.progressive_lockdown.ProgressiveLockdown
    tripwire: Any  # gateway.security.canary_tripwire.CanaryTripwire
    sanitizer: Any  # gateway.ingest_api.sanitizer.PIISanitizer
    facades: Dict[str, Facade]
    local_agents: Set[str]
    heuristic: Any = None
    tool_chain: Any = None
    clock: Callable[[], float] = time.time


class _Denied(Exception):
    def __init__(self, reason: str, message: str):
        super().__init__(message)
        self.reason = reason


@dataclass
class VendorStats:
    """In-memory counters for the Command Center (reset on restart)."""

    calls: int = 0
    ok: int = 0
    denials: Dict[str, int] = field(default_factory=lambda: defaultdict(int))
    dlp_hits: int = 0
    canary_hits: int = 0
    pending_approvals: int = 0
    last_call: Optional[float] = None
    recent: Deque[Dict[str, Any]] = field(default_factory=lambda: deque(maxlen=50))


class _Window:
    """Sliding one-minute window counter keyed by principal or vendor."""

    def __init__(self) -> None:
        self._events: Dict[str, Deque[float]] = defaultdict(deque)

    def hit(self, key: str, limit: int, now: float) -> bool:
        q = self._events[key]
        while q and q[0] <= now - 60.0:
            q.popleft()
        if len(q) >= limit:
            return False
        q.append(now)
        return True


def _result(payload: Any, error: bool = False) -> Dict[str, Any]:
    text = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False)
    out: Dict[str, Any] = {"content": [{"type": "text", "text": text}], "isError": error}
    if not error and isinstance(payload, dict):
        out["structuredContent"] = payload
    return out


def _string_leaves(value: Any) -> List[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for v in value.values() for s in _string_leaves(v)]
    if isinstance(value, list):
        return [s for v in value for s in _string_leaves(v)]
    return []


class EdgeCallPipeline:
    def __init__(self, deps: EdgeDeps):
        self.d = deps
        self.stats: Dict[str, VendorStats] = defaultdict(VendorStats)
        self._client_window = _Window()
        self._vendor_window = _Window()
        self._daily: Dict[Tuple[str, str, str], int] = defaultdict(int)
        self._inflight: Dict[str, int] = defaultdict(int)
        self._suspended_clients: Dict[str, Set[str]] = defaultdict(set)
        self._validators = {
            name: jsonschema.Draft202012Validator(desc["inputSchema"])
            for name, desc in TOOL_DESCRIPTORS.items()
        }

    # ── authN / profile ────────────────────────────────────────────────
    async def _authenticate(self, token: str) -> Tuple[EdgePrincipal, VendorProfile]:
        try:
            principal = await self.d.tokens.verify_access(token)
        except TokenRejected as exc:
            msg = str(exc)
            reason = "revoked" if "revoked" in msg else "unauthorized"
            raise _Denied(reason, f"{'revoked' if reason == 'revoked' else 'unauthorized'}: {msg}")
        profile = self.d.profiles.get(principal.vendor)
        if profile is None or not profile.enabled:
            raise _Denied("vendor_disabled", "vendor disabled")
        if self.d.lockdown.level_of(principal.principal_id) == LockdownLevel.SUSPENDED:
            raise _Denied("revoked", "revoked: client suspended by lockdown")
        if profile.allowed_hours is not None:
            start, end, tz = profile.allowed_hours
            now = datetime.fromtimestamp(self.d.clock(), tz=tz).time()
            inside = start <= now <= end if start <= end else (now >= start or now <= end)
            if not inside:
                raise _Denied("outside_hours", "outside allowed hours")
        return principal, profile

    def _visible_tools(self, profile: VendorProfile) -> List[str]:
        names = []
        for name in sorted(profile.tools):
            needs = TOOL_DESCRIPTORS[name].get("requires_local_agent")
            if needs and needs not in self.d.local_agents:
                continue
            if name in self.d.facades:
                names.append(name)
        return names

    async def list_tools(self, token: str) -> List[Dict[str, Any]]:
        try:
            _, profile = await self._authenticate(token)
        except _Denied as exc:
            raise PermissionError(str(exc)) from exc
        return [mcp_tool(name) for name in self._visible_tools(profile)]

    # ── escalation ladder ──────────────────────────────────────────────
    async def _alert(self, step: str, principal: EdgePrincipal, reason: str) -> None:
        details = {
            "source": "inbound_edge",
            "step": step,
            "vendor": principal.vendor,
            "client_id": principal.client_id,
            "reason": reason,
        }
        await self.d.audit.log_event(
            "edge_lockdown", "critical", details, "inbound_edge", bot_id="edge"
        )
        await self.d.emit(
            make_event(
                "security_alert",
                f"Inbound edge {step}: {principal.vendor}/{principal.client_id} ({reason})",
                details,
                "critical",
            )
        )

    async def _strike(self, principal: EdgePrincipal, reason: str) -> None:
        pid = principal.principal_id
        before = self.d.lockdown.level_of(pid)
        if reason == "canary":
            self.d.lockdown.escalate_to(pid, LockdownLevel.SUSPENDED, "canary hit")
        else:
            self.d.lockdown.record_block(pid, reason, principal.client_id)
        after = self.d.lockdown.level_of(pid)
        if after == before:
            return
        for level in (LockdownLevel.ALERT, LockdownLevel.ESCALATED, LockdownLevel.SUSPENDED):
            if _rank(before) < _rank(level) <= _rank(after) and (
                reason != "canary" or level == LockdownLevel.SUSPENDED
            ):
                await self._alert(_LADDER[level], principal, reason)
        if after == LockdownLevel.SUSPENDED:
            await self.d.store.kill("client", principal.client_id, f"lockdown: {reason}")
            suspended = self._suspended_clients[principal.vendor]
            suspended.add(principal.client_id)
            if reason == "canary" or len(suspended) >= VENDOR_DISABLE_AFTER_SUSPENDED_CLIENTS:
                await self.d.store.kill("vendor", principal.vendor, f"lockdown: {reason}")
                await self._alert("vendor_disabled", principal, reason)

    # ── limits ─────────────────────────────────────────────────────────
    def _check_limits(self, principal: EdgePrincipal, profile: VendorProfile, tool: str) -> None:
        now = self.d.clock()
        level = self.d.lockdown.level_of(principal.principal_id)
        per_client = profile.per_client_per_minute
        if _rank(level) >= _rank(LockdownLevel.ALERT):
            per_client = max(1, per_client // 2)
        if not self._client_window.hit(principal.principal_id, per_client, now):
            raise _Denied("rate_limited", "rate limited (client)")
        if not self._vendor_window.hit(profile.vendor, profile.per_vendor_per_minute, now):
            raise _Denied("rate_limited", "rate limited (vendor)")
        day = time.strftime("%Y-%m-%d", time.gmtime(now))
        if self._daily[(profile.vendor, day, "calls")] >= profile.daily_calls:
            raise _Denied("budget", "daily call budget exhausted")
        if TOOL_DESCRIPTORS[tool]["access"] == "write":
            if _rank(level) >= _rank(LockdownLevel.ESCALATED):
                raise _Denied("writes_disabled", "writes disabled by lockdown")
            if self._daily[(profile.vendor, day, "delegations")] >= profile.daily_delegations:
                raise _Denied("budget", "daily delegation budget exhausted")
        if self._inflight[profile.vendor] >= profile.max_concurrency:
            raise _Denied("concurrency", "concurrency limit reached")
        self._daily[(profile.vendor, day, "calls")] += 1

    # ── P0 ─────────────────────────────────────────────────────────────
    def _p0(self, args: Dict[str, Any]) -> Tuple[float, List[str]]:
        score, hits = 0.0, []
        for leaf in _string_leaves(args):
            candidates = [leaf, normalize_input(leaf)]
            decoded = self.d.encoding_detector.analyze(leaf)
            candidates += [layer.decoded for layer in getattr(decoded, "layers", [])]
            for text in candidates:
                scan = self.d.prompt_guard.scan(text)
                score = max(score, float(scan.score))
                if scan.blocked:
                    hits.extend(scan.patterns or ["prompt_guard"])
                elif self.d.heuristic is not None and 0.3 <= scan.score < 0.8:
                    verdict = self.d.heuristic.classify(text)
                    if verdict.is_injection:
                        hits.append("heuristic_classifier")
                        score = max(score, float(verdict.probability))
        return score, hits

    # ── output ─────────────────────────────────────────────────────────
    async def _scrub(self, value: Any, profile: VendorProfile, findings: Dict[str, int]) -> Any:
        if isinstance(value, dict):
            return {k: await self._scrub(v, profile, findings) for k, v in value.items()}
        if isinstance(value, list):
            return [await self._scrub(v, profile, findings) for v in value]
        if not isinstance(value, str) or not value:
            return value
        result = await self.d.sanitizer.sanitize(
            value, action=profile.dlp_mode, min_confidence=profile.dlp_min_confidence
        )
        for entity in result.entity_types_found:
            findings[entity] = findings.get(entity, 0) + 1
        if result.blocked:
            findings["_blocked"] = 1
        text, cred_blocked = await self.d.sanitizer.block_credentials(
            result.sanitized_content, source="untrusted"
        )
        if cred_blocked:
            findings["CREDENTIAL"] = findings.get("CREDENTIAL", 0) + 1
            return "[credential withheld]"
        return text

    # ── main entry ─────────────────────────────────────────────────────
    async def call_tool(
        self, token: str, name: str, arguments: Dict[str, Any], request_id: str
    ) -> Dict[str, Any]:
        started = self.d.clock()
        arguments = arguments if isinstance(arguments, dict) else {}
        rec: Dict[str, Any] = {
            "request_id": request_id,
            "vendor": None,
            "client_id": None,
            "jti": None,
            "tool": name,
            "args_sha256": hashlib.sha256(canonical_bytes(arguments)).hexdigest(),
            "schema_ok": False,
            "p0_score": 0.0,
            "approval": None,
            "target": None,
            "hermes_session_id": None,
            "response_sha256": None,
            "dlp": {},
            "canary_hits": 0,
            "latency_ms": 0.0,
            "outcome": "error",
        }
        principal: Optional[EdgePrincipal] = None
        profile: Optional[VendorProfile] = None
        inflight = False
        try:
            principal, profile = await self._authenticate(token)
            rec.update(vendor=principal.vendor, client_id=principal.client_id, jti=principal.jti)
            stats = self.stats[principal.vendor]
            stats.calls += 1
            stats.last_call = started

            if name not in self._visible_tools(profile) or profile.tool_access(name) is None:
                raise _Denied("tool_not_permitted", "tool not permitted")
            facade = self.d.facades[name]
            rec["target"] = facade.target

            errors = sorted(self._validators[name].iter_errors(arguments), key=str)
            if errors:
                raise _Denied("schema", f"schema violation: {errors[0].message[:200]}")
            rec["schema_ok"] = True

            self._check_limits(principal, profile, name)
            self._inflight[profile.vendor] += 1
            inflight = True

            if self.d.tool_chain is not None:
                allowed, match = self.d.tool_chain.analyze_tool_call(
                    principal.principal_id, name, arguments, request_id
                )
                if not allowed:
                    raise _Denied("tool_chain", f"tool chain blocked: {getattr(match, 'name', '')}")

            score, hits = self._p0(arguments)
            rec["p0_score"] = round(score, 3)
            if hits:
                if profile.enforcing:
                    raise _Denied("prompt_injection", "prompt injection detected in arguments")
                rec["monitor_violation"] = "prompt_injection"

            call = CallContext(request_id=request_id, principal=principal, profile=profile)
            if TOOL_DESCRIPTORS[name]["access"] == "write":
                ctx = ApprovalContext(
                    principal=principal,
                    vendor_display=profile.display_name,
                    tool=name,
                    target=facade.target,
                    args=arguments,
                    p0_score=score,
                )
                ticket = arguments.get("approval_ticket")
                if not ticket:
                    pending = await self.d.approvals.request(ctx)
                    rec["approval"] = {"request_id": pending.request_id, "decision": "pending"}
                    rec["outcome"] = "awaiting_approval"
                    stats.pending_approvals += 1
                    return _result(
                        {
                            "status": "awaiting_human_approval",
                            "approval_ticket": pending.ticket,
                            "approval_request_id": pending.request_id,
                            "expires_at": pending.expires_at,
                            "args_sha256": pending.args_sha256,
                            "next_step": (
                                "Repeat this exact call with approval_ticket set once the "
                                "owner approves. No decision before expires_at means denied."
                            ),
                        }
                    )
                try:
                    await self.d.approvals.redeem(ticket, ctx)
                except ApprovalPending:
                    rec["outcome"] = "awaiting_approval"
                    return _result({"status": "awaiting_human_approval"})
                except ApprovalDenied as exc:
                    rec["approval"] = {"decision": "denied", "reason": str(exc)}
                    raise _Denied("approval", f"approval: {exc}")
                rec["approval"] = {"decision": "approved"}
                day = time.strftime("%Y-%m-%d", time.gmtime(self.d.clock()))
                self._daily[(profile.vendor, day, "delegations")] += 1
                arguments = {k: v for k, v in arguments.items() if k != "approval_ticket"}

            result = await facade.run(arguments, call)
            rec["hermes_session_id"] = result.pop("hermes_session_id", None)

            raw = json.dumps(result, ensure_ascii=False)
            trip = self.d.tripwire.scan_response(raw, source=f"edge:{principal.vendor}")
            if trip.is_blocked:
                rec["canary_hits"] = len(getattr(trip, "detections", []) or [1])
                stats.canary_hits += 1
                raise _Denied("canary", "response withheld: canary tripwire")

            findings: Dict[str, int] = {}
            clean = await self._scrub(result, profile, findings)
            blocked = findings.pop("_blocked", 0)
            rec["dlp"] = findings
            if findings:
                stats.dlp_hits += 1
            if blocked:
                if profile.enforcing:
                    raise _Denied("dlp", "response withheld by DLP")
                rec["monitor_violation"] = "dlp"

            body = json.dumps(clean, ensure_ascii=False).encode()
            cap = min(profile.max_response_bytes, TOOL_RESPONSE_CAPS.get(name, 1 << 62))
            if len(body) > cap:
                raise _Denied("too_large", f"response too large ({len(body)} > {cap} bytes)")
            rec["response_sha256"] = hashlib.sha256(body).hexdigest()
            rec["outcome"] = "ok"
            stats.ok += 1
            return _result(clean)

        except _Denied as exc:
            rec["outcome"] = "denied"
            rec["deny_reason"] = exc.reason
            if principal is not None:
                self.stats[principal.vendor].denials[exc.reason] += 1
                if exc.reason in _STRIKES:
                    await self._strike(principal, exc.reason)
            return _result(f"denied: {exc}", error=True)
        except Exception as exc:  # fail closed
            logger.exception("inbound edge call failed: %s", type(exc).__name__)
            rec["outcome"] = "error"
            rec["error"] = type(exc).__name__
            return _result("denied: internal error", error=True)
        finally:
            if inflight and profile is not None:
                self._inflight[profile.vendor] -= 1
            rec["latency_ms"] = round((self.d.clock() - started) * 1000, 3)
            await self._record(rec, principal)

    async def _record(self, rec: Dict[str, Any], principal: Optional[EdgePrincipal]) -> None:
        severity = "info" if rec["outcome"] in ("ok", "awaiting_approval") else "warning"
        try:
            await self.d.audit.log_event("edge_call", severity, rec, "inbound_edge", bot_id="edge")
        except Exception as exc:
            logger.error("edge audit write failed: %s", exc)
        if principal is not None:
            self.stats[principal.vendor].recent.appendleft(
                {
                    k: rec.get(k)
                    for k in ("request_id", "client_id", "tool", "outcome", "latency_ms")
                }
                | {"deny_reason": rec.get("deny_reason")}
            )
        try:
            await self.d.emit(
                make_event(
                    "edge_event",
                    f"edge {rec['vendor'] or '?'} {rec['tool']} → {rec['outcome']}",
                    rec,
                    severity,
                )
            )
        except Exception as exc:
            logger.error("edge event emit failed: %s", exc)


def _rank(level: LockdownLevel) -> int:
    return [
        LockdownLevel.NORMAL,
        LockdownLevel.ALERT,
        LockdownLevel.ESCALATED,
        LockdownLevel.SUSPENDED,
    ].index(level)
