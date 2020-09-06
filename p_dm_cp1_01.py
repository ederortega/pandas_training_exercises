import pandas as pd

df = pd.read_csv('data/countries.csv')
print(df.head())
print('=' * 80)
print(df.shape)
print('=' * 80)
print(df.info())
print('=' * 80)
print(df.describe())
print('=' * 80)
# Print the values of countries
print(df.values)
print('=' * 80)
# Print the column index of countries
print(df.columns)
print('=' * 80)
# Print the row index of countries
print(df.index)
