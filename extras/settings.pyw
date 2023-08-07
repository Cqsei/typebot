import tkinter as tk
from tkinter import ttk
import configparser

# Function to save the settings to the INI file
def save_settings():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'speed': speed_entry.get(),
        'time_delay': time_delay_entry.get(),
    }
    config['RANGE'] = {
        'range1': range1_entry.get(),
        'range2': range2_entry.get(),
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    status_label.config(text="Settings saved successfully!")

# Read the current settings from the INI file
config = configparser.ConfigParser()
config.read("config.ini")

# Create the main application window
root = tk.Tk()
root.title("Settings GUI")

# Set the width of the GUI window while specifying a placeholder height value
root.geometry("265x235")

# Create a custom style for bold text
style = ttk.Style()
style.configure('Bold.TLabel', font=('TkDefaultFont', 10, 'bold'))

# Create and pack the widgets
speed_label = ttk.Label(root, text="Speed:")
speed_label.pack()
speed_entry = ttk.Entry(root)
speed_entry.insert(0, config.getfloat('DEFAULT', 'speed', fallback=0.1))
speed_entry.pack()

time_delay_label = ttk.Label(root, text="Time Delay:")
time_delay_label.pack()
time_delay_entry = ttk.Entry(root)
time_delay_entry.insert(0, config.getfloat('DEFAULT', 'time_delay', fallback=5))
time_delay_entry.pack()

# Create a separate section for Advanced settings
advanced_frame = ttk.LabelFrame(root, text="Advanced - Do not edit")
advanced_frame.pack(padx=5, pady=5)

range1_label = ttk.Label(advanced_frame, text="Range 1:")
range1_label.pack()
range1_entry = ttk.Entry(advanced_frame)
range1_entry.insert(0, config.getfloat('RANGE', 'range1', fallback=0.1))
range1_entry.pack()

range2_label = ttk.Label(advanced_frame, text="Range 2:")
range2_label.pack()
range2_entry = ttk.Entry(advanced_frame)
range2_entry.insert(0, config.getfloat('RANGE', 'range2', fallback=0.3))
range2_entry.pack()

save_button = ttk.Button(root, text="Save Settings", command=save_settings)
save_button.pack()

status_label = ttk.Label(root, text="")
status_label.pack()

root.mainloop()
