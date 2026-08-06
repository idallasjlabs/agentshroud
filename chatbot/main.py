"""
Isaiah Chat Service - Phase 3 MVP
Minimal chat service with Isaiah's personality loaded from persona files.
"""

import logging
import os
import time
from collections import defaultdict
from contextlib import asynccontextmanager
from pathlib import Path

import openai
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("chatbot")


class ChatRequest(BaseModel):
    content: str
    content_type: str = "text"
    metadata: dict = {}
    ledger_id: str | None = None
    source: str | None = None


class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: int | None = None


def load_persona_files() -> str:
    """Load Isaiah's persona from IDENTITY, SOUL, and USER files."""
    workspace = Path("/workspace")

    persona_parts = []

    identity_path = workspace / "IDENTITY"
    if identity_path.exists():
        persona_parts.append(f"# IDENTITY\n{identity_path.read_text()}")

    soul_path = workspace / "SOUL.md"
    if soul_path.exists():
        persona_parts.append(f"\n# SOUL\n{soul_path.read_text()}")

    user_path = workspace / "USER"
    if user_path.exists():
        persona_parts.append(f"\n# USER CONTEXT\n{user_path.read_text()}")

    if not persona_parts:
        return """You are Isaiah Dallas Jefferson, Jr., Chief Innovation Engineer at Fluence Energy.
Communication style: Direct, technically precise, efficient.
"""

    return "\n\n".join(persona_parts)


# --- Auth -------------------------------------------------------------------

_bearer = HTTPBearer(auto_error=False)


def _get_auth_token() -> str:
    """Read the expected auth token from env or secrets."""
    secret_path = Path("/run/secrets/chatbot_auth_token")
    if secret_path.exists():
        return secret_path.read_text().strip()
    return os.getenv("CHATBOT_AUTH_TOKEN", "")


async def require_auth(
    credentials: HTTPAuthorizationCredentials | None = Depends(_bearer),
) -> str:
    """Require valid Bearer token for chat endpoints.

    When CHATBOT_AUTH_TOKEN is not set (empty), auth is disabled for backward
    compatibility with existing deployments that don't use auth yet.
    """
    expected = _get_auth_token()
    if not expected:
        # Auth not configured - allow (but log a warning on first request)
        return "unauthenticated"
    if credentials is None or credentials.credentials != expected:
        raise HTTPException(
            status_code=401, detail="Invalid or missing authentication token"
        )
    return "authenticated"


# --- Rate limiting ----------------------------------------------------------

# Simple in-memory sliding-window rate limiter. Not distributed, but sufficient
# for a single-instance prototype.
_RATE_LIMIT_WINDOW = 60  # seconds
_RATE_LIMIT_MAX = 20  # requests per window per source IP
_rate_buckets: dict[str, list[float]] = defaultdict(list)


def _check_rate_limit(client_ip: str) -> None:
    """Raise 429 if the client has exceeded the rate limit."""
    now = time.time()
    window_start = now - _RATE_LIMIT_WINDOW
    # Prune old entries
    _rate_buckets[client_ip] = [t for t in _rate_buckets[client_ip] if t > window_start]
    if len(_rate_buckets[client_ip]) >= _RATE_LIMIT_MAX:
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded ({_RATE_LIMIT_MAX} requests per {_RATE_LIMIT_WINDOW}s)",
        )
    _rate_buckets[client_ip].append(now)


# Module-level state
_openai_client: openai.AsyncOpenAI | None = None
_persona_prompt: str = ""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - initialize OpenAI client and persona once."""
    global _openai_client, _persona_prompt

    # Load persona
    _persona_prompt = load_persona_files()
    logger.info("Persona loaded (%d chars)", len(_persona_prompt))

    # Load API key once
    api_key_path = Path("/run/secrets/openai_api_key")
    if api_key_path.exists():
        api_key = api_key_path.read_text().strip()
    else:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        logger.warning("No OpenAI API key found - chat endpoint will return 503")
    else:
        # Use AsyncOpenAI to avoid blocking the event loop
        _openai_client = openai.AsyncOpenAI(api_key=api_key)
        logger.info("OpenAI async client initialized")

    auth_token = _get_auth_token()
    if not auth_token:
        logger.warning(
            "CHATBOT_AUTH_TOKEN not set - /chat endpoint is unauthenticated. "
            "Set CHATBOT_AUTH_TOKEN to enable Bearer token auth."
        )
    else:
        logger.info("Auth token configured - /chat requires Bearer token")

    logger.info("Isaiah Chat Service started")
    yield
    logger.info("Isaiah Chat Service shutting down")


app = FastAPI(title="Isaiah Chat Service", version="0.1.0", lifespan=lifespan)


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker.

    Reports degraded status when the OpenAI client is not available
    (missing API key), so orchestrators don't route traffic to an instance
    that can't actually serve chat requests.
    """
    client_ready = _openai_client is not None
    return {
        "status": "healthy" if client_ready else "degraded",
        "service": "isaiah-chat",
        "persona_loaded": len(_persona_prompt) > 0,
        "client_ready": client_ready,
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, req: Request, _user: str = Depends(require_auth)):
    """Process chat message with Isaiah's personality."""
    # Rate limit by client IP
    client_ip = req.client.host if req.client else "unknown"
    _check_rate_limit(client_ip)

    if _openai_client is None:
        raise HTTPException(
            status_code=503,
            detail="Chat service is not available (missing configuration)",
        )

    try:
        # Use async client - does not block the event loop
        response = await _openai_client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=2048,
            messages=[
                {"role": "system", "content": _persona_prompt},
                {"role": "user", "content": request.content},
            ],
        )

        return ChatResponse(
            response=response.choices[0].message.content,
            model=response.model,
            tokens_used=response.usage.prompt_tokens + response.usage.completion_tokens,
        )

    except openai.AuthenticationError:
        logger.error("OpenAI authentication failed - API key may be invalid")
        raise HTTPException(
            status_code=503,
            detail="Chat service authentication error (contact administrator)",
        )
    except openai.RateLimitError:
        logger.warning("OpenAI rate limit hit")
        raise HTTPException(
            status_code=429,
            detail="Chat service is temporarily rate-limited, try again later",
        )
    except Exception as e:
        # Log the full error internally but do NOT expose it to the client
        logger.error("Chat request failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=502,
            detail="Chat service encountered an internal error",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=18789)
