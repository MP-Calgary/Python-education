import os
# clear the terminal 
os.system('clear')
import sys

# Add the directory containing the module to the module search path
sys.path.insert(0, '/opt/homebrew/lib/python3.11/site-packages')

import pandas as pd
from tabulate import tabulate

# adding MP_learn folder to the system path (this folder has the Python file called useful_functions, where I can import display_table)
sys.path.insert(0, '//Users/michaelparker/Dropbox (Personal)/MP_Python/MP_learn/')

# from useful_functions import display_table
from datetime import datetime

current_datetime = datetime.now() # Get the current date and time
formatted_datetime = current_datetime.strftime("%-d-%b-%Y %-I:%M:%S %p") # Format the date and time as d-mmm-yyyy h:mm:ss am/pm (without leading zero for the day or hour)
print("")
print("========================================")
print("")
print(formatted_datetime) # Print the formatted date and time
print("")
print("========================================")

#  set which file to load
my_file = 'parkland_export.csv'

if os.path.exists(my_file):

    # used for debugging, have a small set of fixed data
    # excel_data = [
    # ["Arishenkoff, Mark", 45, "29-May-78", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"],
    # ["Bachynski, Jordan", 33, "06-Sep-89", "Melchizedek", "Elder", "Expired", "Regular", "M", "Parkland Ward"],
    # ["Baker, Don", 76, "11-Oct-46", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Blomfield, Paul", 55, "21-Mar-68", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Brown, Courtney", 76, "29-Apr-47", "Melchizedek", "High Priest", "Active", "Regular", "M", "Parkland Ward"],
    # ["Brown, Lane", 65, "05-Feb-58", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"],
    # ["Chihaluca, Admir", 41, "18-Aug-81", "Melchizedek", "Elder", "Active", "Regular", "M", "Parkland Ward"]
    # ]

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

else:
    print(f"File '{my_file}' does not exist.")



# sheet_name = 'Harvest'
# column_indices = [1, 2, 3, 4, 7]  # read columns 1, 2, 3, 4, and 7

# # columns_data = [['Date', '2015/11/25', '2015/11/30', '2015/12/07', '2015/12/11', '2015/12/15'],
# #                 ['Client', 'RandP', 'GOA', 'Robots and Pencils', 'AHS', 'Decisive Farming'],
# #                 ['Project', 'r&p-robofactory-pm/ba guild', 'goa-rmas0049-firebans', 'sales-goa queens printer ministry', 'ahs-wait times-ios', 'decisive-scouting'],
# #                 ['Project Code', '013', '066', '112', '040', '095'],
# #                 ['Hours', 8.5, 6.5, 1.5, 3, 2]]

# if os.path.exists(file_path):

#     columns_data = read_excel_columns(file_path, sheet_name, column_indices)  # returns value into a list

#     transposed_data = zip(*columns_data)  # Transpose the list

#     # convert class zip to a list
#     transposed_list = list(transposed_data)

#     df = pd.DataFrame(transposed_list[1:], columns=transposed_list[0])
#     # print("Pandas list")
#     # print(df)
#     print()
#     print("List of first 5 rows in panda set")
#     print(df.head())
#     print()

#     # want to summarize the data, so it prints total hours by project code
#     hours_sum = df.groupby(['Project Code', 'Project'])['Hours'].sum().reset_index()
#     hours_sum_sorted = hours_sum.sort_values('Hours', ascending=False)

#     num_unique_project_codes = len(hours_sum_sorted)
#     output_list = []

#     for index, row in hours_sum_sorted.iterrows():
#         project_code = row['Project Code']
#         project = row['Project']
#         total_hours = row['Hours']
#         output_list.append((project_code, project, total_hours))

#     print("Code      Project                                 Total hours")
#     display_table(output_list)
#     print("Number of Unique Project Codes:", num_unique_project_codes)
#     print()

#     # Extract year from 'Date' column
#     df['Year'] = pd.to_datetime(df['Date']).dt.year

#     # Group by year and project code
#     grouped = df.groupby(['Year', 'Project Code'])

#     print("List out Project codes broken out by year")
#     print()

#     prev_year = None
#     for (year, project_code), group in grouped:
#         if year != prev_year:
#             if prev_year is not None:
#                 print()  # Print newline before starting the next year
#             print(f"Year: {year}")
#             prev_year = year

#         project_names = group['Project'].unique()
#         project_list = ', '.join(project_names)
#         total_hours = group['Hours'].sum()
#         print(f"Project Codes: {project_code}, Projects: {project_list}, Total Hours: {total_hours}")

#     print()  # Print newline after the last year

# else:
#     print("File: ", file_path, " does not exist.")