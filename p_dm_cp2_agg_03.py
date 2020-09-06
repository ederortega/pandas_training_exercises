import numpy as np
import pandas as pd

df = pd.read_csv('data/countries.csv')

df["Region"] = df["Region"].str.strip()

# Calc total population
total_population = df["Population"].sum()

# Subset for Region EASTERN EUROPE, calc total Population
estearn_europe_pop = df[df["Region"] == "EASTERN EUROPE"]["Population"].sum()

# Subset for Region NORTHERN AFRICA, calc total Population
northern_africa_pop = df[df["Region"] == "NORTHERN AFRICA"]["Population"].sum()

# Subset for Region OCEANIA, calc total Population
oceania_pop = df[df["Region"] == "OCEANIA"]["Population"].sum()

# Get proportion for each Region
pop_by_region = [estearn_europe_pop, northern_africa_pop, oceania_pop] / total_population
print(pop_by_region)
print('=' * 80)
# Group by Region; calc total Population
grouped_pop_by_region = df.groupby("Region")["Population"].sum()

# Get proportion for each Region
pop_by_region = grouped_pop_by_region / grouped_pop_by_region.sum()
print(pop_by_region)
print('=' * 80)
# Group by Region and Climate; calc total Population
pop_by_region_and_climate = df.groupby(["Region", "Climate"])["Population"].sum()
print(pop_by_region_and_climate)
print('=' * 80)

# For each Region, aggregate GDP ($ per capita): get min, max, mean, and median
gdp_stats = df.groupby('Region')['GDP ($ per capita)'].agg([np.min, np.max, np.mean, np.median])

# Print gdp_stats
print(gdp_stats)
print('=' * 80)
# For each Region, aggregate GDP ($ per capita) and Area (sq. mi.): get min, max, mean, and median
gdp_area_stats = df.groupby('Region')[['GDP ($ per capita)', 'Area (sq. mi.)']].agg([np.min, np.max, np.mean, np.median])

# Print gdp_area_stats
print(gdp_area_stats)
