#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Quick verification script for AgentShroud Gateway

set -e

echo "=== AgentShroud Gateway Verification ==="
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version

# Check virtual environment
if [[ ! -d ../.venv ]]; then
    echo "2. Creating virtual environment..."
    cd .. && python3 -m venv .venv && cd gateway
else
    echo "2. Virtual environment exists ✓"
fi

# Install dependencies
echo "3. Installing dependencies..."
source ../.venv/bin/activate
pip install -q -r requirements.txt

# Run tests
echo "4. Running test suite..."
pytest tests/ -v --tb=short -q

echo ""
echo "5. Testing imports..."
python3 -c "from ingest_api.main import app; print('✓ FastAPI app loads')"
python3 -c "from ingest_api.config import load_config; print('✓ Config loads')"
python3 -c "from ingest_api.sanitizer import PIISanitizer; print('✓ Sanitizer loads')"

echo ""
echo "=== Verification Complete ==="
echo ""
echo "To start the gateway:"
echo "  uvicorn ingest_api.main:app --host 127.0.0.1 --port 8080"
echo ""
echo "To test with curl:"
echo "  curl http://localhost:8080/status"
echo ""
