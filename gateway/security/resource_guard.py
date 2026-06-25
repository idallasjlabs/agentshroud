# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Resource Exhaustion Guard - Security Hardening Module
Monitor and limit resource usage to prevent DoS attacks and resource exhaustion.
"""

from __future__ import annotations

import asyncio
import logging
import os
import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import psutil

logger = logging.getLogger(__name__)


class VRAMHeadroomError(Exception):
    """Raised when a local-model call is rejected because estimated VRAM usage
    would exceed the configured headroom threshold.

    This is a hard-reject (fail-closed) to prevent OOM crashes on the GPU host.
    The caller should either route to a smaller model or return a graceful error.
    """


# ---------------------------------------------------------------------------
# VRAM estimation constants
# ---------------------------------------------------------------------------

# Bytes of KV-cache VRAM per token per layer for FP16 attention heads (2 bytes × 2 heads).
# This is a conservative estimate; actual usage varies by model architecture.
_VRAM_BYTES_PER_TOKEN_PER_LAYER: int = 4

# Default number of transformer layers for estimation when model size is unknown.
# Covers up to 14B models (typical local deployment). Callers with model metadata
# should pass a more precise layer count.
_DEFAULT_TRANSFORMER_LAYERS: int = 40


@dataclass
class ResourceLimits:
    """Configuration for resource limits."""

    max_cpu_seconds_per_request: float = 30.0
    max_memory_mb_per_agent: int = 512
    max_disk_writes_mb_per_minute: int = 100
    max_temp_files: int = 1000
    max_open_files_per_agent: int = 100
    max_requests_per_minute: int = 300
    alert_cpu_spike_threshold: float = 80.0  # CPU % that triggers alert
    alert_memory_spike_threshold: float = 90.0  # Memory % that triggers alert
    # Number of consecutive 10-second samples that must exceed a threshold
    # before firing the alert.  Without debouncing, every ClamAV outbound scan,
    # audit-chain flush, or drift-detector pass briefly tripped the spike
    # threshold and produced an alert that AlertDispatcher rate-limited
    # downstream — pure noise.  3 samples = ~30 seconds of sustained pressure,
    # which is the real signal we want.
    alert_spike_debounce_samples: int = 3
    # VRAM headroom required before accepting a long-context local-model call.
    # Set to 0 to disable VRAM pre-flight checks (e.g. in CI / cloud-only mode).
    max_vram_headroom_mb: int = 0


@dataclass
class ResourceUsage:
    """Current resource usage metrics."""

    cpu_seconds: float = 0.0
    memory_mb: float = 0.0
    disk_writes_mb: float = 0.0
    temp_files_count: int = 0
    request_count: int = 0
    open_files_count: int = 0
    last_reset: float = 0.0


class ResourceGuard:
    """Monitor and limit resource usage per agent/request."""

    def __init__(self, limits: Optional[ResourceLimits] = None):
        self.limits = limits or ResourceLimits()
        self.usage_by_agent: Dict[str, ResourceUsage] = defaultdict(ResourceUsage)
        self.baseline_disk_io = self._get_disk_io_stats()
        self.temp_files_by_agent: Dict[str, List[str]] = defaultdict(list)
        self.alert_callbacks: List[Callable[..., Any]] = []
        self.monitoring_active = True
        self._monitor_task: Optional[asyncio.Task] = None
        # Consecutive-over-threshold counters for the spike debounce.
        # Reset whenever a sample comes in under threshold.
        self._cpu_over_count: int = 0
        self._memory_over_count: int = 0
        self._start_monitoring_task()

    def add_alert_callback(self, callback: Callable[..., Any]):
        """Add a callback function to be called when resource alerts are triggered."""
        self.alert_callbacks.append(callback)

    def _start_monitoring_task(self):
        """Start background monitoring task."""
        try:
            loop = asyncio.get_running_loop()
            self._monitor_task = loop.create_task(self._monitor_resources())
        except RuntimeError:
            # No event loop running, monitoring will be manual
            pass

    async def stop(self):
        """Stop background monitoring task cleanly."""
        self.monitoring_active = False
        if self._monitor_task and not self._monitor_task.done():
            self._monitor_task.cancel()
            try:
                await self._monitor_task
            except asyncio.CancelledError:
                pass

    def __del__(self):
        """Best-effort cleanup for test contexts that don't call stop()."""
        self.monitoring_active = False
        task = getattr(self, "_monitor_task", None)
        if task and not task.done():
            try:
                task.cancel()
            except RuntimeError:
                # Event loop already closed during interpreter/test teardown
                pass

    async def _monitor_resources(self):
        """Background task to monitor resource usage and trigger alerts."""
        while self.monitoring_active:
            try:
                await asyncio.sleep(10)  # Check every 10 seconds
                self._check_system_resources()
                self._cleanup_expired_usage()
            except Exception as e:
                logger.error(f"Resource monitoring error: {e}")

    def _check_system_resources(self):
        """Check system-wide resource usage for anomalies (synchronous)."""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent

            debounce = max(1, self.limits.alert_spike_debounce_samples)

            if cpu_percent > self.limits.alert_cpu_spike_threshold:
                self._cpu_over_count += 1
                if self._cpu_over_count == debounce:
                    self._alert_high_usage(
                        "cpu_spike",
                        {
                            "cpu_percent": cpu_percent,
                            "threshold": self.limits.alert_cpu_spike_threshold,
                            "consecutive_samples": self._cpu_over_count,
                        },
                    )
            else:
                self._cpu_over_count = 0

            if memory_percent > self.limits.alert_memory_spike_threshold:
                self._memory_over_count += 1
                if self._memory_over_count == debounce:
                    self._alert_high_usage(
                        "memory_spike",
                        {
                            "memory_percent": memory_percent,
                            "threshold": self.limits.alert_memory_spike_threshold,
                            "consecutive_samples": self._memory_over_count,
                        },
                    )
            else:
                self._memory_over_count = 0
        except Exception as e:
            logger.error(f"System resource check failed: {e}")

    def _alert_high_usage(self, alert_type: str, data: Dict[str, Any]):
        """Trigger a resource usage alert synchronously."""
        alert_data = {
            "type": alert_type,
            "timestamp": time.time(),
            "data": data,
            "source": "resource_guard",
        }
        for callback in self.alert_callbacks:
            try:
                callback(alert_data)
            except Exception as e:
                logger.error(f"Alert callback failed: {e}")

    def check_resource(self, agent_id: str, resource_type: str, amount: int) -> tuple[bool, str]:
        """Check if resource usage is allowed for an agent.

        Args:
            agent_id: Unique agent identifier
            resource_type: Type of resource ('disk_writes_mb', 'temp_files', 'requests')
            amount: Amount to check/add

        Returns:
            Tuple of (allowed: bool, reason: str)
        """
        try:
            usage = self.usage_by_agent[agent_id]

            # Reset sliding window if expired (60 seconds)
            if time.time() - usage.last_reset > 60:
                usage.disk_writes_mb = 0.0
                usage.request_count = 0
                usage.last_reset = time.time()

            if resource_type == "disk_writes_mb":
                total = usage.disk_writes_mb + amount
                if total > self.limits.max_disk_writes_mb_per_minute:
                    return (
                        False,
                        f"Agent {agent_id} disk_writes_mb ({total:.1f}) exceeds limit ({self.limits.max_disk_writes_mb_per_minute})",
                    )
                usage.disk_writes_mb = total
                return True, ""

            elif resource_type == "temp_files":
                total = usage.temp_files_count + amount
                if total > self.limits.max_temp_files:
                    return (
                        False,
                        f"Agent {agent_id} temp_files ({total}) exceeds limit ({self.limits.max_temp_files})",
                    )
                usage.temp_files_count = total
                return True, ""

            elif resource_type == "requests":
                total = usage.request_count + amount
                if total > self.limits.max_requests_per_minute:
                    return (
                        False,
                        f"Agent {agent_id} requests ({total}) exceeds limit ({self.limits.max_requests_per_minute})",
                    )
                usage.request_count = total
                return True, ""

            else:
                raise ValueError(f"Unknown resource type: {resource_type}")

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error checking resource {resource_type} for agent {agent_id}: {e}")
            return False, f"Error checking resource: {e}"

    def _cleanup_expired_usage(self):
        """Clean up old usage data (older than 5 minutes)."""
        current_time = time.time()
        cutoff_time = current_time - 300  # 5 minutes

        expired_agents = []
        for agent_id, usage in self.usage_by_agent.items():
            if usage.last_reset < cutoff_time:
                expired_agents.append(agent_id)

        for agent_id in expired_agents:
            del self.usage_by_agent[agent_id]
            if agent_id in self.temp_files_by_agent:
                del self.temp_files_by_agent[agent_id]

    def _get_disk_io_stats(self) -> Dict[str, Any]:
        """Get current disk I/O statistics."""
        try:
            io_counters = psutil.disk_io_counters()
            return io_counters._asdict() if io_counters else {}
        except Exception:
            return {}

    def start_request_tracking(self, agent_id: str) -> str:
        """Start tracking resources for a specific agent/request."""
        usage = self.usage_by_agent[agent_id]
        usage.last_reset = time.time()

        # Track current process stats as baseline
        try:
            process = psutil.Process()
            usage.cpu_seconds = process.cpu_times().user + process.cpu_times().system
            usage.memory_mb = process.memory_info().rss / (1024 * 1024)
            usage.open_files_count = len(process.open_files())
        except Exception as e:
            logger.warning(f"Failed to get baseline process stats: {e}")

        return agent_id

    def check_cpu_limit(self, agent_id: str) -> bool:
        """Check if agent has exceeded CPU time limit."""
        try:
            usage = self.usage_by_agent[agent_id]
            process = psutil.Process()
            current_cpu = process.cpu_times().user + process.cpu_times().system
            cpu_used = current_cpu - usage.cpu_seconds

            if cpu_used > self.limits.max_cpu_seconds_per_request:
                logger.warning(f"Agent {agent_id} exceeded CPU limit: {cpu_used:.2f}s")
                return False

            return True
        except Exception as e:
            logger.error(f"CPU check failed for agent {agent_id}: {e}")
            return False  # Fail-closed: deny on error

    def check_memory_limit(self, agent_id: str) -> bool:
        """Check if agent has exceeded memory limit."""
        try:
            usage = self.usage_by_agent[agent_id]
            process = psutil.Process()
            current_memory = process.memory_info().rss / (1024 * 1024)
            memory_used = current_memory - usage.memory_mb

            if memory_used > self.limits.max_memory_mb_per_agent:
                logger.warning(f"Agent {agent_id} exceeded memory limit: {memory_used:.2f}MB")
                return False

            return True
        except Exception as e:
            logger.error(f"Memory check failed for agent {agent_id}: {e}")
            return False  # Fail-closed: deny on error

    def check_disk_write_limit(self, agent_id: str) -> bool:
        """Check if agent has exceeded disk write limit."""
        try:
            current_io = self._get_disk_io_stats()
            if not current_io or not self.baseline_disk_io:
                return True

            writes_mb = (
                current_io.get("write_bytes", 0) - self.baseline_disk_io.get("write_bytes", 0)
            ) / (1024 * 1024)

            if writes_mb > self.limits.max_disk_writes_mb_per_minute:
                logger.warning(f"Agent {agent_id} exceeded disk write limit: {writes_mb:.2f}MB")
                return False

            return True
        except Exception as e:
            logger.error(f"Disk write check failed for agent {agent_id}: {e}")
            return False  # Fail-closed: deny on error

    def check_vram_headroom(
        self,
        agent_id: str,
        estimated_tokens: int,
        available_vram_mb: int,
        transformer_layers: int = _DEFAULT_TRANSFORMER_LAYERS,
    ) -> None:
        """Pre-flight VRAM headroom check before dispatching a long-context local-model call.

        Raises VRAMHeadroomError when the estimated KV-cache VRAM for the request
        would exhaust available VRAM below the configured headroom threshold.

        The check is skipped (passes silently) when:
        - limits.max_vram_headroom_mb == 0 (disabled)
        - available_vram_mb >= max_vram_headroom_mb (sufficient headroom)

        Args:
            agent_id: Agent/request identifier for logging.
            estimated_tokens: Total token count (input + output estimate) for the call.
            available_vram_mb: Free VRAM on the GPU host in megabytes.
            transformer_layers: Number of transformer layers (used for KV-cache estimate).

        Raises:
            VRAMHeadroomError: When available_vram_mb < max_vram_headroom_mb.

        Entry point: gateway/security/resource_guard.py:ResourceGuard.check_vram_headroom
        Routing: called by gateway/proxy/llm_proxy.py before local dispatch
        Handler: raises VRAMHeadroomError; caller routes to secondary model or returns error
        """
        threshold = self.limits.max_vram_headroom_mb
        if threshold == 0:
            # VRAM check disabled
            return

        if available_vram_mb >= threshold:
            return

        # Estimate KV-cache VRAM in MB for this request
        kv_cache_bytes = estimated_tokens * transformer_layers * _VRAM_BYTES_PER_TOKEN_PER_LAYER
        kv_cache_mb = kv_cache_bytes // (1024 * 1024)

        msg = (
            f"Agent {agent_id}: insufficient VRAM headroom for {estimated_tokens} token request. "
            f"Available: {available_vram_mb} MB, required threshold: {threshold} MB, "
            f"estimated KV-cache: {kv_cache_mb} MB. "
            f"Route to a smaller model or reduce context length."
        )
        logger.warning("ResourceGuard VRAM pre-flight rejected: %s", msg)
        raise VRAMHeadroomError(msg)

    def register_temp_file(self, agent_id: str, file_path: str) -> bool:
        """Register a temporary file for tracking."""
        temp_files = self.temp_files_by_agent[agent_id]

        if len(temp_files) >= self.limits.max_temp_files:
            logger.warning(f"Agent {agent_id} exceeded temp file limit: {len(temp_files)}")
            return False

        temp_files.append(file_path)
        return True

    def cleanup_temp_files(self, agent_id: str):
        """Clean up temporary files for an agent."""
        temp_files = self.temp_files_by_agent.get(agent_id, [])

        for file_path in temp_files:
            try:
                if os.path.exists(file_path):
                    os.unlink(file_path)
            except Exception as e:
                logger.warning(f"Failed to cleanup temp file {file_path}: {e}")

        if agent_id in self.temp_files_by_agent:
            del self.temp_files_by_agent[agent_id]

    def get_usage_stats(self, agent_id: Optional[str] = None) -> Dict[str, Any]:
        """Get current usage statistics."""
        if agent_id:
            usage = self.usage_by_agent.get(agent_id, ResourceUsage())
            return {
                "agent_id": agent_id,
                "cpu_seconds": usage.cpu_seconds,
                "memory_mb": usage.memory_mb,
                "disk_writes_mb": usage.disk_writes_mb,
                "temp_files_count": len(self.temp_files_by_agent.get(agent_id, [])),
                "open_files_count": usage.open_files_count,
                "last_reset": usage.last_reset,
            }
        else:
            return {
                "total_agents": len(self.usage_by_agent),
                "system_cpu_percent": psutil.cpu_percent(),
                "system_memory_percent": psutil.virtual_memory().percent,
                "limits": {
                    "max_cpu_seconds_per_request": self.limits.max_cpu_seconds_per_request,
                    "max_memory_mb_per_agent": self.limits.max_memory_mb_per_agent,
                    "max_disk_writes_mb_per_minute": self.limits.max_disk_writes_mb_per_minute,
                    "max_temp_files": self.limits.max_temp_files,
                },
            }

    def stop_monitoring(self):
        """Stop background monitoring."""
        self.monitoring_active = False


_global_resource_guard: Optional[ResourceGuard] = None


def get_resource_guard() -> ResourceGuard:
    """Get the global resource guard instance, creating it lazily on first call."""
    global _global_resource_guard
    if _global_resource_guard is None:
        _global_resource_guard = ResourceGuard()
    return _global_resource_guard


def setup_resource_guard(limits: Optional[ResourceLimits] = None) -> ResourceGuard:
    """Setup resource guard with custom limits."""
    global _global_resource_guard
    _global_resource_guard = ResourceGuard(limits)
    return _global_resource_guard
