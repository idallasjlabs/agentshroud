"""
Encrypted Memory Store — AES-256-GCM encryption for data at rest.

Provides EncryptedStore class for encrypting audit ledger entries,
cached PII, and memory/state files. Supports key rotation.
"""

import base64
import json
import os
import struct
import time
from pathlib import Path
from typing import Any, Optional, Union

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# Blob format: version(1) + salt(16) + nonce(12) + key_id(4) + ciphertext(...)
BLOB_VERSION = 1
SALT_SIZE = 16
NONCE_SIZE = 12
KEY_ID_SIZE = 4
HEADER_SIZE = 1 + SALT_SIZE + NONCE_SIZE + KEY_ID_SIZE


class EncryptedStore:
    """AES-256-GCM encrypted storage with key derivation and rotation support."""

    def __init__(
        self,
        master_secret: Optional[str] = None,
        secret_path: Optional[str] = None,
        iterations: int = 600_000,
        key_id: int = 1,
    ):
        """
        Initialize the encrypted store.

        Args:
            master_secret: The master secret string. If None, reads from secret_path
                or SECURECLAW_MASTER_SECRET env var.
            secret_path: Path to Docker secret file (e.g. /run/secrets/master_key).
            iterations: PBKDF2 iteration count.
            key_id: Numeric key identifier for rotation tracking.
        """
        self.iterations = iterations
        self.key_id = key_id
        self._master_secret = self._resolve_secret(master_secret, secret_path)
        if not self._master_secret:
            raise ValueError(
                "No master secret provided. Set master_secret, secret_path, "
                "or SECURECLAW_MASTER_SECRET environment variable."
            )

    @staticmethod
    def _resolve_secret(
        master_secret: Optional[str], secret_path: Optional[str]
    ) -> Optional[bytes]:
        """Resolve master secret from args, file, or environment."""
        if master_secret:
            return master_secret.encode("utf-8")
        if secret_path:
            p = Path(secret_path)
            if p.exists():
                return p.read_bytes().strip()
        env_secret = os.environ.get("SECURECLAW_MASTER_SECRET")
        if env_secret:
            return env_secret.encode("utf-8")
        return None

    def _derive_key(self, salt: bytes) -> bytes:
        """Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.iterations,
        )
        return kdf.derive(self._master_secret)

    def encrypt(self, data: Union[str, bytes, dict]) -> bytes:
        """
        Encrypt data using AES-256-GCM.

        Args:
            data: String, bytes, or dict (JSON-serialized) to encrypt.

        Returns:
            Encrypted blob containing version, salt, nonce, key_id, and ciphertext.
        """
        if isinstance(data, dict):
            plaintext = json.dumps(data, default=str).encode("utf-8")
        elif isinstance(data, str):
            plaintext = data.encode("utf-8")
        else:
            plaintext = data

        salt = os.urandom(SALT_SIZE)
        nonce = os.urandom(NONCE_SIZE)
        key = self._derive_key(salt)

        aesgcm = AESGCM(key)

        # Use version + key_id as AAD to prevent header tampering
        aad = struct.pack("B", BLOB_VERSION) + struct.pack(">I", self.key_id)
        ciphertext = aesgcm.encrypt(nonce, plaintext, aad)

        blob = (
            struct.pack("B", BLOB_VERSION)
            + salt
            + nonce
            + struct.pack(">I", self.key_id)
            + ciphertext
        )
        return blob

    def decrypt(self, blob: bytes) -> bytes:
        """
        Decrypt an AES-256-GCM encrypted blob.

        Args:
            blob: The encrypted blob from encrypt().

        Returns:
            Decrypted data as bytes.

        Raises:
            ValueError: If blob format is invalid.
            cryptography.exceptions.InvalidTag: If decryption fails.
        """
        if len(blob) < HEADER_SIZE:
            raise ValueError("Invalid blob: too short")

        version = struct.unpack("B", blob[0:1])[0]
        if version != BLOB_VERSION:
            raise ValueError(f"Unsupported blob version: {version}")

        offset = 1
        salt = blob[offset : offset + SALT_SIZE]
        offset += SALT_SIZE
        nonce = blob[offset : offset + NONCE_SIZE]
        offset += NONCE_SIZE
        blob_key_id = struct.unpack(">I", blob[offset : offset + KEY_ID_SIZE])[0]
        offset += KEY_ID_SIZE
        ciphertext = blob[offset:]

        key = self._derive_key(salt)
        aesgcm = AESGCM(key)

        # Reconstruct AAD from blob header
        aad = struct.pack("B", version) + struct.pack(">I", blob_key_id)
        return aesgcm.decrypt(nonce, ciphertext, aad)

    def decrypt_str(self, blob: bytes) -> str:
        """Decrypt and return as UTF-8 string."""
        return self.decrypt(blob).decode("utf-8")

    def decrypt_json(self, blob: bytes) -> dict:
        """Decrypt and return as parsed JSON dict."""
        return json.loads(self.decrypt(blob))

    def encrypt_b64(self, data: Union[str, bytes, dict]) -> str:
        """Encrypt and return as base64-encoded string."""
        return base64.b64encode(self.encrypt(data)).decode("ascii")

    def decrypt_b64(self, b64_blob: str) -> bytes:
        """Decrypt a base64-encoded blob."""
        return self.decrypt(base64.b64decode(b64_blob))

    def get_blob_key_id(self, blob: bytes) -> int:
        """Extract the key_id from an encrypted blob without decrypting."""
        if len(blob) < HEADER_SIZE:
            raise ValueError("Invalid blob: too short")
        offset = 1 + SALT_SIZE + NONCE_SIZE
        return struct.unpack(">I", blob[offset : offset + KEY_ID_SIZE])[0]

    def rotate(
        self,
        blobs: list[bytes],
        new_secret: str,
        new_key_id: Optional[int] = None,
    ) -> tuple["EncryptedStore", list[bytes]]:
        """
        Re-encrypt blobs with a new master secret.

        Args:
            blobs: List of encrypted blobs to re-encrypt.
            new_secret: The new master secret.
            new_key_id: New key identifier. Defaults to current + 1.

        Returns:
            Tuple of (new_store, list_of_reencrypted_blobs).
        """
        new_kid = new_key_id if new_key_id is not None else self.key_id + 1
        new_store = EncryptedStore(
            master_secret=new_secret,
            iterations=self.iterations,
            key_id=new_kid,
        )
        new_blobs = []
        for blob in blobs:
            plaintext = self.decrypt(blob)
            new_blobs.append(new_store.encrypt(plaintext))
        return new_store, new_blobs
