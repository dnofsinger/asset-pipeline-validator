import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Violation:
    rule_id: str
    message: str
    file_path: Path

def check_version(file_path: Path) -> list[Violation]:
    if re.search(r"_v\d{3}", file_path.name):
        return []

    return [
        Violation(
            rule_id="VERSION_001",
            message="Filename must include a version like _v001.",
            file_path=file_path,
        )
    ]

def check_no_spaces(file_path: Path) -> list[Violation]:
    if " " not in file_path.name:
        return []

    return [
        Violation(
            rule_id="NAME_001",
            message="Filename must not contain spaces.",
            file_path=file_path,
        )
    ]
