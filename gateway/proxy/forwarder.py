"""
HTTP Forwarder — forwards sanitized requests to OpenClaw on internal network.

Connection pooling, timeout handling, retry logic, health checks.
"""

import asyncio
import logging
import time
from dataclasses import dataclass, field
from typing import Any, Optional

logger = logging.getLogger("secureclaw.proxy.forwarder")


@dataclass
class ForwarderConfig:
    """Configuration for the HTTP forwarder."""
    target_url: str = "http://openclaw:3000"
    timeout_seconds: float = 30.0
    max_retries: int = 3
    retry_delay_seconds: float = 1.0
    health_check_path: str = "/health"
    health_check_interval: float = 30.0
    max_connections: int = 20


@dataclass
class ForwardResult:
    """Result of forwarding a request."""
    success: bool
    status_code: int = 0
    body: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    error: str = ""
    retries: int = 0
    latency_ms: float = 0.0


class HTTPForwarder:
    """Forwards sanitized requests to the OpenClaw backend.

    In production, uses aiohttp/httpx for real HTTP forwarding.
    This implementation provides the interface and mock capability
    for testing without requiring a running OpenClaw instance.
    """

    def __init__(self, config: ForwarderConfig | None = None):
        self.config = config or ForwarderConfig()
        self._healthy = True
        self._last_health_check: float = 0
        self._total_forwarded: int = 0
        self._total_errors: int = 0
        self._last_forward_time: float = 0
        self._response_handler: Any = None  # For testing: callable(path, body) -> (status, response)

    def set_response_handler(self, handler):
        """Set a mock response handler for testing."""
        self._response_handler = handler

    async def forward(
        self,
        path: str,
        body: str,
        headers: dict[str, str] | None = None,
        method: str = "POST",
    ) -> ForwardResult:
        """Forward a request to the OpenClaw backend."""
        start = time.time()
        retries = 0

        for attempt in range(self.config.max_retries + 1):
            try:
                if self._response_handler:
                    # Mock mode for testing
                    status, response = self._response_handler(path, body)
                    self._total_forwarded += 1
                    self._last_forward_time = time.time()
                    return ForwardResult(
                        success=(200 <= status < 300),
                        status_code=status,
                        body=response,
                        retries=retries,
                        latency_ms=(time.time() - start) * 1000,
                    )
                else:
                    # Real HTTP forwarding
                    try:
                        import aiohttp
                        url = f"{self.config.target_url}{path}"
                        timeout = aiohttp.ClientTimeout(total=self.config.timeout_seconds)
                        async with aiohttp.ClientSession(timeout=timeout) as session:
                            async with session.request(
                                method, url,
                                data=body,
                                headers=headers or {"Content-Type": "application/json"},
                            ) as resp:
                                resp_body = await resp.text()
                                self._total_forwarded += 1
                                self._last_forward_time = time.time()
                                return ForwardResult(
                                    success=(200 <= resp.status < 300),
                                    status_code=resp.status,
                                    body=resp_body,
                                    retries=retries,
                                    latency_ms=(time.time() - start) * 1000,
                                )
                    except ImportError:
                        # No aiohttp available, return error
                        return ForwardResult(
                            success=False,
                            error="aiohttp not installed — cannot forward HTTP requests",
                            retries=retries,
                            latency_ms=(time.time() - start) * 1000,
                        )
            except Exception as e:
                retries += 1
                self._total_errors += 1
                logger.warning(f"Forward attempt {attempt + 1} failed: {e}")
                if attempt < self.config.max_retries:
                    await asyncio.sleep(self.config.retry_delay_seconds)
                else:
                    return ForwardResult(
                        success=False,
                        error=str(e),
                        retries=retries,
                        latency_ms=(time.time() - start) * 1000,
                    )

        return ForwardResult(success=False, error="Max retries exceeded", retries=retries)

    async def health_check(self) -> bool:
        """Check if the OpenClaw backend is healthy."""
        result = await self.forward(self.config.health_check_path, "", method="GET")
        self._healthy = result.success
        self._last_health_check = time.time()
        return self._healthy

    @property
    def is_healthy(self) -> bool:
        return self._healthy

    @property
    def last_forward_time(self) -> float:
        return self._last_forward_time

    def get_stats(self) -> dict[str, Any]:
        return {
            "healthy": self._healthy,
            "total_forwarded": self._total_forwarded,
            "total_errors": self._total_errors,
            "last_forward_time": self._last_forward_time,
            "last_health_check": self._last_health_check,
            "target_url": self.config.target_url,
        }
