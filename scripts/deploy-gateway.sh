#!/bin/bash
# AgentShroud Gateway Deployment Script
# Run this script to deploy the gateway with web dashboard

set -e

echo 🚀 Deploying AgentShroud Gateway...

# Navigate to docker directory
cd ~/Development/oneclaw/docker

# Build the gateway service
echo 📦 Building gateway container...
docker compose build gateway

# Deploy the gateway service
echo 🚢 Starting gateway service...
docker compose up -d gateway

echo ✅ Gateway deployed successfully!
echo 
echo 📊 Status:
docker compose ps gateway

echo 
echo 🌐 Access the web dashboard at:
echo  http://marvin.tail240ea8.ts.net:8080/
echo 
echo 📋 To check logs:
echo  cd /home/node/Development/oneclaw/docker