import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Countries
countries = pd.read_csv('data/countries.csv')
print(countries.info())

# List the columns with missing values
cols_with_missing = ['Literacy (%)', 'Climate', 'Industry']

# Create histograms showing the distributions cols_with_missing
countries[cols_with_missing].hist()

# Fill in missing values with 0
countries_filled = countries.fillna(0)

# Create histograms of the filled columns
countries_filled[cols_with_missing].hist()

# Show the plot
plt.show()
