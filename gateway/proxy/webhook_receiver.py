# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Webhook Receiver — receives Telegram/channel webhooks, routes through pipeline.

Provides FastAPI routes that sit in front of OpenClaw, ensuring all
inbound webhooks pass through the SecurityPipeline before forwarding.
Now includes per-user session isolation.
"""


import json
import logging
import time
from pathlib import Path
from typing import Any

from gateway.security.session_manager import UserSessionManager

logger = logging.getLogger("agentshroud.proxy.webhook_receiver")


class WebhookReceiver:
    """Receives webhooks and routes them through the security pipeline.

    In production, this provides FastAPI routes. For testing, the
    process_webhook method can be called directly.
    """

    def __init__(self, pipeline=None, forwarder=None, session_manager=None,
                 workspace_path: str = "/home/node/.openclaw/workspace"):
        self.pipeline = pipeline
        self.forwarder = forwarder

        # Initialize session manager if not provided and in production environment
        if session_manager is None:
            try:
                base_workspace = Path(workspace_path)
                # Only initialize if the base path exists or can be created
                if base_workspace.exists() or self._can_create_directory(base_workspace):
                    # TODO: Load owner_user_id from config
                    from gateway.security.rbac_config import RBACConfig
                    owner_user_id = RBACConfig().owner_user_id
                    self.session_manager = UserSessionManager(
                        base_workspace=base_workspace,
                        owner_user_id=owner_user_id
                    )
                else:
                    logger.warning("Cannot create workspace directory - session isolation disabled")
                    self.session_manager = None
            except Exception as e:
                logger.warning(f"Failed to initialize session manager: {e} - session isolation disabled")
                self.session_manager = None
        else:
            self.session_manager = session_manager
            
        self._stats = {
            "webhooks_received": 0,
            "webhooks_forwarded": 0,
            "webhooks_blocked": 0,
            "last_webhook_time": 0.0,
        }

    def _can_create_directory(self, path: Path) -> bool:
        """Check if we can create the given directory path."""
        try:
            # Try creating a temporary test directory to check permissions
            test_path = path.parent / ".test_mkdir"
            test_path.mkdir(parents=True, exist_ok=True)
            test_path.rmdir()
            return True
        except Exception:
            return False

    async def process_webhook(
        self,
        payload: dict[str, Any],
        source: str = "telegram",
        agent_id: str = "default",
    ) -> dict[str, Any]:
        """Process an incoming webhook through the security pipeline."""
        self._stats["webhooks_received"] += 1
        self._stats["last_webhook_time"] = time.time()

        message_text = self._extract_message(payload)
        if not message_text:
            return {"status": "skipped", "reason": "no message text in payload"}

        # Extract user ID from payload for session isolation
        user_id = None
        if self.session_manager:
            user_id = self._extract_user_id(payload, source)
            if not user_id:
                logger.warning(f"No user ID found in {source} payload")
                user_id = "anonymous"

            logger.info(f"Processing message from user {user_id}")

            # Store user message in conversation history
            self.session_manager.add_conversation_message(
                user_id=user_id,
                role="user", 
                content=message_text,
                metadata={"source": source, "timestamp": time.time()}
            )

        if self.pipeline:
            result = await self.pipeline.process_inbound(
                message=message_text,
                agent_id=agent_id,
                source=source,
                metadata={
                    "webhook_source": source,
                    "user_id": user_id,
                    "session_isolated": True
                },
            )

            if result.blocked:
                self._stats["webhooks_blocked"] += 1
                return {
                    "status": "blocked",
                    "reason": result.block_reason,
                    "prompt_score": result.prompt_score,
                    "patterns": result.prompt_patterns,
                }

            if result.queued_for_approval:
                return {
                    "status": "queued",
                    "approval_id": result.approval_id,
                    "message": "Action queued for approval",
                }

            # Prepare session-isolated payload if session manager is available
            if self.session_manager and user_id:
                session_payload = self._prepare_session_payload(
                    payload, result.sanitized_message, user_id
                )
            else:
                session_payload = self._replace_message(payload, result.sanitized_message)

            if self.forwarder:
                forward_result = await self.forwarder.forward(
                    path="/webhook",
                    body=json.dumps(session_payload),
                )

                if forward_result.success:
                    self._stats["webhooks_forwarded"] += 1

                    # Store assistant response in conversation history
                    if forward_result.body and self.session_manager and user_id:
                        self.session_manager.add_conversation_message(
                            user_id=user_id,
                            role="assistant",
                            content=forward_result.body,
                            metadata={"source": source, "timestamp": time.time()}
                        )

                    if forward_result.body and self.pipeline:
                        outbound = await self.pipeline.process_outbound(
                            response=forward_result.body,
                            agent_id=agent_id,
                        )
                        return {
                            "status": "forwarded",
                            "response": outbound.sanitized_message,
                            "inbound_sanitized": result.pii_redaction_count > 0,
                            "outbound_sanitized": outbound.pii_redaction_count > 0,
                            "user_id": user_id
                        }

                    return {
                        "status": "forwarded",
                        "response": forward_result.body,
                        "user_id": user_id
                    }
                else:
                    return {
                        "status": "forward_error",
                        "error": forward_result.error,
                        "user_id": user_id
                    }

            return {
                "status": "processed",
                "sanitized": result.sanitized_message,
                "pii_stripped": result.pii_redaction_count > 0,
                "audit_id": result.audit_entry_id,
                "user_id": user_id
            }

        logger.warning("Webhook received with no pipeline configured!")
        return {"status": "passthrough", "warning": "no security pipeline", "user_id": user_id}

    def _prepare_session_payload(
        self, original_payload: dict[str, Any], sanitized_message: str, user_id: str
    ) -> dict[str, Any]:
        """Prepare payload with session context injection."""
        # Get session context
        session_context = self.session_manager.get_session_context(user_id)
        session_prompt = self.session_manager.get_session_prompt_addition(user_id)
        
        # Create modified payload with session context
        session_payload = self._replace_message(original_payload, sanitized_message)
        
        # Inject session context into the payload
        if "session_context" not in session_payload:
            session_payload["session_context"] = {}
            
        session_payload["session_context"].update({
            "user_id": user_id,
            "workspace_path": session_context["workspace_path"],
            "memory_path": session_context["memory_path"],
            "trust_level": session_context["trust_level"],
            "conversation_history": session_context["conversation_history"],
            "isolation_prompt": session_prompt,
            "workspace_restricted": True
        })
        
        return session_payload

    @staticmethod
    def _extract_user_id(payload: dict[str, Any], source: str) -> str | None:
        """Extract user ID from webhook payload based on source platform."""
        if source == "telegram":
            # Standard Telegram webhook structure
            if "message" in payload and isinstance(payload["message"], dict):
                message = payload["message"]
                # Check for user in 'from' field
                if "from" in message and isinstance(message["from"], dict):
                    user_id = message["from"].get("id")
                    if user_id:
                        return str(user_id)
                
                # Fallback: check for chat id (in group chats)
                if "chat" in message and isinstance(message["chat"], dict):
                    chat_id = message["chat"].get("id")
                    if chat_id:
                        return str(chat_id)
            
            # Direct user_id field (for testing)
            if "user_id" in payload:
                return str(payload["user_id"])
                
        # For other platforms, add extraction logic here
        logger.warning(f"Could not extract user_id from {source} payload")
        return None

    @staticmethod
    def _extract_message(payload: dict[str, Any]) -> str | None:
        """Extract message text from webhook payload (Telegram format)."""
        if "message" in payload and isinstance(payload["message"], dict):
            return payload["message"].get("text")
        if "text" in payload:
            return payload["text"]
        if "content" in payload:
            return payload["content"]
        return None

    @staticmethod
    def _replace_message(payload: dict[str, Any], new_text: str) -> dict[str, Any]:
        """Replace message text in payload with sanitized version."""
        result = dict(payload)
        if "message" in result and isinstance(result["message"], dict):
            result["message"] = dict(result["message"])
            result["message"]["text"] = new_text
        elif "text" in result:
            result["text"] = new_text
        elif "content" in result:
            result["content"] = new_text
        return result

    def get_stats(self) -> dict[str, Any]:
        return dict(self._stats)