---
title: encrypted_store.py
type: module
file_path: gateway/security/encrypted_store.py
tags: [security, encryption, aes-gcm, key-derivation, pbkdf2, data-at-rest, key-rotation]
related: ["[[Security Modules/canary.py|canary.py]]", "[[Security Modules/env_guard.py|env_guard.py]]", "[[Data Flow]]"]
status: documented
---

# encrypted_store.py

## Purpose
Provides AES-256-GCM authenticated encryption for data at rest — audit ledger entries, cached PII, and state files. Supports key rotation by re-encrypting existing blobs under a new master secret.

## Threat Model
Data at rest exposure — an attacker gaining read access to audit logs, PII cache files, or memory/state dumps and recovering plaintext content. Also covers key compromise: the key rotation mechanism allows re-encryption after a suspected key exposure without data loss.

## Responsibilities
- Derive a 256-bit AES key per encryption operation from a master secret using PBKDF2-HMAC-SHA256 with a fresh random 16-byte salt and 600,000 iterations (NIST recommended minimum as of 2023)
- Encrypt data (str, bytes, or dict) using AES-256-GCM with a random 12-byte nonce and authenticated additional data (AAD) covering the blob version and key ID
- Produce a self-describing binary blob: version(1) + salt(16) + nonce(12) + key_id(4) + ciphertext
- Decrypt blobs with header validation and AAD reconstruction
- Zero key material in memory after use via `ctypes.memset` (best-effort for CPython)
- Resolve master secret from: direct argument, Docker secrets file, or `AGENTSHROUD_MASTER_SECRET` environment variable
- Support base64-encoded blob variants for JSON-safe transport
- Provide `rotate()` to re-encrypt a list of blobs under a new master secret

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `_secure_zero()` | Function | Best-effort memory zeroing of key material |
| `EncryptedStore` | Class | Main encryption/decryption class |
| `EncryptedStore.encrypt()` | Method | Encrypt data; returns binary blob |
| `EncryptedStore.decrypt()` | Method | Decrypt blob; returns bytes |
| `EncryptedStore.decrypt_str()` | Method | Decrypt to UTF-8 string |
| `EncryptedStore.decrypt_json()` | Method | Decrypt to parsed dict |
| `EncryptedStore.encrypt_b64()` | Method | Encrypt and return base64 string |
| `EncryptedStore.decrypt_b64()` | Method | Decrypt base64-encoded blob |
| `EncryptedStore.get_blob_key_id()` | Method | Extract key_id from blob without decryption |
| `EncryptedStore.rotate()` | Method | Re-encrypt blobs under new master secret |

## Function Details

### EncryptedStore.__init__(master_secret, secret_path, iterations, key_id)
**Purpose:** Initialize the store, resolving the master secret from args, file, or environment.
**Parameters:**
- `master_secret` (str | None) — plaintext master secret
- `secret_path` (str | None) — path to Docker secret file
- `iterations` (int, default 600,000) — PBKDF2 iteration count
- `key_id` (int, default 1) — key version identifier for rotation tracking
**Raises:** `ValueError` if no master secret can be resolved.

### EncryptedStore.encrypt(data)
**Purpose:** Generate a fresh salt and nonce per call, derive key, encrypt with AES-256-GCM using version+key_id as AAD, zero the key, return the binary blob.
**Parameters:** `data` (str | bytes | dict) — dict is JSON-serialized before encryption
**Returns:** bytes — self-describing encrypted blob
**Side effects:** Calls `os.urandom()` for salt and nonce; zeroes derived key via `_secure_zero()`.

### EncryptedStore.decrypt(blob)
**Purpose:** Parse the blob header, validate version, derive key from embedded salt, decrypt with AES-256-GCM, zero the key.
**Parameters:** `blob` (bytes)
**Returns:** bytes (plaintext)
**Raises:** `ValueError` if blob too short or wrong version; `cryptography.exceptions.InvalidTag` if decryption fails (indicates tampering or wrong key).
**Side effects:** Zeroes derived key via `_secure_zero()`.

### EncryptedStore.rotate(blobs, new_secret, new_key_id)
**Purpose:** Decrypt each blob with the current store, re-encrypt with a new `EncryptedStore` initialized with `new_secret`. Zeroes plaintext bytearrays after re-encryption.
**Parameters:**
- `blobs` (list[bytes]) — encrypted blobs to rotate
- `new_secret` (str) — new master secret
- `new_key_id` (int | None) — defaults to current key_id + 1
**Returns:** `tuple[EncryptedStore, list[bytes]]` — new store instance and re-encrypted blobs.

### _secure_zero(buffer)
**Purpose:** Overwrite key material bytes to zero using `ctypes.memset`. Works on `bytearray` reliably; attempts CPython-specific internal buffer access for immutable `bytes` objects (defense-in-depth; Python may retain copies).
**Side effects:** Modifies the buffer in-place.

## Blob Wire Format

```
Offset  Size  Description
0       1     Version (currently 1)
1       16    Salt (random, per encryption)
17      12    Nonce (random, per encryption)
29      4     Key ID (big-endian uint32)
33      N     Ciphertext + GCM authentication tag
```

AAD for GCM = bytes([version]) + struct.pack(">I", key_id)

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `iterations` | 600,000 | PBKDF2 iteration count |
| `key_id` | 1 | Numeric key version (increment on rotation) |
| `secret_path` | None | Path to Docker secrets file |

## Mode: Enforce vs Monitor
Not applicable. Encryption is always active; there is no monitor/passthrough mode.

## Environment Variables

| Variable | Description |
|----------|-------------|
| `AGENTSHROUD_MASTER_SECRET` | Master secret if not passed directly or via secret file |

## Key Rotation Workflow
1. Call `store.rotate(all_existing_blobs, new_secret)` → returns `(new_store, new_blobs)`
2. Replace stored blobs with `new_blobs`
3. Update `AGENTSHROUD_MASTER_SECRET` or secret file to `new_secret`
4. Discard old `store` instance
5. Use `new_store` for all future operations

`get_blob_key_id()` can be used to identify which blobs belong to which key version, enabling selective rotation of only blobs encrypted with the compromised key.

## Related
- [[Data Flow]]
- [[Configuration/agentshroud.yaml]]
- [[Security Modules/canary.py|canary.py]]
- [[Security Modules/env_guard.py|env_guard.py]]
