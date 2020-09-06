import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Countries
countries = pd.read_csv('data/countries.csv')

# Check individual values for missing values
print(countries.isna())

# Check each column for missing values
print(countries.isna().any())

# Bar plot of missing values by variable
countries.isna().sum().plot(kind='bar')

# Show plot
plt.show()

# Remove rows with missing values
countries_complete = countries.dropna()

# Check if any columns contain missing values
print(countries_complete.isna().any())
