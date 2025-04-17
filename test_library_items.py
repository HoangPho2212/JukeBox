import pytest
from library_item import LibraryItem
import track_library as lib

# Test for creating a LibraryItem
def test_library_item_creation():
    track = LibraryItem("Shape of You", "Ed Sheeran", 4)
    assert track.name == "Shape of You"
    assert track.artist == "Ed Sheeran"
    assert track.rating == 4
    assert track.play_count == 0

# Test for updating rating
def test_rating_update():
    track = LibraryItem("Shape of You", "Ed Sheeran", 4)
    track.rating = 5
    assert track.rating == 5

# Test for incrementing play count
def test_play_count_increment():
    track = LibraryItem("Shape of You", "Ed Sheeran", 4)
    track.play_count += 1
    assert track.play_count == 1

# Test for getting track data (valid track)
def test_invalid_track_number():
    track_name = lib.get_name("invalid_track")
    assert track_name is None

# Test for getting track data (invalid track)
def test_valid_track_number():
    track_name = lib.get_name("01")
    assert track_name == "Another Brick in the Wall"

# Test for setting invalid rating
def test_set_rating_invalid():
    with pytest.raises(ValueError):
        lib.set_rating("01", 6)

# Test for incrementing play count
def test_increment_play_count():
    initial_count = lib.get_play_count("01")
    lib.increment_play_count("01")
    assert lib.get_play_count("01") == initial_count + 1
