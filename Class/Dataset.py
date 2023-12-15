from datetime import datetime


class Local:
    def __init__(self, date_reported, country,muertes_local,muertes_global,promedio,id_informe):
        self.date_reported = date_reported
        self.country = country
        self.muertes_local = muertes_local
        self.muertes_global = muertes_global
        self.promedio=promedio
        self.id_informe = id_informe

    def mostrar_info_data_set(self):
        print(f"Fecha: {self.date_reported}, country {self.country} muertes_local {self.muertes_local} muertes_global {self.muertes_global} promedio {self.promedio}\n")
