import mysql.connector


class DB:
    def __init__(self):
        self.cursor=""
        # Configuración de la conexión a la base de datos
        self.config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'admin',
            'database': 'ss2_data',
            'raise_on_warnings': True
        }
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(**self.config)
        print("Conexion exitosa a la base de datos")
        self.cursor = self.conexion.cursor()
        print(self.cursor)
        return self.cursor,self.conexion

    def desconectar(self):
        if self.conexion:
            self.conexion.close()

    def commit(self):
        if self.conexion:
            self.conexion.commit()

    def rollback(self):
        if self.conexion:
            self.conexion.rollback()
