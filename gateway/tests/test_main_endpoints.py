# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Main Endpoints Integration Tests - P1 Middleware Wiring
Tests for main.py endpoint integration with middleware blocking.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient
from fastapi import HTTPException

from gateway.ingest_api.main import app
from gateway.ingest_api.models import ForwardRequest
from gateway.ingest_api.middleware import MiddlewareResult


class TestForwardEndpoint:
    """Test /forward endpoint with middleware integration."""
    
    def test_forward_middleware_blocking(self):
        """Test that middleware can block requests with HTTP 403."""
        
        # Mock middleware manager to block the request
        mock_middleware = MagicMock()
        mock_middleware.process.return_value = MiddlewareResult(
            allowed=False,
            reason="Test middleware block"
        )
        
        # Mock auth
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.middleware_manager = mock_middleware
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.post(
                    "/forward",
                    json={
                        "content": "test message",
                        "content_type": "text/plain",
                        "source": "api"
                    },
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should return 403 when middleware blocks
                assert response.status_code == 403
                assert "Request blocked by middleware" in response.json()["detail"]
                
                # Verify middleware was called
                mock_middleware.process.assert_called_once()
    
    def test_forward_middleware_allowed(self):
        """Test that middleware allows requests when they pass checks."""
        
        # Mock middleware manager to allow the request
        mock_middleware = MagicMock()
        mock_middleware.process.return_value = MiddlewareResult(
            allowed=True
        )
        
        # Mock other components
        mock_pipeline = MagicMock()
        mock_pipeline_result = MagicMock()
        mock_pipeline_result.blocked = False
        mock_pipeline_result.queued_for_approval = False
        mock_pipeline_result.sanitized_message = "test message"
        mock_pipeline_result.pii_redaction_count = 0
        mock_pipeline_result.pii_redactions = []
        mock_pipeline_result.audit_entry_id = "test-id"
        mock_pipeline_result.audit_hash = "test-hash"
        mock_pipeline_result.prompt_score = 0.0
        mock_pipeline.process_inbound = AsyncMock(return_value=mock_pipeline_result)
        
        mock_router = MagicMock()
        mock_target = MagicMock()
        mock_target.name = "test-agent"
        mock_router.resolve_target = AsyncMock(return_value=mock_target)
        mock_router.forward_to_agent = AsyncMock(return_value="response")
        
        mock_ledger = MagicMock()
        mock_ledger.log_ingest = AsyncMock(return_value="ledger-id")
        
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.middleware_manager = mock_middleware
            mock_app_state.pipeline = mock_pipeline
            mock_app_state.router = mock_router
            mock_app_state.ledger = mock_ledger
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.post(
                    "/forward",
                    json={
                        "content": "test message",
                        "content_type": "text/plain",
                        "source": "api"
                    },
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should succeed when middleware allows
                assert response.status_code == 201
                
                # Verify middleware was called
                mock_middleware.process.assert_called_once()
    
    def test_forward_middleware_error_handling(self):
        """Test that middleware errors cause requests to be blocked."""
        
        # Mock middleware manager to throw an exception
        mock_middleware = MagicMock()
        mock_middleware.process.side_effect = Exception("Middleware error")
        
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.middleware_manager = mock_middleware
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.post(
                    "/forward",
                    json={
                        "content": "test message",
                        "content_type": "text/plain",
                        "source": "api"
                    },
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should return 500 when middleware fails
                assert response.status_code == 500
                assert "Middleware processing failed" in response.json()["detail"]


class TestStatusEndpoint:
    """Test /status endpoint."""
    
    def test_status_endpoint(self):
        """Test basic status endpoint functionality."""
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            # Mock required app state components
            mock_app_state.config = MagicMock()
            mock_app_state.config.cors_origins = ["http://localhost:3000"]
            
            client = TestClient(app)
            
            response = client.get("/status")
            
            # Should return 200 OK
            assert response.status_code == 200
            assert "status" in response.json()


class TestApprovalEndpoints:
    """Test approval queue endpoints."""
    
    def test_approval_queue_list(self):
        """Test listing pending approvals."""
        
        mock_approval_queue = MagicMock()
        mock_approval_queue.list_pending.return_value = []
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.approval_queue = mock_approval_queue
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.get(
                    "/approval-queue",
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should return 200 OK
                assert response.status_code == 200
                assert isinstance(response.json(), list)
    
    def test_approval_decision(self):
        """Test making approval decisions."""
        
        mock_approval_queue = MagicMock()
        mock_approval_queue.approve = AsyncMock()
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.approval_queue = mock_approval_queue
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.post(
                    "/approve",
                    json={
                        "approval_id": "test-id",
                        "decision": "approved",
                        "reviewer": "test-user"
                    },
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should return 200 OK for valid approval
                assert response.status_code == 200


class TestMCPProxyEndpoint:
    """Test /mcp/proxy endpoint."""
    
    def test_mcp_proxy_endpoint(self):
        """Test MCP proxy endpoint basic functionality."""
        
        mock_mcp_proxy = MagicMock()
        mock_mcp_proxy.execute_tool = AsyncMock(return_value={
            "status": "success",
            "result": "test result"
        })
        mock_auth = MagicMock()
        
        with patch('gateway.ingest_api.main.app_state') as mock_app_state:
            mock_app_state.mcp_proxy = mock_mcp_proxy
            
            client = TestClient(app)
            
            # Mock auth dependency
            with patch('gateway.ingest_api.main.create_auth_dependency') as mock_auth_dep:
                mock_auth_dep.return_value = AsyncMock()
                
                response = client.post(
                    "/mcp/proxy",
                    json={
                        "server_name": "test-server",
                        "tool_name": "test-tool",
                        "arguments": {}
                    },
                    headers={"Authorization": "Bearer fake-token"}
                )
                
                # Should return 200 OK for successful proxy request
                assert response.status_code == 200
                result = response.json()
                assert "status" in result


class TestErrorHandling:
    """Test error handling across endpoints."""
    
    def test_404_error(self):
        """Test 404 handling for non-existent endpoints."""
        
        client = TestClient(app)
        
        response = client.get("/nonexistent")
        
        assert response.status_code == 404
    
    def test_method_not_allowed(self):
        """Test 405 handling for wrong HTTP methods."""
        
        client = TestClient(app)
        
        # Try GET on POST-only endpoint
        response = client.get("/forward")
        
        assert response.status_code == 405
