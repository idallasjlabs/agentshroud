"""Tests for session_security module.
TDD: Written before implementation.
"""

import pytest
import time
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from security.session_security import (
    SessionManager,
    SessionError,
    SessionExpired,
    SessionBindingError,
    EventInjectionError,
    RateLimitExceeded,
)


@pytest.fixture
def manager():
    return SessionManager(
        max_session_age=3600, max_sessions_per_ip=10, rate_limit_window=60
    )


class TestSessionCreation:
    def test_create_session(self, manager):
        s = manager.create_session(ip="1.2.3.4", user_agent="Mozilla/5.0")
        assert s.session_id
        assert len(s.session_id) >= 32

    def test_session_id_is_cryptographically_random(self, manager):
        ids = {
            manager.create_session(f"1.2.3.{i}", "UA").session_id for i in range(100)
        }
        assert len(ids) == 100  # all unique

    def test_session_bound_to_identity(self, manager):
        s = manager.create_session("1.2.3.4", "Mozilla/5.0")
        assert s.ip == "1.2.3.4"
        assert s.user_agent == "Mozilla/5.0"
        assert s.fingerprint  # should have computed fingerprint


class TestSessionValidation:
    def test_valid_session_accepted(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        assert manager.validate_session(s.session_id, "1.2.3.4", "UA")

    def test_wrong_ip_rejected(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        with pytest.raises(SessionBindingError):
            manager.validate_session(s.session_id, "5.6.7.8", "UA")

    def test_wrong_user_agent_rejected(self, manager):
        s = manager.create_session("1.2.3.4", "UA1")
        with pytest.raises(SessionBindingError):
            manager.validate_session(s.session_id, "1.2.3.4", "UA2")

    def test_unknown_session_rejected(self, manager):
        with pytest.raises(SessionError):
            manager.validate_session("nonexistent", "1.2.3.4", "UA")

    def test_expired_session_rejected(self):
        mgr = SessionManager(
            max_session_age=0, max_sessions_per_ip=10, rate_limit_window=60
        )
        s = mgr.create_session("1.2.3.4", "UA")
        time.sleep(0.01)
        with pytest.raises(SessionExpired):
            mgr.validate_session(s.session_id, "1.2.3.4", "UA")


class TestSessionRotation:
    def test_rotate_session(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        old_id = s.session_id
        new_s = manager.rotate_session(old_id, "1.2.3.4", "UA")
        assert new_s.session_id != old_id
        # old session should be invalidated
        with pytest.raises(SessionError):
            manager.validate_session(old_id, "1.2.3.4", "UA")

    def test_rotated_session_valid(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        new_s = manager.rotate_session(s.session_id, "1.2.3.4", "UA")
        assert manager.validate_session(new_s.session_id, "1.2.3.4", "UA")


class TestEventInjection:
    def test_valid_event_source_accepted(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        manager.register_event_source(s.session_id, "mcp-server-1")
        assert manager.validate_event(s.session_id, "mcp-server-1", {"type": "message"})

    def test_unknown_event_source_rejected(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        manager.register_event_source(s.session_id, "mcp-server-1")
        with pytest.raises(EventInjectionError):
            manager.validate_event(s.session_id, "unknown-source", {"type": "message"})

    def test_unregistered_session_event_rejected(self, manager):
        with pytest.raises(SessionError):
            manager.validate_event("nonexistent", "src", {})


class TestRateLimiting:
    def test_rate_limit_exceeded(self):
        mgr = SessionManager(
            max_session_age=3600, max_sessions_per_ip=3, rate_limit_window=60
        )
        for _ in range(3):
            mgr.create_session("10.0.0.1", "UA")
        with pytest.raises(RateLimitExceeded):
            mgr.create_session("10.0.0.1", "UA")

    def test_different_ips_not_rate_limited(self):
        mgr = SessionManager(
            max_session_age=3600, max_sessions_per_ip=2, rate_limit_window=60
        )
        mgr.create_session("10.0.0.1", "UA")
        mgr.create_session("10.0.0.1", "UA")
        mgr.create_session("10.0.0.2", "UA")  # should succeed

    def test_rate_limit_resets_after_window(self):
        mgr = SessionManager(
            max_session_age=3600, max_sessions_per_ip=1, rate_limit_window=0
        )
        mgr.create_session("10.0.0.1", "UA")
        time.sleep(0.01)
        mgr.create_session("10.0.0.1", "UA")  # should succeed since window=0


class TestSessionCleanup:
    def test_cleanup_expired(self):
        mgr = SessionManager(
            max_session_age=0, max_sessions_per_ip=100, rate_limit_window=60
        )
        for i in range(5):
            mgr.create_session(f"1.2.3.{i}", "UA")
        time.sleep(0.01)
        removed = mgr.cleanup_expired()
        assert removed == 5

    def test_destroy_session(self, manager):
        s = manager.create_session("1.2.3.4", "UA")
        manager.destroy_session(s.session_id)
        with pytest.raises(SessionError):
            manager.validate_session(s.session_id, "1.2.3.4", "UA")
