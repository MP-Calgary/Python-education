import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the name and birth year
name = "Michael"  # Replace with any name you want to search for
birth_year = 1967  # Replace with the birth year you want to search for

# Load the CSV file
file_path = 'names_year.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the data for the specified name
df_name = df[df['name'] == name]

# Find the number of occurrences of the name in the specified birth year
df_name_birth_year = df_name[df_name['year'] == birth_year]
name_birth_year_usage = df_name_birth_year['Total'].values[0] if not df_name_birth_year.empty else 0

# Summarize the historical usage of the specified name
historical_usage = df_name[['year', 'Total']].sort_values(by='year')

# Plotting using matplotlib
plt.figure(figsize=(10, 6))

# Plot the historical usage of the name
plt.plot(historical_usage['year'], historical_usage['Total'], color='blue', label=f"Usage of '{name}'")

# Highlight the birth year usage
plt.scatter(df_name_birth_year['year'], df_name_birth_year['Total'], color='red', zorder=5, label=f"Year {birth_year} Usage")

# Add title and labels
plt.title(f"Usage of the name '{name}' over the years (Including {birth_year})")
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')

# Add a legend
plt.legend()

# Save the plot as a PNG file
plt.savefig("name_usage_plot.png")

# Close the plot to avoid display in non-interactive environments
plt.close()