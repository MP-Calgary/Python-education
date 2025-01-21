import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the name and birth year
name = "Brittany"  # Replace with any name you want to search for

# Load the CSV file
file_path = 'names_year.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the data for the specified name
df_name = df[df['name'] == name]

# Summarize the historical usage of the specified name
historical_usage = df_name[['year', 'Total']].sort_values(by='year')

# Find the peak usage year and the guessable age
peak_usage_year = historical_usage.loc[historical_usage['Total'].idxmax()]['year']
peak_usage = historical_usage['Total'].max()
guessable_age = 2025 - peak_usage_year  # Assuming current year is 2025

# Find the years with minimal usage (low occurrences)
min_usage_years = historical_usage[historical_usage['Total'] < historical_usage['Total'].quantile(0.1)]  # Bottom 10% usage

# Plotting using matplotlib
plt.figure(figsize=(10, 6))

# Plot the historical usage of the name
plt.plot(historical_usage['year'], historical_usage['Total'], color='blue', label=f"Usage of '{name}'")

# Highlight the peak usage year
plt.scatter(peak_usage_year, peak_usage, color='red', zorder=5, label=f"Peak Usage in {peak_usage_year}")

# Add title and labels
plt.title(f"Usage of the name '{name}' over the years")
plt.xlabel('Year')
plt.ylabel('Number of Occurrences')

# Add a legend
plt.legend()

# Save the plot as a PNG file
plt.savefig(f"{name}_usage_plot.png")

# Close the plot to avoid display in non-interactive environments
plt.close()

# Output answers to the questions
print("")
print(f"Guessing the age of someone named {name}:")
print(f"The peak year for the name {name} was {peak_usage_year}, which means someone named {name} is most likely around {guessable_age} years old in 2025.")
print(f"Ages you would not guess for {name} are likely in the years {', '.join(map(str, min_usage_years['year'].values))}. These years have very low usage of the name.")
print("")