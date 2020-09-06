import pandas as pd

df = pd.read_csv('data/creditos2.csv')

# Sort creditos by Ubicacion de la oficina
df_ofi = df.sort_values('UBICACION_DE_LA_OFICINA')

# Print the top few rows
print(df_ofi.head())

# Sort creditos by descending monto del prestamo
df_monto = df.sort_values('MONTO_DEL_PRESTAMO', ascending=False)

# Print the top few rows
print(df_monto.head())

# Sort creditos by Ubicacion de la oficina, then by monto del prestamo  
df_ofi_mon = df.sort_values(['UBICACION_DE_LA_OFICINA', 'MONTO_DEL_PRESTAMO'], ascending=[True, False])

# Print the top few rows
print(df_ofi_mon.head())

# Select the Creation date column
r_creation_d = df['RECORD_CREATION_DATE']

# Print the head of the result
print(r_creation_d.head())

# Select the state and family_members columns
df_d_ofi_mon = df[['RECORD_CREATION_DATE','UBICACION_DE_LA_OFICINA', 'MONTO_DEL_PRESTAMO']]

# Print the head of the result
print(df_d_ofi_mon.head())

# Filter for rows where monto is greater than 10000
df_gt_10k = df[df['MONTO_DEL_PRESTAMO'] > 10000]

# See the result
print(df_gt_10k.head())

# Filter for rows where ubicacion is OREGON
df_oregon = df[df['UBICACION_DE_LA_OFICINA'] == 'OREGON']

# See the result
print(df_oregon.head())

# Filter for rows where monto is greater than 10000 and ubicacion is ARIZONA
df_lt_10k_ari = df[(df['MONTO_DEL_PRESTAMO'] < 10000) & (df['UBICACION_DE_LA_OFICINA'] == 'ARIZONA')]

# See the result
print(df_lt_10k_ari.head())

# Subset for rows ubicacion in ARIZONA and OREGON
df_ubi2 = df[df['UBICACION_DE_LA_OFICINA'].isin(['ARIZONA', 'OREGON'])]

# See the result
print(df_ubi2.head())
