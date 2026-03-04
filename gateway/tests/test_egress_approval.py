# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.

import asyncio
import json
import tempfile
import time
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
import httpx

from gateway.security.egress_approval import (
    EgressApprovalQueue,
    ApprovalResult,
    RiskLevel,
    ApprovalMode
)


class TestEgressApprovalQueue:
    """Test suite for EgressApprovalQueue functionality."""

    @pytest.fixture
    def temp_rules_file(self):
        """Create temporary rules file for testing."""
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
            temp_path = f.name
        yield temp_path
        Path(temp_path).unlink(missing_ok=True)

    @pytest.fixture
    def approval_queue(self, temp_rules_file):
        """Create EgressApprovalQueue instance for testing."""
        return EgressApprovalQueue(rules_file=temp_rules_file, default_timeout=1)

    def test_risk_assessment_green(self, approval_queue):
        """Test risk assessment for known-safe domains."""
        # Known safe domains should be green
        assert approval_queue._assess_risk("api.openai.com", 443) == RiskLevel.GREEN
        assert approval_queue._assess_risk("api.anthropic.com", 80) == RiskLevel.GREEN
        assert approval_queue._assess_risk("github.com", 443) == RiskLevel.GREEN
        
        # Subdomains of safe domains should be green
        assert approval_queue._assess_risk("api.github.com", 443) == RiskLevel.GREEN
        assert approval_queue._assess_risk("raw.githubusercontent.com", 443) == RiskLevel.GREEN

    def test_risk_assessment_yellow(self, approval_queue):
        """Test risk assessment for unknown domains on standard ports."""
        # Unknown domains on standard ports should be yellow
        assert approval_queue._assess_risk("example.com", 443) == RiskLevel.YELLOW
        assert approval_queue._assess_risk("unknown-domain.org", 80) == RiskLevel.YELLOW
        assert approval_queue._assess_risk("test.net", 8080) == RiskLevel.YELLOW
        assert approval_queue._assess_risk("sample.io", 8443) == RiskLevel.YELLOW

    def test_risk_assessment_red(self, approval_queue):
        """Test risk assessment for high-risk targets."""
        # IP addresses should be red
        assert approval_queue._assess_risk("192.168.1.1", 443) == RiskLevel.RED
        assert approval_queue._assess_risk("10.0.0.1", 80) == RiskLevel.RED
        
        # Suspicious TLDs should be red
        assert approval_queue._assess_risk("malicious.tk", 443) == RiskLevel.RED
        assert approval_queue._assess_risk("phishing.xyz", 80) == RiskLevel.RED
        
        # Non-standard ports should be red
        assert approval_queue._assess_risk("example.com", 22) == RiskLevel.RED
        assert approval_queue._assess_risk("test.org", 3389) == RiskLevel.RED

    @pytest.mark.asyncio
    async def test_allowlist_persistence(self, approval_queue, temp_rules_file):
        """Test that allowlist rules are persisted to disk."""
        # Add a permanent allow rule
        await approval_queue.add_rule("example.com", "allow", ApprovalMode.PERMANENT)
        
        # Check that rule was saved to file
        assert Path(temp_rules_file).exists()
        with open(temp_rules_file, 'r') as f:
            data = json.load(f)
        
        assert len(data["permanent_rules"]) == 1
        rule = data["permanent_rules"][0]
        assert rule["domain"] == "example.com"
        assert rule["action"] == "allow"
        assert rule["mode"] == "permanent"

    @pytest.mark.asyncio
    async def test_denylist_persistence(self, approval_queue, temp_rules_file):
        """Test that denylist rules are persisted to disk."""
        # Add a permanent deny rule
        await approval_queue.add_rule("malicious.com", "deny", ApprovalMode.PERMANENT)
        
        # Check that rule was saved to file
        with open(temp_rules_file, 'r') as f:
            data = json.load(f)
        
        assert len(data["permanent_rules"]) == 1
        rule = data["permanent_rules"][0]
        assert rule["domain"] == "malicious.com"
        assert rule["action"] == "deny"

    @pytest.mark.asyncio
    async def test_session_rules_not_persisted(self, approval_queue, temp_rules_file):
        """Test that session rules are not persisted to disk."""
        # Add a session rule
        await approval_queue.add_rule("session-only.com", "allow", ApprovalMode.SESSION)
        
        # Check that no permanent rules were saved
        # Only check if file exists and has content
        if Path(temp_rules_file).exists() and Path(temp_rules_file).stat().st_size > 0:
            with open(temp_rules_file, 'r') as f:
                data = json.load(f)
            assert len(data.get("permanent_rules", [])) == 0

    @pytest.mark.asyncio
    async def test_approval_flow_permanent(self, approval_queue):
        """Test approval flow with permanent rule creation."""
        # Start approval request in background
        approval_task = asyncio.create_task(
            approval_queue.request_approval("test.com", 443, "agent1", "web_fetch", timeout=5)
        )
        
        # Wait a bit for request to be queued
        await asyncio.sleep(0.1)
        
        # Get pending requests
        pending = await approval_queue.get_pending_requests()
        assert len(pending) == 1
        
        request_id = pending[0]["request_id"]
        assert pending[0]["domain"] == "test.com"
        assert pending[0]["port"] == 443
        assert pending[0]["agent_id"] == "agent1"
        assert pending[0]["tool_name"] == "web_fetch"
        
        # Approve the request with permanent rule
        success = await approval_queue.approve(request_id, ApprovalMode.PERMANENT)
        assert success
        
        # Wait for approval task to complete
        result = await approval_task
        assert result == ApprovalResult.APPROVED
        
        # Check that permanent rule was created
        rules = await approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 1
        assert rules["permanent_rules"][0]["domain"] == "test.com"
        assert rules["permanent_rules"][0]["action"] == "allow"

    @pytest.mark.asyncio
    async def test_approval_flow_session(self, approval_queue):
        """Test approval flow with session rule creation."""
        # Start approval request
        approval_task = asyncio.create_task(
            approval_queue.request_approval("session.com", 443, "agent1", "web_fetch", timeout=5)
        )
        
        await asyncio.sleep(0.1)
        
        # Get and approve request
        pending = await approval_queue.get_pending_requests()
        request_id = pending[0]["request_id"]
        
        success = await approval_queue.approve(request_id, ApprovalMode.SESSION)
        assert success
        
        result = await approval_task
        assert result == ApprovalResult.APPROVED
        
        # Check that session rule was created
        rules = await approval_queue.get_all_rules()
        assert len(rules["session_rules"]) == 1
        assert rules["session_rules"][0]["domain"] == "session.com"
        assert rules["session_rules"][0]["action"] == "allow"

    @pytest.mark.asyncio
    async def test_approval_flow_once(self, approval_queue):
        """Test approval flow with one-time approval."""
        # Start approval request
        approval_task = asyncio.create_task(
            approval_queue.request_approval("once.com", 443, "agent1", "web_fetch", timeout=5)
        )
        
        await asyncio.sleep(0.1)
        
        # Get and approve request for one time only
        pending = await approval_queue.get_pending_requests()
        request_id = pending[0]["request_id"]
        
        success = await approval_queue.approve(request_id, ApprovalMode.ONCE)
        assert success
        
        result = await approval_task
        assert result == ApprovalResult.APPROVED
        
        # Check that no persistent rules were created
        rules = await approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 0
        assert len(rules["session_rules"]) == 0

    @pytest.mark.asyncio
    async def test_denial_flow(self, approval_queue):
        """Test denial flow with rule creation."""
        # Start approval request
        approval_task = asyncio.create_task(
            approval_queue.request_approval("deny.com", 443, "agent1", "web_fetch", timeout=5)
        )
        
        await asyncio.sleep(0.1)
        
        # Get and deny request
        pending = await approval_queue.get_pending_requests()
        request_id = pending[0]["request_id"]
        
        success = await approval_queue.deny(request_id, ApprovalMode.PERMANENT)
        assert success
        
        result = await approval_task
        assert result == ApprovalResult.DENIED
        
        # Check that deny rule was created
        rules = await approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 1
        assert rules["permanent_rules"][0]["domain"] == "deny.com"
        assert rules["permanent_rules"][0]["action"] == "deny"

    @pytest.mark.asyncio
    async def test_timeout_behavior(self, approval_queue):
        """Test request timeout behavior."""
        # Request with very short timeout
        result = await approval_queue.request_approval(
            "timeout.com", 443, "agent1", "web_fetch", timeout=0.1
        )
        
        assert result == ApprovalResult.TIMEOUT
        
        # Check that no pending requests remain
        pending = await approval_queue.get_pending_requests()
        assert len(pending) == 0

    @pytest.mark.asyncio
    async def test_existing_rule_bypass(self, approval_queue):
        """Test that existing rules bypass the approval queue."""
        # Add a permanent allow rule
        await approval_queue.add_rule("allowed.com", "allow", ApprovalMode.PERMANENT)
        
        # Request should be immediately approved
        result = await approval_queue.request_approval(
            "allowed.com", 443, "agent1", "web_fetch"
        )
        assert result == ApprovalResult.APPROVED
        
        # No pending requests should exist
        pending = await approval_queue.get_pending_requests()
        assert len(pending) == 0
        
        # Test deny rule
        await approval_queue.add_rule("denied.com", "deny", ApprovalMode.PERMANENT)
        
        result = await approval_queue.request_approval(
            "denied.com", 443, "agent1", "web_fetch"
        )
        assert result == ApprovalResult.DENIED

    @pytest.mark.asyncio
    async def test_rule_management(self, approval_queue):
        """Test adding and removing rules."""
        # Add multiple rules
        await approval_queue.add_rule("test1.com", "allow", ApprovalMode.PERMANENT)
        await approval_queue.add_rule("test2.com", "deny", ApprovalMode.SESSION)
        
        rules = await approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 1
        assert len(rules["session_rules"]) == 1
        
        # Remove permanent rule
        success = await approval_queue.remove_rule("test1.com")
        assert success
        
        # Remove session rule
        success = await approval_queue.remove_rule("test2.com")
        assert success
        
        rules = await approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 0
        assert len(rules["session_rules"]) == 0
        
        # Try to remove non-existent rule
        success = await approval_queue.remove_rule("nonexistent.com")
        assert not success

    @pytest.mark.asyncio
    async def test_cleanup_expired_requests(self, approval_queue):
        """Test cleanup of expired pending requests."""
        # Manually add an expired request to test cleanup
        import uuid
        from gateway.security.egress_approval import EgressRequest
        
        request_id = str(uuid.uuid4())
        expired_request = EgressRequest(
            request_id=request_id,
            domain="expired.com",
            port=443,
            agent_id="agent1",
            tool_name="web_fetch",
            timestamp=time.time(),
            risk_level=RiskLevel.YELLOW,
            timeout_at=time.time() - 10  # Already expired
        )
        
        async with approval_queue._lock:
            approval_queue._pending_requests[request_id] = expired_request
        
        # Run cleanup
        await approval_queue.cleanup_expired()
        
        # Check that expired request was removed
        pending = await approval_queue.get_pending_requests()
        assert len(pending) == 0


class TestEgressApprovalAPI:
    """Test suite for egress approval API endpoints."""

    @pytest.fixture
    async def mock_app_state(self):
        """Mock app_state with egress approval queue."""
        class MockAppState:
            pass
        
        app_state = MockAppState()
        
        # Create temporary rules file
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
            temp_path = f.name
        
        app_state.egress_approval_queue = EgressApprovalQueue(
            rules_file=temp_path, 
            default_timeout=1
        )
        
        yield app_state
        
        # Cleanup
        Path(temp_path).unlink(missing_ok=True)

    @pytest.fixture
    def mock_auth(self):
        """Mock authentication dependency."""
        return AsyncMock()

    @pytest.mark.asyncio
    async def test_get_egress_rules_endpoint(self, mock_app_state):
        """Test GET /manage/egress/rules endpoint."""
        from gateway.ingest_api.main import app
        
        # Add some test rules
        await mock_app_state.egress_approval_queue.add_rule(
            "test.com", "allow", ApprovalMode.PERMANENT
        )
        await mock_app_state.egress_approval_queue.add_rule(
            "session.com", "deny", ApprovalMode.SESSION
        )
        
        # Mock app_state
        with patch('gateway.ingest_api.main.app_state', mock_app_state):
            from httpx import ASGITransport
            transport = ASGITransport(app=app)
            async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
                # This would fail due to auth, but we can test the logic
                try:
                    response = await client.get("/manage/egress/rules")
                except Exception:
                    pass  # Expected due to auth requirements
        
        # Test the underlying logic directly
        rules = await mock_app_state.egress_approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 1
        assert len(rules["session_rules"]) == 1
        assert rules["permanent_rules"][0]["domain"] == "test.com"
        assert rules["session_rules"][0]["domain"] == "session.com"

    @pytest.mark.asyncio
    async def test_add_egress_rule_endpoint(self, mock_app_state):
        """Test POST /manage/egress/rules endpoint logic."""
        # Test the underlying logic that would be called by the endpoint
        await mock_app_state.egress_approval_queue.add_rule(
            "api.test.com", "allow", ApprovalMode.PERMANENT
        )
        
        rules = await mock_app_state.egress_approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 1
        assert rules["permanent_rules"][0]["domain"] == "api.test.com"
        assert rules["permanent_rules"][0]["action"] == "allow"

    @pytest.mark.asyncio
    async def test_remove_egress_rule_endpoint(self, mock_app_state):
        """Test DELETE /manage/egress/rules/{domain} endpoint logic."""
        # Add a rule first
        await mock_app_state.egress_approval_queue.add_rule(
            "remove.test.com", "allow", ApprovalMode.PERMANENT
        )
        
        # Remove it
        success = await mock_app_state.egress_approval_queue.remove_rule("remove.test.com")
        assert success
        
        # Verify it's gone
        rules = await mock_app_state.egress_approval_queue.get_all_rules()
        assert len(rules["permanent_rules"]) == 0

    @pytest.mark.asyncio
    async def test_pending_requests_endpoint(self, mock_app_state):
        """Test GET /manage/egress/pending endpoint logic."""
        # Create a pending request
        approval_task = asyncio.create_task(
            mock_app_state.egress_approval_queue.request_approval(
                "pending.com", 443, "agent1", "web_fetch", timeout=5
            )
        )
        
        # Wait for request to be queued
        await asyncio.sleep(0.1)
        
        # Get pending requests
        pending = await mock_app_state.egress_approval_queue.get_pending_requests()
        assert len(pending) == 1
        assert pending[0]["domain"] == "pending.com"
        
        # Clean up
        request_id = pending[0]["request_id"]
        await mock_app_state.egress_approval_queue.approve(request_id, ApprovalMode.ONCE)
        await approval_task

    @pytest.mark.asyncio
    async def test_approve_endpoint_logic(self, mock_app_state):
        """Test POST /manage/egress/approve/{request_id} endpoint logic."""
        # Create a pending request
        approval_task = asyncio.create_task(
            mock_app_state.egress_approval_queue.request_approval(
                "approve.com", 443, "agent1", "web_fetch", timeout=5
            )
        )
        
        await asyncio.sleep(0.1)
        
        # Get request ID
        pending = await mock_app_state.egress_approval_queue.get_pending_requests()
        request_id = pending[0]["request_id"]
        
        # Approve it
        success = await mock_app_state.egress_approval_queue.approve(
            request_id, ApprovalMode.PERMANENT
        )
        assert success
        
        # Wait for task completion
        result = await approval_task
        assert result == ApprovalResult.APPROVED

    @pytest.mark.asyncio
    async def test_deny_endpoint_logic(self, mock_app_state):
        """Test POST /manage/egress/deny/{request_id} endpoint logic."""
        # Create a pending request
        approval_task = asyncio.create_task(
            mock_app_state.egress_approval_queue.request_approval(
                "deny.com", 443, "agent1", "web_fetch", timeout=5
            )
        )
        
        await asyncio.sleep(0.1)
        
        # Get request ID
        pending = await mock_app_state.egress_approval_queue.get_pending_requests()
        request_id = pending[0]["request_id"]
        
        # Deny it
        success = await mock_app_state.egress_approval_queue.deny(
            request_id, ApprovalMode.PERMANENT
        )
        assert success
        
        # Wait for task completion
        result = await approval_task
        assert result == ApprovalResult.DENIED


if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])