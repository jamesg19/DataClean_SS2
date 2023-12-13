from datetime import datetime
import pandas as pd
from Class.Global import Global
from Class.Municipio import Municipio
from File import File
import os

class Logica:
    def __init__(self):
        pass

    def analizar(self):
        url = "https://seminario2.blob.core.windows.net/fase1/global.csv?sp=r&st=2023-12-06T03:45:26Z&se=2024-01-04T11:45:26Z&sv=2022-11-02&sr=b&sig=xdx7LdUOekGyBvGL%2FNE55ZZj9SBvCC%2FWegxtpSsKjJg%3D"
        pais = "Guatemala"
        year=2020
        cantidad_bloque=50

        #self.procesar_arhcivo_global("global.csv",pais,year)
        self.procesar_arhcivo_local(year)
    def procesar_arhcivo_global(self,url,pais,year):
        file = File(url)
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
        #verificar que la fecha y pais no se repita en una misma fila
        datos_filtrados=self.verifica_repeticion_columnas_en_fila(datos_filtrados,'Date_reported','Country')

        lst_global=self.convertir_global_a_object(datos_filtrados)
        for informe in lst_global:
            informe.mostrar_informacion()

    #MANEJA LA LOGICA DEL ARCHIVO LOCAL
    def procesar_arhcivo_local(self,year):
        file = File("municipio.csv")
        data_local=file.download_csv()
        #print("#################")
        #print(data_local.shape[0])
        #print(len(data_local))
        #print(data_local.head())
        #print("######################\n")
        data_local,columnas_validas_fecha=self.get_lista_fechas_local(data_local)

        data_local=self.filtrar_columnas_por_fecha(data_local,year,columnas_validas_fecha)

        data_local=self.verificar_entero_archivo_local(data_local,columnas_validas_fecha)

        data_local=self.verificar_poblacion(data_local,"poblacion")

        data_local=self.analizar_solo_string(data_local,"departamento")

        data_local = self.analizar_solo_string(data_local, "municipio")

        data_local = self.verifica_repeticion_columnas_en_fila(data_local,"departamento","municipio")
        print(data_local.shape[0])
        print(len(data_local))
        print(data_local.head())
        print()
        print(data_local)
        lst=self.convertir_local_a_object(data_local)
        for item in lst:
            #item.mostrar_informacion()
            pass

        os.remove("municipio_limpio.csv")
        data_local.to_csv("municipio_limpio.csv",index=False)


    def get_lista_fechas_local(self,df):
        # Obtiene solo los nombres de las columnas
        nombres_columnas = df.columns[5:].tolist()
        # Filtra las fechas válidas
        fechas_validas = []
        columnas_validas = []

        for indice, fecha_str in enumerate(nombres_columnas):
            try:
                fecha_parseada = datetime.strptime(fecha_str, "%m/%d/%Y")
                fechas_validas.append((indice, fecha_parseada, True))
                columnas_validas.append(fecha_str)

            except ValueError:
                fechas_validas.append((indice, fecha_str, False))
                # La fecha no cumple con el formato especificado
                print(f"Fecha no válida: {fecha_str}")

                #df = df.drop(df.columns[5+indice], axis=1)
                df = df.drop(fecha_str, axis=1)
                print(f"Columna {fecha_str} eliminada.")


        # Imprime las fechas válidas
        #print("\nFechas válidas:")
        #for fecha in fechas_validas:
            #print(fecha)


        return df,columnas_validas

    def filtrar_columnas_por_fecha(self,df,year,columnas_validas_fecha):

        # Convierte las columnas de fechas a objetos datetime para comparar con el año 2020
        # Convierte las fechas de strings a objetos datetime con el formato deseado
        lista=[]
        for item in columnas_validas_fecha:

            fecha_parseada = pd.to_datetime(item, format='%m/%d/%Y')
            lista.append([fecha_parseada,item])

        # Filtra las columnas que corresponden al año X
        #columnas_fechas_filtradas = [str(fecha) for fecha in fechas_parseadas if fecha.year == year]

        for fechas_item in lista:

           if not fechas_item[0].year == year:

               print(fechas_item[1])
               df = df.drop(fechas_item[1], axis=1)

        return df


        #return df_filtrado
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

    def convertir_local_a_object(self, df):

        municipios = []
        fechas = list(df.columns[5:])

        # Itera sobre las filas del DataFrame
        for indice, row in df.iterrows():
            # Obtiene las fechas y convierte a un diccionario

            # Crea una instancia de la clase Municipio
            municipio = Municipio(
                departamento=row['departamento'],
                codigo_departamento=row['codigo_departamento'],
                municipio=row['municipio'],
                codigo_municipio=row['codigo_municipio'],
                poblacion=row['poblacion'],
                fechas=fechas
            )
            #print(municipio.mostrar_informacion())

            municipios.append(municipio)

        return municipios

    #Verifica si la la columna especificada contiene datos enteros
    #si hay un dato que NO sea un entero se elimina la fila
    def verificar_entero(self, datos,column):
        # Convertir la columna 'New_cases' a numérico y eliminar filas con valores no numéricos
        datos.loc[:, column] = pd.to_numeric(datos[column], errors='coerce')
        datos = datos.dropna(subset=[column])  # Eliminar filas con valores no numéricos
        return datos
    #Valida que una columna solo tenga string de lo contrario elimina la fila
    def analizar_solo_string(self,df,columna):
        df=self.eliminar_campo_vacio(df,columna)
        poblacion = df[columna]


        for index, value in poblacion.items():
            try:
                print(isinstance(int(value), int))
                if isinstance(int(value), int):
                    df = df.drop(index=index)
            except:
                pass
        return df
    def verificar_poblacion(self,df,columna):
        # Obtener la columna población

        poblacion = df[columna]

        # Verificar si cada valor es un entero mayor o igual a 0
        for index, value in poblacion.items():
            try:
                if not isinstance(int(value),int) or int(value) <0:
                    df = df.drop(index=index)
            except:
                    df = df.drop(index=index)




        return df
    def eliminar_campo_vacio(self,df,columna):
        df.dropna(subset=[columna], inplace=True)
        return df

    # Verifica la condición en la la lista columnas de fechas sea un entero
    # y sustituye los valores que no cumplen con la condición por 0
    def verificar_entero_archivo_local(self,df,list_columnas):

        print("*** COLUMNAS VALIDAS: ",list_columnas)
        for column in list_columnas:

            # Sustituir los valores no válidos por 0
            try:
                df[column] = df[column].apply(lambda x: 0 if (not isinstance(x, int) and not isinstance(x, float)) or x < 0 else x)
            except:
                pass
        return df

    def verifica_repeticion_columnas_en_fila(self,df,col1,col2):
        # Verifica y elimina filas donde la combinación de "departamento" y "municipio" se repite
        df = df.drop_duplicates(subset=[col1, col2])
        return df
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