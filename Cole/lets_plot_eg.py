# import lets_plot
# print(lets_plot.__version__)

# import sys
# print(sys.executable)


# from lets_plot import *
# import pandas as pd

# # Initialize lets-plot for Jupyter
# LetsPlot.setup_jupyter()

# # Create sample data
# data = {'x': [1, 2, 3, 4, 5], 'y': [3, 7, 8, 5, 9]}
# df = pd.DataFrame(data)

# # Create and display a scatter plot
# ggplot(df, aes('x', 'y')) + geom_point(color='red', size=5) + ggtitle("Scatter Plot Example")

######
#  below here
# from lets_plot import *
# import pandas as pd

# # Initialize Lets-Plot for non-Jupyter environments
# LetsPlot.setup_html()

# # Create sample data
# data = {'x': [1, 2, 3, 4, 5], 'y': [3, 7, 8, 5, 9]}
# df = pd.DataFrame(data)

# # Create and display a scatter plot
# ggplot(df, aes('x', 'y')) + geom_point(color='red', size=5) + ggtitle("Scatter Plot Example")

###### 3rd try
from lets_plot import *
import pandas as pd

# Initialize Lets-Plot for Jupyter
LetsPlot.setup_jupyter()

# Create sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [3, 7, 8, 5, 9]}
df = pd.DataFrame(data)

# Create and display a scatter plot
plot = ggplot(df, aes('x', 'y')) + geom_point(color='red', size=5) + ggtitle("Scatter Plot Example")

# Display the plot inline (only necessary if it does not automatically show)
plot.show()

