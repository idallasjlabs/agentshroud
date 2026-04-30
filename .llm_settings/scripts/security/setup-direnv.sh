#!/usr/bin/env bash
# setup-direnv.sh
# Configure direnv for secure environment variable management

set -e

echo "🔐 Setting up direnv for secure environment variables..."
echo ""

# Check if direnv is installed
if ! command -v direnv &> /dev/null; then
    echo "📦 Installing direnv..."
    if command -v brew &>/dev/null; then
        brew install direnv
    elif command -v apt-get &>/dev/null; then
        sudo apt-get install -y direnv
    elif command -v dnf &>/dev/null; then
        sudo dnf install -y direnv
    elif command -v yum &>/dev/null; then
        sudo yum install -y direnv
    elif command -v pacman &>/dev/null; then
        sudo pacman -S --noconfirm direnv
    else
        echo "❌ Error: No supported package manager found. Install direnv manually:"
        echo "   https://direnv.net/docs/installation.html"
        exit 1
    fi
fi

echo "✅ direnv installed"

# Detect shell
SHELL_RC=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
    HOOK_LINE='eval "$(direnv hook zsh)"'
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
    HOOK_LINE='eval "$(direnv hook bash)"'
else
    echo "⚠️  Unknown shell. Add direnv hook manually."
    exit 1
fi

# Check if already configured
if grep -q "direnv hook" "$SHELL_RC" 2>/dev/null; then
    echo "✅ direnv already configured in $SHELL_RC"
else
    echo "📝 Adding direnv hook to $SHELL_RC..."
    echo "" >> "$SHELL_RC"
    echo "# direnv hook for secure environment variables" >> "$SHELL_RC"
    echo "$HOOK_LINE" >> "$SHELL_RC"
    echo "✅ direnv hook added to $SHELL_RC"
fi

echo ""
echo "📄 Creating .envrc template..."

cat > .envrc.example << 'ENVRC'
# .envrc - Local environment variables (automatically loaded by direnv)
# This file should be committed to git as .envrc.example
# Copy to .envrc and customize for your local environment

# AWS Secrets Manager example
export DB_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id fluence/db/password \
  --query SecretString \
  --output text)

# AWS SSM Parameter Store example
export API_KEY=$(aws ssm get-parameter \
  --name /fluence/api-key \
  --with-decryption \
  --query Parameter.Value \
  --output text)

# Or use environment-specific profiles
export AWS_PROFILE=fluence-dev
export AWS_REGION=us-east-1

# PostgreSQL connection (uses ~/.pgpass for password)
export PGHOST=db.fluence.local
export PGPORT=5432
export PGDATABASE=operations
export PGUSER=fluence_app

# Application settings
export ENVIRONMENT=development
export LOG_LEVEL=INFO
ENVRC

echo "✅ Created .envrc.example"

# Add .envrc to .gitignore if not already there
if [ -f ".gitignore" ]; then
    if ! grep -q "^.envrc$" .gitignore; then
        echo ".envrc" >> .gitignore
        echo "✅ Added .envrc to .gitignore"
    fi
fi

echo ""
echo "✅ direnv setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Copy template: cp .envrc.example .envrc"
echo "   2. Edit .envrc with your actual values"
echo "   3. Allow direnv: direnv allow"
echo "   4. Reload shell: source $SHELL_RC"
echo ""
echo "🔒 Security notes:"
echo "   - .envrc is gitignored automatically"
echo "   - Environment variables are loaded only when you cd into this directory"
echo "   - Variables are unloaded when you leave the directory"
