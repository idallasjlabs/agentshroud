"""
Drift Detection — detect unauthorized container config changes.

Snapshots container configuration and compares against known-good baselines.
Alerts on seccomp profile changes, new capabilities, new mounts, new env vars.
"""

import hashlib
import hmac
import json
import sqlite3
import time
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class ContainerSnapshot:
    container_id: str
    timestamp: float
    seccomp_profile: str = "default"
    capabilities: list[str] = field(default_factory=list)
    mounts: list[str] = field(default_factory=list)
    env_vars: list[str] = field(default_factory=list)
    image: str = ""
    read_only: bool = True
    privileged: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "ContainerSnapshot":
        return cls(**data)

    def config_hash(self) -> str:
        """SHA-256 hash of the config for quick comparison."""
        canonical = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(canonical.encode()).hexdigest()


@dataclass
class DriftAlert:
    container_id: str
    timestamp: float
    category: str  # seccomp, capabilities, mounts, env, image, security
    description: str
    baseline_value: str
    current_value: str
    severity: str = "high"  # low, medium, high, critical


class DriftDetector:
    """Detect configuration drift from known-good baselines."""

    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self._conn = sqlite3.connect(db_path)
        if db_path != ":memory:":
            self._conn.execute("PRAGMA journal_mode=WAL")
        self._init_db()

    def _init_db(self):
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS baselines (
                container_id TEXT PRIMARY KEY,
                snapshot_json TEXT NOT NULL,
                config_hash TEXT NOT NULL,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL
            )
        """)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS drift_alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                container_id TEXT NOT NULL,
                timestamp REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                baseline_value TEXT,
                current_value TEXT,
                severity TEXT NOT NULL,
                acknowledged INTEGER DEFAULT 0
            )
        """)
        self._conn.commit()

    def set_baseline(self, snapshot: ContainerSnapshot) -> str:
        """Store a known-good baseline configuration. Returns config hash."""
        now = time.time()
        snap_json = json.dumps(snapshot.to_dict(), sort_keys=True)
        config_hash = snapshot.config_hash()

        self._conn.execute(
            """INSERT OR REPLACE INTO baselines
               (container_id, snapshot_json, config_hash, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?)""",
            (snapshot.container_id, snap_json, config_hash, now, now),
        )
        self._conn.commit()
        return config_hash

    def get_baseline(self, container_id: str) -> Optional[ContainerSnapshot]:
        """Retrieve baseline snapshot for a container."""
        row = self._conn.execute(
            "SELECT snapshot_json FROM baselines WHERE container_id = ?",
            (container_id,),
        ).fetchone()
        if not row:
            return None
        return ContainerSnapshot.from_dict(json.loads(row[0]))

    def check_drift(self, current: ContainerSnapshot) -> list[DriftAlert]:
        """Compare current config against baseline, return any drift alerts."""
        baseline = self.get_baseline(current.container_id)
        if not baseline:
            return []

        # Quick hash check
        if hmac.compare_digest(baseline.config_hash(), current.config_hash()):
            return []

        alerts = []
        now = time.time()

        # Seccomp profile
        if current.seccomp_profile != baseline.seccomp_profile:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="seccomp",
                description="Seccomp profile changed",
                baseline_value=baseline.seccomp_profile,
                current_value=current.seccomp_profile,
                severity="critical",
            ))

        # Capabilities
        new_caps = set(current.capabilities) - set(baseline.capabilities)
        if new_caps:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="capabilities",
                description=f"New capabilities added: {', '.join(sorted(new_caps))}",
                baseline_value=json.dumps(sorted(baseline.capabilities)),
                current_value=json.dumps(sorted(current.capabilities)),
                severity="critical",
            ))

        removed_caps = set(baseline.capabilities) - set(current.capabilities)
        if removed_caps:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="capabilities",
                description=f"Capabilities removed: {', '.join(sorted(removed_caps))}",
                baseline_value=json.dumps(sorted(baseline.capabilities)),
                current_value=json.dumps(sorted(current.capabilities)),
                severity="medium",
            ))

        # Mounts
        new_mounts = set(current.mounts) - set(baseline.mounts)
        if new_mounts:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="mounts",
                description=f"New mounts detected: {', '.join(sorted(new_mounts))}",
                baseline_value=json.dumps(sorted(baseline.mounts)),
                current_value=json.dumps(sorted(current.mounts)),
                severity="high",
            ))

        # Env vars
        new_env = set(current.env_vars) - set(baseline.env_vars)
        if new_env:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="env",
                description=f"New environment variables: {', '.join(sorted(new_env))}",
                baseline_value=json.dumps(sorted(baseline.env_vars)),
                current_value=json.dumps(sorted(current.env_vars)),
                severity="high",
            ))

        # Image
        if current.image != baseline.image:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="image",
                description="Container image changed",
                baseline_value=baseline.image,
                current_value=current.image,
                severity="high",
            ))

        # Security settings
        if current.privileged and not baseline.privileged:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="security",
                description="Container is now running in privileged mode",
                baseline_value="privileged=False",
                current_value="privileged=True",
                severity="critical",
            ))

        if not current.read_only and baseline.read_only:
            alerts.append(DriftAlert(
                container_id=current.container_id, timestamp=now,
                category="security",
                description="Root filesystem is no longer read-only",
                baseline_value="read_only=True",
                current_value="read_only=False",
                severity="high",
            ))

        # Store alerts
        for alert in alerts:
            self._conn.execute(
                """INSERT INTO drift_alerts
                   (container_id, timestamp, category, description,
                    baseline_value, current_value, severity)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (alert.container_id, alert.timestamp, alert.category,
                 alert.description, alert.baseline_value, alert.current_value,
                 alert.severity),
            )
        self._conn.commit()

        return alerts

    def get_alerts(
        self, container_id: Optional[str] = None,
        unacknowledged_only: bool = False, limit: int = 100
    ) -> list[dict]:
        """Retrieve stored drift alerts."""
        query = "SELECT * FROM drift_alerts WHERE 1=1"
        params = []
        if container_id:
            query += " AND container_id = ?"
            params.append(container_id)
        if unacknowledged_only:
            query += " AND acknowledged = 0"
        query += " ORDER BY timestamp DESC LIMIT ?"
        params.append(limit)

        rows = self._conn.execute(query, params).fetchall()
        return [
            {
                "id": r[0], "container_id": r[1], "timestamp": r[2],
                "category": r[3], "description": r[4],
                "baseline_value": r[5], "current_value": r[6],
                "severity": r[7], "acknowledged": bool(r[8]),
            }
            for r in rows
        ]

    def acknowledge_alert(self, alert_id: int) -> bool:
        """Mark an alert as acknowledged."""
        cursor = self._conn.execute(
            "UPDATE drift_alerts SET acknowledged = 1 WHERE id = ?", (alert_id,)
        )
        self._conn.commit()
        return cursor.rowcount > 0

    def close(self):
        self._conn.close()
