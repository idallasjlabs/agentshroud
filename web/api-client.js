/**
 * AgentShroud API Client
 * Handles all API communication, WebSocket connections, and shared functionality
 */

class AgentShroudAPI {
  constructor(options = {}) {
    this.baseURL = options.baseURL || 'http://localhost:8080';
    this.wsURL = options.wsURL || 'ws://localhost:8081/ws';
    this.timeout = options.timeout || 10000;
    this.ws = null;
    this.wsReconnectAttempts = 0;
    this.wsMaxReconnectAttempts = 5;
    this.wsReconnectDelay = 1000;
    this.eventListeners = new Map();
    
    // Bind methods to maintain context
    this.handleWSOpen = this.handleWSOpen.bind(this);
    this.handleWSMessage = this.handleWSMessage.bind(this);
    this.handleWSClose = this.handleWSClose.bind(this);
    this.handleWSError = this.handleWSError.bind(this);
  }

  /**
   * Generic fetch wrapper with error handling
   */
  async fetch(endpoint, options = {}) {
    const url = `${this.baseURL}${endpoint}`;
    const config = {
      timeout: this.timeout,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    };

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), this.timeout);
      
      const response = await fetch(url, {
        ...config,
        signal: controller.signal
      });
      
      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const contentType = response.headers.get('content-type');
      if (contentType && contentType.includes('application/json')) {
        return await response.json();
      }
      
      return await response.text();
    } catch (error) {
      if (error.name === 'AbortError') {
        throw new Error('Request timeout');
      }
      throw error;
    }
  }

  /**
   * Health check endpoint
   */
  async checkHealth() {
    try {
      const data = await this.fetch('/health');
      return {
        healthy: true,
        status: data.status || 'ok',
        timestamp: data.timestamp || new Date().toISOString(),
        components: data.components || {},
        uptime: data.uptime || 0
      };
    } catch (error) {
      return {
        healthy: false,
        error: error.message,
        timestamp: new Date().toISOString()
      };
    }
  }

  /**
   * Get system status
   */
  async getSystemStatus() {
    return this.fetch('/api/system/status');
  }

  /**
   * Get security modules status
   */
  async getSecurityModules() {
    return this.fetch('/api/security/modules');
  }

  /**
   * Toggle security module status
   */
  async toggleSecurityModule(moduleId, enabled) {
    return this.fetch(`/api/security/modules/${moduleId}`, {
      method: 'PUT',
      body: JSON.stringify({ enabled })
    });
  }

  /**
   * Get audit trail
   */
  async getAuditTrail(options = {}) {
    const params = new URLSearchParams();
    if (options.limit) params.append('limit', options.limit);
    if (options.offset) params.append('offset', options.offset);
    if (options.search) params.append('search', options.search);
    if (options.severity) params.append('severity', options.severity);
    
    const query = params.toString() ? `?${params.toString()}` : '';
    return this.fetch(`/api/audit/trail${query}`);
  }

  /**
   * Get agent trust levels
   */
  async getAgentTrustLevels() {
    return this.fetch('/api/agents/trust-levels');
  }

  /**
   * Get kill switch status
   */
  async getKillSwitchStatus() {
    return this.fetch('/api/kill-switch/status');
  }

  /**
   * Trigger kill switch
   */
  async triggerKillSwitch(confirmation = false) {
    return this.fetch('/api/kill-switch/trigger', {
      method: 'POST',
      body: JSON.stringify({ confirmed: confirmation })
    });
  }

  /**
   * Reset kill switch
   */
  async resetKillSwitch() {
    return this.fetch('/api/kill-switch/reset', {
      method: 'POST'
    });
  }

  /**
   * Get resource usage
   */
  async getResourceUsage() {
    return this.fetch('/api/system/resources');
  }

  /**
   * Get port configuration
   */
  async getPortConfiguration() {
    return this.fetch('/api/system/ports');
  }

  /**
   * Restart gateway
   */
  async restartGateway() {
    return this.fetch('/api/system/restart', {
      method: 'POST'
    });
  }

  /**
   * Run Trivy security scan
   */
  async runTrivyScan() {
    return this.fetch('/api/security/trivy-scan', {
      method: 'POST'
    });
  }

  /**
   * Get logs
   */
  async getLogs(component = 'gateway', lines = 100) {
    return this.fetch(`/api/system/logs/${component}?lines=${lines}`);
  }

  /**
   * Detect available container runtime
   */
  async detectRuntime() {
    try {
      const runtimes = [];
      
      // Check for Docker
      try {
        await this.runCommand('docker --version');
        runtimes.push({ 
          name: 'Docker', 
          command: 'docker', 
          detected: true,
          preferred: true 
        });
      } catch (e) {
        runtimes.push({ 
          name: 'Docker', 
          command: 'docker', 
          detected: false 
        });
      }

      // Check for Podman
      try {
        await this.runCommand('podman --version');
        runtimes.push({ 
          name: 'Podman', 
          command: 'podman', 
          detected: true 
        });
      } catch (e) {
        runtimes.push({ 
          name: 'Podman', 
          command: 'podman', 
          detected: false 
        });
      }

      // Check for Apple Containers (if on macOS)
      if (navigator.platform.includes('Mac')) {
        runtimes.push({ 
          name: 'Apple Containers', 
          command: 'docker', 
          detected: false,
          note: 'Requires Docker Desktop with Apple virtualization' 
        });
      }

      return runtimes;
    } catch (error) {
      console.error('Runtime detection failed:', error);
      return [];
    }
  }

  /**
   * Run a command (for setup wizard)
   */
  async runCommand(command) {
    return this.fetch('/api/system/exec', {
      method: 'POST',
      body: JSON.stringify({ command })
    });
  }

  /**
   * Generate docker-compose configuration
   */
  generateDockerCompose(config) {
    const {
      runtime = 'docker',
      securityMode = 'proxy',
      gatewayPort = 8080,
      wsPort = 8081,
      secretsMethod = '1password',
      onePasswordToken = '',
      customSecrets = {}
    } = config;

    let compose = `version: '3.8'
services:
  agentshroud-gateway:
    image: agentshroud/gateway:latest
    container_name: agentshroud-gateway
    restart: unless-stopped
    ports:
      - "${gatewayPort}:8080"
      - "${wsPort}:8081"
    environment:
      - SECURITY_MODE=${securityMode}
      - LOG_LEVEL=info
`;

    if (secretsMethod === '1password' && onePasswordToken) {
      compose += `      - OP_SERVICE_ACCOUNT_TOKEN=${onePasswordToken}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
`;
    } else if (secretsMethod === 'manual' && Object.keys(customSecrets).length > 0) {
      compose += `    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
`;
      Object.entries(customSecrets).forEach(([key, path]) => {
        compose += `      - ${path}:/run/secrets/${key}:ro
`;
      });
    }

    compose += `
  agentshroud-monitor:
    image: agentshroud/monitor:latest
    container_name: agentshroud-monitor
    restart: unless-stopped
    depends_on:
      - agentshroud-gateway
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - GATEWAY_URL=http://agentshroud-gateway:8080
`;

    if (securityMode === 'sidecar') {
      compose += `
  agentshroud-proxy:
    image: agentshroud/proxy:latest
    container_name: agentshroud-proxy
    restart: unless-stopped
    ports:
      - "3128:3128"
    depends_on:
      - agentshroud-gateway
    environment:
      - GATEWAY_URL=http://agentshroud-gateway:8080
`;
    }

    return compose;
  }

  /**
   * WebSocket connection management
   */
  connectWebSocket() {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      return Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      try {
        this.ws = new WebSocket(this.wsURL);
        this.ws.onopen = (event) => {
          this.handleWSOpen(event);
          resolve();
        };
        this.ws.onmessage = this.handleWSMessage;
        this.ws.onclose = this.handleWSClose;
        this.ws.onerror = (error) => {
          this.handleWSError(error);
          reject(error);
        };
      } catch (error) {
        reject(error);
      }
    });
  }

  disconnectWebSocket() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }

  handleWSOpen(event) {
    console.log('WebSocket connected');
    this.wsReconnectAttempts = 0;
    this.emit('ws:connected', event);
  }

  handleWSMessage(event) {
    try {
      const data = JSON.parse(event.data);
      this.emit('ws:message', data);
      
      // Emit specific event types
      if (data.type) {
        this.emit(`ws:${data.type}`, data);
      }
    } catch (error) {
      console.error('Failed to parse WebSocket message:', error);
    }
  }

  handleWSClose(event) {
    console.log('WebSocket disconnected');
    this.emit('ws:disconnected', event);
    
    // Attempt reconnection if not a clean close
    if (!event.wasClean && this.wsReconnectAttempts < this.wsMaxReconnectAttempts) {
      this.wsReconnectAttempts++;
      console.log(`Attempting WebSocket reconnection ${this.wsReconnectAttempts}/${this.wsMaxReconnectAttempts}`);
      
      setTimeout(() => {
        this.connectWebSocket().catch(error => {
          console.error('WebSocket reconnection failed:', error);
        });
      }, this.wsReconnectDelay * this.wsReconnectAttempts);
    }
  }

  handleWSError(error) {
    console.error('WebSocket error:', error);
    this.emit('ws:error', error);
  }

  /**
   * Send message through WebSocket
   */
  sendWebSocketMessage(message) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(message));
    } else {
      console.warn('WebSocket not connected, cannot send message');
    }
  }

  /**
   * Event emitter functionality
   */
  on(event, callback) {
    if (!this.eventListeners.has(event)) {
      this.eventListeners.set(event, []);
    }
    this.eventListeners.get(event).push(callback);
  }

  off(event, callback) {
    if (this.eventListeners.has(event)) {
      const listeners = this.eventListeners.get(event);
      const index = listeners.indexOf(callback);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    }
  }

  emit(event, data) {
    if (this.eventListeners.has(event)) {
      this.eventListeners.get(event).forEach(callback => {
        try {
          callback(data);
        } catch (error) {
          console.error(`Error in event listener for ${event}:`, error);
        }
      });
    }
  }

  /**
   * Utility functions
   */
  formatBytes(bytes) {
    if (bytes === 0) return '0 B';
    const k = 1024;
    const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  formatUptime(seconds) {
    const days = Math.floor(seconds / 86400);
    const hours = Math.floor((seconds % 86400) / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    
    if (days > 0) {
      return `${days}d ${hours}h ${minutes}m`;
    } else if (hours > 0) {
      return `${hours}h ${minutes}m`;
    } else {
      return `${minutes}m`;
    }
  }

  formatTimestamp(timestamp) {
    return new Date(timestamp).toLocaleString();
  }

  /**
   * Polling utility for periodic updates
   */
  startPolling(callback, interval = 30000) {
    const poll = async () => {
      try {
        await callback();
      } catch (error) {
        console.error('Polling error:', error);
      }
    };

    // Initial call
    poll();
    
    // Set up interval
    const intervalId = setInterval(poll, interval);
    
    return () => clearInterval(intervalId);
  }
}

// Utility functions for form handling and UI updates
const UIUtils = {
  /**
   * Show loading spinner on button
   */
  showButtonLoading(button, text = 'Loading...') {
    const originalText = button.innerHTML;
    button.disabled = true;
    button.innerHTML = `<span class="loading-spinner"></span> ${text}`;
    
    return () => {
      button.disabled = false;
      button.innerHTML = originalText;
    };
  },

  /**
   * Show toast notification
   */
  showToast(message, type = 'info', duration = 5000) {
    // Create toast container if it doesn't exist
    let container = document.querySelector('.toast-container');
    if (!container) {
      container = document.createElement('div');
      container.className = 'toast-container';
      container.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        max-width: 350px;
      `;
      document.body.appendChild(container);
    }

    // Create toast element
    const toast = document.createElement('div');
    toast.className = `alert alert-${type}`;
    toast.style.cssText = `
      margin-bottom: 10px;
      box-shadow: var(--shadow-lg);
      cursor: pointer;
      animation: slideIn 0.3s ease-out;
    `;
    toast.innerHTML = message;

    // Add close functionality
    toast.addEventListener('click', () => {
      toast.style.animation = 'slideOut 0.3s ease-in forwards';
      setTimeout(() => toast.remove(), 300);
    });

    container.appendChild(toast);

    // Auto remove after duration
    if (duration > 0) {
      setTimeout(() => {
        if (toast.parentNode) {
          toast.style.animation = 'slideOut 0.3s ease-in forwards';
          setTimeout(() => toast.remove(), 300);
        }
      }, duration);
    }

    // Add animations to document head if not already added
    if (!document.querySelector('#toast-animations')) {
      const style = document.createElement('style');
      style.id = 'toast-animations';
      style.textContent = `
        @keyframes slideIn {
          from { transform: translateX(100%); opacity: 0; }
          to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideOut {
          from { transform: translateX(0); opacity: 1; }
          to { transform: translateX(100%); opacity: 0; }
        }
      `;
      document.head.appendChild(style);
    }
  },

  /**
   * Update progress bar
   */
  updateProgress(selector, percentage) {
    const progressBar = document.querySelector(`${selector} .progress-fill`);
    if (progressBar) {
      progressBar.style.width = `${Math.max(0, Math.min(100, percentage))}%`;
    }
  },

  /**
   * Validate form inputs
   */
  validateForm(formSelector) {
    const form = document.querySelector(formSelector);
    if (!form) return false;

    let isValid = true;
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');

    inputs.forEach(input => {
      const group = input.closest('.form-group');
      let errorElement = group.querySelector('.form-error');

      // Remove existing error
      if (errorElement) {
        errorElement.remove();
      }

      // Validate input
      if (!input.value.trim()) {
        isValid = false;
        input.style.borderColor = 'var(--danger)';
        
        // Add error message
        errorElement = document.createElement('div');
        errorElement.className = 'form-error';
        errorElement.style.color = 'var(--danger)';
        errorElement.style.fontSize = '0.8rem';
        errorElement.style.marginTop = '0.25rem';
        errorElement.textContent = 'This field is required';
        group.appendChild(errorElement);
      } else {
        input.style.borderColor = '';
      }
    });

    return isValid;
  }
};

// Export for use in other files
if (typeof window !== 'undefined') {
  window.AgentShroudAPI = AgentShroudAPI;
  window.UIUtils = UIUtils;
}