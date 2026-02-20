# Gateway Layer

The gateway layer is the core of AgentShroud's proxy architecture. It sits between user-forwarded content and the OpenClaw agent.

## Structure

```
gateway/
├── ingest_api/
│   ├── main.py           # FastAPI application
│   ├── config.py         # Configuration loader
│   ├── models.py         # Pydantic request/response models
│   ├── auth.py           # Bearer token authentication
│   ├── sanitizer.py      # PII redaction engine
│   ├── router.py         # Multi-agent routing
│   └── ledger.py         # Data inventory tracking
├── approval_queue/
│   └── queue.py          # Action approval service
├── tests/
│   ├── conftest.py       # Test fixtures
│   ├── test_config.py
│   ├── test_sanitizer.py
│   └── test_ledger.py
├── requirements.txt      # Python dependencies
└── Dockerfile           # Gateway container image
```

## Features

### Ingest API
- `POST /forward` - Accepts forwarded content from shortcuts/browser
- `GET /status` - Health check (no auth required)
- `GET /ledger` - Query data ledger (paginated)
- `DELETE /ledger/{id}` - "Forget this" (right to erasure)
- `GET /agents` - List agent targets with health status
- `POST /approve` - Submit approval request
- `WS /ws/approvals` - Real-time approval notifications

### PII Sanitizer
- Microsoft Presidio with spaCy (if available)
- Regex fallback for Python 3.14 compatibility
- Detects: SSN, credit cards, phone, email, addresses
- **Fail closed**: Never forwards unsanitized content on error
- Configurable via agentshroud.yaml

### Data Ledger
- SQLite with aiosqlite (fully async)
- **Stores only SHA-256 hashes, never raw content**
- 90-day retention (configurable)
- Schema versioning for migrations
- Paginated query with filters

### Approval Queue
- In-memory queue (ephemeral by design)
- WebSocket broadcast for real-time notifications
- 1-hour timeout (configurable)
- Supports: email_sending, file_deletion, external_api_calls, skill_installation

### Authentication
- Bearer token with constant-time comparison (prevents timing attacks)
- Rate limiting: 100 requests/minute per IP
- Auto-generates token if not in agentshroud.yaml

## Setup

### 1. Install Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r gateway/requirements.txt
```

### 2. Configure

Edit `agentshroud.yaml` at project root:
- Set `gateway.auth_token` (or let it auto-generate)
- Configure PII redaction rules
- Set ledger retention period

### 3. Run

```bash
uvicorn gateway.ingest_api.main:app --host 127.0.0.1 --port 8080
```

Or with hot reload:

```bash
uvicorn gateway.ingest_api.main:app --host 127.0.0.1 --port 8080 --reload
```

### 4. Test

```bash
# Run test suite
pytest gateway/tests/ -v

# Health check
curl http://localhost:8080/status

# Forward content (replace <TOKEN> with actual auth token)
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"content": "My SSN is 123-45-6789", "source": "shortcut"}'
```

## Tech Stack

- Python 3.13+ (3.14 compatible with regex fallback)
- FastAPI + Uvicorn
- Microsoft Presidio + spaCy (optional, regex fallback included)
- SQLite via aiosqlite
- WebSocket
- Pydantic v2

## Implementation Status

✅ **COMPLETE** - Phase 2 implemented (2026-02-14)

- [x] Configuration loader
- [x] PII sanitizer (Presidio + regex fallback)
- [x] Data ledger (SQLite, hashes only)
- [x] Multi-agent router
- [x] Approval queue (WebSocket)
- [x] FastAPI application
- [x] Dockerfile
- [x] Test suite (17 tests, all passing)
