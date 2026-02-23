# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Resource Exhaustion Guard - Security Hardening Module
Monitor and limit resource usage to prevent DoS attacks and resource exhaustion.
"""
from __future__ import annotations


import asyncio
import os
import psutil
import time
from collections import defaultdict
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


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
        self.alert_callbacks: List[callable] = []
        self.monitoring_active = True
        self._start_monitoring_task()

    def add_alert_callback(self, callback: callable):
        """Add a callback function to be called when resource alerts are triggered."""
        self.alert_callbacks.append(callback)

    def _start_monitoring_task(self):
        """Start background monitoring task."""
        try:
            loop = asyncio.get_event_loop()
            loop.create_task(self._monitor_resources())
        except RuntimeError:
            # No event loop running, monitoring will be manual
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

            if cpu_percent > self.limits.alert_cpu_spike_threshold:
                self._alert_high_usage(
                    "cpu_spike",
                    {
                        "cpu_percent": cpu_percent,
                        "threshold": self.limits.alert_cpu_spike_threshold,
                    },
                )

            if memory_percent > self.limits.alert_memory_spike_threshold:
                self._alert_high_usage(
                    "memory_spike",
                    {
                        "memory_percent": memory_percent,
                        "threshold": self.limits.alert_memory_spike_threshold,
                    },
                )
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

    def check_resource(
        self, agent_id: str, resource_type: str, amount: int
    ) -> tuple[bool, str]:
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
            logger.error(
                f"Error checking resource {resource_type} for agent {agent_id}: {e}"
            )
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
            return (
                psutil.disk_io_counters()._asdict() if psutil.disk_io_counters() else {}
            )
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
            return True  # Allow by default on error

    def check_memory_limit(self, agent_id: str) -> bool:
        """Check if agent has exceeded memory limit."""
        try:
            usage = self.usage_by_agent[agent_id]
            process = psutil.Process()
            current_memory = process.memory_info().rss / (1024 * 1024)
            memory_used = current_memory - usage.memory_mb

            if memory_used > self.limits.max_memory_mb_per_agent:
                logger.warning(
                    f"Agent {agent_id} exceeded memory limit: {memory_used:.2f}MB"
                )
                return False

            return True
        except Exception as e:
            logger.error(f"Memory check failed for agent {agent_id}: {e}")
            return True

    def check_disk_write_limit(self, agent_id: str) -> bool:
        """Check if agent has exceeded disk write limit."""
        try:
            current_io = self._get_disk_io_stats()
            if not current_io or not self.baseline_disk_io:
                return True

            writes_mb = (
                current_io.get("write_bytes", 0)
                - self.baseline_disk_io.get("write_bytes", 0)
            ) / (1024 * 1024)

            if writes_mb > self.limits.max_disk_writes_mb_per_minute:
                logger.warning(
                    f"Agent {agent_id} exceeded disk write limit: {writes_mb:.2f}MB"
                )
                return False

            return True
        except Exception as e:
            logger.error(f"Disk write check failed for agent {agent_id}: {e}")
            return True

    def register_temp_file(self, agent_id: str, file_path: str) -> bool:
        """Register a temporary file for tracking."""
        temp_files = self.temp_files_by_agent[agent_id]

        if len(temp_files) >= self.limits.max_temp_files:
            logger.warning(
                f"Agent {agent_id} exceeded temp file limit: {len(temp_files)}"
            )
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


# Global instance for easy access
global_resource_guard = ResourceGuard()


def get_resource_guard() -> ResourceGuard:
    """Get the global resource guard instance."""
    return global_resource_guard


def setup_resource_guard(limits: Optional[ResourceLimits] = None) -> ResourceGuard:
    """Setup resource guard with custom limits."""
    global global_resource_guard
    global_resource_guard = ResourceGuard(limits)
    return global_resource_guard
