import pandas as pd
import matplotlib.pyplot as plt

# Define the name and movie release year
name = "Forrest"  # Replace with any name you want to search for
movie_release_date = "1994-07-06"  # Date of the movie release

# Load the CSV file
file_path = 'names_year.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the data for the specified name
df_name = df[df['name'] == name]

# Plotting the usage of the name over time
plt.figure(figsize=(10, 6))

# Plot the historical usage of the name
plt.plot(df_name['year'], df_name['Total'], color='blue', label=f"Usage of '{name}'")

# Mark the movie release date on the plot
movie_release_year = int(movie_release_date.split('-')[0])
plt.axvline(x=movie_release_year, color='red', linestyle='--', label=f"Movie Release ({movie_release_year})")

# Add title and labels
plt.title(f"Usage of the name '{name}' over the years (Including {movie_release_year})")
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')

# Add a legend
plt.legend()

# Display the plot
plt.show()
