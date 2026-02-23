# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Session Security Module - Secure session management for MCP gateway.

Provides cryptographically random session IDs, session binding to user identity,
session expiry/rotation, event injection prevention, and rate limiting.

References:
    - Chen et al. 2026 (arXiv:2602.14364) - Session hijacking in agent frameworks
    - Wang et al. 2026 (arXiv:2602.08412) - Event injection attacks
"""
from __future__ import annotations


import hashlib
import secrets
import time
from dataclasses import dataclass, field
from typing import Dict, Set, Any


class SessionError(Exception):
    pass


class SessionExpired(SessionError):
    pass


class SessionBindingError(SessionError):
    pass


class EventInjectionError(SessionError):
    pass


class RateLimitExceeded(SessionError):
    pass


@dataclass
class Session:
    session_id: str
    ip: str
    user_agent: str
    fingerprint: str
    created_at: float = field(default_factory=time.time)
    event_sources: Set[str] = field(default_factory=set)


class SessionManager:
    MAX_TOTAL_SESSIONS = 10000

    def __init__(
        self,
        max_session_age: int = 3600,
        max_sessions_per_ip: int = 10,
        rate_limit_window: int = 60,
    ):
        self.max_session_age = max_session_age
        self.max_sessions_per_ip = max_sessions_per_ip
        self.rate_limit_window = rate_limit_window
        self._sessions: Dict[str, Session] = {}
        self._ip_creation_times: Dict[str, list] = {}

    def _fingerprint(self, ip: str, user_agent: str) -> str:
        return hashlib.sha256(f"{ip}:{user_agent}".encode()).hexdigest()

    def create_session(self, ip: str, user_agent: str) -> Session:
        # Rate limiting
        now = time.time()
        times = self._ip_creation_times.get(ip, [])
        times = [t for t in times if now - t <= self.rate_limit_window]
        if len(times) >= self.max_sessions_per_ip:
            raise RateLimitExceeded(f"Rate limit exceeded for {ip}")
        times.append(now)
        self._ip_creation_times[ip] = times

        # Evict expired sessions if at capacity
        if len(self._sessions) >= self.MAX_TOTAL_SESSIONS:
            self.cleanup_expired()

        sid = secrets.token_urlsafe(32)
        fp = self._fingerprint(ip, user_agent)
        session = Session(session_id=sid, ip=ip, user_agent=user_agent, fingerprint=fp)
        self._sessions[sid] = session
        return session

    def validate_session(self, session_id: str, ip: str, user_agent: str) -> bool:
        session = self._sessions.get(session_id)
        if not session:
            raise SessionError(f"Unknown session: {session_id}")
        if time.time() - session.created_at > self.max_session_age:
            del self._sessions[session_id]
            raise SessionExpired("Session expired")
        expected_fp = self._fingerprint(ip, user_agent)
        if session.fingerprint != expected_fp:
            raise SessionBindingError(
                "Session binding mismatch (IP or user-agent changed)"
            )
        return True

    def rotate_session(self, old_session_id: str, ip: str, user_agent: str) -> Session:
        self.validate_session(old_session_id, ip, user_agent)
        old = self._sessions.pop(old_session_id)
        new_sid = secrets.token_urlsafe(32)
        new_session = Session(
            session_id=new_sid,
            ip=ip,
            user_agent=user_agent,
            fingerprint=old.fingerprint,
            event_sources=old.event_sources,
        )
        self._sessions[new_sid] = new_session
        return new_session

    def destroy_session(self, session_id: str):
        self._sessions.pop(session_id, None)

    def register_event_source(self, session_id: str, source: str):
        session = self._sessions.get(session_id)
        if not session:
            raise SessionError(f"Unknown session: {session_id}")
        session.event_sources.add(source)

    def validate_event(self, session_id: str, source: str, event: Any) -> bool:
        session = self._sessions.get(session_id)
        if not session:
            raise SessionError(f"Unknown session: {session_id}")
        if source not in session.event_sources:
            raise EventInjectionError(f"Unregistered event source: {source}")
        return True

    def cleanup_expired(self) -> int:
        now = time.time()
        expired = [
            sid
            for sid, s in self._sessions.items()
            if now - s.created_at > self.max_session_age
        ]
        for sid in expired:
            del self._sessions[sid]
        # Clean up stale IP rate-limit entries
        stale_ips = [
            ip
            for ip, times in self._ip_creation_times.items()
            if not any(now - t <= self.rate_limit_window for t in times)
        ]
        for ip in stale_ips:
            del self._ip_creation_times[ip]
        return len(expired)
