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
import hashlib
import hmac
import json
import logging
import os
import re
from contextlib import asynccontextmanager
from pathlib import Path
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List
from zoneinfo import ZoneInfo

import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, Response
from websockets.exceptions import (
    ConnectionClosed,
    ConnectionClosedError,
    ConnectionClosedOK,
)

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
_token_file = os.environ.get("GATEWAY_AUTH_TOKEN_FILE", "/run/secrets/gateway_password")
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

_FIRMWARE_BIN_PATH = Path(os.environ.get("FIRMWARE_BIN_PATH", "/firmware/voice_terminal.bin"))
_fw_etag: str = ""
_fw_mtime: float = 0.0

# Server-side utterance safety limits.
# A device that sends LISTEN but never sends END (crash, stuck firmware) would
# otherwise hold the session in LISTENING forever with unbounded pcm_chunks growth.
_LISTEN_MAX_S: float = 15.0              # max seconds to wait for END after LISTEN
# Per-sentence TTS synthesis budget.  Kokoro takes ~0.2-3 s per sentence when
# healthy; a synthesis exceeding this is wedged (e.g. blocked voice-pack
# download) and must not strand the device in THINKING.
_TTS_SENTENCE_TIMEOUT_S: float = float(os.environ.get("VG_TTS_SENTENCE_TIMEOUT_S", "30"))

# ── TTS resume-on-reconnect ───────────────────────────────────────────────────
# Sessions are per-connection, so a hotspot drop mid-downlink used to lose the
# rest of the reply.  The send loop records the reply and its sent offset here;
# a reconnect within the freshness window replays the un-sent remainder.
# Single-device deployment — no per-device keying (the funnel NATs every
# device to one host anyway).
_reply_resume: dict | None = None
# Uplink twin of _reply_resume: preserves a partially-received utterance
# across connection drops so the device resumes with "LISTEN <offset>".
_utterance_resume: dict | None = None
_RESUME_MAX_AGE_S: float = 30.0
_RESUME_REWIND_BYTES: int = 8192   # re-send this much before the recorded
                                   # offset — covers frames lost in flight
_PCM_MAX_BYTES: int  = 16000 * 2 * 20   # 20 s × 16 kHz × 2 bytes/sample S16LE mono


def _get_firmware_etag() -> str | None:
    global _fw_etag, _fw_mtime
    if not _FIRMWARE_BIN_PATH.exists():
        return None
    mtime = _FIRMWARE_BIN_PATH.stat().st_mtime
    if mtime != _fw_mtime or not _fw_etag:
        sha = hashlib.sha256(_FIRMWARE_BIN_PATH.read_bytes()).hexdigest()
        _fw_etag = f'"{sha}"'
        _fw_mtime = mtime
    return _fw_etag


class _State(Enum):
    IDLE = auto()
    LISTENING = auto()
    THINKING = auto()
    SPEAKING = auto()


@asynccontextmanager
async def _lifespan(_app: FastAPI):
    loop = asyncio.get_event_loop()
    await asyncio.gather(
        loop.run_in_executor(None, _stt._get_model),
        loop.run_in_executor(None, _tts._get_pipeline),
    )
    yield


app = FastAPI(title="AgentShroud Voice Gateway", lifespan=_lifespan)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@app.api_route("/firmware/bin", methods=["GET", "HEAD"])
async def firmware_bin(token: str = "") -> Response:
    if _VG_AUTH_TOKEN and not hmac.compare_digest(token, _VG_AUTH_TOKEN):
        return Response(status_code=401)
    etag = _get_firmware_etag()
    if etag is None:
        return Response(status_code=404)
    return FileResponse(
        str(_FIRMWARE_BIN_PATH),
        media_type="application/octet-stream",
        headers={"ETag": etag},
    )


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


_NUMBER_WORDS = {
    "zero": 0, "ten": 10, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "hundred": 100, "one hundred": 100,
}
_UNIT_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9,
}


_VOLUME_RE = re.compile(
    # "[,:]?" — Whisper often punctuates the command ("Set volume, 90%").
    r"\bset\s+(?:the\s+)?volume[,:]?\s+(?:to\s+)?"
    r"(\d{1,3}|[a-z]+(?:[ -][a-z]+)?)\s*(?:%|percent)?\b",
    re.IGNORECASE,
)


def _parse_volume_command(transcript: str) -> int | None:
    """Return the requested volume (0-100, clamped) for a spoken
    "set [the] volume [to] X [%|percent]" command, else None.

    Whisper emits both digit ("80%") and word ("eighty percent") forms —
    handle digits, tens words, and tens+unit compounds ("twenty five").
    """
    t = transcript.lower().strip()
    m = _VOLUME_RE.search(t)
    if not m:
        return None
    raw = m.group(1).replace("-", " ").strip()
    if raw.isdigit():
        val = int(raw)
    elif raw in _NUMBER_WORDS:
        val = _NUMBER_WORDS[raw]
    else:
        parts = raw.split()
        if (
            len(parts) == 2
            and parts[0] in _NUMBER_WORDS
            and parts[1] in _UNIT_WORDS
        ):
            val = _NUMBER_WORDS[parts[0]] + _UNIT_WORDS[parts[1]]
        elif len(parts) == 2 and parts[0] in _NUMBER_WORDS:
            val = _NUMBER_WORDS[parts[0]]   # "eighty percent" already stripped; stray word
        else:
            return None
    return max(0, min(100, val))


def _voice_system_message() -> Dict[str, str]:
    """Build a system message with the current date/time for voice context."""
    tz = ZoneInfo(os.environ.get("GATEWAY_TZ", "America/New_York"))
    now = datetime.now(tz).strftime("%A, %B %d, %Y at %-I:%M %p %Z")
    content = (
        f"You are a concise voice assistant built into an ESP32 device. "
        f"The current date and time is {now}. "
        "Keep every response to 1-2 short spoken sentences — no markdown, "
        "no bullet points, no lists. Plain conversational English only. "
        "If asked a follow-up, remember the prior context in this conversation."
    )
    if "qwen" in _VOICE_MODEL.lower():
        # Qwen3 emits a long <think> block before answering (~30 s per reply
        # measured on LM Studio) — /no_think disables it; voice needs the
        # answer, not the reasoning trace.
        content += " /no_think"
    return {"role": "system", "content": content}


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
                # Voice is interactive: on upstream 429, skip the ~15 s retry
                # preamble and fail over to the local model immediately.
                "X-AgentShroud-Interactive": "1",
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
    # Voice read deadline (VG_AGENT_READ_TIMEOUT_S, default 100 s): Hermes is
    # the owner's admin voice control and a real (slow) answer beats a fast
    # fallback.  Measured 2026-07-06: a Hermes turn takes ~73 s while the
    # Anthropic org quota is 429-ing (its internal LLM calls burn the retry
    # preamble); 3-10 s when quota is healthy.  Gateway's own forward timeout
    # is 120 s — staying under it means we still catch its graceful body.
    _read_s = float(os.environ.get("VG_AGENT_READ_TIMEOUT_S", "100"))
    timeout = httpx.Timeout(connect=10.0, read=_read_s, write=10.0, pool=5.0)
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
                    # Interactive hint — /forward itself makes no LLM calls,
                    # but forwarding it costs nothing and keeps both voice
                    # paths consistent if the pipeline learns to honour it.
                    "X-AgentShroud-Interactive": "1",
                },
            )
        resp.raise_for_status()
        data = resp.json()
        agent_reply = data.get("agent_response") or ""
        if agent_reply.strip():
            logger.info("Agent %r reply: %r", agent, agent_reply[:120])
            return agent_reply.strip()
        # Async agents (OpenClaw) route the message but reply later over Telegram.
        notice = (
            f"{agent.capitalize()} received your message and will reply on Telegram."
        )
        logger.info(
            "Agent %r returned no synchronous reply — notifying user via TTS", agent
        )
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

    # Per-session conversation history — only used by the "direct" fast path.
    # Agents like Hermes maintain their own server-side memory keyed by user_id.
    # Index 0 is always the system message (refreshed at each utterance for time accuracy).
    # User+assistant turns are appended and trimmed to _MAX_HISTORY_TURNS pairs.
    history: List[Dict[str, str]] = [_voice_system_message()]

    pcm_chunks: List[bytes] = []
    _pcm_bytes_total: int = 0       # running byte count — avoids O(n) sum on each chunk
    _listen_deadline: float | None = None   # set when LISTEN fires, cleared on END/timeout
    # Define before the try so the finally clause can always reference it safely,
    # even if a dirty-close fires before the task is created.
    heartbeat = None
    try:
        # Send the initial IDLE state to the device.  This must be inside the try
        # block so that a dirty-close (code 1006) arriving before the first frame
        # is delivered is caught by the existing WebSocketDisconnect handler below,
        # producing one clean INFO log instead of an unhandled ASGI traceback.
        await _send_state(ws, state)
        heartbeat = asyncio.create_task(_keepalive(ws))
        _loop = asyncio.get_running_loop()

        # Resume an interrupted TTS reply from the previous connection.
        global _reply_resume, _utterance_resume
        if _reply_resume is not None:
            _age = _loop.time() - _reply_resume["ts"]
            _pcm, _sent = _reply_resume["pcm"], _reply_resume["sent"]
            if _age <= _RESUME_MAX_AGE_S and _sent < len(_pcm):
                _off = max(0, _sent - _RESUME_REWIND_BYTES)
                logger.info(
                    "Resuming interrupted TTS reply: %d/%d bytes were sent "
                    "%.1fs ago — replaying remainder",
                    _sent, len(_pcm), _age,
                )
                state = _State.SPEAKING
                await _send_state(ws, state)
                for _i in range(_off, len(_pcm), _CHUNK_SIZE):
                    await ws.send_bytes(bytes(_pcm[_i : _i + _CHUNK_SIZE]))
                    _reply_resume["sent"] = _i + _CHUNK_SIZE
                    await asyncio.sleep(0)
                await ws.send_text("END")
                state = _State.IDLE
                await _send_state(ws, state)
            _reply_resume = None   # replayed, stale, or already complete

        while True:
            # While LISTENING, bound the wait so a device that never sends END
            # (crash, stuck firmware) self-heals after _LISTEN_MAX_S seconds.
            if _listen_deadline is not None:
                remaining = _listen_deadline - _loop.time()
                if remaining <= 0:
                    logger.warning(
                        "LISTEN timeout (%.0fs) from %s — finalising utterance",
                        _LISTEN_MAX_S, remote,
                    )
                    _listen_deadline = None
                    message = {"bytes": None, "text": "END"}
                else:
                    try:
                        message = await asyncio.wait_for(ws.receive(), timeout=remaining)
                    except asyncio.TimeoutError:
                        logger.warning(
                            "LISTEN timeout (%.0fs) from %s — finalising utterance",
                            _LISTEN_MAX_S, remote,
                        )
                        _listen_deadline = None
                        message = {"bytes": None, "text": "END"}
            else:
                message = await ws.receive()

            if "bytes" in message and message["bytes"] is not None:
                # Safety cap: stop buffering once we reach the per-utterance limit.
                # This bounds memory even if the device streams indefinitely without END.
                if _pcm_bytes_total < _PCM_MAX_BYTES:
                    pcm_chunks.append(message["bytes"])
                    _pcm_bytes_total += len(message["bytes"])
                    # Keep the cross-connection utterance cache live: a drop
                    # mid-upload preserves everything received so the device
                    # can resume with "LISTEN <offset>" instead of resending
                    # the whole utterance (the dominant THINKING-time cost on
                    # the flaky hotspot link).
                    if _utterance_resume is not None:
                        _utterance_resume["pcm"] += message["bytes"]
                        _utterance_resume["ts"] = _loop.time()
                else:
                    logger.warning(
                        "PCM buffer cap (%d bytes) reached from %s — discarding excess",
                        _PCM_MAX_BYTES, remote,
                    )

            elif "text" in message and message["text"] is not None:
                msg = message["text"].strip()

                if msg == '{"ping":1}':
                    pass  # client keepalive — no response needed

                elif msg.startswith('{"log":'):
                    # Remote-diagnosis channel: the firmware mirrors key diagnostic
                    # lines here when no USB serial is attached.  Print into our own
                    # log so `docker logs` becomes the device trace.
                    try:
                        entry = json.loads(msg).get("log", msg)
                    except json.JSONDecodeError:
                        entry = msg
                    logger.info("[device %s] %s", remote, entry)

                elif msg == "STOP":
                    # Stale STOP: the tap landed just as TTS finished (the
                    # in-stream watcher already exited).  Nothing to abort.
                    logger.info("Stale STOP from %s (not speaking) — ignored", remote)

                elif msg == "LISTEN" or msg.startswith("LISTEN "):
                    # Bare LISTEN = fresh utterance.  "LISTEN <offset>" = the
                    # device resuming after a mid-upload drop: seed the buffer
                    # from the cross-connection cache up to <offset> (the
                    # device resends from there, rewound to cover in-flight
                    # loss) so a drop at 90% costs seconds, not a full resend.
                    _offset = None
                    if msg != "LISTEN":
                        try:
                            _offset = max(0, int(msg.split(None, 1)[1]))
                        except (ValueError, IndexError):
                            _offset = None
                    pcm_chunks.clear()
                    _pcm_bytes_total = 0
                    if (
                        _offset is not None
                        and _utterance_resume is not None
                        and (_loop.time() - _utterance_resume["ts"]) <= _RESUME_MAX_AGE_S
                    ):
                        _cached = bytes(_utterance_resume["pcm"][:_offset])
                        if _cached:
                            pcm_chunks.append(_cached)
                            _pcm_bytes_total = len(_cached)
                        logger.info(
                            "LISTEN resume at %d (%d cached bytes) from %s",
                            _offset, len(_cached), remote,
                        )
                    else:
                        logger.info("LISTEN from %s", remote)
                    # (Re)arm the cache for THIS utterance — chunk appends
                    # keep it current; cleared on END.
                    _utterance_resume = {
                        "pcm": bytearray(b"".join(pcm_chunks)),
                        "ts": _loop.time(),
                    }
                    # Safety: arm the server-side utterance timeout so a device that
                    # never sends END (crash, stuck firmware) can't hold the session in
                    # LISTENING forever.  Cleared when END is received or on timeout.
                    _listen_deadline = _loop.time() + _LISTEN_MAX_S
                    # Refresh the system message so time stays accurate on long sessions.
                    history[0] = _voice_system_message()
                    state = _State.LISTENING
                    await _send_state(ws, state)

                elif msg == "END":
                    _listen_deadline = None   # cancel the utterance timeout
                    _utterance_resume = None  # utterance complete — cache done
                    state = _State.THINKING
                    await _send_state(ws, state)

                    pcm_bytes = b"".join(pcm_chunks)
                    pcm_chunks.clear()
                    _pcm_bytes_total = 0

                    try:
                        loop = _loop
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

                        # Spoken device commands — intercepted server-side, never
                        # routed to an agent.  "set volume X%" sends a control
                        # frame the firmware applies + persists.  The user often
                        # chains a question in the same breath ("Set volume 80.
                        # What time is it?") — route any remainder to the agent
                        # and speak confirmation + answer together.
                        _vol = _parse_volume_command(transcript)
                        _confirm_prefix = ""
                        _query_text = transcript
                        _dispatch = True
                        agent_text = ""
                        if _vol is not None:
                            logger.info("Volume command: %d%% → device", _vol)
                            await ws.send_text(
                                json.dumps({"cmd": "set_volume", "value": _vol})
                            )
                            _confirm_prefix = f"Volume set to {_vol} percent. "
                            _rest = _VOLUME_RE.sub(" ", transcript, count=1)
                            if re.sub(r"[^\w]", "", _rest):
                                _query_text = _rest.strip(" .,!?")
                            else:
                                agent_text = _confirm_prefix.strip()
                                _dispatch = False

                        # Dispatch to the appropriate agent.
                        if _dispatch and agent == "direct":
                            # Fast path: multi-turn LLM proxy (no agentic tools).
                            history.append({"role": "user", "content": _query_text})
                            agent_text = _confirm_prefix + await _call_llm(history)
                        elif _dispatch:
                            # Proxied agent path: full AgentShroud pipeline via /forward.
                            # Hermes and future OpenAI-compat agents return a synchronous
                            # reply; async agents (OpenClaw) get an honest Telegram notice.
                            agent_text = _confirm_prefix + await _call_agent(
                                _query_text, agent
                            )

                        logger.info("Agent reply: %r", agent_text)

                        # Maintain multi-turn history only for the "direct" fast path.
                        # Proxied agents (Hermes, etc.) manage their own conversation state.
                        # A pure volume command never touched history (no user turn).
                        if agent == "direct" and _dispatch:
                            history.append({"role": "assistant", "content": agent_text})
                            if len(history) > 1 + _MAX_HISTORY_TURNS * 2:
                                history = (
                                    history[:1] + history[-(_MAX_HISTORY_TURNS * 2) :]
                                )

                        # Pipeline synthesis with sending: synthesise sentence N+1
                        # concurrently in a thread while sentence N's PCM frames are
                        # being transmitted.  Without this, inter-sentence Kokoro
                        # inference (~200-500 ms each) creates audio gaps that empty
                        # the ESP32 DMA buffer and produce audible dropouts.
                        #
                        # SPEAKING state is sent immediately before the first PCM
                        # frame (not before synthesis) so the ESP32 mouth animation
                        # is synchronised with the audio onset rather than leading it
                        # by the full first-sentence inference time.
                        sentences = _tts.split_for_speech(agent_text)
                        _synth_q: asyncio.Queue[bytes | None] = asyncio.Queue(maxsize=2)

                        # 0.4 s of leading silence on the first sentence: any
                        # residual playback-start transient on the device (amp
                        # wake, ring flush, connection churn) lands in silence
                        # instead of on the first spoken word.
                        _lead_pad = b"\x00" * 12800

                        async def _synthesize_all() -> None:
                            # Bounded per sentence: a wedged synthesis (live
                            # incident 2026-07-03/04 — Kokoro hung fetching an
                            # uncached voice pack) must never strand the device
                            # in THINKING.  On timeout/failure, stop synthesis
                            # but still deliver the sentinel so the send loop
                            # exits and END + state:idle reach the device.
                            _first = True
                            for _s in sentences:
                                try:
                                    _pcm = await asyncio.wait_for(
                                        loop.run_in_executor(None, _tts.synthesize, _s),
                                        timeout=_TTS_SENTENCE_TIMEOUT_S,
                                    )
                                    if _first:
                                        _pcm = _lead_pad + _pcm
                                        _first = False
                                except Exception as _exc:
                                    logger.error(
                                        "TTS failed/timed out (%.0fs) for %r — "
                                        "aborting remaining sentences: %s",
                                        _TTS_SENTENCE_TIMEOUT_S, _s[:60], _exc,
                                    )
                                    break
                                await _synth_q.put(_pcm)
                            await _synth_q.put(None)  # sentinel

                        synth_task = asyncio.create_task(_synthesize_all())

                        # STOP protocol: the device sends a "STOP" text frame when
                        # the user taps during SPEAKING.  The send loop below never
                        # reads the socket, so without a concurrent reader the STOP
                        # would sit unread until the full reply (8-30 s of PCM) was
                        # transmitted — during which the device stays deaf.  The
                        # watcher reads concurrently, honours STOP mid-stream, and
                        # keeps the remote-diag {"log":...} channel flowing.
                        _stop_requested = asyncio.Event()

                        async def _watch_for_stop() -> None:
                            while True:
                                _m = await ws.receive()
                                _t = (_m.get("text") or "").strip()
                                if _t == "STOP":
                                    logger.info(
                                        "STOP from %s — aborting TTS stream", remote
                                    )
                                    _stop_requested.set()
                                    return
                                if _t.startswith('{"log":'):
                                    try:
                                        _entry = json.loads(_t).get("log", _t)
                                    except json.JSONDecodeError:
                                        _entry = _t
                                    logger.info("[device %s] %s", remote, _entry)
                                # Anything else during SPEAKING (keepalive pings,
                                # stray PCM) is ignored.

                        watcher = asyncio.create_task(_watch_for_stop())
                        _stop_wait = asyncio.create_task(_stop_requested.wait())
                        _speaking_sent = False
                        # Arm the resume cache: if this connection dies before
                        # the reply finishes, the next connection replays the
                        # remainder (see the resume block at connect time).
                        _reply_resume = {
                            "pcm": bytearray(),
                            "sent": 0,
                            "ts": _loop.time(),
                        }
                        try:
                            while not _stop_requested.is_set():
                                _get = asyncio.create_task(_synth_q.get())
                                _done, _ = await asyncio.wait(
                                    {_get, _stop_wait},
                                    return_when=asyncio.FIRST_COMPLETED,
                                )
                                if _get not in _done:
                                    _get.cancel()
                                    break
                                pcm = _get.result()
                                if pcm is None:
                                    break
                                _reply_resume["pcm"] += pcm
                                for i in range(0, len(pcm), _CHUNK_SIZE):
                                    if _stop_requested.is_set():
                                        break
                                    frame = pcm[i : i + _CHUNK_SIZE]
                                    if frame:
                                        if not _speaking_sent:
                                            state = _State.SPEAKING
                                            await _send_state(ws, state)
                                            _speaking_sent = True
                                        await ws.send_bytes(frame)
                                        _reply_resume["sent"] += len(frame)
                                        await asyncio.sleep(0)
                        finally:
                            for _task in (watcher, _stop_wait, synth_task):
                                if not _task.done():
                                    _task.cancel()
                            for _task in (watcher, _stop_wait, synth_task):
                                # The watcher may hold a WebSocketDisconnect from a
                                # mid-stream close; swallow it here — the main
                                # receive loop observes the close itself on its
                                # next ws.receive().
                                try:
                                    await _task
                                except asyncio.CancelledError:
                                    pass
                                except Exception:
                                    pass

                        await ws.send_text("END")
                        state = _State.IDLE
                        await _send_state(ws, state)
                        # Reply fully delivered (or user-STOPped) — nothing to
                        # resume.  A mid-stream drop never reaches this line,
                        # leaving the cache armed for the reconnect replay.
                        _reply_resume = None

                    except Exception as exc:
                        logger.error("Pipeline error: %s", exc, exc_info=True)
                        # Roll back the user turn appended for the "direct" path only
                        # (proxied agents don't mutate local history on the call path).
                        if (
                            agent == "direct"
                            and history
                            and history[-1]["role"] == "user"
                        ):
                            history.pop()
                        try:
                            state = _State.IDLE
                            await _send_state(ws, state)
                        except Exception:
                            pass

    except WebSocketDisconnect:
        logger.info("Disconnected: %s", remote)
    except (ConnectionClosed, ConnectionClosedError, ConnectionClosedOK) as exc:
        # Raised by the websockets library on ungraceful (code 1006) or library-level
        # graceful close — expected when the ESP32 loses WiFi/power mid-session.
        # Log at INFO, not ERROR: this is normal device behaviour, not a server fault.
        code = getattr(exc, "code", "?")
        logger.info("Disconnected (websockets code %s): %s", code, remote)
    except RuntimeError as exc:
        if "disconnect" in str(exc).lower():
            logger.info("Disconnected (dirty close): %s", remote)
        else:
            logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    except Exception as exc:
        logger.error("Unhandled WS error from %s: %s", remote, exc, exc_info=True)
    finally:
        if heartbeat is not None:
            heartbeat.cancel()
