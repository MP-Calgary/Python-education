import os

# Clear the terminal
os.system('clear')

def km_to_miles(minutes, seconds):
    # Convert minutes and seconds to total seconds per kilometer
    total_seconds = (minutes * 60) + seconds

    # Convert seconds per kilometer to seconds per mile
    seconds_per_mile = total_seconds * 1.60934

    # Convert seconds per mile to minutes and seconds
    minutes_per_mile = int(seconds_per_mile // 60)
    seconds_per_mile = int(seconds_per_mile % 60)

    return minutes_per_mile, seconds_per_mile


def miles_to_km(minutes, seconds):
    # Convert minutes and seconds to total seconds per mile
    total_seconds = (minutes * 60) + seconds

    # Convert seconds per mile to seconds per kilometer
    seconds_per_km = total_seconds / 1.60934

    # Convert seconds per kilometer to minutes and seconds
    minutes_per_km = int(seconds_per_km // 60)
    seconds_per_km = int(seconds_per_km % 60)

    return minutes_per_km, seconds_per_km


conversion_direction = None

while conversion_direction != '0':
    # Prompt the user for the conversion direction
    print("Enter ")
    print("'0' to quit: ")
    print("'1' to convert min/km to min/miles,")
    print("'2' to convert min/miles to min/km,")
    conversion_direction = input("Value: ")

    if conversion_direction == '0':
        print("Goodbye!")
    elif conversion_direction in ['1', '2']:
        if conversion_direction == '1':
            min_prompt = "Enter minutes per km: "
            sec_prompt = "Enter the additional seconds per km: "
        elif conversion_direction == '2':
            min_prompt = "Enter minutes per mile: "
            sec_prompt = "Enter the additional seconds per mile: "

        while True:
            try:
                minutes = int(input(min_prompt))
                seconds = int(input(sec_prompt))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value for minutes and seconds.")

        if conversion_direction == '1':
            print()
            # Convert from metric to imperial (km to miles)
            minutes_per_mile, seconds_per_mile = km_to_miles(minutes, seconds)
            print()
            print(f"{minutes} min {seconds} sec /km = "
                  f"{minutes_per_mile} min {seconds_per_mile} sec /mile.")
            print()
            # quit program
            conversion_direction = '0'
        elif conversion_direction == '2':
            print()
            # Convert from imperial to metric (miles to km)
            minutes_per_km, seconds_per_km = miles_to_km(minutes, seconds)
            print()
            print(f"{minutes} min {seconds} sec /mile = "
                  f"{minutes_per_km} min {seconds_per_km} sec /km.")
            print()
            conversion_direction = '0'
    else:
        print("Invalid input. Please enter '1', '2', or '0' to select the conversion direction.")
