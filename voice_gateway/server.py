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

import asyncio
import json
import logging
import os
import re
from enum import Enum, auto
from typing import List

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from . import stt as _stt
from . import tts as _tts

logger = logging.getLogger("voice_gateway.server")

_GATEWAY_URL = os.environ.get("GATEWAY_URL", "http://gateway:8080")
_CHUNK_SIZE = 4096  # bytes per TTS chunk

# The RBAC middleware resolves `source` to a user_id for permission checking.
# The voice-terminal is the device owner, so we use the owner's Telegram user_id
# (which has OWNER role in RBAC and can invoke tool_use).  Set via docker-compose
# GATEWAY_OWNER_USER_ID env var; falls back to "api" (viewer, blocked) if unset.
_OWNER_USER_ID = os.environ.get("GATEWAY_OWNER_USER_ID", "")

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

# Token that the ESP32 voice terminal must send as ?token= in the WS URL.
# Read from Docker secret first, then fall back to env var.
# If empty, the check is skipped (dev/test mode — set in production).
_vg_token_file = os.environ.get(
    "VOICE_GW_AUTH_TOKEN_FILE", "/run/secrets/voice_gateway_token"
)
if os.path.isfile(_vg_token_file):
    with open(_vg_token_file) as _vfh:
        _VG_AUTH_TOKEN = _vfh.read().strip()
else:
    _VG_AUTH_TOKEN = os.environ.get("VOICE_GW_AUTH_TOKEN", "")
if not _VG_AUTH_TOKEN:
    logger.warning(
        "VOICE_GW_AUTH_TOKEN not set — /voice WebSocket is unauthenticated. "
        "Mount docker secret 'voice_gateway_token' or set VOICE_GW_AUTH_TOKEN env var."
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


async def _keepalive(ws: WebSocket) -> None:
    """Send a heartbeat every 8 s to prevent ESP32 network_timeout_ms=10000 disconnects."""
    try:
        while True:
            await asyncio.sleep(8)
            await ws.send_text('{"heartbeat":1}')
    except Exception:
        pass


async def _send_state(ws: WebSocket, state: _State) -> None:
    name = state.name.lower()
    await ws.send_text(json.dumps({"state": name}))
    logger.debug("→ state: %s", name)


async def _call_forward(transcript: str) -> str:
    """POST transcript to AgentShroud /forward, return agent_response text."""
    async with httpx.AsyncClient(timeout=120.0, trust_env=False) as client:
        resp = await client.post(
            f"{_GATEWAY_URL}/forward",
            json={
                "content": transcript,
                "source": "api",
                "content_type": "text",
                "route_to": "hermes",
                # user_id drives RBAC: middleware resolves this field first, before source.
                # Owner UID maps to OWNER role (tool_use allowed); falls back to None
                # (→ viewer, blocked) if the env var is not set.
                "user_id": _OWNER_USER_ID or None,
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
    # Auth: check ?token= query parameter before processing any frames.
    # _VG_AUTH_TOKEN is empty in dev/test (skipped); set via docker secret in prod.
    token = ws.query_params.get("token", "")
    if _VG_AUTH_TOKEN and token != _VG_AUTH_TOKEN:
        logger.warning("Rejected WS connection (invalid token) from %s", ws.client)
        await ws.close(code=1008)  # 1008 = Policy Violation
        return

    remote = ws.client
    logger.info("Connection from %s (authenticated)", remote)

    state = _State.IDLE
    await _send_state(ws, state)

    pcm_chunks: List[bytes] = []
    heartbeat = asyncio.create_task(_keepalive(ws))
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

                        # Reject empty transcripts and Whisper hallucinations that
                        # contain only punctuation/whitespace (e.g. "...", ". . .")
                        # on near-silent or very short audio frames.
                        _words = re.sub(r"[^\w]", "", transcript)
                        if not _words:
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
    except RuntimeError as exc:
        # Starlette raises RuntimeError("Cannot call 'receive' once a disconnect
        # message has been received") on a dirty close — treat it as a normal disconnect.
        if "disconnect" in str(exc).lower():
            logger.info("Disconnected (dirty close): %s", remote)
        else:
            logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    except Exception as exc:
        logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    finally:
        heartbeat.cancel()
