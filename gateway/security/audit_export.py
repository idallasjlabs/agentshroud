# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Audit export functionality with CEF, JSON-LD, and JSON formats.

Exports security audit logs in compliance-ready formats with tamper-evident 
verification capabilities.
"""

import json
import logging
from datetime import datetime, timezone
from io import StringIO
from typing import Optional, TextIO, Union
from urllib.parse import quote

from .audit_store import AuditEvent, AuditStore

logger = logging.getLogger("agentshroud.gateway.security.audit_export")


class AuditExportConfig:
    """Configuration for audit export functionality."""

    def __init__(
        self,
        default_format: str = "json",
        cef_vendor: str = "AgentShroud",
        cef_product: str = "Gateway",
        cef_version: str = "0.7.0",
        jsonld_context: Optional[dict] = None,
        include_hash_verification: bool = True,
    ):
        self.default_format = default_format
        self.cef_vendor = cef_vendor
        self.cef_product = cef_product
        self.cef_version = cef_version
        self.jsonld_context = jsonld_context or self._default_jsonld_context()
        self.include_hash_verification = include_hash_verification

    @staticmethod
    def _default_jsonld_context() -> dict:
        """Default JSON-LD context for security ontology."""
        return {
            "@context": {
                "security": "https://w3id.org/security#",
                "event": "security:AuditEvent", 
                "timestamp": {"@type": "@id"},
                "severity": "security:threatLevel",
                "eventType": "security:eventCategory",
                "sourceModule": "security:source",
                "details": "security:eventData",
                "entryHash": "security:cryptographicHash",
                "previousHash": "security:previousHash"
            }
        }


class AuditExporter:
    """Exports audit events in various compliance formats."""

    def __init__(self, config: AuditExportConfig, audit_store: AuditStore):
        self.config = config
        self.audit_store = audit_store

    async def export_events(
        self,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        format_type: str = "json",
        output: Optional[Union[str, TextIO]] = None,
        event_type: Optional[str] = None,
        severity_min: Optional[str] = None,
        limit: int = 10000,
    ) -> dict:
        """Export audit events in the specified format.
        
        Args:
            start_time: ISO timestamp to start export from
            end_time: ISO timestamp to end export at
            format_type: Export format ('cef', 'json-ld', 'json')
            output: File path or TextIO object to write to (None = return string)
            event_type: Filter by event type
            severity_min: Filter by minimum severity level
            limit: Maximum number of events to export
            
        Returns:
            Dict with export results including record count, hash verification
        """
        # Query events from store
        events = await self.audit_store.query_events(
            start_time=start_time,
            end_time=end_time,
            event_type=event_type,
            severity_min=severity_min,
            limit=limit,
        )

        if not events:
            return {
                "format": format_type,
                "record_count": 0,
                "hash_verification": {"verified": True, "message": "No events to verify"},
                "export_content": "",
            }

        # Verify hash chain if enabled
        hash_verification = {"verified": True, "message": "Hash verification disabled"}
        if self.config.include_hash_verification:
            verified, message = await self.audit_store.verify_hash_chain(
                start_id=events[-1].event_id if events else None, 
                limit=limit
            )
            hash_verification = {"verified": verified, "message": message}

        # Generate export content
        if format_type.lower() == "cef":
            export_content = self._export_cef(events)
        elif format_type.lower() == "json-ld":
            export_content = self._export_jsonld(events)
        else:  # Default to JSON
            export_content = self._export_json(events)

        # Write to output if specified
        if output:
            if isinstance(output, str):
                with open(output, "w") as f:
                    f.write(export_content)
            else:
                output.write(export_content)

        return {
            "format": format_type,
            "record_count": len(events),
            "hash_verification": hash_verification,
            "export_content": export_content if output is None else None,
            "export_timestamp": datetime.now(tz=timezone.utc).isoformat() + "Z",
        }

    def _export_cef(self, events: list[AuditEvent]) -> str:
        """Export events in Common Event Format (CEF).
        
        CEF Format: CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
        """
        output = StringIO()
        
        for event in events:
            # Map severity to CEF numeric scale (0-10)
            severity_map = {
                "CRITICAL": "10",
                "HIGH": "7", 
                "MEDIUM": "5",
                "LOW": "3",
                "INFO": "1"
            }
            cef_severity = severity_map.get(event.severity, "5")
            
            # Escape pipe characters in fields
            def escape_cef(text: str) -> str:
                return str(text).replace("|", "\\|").replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r")
            
            # Build extensions
            extensions = []
            if event.details:
                for key, value in event.details.items():
                    # Convert to CEF extension format (key=value)
                    safe_key = "".join(c for c in key if c.isalnum() or c in "_-")
                    safe_value = quote(str(value)) if value else ""
                    extensions.append(f"{safe_key}={safe_value}")
            
            # Add hash information
            extensions.append(f"entryHash={event.entry_hash}")
            if event.prev_hash:
                extensions.append(f"previousHash={event.prev_hash}")
            extensions.append(f"sourceModule={escape_cef(event.source_module)}")
            extensions.append(f"eventId={escape_cef(event.event_id)}")
            
            extension_str = " ".join(extensions)
            
            # Build CEF record
            cef_line = (
                f"CEF:0|{escape_cef(self.config.cef_vendor)}|{escape_cef(self.config.cef_product)}|"
                f"{escape_cef(self.config.cef_version)}|{escape_cef(event.event_type)}|"
                f"{escape_cef(event.event_type)}|{cef_severity}|{extension_str}"
            )
            
            output.write(cef_line + "\n")
        
        return output.getvalue()

    def _parse_cef_for_verification(self, cef_content: str) -> list[dict]:
        """Parse CEF lines and extract entryHash/previousHash for chain verification.

        Returns a list of dicts with keys: entry_hash, prev_hash.
        Lines that cannot be parsed are skipped.
        """
        records = []
        for line in cef_content.splitlines():
            line = line.strip()
            if not line or not line.startswith("CEF:"):
                continue
            # Extension fields are everything after the 7th pipe-delimited field
            # CEF:Version|Vendor|Product|Version|EventClassID|Name|Severity|Extensions
            parts = line.split("|", 7)
            if len(parts) < 8:
                continue
            extensions = parts[7]
            entry_hash = None
            prev_hash = None
            for field in extensions.split(" "):
                if field.startswith("entryHash="):
                    entry_hash = field[len("entryHash="):]
                elif field.startswith("previousHash="):
                    prev_hash = field[len("previousHash="):]
            if entry_hash:
                records.append({"entry_hash": entry_hash, "prev_hash": prev_hash})
        return records

    def _export_jsonld(self, events: list[AuditEvent]) -> str:
        """Export events in JSON-LD format with security ontology."""
        export_data = {
            **self.config.jsonld_context,
            "@type": "AuditExport",
            "exportTimestamp": datetime.now(tz=timezone.utc).isoformat() + "Z",
            "events": []
        }
        
        for event in events:
            jsonld_event = {
                "@type": "event",
                "eventId": event.event_id,
                "timestamp": event.timestamp,
                "eventType": event.event_type,
                "severity": event.severity,
                "sourceModule": event.source_module,
                "details": event.details,
                "entryHash": event.entry_hash,
            }
            
            if event.prev_hash:
                jsonld_event["previousHash"] = event.prev_hash
                
            export_data["events"].append(jsonld_event)
        
        return json.dumps(export_data, indent=2, sort_keys=True)

    def _export_json(self, events: list[AuditEvent]) -> str:
        """Export events in standard JSON format."""
        export_data = {
            "export_metadata": {
                "format": "json",
                "export_timestamp": datetime.now(tz=timezone.utc).isoformat() + "Z",
                "record_count": len(events),
                "vendor": self.config.cef_vendor,
                "product": self.config.cef_product,
                "version": self.config.cef_version,
            },
            "events": [event.to_dict() for event in events]
        }
        
        return json.dumps(export_data, indent=2, sort_keys=True)

    async def verify_export_integrity(self, export_content: str, format_type: str = "json") -> dict:
        """Verify the integrity of an exported audit log.
        
        Args:
            export_content: The exported content to verify
            format_type: Format of the export ('json', 'json-ld', 'cef')
            
        Returns:
            Dict with verification results
        """
        try:
            if format_type.lower() == "json":
                data = json.loads(export_content)
                events = data.get("events", [])
            elif format_type.lower() == "json-ld":
                data = json.loads(export_content)
                events = data.get("events", [])
            else:  # CEF format
                events = self._parse_cef_for_verification(export_content)

            if not events:
                return {"verified": True, "message": "No events to verify"}
            
            # Sort events by timestamp for hash chain verification (JSON/JSON-LD only)
            if format_type.lower() != "cef":
                events.sort(key=lambda e: e.get("timestamp", "") if isinstance(e, dict) else getattr(e, "timestamp", ""))

            # Verify hash chain in the export
            expected_prev_hash = None
            for i, event_data in enumerate(events):
                if format_type.lower() == "cef":
                    # CEF records have entry_hash and prev_hash extracted from extensions
                    entry_hash = event_data.get("entry_hash")
                    prev_hash = event_data.get("prev_hash")
                    if prev_hash != expected_prev_hash:
                        return {
                            "verified": False,
                            "message": f"CEF hash chain broken at record {i+1}: "
                                       f"expected prev_hash={expected_prev_hash}, got={prev_hash}",
                        }
                    expected_prev_hash = entry_hash
                else:
                    # JSON / JSON-LD: full event recomputation
                    event_id = event_data.get("event_id")
                    entry_hash = event_data.get("entry_hash")
                    prev_hash = event_data.get("prev_hash")

                    event = AuditEvent(
                        event_id=event_id,
                        event_type=event_data.get("event_type"),
                        severity=event_data.get("severity"),
                        source_module=event_data.get("source_module"),
                        details=event_data.get("details", {}),
                        timestamp=event_data.get("timestamp"),
                    )

                    if prev_hash != expected_prev_hash:
                        return {
                            "verified": False,
                            "message": f"Hash chain broken at event {i+1} ({event_id}): expected prev_hash {expected_prev_hash}, got {prev_hash}"
                        }

                    computed_hash = event.compute_entry_hash(prev_hash)
                    if computed_hash != entry_hash:
                        return {
                            "verified": False,
                            "message": f"Entry hash mismatch at event {i+1} ({event_id}): expected {computed_hash}, got {entry_hash}"
                        }

                    expected_prev_hash = entry_hash

            return {"verified": True, "message": f"Verified {len(events)} events in export"}

        except json.JSONDecodeError as e:
            return {"verified": False, "message": f"Invalid JSON: {e}"}
        except Exception as e:
            return {"verified": False, "message": f"Verification error: {e}"}