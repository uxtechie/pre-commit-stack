# 🚀 Pre-commit Stack Universal

Stack de pre-commit hooks universal y modular para proyectos multi-lenguaje, optimizado para desarrollo profesional con las últimas herramientas open source (Noviembre 2025).

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Stacks Soportados](#-stacks-soportados)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Configuración por Stack](#-configuración-por-stack)
- [Comandos Make](#-comandos-make)
- [Requisitos](#-requisitos)
- [Roadmap](#-roadmap)

## ✨ Características

- ✅ **Multi-lenguaje**: Soporte para 8+ lenguajes y frameworks
- ⚡ **Alto rendimiento**: Herramientas modernas escritas en Rust (Ruff, Biome)
- 🛡️ **Seguridad multi-capa**: Detección de secretos, vulnerabilidades y SQL injection
- 🎯 **Modular**: Activa solo los stacks que necesites
- 🔄 **Siempre actualizado**: Versiones más recientes (Nov 2025)
- 📊 **Métricas de código**: Coverage, complejidad, código no usado
- 🐘 **Optimizado para Odoo 19**: Validaciones específicas para Odoo

## 🎨 Stacks Soportados

| Stack | Herramientas | Características |
|-------|--------------|-----------------|
| **Python** | Ruff, Mypy, Bandit, Safety | Linting ultra-rápido, type checking 40% más rápido (v1.18), seguridad |
| **Rust** | Clippy, Fmt, Audit, Coverage | Linting, formato, security audit, coverage con llvm-cov, detección de deps no usadas |
| **Flutter/Dart** | Dart Analyze, **DCM** | Análisis estándar + métricas premium (complejidad, código no usado) |
| **TypeScript/JS** | **Biome v2** | Type-aware linting sin TypeScript compiler, 373 reglas, soporte Vue/Svelte/Astro |
| **PostgreSQL/plSQL** | SQLFluff, Squawk | Linting SQL, prevención de downtime en migraciones, detección SQL injection |
| **Odoo 19** | OCA tools, Pylint-Odoo | Validación de módulos, XML, manifests, OWL components |
| **Shell** | ShellCheck, shfmt | Linting y formato de scripts bash |
| **HTML/CSS** | Stylelint, HTMLHint | Validación y formato |
| **Docker** | Hadolint, **Trivy** | Linting Dockerfile + security scanning |
| **General** | Gitleaks, detect-secrets | Detección de secretos multi-capa |

### 🆕 Novedades de esta versión

- **Biome v2.3.5**: Type-aware linting para JS/TS sin compilador TypeScript
- **Mypy v1.18.2**: 40% más rápido en type checking
- **DCM para Flutter**: Detección de código no usado, métricas de complejidad
- **Stack PostgreSQL completo**: Crítico para Odoo 19
- **Trivy**: Security scanning de Docker y filesystems
- **Rust enhanced**: Coverage con llvm-cov, detección de deps no usadas

## 🚀 Instalación

### Requisitos previos

```bash
# Python 3.11+
python --version  # >= 3.11

# Pre-commit
pip install pre-commit>=4.4.0

# Git repository
git init  # si es un proyecto nuevo
```

### Instalación completa

```bash
# 1. Clonar o copiar este repositorio
git clone <este-repo>

# 2. Instalar dependencias Python
pip install -e .

# 3. Instalar pre-commit hooks
make setup

# 4. (Opcional) Instalar herramientas adicionales según tu stack
```

### Instalación por stack

#### Stack Python
```bash
pip install ruff mypy bandit safety pip-audit
```

#### Stack Rust
```bash
cargo install cargo-audit cargo-deny cargo-outdated cargo-udeps
cargo install cargo-llvm-cov
```

#### Stack Flutter/Dart
```bash
dart pub global activate dcm
```

#### Stack TypeScript/JavaScript
```bash
npm install -g @biomejs/biome@2.3.5
```

#### Stack PostgreSQL
```bash
pip install sqlfluff squawk
```

#### Stack Docker
```bash
# Trivy
brew install trivy
# o
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
```

#### Stack General (Secrets)
```bash
# Gitleaks
brew install gitleaks

# detect-secrets
pip install detect-secrets
detect-secrets scan --baseline .secrets.baseline
```

## 💻 Uso

### Ejecución manual

```bash
# Ejecutar todos los hooks en todos los archivos
pre-commit run --all-files

# Ejecutar un hook específico
pre-commit run ruff --all-files
pre-commit run biome-check --all-files
pre-commit run sqlfluff-lint --all-files

# Ejecutar solo en archivos staged
pre-commit run
```

### Ejecución automática

Los hooks se ejecutan automáticamente en:
- **pre-commit**: Antes de cada commit
- **commit-msg**: Validación de mensaje de commit (Conventional Commits)
- **pre-push**: Tests, coverage, security scans completos

### Comandos Make disponibles

```bash
# Setup inicial
make setup          # Instala hooks y dependencias

# Linting y formato
make lint           # Ejecuta todos los pre-commit hooks
make format         # Formatea código (Python)

# Python
make test           # Ejecuta tests
make coverage       # Genera reporte de coverage

# Odoo
make odoo-lint      # Linting específico de Odoo
make odoo-check-structure

# PostgreSQL/SQL
make sql-lint       # Lint archivos SQL
make sql-fix        # Auto-fix SQL
make sql-check-injection  # Detecta SQL injection

# Rust
make rust-coverage  # Genera reporte HTML de coverage
make rust-outdated  # Deps obsoletas
make rust-udeps     # Deps no usadas

# Flutter/Dart
make flutter-analyze      # Análisis completo (dart + dcm)
make flutter-metrics      # Métricas de código
make flutter-coverage     # Coverage HTML

# Docker
make docker-scan    # Security scan con Trivy

# Seguridad
make security       # Todos los checks de seguridad
make secrets-scan   # Escaneo de secretos
make audit          # Audit de dependencias

# Limpieza
make clean          # Limpia archivos temporales
```

## ⚙️ Configuración por Stack

### Python (pyproject.toml)

El proyecto usa Ruff para linting y formatting, con configuración específica para Odoo:

```toml
[tool.ruff]
target-version = "py311"
line-length = 79

[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP", "B", "C4", "DTZ", "T10", ...]
ignore = ["E501", "N999", ...]
```

### TypeScript/JavaScript (biome.json)

Biome v2 con type-aware linting:

```json
{
  "$schema": "https://biomejs.dev/schemas/2.3.5/schema.json",
  "files": {
    "include": ["**/*.ts", "**/*.tsx", "**/*.vue", "**/*.svelte", "**/*.astro"]
  }
}
```

### Flutter/Dart (dcm.yaml)

DCM con métricas estrictas:

```yaml
metrics:
  cyclomatic-complexity: 20
  lines-of-code: 100
  number-of-parameters: 4
```

### PostgreSQL (.sqlfluff)

SQLFluff configurado para PostgreSQL:

```ini
[sqlfluff]
dialect = postgres
max_line_length = 120
```

### Rust (deny.toml)

Cargo-deny para licencias y security:

```toml
[licenses]
allow = ["MIT", "Apache-2.0", "BSD-3-Clause"]
deny = ["GPL-2.0", "GPL-3.0"]
```

## 📊 Métricas y Reportes

### Python Coverage
```bash
make coverage
# Abre: htmlcov/index.html
```

### Rust Coverage
```bash
make rust-coverage
# Abre: target/llvm-cov/html/index.html
```

### Flutter Coverage
```bash
make flutter-coverage
# Abre: coverage/html/index.html
```

### Flutter Métricas
```bash
make flutter-metrics
# Muestra archivos/código no usado
```

## 🔒 Seguridad

El stack implementa múltiples capas de seguridad:

1. **Detección de secretos** (2 capas):
   - Gitleaks: Rápido y comprehensivo
   - detect-secrets: Patrones complementarios

2. **Vulnerabilidades**:
   - Python: Bandit + Safety
   - Rust: cargo-audit + cargo-deny
   - npm: npm audit
   - Docker: Trivy

3. **SQL Injection**:
   - Análisis estático de código Python
   - Detección de patrones peligrosos (f-strings, concatenación)

4. **Docker Security**:
   - Trivy config scan
   - Trivy filesystem scan

## 🎯 Casos de Uso

### Proyecto Python + PostgreSQL + Odoo
```yaml
# Solo activar estos stacks en .pre-commit-config.yaml
# Comentar o eliminar los demás
```

### Proyecto Flutter
```bash
# Instalar DCM
dart pub global activate dcm

# Ejecutar
make flutter-analyze
```

### Proyecto Rust + PostgreSQL
```bash
# Instalar herramientas Rust
cargo install cargo-llvm-cov cargo-audit

# Ejecutar
make lint
make rust-coverage
```

## 🛠️ Requisitos de Herramientas

### Obligatorias (core)
- Python >= 3.11
- pre-commit >= 4.4.0
- Git

### Por stack (instalar según necesidad)

**Python:**
- ruff >= 0.14.5
- mypy >= 1.18.2
- bandit >= 1.7.10

**Rust:**
- rustc + cargo (stable)
- cargo nightly (para udeps)
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

### Fase 1: Completado ✅
- [x] Actualización Biome v2
- [x] Actualización Mypy v1.18.2
- [x] Stack PostgreSQL/plSQL completo
- [x] DCM para Flutter/Dart
- [x] Rust enhanced (coverage, deps)
- [x] Multi-layer secrets detection
- [x] Trivy security scanning

### Fase 2: En progreso 🚧
- [ ] CLI tool para inicialización de proyectos
- [ ] Templates por stack
- [ ] Configuraciones predefinidas
- [ ] Tests automatizados del stack

### Fase 3: Planeado 📝
- [ ] GitHub Actions workflows
- [ ] GitLab CI templates
- [ ] Docker image con todas las herramientas
- [ ] VS Code extension
- [ ] Dashboard de métricas

## 📚 Documentación Adicional

- [Pre-commit oficial](https://pre-commit.com/)
- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Biome documentation](https://biomejs.dev/)
- [DCM documentation](https://dcm.dev/)
- [SQLFluff documentation](https://docs.sqlfluff.com/)
- [Trivy documentation](https://aquasecurity.github.io/trivy/)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'feat: add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

MIT License - ver el archivo LICENSE para más detalles

## 🙏 Agradecimientos

Este proyecto usa las siguientes herramientas open source:
- [pre-commit](https://github.com/pre-commit/pre-commit)
- [Ruff](https://github.com/astral-sh/ruff)
- [Biome](https://github.com/biomejs/biome)
- [DCM](https://github.com/dart-code-checker/dart-code-metrics)
- [SQLFluff](https://github.com/sqlfluff/sqlfluff)
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [Trivy](https://github.com/aquasecurity/trivy)
- Y muchas más...

---

**Versión**: 0.1.0
**Última actualización**: Noviembre 2025
**Stack optimizado para**: Odoo 19.0, Python 3.11+, Rust stable, Flutter 3.x, Node.js 18+
