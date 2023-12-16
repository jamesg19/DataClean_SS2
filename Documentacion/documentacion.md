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
### Fechas:
- verifica que tenga fechas en formato valido %m/%d/%Y
- verifica que NO tenga fechas en blanco de lo contrario elimina el registro la columna completa
- verifica que sea una fecha segun el rango especificado
### Departamento:
- verifica que contenga solo string de lo contrario elimina el registro
### Codigo_departamento:
- verifica que contenga solo numeros de lo contrario elimina el registro
### Municipio:
- verifica que contenga solo string de lo contrario elimina el registro
### Codigo_municipio:
- verifica que contenga solo string de lo contrario elimina el registro

### Poblacion:
- verifica que contenga solo numeros enteros positivos

# Estructura de la Tabla 'dataset' COMBINADO

## Columnas:

### id:
- Identificador único para cada registro en la tabla.
- su valor es unicamente enteros.

### date_reported :
- Almacena la fecha del informe.
- esta agrupada para ambos informes.

### country:
- Almacena el nombre del país.
- Tipo de dato VARCHAR con una longitud máxima de 50 caracteres.

### muertes_local :
- Número de muertes del conjunto de datos local.
- Tipo de dato INT (entero).

### muertes_global:
- Número de muertes del conjunto de datos global.
- Tipo de dato entero.

### promedio :
- Almacena el promedio de muertes, calculado a partir de los datos locales y globales.
- Tipo de dato DOUBLE para permitir valores decimales.

### tipo:
- Almacena algún tipo de clasificación o información adicional sobre el registro.
- Tipo de dato VARCHAR con una longitud máxima de 50 caracteres.

### id_informe :
- Clave externa que se relaciona con el identificador único de la tabla 'informe'.
- Asegura la integridad referencial entre las tablas.


