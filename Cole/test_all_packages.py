import pandas as pd
import numpy as np
import altair as alt
import lets_plot as lp
import sklearn as sk
import palmerpenguins as pp
import nbformat as nf
import nbclient as nc
import yaml as ym
import os

print("")   # start with an empty line, to seperate in terminal

# test pandas
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}  # Create a simple DataFrame
df = pd.DataFrame(data)
print("Testing Pandas")
print(df)       # Print the DataFrame
print("")       # blank line to separate next test
# -------------------

# test numpy
arr = np.array([1, 2, 3, 4, 5])     # Create a simple NumPy array
print("Testing NumPy")
print("Array:", arr)        # Print the array
print("Sum of the array:", np.sum(arr))  # Print sum
print("")       # blank line to separate next test
# -------------------

# test altair
alt_data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [3, 5, 2, 8, 7]
})   # Create a simple DataFrame

chart = alt.Chart(alt_data).mark_line().encode(
    x='x',
    y='y'
) # Create a basic chart

file_path = 'chart.html'    # set filename
chart.save(file_path)  # Save the chart as an HTML file


full_path = os.path.abspath(file_path) # Print the full path where the file was saved
print("Testing Altair")
print(f"Chart saved to: {full_path}")
print("") 
# ------------------- 

print("Testing lets_plot")
plot_data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [3, 5, 2, 8, 7]
}) # Create a simple DataFrame

plot = lp.ggplot(plot_data, lp.aes(x='x', y='y')) + lp.geom_point()  # Create a basic scatter plot
file_path = 'plot.html'     # Save the plot as an HTML file using ggsave
lp.ggsave(filename=file_path, plot=plot)  # Correct method to save the plot
full_path = os.path.join(os.path.abspath('lets-plot-images'), file_path)  # Adjust the path to include the correct directory
print(f"Plot saved to: {full_path}")  # Print the full path where the file was saved
print("")
# -------------------  

# Test Sklearn
iris = sk.datasets.load_iris()      # Load the Iris dataset using the full path to the function
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)  # Convert to DataFrame for better visualization
print("Testing scikit-learn with the Iris dataset:")  # Print the first few rows of the dataset
print(iris_df.head())
print("")  
# -------------------

# Testing palmerpenguins
penguins = pp.load_penguins()   # Load dataset
print("Testing Penguins")
print(penguins.head())
print("") 
# -------------------

# testing NBformat
file_path = "test_notebook.ipynb"    # Define the notebook file path
with open(file_path) as f:
    nb = nf.read(f, as_version=4)  # Read notebook in version 4 format

client = nc.NotebookClient(nb)   # Create a notebook client and execute the notebook

client.execute()  # Execute the notebook

# Print the full path where the notebook was executed
full_path = os.path.abspath(file_path)
print("Testing NBformat")
print(f"Notebook executed: {full_path}")
print("")
# -------------------  

# testing NBclient

with open('test_notebook.ipynb') as f:
    nb = nf.read(f, as_version=4)   # Load an existing notebook

client = nc.NotebookClient(nb)      # Create a NotebookClient object
client.execute()        # Execute the notebook
output_file = 'executed_notebook.ipynb'   # Save the executed notebook

with open(output_file, 'w') as f:
    nf.write(nb, f)         # Check if the notebook was modified and saved

full_path = os.path.abspath(output_file)        # Print success message with the full path of the saved file
print("Testing Nbclient")
print(f"Notebook executed and saved successfully to: {full_path}")
print("")
# -------------------

# now testing YAML
data = {'name': 'John', 'age': 30, 'city': 'New York'}      # Data to be written to YAML

output_file = 'test_output.yaml'    # Specify the output YAML file

with open(output_file, 'w') as f:
    ym.dump(data, f)            # Write the data to a YAML file


full_path = os.path.abspath(output_file)        # Print success message with the full path of the saved file
print("Testing YAML")
print(f"YAML data saved successfully to: {full_path}")
print("")   # have blank line at end, to seperate in terminal
# -------------------