from Class.Global import Global
from DB import DB
from File import File
import sys

from Logica import Logica





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #analizar_data()
    dataBase=DB()
    dataBase.conectar()
    logica=Logica()
    logica.analizar()
