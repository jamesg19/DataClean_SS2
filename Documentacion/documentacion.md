# Limpieza de Datos

## Archivo Global:

### Date_reported:
- Formato establecido: `%m/%d/%Y`.
- Se filtran todos los campos por año.
- Se verifica que no haya fechas duplicadas por país; si hay alguna duplicada, se elimina y se mantiene solo el primer registro.
- Se eliminan las filas con fechas vacías.

### Country_code:
- Se verifica que tenga un valor; de lo contrario, se elimina toda la fila.

### Country:
- Se filtra por país, sin importar si está en minúsculas o mayúsculas.
- Se verifica que tenga un valor; de lo contrario, se elimina toda la fila.
- Se verifica que no contenga un número entero, ya que debe tener un nombre coherente.

### WHO_region:
- Columna eliminada, ya que es irrelevante para el análisis.

### New_cases:
- Columna eliminada, ya que es irrelevante para el análisis (en el archivo de municipios es el número de muertes por fecha).

### Cumulative_cases:
- Columna eliminada, ya que es irrelevante para el análisis (en el archivo de municipios es el número de muertes por fecha).

### New_deaths:
- Se verifica que sea un número entero mayor o igual a 0; de lo contrario, se elimina toda la fila.
- Se elimina la fila si tiene un campo vacío.

### Cumulative_deaths:
- Se verifica que sea un número entero mayor o igual a 0; de lo contrario, se elimina toda la fila.
- Se elimina la fila si tiene un campo vacío.

## Archivo Local:

### Departamento:

### Codigo_departamento:

### Municipio:

### Codigo_municipio:

### Poblacion:
