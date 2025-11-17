.PHONY: setup lint format test odoo-* clean

# Python version for Odoo 19 (requires 3.11+)
PYTHON := python3.11
ODOO_VERSION := 19.0

# Setup
setup:
	$(PYTHON) -m pip install -U pip pre-commit
	pre-commit install --install-hooks
	pre-commit install --hook-type commit-msg
	pre-commit install --hook-type pre-push
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r requirements-dev.txt

# Update hooks
update:
	pre-commit autoupdate

# Run all pre-commit hooks
lint:
	pre-commit run --all-files

# Odoo specific linting
odoo-lint:
	pylint --load-plugins=pylint_odoo \
		--valid-odoo-versions=$(ODOO_VERSION) \
		-d all -e odoolint \
		--rcfile=.pylintrc \
		addons/*/

# Check Odoo module structure
odoo-check-structure:
	@for manifest in addons/*/__manifest__.py; do \
		echo "Checking $$manifest for Odoo compliance..."; \
		$(PYTHON) scripts/validate_odoo_structure.py $$manifest; \
	done

# Check OWL components (Odoo uses OWL framework)
odoo-check-owl:
	@echo "Validating OWL components..."
	@find addons -path "*/static/src/*.js" -o -path "*/static/src/*.xml" | \
		while read f; do \
			$(PYTHON) scripts/validate_owl_components.py "$$f"; \
		done

# Check AI Server Actions
odoo-check-ai:
	@echo "Validating AI Server Actions..."
	@find addons -name "*server_action*.xml" | \
		while read f; do \
			xmllint --noout "$$f" 2>&1 || echo "Error in $$f"; \
		done

# Check ESG/Sustainability modules
odoo-check-esg:
	@echo "Checking ESG/Sustainability compliance..."
	@$(PYTHON) scripts/check_esg_data.py addons/

# Format code
format:
	ruff format addons/
	ruff check --fix addons/

# Run tests
test:
	pytest tests/ -v

coverage:
	pytest --cov=src --cov-report=html --cov-report=term

# Odoo specific tests
odoo-test:
	odoo-bin -c odoo.conf --test-enable --stop-after-init \
		--log-level=test -d test_db -u all

# PostgreSQL/SQL checks
sql-lint:
	@echo "Linting SQL files..."
	@find . -name "*.sql" -not -path "*/node_modules/*" -not -path "*/.git/*" | \
		xargs -I {} sqlfluff lint --dialect postgres {}

sql-fix:
	@echo "Auto-fixing SQL files..."
	@find . -name "*.sql" -not -path "*/node_modules/*" -not -path "*/.git/*" | \
		xargs -I {} sqlfluff fix --dialect postgres {}

sql-check-injection:
	@echo "Checking for SQL injection vulnerabilities..."
	@$(PYTHON) scripts/check_sql_injection.py $$(find . -name "*.py" -not -path "*/tests/*")

# Security checks
security:
	gitleaks detect --verbose --redact
	bandit -r addons/ -c pyproject.toml
	safety check
	$(MAKE) sql-check-injection

# Audit dependencies
audit:
	pip-audit
	npm audit
	cargo audit

# Rust-specific commands
rust-coverage:
	cargo llvm-cov --html --open

rust-outdated:
	cargo outdated

rust-udeps:
	cargo +nightly udeps --all-targets

# Flutter/Dart-specific commands
flutter-analyze:
	dart analyze
	dcm analyze

flutter-metrics:
	dcm check-unused-files
	dcm check-unused-code

flutter-coverage:
	flutter test --coverage
	genhtml coverage/lcov.info -o coverage/html
	@echo "Coverage report: coverage/html/index.html"

# Docker security
docker-scan:
	trivy config .
	trivy fs --severity CRITICAL .

# Secrets scanning
secrets-scan:
	gitleaks detect --verbose --redact
	detect-secrets scan --baseline .secrets.baseline

secrets-audit:
	detect-secrets audit .secrets.baseline

# Clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
