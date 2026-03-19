---
title: python-jose
type: dependency
tags: [authentication, jwt, cryptography, python]
related: [Gateway Core/auth.py, Dependencies/All Dependencies]
status: documented
---

# python-jose

**Package:** `python-jose[cryptography]`
**Version:** ≥3.3.0,<4.0.0
**Used in:** Gateway authentication

## Purpose

JWT (JSON Web Token) and HMAC cryptography library. Used for authentication token operations including HMAC-based shared secret validation and JWT token handling if extended to JWT auth.

## Current Usage

AgentShroud currently uses **shared-secret** authentication (`auth_method: shared_secret`). `python-jose` provides the HMAC comparison utilities used in `auth.py` for constant-time token validation.

## Key Features

| Feature | Usage |
|---------|-------|
| `hmac.compare_digest` | Constant-time comparison to prevent timing attacks |
| JWT encoding/decoding | Available for future OAuth/JWT auth method |

## Auth Methods

Per `agentshroud.yaml`:
```yaml
gateway:
  auth_method: "shared_secret"
```

Currently only `shared_secret` is implemented. JWT is available via python-jose if `auth_method` is extended.

## Security Note

Always use constant-time comparison (`hmac.compare_digest` or `secrets.compare_digest`) when comparing auth tokens. Never use `==` which is vulnerable to timing attacks.

## Related Notes

- [[Gateway Core/auth.py|auth.py]] — Authentication implementation
- [[GATEWAY_AUTH_TOKEN]] — The shared secret
- [[Dependencies/All Dependencies]] — Full dependency list
