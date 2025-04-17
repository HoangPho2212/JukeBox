import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import create_track_list_gui, PlaylistManager  # Import the function for Create Track List
from update_tracks import update_track_gui  # Import the function for Update Track Rating

# These functions should ONLY be called when the buttons are clicked
def create_track_list_clicked():
    print("Create Track List button clicked")  # Debug line to check if the button triggers the function
    status_lbl.configure(text="Create track button was clicked!")
    create_track_list_gui()

def update_tracks_clicked():
    print("Update Tracks button clicked")# Debug line to check if the button triggers the function
    status_lbl.configure(text="View Tracks button was clicked!")
    update_track_gui()

def view_tracks_clicked():
    print("View Tracks button clicked!")  # Debug line to track button click
    status_lbl.configure(text="View Tracks button was clicked!")
    # Open the TrackViewer in a new Toplevel window
    TrackViewer(tk.Toplevel(window))

# Set up the main window
window = tk.Tk()
window.geometry("370x150")
window.title("JukeBox")
window.configure(bg="lightblue")

fonts.configure()

header_lbl = tk.Label(window,bg="lightblue", text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Buttons that trigger the respective functions
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)  # View Tracks button only opens the window on click
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_list_clicked)  # Ensure this is only triggered on button click
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)  # Ensure this is only triggered on button click
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, bg='lightblue', text="status", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Ensure the mainloop() is only called once at the very end
window.mainloop()  # This should be the ONLY mainloop in the script
