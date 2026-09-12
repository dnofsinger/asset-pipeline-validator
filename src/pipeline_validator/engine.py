from pathlib import Path

from pipeline_validator.rules import (
    Violation,
    check_no_spaces,
    check_scenes_folder_exists,
    check_version,
)

DIRECTORY_RULES = [
    check_scenes_folder_exists,
]

FILE_RULES = [
    check_version,
    check_no_spaces,
]

def run_rules(directory: Path) -> list[Violation]:
    violations: list[Violation] = []

    for rule in DIRECTORY_RULES:
        violations.extend(rule(directory))

    for file_path in directory.rglob("*"):
        if file_path.is_file():
            for rule in FILE_RULES:
                violations.extend(rule(file_path))

    return violations