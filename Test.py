import pandas as pd

# Supongamos que tienes un DataFrame llamado df
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Imprime el DataFrame original
print("DataFrame original:")
print(df)

# Supongamos que quieres eliminar la columna en el índice 1 (segunda columna)
indice_a_eliminar = 1

# Elimina la columna por índice
df = df.drop(df.columns[indice_a_eliminar], axis=1)

# Imprime el DataFrame después de eliminar la columna
print("\nDataFrame después de eliminar la columna:")
print(df)