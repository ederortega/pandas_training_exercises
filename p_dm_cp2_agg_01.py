import numpy as np
import pandas as pd

df = pd.read_csv('data/creditos2.csv')

df['FECHA'] = df.RECORD_CREATION_DATE.str.slice(0, 10)
df['FECHA'] = pd.to_datetime(df['FECHA'])

# Print the head of the sales DataFrame
print(df.head())

# Print the info about the sales DataFrame
print(df.info())

# Print the mean of MONTO_DEL_PRESTAMO
print('Monto del Prestamo (Mean): {}'.format(df['MONTO_DEL_PRESTAMO'].mean()))

# Print the median of MONTO_DEL_PRESTAMO
print('Monto del Prestamo (Median): {}'.format(df['MONTO_DEL_PRESTAMO'].median()))

# Print the maximum of the FECHA column
print('Fecha Maxima: {}'.format(df['FECHA'].max()))

# Print the minimum of the FECHA column
print('Fecha Minima: {}'.format(df['FECHA'].min()))

# A custom IQR (interquartile) function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
 
# Print IQR of the MONTO_DEL_PRESTAMO column
print('Monto del Prestamo IQR: {}'.format(df['MONTO_DEL_PRESTAMO'].agg(iqr)))

# Update to print IQR and median of MONTO_DEL_PRESTAMO
print('{} Monto del Prestamo {}'.format('='*20, '='*20))
print(df['MONTO_DEL_PRESTAMO'].agg([iqr, np.median]))
print('=' * 60)
# Sort df by FECHA
df_fecha = df.sort_values('FECHA')

monto_no_incumplido = df_fecha[df_fecha['PRESTAMO_INCUMPLIDO'] == 'FALSO']['MONTO_DEL_PRESTAMO'].sum()
print('Total prestamos no imcumplidos: {}'.format(monto_no_incumplido))
print('=' * 60)
# Get the cumulative sum of MONTO_DEL_PRESTAMO, add as CUM_MONTO_PRESTAMO col
df_fecha['CUM_MONTO_PRESTAMO'] = df_fecha['MONTO_DEL_PRESTAMO'].cumsum()

# Get the cumulative max of MONTO_DEL_PRESTAMO, add as CUM_MAX_PRESTAMO col
df_fecha['CUM_MAX_PRESTAMO'] = df_fecha['MONTO_DEL_PRESTAMO'].cummax()

# See the columns you calculated
print(df_fecha[["FECHA", "MONTO_DEL_PRESTAMO", "CUM_MONTO_PRESTAMO", "CUM_MAX_PRESTAMO"]].head())
