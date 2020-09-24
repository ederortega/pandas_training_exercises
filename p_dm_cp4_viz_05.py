import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Countries
countries = pd.read_csv('data/countries.csv')

countries['Literacy (%)'] = countries['Literacy (%)'].str.replace(',', '.')
countries['Literacy (%)'] = pd.to_numeric(countries['Literacy (%)'], downcast='float')

# Make a scatter plot
fig, ax = plt.subplots(figsize=(14,9))
volume = countries['Population'] / countries['Area (sq. mi.)']
colors = countries['Literacy (%)'] / 100
ax.scatter(countries['GDP ($ per capita)'], countries['Literacy (%)'], s=volume, c=colors, alpha=0.5)

ax.set_xlabel('GDP ($ per capita)', fontsize=15)
ax.set_ylabel('Literacy (%)', fontsize=15)
ax.set_title('GDP per capita vs Literacy (%)', fontsize=15)
plt.xscale("log")
# plt.yscale("log")
# Show the plot
plt.show()
