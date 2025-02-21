
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

print(__file__)  # Prints the full path of the script file
current_dir = Path(__file__).parent # Gets the directory containing the script
print(current_dir)  # Prints the script's directory

# Load data from a CSV file dumped in the repo
data = pd.read_csv('data.csv')
print("Data loaded:")
print(data.head())

# Calculate some basic statistics directly in the global scope
mean_value = data['value1'].mean()
std_value = data['value1'].std()
print("Mean of value1:", mean_value)
print("Standard deviation of value1:", std_value)

# Create a scatter plot without any function encapsulation
plt.figure(figsize=(8, 6))
plt.scatter(data['value1'], data['value2'], c='blue', alpha=0.5)
plt.title('Scatter Plot of value1 vs. value2')
plt.xlabel('value1')
plt.ylabel('value2')
plt.show()

# Some extra messy code: looping and printing out repeated info
for i in range(3):
    print("Iteration", i, "- Mean value1:", mean_value)

# Redundant code that doesn't affect anything (for demo purposes)
unused_variable = "This variable is never used!"

# Extra comments and to-do notes left in the code
# TODO: Refactor code into functions
# FIXME: Parameterize file paths and configuration settings

# End of messy script
