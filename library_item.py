class LibraryItem:
    def __init__(self, name, artist, rating=0, image_path=None):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.play_count = 0
        self.image_path = image_path

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
