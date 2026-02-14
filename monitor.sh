#!/bin/bash

###############################################################################
# Health Monitoring Script
# Project: One Claw Tied Behind Your Back
#
# Monitors OpenClaw services and alerts on failures
# Add to crontab: */5 * * * * ~/.oneclaw-secure/monitor.sh
###############################################################################

INSTALL_DIR="$HOME/.oneclaw-secure"
LOG_FILE="$INSTALL_DIR/logs/monitor.log"
ALERT_THRESHOLD=3  # Number of failures before alerting

# Create log directory if it doesn't exist
mkdir -p "$INSTALL_DIR/logs"

# Function: Log message
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Function: Send alert
send_alert() {
    local message="$1"

    # Log the alert
    log_message "ALERT: $message"

    # Display macOS notification
    osascript -e "display notification \"$message\" with title \"OpenClaw Alert\" sound name \"Basso\""

    # Optional: Send Telegram message (if configured)
    # Uncomment and configure if you want alerts via Telegram
    # TELEGRAM_BOT_TOKEN="your_bot_token"
    # TELEGRAM_CHAT_ID="your_chat_id"
    # curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage" \
    #   -d "chat_id=$TELEGRAM_CHAT_ID" \
    #   -d "text=🚨 OpenClaw Alert: $message" > /dev/null
}

# Function: Check container status
check_container() {
    if docker ps --filter "name=oneclaw_gateway" --format "{{.Status}}" | grep -q "Up"; then
        return 0
    else
        return 1
    fi
}

# Function: Check gateway health
check_gateway() {
    if curl -s --connect-timeout 5 http://localhost:18789/health > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function: Check bridge health
check_bridge() {
    if curl -s --connect-timeout 5 http://localhost:8765/health > /dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function: Check resource usage
check_resources() {
    # Get container stats
    local stats=$(docker stats oneclaw_gateway --no-stream --format "{{.CPUPerc}} {{.MemUsage}}" 2>/dev/null)

    if [[ -z "$stats" ]]; then
        return 1
    fi

    local cpu=$(echo "$stats" | awk '{print $1}' | tr -d '%')
    local mem=$(echo "$stats" | awk '{print $2}' | tr -d 'MiB')

    # Alert if CPU > 90% or Memory > 3.5GB
    if (( $(echo "$cpu > 90" | bc -l) )); then
        send_alert "High CPU usage: ${cpu}%"
    fi

    if (( $(echo "$mem > 3584" | bc -l) )); then
        send_alert "High memory usage: ${mem}MiB"
    fi

    return 0
}

# Function: Get failure count
get_failure_count() {
    local count_file="$INSTALL_DIR/logs/.failure_count"
    if [[ -f "$count_file" ]]; then
        cat "$count_file"
    else
        echo "0"
    fi
}

# Function: Set failure count
set_failure_count() {
    local count="$1"
    echo "$count" > "$INSTALL_DIR/logs/.failure_count"
}

# Function: Auto-restart if needed
auto_restart() {
    local component="$1"

    log_message "Attempting to restart $component..."

    if [[ "$component" == "container" ]]; then
        cd "$INSTALL_DIR"
        ./stop.sh >> "$LOG_FILE" 2>&1
        sleep 5
        ./start.sh >> "$LOG_FILE" 2>&1

        if check_container && check_gateway; then
            log_message "Successfully restarted container"
            send_alert "Container was down and has been restarted"
            set_failure_count 0
        else
            log_message "Failed to restart container"
            send_alert "Container restart failed - manual intervention required"
        fi
    elif [[ "$component" == "bridge" ]]; then
        launchctl unload ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist 2>> "$LOG_FILE"
        sleep 2
        launchctl load ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist 2>> "$LOG_FILE"

        if check_bridge; then
            log_message "Successfully restarted bridge"
            send_alert "Bridge was down and has been restarted"
            set_failure_count 0
        else
            log_message "Failed to restart bridge"
            send_alert "Bridge restart failed - manual intervention required"
        fi
    fi
}

# Main monitoring logic
main() {
    local failures=0

    # Check container status
    if ! check_container; then
        log_message "Container is not running"
        failures=$((failures + 1))

        # Increment failure count
        local count=$(get_failure_count)
        count=$((count + 1))
        set_failure_count "$count"

        # Auto-restart if threshold reached
        if [[ $count -ge $ALERT_THRESHOLD ]]; then
            auto_restart "container"
        fi
    fi

    # Check gateway health
    if check_container; then
        if ! check_gateway; then
            log_message "Gateway health check failed"
            failures=$((failures + 1))

            local count=$(get_failure_count)
            count=$((count + 1))
            set_failure_count "$count"

            if [[ $count -ge $ALERT_THRESHOLD ]]; then
                auto_restart "container"
            fi
        else
            # Gateway is healthy, reset failure count
            set_failure_count 0
        fi
    fi

    # Check bridge health
    if ! check_bridge; then
        log_message "Bridge health check failed"
        # Bridge failures don't count toward main threshold
        # but we still alert
        send_alert "macOS bridge is not responding"
        auto_restart "bridge"
    fi

    # Check resource usage (only if container is running)
    if check_container; then
        check_resources
    fi

    # Log success if no failures
    if [[ $failures -eq 0 ]]; then
        log_message "All checks passed"
    fi
}

# Run main function
main
