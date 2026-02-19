# ADR-006: Multi-Runtime Support (Docker/Podman/Apple Containers)

## Status
**Accepted** - December 2025

## Context

AgentShroud must support diverse container runtime environments across different operating systems and security requirements.

## Decision

Implement **Multi-Runtime Container Support** with runtime detection and adaptation:

### Supported Runtimes
- **Docker**: Standard deployment on Linux/Windows/macOS
- **Podman**: Rootless containers for enhanced security
- **Apple Containers**: Native macOS containerization with Keychain integration

### Runtime Abstraction Layer
```python
class ContainerRuntime:
    @abstractmethod
    def create_network(self, name: str, config: NetworkConfig) -> Network
    
    @abstractmethod
    def deploy_service(self, spec: ServiceSpec) -> Service
    
    @abstractmethod
    def get_runtime_info(self) -> RuntimeInfo
```

## Consequences

### Positive Consequences
- **Platform Flexibility**: Deploy on any supported container runtime
- **Security Options**: Choose runtime based on security requirements (rootless Podman)
- **Native Integration**: Leverage platform-specific features (macOS Keychain)

### Negative Consequences
- **Implementation Complexity**: Must handle runtime-specific differences
- **Testing Matrix**: Requires testing across all supported runtimes
- **Feature Parity**: Some features may not be available on all runtimes

### Mitigation
- Runtime detection and capability discovery
- Feature flags for runtime-specific functionality
- Comprehensive CI/CD testing across all platforms