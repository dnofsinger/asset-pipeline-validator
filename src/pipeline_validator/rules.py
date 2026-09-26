import re
from dataclasses import dataclass
from pathlib import Path
from pipeline_validator.constants import RuleName


@dataclass
class Rule:
    ruleName: RuleName
    ruleDesc: str
    rulePass: bool

@dataclass
class Violation:
    rule_id: str
    message: str
    file_path: Path

def check_scenes_folder_exists(file_path: Path) -> list[Violation]:
    # Check to see if the scenes folder is a subfolder of the given file_path.
    # If it is, return an empty list. If not, return a Violation.
    scenes_folder = file_path / "scenes"

    if file_path.is_dir() and scenes_folder.is_dir():
        return []

    return [
        Violation(
            rule_id=RuleName.SCENES_FOLDER,
            message="The 'scenes' folder must exist.",
            file_path=file_path,
        )
    ]

def check_textures_folder_exists(file_path: Path) -> list[Violation]:
    # Check to see if the textures folder is a subfolder of the given file_path.
    # If it is, return an empty list. If not, return a Violation.
    textures_folder = file_path / "textures"

    if file_path.is_dir() and textures_folder.is_dir():
        return []

    return [
        Violation(
            rule_id=RuleName.TEXTURES_FOLDER,
            message="The 'textures' folder must exist.",
            file_path=file_path,
        )
    ]

def check_exports_folder_exists(file_path: Path) -> list[Violation]:
    # Check to see if the textures folder is a subfolder of the given file_path.
    # If it is, return an empty list. If not, return a Violation.
    exports_folder = file_path / "exports"

    if file_path.is_dir() and exports_folder.is_dir():
        return []

    return [
        Violation(
            rule_id=RuleName.EXPORTS_FOLDER,
            message="The 'exports' folder must exist.",
            file_path=file_path,
        )
    ]

def check_version(file_path: Path) -> list[Violation]:
    if re.search(r"_v\d{3}", file_path.name):
        return []

    return [
        Violation(
            rule_id=RuleName.VERSION,
            message="File name must include a version like _v001.",
            file_path=file_path,
        )
    ]

def check_no_spaces(file_path: Path) -> list[Violation]:
    if " " not in file_path.name:
        return []

    return [
        Violation(
            rule_id=RuleName.NO_SPACES,
            message="Filename must not contain spaces.",
            file_path=file_path,
        )
    ]
