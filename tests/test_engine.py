from pathlib import Path

from pipeline_validator.engine import run_rules


def test_run_rules_collects_violations():
    files = [
        Path("knight_v001.fbx"),
        Path("bad knight.fbx"),
    ]

    violations = run_rules(files)

    assert len(violations) == 2