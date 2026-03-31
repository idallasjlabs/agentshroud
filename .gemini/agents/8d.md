---
name: 8d-root-cause-analysis
description: >
  Use this skill when performing root cause analysis on incidents in battery energy storage systems (BESS)
  and industrial control systems. Triggers include: any mention of 'root cause', 'RCA', '8D', 'incident analysis',
  'fault analysis', 'error investigation', 'correlated events', 'anomaly detection', or when a user provides
  an Array ID, timestamp, and error data point for investigation. This skill follows the 8D (Eight Disciplines)
  methodology adapted for data-driven analysis of control system incidents. It integrates with AWS Athena
  for querying telemetry, metadata, and configuration data. No source code analysis is performed — all
  investigation is conducted through operational data, device metadata, and optionally XML configuration files
  that describe device relationships and system topology.
version: 1.0.0
domain: Industrial Control Systems / Energy Storage
data_sources:
  - AWS Athena (telemetry, metadata, alarms, events)
  - XML configuration files (device topology and relationships)
  - Historical incident reports (learning corpus)
license: Proprietary
---

# 8D Root Cause Analysis — Data-Driven Control System Investigation

## Overview

This skill guides an AI agent through a structured 8D root cause analysis process for incidents
occurring in battery energy storage systems (BESS) and related industrial control systems. The agent
operates exclusively on operational data — no source code is examined. Investigation is conducted by
querying time-series telemetry, alarm/event logs, device metadata, and system configuration data
available through AWS Athena.

The agent's objective is to systematically identify what happened, find correlated events across the
system, isolate contributing factors, and determine the root cause of an incident. Over time, the
agent builds institutional knowledge from resolved incidents to improve future investigations.

## Architecture Context

```
┌─────────────────────────────────────────────────────────────┐
│                    8D RCA Agent                              │
│  (This Skill — Orchestrates the investigation process)      │
├─────────────────────────────────────────────────────────────┤
│                    AWS Agent                                 │
│  (Data retrieval layer — queries Athena, S3, metadata)      │
├─────────────────────────────────────────────────────────────┤
│                  AWS Athena / Data Lake                      │
│  ┌──────────┐ ┌──────────┐ ┌───────────┐ ┌──────────────┐  │
│  │Telemetry │ │ Alarms & │ │  Device   │ │Configuration │  │
│  │Time-Series│ │ Events  │ │ Metadata  │ │  (XML/JSON)  │  │
│  └──────────┘ └──────────┘ └───────────┘ └──────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Input Requirements

When initiating an investigation, the user must provide:

| Parameter       | Description                                              | Example                          |
|-----------------|----------------------------------------------------------|----------------------------------|
| `array_id`      | The Array or site identifier where the incident occurred | `ARRAY-US-TX-042`                |
| `timestamp`     | The timestamp of the error/incident data point           | `2025-02-14T14:32:17Z`          |
| `error_datapoint` | The specific data point or alarm that triggered investigation | `BMS_CELL_OVERVOLT_RACK03_MOD12` |
| `severity`      | Optional — incident severity (critical/major/minor)      | `critical`                       |
| `context`       | Optional — any known context or user observations        | Free text                        |

## The 8D Investigation Process

### D0 — Planning & Scoping

**Objective:** Define the investigation scope and gather initial context before querying data.

**Actions:**
1. Confirm the input parameters (array, timestamp, error data point)
2. Determine the system topology for the affected array
   - Query device metadata from Athena to understand what devices exist at this array
   - If an XML configuration file is provided, parse it to map device relationships
   - Build a mental model: Array → Racks → Modules → Cells, plus BMS, PCS, HVAC, meters, network devices
3. Identify all relevant data tables in Athena for this array
4. Establish time windows for data collection:
   - **Narrow window:** ±5 minutes from incident timestamp
   - **Medium window:** ±15 minutes from incident timestamp
   - **Wide window:** ±60 minutes from incident timestamp (for slow-developing conditions)
5. Document the investigation plan

**Key Questions to Answer:**
- What type of system/device generated the error?
- What is the normal operating state of this data point?
- What other devices/systems are logically or physically connected?
- Has this exact error occurred before at this array?

**Athena Query Pattern — Device Discovery:**
```sql
SELECT device_id, device_type, device_name, parent_device_id, rack_id, module_id
FROM device_metadata
WHERE array_id = '{array_id}'
ORDER BY device_type, device_id;
```

**Athena Query Pattern — Historical Occurrence:**
```sql
SELECT timestamp, value, quality, status
FROM telemetry
WHERE array_id = '{array_id}'
  AND datapoint_name = '{error_datapoint}'
  AND timestamp BETWEEN date_add('day', -90, TIMESTAMP '{timestamp}')
                     AND TIMESTAMP '{timestamp}'
ORDER BY timestamp DESC
LIMIT 100;
```

---

### D1 — Team & Expertise Identification

**Objective:** Identify the domains of expertise needed based on the incident type.

**Actions:**
1. Classify the incident domain based on the error data point:
   - **Battery/Cell level:** BMS telemetry, cell voltage, temperature, SOC, SOH
   - **Power Conversion:** PCS faults, AC/DC measurements, grid-side anomalies
   - **Thermal Management:** HVAC telemetry, ambient/rack temperatures, coolant flow
   - **Controls/Communication:** Network latency, command/response gaps, protocol errors
   - **Site Infrastructure:** Utility meter, transformer, switchgear, auxiliary power
2. Flag which team members or subject matter experts should be consulted
3. Note if the incident crosses multiple domains (these are often the hardest to root-cause)

**Agent Note:** The AI agent serves as the initial investigator and data analyst. It should clearly
flag when human expertise is required for domain-specific interpretation, especially for:
- Electrochemistry anomalies (cell degradation patterns)
- Power electronics failure modes
- Grid code compliance issues
- Physical/environmental causes (water ingress, rodent damage, etc.)

---

### D2 — Problem Description (Data Collection & Characterization)

**Objective:** Build a comprehensive, data-driven description of the incident using the "IS / IS NOT" framework.

**Actions:**

#### Step 1: Collect the Error Event Data
```sql
-- Get the exact error event and surrounding data
SELECT timestamp, datapoint_name, value, quality, unit
FROM telemetry
WHERE array_id = '{array_id}'
  AND datapoint_name = '{error_datapoint}'
  AND timestamp BETWEEN date_add('minute', -15, TIMESTAMP '{timestamp}')
                     AND date_add('minute', 15, TIMESTAMP '{timestamp}')
ORDER BY timestamp ASC;
```

#### Step 2: Collect ALL Data in the Time Window
```sql
-- Get everything that happened at this array in the time window
SELECT timestamp, device_id, datapoint_name, value, quality, unit
FROM telemetry
WHERE array_id = '{array_id}'
  AND timestamp BETWEEN date_add('minute', -15, TIMESTAMP '{timestamp}')
                     AND date_add('minute', 15, TIMESTAMP '{timestamp}')
ORDER BY timestamp ASC;
```

#### Step 3: Collect Alarms and Events
```sql
SELECT timestamp, alarm_id, alarm_name, severity, device_id, state, description
FROM alarms_events
WHERE array_id = '{array_id}'
  AND timestamp BETWEEN date_add('minute', -15, TIMESTAMP '{timestamp}')
                     AND date_add('minute', 15, TIMESTAMP '{timestamp}')
ORDER BY timestamp ASC;
```

#### Step 4: Build the IS / IS NOT Matrix

| Dimension     | IS                                      | IS NOT                                   |
|---------------|------------------------------------------|------------------------------------------|
| **WHAT**      | Which data point(s) are in error state   | Which similar data points are normal      |
| **WHERE**     | Which device, rack, module, cell         | Which adjacent devices are unaffected     |
| **WHEN**      | Exact timestamp and duration             | When did it last operate normally         |
| **EXTENT**    | How many data points affected            | What is the boundary of the impact        |

#### Step 5: Establish Baseline
```sql
-- What does "normal" look like for this data point?
SELECT
  AVG(CAST(value AS DOUBLE)) as avg_val,
  MIN(CAST(value AS DOUBLE)) as min_val,
  MAX(CAST(value AS DOUBLE)) as max_val,
  STDDEV(CAST(value AS DOUBLE)) as std_dev,
  COUNT(*) as sample_count
FROM telemetry
WHERE array_id = '{array_id}'
  AND datapoint_name = '{error_datapoint}'
  AND timestamp BETWEEN date_add('day', -7, TIMESTAMP '{timestamp}')
                     AND date_add('minute', -30, TIMESTAMP '{timestamp}')
  AND quality = 'GOOD';
```

---

### D3 — Interim Containment Assessment

**Objective:** Identify what protective actions were or should be taken.

**Actions:**
1. Check if the system's built-in protections activated:
   ```sql
   SELECT timestamp, datapoint_name, value
   FROM telemetry
   WHERE array_id = '{array_id}'
     AND datapoint_name LIKE '%PROTECTION%' OR datapoint_name LIKE '%TRIP%'
         OR datapoint_name LIKE '%LIMIT%' OR datapoint_name LIKE '%SHUTDOWN%'
     AND timestamp BETWEEN date_add('minute', -5, TIMESTAMP '{timestamp}')
                        AND date_add('minute', 30, TIMESTAMP '{timestamp}')
   ORDER BY timestamp ASC;
   ```
2. Determine if the system is currently in a safe state
3. Identify if manual intervention was performed (operator commands in the log)
4. Recommend containment actions if the system is still at risk:
   - Reduce power output / curtail operation
   - Isolate affected rack/module
   - Increase monitoring frequency
   - Notify on-site personnel

**Agent Note:** The agent should ALWAYS flag safety-critical containment needs prominently.
Never downplay a potential safety issue. When in doubt, recommend the more conservative action.

---

### D4 — Root Cause Analysis (Correlated Event Detection)

**Objective:** This is the core analytical phase. Systematically identify all changes and anomalies
in the time window, correlate them, and isolate the root cause.

**Phase 4A: Anomaly Detection — Find Everything That Changed**

For each data point active at the array during the time window, compare against baseline:

```sql
-- Identify data points that deviated from normal during the incident window
WITH baseline AS (
  SELECT
    datapoint_name,
    AVG(CAST(value AS DOUBLE)) as baseline_avg,
    STDDEV(CAST(value AS DOUBLE)) as baseline_std
  FROM telemetry
  WHERE array_id = '{array_id}'
    AND timestamp BETWEEN date_add('day', -7, TIMESTAMP '{timestamp}')
                       AND date_add('hour', -1, TIMESTAMP '{timestamp}')
    AND quality = 'GOOD'
  GROUP BY datapoint_name
),
incident_data AS (
  SELECT
    datapoint_name,
    timestamp,
    CAST(value AS DOUBLE) as val
  FROM telemetry
  WHERE array_id = '{array_id}'
    AND timestamp BETWEEN date_add('minute', -{window_minutes}, TIMESTAMP '{timestamp}')
                       AND date_add('minute', {window_minutes}, TIMESTAMP '{timestamp}')
)
SELECT
  i.datapoint_name,
  i.timestamp,
  i.val as incident_value,
  b.baseline_avg,
  b.baseline_std,
  ABS(i.val - b.baseline_avg) / NULLIF(b.baseline_std, 0) as z_score
FROM incident_data i
JOIN baseline b ON i.datapoint_name = b.datapoint_name
WHERE ABS(i.val - b.baseline_avg) / NULLIF(b.baseline_std, 0) > 2.0
ORDER BY i.timestamp ASC;
```

**Phase 4B: Temporal Correlation — Build the Event Timeline**

Assemble all anomalous events in strict chronological order:

```
TIMESTAMP               | DEVICE          | DATA POINT              | VALUE    | DEVIATION
─────────────────────────────────────────────────────────────────────────────────────────────
2025-02-14T14:27:03Z    | HVAC_01         | COOLANT_FLOW_RATE       | 12.3 LPM| -2.8σ (low)
2025-02-14T14:28:45Z    | RACK_03         | RACK_INLET_TEMP         | 34.2°C  | +2.1σ (high)
2025-02-14T14:30:11Z    | RACK_03_MOD_12  | CELL_TEMP_MAX           | 38.7°C  | +3.4σ (high)
2025-02-14T14:31:58Z    | RACK_03_MOD_12  | CELL_VOLTAGE_MAX        | 3.72V   | +2.9σ (high)
2025-02-14T14:32:17Z    | BMS_RACK_03     | BMS_CELL_OVERVOLT_ALARM | ACTIVE  | *** INCIDENT ***
```

**Phase 4C: Causal Chain Analysis**

Using the timeline, work backwards from the incident to identify the causal chain:

1. **Identify the trigger event** — the first anomaly in the timeline
2. **Trace the propagation path** — how did the initial anomaly cascade through the system?
3. **Check for independent concurrent events** — are there unrelated anomalies that happened to coincide?
4. **Validate against physics** — does the causal chain make physical sense?
   - Thermal: Heat transfer takes time → temperature changes should propagate with delay
   - Electrical: Voltage/current changes propagate near-instantly within a circuit
   - Mechanical: Pump/fan failures show gradual degradation before sudden failure
   - Communication: Network issues show latency spikes or dropped packets before total failure

**Phase 4D: Device Relationship Analysis**

If an XML configuration file is provided, use it to understand:
- Parent-child device relationships
- Communication paths between devices
- Shared resources (cooling loops, DC buses, communication networks)
- Protection zone boundaries

```
Parse XML to extract:
- <Device id="..." type="..." parent="...">
- <Connection source="..." target="..." type="...">
- <ProtectionZone devices="..." trip_action="...">
```

**Phase 4E: Root Cause Determination**

Apply the "5 Whys" framework using data:

| Why # | Question                                           | Data-Driven Answer                        |
|-------|----------------------------------------------------|-------------------------------------------|
| 1     | Why did the overvoltage alarm trigger?             | Cell voltage exceeded 3.70V threshold      |
| 2     | Why did cell voltage rise above threshold?         | Cell temperature was elevated (+3.4σ)      |
| 3     | Why was cell temperature elevated?                 | Rack inlet temperature was high (+2.1σ)    |
| 4     | Why was rack inlet temperature high?               | Coolant flow rate dropped (-2.8σ)          |
| 5     | Why did coolant flow rate drop?                    | [Requires further investigation — pump data, valve position, coolant level] |

**Classification of Root Cause:**
- **Confirmed by data:** The causal chain is fully supported by telemetry evidence
- **Probable (high confidence):** The causal chain is strongly indicated but has a gap
- **Possible (medium confidence):** The data is consistent with this cause but alternatives exist
- **Inconclusive:** The data does not conclusively point to a single root cause

---

### D5 — Permanent Corrective Action Definition

**Objective:** Based on the confirmed or probable root cause, define corrective actions.

**Actions:**
1. Categorize the root cause:
   - **Equipment failure:** Component needs replacement or repair
   - **Configuration error:** Settings, thresholds, or parameters are incorrect
   - **Environmental:** External conditions exceeded design parameters
   - **Operational:** Human action or procedure caused the incident
   - **Design limitation:** System design does not adequately handle this scenario
   - **Software/firmware:** Control logic or communication issue (flag for code team)
2. Recommend specific corrective actions with priority
3. Identify if similar conditions exist at other arrays (fleet-wide risk)

```sql
-- Check if the root cause condition exists at other arrays
SELECT array_id, COUNT(*) as occurrence_count,
       MAX(timestamp) as most_recent
FROM telemetry
WHERE datapoint_name = '{root_cause_datapoint}'
  AND {root_cause_condition}
  AND timestamp > date_add('day', -30, NOW())
GROUP BY array_id
ORDER BY occurrence_count DESC;
```

---

### D6 — Implementation Verification

**Objective:** After corrective actions are implemented, verify they resolved the issue.

**Actions:**
1. Monitor the previously affected data points for return to baseline:
   ```sql
   SELECT timestamp, datapoint_name, value
   FROM telemetry
   WHERE array_id = '{array_id}'
     AND datapoint_name IN ('{affected_datapoints}')
     AND timestamp > TIMESTAMP '{correction_timestamp}'
   ORDER BY timestamp ASC;
   ```
2. Confirm no new anomalies were introduced by the corrective action
3. Verify system performance metrics are within normal range
4. Document before/after comparison

---

### D7 — Systemic Prevention

**Objective:** Prevent recurrence across the fleet.

**Actions:**
1. Update monitoring thresholds if the incident revealed blind spots
2. Create or update alarm configurations
3. Document the incident pattern for the knowledge base (see Learning System below)
4. Recommend firmware/software updates if applicable
5. Update standard operating procedures
6. Identify predictive indicators that could provide early warning

```sql
-- Create a predictive query: Did the root cause condition appear before the incident?
-- If so, how far in advance? This becomes an early warning indicator.
SELECT timestamp, value,
       date_diff('minute', timestamp, TIMESTAMP '{incident_timestamp}') as minutes_before_incident
FROM telemetry
WHERE array_id = '{array_id}'
  AND datapoint_name = '{root_cause_datapoint}'
  AND timestamp BETWEEN date_add('hour', -24, TIMESTAMP '{incident_timestamp}')
                     AND TIMESTAMP '{incident_timestamp}'
  AND {abnormal_condition}
ORDER BY timestamp ASC;
```

---

### D8 — Documentation & Recognition

**Objective:** Close the investigation with complete documentation.

**Deliverables:**
1. **8D Report** — Complete investigation record including:
   - Incident summary (D0-D2)
   - Correlated event timeline (D4)
   - Causal chain diagram (D4)
   - Root cause classification and confidence level (D4)
   - Corrective actions and verification results (D5-D6)
   - Prevention measures (D7)
2. **Knowledge Base Entry** — Structured record for the learning system
3. **Fleet Advisory** — If applicable, notification for other arrays at risk

---

## Learning System (Continuous Improvement)

The agent improves over time by maintaining a knowledge base of resolved incidents.

### Knowledge Base Schema

Each resolved incident adds an entry:

```json
{
  "incident_id": "INC-2025-0214-001",
  "array_id": "ARRAY-US-TX-042",
  "timestamp": "2025-02-14T14:32:17Z",
  "error_datapoint": "BMS_CELL_OVERVOLT_RACK03_MOD12",
  "root_cause_category": "equipment_failure",
  "root_cause_summary": "HVAC coolant pump degradation caused reduced flow, leading to thermal runaway in Rack 03",
  "causal_chain": [
    "coolant_pump_degradation",
    "reduced_coolant_flow",
    "elevated_rack_inlet_temperature",
    "elevated_cell_temperature",
    "cell_voltage_rise",
    "overvoltage_alarm"
  ],
  "early_warning_indicators": [
    {
      "datapoint": "COOLANT_FLOW_RATE",
      "condition": "value < baseline - 2*stddev",
      "lead_time_minutes": 5
    }
  ],
  "corrective_actions": ["pump_replacement", "flow_threshold_update"],
  "confidence": "confirmed",
  "resolution_date": "2025-02-15",
  "similar_incidents": ["INC-2024-0918-003", "INC-2024-1201-007"]
}
```

### Pattern Matching for New Incidents

When investigating a new incident, the agent should:

1. **Search for similar past incidents:**
   - Same error data point
   - Same device type
   - Same array or similar array configuration
   - Similar correlated event patterns
2. **Apply learned causal chains:**
   - If a known pattern matches, test the known root cause hypothesis first
   - This accelerates investigation — check the most likely cause before broad analysis
3. **Identify novel patterns:**
   - If no known pattern matches, this is a new failure mode
   - Document thoroughly for future reference
4. **Track accuracy:**
   - Record whether pattern-matched hypotheses were correct
   - Weight frequently correct patterns higher in future investigations

### Confidence Scoring

The agent should track and report its confidence using this framework:

| Confidence Level | Criteria                                                        | Action                          |
|------------------|-----------------------------------------------------------------|---------------------------------|
| **Confirmed**    | Complete data-supported causal chain, verified by correction    | Close and document              |
| **High (>80%)**  | Strong data support, consistent with known patterns             | Recommend corrective action     |
| **Medium (50-80%)** | Partial data support, plausible but gaps exist               | Request additional data/review  |
| **Low (<50%)**   | Limited data, multiple competing hypotheses                     | Escalate to human SME           |
| **Inconclusive** | Insufficient data to determine root cause                       | Document findings, request instrumentation improvement |

---

## XML Configuration File Parsing

When the user provides an XML configuration file, extract and use the following:

### Device Hierarchy
```xml
<!-- Example structure — actual schema will vary -->
<System id="ARRAY-US-TX-042">
  <Rack id="RACK_03">
    <Module id="MOD_12">
      <Cell id="CELL_01" ... />
    </Module>
    <BMS id="BMS_RACK_03" monitors="RACK_03" />
  </Rack>
  <PCS id="PCS_01" connected_racks="RACK_01,RACK_02,RACK_03" />
  <HVAC id="HVAC_01" cooling_zones="RACK_01,RACK_02,RACK_03,RACK_04" />
</System>
```

### What to Extract:
- **Parent-child relationships:** Which modules belong to which racks
- **Shared resources:** Which devices share cooling, power buses, or communication networks
- **Protection boundaries:** Which devices are in the same protection zone
- **Communication topology:** How devices communicate (serial, Ethernet, CAN bus)

### Why This Matters:
A failure in a shared resource (e.g., a cooling loop serving 4 racks) can cause
correlated symptoms across all devices sharing that resource. The configuration file
helps the agent distinguish between:
- **Common cause:** One failure causing multiple symptoms (the cooling pump example)
- **Cascading failure:** One failure triggering another in sequence
- **Coincidental:** Independent failures that happened to occur in the same time window

---

## Agent Interaction Protocol

### How to Collaborate with the AWS Agent

The 8D RCA agent does not query Athena directly. It formulates the analytical questions
and query patterns, then delegates data retrieval to the AWS agent.

**Workflow:**
1. 8D agent determines what data is needed (based on current investigation phase)
2. 8D agent sends a structured data request to the AWS agent
3. AWS agent executes the Athena query and returns results
4. 8D agent analyzes the results and determines the next step
5. Repeat until root cause is identified or investigation is inconclusive

**Data Request Format:**
```json
{
  "request_type": "telemetry_query",
  "purpose": "D4 - Anomaly detection in ±15min window",
  "array_id": "ARRAY-US-TX-042",
  "time_range": {
    "start": "2025-02-14T14:17:17Z",
    "end": "2025-02-14T14:47:17Z"
  },
  "filters": {
    "device_ids": ["RACK_03", "HVAC_01"],
    "datapoint_pattern": "*"
  },
  "expected_output": "All telemetry data points for specified devices in time range"
}
```

### How to Interact with the Human Investigator

The agent should:
1. **Present findings clearly** — Use the correlated event timeline format
2. **Ask targeted questions** — When data alone is insufficient, ask specific questions:
   - "Was there any maintenance activity on HVAC_01 on this date?"
   - "Has the coolant been topped off recently?"
   - "Were there any weather events (extreme heat) at this site?"
3. **Provide options, not just answers** — When confidence is medium or low, present
   the top 2-3 hypotheses with supporting evidence for each
4. **Never guess** — If the data doesn't support a conclusion, say so clearly

---

## Critical Rules

1. **Safety first.** If the data suggests an ongoing safety risk (thermal runaway, electrical fault,
   structural concern), flag it immediately before continuing the investigation.
2. **Data speaks.** Never assume a root cause without data support. Correlation is not causation —
   validate the causal chain against physical principles.
3. **Timestamp precision matters.** Always use UTC. Align timestamps across data sources.
   Account for clock skew between devices if detected.
4. **Start wide, narrow down.** Begin with all data in the time window, then systematically
   eliminate data points that are within normal range.
5. **Document everything.** Every query, every finding, every hypothesis — document it.
   The investigation record is as valuable as the conclusion.
6. **Know your limits.** The agent should clearly state when human expertise is needed.
   Physical inspection, electrochemical analysis, and power electronics diagnostics
   require domain experts.
7. **No source code.** This agent analyzes operational data only. If the root cause appears
   to be a software/firmware issue, document the evidence and escalate to the development team.
8. **Respect the process.** Do not skip steps. Even if the root cause seems obvious from D2,
   complete the full 8D to ensure nothing is missed and the investigation is defensible.

