import numpy as np
import pandas as pd

df = pd.read_csv('data/creditos2.csv')

print(df.info())

# Drop duplicate PRESTAMO_INCUMPLIDO combinations
df_no_incumplido = df.drop_duplicates(subset='PRESTAMO_INCUMPLIDO')
print(df_no_incumplido.info())

# Drop duplicate DEUDA_EXISTENTE/NOTAS_DEL_AGENTE combinations
df_no_notas = df.drop_duplicates(subset=['DEUDA_EXISTENTE', 'NOTAS_DEL_AGENTE'])
print(df_no_notas.info())

incumplidos_v = df['PRESTAMO_INCUMPLIDO'] == 'VERDADERO'

# Subset the rows that PRESTAMO_INCUMPLIDO are VERDADERO and drop duplicate DEUDA_EXISTENTE
df_deuda_existente = df[incumplidos_v].drop_duplicates(subset='DEUDA_EXISTENTE')
print(df_deuda_existente[['RECORD_CREATION_DATE', 'MONTO_DEL_PRESTAMO', 'DEUDA_EXISTENTE']])

# Count the number of records by PRESTAMO_INCUMPLIDO 
deuda_e_counts = df_deuda_existente['PRESTAMO_INCUMPLIDO'].value_counts()
print('=' * 80)
print(deuda_e_counts)

# Get the proportion of records of each PRESTAMO_INCUMPLIDO 
deuda_proportion = df_deuda_existente['PRESTAMO_INCUMPLIDO'].value_counts(normalize=True)
print('=' * 80)
print(deuda_proportion)

# Count the number of each DEUDA_EXISTENTE number and sort
deuda_count = df_no_notas['DEUDA_EXISTENTE'].value_counts(sort=True)
print('=' * 80)
print(deuda_count)

# Get the proportion of DEUDA_EXISTENTE of each number and sort
deuda_props_count = df_no_notas['DEUDA_EXISTENTE'].value_counts(sort=True, normalize=True)
print('=' * 80)
print(deuda_props_count)
