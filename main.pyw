import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os
import configparser

# Function to handle the "Play" button click event
def play_game():
    settings_file = "typebot.py"
    if os.path.exists(settings_file):
        os.system(f"start {settings_file}")  # Open the file using the default text editor
    else:
        print("Settings file not found.")

# Function to open the settings file in the default text editor
def open_settings():
    settings_file = "extras/settings.pyw"
    if os.path.exists(settings_file):
        os.system(f"start {settings_file}")  # Open the file using the default text editor
    else:
        print("Settings file not found.")

# Create the main application window
root = tk.Tk()
root.title("Typebot GUI")

root.geometry("280x330")

style = ttk.Style()
style.configure('Bold.TLabel', font=('TkDefaultFont', 12, 'bold'))

# Label for "TYPEBOT" text in bold
typebot_label = ttk.Label(root, text="TYPEBOT", style='Bold.TLabel')
typebot_label.pack(pady=5)

# Label for emergency exit instruction (split into two lines)
emergency_label = ttk.Label(root, text="WHEN YOU PRESS PLAY,\nPRESS CTRL+F8 TO EMERGENCY EXIT",
                            anchor='center', justify='center')
emergency_label.pack(pady=5)

# Load the logo image
logo_image = Image.open("extras/logo.png")
logo_image = logo_image.resize((150, 150))  # Resize the logo to 150x150 pixels
logo_photo = ImageTk.PhotoImage(logo_image)

# Create and pack the logo label
logo_label = ttk.Label(root, image=logo_photo)
logo_label.pack(pady=10)

# Create and pack the "Play" button with a larger size
play_button = ttk.Button(root, text="Play", command=play_game, width=20)
play_button.pack(pady=5, padx=20)

# Create and pack the "Settings" button with a larger size
settings_button = ttk.Button(root, text="Settings", command=open_settings, width=20)
settings_button.pack(pady=5, padx=20)

root.mainloop()
