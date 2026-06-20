# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Voice Gateway — FastAPI app exposing GET /health and WebSocket /voice.

Per-connection state machine: IDLE → LISTENING → THINKING → SPEAKING → IDLE.
State events are sent as JSON text frames; audio data is binary (raw S16LE PCM).

Device → gateway protocol:
  • Text "LISTEN"  — device starting a new utterance
  • Binary frame   — raw S16LE 16 kHz mono PCM chunk
  • Text "END"     — utterance complete (button released / VAD timeout)

Gateway → device protocol:
  • Text JSON      — {"state": "listening|thinking|speaking|idle"}
  • Binary frame   — raw S16LE TTS PCM chunk (22050 Hz, mono)
  • Text "END"     — TTS stream complete, device may start next utterance

Required env vars (set by docker-compose):
  GATEWAY_URL         — e.g. http://gateway:8080
  GATEWAY_AUTH_TOKEN  — Bearer token for POST /forward
"""

from __future__ import annotations

import json
import logging
import os
from enum import Enum, auto
from typing import List

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from . import stt as _stt
from . import tts as _tts

logger = logging.getLogger("voice_gateway.server")

_GATEWAY_URL = os.environ.get("GATEWAY_URL", "http://gateway:8080")
_CHUNK_SIZE = 4096  # bytes per TTS chunk

# Read the bearer token from a secret file first (Docker secrets pattern), then
# fall back to the env var — mirrors how agentshroud-gateway reads GATEWAY_AUTH_TOKEN_FILE.
# Token value is never logged.
_token_file = os.environ.get(
    "GATEWAY_AUTH_TOKEN_FILE", "/run/secrets/gateway_password"
)
if os.path.isfile(_token_file):
    with open(_token_file) as _fh:
        _GATEWAY_TOKEN = _fh.read().strip()
else:
    _GATEWAY_TOKEN = os.environ.get("GATEWAY_AUTH_TOKEN", "")
if not _GATEWAY_TOKEN:
    logger.warning(
        "GATEWAY_AUTH_TOKEN not set — /forward calls will fail authentication. "
        "Mount docker secret 'gateway_password' or set GATEWAY_AUTH_TOKEN env var."
    )


class _State(Enum):
    IDLE = auto()
    LISTENING = auto()
    THINKING = auto()
    SPEAKING = auto()


app = FastAPI(title="AgentShroud Voice Gateway")


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


async def _send_state(ws: WebSocket, state: _State) -> None:
    name = state.name.lower()
    await ws.send_text(json.dumps({"state": name}))
    logger.debug("→ state: %s", name)


async def _call_forward(transcript: str) -> str:
    """POST transcript to AgentShroud /forward, return agent_response text."""
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(
            f"{_GATEWAY_URL}/forward",
            json={
                "content": transcript,
                "source": "api",
                "content_type": "text",
                "route_to": "hermes",
            },
            headers={"Authorization": f"Bearer {_GATEWAY_TOKEN}"},
        )

    if resp.status_code == 202:
        return "Your request has been queued for approval."

    resp.raise_for_status()
    data = resp.json()
    agent_response = data.get("agent_response") or ""
    if not agent_response:
        return "Sorry, Hermes is offline right now."
    return agent_response


@app.websocket("/voice")
async def voice_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    remote = ws.client
    logger.info("Connection from %s", remote)

    state = _State.LISTENING
    await _send_state(ws, state)

    pcm_chunks: List[bytes] = []

    try:
        while True:
            message = await ws.receive()

            if "bytes" in message and message["bytes"] is not None:
                pcm_chunks.append(message["bytes"])

            elif "text" in message and message["text"] is not None:
                msg = message["text"].strip()

                if msg == "LISTEN":
                    pcm_chunks.clear()
                    state = _State.LISTENING
                    await _send_state(ws, state)

                elif msg == "END":
                    state = _State.THINKING
                    await _send_state(ws, state)

                    pcm_bytes = b"".join(pcm_chunks)
                    pcm_chunks.clear()

                    try:
                        transcript = _stt.transcribe(pcm_bytes)
                        logger.info("Transcript: %r", transcript)

                        if not transcript.strip():
                            state = _State.IDLE
                            await _send_state(ws, state)
                            continue

                        agent_text = await _call_forward(transcript)
                        logger.info("Agent reply: %r", agent_text)

                        state = _State.SPEAKING
                        await _send_state(ws, state)

                        pcm_reply = _tts.synthesize(agent_text)

                        for i in range(0, max(len(pcm_reply), 1), _CHUNK_SIZE):
                            chunk = pcm_reply[i : i + _CHUNK_SIZE]
                            if chunk:
                                await ws.send_bytes(chunk)

                        await ws.send_text("END")
                        state = _State.IDLE
                        await _send_state(ws, state)

                    except Exception as exc:
                        logger.error("Pipeline error: %s", exc, exc_info=True)
                        try:
                            state = _State.IDLE
                            await _send_state(ws, state)
                        except Exception:
                            pass

    except WebSocketDisconnect:
        logger.info("Disconnected: %s", remote)
    except Exception as exc:
        logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
