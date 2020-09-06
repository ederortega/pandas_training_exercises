import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creditos
creditos = pd.read_csv('data/creditos2.csv')

# Look at the first few rows of data
print(creditos.head())

# Get the total sum of monto by office
monto_by_office = creditos.groupby('UBICACION_DE_LA_OFICINA')['MONTO_DEL_PRESTAMO'].sum()

# Create a bar plot of total monto by office
monto_by_office.plot(kind='bar')

# Show the plot
plt.show()


# weather history of a city
weather = pd.read_csv('weatherHistory.csv', parse_dates=['Date'])

# Look at the first few rows of data
print(weather.info())

# weather_temp_c = weather[weather['Date'] < '2006-01-03'][['Date', 'Temperature (C)']]
weather_temp_c = weather.groupby([weather.Date.dt.year, weather.Date.dt.month])['Temperature (C)'].max()
# Create a line plot of temperature by date
weather_temp_c.plot(kind='line')

plt.xlabel('Year, month')
# Show the plot
plt.show()


# Countries
countries = pd.read_csv('countries.csv')

# Scatter plot of Population vs GDP ($ per capita) with title
countries.plot(x='Population', y='GDP ($ per capita)', kind='scatter', title='Population vs. GDP per capita')

# Show the plot
plt.show()
