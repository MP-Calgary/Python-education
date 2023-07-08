import PySimpleGUI as sg
import os
os.system('clear')

# Define the GUI layout
layout = [
    [sg.Text("Select pace unit:", font=("Helvetica", 16))],
    [sg.Radio("min/km", "pace_unit", key="unit_km", default=True, font=("Helvetica", 16)),
     sg.Radio("min/mile", "pace_unit", key="unit_mile", font=("Helvetica", 16))],
    [sg.Text("Enter pace in minutes:", font=("Helvetica", 16)),
     sg.Input(key="pace_min", size=(4, 1), font=("Helvetica", 16), enable_events=True)],
    [sg.Text("Enter pace in seconds:", font=("Helvetica", 16)),
     sg.Input(key="pace_sec", size=(4, 1), font=("Helvetica", 16), enable_events=True)],
    [sg.Button("Convert", key="convert_btn", font=("Helvetica", 16)), sg.Button("OK", font=("Helvetica", 16))],
    [sg.Text("", key="converted_pace", font=("Helvetica", 32), visible=False)]
]

# Create the window
window = sg.Window("Pace Input", layout)

# Function to convert the pace and update the window
def convert_pace():
    try:
        # Get the values entered by the user
        pace_min = int(values["pace_min"]) if values["pace_min"].isdigit() else 0
        pace_sec = int(values["pace_sec"]) if values["pace_sec"].isdigit() else 0

        # Convert pace to min:sec format
        total_sec = pace_min * 60 + pace_sec
        pace_min_sec = divmod(total_sec, 60)
        pace_min_sec_format = f"{pace_min_sec[0]}:{pace_min_sec[1]:02d}"

        # Convert pace to min/km or min/mile format
        if values["unit_km"]:
            pace_km = total_sec / 60 / (1 / 1.60934)  # Convert min/km to min/mile
            pace_km_min = int(pace_km)
            pace_km_sec = int((pace_km % 1) * 60)
            pace_km_format = f"{pace_km_min}:{pace_km_sec:02d}"
            window["converted_pace"].update(f"min/mile: {pace_km_format}", font=("Helvetica", 32), visible=True)
            # print("Converted pace: min/mile", pace_km_format)
        else:
            pace_mile = total_sec / 60 / (1 * 1.60934)  # Convert min/mile to min/km
            pace_mile_min = int(pace_mile)
            pace_mile_sec = int((pace_mile % 1) * 60)
            pace_mile_format = f"{pace_mile_min}:{pace_mile_sec:02d}"
            window["converted_pace"].update(f"min/km: {pace_mile_format}", font=("Helvetica", 32), visible=True)
            # print("Converted pace: min/km", pace_mile_format)

    except ValueError:
        sg.popup_error("Invalid input. Please enter numeric values for pace.")

# Event loop to process events
while True:
    event, values = window.read()

    # Check if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Convert button event
    if event == "convert_btn":
        convert_pace()

    # OK button event
    if event == "OK":
        break

# Print the entered values and pace unit
pace_min = int(values["pace_min"]) if values["pace_min"].isdigit() else 0
pace_sec = int(values["pace_sec"]) if values["pace_sec"].isdigit() else 0

print("Pace in minutes:", pace_min)
print("Pace in seconds:", pace_sec)
print("Pace unit:", "min/km" if values["unit_km"] else "min/mile")
print("Converted pace:", window["converted_pace"].DisplayText)  # Print converted pace from the window

# Close the window
window.close()
