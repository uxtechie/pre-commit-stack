#!/usr/bin/env python3
"""Check SQL syntax using sqlparse library.

This script validates SQL files for basic syntax errors.
"""

import sys
from pathlib import Path
from typing import List

try:
    import sqlparse
except ImportError:
    print("Error: sqlparse not installed. Run: pip install sqlparse")
    sys.exit(1)


def check_sql_file(filepath: str) -> tuple[bool, List[str]]:
    """Check a SQL file for syntax errors.

    Args:
        filepath: Path to SQL file to check

    Returns:
        Tuple of (is_valid, errors) where is_valid is True if no errors found
    """
    errors = []
    try:
        content = Path(filepath).read_text(encoding="utf-8")

        # Parse SQL content
        statements = sqlparse.parse(content)

        if not statements:
            errors.append(f"{filepath}: Empty or invalid SQL file")
            return False, errors

        # Check for basic syntax issues
        for idx, statement in enumerate(statements, 1):
            # Remove comments and whitespace
            stripped = statement.value.strip()
            if not stripped or stripped.startswith("--"):
                continue

            # Check for common SQL injection patterns (basic)
            dangerous_patterns = [
                "exec(",
                "execute(",
                "eval(",
                "';",
                '";',
            ]

            for pattern in dangerous_patterns:
                if pattern.lower() in stripped.lower():
                    errors.append(
                        f"{filepath}:{idx}: Potentially dangerous pattern "
                        f"'{pattern}' found"
                    )

        return len(errors) == 0, errors

    except UnicodeDecodeError:
        errors.append(f"{filepath}: File encoding error (expected UTF-8)")
        return False, errors
    except Exception as e:
        errors.append(f"{filepath}: Error parsing SQL: {e}")
        return False, errors


def main() -> int:
    """Main entry point for SQL syntax checking.

    Returns:
        Exit code (0 for success, 1 for errors found)
    """
    if len(sys.argv) < 2:
        print("Usage: check_sql_syntax.py <file1.sql> [file2.sql ...]")
        return 1

    all_valid = True
    for filepath in sys.argv[1:]:
        is_valid, errors = check_sql_file(filepath)
        if not is_valid:
            all_valid = False
            for error in errors:
                print(f"❌ {error}")
        else:
            print(f"✅ {filepath}: SQL syntax OK")

    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
