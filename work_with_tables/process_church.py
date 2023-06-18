import os
# clear the terminal 
os.system('clear')
import sys

# Add the folder to the system path containing the path to where package tabulate exists
sys.path.insert(0, '/opt/homebrew/lib/python3.11/site-packages')

import pandas as pd
from tabulate import tabulate

from datetime import datetime

def prompt_user_which_filter():
    options = {
        0: "Quit program",
        1: "Filter data based on 'Gender' = 'M' & 'Priesthood' = 'Melchizedek'",
        2: "Filter data based on 'Gender' = 'M' & 'Priesthood' = 'Melchizedek' & 'Temple Recommend Status' = 'Active'",
        3: "Filter data based on 'Gender' = 'F'",
        4: "Filter data based on 'Gender' = 'F' & 'Temple Recommend Type' = 'Regular' & 'Temple Recommend Status' = 'Active'"
    }

    while True:
        print("Select an option:")
        for key, value in options.items():
            print(f"{key} - {value}")

        try:
            choice = int(input("Enter your choice: "))
            if choice in options:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical choice.")

def prompt_user_which_report():
    options = {
        0: "Quit program",
        1: "Detailed list",
        2: "Counts by age group"
    }

    while True:
        print("Select an option:")
        for key, value in options.items():
            print(f"{key} - {value}")

        try:
            choice = int(input("Enter your choice: "))
            if choice in options:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical choice.")
        
current_datetime = datetime.now() # Get the current date and time
formatted_datetime = current_datetime.strftime("%-d-%b-%Y %-I:%M:%S %p") # Format the date and time as d-mmm-yyyy h:mm:ss am/pm (without leading zero for the day or hour)
print("")
print("========================================")
print(formatted_datetime) # Print the formatted date and time
print("========================================")

#  set which file to load
# my_file = 'parkland_export.csv'
# my_file = 'queensland_export.csv'
# my_file = 'midnapore_export.csv'
my_file = 'sundance_export.csv'

if os.path.exists(my_file):

    # used for debugging, have a small set of fixed data
    # ----
    # sample_data = [
    # ["Arishenkoff, Mark", 45, "29-May-78", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"],
    # ["Bachynski, Jordan", 33, "06-Sep-89", "Melchizedek", "Elder", "Expired", "Regular", "M", "Parkland Ward"],
    # ["Baker, Don", 76, "11-Oct-46", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Blomfield, Paul", 55, "21-Mar-68", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Brown, Courtney", 76, "29-Apr-47", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Brown, Lane", 65, "05-Feb-58", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"],
    # ["Chihaluca, Admir", 41, "18-Aug-81", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"]
    # ]
    # columns = ["Preferred Name", "Age", "Birth Date", "Priesthood", "Priesthood office",
    #        "Temple Recommend Status", "Temple Recommend Type", "Gender", "Unit"]

    # excel_data = pd.DataFrame(sample_data, columns=columns)
    # ---- end of debugging data

    # import csv into a pandas dataframe
    excel_data = pd.read_csv(my_file)

    # set col names
    excel_data.columns = ["Preferred Name", "Age", "Birth Date", "Priesthood", "Priesthood office",
                      "Temple Recommend Status", "Temple Recommend Type", "Gender", "Unit"]
    
    # print(excel_data)

    # prompt user for what kind of filter they want
    filter_choice = prompt_user_which_filter()
    print()
    print()

    if filter_choice == 0:
        # Quit program
        quit()
    elif filter_choice == 1:
        # Filter data based on 'Gender' = 'M' & 'Priesthood' = 'Melchizedek'
        filtered_data = excel_data[
            (excel_data['Gender'] == 'M') &
            (excel_data['Priesthood'] == 'Melchizedek')
        ]
    elif filter_choice == 2:
        # Filter data based on 'Gender' = 'M', 'Priesthood' = 'Melchizedek', and 'Temple Recommend Status' = 'Active'
        filtered_data = excel_data[
            (excel_data['Gender'] == 'M') &
            (excel_data['Priesthood'] == 'Melchizedek') &
            (excel_data['Temple Recommend Status'] == 'Active')
        ]
    elif filter_choice == 3:
        # Filter data based on 'Gender' = 'F'
        filtered_data = excel_data[
            (excel_data['Gender'] == 'F') 
        ]
    elif filter_choice == 4:
        # Filter data based on 'Gender' = 'F', and 'Temple Recommend Status' = 'Active'
        filtered_data = excel_data[
            (excel_data['Gender'] == 'F') &
            (excel_data['Temple Recommend Type'] == 'Regular') & 
            (excel_data['Temple Recommend Status'] == 'Active')
        ]


    report_choice = prompt_user_which_report()


    # # Filter the DataFrame based on 'Gender' and 'Priesthood'
    # filtered_data = excel_data[
    #     (excel_data['Gender'] == 'M') &
    #     (excel_data['Priesthood'] == 'Melchizedek')
    # ]

    # Sort the filtered DataFrame by age
    sorted_data = filtered_data.sort_values('Age')

    # Convert the sorted DataFrame to a list of lists
    table_data = sorted_data.values.tolist()

    if report_choice == 1:
        # Print the table using tabulate
        print(tabulate(table_data, headers=sorted_data.columns, tablefmt='pretty'))

        # Print the total number of rows
        total_rows = len(table_data)
        print(f"Total Rows: {total_rows}")
    elif report_choice == 2:

        # Calculate counts of rows for age groups by 5
        age_bins = range(0, sorted_data['Age'].max() + 6, 5)
        age_groups = pd.cut(sorted_data['Age'], bins=age_bins, right=False)
        age_counts = sorted_data.groupby(age_groups).size().reset_index(name='Count')

        # Create age group labels aligned with the bins
        age_group_labels = [f'{age_bins[i]}-{age_bins[i+1]-1}' for i in range(len(age_bins)-1)]
        age_group_counts = age_counts.values.tolist()

        # Print the counts for age groups
        print('\nCounts of Rows for Age Groups:')
        print(tabulate(age_group_counts, headers=['Age Group', 'Count'], tablefmt='pretty'))

        # Calculate and print the total count of rows
        total_count = age_counts['Count'].sum()
        print(f"Total Count: {total_count}")
        print("\n\n")

else:
    print(f"File '{my_file}' does not exist.")