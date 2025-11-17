#!/usr/bin/env python3
"""
Validate Odoo 19 module structure and new features compliance.
"""
import ast
import sys
from pathlib import Path


REQUIRED_MANIFEST_KEYS = {
    'name',
    'version',
    'depends',
    'license',
    'author',  # Now required in Odoo 19
}

ALLOWED_LICENSES = {
    'AGPL-3',
    'LGPL-3',
    'GPL-3',
    'Apache-2.0',
    'MIT',
    'Other proprietary',
}

DEPRECATED_KEYS = {
    'active',        # Deprecated in Odoo 19
    'description',   # Use README.md instead
}

REQUIRED_FILES = {
    '__init__.py',
    '__manifest__.py',
    'README.md',
    'LICENSE',  # More strictly enforced in Odoo 19
}

RECOMMENDED_DIRS = {
    'models',
    'views',
    'security',
    'data',
}

# New in Odoo 19
OWL_COMPONENT_STRUCTURE = {
    'static/src/components',
    'static/src/views',
    'static/src/xml',
}


def validate_manifest(manifest_path: Path) -> list[str]:
    """Validate __manifest__.py for Odoo."""
    errors = []

    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
            manifest = ast.literal_eval(content)
    except Exception as e:
        return [f"Error parsing manifest: {e}"]

    # Check required keys
    missing_keys = REQUIRED_MANIFEST_KEYS - set(manifest.keys())
    if missing_keys:
        errors.append(f"Missing required keys: {missing_keys}")

    # Check deprecated keys
    deprecated_found = DEPRECATED_KEYS & set(manifest.keys())
    if deprecated_found:
        errors.append(
            f"Deprecated keys found: {deprecated_found}. "
            "Remove these keys from manifest."
        )

    # Validate license
    license_key = manifest.get('license')
    if license_key and license_key not in ALLOWED_LICENSES:
        errors.append(
            f"Invalid license '{license_key}'. "
            f"Must be one of: {ALLOWED_LICENSES}"
        )

    # Check version format (19.0.X.Y.Z)
    version = manifest.get('version', '')
    if not version.startswith('19.0.'):
        errors.append(
            f"Version '{version}' must start with '19.0.' for Odoo"
        )

    parts = version.split('.')
    if len(parts) != 5:
        errors.append(
            f"Version '{version}' should have format 19.0.X.Y.Z"
        )

    # Check for AI-related dependencies if using AI features
    if any('ai' in dep.lower() for dep in manifest.get('depends', [])):
        if 'data' not in manifest or not any(
            'server_action' in f for f in manifest.get('data', [])
        ):
            errors.append(
                "Module uses AI dependencies but no AI server actions found"
            )

    # Check installable flag
    if not manifest.get('installable', True):
        errors.append("Module is marked as not installable")

    return errors


def validate_odoo_structure(module_path: Path) -> list[str]:
    """Validate Odoo module directory structure."""
    errors = []

    # Check required files
    for required_file in REQUIRED_FILES:
        file_path = module_path / required_file
        if not file_path.exists():
            errors.append(f"Missing required file: {required_file}")

    # Check README format
    readme_path = module_path / 'README.md'
    if readme_path.exists():
        content = readme_path.read_text()
        if len(content) < 100:
            errors.append("README.md is too short (< 100 chars)")

    # Check for at least one content directory
    has_content = any(
        (module_path / dir_name).exists()
        for dir_name in RECOMMENDED_DIRS
    )

    if not has_content:
        errors.append(
            f"Module should have at least one of: {RECOMMENDED_DIRS}"
        )

    # Check for OWL components structure (if using frontend)
    static_src = module_path / 'static' / 'src'
    if static_src.exists():
        has_owl_structure = any(
            (module_path / owl_dir).exists()
            for owl_dir in OWL_COMPONENT_STRUCTURE
        )
        if not has_owl_structure:
            errors.append(
                "Module has static/src but doesn't follow OWL structure. "
                f"Expected one of: {OWL_COMPONENT_STRUCTURE}"
            )

    # Check security folder
    security_path = module_path / 'security'
    if security_path.exists():
        has_ir_model_access = (security_path / 'ir.model.access.csv').exists()
        if not has_ir_model_access:
            errors.append(
                "security/ folder exists but no ir.model.access.csv found"
            )

    return errors


def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: validate_odoo19_structure.py <manifest_path>")
        sys.exit(1)

    manifest_path = Path(sys.argv[1])
    module_path = manifest_path.parent

    errors = []
    errors.extend(validate_manifest_19(manifest_path))
    errors.extend(validate_odoo_structure(module_path))

    if errors:
        print(f"\n❌ Validation failed for {module_path.name} (Odoo):")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    print(f"✅ Module {module_path.name} is Odoo compliant")
    sys.exit(0)


if __name__ == '__main__':
    main()