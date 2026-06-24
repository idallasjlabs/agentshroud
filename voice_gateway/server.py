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

# Model for voice — used only by the "direct" fast-path (_call_llm).
# Other agents (hermes, openclaw, …) route through /forward → gateway pipeline.
_VOICE_MODEL = os.environ.get("VOICE_MODEL", "claude-haiku-4-5-20251001")

# Default proxied agent to route voice to.  Override per-connection via ?agent= query param.
# "direct" = fast path (_call_llm, bypasses /forward pipeline, backward-compat).
# Any other value = gateway /forward with route_to=<value>.
_DEFAULT_AGENT = os.environ.get("VOICE_DEFAULT_AGENT", "hermes")

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
    """Send a heartbeat every 4 s to keep Tailscale Funnel relay and hotspot NAT alive."""
    try:
        while True:
            await asyncio.sleep(4)
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

    Fast path — bypasses the full agentic loop for lower latency. Used only
    when ?agent=direct (or _DEFAULT_AGENT=="direct"). Gateway substitutes its
    own Anthropic key, so no API key is needed here. Still routes through
    AgentShroud's security pipeline (PII, audit, egress).
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


async def _call_agent(transcript: str, agent: str) -> str:
    """Route a voice utterance to a proxied agent via the AgentShroud gateway /forward endpoint.

    Unlike _call_llm, this path runs the full AgentShroud security pipeline:
    PII redaction, prompt-guard scoring, audit hash-chain, egress policy.

    Hermes (and any future agent with an OpenAI-compat chat_path) returns a
    synchronous agent_response in the ForwardResponse body.  Async agents like
    OpenClaw have no synchronous body reply; in that case we return an honest
    spoken notice so the user knows their message was received.

    Args:
        transcript: STT-produced utterance text (already PII-clean at voice level).
        agent:      AgentShroud bot slug (e.g. "hermes", "openclaw").  Must match
                    a key in the agentshroud.yaml bots: section.

    Returns:
        Spoken reply string (suitable for TTS synthesis).
    """
    # Voice timeout: 35 s read deadline — enough for any normal agent reply (typical
    # Hermes: 3-10 s).  Gateway's own internal forward timeout is 120 s; setting
    # httpx read=125 s means we always catch its graceful 201 body when it fires.
    # The 35 s read deadline fires first for a hung agent, returning a spoken
    # fallback so the ESP returns to IDLE rather than sitting in THINKING for 2 min.
    timeout = httpx.Timeout(connect=10.0, read=35.0, write=10.0, pool=5.0)
    try:
        async with httpx.AsyncClient(timeout=timeout, trust_env=False) as client:
            resp = await client.post(
                f"{_GATEWAY_URL}/forward",
                json={
                    "content": transcript,
                    "source": "api",
                    "route_to": agent,
                    "user_id": _OWNER_USER_ID or "voice",
                },
                headers={
                    "Authorization": f"Bearer {_GATEWAY_TOKEN}",
                    "X-AgentShroud-User-Id": _OWNER_USER_ID or "voice",
                },
            )
        resp.raise_for_status()
        data = resp.json()
        agent_reply = data.get("agent_response") or ""
        if agent_reply.strip():
            logger.info("Agent %r reply: %r", agent, agent_reply[:120])
            return agent_reply.strip()
        # Async agents (OpenClaw) route the message but reply later over Telegram.
        notice = f"{agent.capitalize()} received your message and will reply on Telegram."
        logger.info("Agent %r returned no synchronous reply — notifying user via TTS", agent)
        return notice
    except httpx.ReadTimeout:
        logger.warning(
            "Agent %r read timeout after 35 s — returning voice fallback", agent
        )
        return "I'm having trouble connecting right now. Please try again in a moment."


@app.websocket("/voice")
async def voice_endpoint(ws: WebSocket) -> None:
    await ws.accept()
    token = ws.query_params.get("token", "")
    if _VG_AUTH_TOKEN and token != _VG_AUTH_TOKEN:
        logger.warning("Rejected WS connection (invalid token) from %s", ws.client)
        await ws.close(code=1008)
        return

    # Agent routing: ?agent=<slug> selects the target proxied agent.
    # "direct" = fast LLM path (legacy, lower latency, no agentic tools).
    # Any other value = gateway POST /forward with route_to=<slug>.
    agent = ws.query_params.get("agent", _DEFAULT_AGENT)
    remote = ws.client
    logger.info("Connection from %s (authenticated) → agent=%r", remote, agent)

    state = _State.IDLE
    await _send_state(ws, state)

    # Per-session conversation history — only used by the "direct" fast path.
    # Agents like Hermes maintain their own server-side memory keyed by user_id.
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
                        loop = asyncio.get_event_loop()
                        # Run blocking CPU inference in a thread so the event loop
                        # stays live for WebSocket PING/PONG during STT and TTS.
                        transcript = await loop.run_in_executor(
                            None, _stt.transcribe, pcm_bytes
                        )
                        logger.info("Transcript: %r", transcript)

                        _words = re.sub(r"[^\w]", "", transcript)
                        if not _words:
                            state = _State.IDLE
                            await _send_state(ws, state)
                            continue

                        # Dispatch to the appropriate agent.
                        if agent == "direct":
                            # Fast path: multi-turn LLM proxy (no agentic tools).
                            history.append({"role": "user", "content": transcript})
                            agent_text = await _call_llm(history)
                        else:
                            # Proxied agent path: full AgentShroud pipeline via /forward.
                            # Hermes and future OpenAI-compat agents return a synchronous
                            # reply; async agents (OpenClaw) get an honest Telegram notice.
                            agent_text = await _call_agent(transcript, agent)

                        logger.info("Agent reply: %r", agent_text)

                        # Maintain multi-turn history only for the "direct" fast path.
                        # Proxied agents (Hermes, etc.) manage their own conversation state.
                        if agent == "direct":
                            history.append({"role": "assistant", "content": agent_text})
                            if len(history) > 1 + _MAX_HISTORY_TURNS * 2:
                                history = history[:1] + history[-(  _MAX_HISTORY_TURNS * 2):]

                        state = _State.SPEAKING
                        await _send_state(ws, state)

                        pcm_reply = await loop.run_in_executor(
                            None, _tts.synthesize, agent_text
                        )

                        for i in range(0, max(len(pcm_reply), 1), _CHUNK_SIZE):
                            chunk = pcm_reply[i : i + _CHUNK_SIZE]
                            if chunk:
                                await ws.send_bytes(chunk)
                                await asyncio.sleep(0)  # yield between chunks

                        await ws.send_text("END")
                        state = _State.IDLE
                        await _send_state(ws, state)

                    except Exception as exc:
                        logger.error("Pipeline error: %s", exc, exc_info=True)
                        # Roll back the user turn appended for the "direct" path only
                        # (proxied agents don't mutate local history on the call path).
                        if agent == "direct" and history and history[-1]["role"] == "user":
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
