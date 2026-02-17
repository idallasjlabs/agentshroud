"""
Isaiah Chat Service - Phase 3 MVP
Minimal chat service with Isaiah's personality loaded from persona files.
"""

import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logger = logging.getLogger("chatbot")


class ChatRequest(BaseModel):
    content: str
    content_type: str = "text"
    metadata: dict = {}
    ledger_id: Optional[str] = None
    source: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: Optional[int] = None


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


# Module-level state
_openai_client: openai.OpenAI | None = None
_persona_prompt: str = ""


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPI lifespan - initialize OpenAI client and persona once."""
    global _openai_client, _persona_prompt

    # Load persona
    _persona_prompt = load_persona_files()
    logger.info(f"✅ Persona loaded ({len(_persona_prompt)} chars)")

    # Load API key once
    api_key_path = Path("/run/secrets/openai_api_key")
    if api_key_path.exists():
        api_key = api_key_path.read_text().strip()
    else:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        logger.warning("No API key found")
    else:
        _openai_client = openai.OpenAI(api_key=api_key)
        logger.info("✅ OpenAI client initialized")

    logger.info("✅ Isaiah Chat Service started")
    yield
    logger.info("Isaiah Chat Service shutting down")


app = FastAPI(title="Isaiah Chat Service", version="0.1.0", lifespan=lifespan)


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker."""
    return {
        "status": "healthy",
        "service": "isaiah-chat",
        "persona_loaded": len(_persona_prompt) > 0,
        "client_ready": _openai_client is not None,
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat message with Isaiah's personality."""
    if _openai_client is None:
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key not configured"
        )

    try:
        response = _openai_client.chat.completions.create(
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

    except openai.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18789)
