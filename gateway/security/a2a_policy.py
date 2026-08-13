# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""A2A (Agent-to-Agent) security policy engine (SCRUM-129).

Governance for Hermes v0.20.0+'s inbound A2A protocol surface: the real Google/
Linux Foundation A2A v1.0.1 spec (JSON-RPC 2.0 over HTTP). Given a
(peer_id, method, task_id) tuple, this engine returns an allow / deny /
require-approval decision — mirroring gateway/security/mcp_policy.py's shape,
since A2A's inbound governance problem (peer identity + action risk tier, with
a default-deny posture) is structurally the same class of problem MCP tool
calls are.

Two things A2A needs that MCP does not:

  - Task ownership tracking. A2A calls are frequently *task-scoped*
    (GetTask/CancelTask/SubscribeToTask reference a task_id created by an
    earlier SendMessage). Hermes's own contextId handling has a known,
    currently-unpatched collision bug (upstream issue #83701) that can let one
    peer's task reference resolve into another peer's conversation history.
    This engine tracks task ownership independently — a peer may only act on
    a task_id it created — so that bug becomes moot for anything AgentShroud
    intercepts, regardless of whether/when Hermes fixes its own code.
  - A hardened push-notification callback-URL validator
    (:func:`is_safe_a2a_callback_url`), an independent mitigation for a known,
    currently-unpatched SSRF bypass in Hermes's own callback-URL guard
    (upstream issue #78298): alternate IP encodings (decimal, hex, octal,
    trailing-dot) sail past Hermes's ``ipaddress.ip_address()``-only check.

See docs/security/threat-model.md, "A2A (Agent-to-Agent) Protocol Threat
Analysis", for the full source-level audit this module's mitigations map to.

Design notes
------------
* ``evaluate`` is pure (no I/O, no await) — trivially unit-testable and cheap
  enough for the hot path. ``enforce`` wraps it with the async approval-queue
  round-trip, identical fail-closed contract to ``MCPPolicyEngine.enforce``.
* ``owner_bypass`` is forced ``False`` unconditionally, regardless of what a
  config author sets — unlike MCP tool calls (issued by AgentShroud's own
  bots), an A2A caller is always an *external* peer. There is no meaningful
  sense in which a peer is "the owner."
* Scope: **inbound only** (a peer calling Hermes). Outbound governance
  (Hermes's own `a2a` toolset calling other peers) is architecturally capped
  by the existing HTTP CONNECT-tunnel proxy's opacity to HTTPS payload content
  and is tracked as a separate follow-up ticket.

IEC 62443 alignment: FR3 (SL3) — per-identity, per-resource access control at
every A2A method-call boundary; deny-by-default with an explicit allowlist.
FR7 (SL2) — task-ownership isolation prevents one peer's requests from
resolving into another peer's session/task state.
"""

from __future__ import annotations

import ipaddress
import logging
import re
import socket
import unicodedata
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional
from urllib.parse import urlsplit

logger = logging.getLogger("agentshroud.security.a2a_policy")


# ---------------------------------------------------------------------------
# A2A method surface (spec-defined enum, not an open string — see module
# docstring: unlike MCP tool names, A2A's method set is fixed by the JSON-RPC
# 2.0 binding of the spec, so an explicit tier map is more correct than a
# keyword heuristic).
# ---------------------------------------------------------------------------


class A2AMethod(str, Enum):
    """Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs."""

    SEND_MESSAGE = "SendMessage"
    SEND_STREAMING_MESSAGE = "SendStreamingMessage"
    GET_TASK = "GetTask"
    LIST_TASKS = "ListTasks"
    CANCEL_TASK = "CancelTask"
    SUBSCRIBE_TO_TASK = "SubscribeToTask"
    GET_PUSH_NOTIFICATION_CONFIG = "GetTaskPushNotificationConfig"
    SET_PUSH_NOTIFICATION_CONFIG = "SetTaskPushNotificationConfig"
    DELETE_PUSH_NOTIFICATION_CONFIG = "DeleteTaskPushNotificationConfig"


# Methods that create a new task (their task_id becomes owned by the caller).
_TASK_CREATING_METHODS = frozenset({A2AMethod.SEND_MESSAGE, A2AMethod.SEND_STREAMING_MESSAGE})

# Methods that reference an existing task_id and must be checked for ownership.
_TASK_SCOPED_METHODS = frozenset(
    {
        A2AMethod.GET_TASK,
        A2AMethod.CANCEL_TASK,
        A2AMethod.SUBSCRIBE_TO_TASK,
        A2AMethod.GET_PUSH_NOTIFICATION_CONFIG,
        A2AMethod.SET_PUSH_NOTIFICATION_CONFIG,
        A2AMethod.DELETE_PUSH_NOTIFICATION_CONFIG,
    }
)

# Fixed baseline risk tiers. Spec-defined method set — an explicit map, not a
# substring heuristic (see module docstring).
_DEFAULT_METHOD_TIERS: Dict[A2AMethod, str] = {
    A2AMethod.GET_TASK: "low",
    A2AMethod.LIST_TASKS: "low",
    A2AMethod.GET_PUSH_NOTIFICATION_CONFIG: "low",
    A2AMethod.SEND_MESSAGE: "medium",
    A2AMethod.SUBSCRIBE_TO_TASK: "medium",
    A2AMethod.SEND_STREAMING_MESSAGE: "high",
    A2AMethod.SET_PUSH_NOTIFICATION_CONFIG: "high",
    A2AMethod.DELETE_PUSH_NOTIFICATION_CONFIG: "high",
    A2AMethod.CANCEL_TASK: "high",
}


def _method_of(method: "A2AMethod | str") -> A2AMethod:
    """Accept either the enum or its string value (JSON-RPC payloads arrive
    as plain strings; callers/tests may pass either)."""
    if isinstance(method, A2AMethod):
        return method
    return A2AMethod(str(method))


# ---------------------------------------------------------------------------
# Decision types
# ---------------------------------------------------------------------------


class A2APolicyAction(str, Enum):
    """The three terminal policy outcomes for an A2A request."""

    ALLOW = "allow"
    DENY = "deny"
    REQUIRE_APPROVAL = "require_approval"


@dataclass
class A2APolicyDecision:
    """The result of evaluating a single A2A request against the policy."""

    action: A2APolicyAction
    peer_id: str
    method: str
    reason: str = ""
    risk_tier: str = "low"
    matched_rule: str = ""

    @property
    def allowed(self) -> bool:
        """True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on
        its own — ``enforce`` resolves it to ALLOW/DENY."""
        return self.action is A2APolicyAction.ALLOW


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------


def _norm(value: str) -> str:
    """Normalize a peer-id reference for robust, evasion-resistant matching.

    Same NFKC-then-casefold approach as mcp_policy.py::_norm — collapses
    fullwidth/homoglyph/compatibility variants before comparison.
    """
    return unicodedata.normalize("NFKC", str(value)).strip().casefold()


@dataclass
class A2APolicyConfig:
    """Declarative A2A security policy.

    Loaded from the ``a2a_policy:`` section of agentshroud.yaml via
    :meth:`from_dict`. Empty config -> deny everything (fail closed) — see
    test_a2a_policy_default_failclosed.py, mirroring the WS-E RT-11 lesson
    that a policy engine must never ship dormant/default-open.
    """

    default_action: A2APolicyAction = A2APolicyAction.DENY
    allowed_peers: list = field(default_factory=list)
    denied_peers: list = field(default_factory=list)
    high_risk_actions: list = field(default_factory=lambda: ["high", "critical"])

    # Unconditionally forced False in __post_init__ regardless of input — see
    # module docstring. Not a real operator knob; kept as a field only so
    # from_dict() has somewhere to observe a config author's (ignored) intent
    # and log it, rather than silently dropping the key.
    owner_bypass: bool = False
    owner_user_id: str = ""

    _allowed: frozenset = field(default_factory=frozenset, init=False, repr=False)
    _denied: frozenset = field(default_factory=frozenset, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.owner_bypass:
            logger.warning(
                "a2a_policy.owner_bypass was set but is not honoured for A2A — "
                "an external peer is never treated as the human operator; forcing False."
            )
        self.owner_bypass = False
        self._allowed = frozenset(_norm(p) for p in self.allowed_peers)
        self._denied = frozenset(_norm(p) for p in self.denied_peers)

    @classmethod
    def from_dict(cls, data: Optional[Dict[str, Any]]) -> "A2APolicyConfig":
        """Parse a policy config from a plain dict (e.g. loaded from YAML)."""
        data = data or {}
        default_raw = str(data.get("default_action", "deny")).lower()
        try:
            default_action = A2APolicyAction(default_raw)
        except ValueError:
            logger.warning(
                "Invalid a2a_policy.default_action=%r — falling back to deny", default_raw
            )
            default_action = A2APolicyAction.DENY
        return cls(
            default_action=default_action,
            allowed_peers=list(data.get("allowed_peers", [])),
            denied_peers=list(data.get("denied_peers", [])),
            high_risk_actions=list(data.get("high_risk_actions", ["high", "critical"])),
            owner_bypass=bool(data.get("owner_bypass", False)),
            owner_user_id=str(data.get("owner_user_id", "") or ""),
        )


# ---------------------------------------------------------------------------
# Hardened push-notification callback-URL validator (independent mitigation
# for upstream gap #78298 — see docs/security/threat-model.md).
#
# NOTE: gateway/security/egress_filter.py::_is_private_ip has the same class
# of bug (delegates straight to ipaddress.ip_address(), which raises
# ValueError — not "not private" — on decimal/hex/octal literals, and that
# ValueError path does not re-check the alternate encodings). This validator
# is intentionally self-contained rather than calling into egress_filter, so
# fixing this one does not depend on (or silently mask the need to also fix)
# that pre-existing, broader gap. Flagged as a separate follow-up ticket.
# ---------------------------------------------------------------------------

_BLOCKED_HOSTNAMES = frozenset({"localhost", "localhost.localdomain"})

# Matches a bare decimal or hex (0x...) IPv4-as-integer literal — forms
# ipaddress.ip_address() does NOT parse, so they fall through its ValueError
# branch unexamined. Octal and short-form dotted encodings (e.g. "0177.0.0.1",
# "127.1") are handled below via socket.inet_aton, which implements the BSD
# per-octet radix rules directly rather than needing a second regex.
_DECIMAL_IPV4 = re.compile(r"^\d{1,10}$")
_HEX_IPV4 = re.compile(r"^0[xX][0-9a-fA-F]{1,8}$")


def _int_to_ipv4(value: int) -> Optional[ipaddress.IPv4Address]:
    if 0 <= value <= 0xFFFFFFFF:
        try:
            return ipaddress.IPv4Address(value)
        except ValueError:
            return None
    return None


def _canonicalize_ip_literal(host: str) -> Optional[ipaddress._BaseAddress]:
    """Best-effort canonicalization of alternate IPv4 encodings that
    ``ipaddress.ip_address()`` refuses to parse on its own, so the SSRF check
    below sees the *real* address rather than treating an unparseable string
    as "not an IP, must be a safe hostname."
    """
    stripped = host.strip("[]")

    # Canonical form — let ipaddress handle it directly.
    try:
        return ipaddress.ip_address(stripped)
    except ValueError:
        pass

    # Decimal (e.g. "2130706433" == 127.0.0.1).
    if _DECIMAL_IPV4.match(stripped):
        return _int_to_ipv4(int(stripped, 10))

    # Hex (e.g. "0x7f000001" == 127.0.0.1).
    if _HEX_IPV4.match(stripped):
        return _int_to_ipv4(int(stripped, 16))

    # Per-octet mixed decimal/hex/octal, and short-form dotted addresses
    # (e.g. "127.1" == 127.0.0.1, "0177.0.0.1" == 127.0.0.1,
    # "0x7f.0.0.1" == 127.0.0.1). socket.inet_aton handles the classic BSD
    # short-form + per-octet radix rules that ipaddress deliberately rejects
    # as ambiguous; this is exactly the leniency an attacker exploits, which
    # is why we canonicalize it ourselves instead of trusting the strict
    # parser's rejection to mean "safe."
    try:
        packed = socket.inet_aton(stripped)
        return ipaddress.IPv4Address(packed)
    except (OSError, ValueError):
        pass

    return None


def is_safe_a2a_callback_url(url: str) -> bool:
    """Hardened SSRF guard for A2A push-notification callback URLs.

    Independent mitigation for upstream Hermes gap #78298: alternate IP
    encodings (decimal/hex/octal/trailing-dot/short-form) bypass Hermes's own
    ``ipaddress.ip_address()``-only guard. Returns False (unsafe) for:
      * non-http(s) schemes,
      * any hostname/IP that canonicalizes to a private, loopback,
        link-local, reserved, or multicast address (covers RFC 1918, the
        169.254.169.254 cloud-metadata endpoint, and ::1/::ffff:127.0.0.1),
      * known localhost hostname aliases, with or without a trailing dot,
      * a hostname that resolves (forward DNS) to any of the above — this is
        re-checked on every call, not cached, to resist DNS rebinding.

    Fails closed: any parse/resolution error is treated as unsafe.
    """
    try:
        parsed = urlsplit(url)
    except ValueError:
        return False

    if parsed.scheme not in ("http", "https"):
        return False

    host = (parsed.hostname or "").strip()
    if not host:
        return False

    # Trailing-dot FQDN normalization (RFC 1035 root-label bypass attempt).
    host = host.rstrip(".")
    if not host:
        return False

    if host.casefold() in _BLOCKED_HOSTNAMES:
        return False

    literal = _canonicalize_ip_literal(host)
    if literal is not None:
        return _address_is_public(literal)

    # Not any recognized IP-literal encoding — it's a real hostname. Resolve
    # it and check every returned address, since the callback will actually
    # be dialed against whatever DNS returns at request time, not at
    # config-set time (DNS rebinding).
    try:
        infos = socket.getaddrinfo(host, None)
    except (socket.gaierror, UnicodeError, OSError):
        # Cannot resolve -> cannot verify safety -> fail closed.
        return False

    for info in infos:
        addr_str = info[4][0]
        try:
            addr = ipaddress.ip_address(addr_str)
        except ValueError:
            return False
        if not _address_is_public(addr):
            return False

    return True


def _address_is_public(addr) -> bool:
    if isinstance(addr, ipaddress.IPv6Address) and addr.ipv4_mapped:
        addr = addr.ipv4_mapped
    return not (
        addr.is_private
        or addr.is_loopback
        or addr.is_link_local
        or addr.is_reserved
        or addr.is_multicast
        or addr.is_unspecified
    )


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------


class A2APolicyEngine:
    """Decides allow / deny / require-approval for inbound A2A requests.

    Usage::

        engine = A2APolicyEngine(config, approval_queue=queue)
        decision = engine.evaluate("alice", A2AMethod.SendMessage)
        # or, resolving the approval round-trip:
        decision = await engine.enforce("alice", A2AMethod.CancelTask, task_id="t-1")
    """

    def __init__(
        self,
        config: Optional[A2APolicyConfig] = None,
        approval_queue=None,
    ):
        self._cfg = config or A2APolicyConfig()
        self._approval_queue = approval_queue
        # task_id -> peer_id that created it. Deliberately in-process/
        # in-memory: this is a defense-in-depth check independent of
        # whatever Hermes's own (currently buggy) contextId persistence does,
        # not a durable record of task state.
        self._task_owner: Dict[str, str] = {}

    # ---- pure decision ----------------------------------------------------

    def evaluate(
        self,
        peer_id: str,
        method: "A2AMethod | str",
        task_id: Optional[str] = None,
        callback_url: Optional[str] = None,
    ) -> A2APolicyDecision:
        """Evaluate a single A2A request. Pure — no I/O, no side effects
        beyond best-effort SOC heat-map telemetry and the in-memory task-
        ownership map (updated only on ALLOW/REQUIRE_APPROVAL of a
        task-creating call, never on a call this evaluation denies).

        Precedence (first match wins):
          1. Peer denylist              -> DENY (deny wins over allow).
          2. Peer not allowlisted (under default-deny) -> DENY.
          3. Task-scoped call on a task the peer doesn't own -> DENY.
          4. SetPushNotificationConfig with an unsafe callback URL -> DENY.
          5. High-risk method            -> REQUIRE_APPROVAL.
          6. Otherwise                   -> ALLOW.
        """
        peer = _norm(peer_id)
        m = _method_of(method)

        decision = self._decide(peer, m, task_id, callback_url)

        try:
            from gateway.security.module_stats import record_decision

            record_decision("a2a_policy", decision.action is A2APolicyAction.ALLOW)
        except Exception:  # pragma: no cover - telemetry must never raise
            pass

        if decision.action is not A2APolicyAction.ALLOW:
            logger.warning(
                "A2A policy %s: peer=%s method=%s task=%s tier=%s rule=%s",
                decision.action.value,
                peer_id,
                m.value,
                task_id,
                decision.risk_tier,
                decision.matched_rule,
            )

        # Record ownership only for a task-creating call that was not denied
        # outright — a REQUIRE_APPROVAL call still reserves the task_id for
        # this peer, since the alternative (waiting for approval to resolve
        # before recording ownership) would leave a race window where a
        # second peer could claim the same task_id first.
        if m in _TASK_CREATING_METHODS and task_id and decision.action is not A2APolicyAction.DENY:
            self._task_owner.setdefault(task_id, peer)

        return decision

    def _decide(
        self,
        peer: str,
        method: A2AMethod,
        task_id: Optional[str],
        callback_url: Optional[str],
    ) -> A2APolicyDecision:
        cfg = self._cfg

        # 1. Peer denylist — deny wins over allow.
        if peer in cfg._denied:
            return A2APolicyDecision(
                action=A2APolicyAction.DENY,
                peer_id=peer,
                method=method.value,
                reason=f"peer '{peer}' is on the A2A peer denylist",
                risk_tier=self._tier_for(method),
                matched_rule="peer_denylist",
            )

        # 2. Allowlist / default action.
        if peer not in cfg._allowed:
            if cfg.default_action is A2APolicyAction.ALLOW:
                pass  # Operator explicitly opted into default-allow.
            else:
                return A2APolicyDecision(
                    action=A2APolicyAction.DENY,
                    peer_id=peer,
                    method=method.value,
                    reason=f"peer '{peer}' is not in the allowlist (default-deny posture)",
                    risk_tier=self._tier_for(method),
                    matched_rule="default_deny",
                )

        # 3. Task ownership — independent mitigation for upstream gap #83701.
        # A task_id this engine has never seen is not an ownership violation
        # (e.g. engine restart, or a task predating this module) — it falls
        # through to normal risk-tier evaluation rather than a false-positive
        # deny.
        if method in _TASK_SCOPED_METHODS and task_id:
            owner = self._task_owner.get(task_id)
            if owner is not None and owner != peer:
                return A2APolicyDecision(
                    action=A2APolicyAction.DENY,
                    peer_id=peer,
                    method=method.value,
                    reason=(
                        f"peer '{peer}' does not own task '{task_id}' "
                        f"(created by a different peer)"
                    ),
                    risk_tier=self._tier_for(method),
                    matched_rule="task_ownership",
                )

        # 4. Push-notification callback SSRF check — independent mitigation
        # for upstream gap #78298. Checked before the generic risk-tier gate
        # so an unsafe callback is a hard DENY, never merely REQUIRE_APPROVAL
        # (a human approver is not expected to manually re-derive whether a
        # URL is an SSRF vector).
        if method is A2AMethod.SET_PUSH_NOTIFICATION_CONFIG and callback_url is not None:
            if not is_safe_a2a_callback_url(callback_url):
                return A2APolicyDecision(
                    action=A2APolicyAction.DENY,
                    peer_id=peer,
                    method=method.value,
                    reason=f"callback URL '{callback_url}' failed the SSRF safety check",
                    risk_tier="high",
                    matched_rule="ssrf_callback_blocked",
                )

        # 5. Risk tier -> approval gate. owner_bypass is unconditionally
        # False for A2A (enforced in A2APolicyConfig.__post_init__), so there
        # is deliberately no bypass branch here at all, unlike mcp_policy.py.
        tier = self._tier_for(method)
        if tier in {t.lower() for t in cfg.high_risk_actions}:
            return A2APolicyDecision(
                action=A2APolicyAction.REQUIRE_APPROVAL,
                peer_id=peer,
                method=method.value,
                reason=f"method '{method.value}' is {tier}-risk and requires human approval",
                risk_tier=tier,
                matched_rule="risk_tier",
            )

        # 6. Allowlisted + safe method -> allow.
        return A2APolicyDecision(
            action=A2APolicyAction.ALLOW,
            peer_id=peer,
            method=method.value,
            reason=f"peer '{peer}' allowlisted; method '{method.value}' is {tier}-risk",
            risk_tier=tier,
            matched_rule="allowlist",
        )

    def _tier_for(self, method: A2AMethod) -> str:
        return _DEFAULT_METHOD_TIERS.get(method, "high")

    # ---- async enforcement (approval-queue round-trip) --------------------

    async def enforce(
        self,
        peer_id: str,
        method: "A2AMethod | str",
        task_id: Optional[str] = None,
        callback_url: Optional[str] = None,
    ) -> A2APolicyDecision:
        """Evaluate and resolve the decision to a terminal ALLOW/DENY.

        Identical fail-closed contract to MCPPolicyEngine.enforce: for
        REQUIRE_APPROVAL, enqueues through the wired approval queue and waits
        for the human decision. Fails CLOSED (DENY) if no approval queue is
        configured, or if the queue reports no wait required for a call the
        engine deemed high-risk (the engine's verdict is never silently
        downgraded).
        """
        decision = self.evaluate(peer_id, method, task_id=task_id, callback_url=callback_url)

        if decision.action is not A2APolicyAction.REQUIRE_APPROVAL:
            return decision

        peer = _norm(peer_id)
        m = _method_of(method)
        qualified = f"a2a:{peer}:{m.value}"

        if self._approval_queue is None:
            logger.warning(
                "A2A policy DENY (fail-closed): high-risk method '%s' but no approval "
                "queue configured (peer=%s)",
                qualified,
                peer_id,
            )
            return A2APolicyDecision(
                action=A2APolicyAction.DENY,
                peer_id=peer,
                method=m.value,
                reason=(
                    f"method '{qualified}' requires approval but no approval queue "
                    f"is configured — denied (fail-closed)"
                ),
                risk_tier=decision.risk_tier,
                matched_rule="approval_unavailable",
            )

        args = {"task_id": task_id} if task_id else {}
        try:
            request_id, requires_wait = await self._approval_queue.submit_tool_request(
                qualified, args, peer_id, force_tier=decision.risk_tier
            )
        except TypeError:
            request_id, requires_wait = await self._approval_queue.submit_tool_request(
                qualified, args, peer_id
            )

        if not requires_wait:
            logger.warning(
                "A2A policy DENY (fail-closed): approval queue returned "
                "requires_wait=False for engine-deemed %s-risk method '%s' "
                "(peer=%s) — refusing to downgrade to ALLOW",
                decision.risk_tier,
                qualified,
                peer_id,
            )
            return A2APolicyDecision(
                action=A2APolicyAction.DENY,
                peer_id=peer,
                method=m.value,
                reason=(
                    f"method '{qualified}' was deemed {decision.risk_tier}-risk by the "
                    f"policy engine but the approval queue did not require a wait — "
                    f"denied (fail-closed; engine verdict wins)"
                ),
                risk_tier=decision.risk_tier,
                matched_rule="approval_downgrade_refused",
            )

        approved = await self._approval_queue.wait_for_decision(request_id)
        if approved:
            return A2APolicyDecision(
                action=A2APolicyAction.ALLOW,
                peer_id=peer,
                method=m.value,
                reason=f"human operator approved '{qualified}' (request {request_id})",
                risk_tier=decision.risk_tier,
                matched_rule="approved",
            )
        return A2APolicyDecision(
            action=A2APolicyAction.DENY,
            peer_id=peer,
            method=m.value,
            reason=f"method '{qualified}' was denied by the human operator (request {request_id})",
            risk_tier=decision.risk_tier,
            matched_rule="rejected",
        )
