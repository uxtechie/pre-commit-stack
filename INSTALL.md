# 📦 Guía de Instalación Completa

Esta guía te ayudará a instalar todas las herramientas necesarias para el pre-commit stack.

## 🎯 Instalación Rápida (Recomendada)

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd pre-commit-stack

# 2. Ejecutar setup completo
make setup

# 3. Listo! Los hooks están instalados
```

## 📋 Instalación Detallada por Stack

### 🐍 Python Stack

```bash
# Dependencias base (obligatorio)
pip install -e .

# Herramientas de desarrollo
pip install pre-commit ruff mypy bandit safety pip-audit pytest pytest-cov

# Verificar instalación
ruff --version    # 0.14.5+
mypy --version    # 1.18.2+
bandit --version  # 1.7.10+
```

### 🦀 Rust Stack

```bash
# Rustup (si no lo tienes)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Nightly (para cargo-udeps)
rustup toolchain install nightly

# Herramientas de calidad
cargo install cargo-audit
cargo install cargo-deny
cargo install cargo-outdated
cargo install cargo-llvm-cov
cargo install cargo-udeps --locked

# Verificar instalación
cargo --version
cargo +nightly --version
cargo audit --version
cargo llvm-cov --version
```

### 📱 Flutter/Dart Stack

```bash
# Flutter SDK (si no lo tienes)
# https://docs.flutter.dev/get-started/install

# DCM (Dart Code Metrics)
dart pub global activate dcm

# Añadir al PATH si es necesario
export PATH="$PATH":"$HOME/.pub-cache/bin"

# Verificar instalación
flutter --version
dart --version
dcm --version
```

### 📝 TypeScript/JavaScript Stack

```bash
# Node.js (si no lo tienes)
# Usa nvm: https://github.com/nvm-sh/nvm

# Biome v2
npm install -g @biomejs/biome@2.3.5

# O con pnpm
pnpm add -g @biomejs/biome@2.3.5

# Verificar instalación
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

# Linux (descarga binary)
wget https://github.com/sbdchd/squawk/releases/download/v1.1.0/squawk-linux-x86_64
chmod +x squawk-linux-x86_64
sudo mv squawk-linux-x86_64 /usr/local/bin/squawk

# Verificar instalación
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

# Verificar instalación
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

# Crear baseline inicial
detect-secrets scan --baseline .secrets.baseline

# Verificar instalación
gitleaks version
detect-secrets --version
```

### 🐘 Odoo 19 Stack

```bash
# Pylint-odoo
pip install pylint-odoo>=9.3.22

# OCA pre-commit hooks
pip install oca-odoo-pre-commit-hooks>=0.1.6

# Verificar instalación
pylint --load-plugins=pylint_odoo --version
```

## 🔧 Configuración Post-Instalación

### 1. Inicializar Pre-commit

```bash
# Instalar los hooks en el repositorio
pre-commit install --install-hooks

# Instalar hook de commit-msg
pre-commit install --hook-type commit-msg

# Instalar hook de pre-push
pre-commit install --hook-type pre-push

# Verificar configuración
pre-commit validate-config
```

### 2. Ejecutar Primera Vez

```bash
# Ejecutar en todos los archivos (puede tardar)
pre-commit run --all-files

# Si hay errores, intenta auto-fix
make format
make sql-fix

# Ejecutar de nuevo
pre-commit run --all-files
```

### 3. Configurar Secrets Baseline

```bash
# Crear baseline de secretos existentes (si los hay)
detect-secrets scan --baseline .secrets.baseline

# Auditar y marcar falsos positivos
detect-secrets audit .secrets.baseline
```

## 📦 Instalación por Sistema Operativo

### macOS

```bash
# Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar todo con Homebrew
brew install python@3.11 node rust git
brew install gitleaks trivy hadolint
brew install shellcheck shfmt

# Instalar Flutter
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
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Dependencias base
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

### Windows (WSL2 recomendado)

```bash
# Instalar WSL2 primero
# Luego seguir instrucciones de Ubuntu arriba

# O usar Chocolatey
choco install python nodejs git rust gitleaks

# Python packages
pip install -e .

# Node packages
npm install -g @biomejs/biome@2.3.5

# Rust tools
cargo install cargo-audit cargo-deny cargo-outdated cargo-llvm-cov
```

## ✅ Verificación de Instalación

Ejecuta este script para verificar que todo está instalado:

```bash
#!/bin/bash
echo "🔍 Verificando instalación de herramientas..."

check_tool() {
    if command -v $1 &> /dev/null; then
        echo "✅ $1: $(command -v $1)"
        $1 --version 2>/dev/null || echo "   (instalado pero sin --version)"
    else
        echo "❌ $1: NO ENCONTRADO"
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
echo "🎉 Verificación completa!"
```

## 🆘 Solución de Problemas

### Error: "command not found"

```bash
# Añadir al PATH
export PATH="$PATH:$HOME/.local/bin"
export PATH="$PATH:$HOME/.cargo/bin"
export PATH="$PATH:$HOME/.pub-cache/bin"

# Hacer permanente (añadir a ~/.bashrc o ~/.zshrc)
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
```

### Error: "pre-commit command not found"

```bash
# Reinstalar pre-commit
pip install --user pre-commit
# O
pip3 install --user pre-commit
```

### Error: "cargo: command not found"

```bash
# Instalar Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

### Error: "dcm: command not found"

```bash
# Activar DCM globalmente
dart pub global activate dcm

# Añadir al PATH
export PATH="$PATH":"$HOME/.pub-cache/bin"
```

### Error al ejecutar pre-commit hooks

```bash
# Limpiar cache
pre-commit clean

# Reinstalar hooks
pre-commit install --install-hooks --overwrite

# Ejecutar con verbose para ver errores
pre-commit run --all-files --verbose
```

## 📚 Recursos Adicionales

- [Guía oficial de pre-commit](https://pre-commit.com/#install)
- [Ruff installation](https://docs.astral.sh/ruff/installation/)
- [Rust installation](https://www.rust-lang.org/tools/install)
- [Flutter installation](https://docs.flutter.dev/get-started/install)
- [Node.js installation](https://nodejs.org/en/download/)

---

**¿Necesitas ayuda?** Abre un issue en el repositorio del proyecto.
