#!/bin/bash

###############################################################################
# Account Setup Wizard for OpenClaw
# Project: One Claw Tied Behind Your Back
#
# This wizard guides you through creating service accounts for OpenClaw
# Username: therealidallasj
###############################################################################

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  OpenClaw Account Setup Wizard                             ║"
echo "║  Username: therealidallasj                                 ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "This wizard will guide you through creating service accounts for OpenClaw."
echo "All accounts will use the username: therealidallasj"
echo ""
echo "Note: Most steps require manual completion due to CAPTCHA, 2FA, and"
echo "phone verification. This wizard will open the necessary web pages and"
echo "guide you through each step."
echo ""

read -p "Press Enter to begin..."
echo ""

###############################################################################
# Step 1: Gmail/Google Account
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 1: Create Gmail / Google Account${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Email: therealidallasj@gmail.com"
echo ""
echo "Instructions:"
echo "1. A browser will open to the Google account signup page"
echo "2. Enter the following details:"
echo "   - First name: The Real"
echo "   - Last name: IDallasJ"
echo "   - Username: therealidallasj"
echo "   - Create a strong password (save in password manager)"
echo "3. Complete phone verification"
echo "4. Skip recovery email (optional)"
echo "5. Enable 2-Factor Authentication (Settings > Security)"
echo "   - Use authenticator app (Google Authenticator, Authy, 1Password, etc.)"
echo "6. Save backup codes in a secure location"
echo ""

read -p "Press Enter to open Google signup page..."
open "https://accounts.google.com/signup"
echo ""
read -p "Press Enter once account is created and 2FA is enabled..."
echo ""
echo -e "${GREEN}✓${NC} Gmail account created"
echo ""

###############################################################################
# Step 2: Apple ID
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 2: Create Apple ID${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Apple ID: therealidallasj@icloud.com"
echo ""
echo "Instructions:"
echo "1. A browser will open to the Apple ID creation page"
echo "2. Enter the following details:"
echo "   - Email: Create a new iCloud email"
echo "   - iCloud email: therealidallasj@icloud.com"
echo "   - Password: Create a strong password (different from Gmail)"
echo "3. Complete phone verification"
echo "4. Enable 2-Factor Authentication (required by Apple)"
echo "5. Sign into iCloud on this Mac:"
echo "   - System Settings > Apple ID"
echo "6. Sign into Messages.app:"
echo "   - Messages > Settings > Accounts"
echo "   - Enable iMessage"
echo ""

read -p "Press Enter to open Apple ID creation page..."
open "https://appleid.apple.com/account"
echo ""
read -p "Press Enter once Apple ID is created and signed in to Messages.app..."
echo ""
echo -e "${GREEN}✓${NC} Apple ID created and signed in"
echo ""

###############################################################################
# Step 3: Google Cloud Console (for Gmail/Calendar APIs)
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 3: Enable Google APIs${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Required for: Gmail, Google Calendar, Google Tasks integration"
echo ""
echo "Instructions:"
echo "1. Create a new Google Cloud Project:"
echo "   - Project name: openclaw-integration"
echo "2. Enable the following APIs:"
echo "   - Gmail API"
echo "   - Google Calendar API"
echo "   - Google Tasks API"
echo "   - Cloud Pub/Sub API (for Gmail push notifications)"
echo "3. Create OAuth 2.0 credentials:"
echo "   - Credentials > Create Credentials > OAuth client ID"
echo "   - Application type: Web application"
echo "   - Name: OpenClaw"
echo "   - Authorized redirect URIs:"
echo "     - http://localhost:18789/oauth/google/callback"
echo "     - http://localhost:3000/oauth/google/callback"
echo "4. Download the client_secret.json file"
echo "5. Note your Client ID and Client Secret"
echo ""

read -p "Press Enter to open Google Cloud Console..."
open "https://console.cloud.google.com/apis/dashboard"
echo ""
read -p "Press Enter once APIs are enabled and OAuth credentials are created..."
echo ""

echo "Please enter your Google OAuth credentials:"
read -p "Client ID: " GOOGLE_CLIENT_ID
read -p "Client Secret: " GOOGLE_CLIENT_SECRET
echo ""
echo -e "${GREEN}✓${NC} Google APIs enabled"
echo ""

###############################################################################
# Step 4: Telegram Bot
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 4: Create Telegram Bot${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Bot username: @therealidallasj"
echo ""
echo "Instructions:"
echo "1. Open Telegram on your phone or desktop"
echo "2. Search for @BotFather"
echo "3. Send: /newbot"
echo "4. Bot name: The Real IDallasJ Assistant"
echo "5. Bot username: therealidallasj (or therealidallasj_bot if taken)"
echo "6. Copy the bot token (starts with a number, contains a colon)"
echo "7. Send: /setdescription - Set bot description"
echo "8. Send: /setuserpic - Upload a profile picture (optional)"
echo ""

echo "Opening Telegram Web..."
open "https://web.telegram.org"
echo ""
read -p "Press Enter once bot is created..."
echo ""

read -p "Telegram Bot Token: " TELEGRAM_BOT_TOKEN
echo ""
echo -e "${GREEN}✓${NC} Telegram bot created"
echo ""

###############################################################################
# Step 5: PayPal Account
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 5: PayPal Account Setup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Email: therealidallasj@gmail.com"
echo ""
echo "Instructions:"
echo "1. Open PayPal signup page"
echo "2. Email: therealidallasj@gmail.com"
echo "3. Create password (different from Gmail)"
echo "4. Complete identity verification"
echo "5. Link a bank account or debit card"
echo "6. Add \$40 to PayPal balance"
echo "7. Set up spending limit (optional):"
echo "   - Wallet > Settings > Payment preferences"
echo "   - Set monthly spending limit to \$40"
echo ""
echo "Note: PayPal API integration is optional and requires additional setup"
echo "for automated purchases. For now, OpenClaw can use browser automation"
echo "with manual approval."
echo ""

read -p "Press Enter to open PayPal signup page..."
open "https://www.paypal.com/signup"
echo ""
read -p "Press Enter once PayPal account is created and funded..."
echo ""
echo -e "${GREEN}✓${NC} PayPal account created"
echo ""

###############################################################################
# Step 6: Optional Services
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 6: Optional Service Accounts${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "The following services are optional but recommended:"
echo ""

# Todoist
echo "Todoist (Task Management):"
echo "  Email: therealidallasj@gmail.com"
echo "  URL: https://todoist.com/auth/signup"
read -p "Create Todoist account? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "https://todoist.com/auth/signup"
    read -p "Press Enter once account is created..."
    echo -e "${GREEN}✓${NC} Todoist account created"
fi
echo ""

# Slack Workspace
echo "Slack Workspace (Alternative Chat Interface):"
echo "  Workspace name: therealidallasj-assistant"
echo "  Email: therealidallasj@gmail.com"
echo "  URL: https://slack.com/create"
read -p "Create Slack workspace? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "https://slack.com/create"
    read -p "Press Enter once workspace is created..."
    echo -e "${GREEN}✓${NC} Slack workspace created"
fi
echo ""

###############################################################################
# Step 7: Update .env file
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 7: Update Environment Variables${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

ENV_FILE="$HOME/.oneclaw-secure/secrets/.env"

if [[ -f "$ENV_FILE" ]]; then
    echo "Updating $ENV_FILE with your credentials..."
    echo ""

    # Update Google credentials
    if [[ -n "$GOOGLE_CLIENT_ID" ]]; then
        sed -i '' "s|GMAIL_CLIENT_ID=|GMAIL_CLIENT_ID=$GOOGLE_CLIENT_ID|" "$ENV_FILE"
        sed -i '' "s|GMAIL_CLIENT_SECRET=|GMAIL_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET|" "$ENV_FILE"
        sed -i '' "s|GOOGLE_CALENDAR_CLIENT_ID=|GOOGLE_CALENDAR_CLIENT_ID=$GOOGLE_CLIENT_ID|" "$ENV_FILE"
        sed -i '' "s|GOOGLE_CALENDAR_CLIENT_SECRET=|GOOGLE_CALENDAR_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET|" "$ENV_FILE"
        sed -i '' "s|GOOGLE_TASKS_CLIENT_ID=|GOOGLE_TASKS_CLIENT_ID=$GOOGLE_CLIENT_ID|" "$ENV_FILE"
        sed -i '' "s|GOOGLE_TASKS_CLIENT_SECRET=|GOOGLE_TASKS_CLIENT_SECRET=$GOOGLE_CLIENT_SECRET|" "$ENV_FILE"
    fi

    # Update Telegram token
    if [[ -n "$TELEGRAM_BOT_TOKEN" ]]; then
        sed -i '' "s|TELEGRAM_BOT_TOKEN=|TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN|" "$ENV_FILE"
    fi

    echo -e "${GREEN}✓${NC} Environment variables updated"
else
    echo -e "${YELLOW}⚠️${NC}  .env file not found at $ENV_FILE"
    echo "Please run the main deployment script first: ./deploy-openclaw.sh"
fi
echo ""

###############################################################################
# Summary
###############################################################################
echo -e "${GREEN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Account Setup Complete!                                   ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "Accounts created with username: therealidallasj"
echo ""
echo "✓ Gmail: therealidallasj@gmail.com"
echo "✓ Apple ID: therealidallasj@icloud.com"
echo "✓ Telegram: @therealidallasj"
echo "✓ PayPal: therealidallasj@gmail.com"
echo ""

echo -e "${YELLOW}IMPORTANT: Still required:${NC}"
echo ""
echo "1. Add your AI provider API key to:"
echo "   $ENV_FILE"
echo "   Required: ANTHROPIC_API_KEY or OPENAI_API_KEY"
echo ""
echo "2. Install and configure BlueBubbles for iMessage:"
echo "   brew install --cask bluebubbles"
echo "   - Enable Web API"
echo "   - Set password (matches BLUEBUBBLES_PASSWORD in .env)"
echo "   - Configure webhook URL: http://localhost:8765/bluebubbles-webhook"
echo ""
echo "3. Complete OpenClaw Gmail setup:"
echo "   After starting OpenClaw, run:"
echo "   openclaw webhooks gmail setup --account therealidallasj@gmail.com"
echo ""

echo "Next steps:"
echo "1. Start OpenClaw: cd ~/.oneclaw-secure && ./start.sh"
echo "2. Access WebChat UI: http://localhost:18790"
echo "3. Pair your personal accounts with OpenClaw via /pair command"
echo ""

echo "Documentation:"
echo "  https://docs.oneclaw.ai"
echo ""
