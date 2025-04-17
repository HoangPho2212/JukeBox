import tkinter as tk
import font_manager as font
import track_library as lib
import json

class PlaylistManager:
    def __init__(self, track_list_text, result_lbl):
        self.playlist = []
        self.track_list_text = track_list_text
        self.result_lbl = result_lbl

    def save_playlist(self):
        with open('playlist.json', 'w') as f:
            json.dump(self.playlist, f)
        print("Playlist saved")

    def load_playlist(self):
        with open('playlist.json', 'r') as f:
            load_playlist = json.load(f)
            self.playlist = []
            for track_name in load_playlist:
                track = lib.get_track_by_name(track_name)
                if track:
                    self.playlist.append(track)
        print("Playlist loaded")
        self.update_playlist_display()

    def update_playlist_display(self):
        self.track_list_text.delete(1.0, tk.END)
        for track in self.playlist:
            self.track_list_text.insert(tk.END, track.name + "\n")

    def add_track(self, track_number):
        if not track_number.isdigit():
            self.result_lbl.config(text="Invalid track number. Please enter a numeric value")
            return
        track_name = lib.get_name(track_number)
        if track_name:
            self.track_list_text.insert(tk.END, track_name + "\n")
            self.result_lbl.config(text=f"Track '{track_name}' added to playlist!")
            self.playlist.append(track_name)
        else:
            self.result_lbl.config(text=f"Track {track_number} not found")

def create_track_list_gui():
    # Create the main window for the Create Track List interface
    window = tk.Tk()
    window.geometry("400x650")
    window.title("Create Track List")
    font.configure()
    window.resizable(False, False)

    # Create the header label
    header_lbl = tk.Label(window, text="Create Your Playlist", font=("Helvetica", 16, "bold"))
    header_lbl.grid(row=0, column=0, columnspan= 2, pady=10)

    # Create input for track number
    track_num_lbl = tk.Label(window, text="Enter Track Number:")
    track_num_lbl.grid(row=1, column=0, pady=20)
    track_num_entry = tk.Entry(window, width=40)
    track_num_entry.grid(row=2, column=0, columnspan= 2, padx=10)

    # Add track button with blue color
    def add_track():
        track_number = track_num_entry.get()
        playlist_manager.add_track(track_number)

    add_track_btn = tk.Button(window, text="Add Track to Playlist", width=20, command=add_track, bg="#1F6CDD", fg="white")
    add_track_btn.grid(row=3, column=0, padx=10, pady=10)

    play_list_lbl = tk.Label(window, text="Playlist: ")
    play_list_lbl.grid(row= 4, column= 0)

    # Create text area for playlist
    track_list_text = tk.Text(window, height=10, width= 40)
    track_list_text.grid(row=5, column=0,columnspan= 2, padx= 10, pady=10)

    # Create playlist manager instance
    result_lbl = tk.Label(window, text="Track details will appear here", font=("Helvetica", 10), fg="#474043")
    result_lbl.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    playlist_manager = PlaylistManager(track_list_text, result_lbl)

    # Create play, reset, save buttons
    def play_playlist():
        tracks = track_list_text.get(1.0, tk.END).split("\n")
        for track in tracks:
            if track.strip():
                track_number = [key for key, value in lib.library.items() if value.name == track.strip()]
                if track_number:
                    lib.increment_play_count(track_number[0])
        result_lbl.config(text="Playlist played successfully!")

    def reset_playlist():
        track_list_text.delete(1.0, tk.END)
        result_lbl.config(text="Playlist reset!")

    save_btn = tk.Button(window, text="Save Playlist", command=playlist_manager.save_playlist)
    save_btn.grid(row= 7, column=0, padx=10, pady=10)

    play_btn = tk.Button(window, text="Play Playlist", command=play_playlist)
    play_btn.grid(row=6, column=0, padx=10, pady=10 )

    reset_btn = tk.Button(window, text="Reset Playlist", command=reset_playlist)
    reset_btn.grid(row=6, column=1)

    # Load playlist button
    load_btn = tk.Button(window, text="Load Playlist", command=playlist_manager.load_playlist)
    load_btn.grid(row=3, column=1)


create_track_list_gui()
