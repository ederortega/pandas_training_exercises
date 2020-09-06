import numpy as np
import pandas as pd

temperatures = pd.read_csv('data/Avg_World_Temp_2020.csv', index_col='Index')

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['Country', 'City'])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])

# Subset columns from Jan to Jun
print(temperatures_srt.loc[:,'Jan':'Jul'])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'),'Jan':'Jul'])
