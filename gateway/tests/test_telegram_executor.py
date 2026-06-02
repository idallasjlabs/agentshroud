# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Regression guard for the gateway Telegram I/O ThreadPoolExecutor fix.

Prevents reduction of max_workers below 64, which would re-introduce the
long-poll starvation bug: getUpdates calls holding all asyncio executor threads
cause sendMessage/sendPhoto to time out with synthetic 504s.
"""

import inspect

from gateway.ingest_api import lifespan as _lifespan_module


def test_lifespan_installs_64_worker_executor():
    """lifespan startup must install ThreadPoolExecutor(max_workers=64)."""
    src = inspect.getsource(_lifespan_module)
    assert "max_workers=64" in src, (
        "lifespan must install ThreadPoolExecutor(max_workers=64) "
        "to prevent Telegram long-poll thread starvation"
    )
    assert "set_default_executor" in src, (
        "lifespan must call asyncio loop.set_default_executor() " "with the 64-worker executor"
    )
    assert "tg-io" in src, "ThreadPoolExecutor must use thread_name_prefix='tg-io' for diagnostics"
