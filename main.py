from Class.Global import Global
from DB import DB
import time
from File import File
import sys

from Logica import Logica



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = sys.argv[1]
    pais = sys.argv[2]
    year=int(sys.argv[3])
    cantidad = int(sys.argv[4])
    # Registra el tiempo de inicio
    tiempo_inicio = time.time()


    logica=Logica()
    logica.analizar(url,pais,year,cantidad)

    # Registra el tiempo de finalización
    tiempo_fin = time.time()

    # Calcula la duración total
    duracion_total = tiempo_fin - tiempo_inicio

    print(f"El código tardó {duracion_total} segundos en ejecutarse.")
