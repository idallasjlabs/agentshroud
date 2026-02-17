# PR #4 Round 1 - Gemini Review

## CRITICAL
1. XSS in renderApprovals onclick concatenation → FIXED (event delegation + data attributes)
2. EventBus _lock never used → FIXED (async lock on all shared state)

## HIGH  
3. Auth token in URL query param → Accepted (local network only, Tailscale)
4. Event count merge logic → FIXED (Math.max)

## MEDIUM
5. Inconsistent WS subscription → Accepted (parallel mechanism intentional)
6. Missing CSP → FIXED (CSP header added)
