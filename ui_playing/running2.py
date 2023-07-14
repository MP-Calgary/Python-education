import PySimpleGUI as sg
import os
os.system('clear')

# Define the GUI layout for the "Unit Conversion" tab
unit_conversion_layout = [
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

# Define the GUI layout for the "Race Predictor" tab
race_predictor_layout = [
    [sg.Text("Predicted Pace (min:sec):", font=("Helvetica", 16))],
    [sg.Input(key="predicted_pace", size=(6, 1), font=("Helvetica", 16), enable_events=True)],
    [sg.Text("Distance (km):", font=("Helvetica", 16))],
    [sg.Input(key="distance", size=(6, 1), font=("Helvetica", 16), enable_events=True)],
    [sg.Button("Calculate", key="calculate_btn", font=("Helvetica", 16))],
    [sg.Text("", key="race_time", font=("Helvetica", 32), visible=False)],
    [sg.Button("OK", font=("Helvetica", 16), key="ok_btn")]
]

interval_layout = [
    [sg.Text('Interval Pace (min:sec):'), sg.Input(key='-PACE-', size=(6, 1))],
    [sg.Text('Distance:'), sg.Combo(['100m', '200m', '400m', '600m', '800m', '1000m', '1600m'], key='-DISTANCE-', size=(6, 1))],
    [sg.Button('Convert2', size=(10, 1)), sg.Button('Ok2', size=(10, 1))],
    [sg.Text("", key="Interval_time", font=("Helvetica", 32), visible=False)]
]


# Define the main layout with the tab group
layout = [
    [sg.TabGroup([[sg.Tab("Unit Conversion", unit_conversion_layout),
                   sg.Tab("Race Predictor", race_predictor_layout),
                   sg.Tab("Interval calculator", interval_layout)]],
                 font=("Helvetica", 16))]
]

# set that the calulations have not been run
tab1_result = [False]
tab2_result = [False]
tab3_result = [False]

# Create the window
window = sg.Window("Running calculations", layout)

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
            convert_from = 'min/km'
            convert_to = 'min/mile'
            pace_km = total_sec / 60 / (1 / 1.60934)  # Convert min/km to min/mile
            pace_km_min = int(pace_km)
            pace_km_sec = int((pace_km % 1) * 60)
            pace_km_format = f"{pace_km_min}:{pace_km_sec:02d}"
            pace_formatted = pace_km_format
            window["converted_pace"].update(f"min/mile: {pace_formatted}", font=("Helvetica", 32), visible=True)
        else:
            convert_from = 'min/mile'
            convert_to = 'min/km'
            pace_mile = total_sec / 60 / (1 * 1.60934)  # Convert min/mile to min/km
            pace_mile_min = int(pace_mile)
            pace_mile_sec = int((pace_mile % 1) * 60)
            pace_mile_format = f"{pace_mile_min}:{pace_mile_sec:02d}"
            pace_formatted = pace_mile_format
            window["converted_pace"].update(f"min/km: {pace_formatted}", font=("Helvetica", 32), visible=True)

        return_list = [True, convert_from, convert_to, pace_min, pace_sec, pace_formatted ]
        return return_list

    except ValueError:
        sg.popup_error("Invalid input. Please enter numeric values for pace.")
        return_list = [False, '', '', 0, 0, '' ]
        return return_list

# Function to calculate the race time and update the window
def calculate_race_time():
    try:
        # Get the values entered by the user
        predicted_pace = values["predicted_pace"]
        distance = float(values["distance"]) if values["distance"].replace(".", "", 1).isdigit() else 0.0

        # Calculate the race time
        pace_min, pace_sec = predicted_pace.split(":")
        total_sec_per_km = int(pace_min) * 60 + int(pace_sec)
        race_time_sec = total_sec_per_km * distance

        # Convert the race time to hours, minutes, and seconds
        race_time_hour, remainder = divmod(race_time_sec, 3600)
        race_time_min, race_time_sec = divmod(remainder, 60)

        # Format the race time as "h:mm:ss"
        race_time_format = f"{int(race_time_hour)}:{int(race_time_min):02d}:{int(race_time_sec):02d}"

        # Update the window with the race time
        window["race_time"].update(f"Race Time: {race_time_format}", font=("Helvetica", 32), visible=True)

        return_list = [True, predicted_pace, distance, race_time_format]

        return return_list

    except ValueError:
        sg.popup_error("Invalid input. Please enter numeric values for predicted pace and distance.")
        return_list = [False, 0, 0, '' ]
        return return_list

def calc_time():
    try:
        interval_pace = values['-PACE-']
        input_distance = values['-DISTANCE-']
        distance = int(input_distance[:-1])
        minutes, seconds = map(int, interval_pace.split(':'))
        total_seconds = minutes * 60 + seconds
        pace_per_meter = total_seconds / 1000  # Pace per meter
        time = pace_per_meter * float(distance)
        minutes = int(time // 60)
        seconds = int(time % 60)
        window["Interval_time"].update(f"Time: {minutes} min {seconds} sec to go {distance} meters.",
                                    font=("Helvetica", 32), visible=True)
        
        return_list = [True, interval_pace, input_distance, minutes, seconds]
        return return_list
    
    except ValueError:
        sg.popup_error("Invalid input. Please enter numeric values for pace and distance.")
        return_list = [False, '', '', 0, 0]
        return return_list

# Event loop to process events
while True:
    event, values = window.read()

    # Check if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Convert button event in "Unit Conversion" tab
    if event == "convert_btn":
        tab1_result = convert_pace()

    # Calculate button event in "Race Predictor" tab
    if event == "calculate_btn":
        tab2_result = calculate_race_time()

    # OK button event
    if event == "OK":
        break

    # OK button (2nd tab) event
    if event == "ok_btn":
        break

    # OK button (3nd tab) event
    if event == "Ok2":
        break

    # convert button (3nd tab) event
    if event == "Convert2":
         tab3_result = calc_time()
    
# Confirm tab 1 ran (this is in index 0), and then print the last results from it
if tab1_result[0] == True:
    print(f"Converted {tab1_result[3]}:{tab1_result[4]} {tab1_result[1]} to {tab1_result[5]} {tab1_result[2]}")

# Confirm tab 2 ran (this is in index 0), and then print the last results from it
if tab2_result[0] == True:
    print(f"With a pace of {tab2_result[1]} min/km, for a distance of {tab2_result[2]} km, it will take {tab2_result[3]} (h:min:sec) to finish")

# Confirm tab 3 ran (this is in index 0), and then print the last results from it
if tab3_result[0] == True:
    print(f"With a pace of {tab3_result[1]} min/km, for a distance of {tab3_result[2]}, it will take {tab3_result[3]}:{tab3_result[4]} (min:sec) to finish")

# Close the window
window.close()
