#!/usr/bin/env python3
"""Check Python files for potential SQL injection vulnerabilities.

This script analyzes Python code (especially Odoo modules) for unsafe SQL
construction patterns that could lead to SQL injection attacks.
"""

import ast
import re
import sys
from pathlib import Path
from typing import List


class SQLInjectionChecker(ast.NodeVisitor):
    """AST visitor to detect SQL injection vulnerabilities."""

    def __init__(self, filepath: str):
        """Initialize checker with filepath."""
        self.filepath = filepath
        self.issues: List[str] = []

    def visit_Call(self, node: ast.Call) -> None:
        """Check function calls for SQL injection patterns."""
        # Check for cr.execute() calls (Odoo database cursor)
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "execute" and len(node.args) > 0:
                first_arg = node.args[0]

                # Check for string formatting in SQL
                if isinstance(first_arg, (ast.BinOp, ast.JoinedStr)):
                    # String concatenation or f-strings
                    self.issues.append(
                        f"{self.filepath}:{node.lineno}: "
                        "Potential SQL injection: "
                        "SQL string uses concatenation or f-string. "
                        "Use parameterized queries instead."
                    )
                elif isinstance(first_arg, ast.Call):
                    if isinstance(first_arg.func, ast.Attribute):
                        if first_arg.func.attr in ["format", "replace"]:
                            self.issues.append(
                                f"{self.filepath}:{node.lineno}: "
                                "Potential SQL injection: "
                                "SQL string uses .format() or .replace(). "
                                "Use parameterized queries with %s placeholders."
                            )

        self.generic_visit(node)


def check_python_file(filepath: str) -> tuple[bool, List[str]]:
    """Check a Python file for SQL injection vulnerabilities.

    Args:
        filepath: Path to Python file to check

    Returns:
        Tuple of (is_safe, issues) where is_safe is True if no issues found
    """
    try:
        content = Path(filepath).read_text(encoding="utf-8")

        # Quick regex check for common patterns
        issues = []

        # Pattern 1: String formatting in execute()
        pattern_format = re.compile(
            r'\.execute\(["\'].*?%(?!s).*?["\']', re.DOTALL
        )
        if pattern_format.search(content):
            issues.append(
                f"{filepath}: "
                "Detected string formatting in SQL execute() call. "
                "Use parameterized queries."
            )

        # Pattern 2: f-strings in SQL (very dangerous)
        pattern_fstring = re.compile(
            r'\.execute\(f["\'].*?\{.*?\}.*?["\']', re.DOTALL
        )
        if pattern_fstring.search(content):
            issues.append(
                f"{filepath}: "
                "CRITICAL: f-string used in SQL execute() call. "
                "This is a SQL injection vulnerability!"
            )

        # Pattern 3: String concatenation with +
        pattern_concat = re.compile(
            r'\.execute\([^)]*\+[^)]*\)', re.DOTALL
        )
        if pattern_concat.search(content):
            issues.append(
                f"{filepath}: "
                "String concatenation detected in SQL execute(). "
                "Use parameterized queries."
            )

        # AST-based deep analysis
        try:
            tree = ast.parse(content, filename=filepath)
            checker = SQLInjectionChecker(filepath)
            checker.visit(tree)
            issues.extend(checker.issues)
        except SyntaxError:
            # Skip files with syntax errors (other tools will catch this)
            pass

        return len(issues) == 0, issues

    except UnicodeDecodeError:
        return False, [f"{filepath}: File encoding error (expected UTF-8)"]
    except Exception as e:
        return False, [f"{filepath}: Error analyzing file: {e}"]


def main() -> int:
    """Main entry point for SQL injection checking.

    Returns:
        Exit code (0 for success, 1 for issues found)
    """
    if len(sys.argv) < 2:
        print("Usage: check_sql_injection.py <file1.py> [file2.py ...]")
        return 1

    all_safe = True
    for filepath in sys.argv[1:]:
        # Only check files likely to have SQL (skip test files for now)
        if "test" in filepath.lower() or "__init__" in filepath:
            continue

        is_safe, issues = check_python_file(filepath)
        if not is_safe:
            all_safe = False
            for issue in issues:
                print(f"❌ {issue}")

    return 0 if all_safe else 1


if __name__ == "__main__":
    sys.exit(main())
