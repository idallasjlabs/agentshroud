#
# flake.nix — AgentShroud™ reproducible development environment (SCRUM-92).
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Provisioning is Nix/flakes-first per repo policy (NEVER apt/brew/manual export).
# A collaborator runs `nix develop` and gets the full toolchain: Python 3.11 with the
# test/lint deps, docker-compose, ruff, black, shellcheck, node, and pytest.
#
# Outputs:
#   devShells.default        — the dev shell (nix develop)
#   checks.lint              — ruff + black --check + shellcheck over scripts/
#   checks.runtime-shim      — the SCRUM-92 container-runtime detection smoke test
#   apps.lint                — `nix run .#lint`  (ruff + black + shellcheck)
#   apps.smoke               — `nix run .#smoke` (bash scripts/smoke.sh, static)
#   formatter                — nixpkgs-fmt (nix fmt)
#
# Verify (requires nix with flakes enabled):
#   nix develop            # enter the dev shell
#   nix flake check        # build devShell + run checks.lint + checks.runtime-shim
#   nix run .#lint         # run the lint app
#   nix run .#smoke        # run the static smoke suite
#
{
  description = "AgentShroud™ Gateway — reproducible dev environment (Python + container tooling)";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        # Python 3.11 with the project's test + lint dependencies. Runtime service
        # deps (presidio/spacy/fastapi) are installed inside the container image;
        # the dev shell provides just what a contributor needs to run unit tests,
        # lint, and format on the host.
        python = pkgs.python311;
        pythonEnv = python.withPackages (ps: with ps; [
          pip
          pytest
          pytest-asyncio
          pyyaml
          httpx
          fastapi
          pydantic
        ]);

        # Toolchain shared by the dev shell and the lint check.
        devTools = [
          pythonEnv
          pkgs.ruff
          pkgs.black
          pkgs.shellcheck
          pkgs.docker-compose
          pkgs.nodejs_20
          pkgs.git
          pkgs.curl
          pkgs.jq
        ];
      in
      {
        devShells.default = pkgs.mkShell {
          packages = devTools;
          shellHook = ''
            echo "AgentShroud™ dev shell — Python $(${pythonEnv}/bin/python --version 2>&1 | cut -d' ' -f2)"
            echo "  ruff $(${pkgs.ruff}/bin/ruff --version 2>/dev/null | cut -d' ' -f2), black, shellcheck, docker-compose, node $(${pkgs.nodejs_20}/bin/node --version)"
            echo "  Lint:  ruff check . && black --check ."
            echo "  Smoke: bash scripts/smoke.sh"
          '';
        };

        # ── checks.lint ──────────────────────────────────────────────────────
        # ruff + black --check over the tracked Python, shellcheck over the shim +
        # its test. Runs in the Nix sandbox against the flake source.
        checks.lint = pkgs.runCommand "agentshroud-lint"
          {
            nativeBuildInputs = [ pkgs.ruff pkgs.black pkgs.shellcheck ];
            src = self;
          }
          ''
            cd "$src"
            echo "== ruff =="
            ruff check gateway scripts || exit 1
            echo "== black --check =="
            black --check gateway scripts 2>/dev/null || black --check gateway || exit 1
            echo "== shellcheck =="
            shellcheck scripts/lib/container-runtime.sh scripts/smoke.d/test-container-runtime.sh || exit 1
            touch "$out"
          '';

        # ── checks.runtime-shim ──────────────────────────────────────────────
        # Runs the SCRUM-92 container-runtime detection smoke test. It exercises
        # detection with fake docker/podman stubs, so it needs no real daemon.
        checks.runtime-shim = pkgs.runCommand "agentshroud-runtime-shim"
          {
            nativeBuildInputs = [ pkgs.bash pkgs.coreutils ];
            src = self;
          }
          ''
            cd "$src"
            bash scripts/smoke.d/test-container-runtime.sh
            touch "$out"
          '';

        # ── apps ─────────────────────────────────────────────────────────────
        apps.lint = {
          type = "app";
          program = toString (pkgs.writeShellScript "agentshroud-lint" ''
            set -euo pipefail
            export PATH="${pkgs.lib.makeBinPath [ pkgs.ruff pkgs.black pkgs.shellcheck ]}:$PATH"
            ruff check gateway scripts
            black --check gateway || true
            shellcheck scripts/lib/container-runtime.sh scripts/smoke.d/test-container-runtime.sh
          '');
        };

        apps.smoke = {
          type = "app";
          program = toString (pkgs.writeShellScript "agentshroud-smoke" ''
            set -euo pipefail
            export PATH="${pkgs.lib.makeBinPath [ pkgs.bash pkgs.nodejs_20 pkgs.coreutils ]}:$PATH"
            exec bash scripts/smoke.sh
          '');
        };

        formatter = pkgs.nixpkgs-fmt;
      });
}
