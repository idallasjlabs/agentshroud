"""
Webhook Receiver — receives Telegram/channel webhooks, routes through pipeline.

Provides FastAPI routes that sit in front of OpenClaw, ensuring all
inbound webhooks pass through the SecurityPipeline before forwarding.
"""
from __future__ import annotations

import json
import logging
import time
from typing import Any

logger = logging.getLogger("secureclaw.proxy.webhook_receiver")


class WebhookReceiver:
    """Receives webhooks and routes them through the security pipeline.

    In production, this provides FastAPI routes. For testing, the
    process_webhook method can be called directly.
    """

    def __init__(self, pipeline=None, forwarder=None):
        self.pipeline = pipeline
        self.forwarder = forwarder
        self._stats = {
            "webhooks_received": 0,
            "webhooks_forwarded": 0,
            "webhooks_blocked": 0,
            "last_webhook_time": 0.0,
        }

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

        if self.pipeline:
            result = await self.pipeline.process_inbound(
                message=message_text,
                agent_id=agent_id,
                source=source,
                metadata={"webhook_source": source},
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

            sanitized_payload = self._replace_message(payload, result.sanitized_message)

            if self.forwarder:
                forward_result = await self.forwarder.forward(
                    path="/webhook",
                    body=json.dumps(sanitized_payload),
                )

                if forward_result.success:
                    self._stats["webhooks_forwarded"] += 1

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
                        }

                    return {
                        "status": "forwarded",
                        "response": forward_result.body,
                    }
                else:
                    return {
                        "status": "forward_error",
                        "error": forward_result.error,
                    }

            return {
                "status": "processed",
                "sanitized": result.sanitized_message,
                "pii_stripped": result.pii_redaction_count > 0,
                "audit_id": result.audit_entry_id,
            }

        logger.warning("Webhook received with no pipeline configured!")
        return {"status": "passthrough", "warning": "no security pipeline"}

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
