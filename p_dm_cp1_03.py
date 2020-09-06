import pandas as pd

countries = pd.read_csv('data/countries.csv')

columns_to_show = ['Country', 'Population', 'Area (sq. mi.)', 'Pop. per Area', 'Year']
# Add P per Area columna by divide Population and Area (sq. mi.) 
countries['Pop. per Area'] = countries['Population'] / countries['Area (sq. mi.)']
# Add year
countries['Year'] = 2000

# See the result
print(countries[columns_to_show].head())

# Subset rows for 'Pop. per Area greater than 500
high_density = countries[countries['Pop. per Area'] > 500]

# Sort high_homelessness by descending indiv_per_10k
high_density = high_density.sort_values('Pop. per Area', ascending=False)

# See the result
print(high_density[columns_to_show].head())

print(high_density[columns_to_show].tail())
