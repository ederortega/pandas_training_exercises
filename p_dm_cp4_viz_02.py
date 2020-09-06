import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Creditos
creditos = pd.read_csv('data/creditos2.csv')

# Look at the first few rows of data
print(creditos.head())

# Histogram of conventional MONTO of SOUTHERN CALIFORNIA OFFICE  
creditos[creditos['UBICACION_DE_LA_OFICINA'] == 'SOUTHERN CALIFORNIA']['MONTO_DEL_PRESTAMO'].hist(alpha=0.5, bins=20)

# Histogram of conventional MONTO of ARIZONA OFFICE 
creditos[creditos['UBICACION_DE_LA_OFICINA'] == 'ARIZONA']['MONTO_DEL_PRESTAMO'].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(['SOUTHERN CALIFORNIA', 'ARIZONA'])

# Show the plot
plt.show()