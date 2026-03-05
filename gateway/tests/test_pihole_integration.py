# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.

import pytest


class TestPiholeIntegration:
    """Test Pi-hole DNS management integration."""

    def test_pihole_password_file_exists(self):
        """Test that Pi-hole password file was created."""
        import os
        password_file = "docker/secrets/pihole_password.txt"
        assert os.path.exists(password_file), "Pi-hole password file should exist"
        
        with open(password_file, 'r') as f:
            password = f.read().strip()
            assert len(password) > 0, "Password should not be empty"
            assert len(password) == 32, "Password should be 32 characters (hex)"

    def test_pihole_setup_script_exists(self):
        """Test that Pi-hole setup script was created and is executable."""
        import os
        script_file = "docker/scripts/pihole-setup-blocklists.sh"
        assert os.path.exists(script_file), "Pi-hole setup script should exist"
        assert os.access(script_file, os.X_OK), "Script should be executable"

    def test_docker_compose_has_pihole_service(self):
        """Test that docker-compose.yml contains Pi-hole service."""
        import yaml
        
        with open('docker/docker-compose.yml', 'r') as f:
            compose_data = yaml.safe_load(f)
        
        assert 'pihole' in compose_data['services'], "Pi-hole service should be in compose file"
        
        pihole_service = compose_data['services']['pihole']
        assert pihole_service['image'].startswith('pihole/pihole'), 'Pi-hole image should be pihole/pihole (pinned or tagged)'
        assert pihole_service['container_name'] == 'agentshroud-pihole'
        assert pihole_service['hostname'] == 'pihole'
        
        # Check environment variables (list format: KEY=VALUE)
        env = pihole_service['environment']
        env_dict = {}
        for item in env:
            if '=' in item:
                k, v = item.split('=', 1)
                env_dict[k] = v
        assert 'WEBPASSWORD_FILE' in env_dict
        assert env_dict['PIHOLE_DNS_'] == '8.8.8.8;8.8.4.4'
        assert env_dict['DNSMASQ_LISTENING'] == 'all'
        
        # Check volumes
        volumes = pihole_service['volumes']
        assert 'pihole-etc:/etc/pihole' in volumes
        assert 'pihole-dnsmasq:/etc/dnsmasq.d' in volumes
        
        # Enforcement hardening: pihole runs on isolated network without exposed ports
        # Admin access is via gateway proxy only

    def test_services_use_pihole_dns(self):
        """Test that gateway and agentshroud services use Pi-hole DNS."""
        import yaml
        
        with open('docker/docker-compose.yml', 'r') as f:
            compose_data = yaml.safe_load(f)
        
        # Check gateway service uses Pi-hole DNS
        gateway_service = compose_data['services']['gateway']
        assert 'dns' in gateway_service, "Gateway should have DNS configuration"
        assert gateway_service['dns'] == ['172.21.0.10'], "Gateway should use Pi-hole DNS"

        # Check agentshroud service depends on pihole
        agentshroud_service = compose_data['services']['agentshroud']
        assert 'depends_on' in agentshroud_service, "AgentShroud should depend on services"
        deps = agentshroud_service['depends_on']
        assert 'pihole' in deps, "AgentShroud should depend on Pi-hole"

    def test_pihole_secrets_and_volumes_configured(self):
        """Test that Pi-hole secrets and volumes are configured in compose file."""
        import yaml
        
        with open('docker/docker-compose.yml', 'r') as f:
            compose_data = yaml.safe_load(f)
        
        # Check secrets
        secrets = compose_data['secrets']
        assert 'pihole_password' in secrets, "Pi-hole password secret should be configured"
        assert secrets['pihole_password']['file'] == './secrets/pihole_password.txt'
        
        # Check volumes
        volumes = compose_data['volumes']
        assert 'pihole-etc' in volumes, "Pi-hole config volume should be configured"
        assert 'pihole-dnsmasq' in volumes, "Pi-hole dnsmasq volume should be configured"

    def test_host_specific_compose_files_updated(self):
        """Test that host-specific compose files have Pi-hole port overrides."""
        # Test marvin-prod.yml
        with open('docker/docker-compose.marvin-prod.yml', 'r') as f:
            prod_content = f.read()
        
        assert 'pihole:' in prod_content, "Prod compose should have Pi-hole overrides"
        assert '127.0.0.1:6353:53/tcp' in prod_content, "Prod should use port 6353 for TCP DNS"
        assert '127.0.0.1:6353:53/udp' in prod_content, "Prod should use port 6353 for UDP DNS"
        assert '127.0.0.1:6380:80/tcp' in prod_content, "Prod should use port 6380 for web interface"
        
        # Test marvin-test.yml
        with open('docker/docker-compose.marvin-test.yml', 'r') as f:
            test_content = f.read()
        
        assert 'pihole:' in test_content, "Test compose should have Pi-hole overrides"
        assert '127.0.0.1:6353:53/tcp' in test_content, "Test should use port 6353 for TCP DNS"
        assert '127.0.0.1:6353:53/udp' in test_content, "Test should use port 6353 for UDP DNS"
        assert '127.0.0.1:6380:80/tcp' in test_content, "Test should use port 6380 for web interface"

    def test_dns_management_endpoints_exist(self):
        """Test that DNS management endpoints exist in main.py."""
        with open('gateway/ingest_api/main.py', 'r') as f:
            main_content = f.read()
        
        # Check that DNS endpoints are defined
        assert '@app.get("/manage/dns")' in main_content, "DNS stats endpoint should exist"
        assert '@app.post("/manage/dns/blocklist")' in main_content, "Blocklist management endpoint should exist"
        
        # Check function names
        assert 'async def get_dns_stats(' in main_content, "DNS stats function should exist"
        assert 'async def manage_blocklist(' in main_content, "Blocklist management function should exist"
        
        # Check basic functionality
        assert 'http://pihole:80/admin/api.php' in main_content, "Should query Pi-hole API"
        assert 'aiohttp.ClientSession' in main_content, "Should use aiohttp for requests"
