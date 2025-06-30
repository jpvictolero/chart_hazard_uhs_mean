import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file and Read the data from the sheet named 'Sheet1'
file_path = "first.csv"
df = pd.read_csv(file_path)

# Extract numerical columns, including 'PGA' (replace PGA with 0 in x_values) and convert them to float
numeric_cols = [col for col in df.columns[4:] if str(col).replace(".", "").isdigit() or col == "PGA"]
x_values = [0] + list(map(float, numeric_cols[1:]))

# Define colors based on the third column (100/1000)
color_map = {100: 'blue', 1000: 'red'}
labels_map = {100: 'PSHA: 100-year MRI', 1000: 'PSHA: 1000-year MRI'}

# Track unique labels for the legend
unique_labels = {}

# Plot the data for each row
plt.figure(figsize=(12, 6))
for index, row in df.iterrows():
    # Get the value from the third column
    category = row[df.columns[3]]
    # Default to black if value is not 100 or 1000
    color = color_map.get(category, 'black')
    label = labels_map.get(category)
    
    # Only add unique labels to the legend
    if category not in unique_labels:
        unique_labels[category] = label
        plt.plot(x_values, row[numeric_cols], color=color, label=label)
    else:
        plt.plot(x_values, row[numeric_cols], color=color)

# Chart labels and legend and Use 'PGA' as x-axis label
# Label for x-axis
plt.xlabel("Period, seconds")
# Label for y-axis
plt.ylabel("Acceleration, g")
# Title
plt.title("Pier 3, Pier 4, Pier 5, Pier 6, and Pier 7 Uniform Hazard Spectra: PSHA: 100-year MRI, PSHA: 1000-year MRI")
plt.legend()
plt.grid()

# Set y-axis major ticks, 0 to 2.0 in 0.2 increments
plt.yticks(np.arange(0, 2.1, 0.2))

# Set x-axis tick labels
x_tick_labels = ["PGA", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3]
plt.xticks(x_values, x_tick_labels, rotation=45)

plt.show()
