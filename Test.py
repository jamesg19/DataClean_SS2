import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path = '/'
filename = 'data.csv'
df = pd.read_csv(f'{filename}')
df.columns

# Utilizar describe para obtener estadísticas descriptivas
descripcion = df.describe()

# Utilizar info para obtener información general del DataFrame
informacion = df.info()

# Obtener la tabla de correlación
tabla_correlacion = df.corr(numeric_only=True)

# Imprimir los resultados
print("\nInformación del DataFrame:")
print(informacion)
print("Estadísticas Descriptivas:")
print(descripcion)
# Imprimir la tabla de correlación

print("Tabla de Correlación:")
print(tabla_correlacion)
# Mostrar el mapa de calor
sns.heatmap(tabla_correlacion, annot=True, cmap='coolwarm', linewidths=.5)
plt.show()