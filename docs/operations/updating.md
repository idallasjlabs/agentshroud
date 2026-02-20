# Updating AgentShroud

Universal update guide for all platforms.

## Check Current Version

```bash
cat README.md | head -5
# or
git describe --tags --always
```

## Update from Git

### Tracking a Tagged Release

```bash
git fetch --all --tags
git checkout v<new-version>
cd docker && docker compose build && docker compose up -d
```

### Tracking Main Branch

```bash
git pull origin main
cd docker && docker compose build && docker compose up -d
```

## Update from Release Tarball

For deployments without Git:

1. Download the release tarball from the [Releases page](https://github.com/yourusername/agentshroud/releases)
2. Back up your current installation:
   ```bash
   cp -r agentshroud agentshroud.backup
   ```
3. Extract the new release:
   ```bash
   tar xzf agentshroud-v0.2.0.tar.gz
   ```
4. Copy your configuration:
   ```bash
   cp agentshroud.backup/agentshroud.yaml agentshroud/agentshroud.yaml
   cp -r agentshroud.backup/docker/secrets agentshroud/docker/secrets
   ```
5. Rebuild and restart:
   ```bash
   cd agentshroud/docker && docker compose build && docker compose up -d
   ```

## Database Migrations

Currently, AgentShroud does not require database migrations. If future versions introduce migrations, they will be documented in the release notes and run automatically on startup.

## Rollback Procedure

If an update causes issues:

### With Git

```bash
# Check available tags
git tag -l

# Roll back to the previous version
git checkout v<previous-version>
cd docker && docker compose build && docker compose up -d
```

### Without Git

Restore from your backup:

```bash
rm -rf agentshroud
mv agentshroud.backup agentshroud
cd agentshroud/docker && docker compose build && docker compose up -d
```

## Checking the Changelog

Review what changed between versions:

```bash
# Git log between tags
git log v0.1.0..v0.2.0 --oneline

# Or check the CHANGELOG if available
cat CHANGELOG.md
```

Release notes are also published on the [GitHub Releases page](https://github.com/yourusername/agentshroud/releases).
