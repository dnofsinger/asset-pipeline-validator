from pathlib import Path
from pipeline_validator.rules import Violation, check_version, check_no_spaces

RULES = [
    check_version,
    check_no_spaces,
]

def run_rules(file_paths: list[Path]) -> list[Violation]:
    violations: list[Violation] = []

    for file_path in file_paths:
        for rule in RULES:
            violations.extend(rule(file_path))

    return violations