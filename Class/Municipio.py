from datetime import datetime

class Municipio:
    def __init__(self, departamento, codigo_departamento, municipio, codigo_municipio, poblacion, fechas):
        self.departamento = departamento
        self.codigo_departamento = codigo_departamento
        self.municipio = municipio
        self.codigo_municipio = codigo_municipio
        self.poblacion = poblacion
        self.fechas = fechas

    def mostrar_informacion(self):

        print(f"Departamento: {self.departamento}, Codigo_departamento {self.codigo_departamento}, municipio: {self.municipio}, codigo_municipio{self.codigo_municipio}, Poblacion: {self.poblacion}, \nFechas: {self.fechas})\n")