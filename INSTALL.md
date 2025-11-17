# 📦 Complete Installation Guide

This guide will help you install all the necessary tools for the pre-commit stack.

## 🎯 Quick Installation (Recommended)

```bash
# 1. Clone the repository
git clone <repo-url>
cd pre-commit-stack

# 2. Run complete setup
make setup

# 3. Done! Hooks are installed
```

## 📋 Detailed Installation by Stack

### 🐍 Python Stack

```bash
# Base dependencies (mandatory)
pip install -e .

# Development tools
pip install pre-commit ruff mypy bandit safety pip-audit pytest pytest-cov yamllint

# Verify installation
ruff --version      # 0.14.5+
mypy --version      # 1.18.2+
bandit --version    # 1.7.10+
yamllint --version  # 1.37.1+
```

### 🦀 Rust Stack

```bash
# Rustup (if you don't have it)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Nightly (for cargo-udeps)
rustup toolchain install nightly

# Quality tools
cargo install cargo-audit
cargo install cargo-deny
cargo install cargo-outdated
cargo install cargo-llvm-cov
cargo install cargo-udeps --locked

# Verify installation
cargo --version
cargo +nightly --version
cargo audit --version
cargo llvm-cov --version
```

### 📱 Flutter/Dart Stack

```bash
# Flutter SDK (if you don't have it)
# https://docs.flutter.dev/get-started/install

# DCM (Dart Code Metrics)
dart pub global activate dcm

# Add to PATH if necessary
export PATH="$PATH":"$HOME/.pub-cache/bin"

# Verify installation
flutter --version
dart --version
dcm --version
```

### 📝 TypeScript/JavaScript Stack

```bash
# Node.js (if you don't have it)
# Use nvm: https://github.com/nvm-sh/nvm

# Biome v2
npm install -g @biomejs/biome@2.3.5

# Or with pnpm
pnpm add -g @biomejs/biome@2.3.5

# Verify installation
node --version  # v18+
biome --version # 2.3.5
```

### 🐘 PostgreSQL/plSQL Stack

```bash
# SQLFluff
pip install sqlfluff>=3.4.0

# Squawk
# macOS
brew install sbdchd/squawk/squawk

# Linux (download binary)
wget https://github.com/sbdchd/squawk/releases/download/v1.1.0/squawk-linux-x86_64
chmod +x squawk-linux-x86_64
sudo mv squawk-linux-x86_64 /usr/local/bin/squawk

# Verify installation
sqlfluff version
squawk --version
```

### 🐳 Docker Stack

```bash
# Hadolint
# macOS
brew install hadolint

# Linux
wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64
chmod +x hadolint-Linux-x86_64
sudo mv hadolint-Linux-x86_64 /usr/local/bin/hadolint

# Trivy (security scanner)
# macOS
brew install trivy

# Linux
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Verify installation
hadolint --version
trivy --version
```

### 🔒 Security Stack

```bash
# Gitleaks
# macOS
brew install gitleaks

# Linux
wget https://github.com/gitleaks/gitleaks/releases/download/v8.29.0/gitleaks_8.29.0_linux_x64.tar.gz
tar -xzf gitleaks_8.29.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/

# detect-secrets
pip install detect-secrets>=1.5.0

# Create initial baseline
detect-secrets scan --baseline .secrets.baseline

# Verify installation
gitleaks version
detect-secrets --version
```

### 🐘 Odoo 19 Stack

```bash
# Pylint-odoo
pip install pylint-odoo>=9.3.22

# OCA pre-commit hooks
pip install oca-odoo-pre-commit-hooks>=0.1.6

# Verify installation
pylint --load-plugins=pylint_odoo --version
```

## 🔧 Post-Installation Configuration

### 1. Initialize Pre-commit

```bash
# Install hooks in the repository
pre-commit install --install-hooks

# Install commit-msg hook
pre-commit install --hook-type commit-msg

# Install pre-push hook
pre-commit install --hook-type pre-push

# Verify configuration
pre-commit validate-config
```

### 2. First Run

```bash
# Run on all files (may take time)
pre-commit run --all-files

# If there are errors, try auto-fix
make format
make sql-fix

# Run again
pre-commit run --all-files
```

### 3. Configure Secrets Baseline

```bash
# Create baseline of existing secrets (if any)
detect-secrets scan --baseline .secrets.baseline

# Audit and mark false positives
detect-secrets audit .secrets.baseline
```

## 📦 Installation by Operating System

### macOS

```bash
# Homebrew (if you don't have it)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install everything with Homebrew
brew install python@3.11 node rust git
brew install gitleaks trivy hadolint
brew install shellcheck shfmt

# Install Flutter
brew install --cask flutter

# Python packages
pip3 install -e .

# Node packages
npm install -g @biomejs/biome@2.3.5

# Rust tools
cargo install cargo-audit cargo-deny cargo-outdated cargo-llvm-cov
```

### Ubuntu/Debian

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Base dependencies
sudo apt install -y python3.11 python3-pip nodejs npm git build-essential

# Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Gitleaks
wget https://github.com/gitleaks/gitleaks/releases/download/v8.29.0/gitleaks_8.29.0_linux_x64.tar.gz
tar -xzf gitleaks_8.29.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/

# Trivy
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Python packages
pip3 install -e .

# Node packages
npm install -g @biomejs/biome@2.3.5

# Rust tools
cargo install cargo-audit cargo-deny cargo-outdated cargo-llvm-cov
```

### Windows (WSL2 recommended)

```bash
# Install WSL2 first
# Then follow Ubuntu instructions above

# Or use Chocolatey
choco install python nodejs git rust gitleaks

# Python packages
pip install -e .

# Node packages
npm install -g @biomejs/biome@2.3.5

# Rust tools
cargo install cargo-audit cargo-deny cargo-outdated cargo-llvm-cov
```

## ✅ Installation Verification

Run this script to verify everything is installed:

```bash
#!/bin/bash
echo "🔍 Verifying tool installation..."

check_tool() {
    if command -v $1 &> /dev/null; then
        echo "✅ $1: $(command -v $1)"
        $1 --version 2>/dev/null || echo "   (installed but no --version)"
    else
        echo "❌ $1: NOT FOUND"
    fi
}

# Core
check_tool python3
check_tool git
check_tool pre-commit

# Python
check_tool ruff
check_tool mypy
check_tool bandit

# Rust
check_tool cargo
check_tool cargo-audit
check_tool cargo-deny
check_tool cargo-llvm-cov

# Node/TypeScript
check_tool node
check_tool npm
check_tool biome

# Flutter/Dart
check_tool flutter
check_tool dart
check_tool dcm

# SQL
check_tool sqlfluff
check_tool squawk

# Docker
check_tool hadolint
check_tool trivy

# Security
check_tool gitleaks
check_tool detect-secrets

echo ""
echo "🎉 Verification complete!"
```

## 🆘 Troubleshooting

### Error: "command not found"

```bash
# Add to PATH
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/.pub-cache/bin"

# Make permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
```

### Error: "pre-commit command not found"

```bash
# Reinstall pre-commit
pip install --user pre-commit
# Or
pip3 install --user pre-commit
```

### Error: "cargo: command not found"

```bash
# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

### Error: "dcm: command not found"

```bash
# Activate DCM globally
dart pub global activate dcm

# Add to PATH
export PATH="$PATH":"$HOME/.pub-cache/bin"
```

### Error running pre-commit hooks

```bash
# Clean cache
pre-commit clean

# Reinstall hooks
pre-commit install --install-hooks --overwrite

# Run with verbose to see errors
pre-commit run --all-files --verbose
```

## 📚 Additional Resources

- [Official pre-commit guide](https://pre-commit.com/#install)
- [Ruff installation](https://docs.astral.sh/ruff/installation/)
- [Rust installation](https://www.rust-lang.org/tools/install)
- [Flutter installation](https://docs.flutter.dev/get-started/install)
- [Node.js installation](https://nodejs.org/en/download/)

---

**Need help?** Open an issue in the project repository.
