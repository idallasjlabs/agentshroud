# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
import logging

import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

from .server import app  # noqa: E402

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8765,
        log_level="info",
        # WS-level ping/pong disabled — Tailscale Funnel does not reliably relay
        # WebSocket control frames (PING/PONG) through the DERP relay path.
        # With ws_ping_interval set, the server's 20 s pong-timeout fires and
        # force-closes the connection (dirty close) every ~30 s.
        # Application-level keepalive ({"heartbeat":1} every 4 s in server.py)
        # keeps the Funnel relay and hotspot NAT alive without control frames.
        ws_ping_interval=None,
        ws_ping_timeout=None,
    )
