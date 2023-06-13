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

import random

def generate_random_list(num_integers):
    random_list = []
    for _ in range(num_integers):
        random_list.append(random.randint(1, 500))
    return random_list