import numpy as np
import pandas as pd

df = pd.read_csv('data/countries.csv')

# Pivot for mean GDP ($ per capita) for each Region
mean_GDP_by_region = df.pivot_table(values='GDP ($ per capita)', index='Region')

# Print mean_GDP_by_region
print(mean_GDP_by_region)
print('=' * 80)
# Pivot for mean and median GDP ($ per capita) for Region
mean_med_GDP_by_region = df.pivot_table(values='GDP ($ per capita)', index='Region', aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_GDP_by_region)
print('=' * 80)

# Pivot for mean GDP ($ per capita) by Region and Climate 
mean_GDP_by_region_climate = df.pivot_table(values='GDP ($ per capita)', index='Region', columns='Climate')

# Print mean_GDP_by_region_climate
print(mean_GDP_by_region_climate)
print('=' * 100)
# Pivot for mean GDP ($ per capita) by Region and Climate, fill missing values with 0
mean_GDP_by_region_climate = df.pivot_table(values='GDP ($ per capita)', index='Region', columns='Climate', fill_value=0)

# Print mean_GDP_by_region_climate
print(mean_GDP_by_region_climate)
print('=' * 120)
# Pivot for mean GDP ($ per capita) by Region and Climate, fill missing values with 0; sum all rows and cols
mean_GDP_by_region_climate = df.pivot_table(values='GDP ($ per capita)', index='Region', columns='Climate', fill_value=0, margins=True, aggfunc=[np.sum])

# Print mean_GDP_by_region_climate
print(mean_GDP_by_region_climate)
