# 🚀 Universal Pre-commit Stack

Universal and modular pre-commit hooks stack for multi-language projects, optimized for professional development with the latest open source tools (November 2025).

## 📋 Table of Contents

- [Features](#-features)
- [Supported Stacks](#-supported-stacks)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration by Stack](#-configuration-by-stack)
- [Make Commands](#-make-commands)
- [Requirements](#-requirements)
- [Roadmap](#-roadmap)

## ✨ Features

- ✅ **Multi-language**: Support for 8+ languages and frameworks
- ⚡ **High performance**: Modern tools written in Rust (Ruff, Biome)
- 🛡️ **Multi-layer security**: Secrets detection, vulnerabilities, and SQL injection
- 🎯 **Modular**: Activate only the stacks you need
- 🔄 **Always up-to-date**: Latest versions (Nov 2025)
- 📊 **Code metrics**: Coverage, complexity, unused code detection
- 🐘 **Optimized for Odoo 19**: Specific validations for Odoo

## 🎨 Supported Stacks

| Stack | Tools | Features |
|-------|-------|----------|
| **Python** | Ruff, Mypy, Bandit, Safety | Ultra-fast linting, 40% faster type checking (v1.18), security |
| **Rust** | Clippy, Fmt, Audit, Coverage | Linting, formatting, security audit, coverage with llvm-cov, unused deps detection |
| **Flutter/Dart** | Flutter Analyze (auto-detect), **DCM** | Auto-detection Flutter vs Dart + premium metrics (complexity, unused code) |
| **TypeScript/JS** | **Biome v2** | Type-aware linting without TypeScript compiler, 373 rules, Vue/Svelte/Astro support |
| **PostgreSQL/plSQL** | SQLFluff, Squawk | SQL linting, migration downtime prevention, SQL injection detection |
| **Odoo 19** | OCA tools, Pylint-Odoo | Module validation, XML, manifests, OWL components |
| **Shell** | ShellCheck, shfmt | Linting and formatting for bash scripts |
| **HTML/CSS** | Stylelint, HTMLHint | Validation and formatting |
| **Docker** | Hadolint, **Trivy** | Dockerfile linting + security scanning |
| **YAML** | yamllint v1.37.1 | Comprehensive linting (more than basic check-yaml) |
| **TOML** | **Taplo v0.9.3** | Linting and formatting for pyproject.toml, Cargo.toml, etc. |
| **Markdown** | markdownlint v0.45.0 | Linting and auto-fix with customizable rules |
| **General** | Gitleaks, detect-secrets | Multi-layer secrets detection |

### 🆕 What's New in This Version

- **Biome v2.3.5**: Type-aware linting for JS/TS without TypeScript compiler
- **Mypy v1.18.2**: 40% faster type checking
- **DCM for Flutter**: Unused code detection, complexity metrics
- **Flutter analyze auto-detect**: Automatically detects Flutter vs pure Dart projects
- **Complete PostgreSQL stack**: Critical for Odoo 19
- **yamllint v1.37.1**: Comprehensive YAML linting (beyond basic check-yaml)
- **Taplo v0.9.3**: TOML linting and formatting (pyproject.toml, Cargo.toml, etc.)
- **markdownlint v0.45.0**: Updated with custom configuration
- **Trivy**: Security scanning for Docker and filesystems
- **Rust enhanced**: Coverage with llvm-cov, unused deps detection

## 🚀 Installation

### Prerequisites

```bash
# Python 3.11+
python --version  # >= 3.11

# Pre-commit
pip install pre-commit>=4.4.0

# Git repository
git init  # if it's a new project
```

### Full Installation

```bash
# 1. Clone or copy this repository
git clone <this-repo>

# 2. Install Python dependencies
pip install -e .

# 3. Install pre-commit hooks
make setup

# 4. (Optional) Install additional tools per stack
```

### Installation by Stack

#### Python Stack
```bash
pip install ruff mypy bandit safety pip-audit
```

#### Rust Stack
```bash
cargo install cargo-audit cargo-deny cargo-outdated cargo-udeps
cargo install cargo-llvm-cov
```

#### Flutter/Dart Stack
```bash
dart pub global activate dcm
```

#### TypeScript/JavaScript Stack
```bash
npm install -g @biomejs/biome@2.3.5
```

#### PostgreSQL Stack
```bash
pip install sqlfluff squawk
```

#### Docker Stack
```bash
# Trivy
brew install trivy
# or
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
```

#### General Stack (Secrets)
```bash
# Gitleaks
brew install gitleaks

# detect-secrets
pip install detect-secrets
detect-secrets scan --baseline .secrets.baseline
```

## 💻 Usage

### Manual Execution

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run a specific hook
pre-commit run ruff --all-files
pre-commit run biome-check --all-files
pre-commit run sqlfluff-lint --all-files

# Run only on staged files
pre-commit run
```

### Automatic Execution

Hooks run automatically on:
- **pre-commit**: Before each commit
- **commit-msg**: Commit message validation (Conventional Commits)
- **pre-push**: Complete tests, coverage, security scans

### Available Make Commands

```bash
# Initial setup
make setup          # Install hooks and dependencies

# Linting and formatting
make lint           # Run all pre-commit hooks
make format         # Format code (Python)

# Python
make test           # Run tests
make coverage       # Generate coverage report

# Odoo
make odoo-lint      # Odoo-specific linting
make odoo-check-structure

# PostgreSQL/SQL
make sql-lint       # Lint SQL files
make sql-fix        # Auto-fix SQL
make sql-check-injection  # Detect SQL injection

# Rust
make rust-coverage  # Generate HTML coverage report
make rust-outdated  # Outdated deps
make rust-udeps     # Unused deps

# Flutter/Dart
make flutter-analyze      # Complete analysis (dart + dcm)
make flutter-metrics      # Code metrics
make flutter-coverage     # HTML coverage

# Docker
make docker-scan    # Security scan with Trivy

# Security
make security       # All security checks
make secrets-scan   # Secrets scanning
make audit          # Dependencies audit

# Cleanup
make clean          # Clean temporary files
```

## ⚙️ Configuration by Stack

### Python (pyproject.toml)

Project uses Ruff for linting and formatting, with Odoo-specific configuration:

```toml
[tool.ruff]
target-version = "py311"
line-length = 79

[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "C4", "DTZ", "T10", ...]
ignore = ["E501", "N999", ...]
```

### TypeScript/JavaScript (biome.json)

Biome v2 with type-aware linting:

```json
{
  "$schema": "https://biomejs.dev/schemas/2.3.5/schema.json",
  "files": {
    "include": ["**/*.ts", "**/*.tsx", "**/*.vue", "**/*.svelte", "**/*.astro"]
  }
}
```

### Flutter/Dart (dcm.yaml)

DCM with strict metrics:

```yaml
metrics:
  cyclomatic-complexity: 20
  lines-of-code: 100
  number-of-parameters: 4
```

### PostgreSQL (.sqlfluff)

SQLFluff configured for PostgreSQL:

```ini
[sqlfluff]
dialect = postgres
max_line_length = 120
```

### YAML (.yamllint)

Yamllint with relaxed configuration:

```yaml
extends: relaxed
rules:
  line-length:
    max: 120
```

### TOML (.taplo.toml)

Taplo for formatting and linting:

```toml
[formatting]
array_trailing_comma = true
column_width = 100
trailing_newline = true
```

### Markdown (.markdownlint.json)

Custom Markdownlint:

```json
{
  "line-length": { "line_length": 120 },
  "no-inline-html": {
    "allowed_elements": ["details", "summary", "br"]
  }
}
```

### Rust (deny.toml)

Cargo-deny for licenses and security:

```toml
[licenses]
allow = ["MIT", "Apache-2.0", "BSD-3-Clause"]
deny = ["GPL-2.0", "GPL-3.0"]
```

## 📊 Metrics and Reports

### Python Coverage
```bash
make coverage
# Opens: htmlcov/index.html
```

### Rust Coverage
```bash
make rust-coverage
# Opens: target/llvm-cov/html/index.html
```

### Flutter Coverage
```bash
make flutter-coverage
# Opens: coverage/html/index.html
```

### Flutter Metrics
```bash
make flutter-metrics
# Shows unused files/code
```

## 🔒 Security

The stack implements multiple security layers:

1. **Secrets Detection** (2 layers):
   - Gitleaks: Fast and comprehensive
   - detect-secrets: Complementary patterns

2. **Vulnerabilities**:
   - Python: Bandit + Safety
   - Rust: cargo-audit + cargo-deny
   - npm: npm audit
   - Docker: Trivy

3. **SQL Injection**:
   - Static Python code analysis
   - Dangerous patterns detection (f-strings, concatenation)

4. **Docker Security**:
   - Trivy config scan
   - Trivy filesystem scan

## 🎯 Use Cases

### Python + PostgreSQL + Odoo Project
```yaml
# Only activate these stacks in .pre-commit-config.yaml
# Comment out or remove the others
```

### Flutter Project
```bash
# Install DCM
dart pub global activate dcm

# Run
make flutter-analyze
```

### Rust + PostgreSQL Project
```bash
# Install Rust tools
cargo install cargo-llvm-cov cargo-audit

# Run
make lint
make rust-coverage
```

## 🛠️ Tool Requirements

### Mandatory (core)
- Python >= 3.11
- pre-commit >= 4.4.0
- Git

### Per stack (install as needed)

**Python:**
- ruff >= 0.14.5
- mypy >= 1.18.2
- bandit >= 1.7.10

**Rust:**
- rustc + cargo (stable)
- cargo nightly (for udeps)
- cargo-llvm-cov
- cargo-audit, cargo-deny, cargo-outdated

**Flutter/Dart:**
- Dart SDK
- Flutter SDK
- DCM (`dart pub global activate dcm`)

**TypeScript/JavaScript:**
- Node.js >= 18
- @biomejs/biome >= 2.3.5

**PostgreSQL:**
- sqlfluff >= 3.4.0
- squawk >= 1.1.0

**Docker:**
- trivy

**Secrets:**
- gitleaks >= 8.29.0
- detect-secrets >= 1.5.0

## 🗺️ Roadmap

### Phase 1: Completed ✅
- [x] Biome v2 update
- [x] Mypy v1.18.2 update
- [x] Complete PostgreSQL/plSQL stack
- [x] DCM for Flutter/Dart
- [x] Rust enhanced (coverage, deps)
- [x] Multi-layer secrets detection
- [x] Trivy security scanning

### Phase 2: In Progress 🚧
- [ ] CLI tool for project initialization
- [ ] Templates per stack
- [ ] Predefined configurations
- [ ] Automated stack tests

### Phase 3: Planned 📝
- [ ] GitHub Actions workflows
- [ ] GitLab CI templates
- [ ] Docker image with all tools
- [ ] VS Code extension
- [ ] Metrics dashboard

## 📚 Additional Documentation

- [Official Pre-commit](https://pre-commit.com/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Biome documentation](https://biomejs.dev/)
- [DCM documentation](https://dcm.dev/)
- [SQLFluff documentation](https://docs.sqlfluff.com/)
- [Trivy documentation](https://aquasecurity.github.io/trivy/)

## 🤝 Contributing

Contributions are welcome. Please:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - see the LICENSE file for more details

## 🙏 Acknowledgments

This project uses the following open source tools:
- [pre-commit](https://github.com/pre-commit/pre-commit)
- [Ruff](https://github.com/astral-sh/ruff)
- [Biome](https://github.com/biomejs/biome)
- [DCM](https://github.com/dart-code-checker/dart-code-metrics)
- [SQLFluff](https://github.com/sqlfluff/sqlfluff)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [Trivy](https://github.com/aquasecurity/trivy)
- And many more...

---

**Version**: 0.1.0
**Last Updated**: November 2025
**Stack Optimized For**: Odoo 19.0, Python 3.11+, Rust stable, Flutter 3.x, Node.js 18+
