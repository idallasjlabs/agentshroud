---
type: community
cohesion: 0.07
members: 57
---

# Module Group 68

**Cohesion:** 0.07 - loosely connected
**Members:** 57 nodes

## Members
- [[.__init__()_146]] - code - gateway/tools/port_manager.py
- [[.find_available_port()]] - code - gateway/tools/port_manager.py
- [[.generate_compose_ports()]] - code - gateway/tools/port_manager.py
- [[.has_conflicts()]] - code - gateway/tools/port_manager.py
- [[.is_port_available()]] - code - gateway/tools/port_manager.py
- [[.is_port_available_udp()]] - code - gateway/tools/port_manager.py
- [[.ports()]] - code - gateway/tools/port_manager.py
- [[.resolve_ports()]] - code - gateway/tools/port_manager.py
- [[.summary()]] - code - gateway/tools/port_manager.py
- [[.test_all_free_no_conflicts()]] - code - gateway/tests/test_port_manager.py
- [[.test_basic_mapping()]] - code - gateway/tests/test_port_manager.py
- [[.test_bound_port_is_not_available()]] - code - gateway/tests/test_port_manager.py
- [[.test_conflict_auto_resolved()]] - code - gateway/tests/test_port_manager.py
- [[.test_conflict_no_auto_resolve()]] - code - gateway/tests/test_port_manager.py
- [[.test_duplicate_port_detection()]] - code - gateway/tests/test_port_manager.py
- [[.test_finds_base_when_free()]] - code - gateway/tests/test_port_manager.py
- [[.test_has_conflicts()]] - code - gateway/tests/test_port_manager.py
- [[.test_no_conflict_mapping()]] - code - gateway/tests/test_port_manager.py
- [[.test_offset_applied()]] - code - gateway/tests/test_port_manager.py
- [[.test_ports_property()]] - code - gateway/tests/test_port_manager.py
- [[.test_raises_if_no_port_found()]] - code - gateway/tests/test_port_manager.py
- [[.test_skips_bound_port()]] - code - gateway/tests/test_port_manager.py
- [[.test_skips_excluded_ports()]] - code - gateway/tests/test_port_manager.py
- [[.test_summary_format()]] - code - gateway/tests/test_port_manager.py
- [[.test_udp_bound_not_available()]] - code - gateway/tests/test_port_manager.py
- [[.test_udp_unbound_available()]] - code - gateway/tests/test_port_manager.py
- [[.test_unbound_port_is_available()]] - code - gateway/tests/test_port_manager.py
- [[Busy port should be detected via connect_ex check.]] - rationale - gateway/tests/test_port_manager.py
- [[Check if a TCP port is available for binding.          Tries to bind briefly. Re]] - rationale - gateway/tools/port_manager.py
- [[Check if a UDP port is available (used for DNS).]] - rationale - gateway/tools/port_manager.py
- [[Detect port conflicts and auto-assign available ports.]] - rationale - gateway/tools/port_manager.py
- [[Find next available port starting from base.          Args             base St]] - rationale - gateway/tools/port_manager.py
- [[Generate docker-compose port mapping strings from resolution.          Returns d]] - rationale - gateway/tools/port_manager.py
- [[Get the final port mapping.]] - rationale - gateway/tools/port_manager.py
- [[If all ports in range are excluded, raises RuntimeError.]] - rationale - gateway/tests/test_port_manager.py
- [[PortAssignment]] - code - gateway/tools/port_manager.py
- [[PortManager]] - code - gateway/tools/port_manager.py
- [[PortResolution]] - code - gateway/tools/port_manager.py
- [[Quick check are the default ports available Log and return result.]] - rationale - gateway/tools/port_manager.py
- [[Record of a port assignment decision.]] - rationale - gateway/tools/port_manager.py
- [[Resolve all ports, detecting conflicts and auto-assigning if needed.          Ar]] - rationale - gateway/tools/port_manager.py
- [[Result of resolving all ports for an instance.]] - rationale - gateway/tools/port_manager.py
- [[Test PortResolution dataclass.]] - rationale - gateway/tests/test_port_manager.py
- [[Test auto-port discovery.]] - rationale - gateway/tests/test_port_manager.py
- [[Test docker-compose port mapping generation.]] - rationale - gateway/tests/test_port_manager.py
- [[Test full port resolution logic.]] - rationale - gateway/tests/test_port_manager.py
- [[Test port availability detection.]] - rationale - gateway/tests/test_port_manager.py
- [[TestFindAvailablePort]] - code - gateway/tests/test_port_manager.py
- [[TestGenerateComposePorts]] - code - gateway/tests/test_port_manager.py
- [[TestIsPortAvailable]] - code - gateway/tests/test_port_manager.py
- [[TestPortResolution]] - code - gateway/tests/test_port_manager.py
- [[TestResolveports]] - code - gateway/tests/test_port_manager.py
- [[Two services requesting same port — second gets reassigned.]] - rationale - gateway/tests/test_port_manager.py
- [[_fake_socket_factory()]] - code - gateway/tests/test_port_manager.py
- [[check_and_report()]] - code - gateway/tools/port_manager.py
- [[port_manager.py]] - code - gateway/tools/port_manager.py
- [[test_port_manager.py]] - code - gateway/tests/test_port_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_68
SORT file.name ASC
```
