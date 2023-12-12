import itertools
from datetime import datetime

import pandas as pd

from Class.Global import Global
from File import File


class Logica:
    def __init__(self):
        pass

    def analizar(self):
        url = "https://seminario2.blob.core.windows.net/fase1/global.csv?sp=r&st=2023-12-06T03:45:26Z&se=2024-01-04T11:45:26Z&sv=2022-11-02&sr=b&sig=xdx7LdUOekGyBvGL%2FNE55ZZj9SBvCC%2FWegxtpSsKjJg%3D"
        pais = "Guatemala"
        year=2021
        cantidad_bloque=50

        #self.procesar_arhcivo_global("global.csv",pais,year)
        self.procesar_arhcivo_local()
    def procesar_arhcivo_global(self,url,pais,year):
        file = File(url);
        datos = file.download_csv()
        # filtrar por pais
        datos_filtrados = file.filtar_country_global(datos, pais)
        print(datos_filtrados.head())
        # verificar que sean enteros en numero de muertes diarias
        datos_filtrados = self.verificar_entero(datos_filtrados, 'New_deaths')
        # verificar que sean enteros en numero acumulado de muertes
        datos_filtrados = self.verificar_entero(datos_filtrados, 'Cumulative_deaths')
        print(datos_filtrados.shape[0])
        #Verificar fechas duplicadas
        datos_filtrados =self.eliminar_fecha_duplicada(datos_filtrados,'Date_reported')
        # verificar formato de fecha
        datos_filtrados = self.verificar_fecha(datos_filtrados,year,'Date_reported')
        print(datos_filtrados.shape[0])
        print(datos_filtrados.head())

        lst_global=self.convertir_global_a_object(datos_filtrados)
        #for informe in lst_global:
            #informe.mostrar_informacion()
    def procesar_arhcivo_local(self):
        file = File("municipio.csv")
        data_local=file.download_csv()
        print("#################")
        print(data_local.shape[0])
        print(data_local.head())
        print("######################\n")
        list_fechas=self.get_lista_fechas_local(data_local)

        data_local=self.verificar_columna_con_fecha(data_local)
        print(data_local.shape[0])
        print(data_local.head())


    def get_lista_fechas_local(self,df):
        # Obtiene solo los nombres de las columnas
        nombres_columnas = df.columns[5:].tolist()
        print(nombres_columnas)

        # Filtra las fechas válidas
        fechas_validas = []

        for indice, fecha_str in enumerate(nombres_columnas):
            try:
                fecha_parseada = datetime.strptime(fecha_str, "%m/%d/%Y")
                fechas_validas.append((indice, fecha_parseada, True))
            except ValueError:
                fechas_validas.append((indice, fecha_str, False))
                # La fecha no cumple con el formato especificado
                print(f"Fecha no válida: {fecha_str}")
                # Elimina la sexta columna (índice 5 en base 0)
                df = df.drop(df.columns[5+indice], axis=1)

        # Imprime las fechas válidas
        print("\nFechas válidas:")
        for fecha in fechas_validas:
            print(fecha)


        return nombres_columnas

    def verificar_columna_con_fecha(self,df):
        # Convertir la columna de fecha en un objeto de fecha y hora de pandas
        dff=df.iloc[:, 5:] = df.iloc[:, 5:].apply(pd.to_datetime, format='%d/%m/%Y', errors='coerce')
        # Eliminar las columnas que no cumplen con el formato
        dff.dropna(subset=dff.columns[5:], how='all', inplace=True)
        return df


    # Elimina los datos que no tengan fecha
    def limpiar_data_global_date_reported(self,data,column):
        datos = data.dropna(subset=[column])
        return datos


    # Retorna una lista de objetos
    def convertir_global_a_object(self, datos_filtrados):
        informe_global = []
        for indice, fila in datos_filtrados.iterrows():
            informe = Global(
                date_reported=fila['Date_reported'],
                country=fila['Country'],
                new_deaths=fila['New_deaths'],
                cumulative_deaths=fila['Cumulative_deaths'])
            informe_global.append(informe)
        return informe_global


    def verificar_entero(self, datos,column):
        # Convertir la columna 'New_cases' a numérico y eliminar filas con valores no numéricos
        datos.loc[:, column] = pd.to_numeric(datos[column], errors='coerce')
        datos = datos.dropna(subset=[column])  # Eliminar filas con valores no numéricos
        return datos

    def verificar_fecha(self,datos,year,column):
        # Convertir la columna 'fecha' en un objeto de fecha y hora de pandas
        datos[column] = pd.to_datetime(datos[column], format='%m/%d/%Y', errors='coerce')
        # Eliminar las filas que no cumplen con el formato
        datos.dropna(subset=[column], inplace=True)
        # Filtrar datos para un año específico, por ejemplo, 2023

        datos_filtrados = datos[datos[column].dt.year == year]

        return datos_filtrados

    def eliminar_fecha_duplicada(self,datos,column):
        data= datos.drop_duplicates(subset=[column])
        return data