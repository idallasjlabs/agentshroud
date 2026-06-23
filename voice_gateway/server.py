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
  GATEWAY_URL           — e.g. http://gateway:8080
  GATEWAY_AUTH_TOKEN    — Bearer token for gateway (kept for /forward fallback)
  GATEWAY_OWNER_USER_ID — owner Telegram UID for RBAC propagation
  VOICE_MODEL           — LLM model for voice (default: claude-haiku-4-5-20251001)
  GATEWAY_TZ            — IANA timezone for date/time injection (default: America/New_York)
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List
from zoneinfo import ZoneInfo

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from . import stt as _stt
from . import tts as _tts

logger = logging.getLogger("voice_gateway.server")

_GATEWAY_URL = os.environ.get("GATEWAY_URL", "http://gateway:8080")
_CHUNK_SIZE = 4096  # bytes per TTS chunk

_OWNER_USER_ID = os.environ.get("GATEWAY_OWNER_USER_ID", "")

# Model for voice — bypasses Hermes agentic overhead, calls gateway's OpenAI-compat
# proxy directly. Gateway substitutes its own Anthropic key; no key needed here.
_VOICE_MODEL = os.environ.get("VOICE_MODEL", "claude-haiku-4-5-20251001")

# Conversation history: keep at most this many user+assistant turn pairs.
# Older turns are dropped (FIFO) to bound token usage and maintain context.
_MAX_HISTORY_TURNS = 10

# Read the bearer token (kept for compatibility / future use).
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
        "GATEWAY_AUTH_TOKEN not set — gateway calls may fail authentication."
    )

# WS auth token the ESP32 must provide as ?token=.
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


def _voice_system_message() -> Dict[str, str]:
    """Build a system message with the current date/time for voice context."""
    tz = ZoneInfo(os.environ.get("GATEWAY_TZ", "America/New_York"))
    now = datetime.now(tz).strftime("%A, %B %d, %Y at %-I:%M %p %Z")
    return {
        "role": "system",
        "content": (
            f"You are a concise voice assistant built into an ESP32 device. "
            f"The current date and time is {now}. "
            "Keep every response to 1-2 short spoken sentences — no markdown, "
            "no bullet points, no lists. Plain conversational English only. "
            "If asked a follow-up, remember the prior context in this conversation."
        ),
    }


async def _call_llm(history: List[Dict[str, str]]) -> str:
    """POST conversation history to the gateway's OpenAI-compat endpoint.

    Bypasses Hermes's full agentic loop for lower latency. The gateway's LLM
    proxy substitutes its own Anthropic key, so no API key is needed here.
    Still routes through AgentShroud's security pipeline (PII, audit, egress).
    """
    async with httpx.AsyncClient(timeout=30.0, trust_env=False) as client:
        resp = await client.post(
            f"{_GATEWAY_URL}/v1/chat/completions",
            json={
                "model": _VOICE_MODEL,
                "messages": history,
                "max_tokens": 150,  # ~100 words — keep voice replies brief
            },
            headers={
                # IP allowlist passes (isolated network); proxy substitutes Anthropic key.
                "Authorization": f"Bearer {_GATEWAY_TOKEN}",
                # Propagate owner identity for RBAC and audit trail.
                "X-AgentShroud-User-Id": _OWNER_USER_ID or "voice",
            },
        )
    resp.raise_for_status()
    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"Unexpected LLM response shape: {exc}") from exc


@app.websocket("/voice")
async def voice_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    token = ws.query_params.get("token", "")
    if _VG_AUTH_TOKEN and token != _VG_AUTH_TOKEN:
        logger.warning("Rejected WS connection (invalid token) from %s", ws.client)
        await ws.close(code=1008)
        return

    remote = ws.client
    logger.info("Connection from %s (authenticated)", remote)

    state = _State.IDLE
    await _send_state(ws, state)

    # Per-session conversation history.
    # Index 0 is always the system message (refreshed at each utterance for time accuracy).
    # User+assistant turns are appended and trimmed to _MAX_HISTORY_TURNS pairs.
    history: List[Dict[str, str]] = [_voice_system_message()]

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
                    # Refresh the system message so time stays accurate on long sessions.
                    history[0] = _voice_system_message()
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

                        _words = re.sub(r"[^\w]", "", transcript)
                        if not _words:
                            state = _State.IDLE
                            await _send_state(ws, state)
                            continue

                        # Add user turn to history before calling LLM.
                        history.append({"role": "user", "content": transcript})

                        agent_text = await _call_llm(history)
                        logger.info("Agent reply: %r", agent_text)

                        # Append assistant turn and trim old turns.
                        history.append({"role": "assistant", "content": agent_text})
                        if len(history) > 1 + _MAX_HISTORY_TURNS * 2:
                            history = history[:1] + history[-(  _MAX_HISTORY_TURNS * 2):]

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
                        # Roll back the user turn we already appended (no assistant reply).
                        if history and history[-1]["role"] == "user":
                            history.pop()
                        try:
                            state = _State.IDLE
                            await _send_state(ws, state)
                        except Exception:
                            pass

    except WebSocketDisconnect:
        logger.info("Disconnected: %s", remote)
    except RuntimeError as exc:
        if "disconnect" in str(exc).lower():
            logger.info("Disconnected (dirty close): %s", remote)
        else:
            logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    except Exception as exc:
        logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    finally:
        heartbeat.cancel()
