from pathlib import Path

from pipeline_validator.engine import run_rules


def test_run_rules_collects_violations(tmp_path: Path):
    (tmp_path / "knight_v001.fbx").touch()
    (tmp_path / "bad knight.fbx").touch()

    (tmp_path / "scenes").mkdir()

    violations = run_rules(tmp_path)

    assert len(violations) == 4