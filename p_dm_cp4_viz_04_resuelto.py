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
print(countries[cols_with_missing].head())

print(countries[cols_with_missing].tail())

for col in cols_with_missing:
    countries[col] = countries[col].str.replace(',', '.')
    countries[col] = pd.to_numeric(countries[col], downcast='float')

print(countries[cols_with_missing].head())

print(countries.info())

# Create histograms showing the distributions cols_with_missing
countries[cols_with_missing].hist()

# Fill in missing values with 0
countries_filled = countries.fillna(0)

# Create histograms of the filled columns
countries_filled[cols_with_missing].hist()

# Show the plot
plt.show()
