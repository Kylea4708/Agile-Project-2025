import pytest
from models import Genre

# tests regular
def test_genre():
    genre = Genre (
        id = 1,
        name = "genre"
    )

    assert genre.id == 1
    assert genre.name == "genre"

# tests invalid id
def test_id_not_int():
    genre = Genre (
        id = ""
    )

    assert genre.id != int()

    with pytest.raises(TypeError):
        genre.id("1")


# test invalid name
def test_invalid_name():
    genre = Genre (
        name = 1
    )

    assert genre.name != str()

    with pytest.raises(TypeError):
        genre.name(1)

# test null name
def test_null_name():
    genre = Genre (
        name = None
    )

    assert genre.name is None

    with pytest.raises(TypeError):
        genre.name(None)