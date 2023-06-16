import os
# clear the terminal 
os.system('clear')
import sys

# Add the folder to the system path containing the path to where package tabulate exists
sys.path.insert(0, '/opt/homebrew/lib/python3.11/site-packages')

import pandas as pd
from tabulate import tabulate

from datetime import datetime

current_datetime = datetime.now() # Get the current date and time
formatted_datetime = current_datetime.strftime("%-d-%b-%Y %-I:%M:%S %p") # Format the date and time as d-mmm-yyyy h:mm:ss am/pm (without leading zero for the day or hour)
print("")
print("========================================")
print(formatted_datetime) # Print the formatted date and time
print("========================================")

#  set which file to load
my_file = 'parkland_export.csv'

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

    # Filter the DataFrame based on 'Gender' and 'Priesthood'
    filtered_data = excel_data[(excel_data['Gender'] == 'M') & (excel_data['Priesthood'] == 'Melchizedek')]

    # Sort the filtered DataFrame by age
    sorted_data = filtered_data.sort_values('Age')

    # Convert the sorted DataFrame to a list of lists
    table_data = sorted_data.values.tolist()

    # Print the table using tabulate
    print(tabulate(table_data, headers=sorted_data.columns, tablefmt='pretty'))

    # Print the total number of rows
    print(f"Total Rows: {len(table_data)}")

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

    # ------------------
    # Filter the DataFrame based on 'Gender', 'Priesthood', and 'Temple Recommend Status'
    filtered_data = excel_data[
        (excel_data['Gender'] == 'M') &
        (excel_data['Priesthood'] == 'Melchizedek') &
        (excel_data['Temple Recommend Status'] == 'Active')
    ]

    # Sort the filtered DataFrame by age
    sorted_data = filtered_data.sort_values('Age')

    # Convert the sorted DataFrame to a list of lists
    table_data = sorted_data.values.tolist()

    # Print the table using tabulate
    print("Data where Temple Recommend Status = 'Active' ")
    print(tabulate(table_data, headers=sorted_data.columns, tablefmt='pretty'))

    # Print the total number of rows
    total_rows = len(table_data)
    print(f"Total Rows: {total_rows}")

    # Calculate counts of rows for age groups by 5
    age_bins = range(0, sorted_data['Age'].max() + 6, 5)
    age_groups = pd.cut(sorted_data['Age'], bins=age_bins, right=False)
    age_counts = sorted_data.groupby(age_groups).size().reset_index(name='Count')

    # Create age group labels aligned with the bins
    age_group_labels = [f'{age_bins[i]}-{age_bins[i+1]-1}' for i in range(len(age_bins)-1)]
    age_group_counts = age_counts.values.tolist()

    # Print the counts for age groups
    print("Counts of Rows for Age Groups Temple Recommend Status = 'Active'")
    print(tabulate(age_group_counts, headers=['Age Group', 'Count'], tablefmt='pretty'))

    # Calculate and print the total count of rows
    total_count = age_counts['Count'].sum()
    print(f"Total Count where Temple Recommend Status = 'Active': {total_count}")

else:
    print(f"File '{my_file}' does not exist.")