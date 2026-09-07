from pathlib import Path

from pipeline_validator.rules import check_no_spaces, check_scenes_folder_exists, check_version


def test_check_scenes_folder_exists_passes(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    scenes_folder = Path.cwd() / "scenes"
    scenes_folder.mkdir()
    violations = check_scenes_folder_exists(Path.cwd())
    assert violations == []

def test_check_version_passes():
    violations = check_version(Path("knight_v001.fbx"))
    assert violations == []

def test_check_version_fails():
    violations = check_version(Path("knight.fbx"))
    assert len(violations) == 1
    assert violations[0].rule_id == "VERSION_001"

def test_check_no_spaces_fails():
    violations = check_no_spaces(Path("bad knight_v001.fbx"))
    assert len(violations) == 1
    assert violations[0].rule_id == "NAME_001"