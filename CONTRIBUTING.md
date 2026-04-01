# Contributing to AgentShroud™

> *This communication is issued under the AgentShroud™ project. AgentShroud™ is a trademark of Isaiah Jefferson, established February 2026. All project materials, methodologies, architectures, and associated intellectual property are proprietary and confidential. Participation as a collaborator does not transfer ownership, licensing rights, or any claim to the AgentShroud™ brand or codebase without a separate written agreement.*

Thank you for your interest in contributing! This guide covers the process from setup to merge.

## Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/agentshroud.git
cd agentshroud

# 2. Create Python 3.9+ virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r gateway/requirements.txt
pip install black isort flake8 pytest-cov

# 4. Verify tests pass
pytest gateway/tests/ -v
```

## Code Style

We use these tools (enforced in CI):

- **[black](https://black.readthedocs.io/)** — Code formatting (line length 100)
- **[isort](https://pycqa.github.io/isort/)** — Import sorting (black-compatible profile)
- **[flake8](https://flake8.pycqa.org/)** — Linting

```bash
# Format
black gateway/ --line-length 100
isort gateway/ --profile black

# Lint
flake8 gateway/ --max-line-length 100
```

## Pull Request Process

1. **Branch** — Create a feature branch from `main`: `feature/your-feature`
2. **Code** — Implement your changes with tests
3. **Test** — Run full suite: `pytest gateway/tests/ -v --cov=gateway`
4. **PR** — Open a pull request against `main`
5. **Review** — Peer review by 2 AI models (automated via CI)
6. **Merge** — After approval with no CRITICAL or HIGH findings

### Requirements

- **90%+ test coverage** on new code
- **All existing tests pass** (currently 3,700+)
- **No CRITICAL or HIGH** security findings in peer review
- **Code formatted** with black/isort (CI checks this)

## Test Guidelines

- Put tests in `gateway/tests/test_<module>.py`
- Use `pytest-asyncio` for async tests
- Use fixtures from `conftest.py` where possible
- Mock external dependencies (no network calls in tests)

```python
import pytest
from gateway.ingest_api.your_module import YourClass

class TestYourClass:
    def test_basic_behavior(self):
        obj = YourClass()
        assert obj.do_thing() == expected

    @pytest.mark.asyncio
    async def test_async_behavior(self):
        result = await obj.async_method()
        assert result is not None
```

## What to Contribute

- 🐛 Bug fixes (always welcome)
- 📝 Documentation improvements
- 🔒 Security enhancements
- ✨ New security modules
- 🧪 Test coverage improvements
- 🐳 Docker/deployment improvements

## Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be respectful, inclusive, and constructive.

## Questions?

Open a [Discussion](https://github.com/idallasjlabs/agentshroud/discussions) for general questions or file a [GitHub Issue](https://github.com/idallasjlabs/agentshroud/issues) for bugs and feature requests.

## Response SLA

| Type | Response time |
|------|--------------|
| Bug report | Acknowledged within **48 hours** |
| Feature request | Reviewed within **7 days** |
| Security vulnerability | See [SECURITY.md](SECURITY.md) — 48h acknowledgment, 7-day critical fix |
| Pull request | First review within **7 days** |

---

AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633) Patent Pending — U.S. Provisional Application No. 64/018,744 Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
© 2026 Isaiah Dallas Jefferson, Jr.. All rights reserved.
See [docs/project/legal/TRADEMARK.md](docs/project/legal/TRADEMARK.md).
