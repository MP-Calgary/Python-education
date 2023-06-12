import os
# clear the terminal 
os.system('clear')

from datetime import datetime

current_datetime = datetime.now() # Get the current date and time
formatted_datetime = current_datetime.strftime("%-d-%b-%Y %-I:%M:%S %p") # Format the date and time as d-mmm-yyyy h:mm:ss am/pm (without leading zero for the day or hour)
print("")
print("========================================")
print("")
print(formatted_datetime) # Print the formatted date and time
print("")
print("========================================")


import pylightxl as xl

def read_excel_columns(file_path, sheet_name, column_indices):
    workbook = xl.readxl(file_path)
    sheet = workbook.ws(sheet_name)

    columns_data = [[] for _ in range(len(column_indices))]
    for row in sheet.rows:
        for i, column_index in enumerate(column_indices):
            if row:
                cell_value = row[column_index - 1]  # Adjust the column index by subtracting 1
                columns_data[i].append(cell_value)

    return columns_data

# Usage example
file_path = 'small_test_harvest.xlsx'
sheet_name = 'Harvest'
column_indices = [1, 2, 3, 4, 7]  # Assuming you want to read columns 1, 2, 3, 4, and 7

# columns_data = [['Date', '2015/11/25', '2015/11/30', '2015/12/07', '2015/12/11', '2015/12/15'],
#                 ['Client', 'RandP', 'GOA', 'Robots and Pencils', 'AHS', 'Decisive Farming'],
#                 ['Project', 'r&p-robofactory-pm/ba guild', 'goa-rmas0049-firebans', 'sales-goa queens printer ministry', 'ahs-wait times-ios', 'decisive-scouting'],
#                 ['Project Code', '013', '066', '112', '040', '095'],
#                 ['Hours', 8.5, 6.5, 1.5, 3, 2]]

columns_data = read_excel_columns(file_path, sheet_name, column_indices)  # returns value into a list

print("The original list")
print()
print("the data type of columns_data is: ", type(columns_data))
print()
print(columns_data)
print()

print("The list in excel tabular format")
print()
# Calculate the maximum width for each column
column_widths = [max(len(str(row[i])) for row in columns_data) for i in range(len(columns_data[0]))]

# Print the data rows with justified columns
for row in zip(*columns_data):
    formatted_row = [str(element).ljust(column_widths[i]) for i, element in enumerate(row)]
    print(' | '.join(formatted_row))

print()
print("The list in transposed format")
print()

transposed_data = zip(*columns_data)  # Transpose the list

# Get the maximum width of each column
max_widths = [max(len(str(element)) for element in column) for column in transposed_data]

hours_sum = 0.0  # Variable to keep track of the sum of Hours

for row in columns_data:
    row_str = ' | '.join(str(element).ljust(max_widths[i]) for i, element in enumerate(row))
    print(row_str)

    if row[0] == 'Hours':  # Check if it's the 'Hours' row
        for i, element in enumerate(row[1:], 1):
            if isinstance(element, (int, float)):
                hours_sum += float(element)

print("Total Hours:", hours_sum)  # Print the total sum of Hours

print()

# Need to call zip again, because zip (returns an iterator) and it was consumed when it was used above
transposed_data = zip(*columns_data)  

# convert class zip to a list
transposed_list = list(transposed_data)
print("transposed data converted to a list")
print("transposed_list")
print(transposed_list)

print()
print("the data type of transposed_list is: ", type(transposed_list))
print()
