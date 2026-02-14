#!/bin/bash
# setup-pgpass.sh
# Configure PostgreSQL password file for secure authentication

set -e

echo "🔐 Setting up PostgreSQL password file..."
echo ""

PGPASS_FILE="$HOME/.pgpass"

# Create pgpass file if it doesn't exist
if [ ! -f "$PGPASS_FILE" ]; then
    touch "$PGPASS_FILE"
    chmod 600 "$PGPASS_FILE"
    echo "✅ Created $PGPASS_FILE with secure permissions (600)"
else
    echo "⚠️  $PGPASS_FILE already exists"
    
    # Check permissions
    PERMS=$(stat -f "%OLp" "$PGPASS_FILE" 2>/dev/null || stat -c "%a" "$PGPASS_FILE" 2>/dev/null)
    if [ "$PERMS" != "600" ]; then
        echo "⚠️  Fixing permissions (was $PERMS, should be 600)"
        chmod 600 "$PGPASS_FILE"
    fi
fi

echo ""
echo "📄 PostgreSQL password file format:"
echo "   hostname:port:database:username:password"
echo ""
echo "Example entries:"
cat << 'EXAMPLES'
# Production database
prod-db.fluence.io:5432:operations:app_user:secret_password_here

# Development database  
dev-db.fluence.local:5432:*:fluence_dev:dev_password

# Localhost (any database)
localhost:5432:*:postgres:local_password

# AWS RDS instance
fluence-ops.abc123.us-east-1.rds.amazonaws.com:5432:operations:admin:aws_password
EXAMPLES

echo ""
echo "🔒 Alternative: AWS RDS IAM Authentication"
echo ""
echo "For AWS RDS, you can use IAM authentication instead:"
cat << 'IAM_AUTH'
# Generate auth token
export PGPASSWORD=$(aws rds generate-db-auth-token \
  --hostname fluence-ops.abc123.us-east-1.rds.amazonaws.com \
  --port 5432 \
  --username iam_user \
  --region us-east-1)

# Connect with token
psql -h fluence-ops.abc123.us-east-1.rds.amazonaws.com \
     -U iam_user \
     -d operations
IAM_AUTH

echo ""
echo "✅ PostgreSQL password setup complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Edit $PGPASS_FILE and add your connection entries"
echo "   2. Format: hostname:port:database:username:password"
echo "   3. Test connection: psql -h hostname -U username -d database"
echo ""
echo "🔒 Security notes:"
echo "   - File must have 600 permissions (owner read/write only)"
echo "   - Never commit this file to git"
echo "   - Use wildcards (*) for flexible matching"
echo "   - Consider AWS RDS IAM auth for production"
