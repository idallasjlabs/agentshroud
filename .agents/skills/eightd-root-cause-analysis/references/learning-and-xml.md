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
