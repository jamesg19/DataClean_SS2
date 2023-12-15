from datetime import datetime


class DataLocal:
    def __init__(self, fecha, cantidad_local,cantidad_global):
        self.fecha = fecha
        self.cantidad_local = cantidad_local
        self.cantidad_global = cantidad_global

    def mostrar_informacion(self):
        #print("HI")
        print(f"Fecha: {self.fecha}, Cantidad_Local {self.cantidad_local}, Cantidad_Global {self.cantidad_global}\n")

    def convert_fecha_db(self):
        fecha_obj = datetime.strptime(self.fecha, "%m/%d/%Y")
        # Formatea la fecha en el nuevo formato "yyyy-mm-dd"
        fecha_nuevo_formato = fecha_obj.strftime("%Y-%m-%d")
        self.fecha=fecha_nuevo_formato