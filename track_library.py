from library_item import LibraryItem


library = {}

library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4, "tracks_img/ChatGPT 01.png")
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5, "tracks_img/ChatGPT 02.png")
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2, "tracks_img/ChatGPT 03.png")
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1, "tracks_img/ChatGPT 04.png")
library["05"] = LibraryItem("Someone Like You", "Adele", 3, "tracks_img/ChatGPT 05.png" )
library["06"] = LibraryItem("Cheating on You", "Charlie Puth", 5, "tracks_img/ChatGPT 06.png")
library["07"] = LibraryItem("There's nothing holding me back", "Shaw Mendes", 4, "tracks_img/ChatGPT 07.png")
library["08"] = LibraryItem("Gia Nhu", "Soobin Hoang Son", 5,"tracks_img/ChatGPT 08.png")
library["09"] = LibraryItem("Old town road", "Lil Nas X", 4, "tracks_img/ChatGPT 09.png")

def get_track_by_name(track_name):
    for track in library.values():  # Assuming 'library' is a dictionary of track objects
        if track.name.lower() == track_name.lower():  # Case insensitive comparison
            return track
    return None  # Return None if the track is not found

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        if rating < 0 or rating > 5:
            raise ValueError("Ratting must in range 0 to 5")
        item = library[key]
        item.rating = rating
    except KeyError :
        return
    except ValueError as e:
        raise e


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
