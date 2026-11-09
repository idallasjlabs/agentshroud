# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Curated tool descriptors for the Inbound MCP Edge (SCRUM-211, threat T7).

Hosted agents never see a raw passthrough tool. They see only the descriptors
below: narrow, closed JSON Schemas (``additionalProperties: false``, bounded
lengths, enums, character allowlists, no free-form paths or shell strings).

Each descriptor is hashed (SHA-256 over canonical JSON). The hashes are listed in
``config/inbound-edge/descriptors.manifest.json``, which is signed with an
Ed25519 key the owner holds. At startup the edge and the gateway both call
:func:`verify_descriptors`; any drift — an edited description, a widened schema,
an added tool — refuses to start. Changing a tool therefore requires a new
signed manifest, i.e. a deliberate release.

IEC 62443 alignment: FR3 (System Integrity) — integrity of the tool surface
exposed to untrusted principals.
"""

import base64
import binascii
import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

CONFIG_DIR = Path(__file__).resolve().parents[2] / "config" / "inbound-edge"
MANIFEST_PATH = CONFIG_DIR / "descriptors.manifest.json"
SIGNATURE_PATH = CONFIG_DIR / "descriptors.manifest.sig"
PUBLIC_KEY_PATH = CONFIG_DIR / "descriptors.pub.pem"

MANIFEST_VERSION = 1

# Printable text only: no C0 control characters and no DEL. The end anchor is
# (?![\\s\\S]) rather than $: Python's re (used by jsonschema) lets $ match before a
# trailing newline, so "x\\n" passed — found by test_edge_fuzz. The lookahead means
# end-of-string in both Python and ECMA-262 regex dialects.
_SINGLE_LINE = "^[^\\u0000-\\u001f\\u007f]+(?![\\s\\S])"
# Free text may carry newlines and tabs, but no other control characters.
_MULTI_LINE = "^[^\\u0000-\\u0008\\u000b-\\u001f\\u007f]+(?![\\s\\S])"
# secrets.token_urlsafe(32) — the format approval tickets are minted in.
_TICKET = {"type": "string", "pattern": "^[A-Za-z0-9_-]{43}$", "maxLength": 43}

TOOL_DESCRIPTORS: Dict[str, Dict[str, Any]] = {
    "lab_search": {
        "version": "1.0.0",
        "access": "read",
        "description": (
            "Search the web through the owner's private SearXNG instance. "
            "Returns titles, URLs and snippets only."
        ),
        "inputSchema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["query"],
            "properties": {
                "query": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 256,
                    "pattern": _SINGLE_LINE,
                },
                "max_results": {"type": "integer", "enum": [5, 10, 20]},
            },
        },
    },
    "pke_status": {
        "version": "1.0.0",
        "access": "read",
        "description": (
            "Read-only status of the owner's published podcast feeds: last "
            "episode date, episode count and freshness per feed."
        ),
        "inputSchema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "detail": {"type": "string", "enum": ["summary", "per_feed"]},
            },
        },
    },
    "delegate_to_hermes": {
        "version": "1.0.0",
        "access": "write",
        "requires_local_agent": "hermes",
        "description": (
            "Ask the owner's local agent to carry out a task. Every call needs "
            "the owner's approval: the first call returns an approval ticket; "
            "repeat the identical call with that ticket once it is approved."
        ),
        "inputSchema": {
            "type": "object",
            "additionalProperties": False,
            "required": ["task", "priority"],
            "properties": {
                "task": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 2000,
                    "pattern": _MULTI_LINE,
                },
                "priority": {"type": "string", "enum": ["low", "normal", "high"]},
                "approval_ticket": _TICKET,
            },
        },
    },
}


class DescriptorIntegrityError(RuntimeError):
    """The served descriptors do not match the signed manifest. Refuse to start."""


def canonical_bytes(obj: Any) -> bytes:
    """Canonical JSON: sorted keys, no insignificant whitespace, UTF-8."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def descriptor_hash(descriptor: Mapping[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(descriptor)).hexdigest()


def build_manifest(descriptors: Mapping[str, Mapping[str, Any]] = TOOL_DESCRIPTORS) -> dict:
    return {
        "manifest_version": MANIFEST_VERSION,
        "tools": {
            name: {"version": desc["version"], "sha256": descriptor_hash(desc)}
            for name, desc in sorted(descriptors.items())
        },
    }


def _load_public_key(public_key_pem: bytes) -> Ed25519PublicKey:
    try:
        key = serialization.load_pem_public_key(public_key_pem)
    except (ValueError, TypeError) as exc:
        raise DescriptorIntegrityError(f"unreadable public key: {exc}") from exc
    if not isinstance(key, Ed25519PublicKey):
        raise DescriptorIntegrityError("descriptor signing key must be Ed25519")
    return key


def verify_descriptors(
    manifest: Mapping[str, Any],
    signature_b64: str,
    public_key_pem: bytes,
    descriptors: Mapping[str, Mapping[str, Any]] = TOOL_DESCRIPTORS,
) -> None:
    """Verify the manifest signature, then that ``descriptors`` match it exactly.

    Raises :class:`DescriptorIntegrityError` on any mismatch. Never returns a
    partial result: either every served descriptor is the signed one, or none is.
    """
    key = _load_public_key(public_key_pem)
    try:
        signature = base64.b64decode(signature_b64, validate=True)
        key.verify(signature, canonical_bytes(manifest))
    except (binascii.Error, ValueError, InvalidSignature) as exc:
        raise DescriptorIntegrityError("manifest signature invalid") from exc

    signed = manifest.get("tools", {})
    served = set(descriptors)
    unsigned = served - set(signed)
    if unsigned:
        raise DescriptorIntegrityError(f"tools not in signed manifest: {sorted(unsigned)}")
    missing = set(signed) - served
    if missing:
        raise DescriptorIntegrityError(f"signed tools missing from code: {sorted(missing)}")
    for name in sorted(served):
        if descriptor_hash(descriptors[name]) != signed[name].get("sha256"):
            raise DescriptorIntegrityError(f"descriptor drift: {name}")


def verify_shipped_descriptors() -> None:
    """Startup check against the manifest, signature and key committed under config/."""
    try:
        manifest = json.loads(MANIFEST_PATH.read_text())
        signature = SIGNATURE_PATH.read_text().strip()
        public_key = PUBLIC_KEY_PATH.read_bytes()
    except (OSError, ValueError) as exc:
        raise DescriptorIntegrityError(f"descriptor manifest unavailable: {exc}") from exc
    verify_descriptors(manifest, signature, public_key, TOOL_DESCRIPTORS)


def mcp_tool(name: str) -> dict:
    """The MCP ``Tool`` view of a descriptor (internal fields stripped)."""
    desc = TOOL_DESCRIPTORS[name]
    return {
        "name": name,
        "description": desc["description"],
        "inputSchema": copy.deepcopy(desc["inputSchema"]),
    }


# ── owner signing workflow ───────────────────────────────────────────────────
#
#   python -m gateway.inbound_edge.descriptors keygen | keyring set agentshroud-edge descriptors
#   python -m gateway.inbound_edge.descriptors manifest
#   keyring get agentshroud-edge descriptors | python -m gateway.inbound_edge.descriptors sign
#
# keygen prints the raw Ed25519 private key once, base64 on one line, for a
# keychain/1Password to store; only the public key is written to disk. sign reads
# the key from stdin (never argv), refuses a key that does not match the committed
# public key, and verifies the result before writing the signature.


def main(argv=None, stdin=None) -> int:
    import argparse
    import sys

    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

    parser = argparse.ArgumentParser(prog="python -m gateway.inbound_edge.descriptors")
    parser.add_argument("command", choices=["keygen", "manifest", "sign", "verify"])
    parser.add_argument("--manifest", type=Path, default=MANIFEST_PATH)
    parser.add_argument("--signature", type=Path, default=SIGNATURE_PATH)
    parser.add_argument("--public-key", type=Path, default=PUBLIC_KEY_PATH)
    args = parser.parse_args(argv)
    stdin = stdin or sys.stdin

    if args.command == "keygen":
        key = Ed25519PrivateKey.generate()
        args.public_key.write_bytes(
            key.public_key().public_bytes(
                serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
        raw = key.private_bytes(
            serialization.Encoding.Raw,
            serialization.PrivateFormat.Raw,
            serialization.NoEncryption(),
        )
        print(base64.b64encode(raw).decode())
        return 0
    if args.command == "manifest":
        args.manifest.write_text(json.dumps(build_manifest(), indent=2, sort_keys=True) + "\n")
        return 0
    if args.command == "sign":
        try:
            key = Ed25519PrivateKey.from_private_bytes(base64.b64decode(stdin.readline().strip()))
        except (binascii.Error, ValueError):
            print("sign: stdin did not contain a base64 Ed25519 private key", file=sys.stderr)
            return 1
        manifest = json.loads(args.manifest.read_text())
        signature = base64.b64encode(key.sign(canonical_bytes(manifest))).decode()
        try:
            verify_descriptors(manifest, signature, args.public_key.read_bytes())
        except DescriptorIntegrityError as exc:
            print(f"sign: refusing to write signature: {exc}", file=sys.stderr)
            return 1
        args.signature.write_text(signature + "\n")
        return 0
    try:
        verify_descriptors(
            json.loads(args.manifest.read_text()),
            args.signature.read_text().strip(),
            args.public_key.read_bytes(),
        )
    except (OSError, DescriptorIntegrityError) as exc:
        print(f"verify: FAILED: {exc}", file=sys.stderr)
        return 1
    print("verify: OK")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
