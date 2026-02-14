"""
Isaiah Chat Service - Phase 3 MVP
Minimal chat service with Isaiah's personality loaded from persona files.
"""

import os
from pathlib import Path
from typing import Optional

import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Isaiah Chat Service", version="0.1.0")


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

    # Load IDENTITY (no .md extension in mount)
    identity_path = workspace / "IDENTITY"
    if identity_path.exists():
        persona_parts.append(f"# IDENTITY\n{identity_path.read_text()}")

    # Load SOUL
    soul_path = workspace / "SOUL.md"
    if soul_path.exists():
        persona_parts.append(f"\n# SOUL\n{soul_path.read_text()}")

    # Load USER (no .md extension in mount)
    user_path = workspace / "USER"
    if user_path.exists():
        persona_parts.append(f"\n# USER CONTEXT\n{user_path.read_text()}")

    if not persona_parts:
        # Fallback if files not mounted
        return """You are Isaiah Dallas Jefferson, Jr., Chief Innovation Engineer at Fluence Energy.

Communication style:
- Direct, technically precise, efficient - no fluff
- Command-line first mindset
- "Give me the working solution, not the theory"
- Like a senior engineer in a technical conversation

Technical background:
- Systems architect, not a developer
- "Gozinta and comesouta guy" (input/output flow expert)
- Focus: Cloud infrastructure (AWS), data engineering, BESS (battery energy storage systems)
- Team: Global Services Digital Enablement & Governance (GSDE&G)
- Environment: macOS, iTerm2, zsh, Python, AWS Glue/Athena/Step Functions
- Data lakehouse: 275TB, 23M+ data points

Core values:
- Technical excellence: production-ready, documented code
- Security first: credentials in secrets, clean git history
- Team empowerment: cross-platform, copy-paste ready tools
- Cost consciousness: every resource tagged and justified
"""

    return "\n\n".join(persona_parts)


# Load persona on startup
PERSONA_SYSTEM_PROMPT = load_persona_files()


@app.on_event("startup")
async def startup_event():
    """Verify API key and persona loaded."""
    api_key_path = Path("/run/secrets/openai_api_key")

    if not api_key_path.exists():
        # Fallback to environment variable
        if not os.getenv("OPENAI_API_KEY"):
            print("WARNING: No API key found at /run/secrets/openai_api_key or OPENAI_API_KEY env var")

    print("✅ Isaiah Chat Service started")
    print(f"✅ Persona loaded ({len(PERSONA_SYSTEM_PROMPT)} chars)")


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker."""
    return {
        "status": "healthy",
        "service": "isaiah-chat",
        "persona_loaded": len(PERSONA_SYSTEM_PROMPT) > 0,
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process chat message with Isaiah's personality.

    This endpoint is called by the Gateway after PII sanitization.
    """
    # Get API key from Docker secret or environment
    api_key_path = Path("/run/secrets/openai_api_key")

    if api_key_path.exists():
        api_key = api_key_path.read_text().strip()
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=500,
                detail="OpenAI API key not configured"
            )

    try:
        client = openai.OpenAI(api_key=api_key)

        # Call OpenAI API with Isaiah's persona
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=2048,
            messages=[
                {
                    "role": "system",
                    "content": PERSONA_SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": request.content
                }
            ]
        )

        response_text = response.choices[0].message.content

        return ChatResponse(
            response=response_text,
            model=response.model,
            tokens_used=response.usage.prompt_tokens + response.usage.completion_tokens
        )

    except openai.APIError as e:
        raise HTTPException(
            status_code=500,
            detail=f"OpenAI API error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18789)
