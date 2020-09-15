import numpy as np
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv('data/sp500.csv', index_col='Date', parse_dates=True)

# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv('data/exchange.csv', index_col='Date', parse_dates=True)

# Merge sp500 with exchange on 'Date': merge_by_date
merge_by_date = pd.merge(sp500, exchange, on='Date')

# Print merge_by_date
print(merge_by_date.head())
