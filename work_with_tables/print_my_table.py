import os
# clear the terminal 
os.system('clear')

# dota_teams = ["Liquid", "Virtus.pro", "PSG.LGD", "Team Secret"]
# data = [[1, 2, 1, 'x'],
# ['x', 1, 1, 'x'],
# [1, 'x', 0, 1],
# [2, 0, 2, 1]]
# format_row = "{:>12}" * (len(dota_teams) + 1)
# print(format_row.format("", *dota_teams))
# for team, row in zip(dota_teams, data):
#     print(format_row.format(team, *row))

def display_table(data):
    # Determine the maximum width for each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    # Print the table header
    print('+', end='')
    for width in column_widths:
        print('-' * (width + 2), end='+')
    print()

    # Print the table rows
    for row in data:
        print('|', end='')
        for item, width in zip(row, column_widths):
            print(f' {str(item):{width}} ', end='|')
        print()

    # Print the table footer
    print('+', end='')
    for width in column_widths:
        print('-' * (width + 2), end='+')
    print()


# Example usage
table_data = [
    ['Name', 'Age', 'City', 'Country', 'Occupation', 'Salary'],
    ['John Doe', 28, 'New York', 'USA', 'Engineer', '$150,000'],
    ['Jane Smith', 32, 'London', 'UK', 'Teacher', '$35,000'],
    ['Michael Johnson', 45, 'Paris', 'France', 'Artist','$25,000'],
    ['Emily Davis', 39, 'Sydney', 'Australia', 'Doctor','$1,245,000'],
    ['Jonathon Anderson', 39, 'San Francisco', 'United States of America', 'Computer Engineer','$545,000']
]

display_table(table_data)
