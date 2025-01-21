import pandas as pd
import matplotlib.pyplot as plt

# List of names to compare
names_to_compare = ["Mary", "Martha", "Peter", "Paul"]

# Load the CSV file
file_path = 'names_year.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Filter the data for the names of interest and the years 1920 - 2000
df_filtered = df[(df['name'].isin(names_to_compare)) & (df['year'] >= 1920) & (df['year'] <= 2000)]

# Plotting the data for the four names
plt.figure(figsize=(12, 6))

for name in names_to_compare:
    # Filter for each name
    df_name = df_filtered[df_filtered['name'] == name]
    plt.plot(df_name['year'], df_name['Total'], label=name)

# Add title and labels
plt.title("Usage of Christian Names (Mary, Martha, Peter, Paul) from 1920 to 2000")
plt.xlabel("Year")
plt.ylabel("Number of Occurrences")

# Add a legend to differentiate the names
plt.legend()

# Display the plot
plt.show()
