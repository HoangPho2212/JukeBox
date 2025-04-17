import tkinter as tk
import font_manager as font
import track_library as lib

def update_track_gui():
    window = tk.Tk()
    window.geometry("400x350")
    window.title("Update Track Rating")
    window.resizable(False, False)
    font.configure()

    # Header
    header_lbl = tk.Label(window, text="Update Track Rating", font=("Helvetica", 16, "bold"))
    header_lbl.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Input field for track number
    track_num_lbl = tk.Label(window, text="Enter Track Number:", font=("Helvetica", 12))
    track_num_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    track_num_entry = tk.Entry(window, font=("Helvetica", 12), width=20)
    track_num_entry.grid(row=1, column=1, padx=10, pady=10)

    # Input field for new rating
    rating_lbl = tk.Label(window, text="Enter New Rating (0-5):", font=("Helvetica", 12))
    rating_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    rating_entry = tk.Entry(window, font=("Helvetica", 12), width=20)
    rating_entry.grid(row=2, column=1, padx=10, pady=10)

    # Result label for feedback
    result_lbl = tk.Label(window, text="Track details will appear here", font=("Helvetica", 10), fg="#474043")
    result_lbl.grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    # Function to update the track rating
    def update_rating():
        try:
            track_number = track_num_entry.get()
            new_rating = int(rating_entry.get())
            if new_rating < 0 or new_rating > 5:
                raise ValueError("Rating must be in range 0 to 5.")
            lib.set_rating(track_number, new_rating) # Update the track rating
            track_name = lib.get_name(track_number)
            track_detail = f"Track: {track_name}\nNew Rating: {new_rating}\nPlays: {lib.get_play_count(track_number)}"
            result_lbl.config(text=track_detail, fg="#28a745")  # Success message in green
        except ValueError as e:
            result_lbl.config(text=f"Error: {e}", fg="#dc3545")  # Error message in red
        except Exception as e:
            result_lbl.config(text=f"Track not found or invalid input.\n{e}", fg="#dc3545")

    # Update Rating button
    update_rating_btn = tk.Button(window, text="Update Rating", command=update_rating, bg="#1F6CDD", fg="white", width=20)
    update_rating_btn.grid(row=3, column=0, columnspan=2, padx=20, pady=20)


update_track_gui()
