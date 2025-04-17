import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from tkinter import PhotoImage


class TrackViewer:
    def __init__(self, window):
        self.window = window
        window.geometry("950x550")
        window.title("View Tracks")
        window.configure(bg="lightblue")

        # Initialize widgets
        self.search_entry = tk.Entry(window)
        self.search_entry.grid(row=3, column=1, padx=10, pady=10)

        self.search_btn = tk.Button(window, text="Search", command=self.search_tracks)
        self.search_btn.grid(row=4, column=1, padx=10, pady=10)

        self.sort_by_rating_btn = tk.Button(window, text="sort by Rating", command=self.sort_by_rating)
        self.sort_by_rating_btn.grid(row=2, column=2, padx=10, pady=10)

        self.list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        self.list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        self.enter_lbl = tk.Label(window, text="Enter Track Number")
        self.enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        self.check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        self.check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=40, height=12, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

    def search_tracks(self):
        search_term = self.search_entry.get().lower()
        filtered_tracks = [track for track in lib.library.values() if
                           search_term in track.name.lower() or search_term in track.artist.lower()]
        filtered_tracks_text = "\n".join([f"{track.name} by {track.artist}" for track in filtered_tracks])
        self.set_text(self.track_txt, filtered_tracks_text)

    def sort_by_rating(self):
        sorted_tracks = sorted(lib.library.values(), key=lambda x: x.rating, reverse=True)
        self.display_sorted_tracks(sorted_tracks)

    def display_sorted_tracks(self, sorted_tracks):
        track_text = '\n'.join([f"{track.name} by {track.artist} (Rating: {track.rating})" for track in sorted_tracks])
        self.set_text(self.track_txt, track_text)

    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            image_path = lib.library[key].image_path
            track_details = f"{name}\n{artist}\nRating: {rating}\nPlay count: {play_count}"
            self.set_text(self.track_txt, track_details, image_path)
        else:
            self.set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        self.set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def set_text(self, text_area, content, image_path=None):
        text_area.delete("1.0", tk.END)
        text_area.insert(1.0, content)

        if image_path:
            try:
                if hasattr(self, 'image_label') and self.image_label:
                    self.image_label.destroy()  # remove old image if it exists

                track_image = PhotoImage(file=image_path, master=self.window)
                self.image_label = tk.Label(self.window, image=track_image)
                self.image_label.image = track_image
                self.image_label.grid(row=2, column=3, padx=10, pady=10)
                self.image_label.config(width=200, height=200)
            except Exception as e:
                print(f"Error loading image: {e}")

