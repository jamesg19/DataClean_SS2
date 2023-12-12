from datetime import datetime

class Municipio:
    def __init__(self, departamento, codigo_departamento, fecha,cantidad):
        self.departamento = departamento
        self.codigo_departamento = codigo_departamento
        self.fecha = fecha
        self.cantidad=cantidad

    def mostrar_informacion(self):
        print(f"Departamento: {self.departamento}, Código Departamento: {self.codigo_departamento}, "
              f"Fecha: {self.fecha}, Cnatidad: {self.cantidad}\n")