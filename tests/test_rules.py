from pipeline_validator.rules import has_valid_version


# def test_check_version():
#     assert has_valid_version("knight.fbx")

def test_valid_version():
    assert has_valid_version("knight_v001.fbx")

def test_invalid_version():
    assert not has_valid_version("knight.fbx")