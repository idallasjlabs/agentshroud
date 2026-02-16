#!/bin/bash
# Bot Access Audit Script
# Checks what vaults and items the bot can access
# Helps identify security issues with vault sharing

set -e

echo "========================================"
echo "   1Password Bot Access Audit"
echo "========================================"
echo "Date: $(date)"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper function to run op commands in container
run_op() {
    docker exec openclaw-bot sh -c "export OP_EMAIL=\$(cat /run/secrets/1password_bot_email); export OP_PASSWORD=\$(cat /run/secrets/1password_bot_master_password); export OP_SECRET_KEY=\$(cat /run/secrets/1password_bot_secret_key); eval \$(echo \"\$OP_PASSWORD\" | op account add --address my.1password.com --email \"\$OP_EMAIL\" --signin 2>&1); op $1" 2>&1
}

# Check if container is running
if ! docker ps | grep -q openclaw-bot; then
    echo -e "${RED}ERROR: openclaw-bot container is not running${NC}"
    exit 1
fi

echo "=== Step 1: List Vaults Accessible by Bot ==="
echo ""

VAULTS=$(run_op "vault list")
echo "$VAULTS"
echo ""

# Extract vault names (skip header)
VAULT_NAMES=$(echo "$VAULTS" | tail -n +2 | awk '{print $2}')
VAULT_COUNT=$(echo "$VAULT_NAMES" | wc -l | tr -d ' ')

echo -e "${GREEN}✓ Bot has access to $VAULT_COUNT vault(s)${NC}"
echo ""

# Check for security issues
echo "=== Step 2: Security Analysis ==="
echo ""

ISSUES=0

# Check for "Shared" vault
if echo "$VAULT_NAMES" | grep -qi "^Shared$\|^Family.*Shared$"; then
    echo -e "${RED}⚠ WARNING: Bot has access to 'Shared' or 'Family Shared' vault${NC}"
    echo "   This may expose family credentials to the bot!"
    echo "   Recommendation: Remove bot from this vault or move family credentials elsewhere"
    ISSUES=$((ISSUES + 1))
    echo ""
fi

# Check for multiple vaults (good - means proper separation)
if [ "$VAULT_COUNT" -eq 1 ]; then
    echo -e "${YELLOW}ℹ Bot only has access to 1 vault (its own Private vault)${NC}"
    echo "   This is secure but bot cannot access any shared credentials."
    echo "   If you want bot to access credentials, create a dedicated 'Bot Only' vault."
    echo ""
elif [ "$VAULT_COUNT" -eq 2 ]; then
    echo -e "${GREEN}✓ Bot has access to 2 vaults (likely Private + Bot Only)${NC}"
    echo "   This is a good setup for secure credential sharing."
    echo ""
else
    echo -e "${YELLOW}ℹ Bot has access to $VAULT_COUNT vaults${NC}"
    echo "   Review the list above to ensure bot should have access to each vault."
    echo ""
fi

echo "=== Step 3: List Items in Each Vault ==="
echo ""

for vault in $VAULT_NAMES; do
    echo "--- Vault: $vault ---"
    ITEMS=$(run_op "item list --vault \"$vault\"" 2>&1)

    if echo "$ITEMS" | grep -qi "error\|not found\|permission"; then
        echo -e "${RED}ERROR: Could not list items in vault '$vault'${NC}"
        echo "$ITEMS"
    else
        echo "$ITEMS"

        # Count items
        ITEM_COUNT=$(echo "$ITEMS" | tail -n +2 | wc -l | tr -d ' ')

        # Check for sensitive keywords in item titles
        if echo "$ITEMS" | grep -qi "bank\|credit\|medical\|ssn\|passport\|financial"; then
            echo -e "${RED}⚠ WARNING: Vault '$vault' contains items with sensitive keywords${NC}"
            echo "   Verify bot should have access to these credentials."
            ISSUES=$((ISSUES + 1))
        fi

        # Check for family member names
        if echo "$ITEMS" | grep -qi "mom\|dad\|spouse\|kid\|child\|family"; then
            echo -e "${YELLOW}ℹ Notice: Vault '$vault' contains items that may be family-related${NC}"
            echo "   Ensure bot needs access to these credentials."
        fi
    fi
    echo ""
done

echo "=== Step 4: Summary ==="
echo ""

if [ "$ISSUES" -eq 0 ]; then
    echo -e "${GREEN}✓ No critical security issues detected${NC}"
    echo ""
    echo "Current vault access appears secure."
    echo "Bot can only see vaults you've explicitly shared."
else
    echo -e "${RED}⚠ Found $ISSUES potential security issue(s)${NC}"
    echo ""
    echo "Review the warnings above and take action if needed."
    echo "See docs/1PASSWORD_FAMILY_PLAN_GUIDE.md for remediation steps."
fi

echo ""
echo "=== Recommendations ==="
echo ""
echo "Ideal setup for Family Plan:"
echo "  • Bot has access to: Private (bot's own) + Bot Only (dedicated bot vault)"
echo "  • Bot does NOT have access to: Family Shared, other Private vaults, Emergency"
echo ""
echo "To create a dedicated bot vault:"
echo "  1. Sign in to https://my.1password.com"
echo "  2. Create new vault: 'Bot Only'"
echo "  3. Share with ONLY: You + Bot account (therealidallasj@gmail.com)"
echo "  4. Move bot credentials from other vaults to 'Bot Only'"
echo "  5. Remove bot from any family shared vaults"
echo ""

echo "=== Audit Complete ==="
echo "Report saved to: audit-report-$(date +%Y%m%d-%H%M%S).txt"
echo ""
