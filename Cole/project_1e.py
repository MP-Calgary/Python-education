import pandas as pd
import matplotlib.pyplot as plt

# Define the name and movie release dates
name = "Elliot"  # Name to analyze
movie_release_dates = [
    ("1982-06-11", "ET Release 1 (1982)"),
    ("1985-07-19", "ET Release 2 (1985)"),
    ("2002-03-22", "ET Release 3 (2002)")
]

# Load the CSV file
file_path = 'names_year.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the data for the specified name and years from 1950 onward
df_name = df[(df['name'] == name) & (df['year'] >= 1950)]

# Plotting the usage of the name over time
plt.figure(figsize=(10, 6))

# Plot the historical usage of the name
plt.plot(df_name['year'], df_name['Total'], color='blue', label=f"Usage of '{name}'")

# Mark the movie release dates on the plot
for release_date, label in movie_release_dates:
    release_year = int(release_date.split('-')[0])  # Extract the year from the release date
    plt.axvline(x=release_year, color='red', linestyle='--', label=label)

# Add title and labels
plt.title(f"Usage of the name '{name}' over the years (1950-2020)")
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')

# Set x-axis range to ensure it goes from 1950 to 2020
plt.xlim(1950, 2020)

# Add a legend
plt.legend()

# Display the plot
plt.show()
