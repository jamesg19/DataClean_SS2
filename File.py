import requests
import pandas as pd
from urllib.error import HTTPError, URLError
from pandas.errors import ParserError

from Class.Global import Global


class File:

    def __init__(self,url):
        self.url=url

    # Método de la clase
    def download_csv(self):
        try:
            #response = requests.get(self.url)
            datos = pd.read_csv(self.url, low_memory=False)

            print('Archivo CSV leido exitosamente...')
            return datos
        except HTTPError as e:
            print(f'Error HTTP al intentar acceder a la URL: {e}')

        except URLError as e:
            print(f'Error de URL: {e}')
            datos=""
            return datos
        except ParserError as e:
            print(f'Error al analizar el archivo CSV: {e}')
            datos = ""
            return datos
        except Exception as e:
            print(f'Otro error: {e}')
            datos = ""
            return datos
    def filtar_country_global(self, datos, pais):
        #datos_filtrados = datos[datos['Country'] == pais]

        datos['Country'] = datos['Country'].str.lower()
        pais = pais.lower()

        # Filtrar por país
        datos_filtrados = datos[datos['Country'] == pais.lower()]
        return datos_filtrados

        # informe_global = []
        # for indice, fila in datos_filtrados.iterrows():
        #     informe = Global(
        #         date_reported=fila['Date_reported'],
        #         country=fila['Country'],
        #         new_deaths=fila['New_deaths'],
        #         cumulative_deaths=fila['Cumulative_deaths']
        #     )
        #     informe_global.append(informe)
        #return datos_filtrados







