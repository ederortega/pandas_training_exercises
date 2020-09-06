import numpy as np
import pandas as pd

temperatures = pd.read_csv('data/weatherHistory.csv', parse_dates=['Date'])

# Use Boolean conditions to subset temperatures for rows in 2006 and 2009
temperatures_bool = temperatures[(temperatures['Date'] >= '2006-01-01') & (temperatures['Date'] <= '2009-12-31')]
print(temperatures_bool)

# Set date as an index
temperatures_ind = temperatures.set_index('Date')

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['Aug 2010':'Feb 2011'])

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:,2:4])

# Use slicing in both directions at once
print(temperatures.iloc[0:5, 2:4])
