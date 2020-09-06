import numpy as np
import pandas as pd

temperatures = pd.read_csv('data/Avg_World_Temp_2020.csv')

# Pivot avg_temp_c by country and city vs continent
temp_by_country_city_vs_continent = temperatures.pivot_table('Avg_Year', index=['Country', 'City'], columns='Continent')

# See the result
print(temp_by_country_city_vs_continent)

# Subset for Egypt to India
print(temp_by_country_city_vs_continent.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_continent.loc[('Egypt', 'Cairo'):('India','Delhi')])

# Subset in both directions at once
print(temp_by_country_city_vs_continent.loc[('Egypt', 'Cairo'):('India','Delhi'), 'Africa':'Europe'])

# Get the worldwide mean temp by continent
mean_temp_by_continent = temp_by_country_city_vs_continent.mean()

print('-------- Mean by Continent: {}'.format(mean_temp_by_continent))
# Filter for the continent that had the highest mean temp
print(mean_temp_by_continent[mean_temp_by_continent == mean_temp_by_continent.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_continent.mean(axis='columns')

print('-------- Mean by City: {}'.format(mean_temp_by_city))
# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
