import mysql.connector


class DB:
    def __init__(self):
        # Configuración de la conexión a la base de datos
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'admin',
            'database': 'paqueteria',
            'raise_on_warnings': True
        }
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(**self.config)
        print("Conexion exitosa a la base de datos")
        return self.conexion

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
