import math

import mysql

from DB import DB


class GestorDB:
    def __init__(self):
        self.cursor=None
        self.conexion=None
        self.procesar()

    def procesar(self):
        dataBase = DB()
        self.cursor,self.conexion=dataBase.conectar()


    def insertar_informe(self,nombre):
        query = "INSERT INTO informe (nombre) VALUES (%s)"
        values = (nombre,)
        self.cursor.execute(query, values)

        # Hacer commit para aplicar los cambios

        self.conexion.commit()
        id_informe_insertado = self.cursor.lastrowid
        return id_informe_insertado

    def insertar_informes_en_bloques(self, listas, tamano_bloque,pais,id_informe_insertado):
        bloques = len(listas) / tamano_bloque
        exitoso=0
        fallidos=0
        lst=[]
        tmp_lst=[]
        try:

            print("Inserting informes en bloques"   )
            print(len(listas))
            # Conectar a la base de datos
            with self.conexion:
                # Iterar sobre los bloques de 50 informes
                for i in range(0, len(listas), tamano_bloque):

                    bloque_actual = listas[i:i + tamano_bloque]
                    #print("Bloque actual ",len(bloque_actual))

                    # Crear una cadena con múltiples placeholders (%s) para los valores
                    placeholders = ', '.join(['(%s, %s, %s, %s, %s, %s, %s)'])

                    # Concatenar la cadena de consulta
                    query = f"INSERT INTO dataset (date_reported, country,muertes_local,muertes_global,promedio,tipo,id_informe) VALUES {placeholders}"


                    # Crear una lista de valores para el bloque actual
                    values = [(str(informe.fecha), pais,int(informe.cantidad_local),int(informe.cantidad_global),(int(informe.cantidad_local)+int(informe.cantidad_global))/2," ",id_informe_insertado) for informe in bloque_actual]
                    # print(query)
                    # print(values)
                    tmp_lst+=bloque_actual
                    # Ejecutar la consulta con los valores del bloque actual
                    self.cursor.executemany(query, values)
                    exitoso +=1

                # Hacer commit para aplicar los cambios
                self.conexion.commit()

        except mysql.connector.Error as err:
            fallidos +=1
            #Agrega la lista de bloques fallidos
            lst+=tmp_lst
            print(f'Error al manejar la transacción: {err}')

            # Si ocurre un error, realizar un rollback
            self.conexion.rollback()
            print("Rollback realizado")
        self.informe(bloques,exitoso,fallidos)
        if len(lst) >0:
            print("Reintenta insertando los bloques fallidos")
            self.insertar_bloques_fallidos(listas,tamano_bloque,pais,id_informe_insertado)

    def informe(self,cantida_bloque,exitoso,fallidos):
        print("Informe de insert")
        print("Cantidad de bloques : ", math.ceil(cantida_bloque))
        print("Cantidad de bloques EXITOSOS: ",exitoso)
        print("Cantidad de bloques FALLIDOS: ", fallidos)


    def insertar_bloques_fallidos(self, listas, tamano_bloque,pais,id_informe_insertado):
        bloques = len(listas) / tamano_bloque
        exitoso=0
        fallidos=0
        try:

            print("Inserting informes en bloques"   )
            print(len(listas))
            # Conectar a la base de datos
            with self.conexion:
                # Iterar sobre los bloques de 50 informes
                for i in range(0, len(listas), tamano_bloque):

                    bloque_actual = listas[i:i + tamano_bloque]
                    #print("Bloque actual ",len(bloque_actual))

                    # Crear una cadena con múltiples placeholders (%s) para los valores
                    placeholders = ', '.join(['(%s, %s, %s, %s, %s, %s, %s)'])

                    # Concatenar la cadena de consulta
                    query = f"INSERT INTO dataset (date_reported, country,muertes_local,muertes_global,promedio,tipo,id_informe) VALUES {placeholders}"


                    # Crear una lista de valores para el bloque actual
                    values = [(str(informe.fecha), pais,int(informe.cantidad_local),int(informe.cantidad_global),(int(informe.cantidad_local)+int(informe.cantidad_global))/2," ",id_informe_insertado) for informe in bloque_actual]

                    self.cursor.executemany(query, values)
                    exitoso +=1

                # Hacer commit para aplicar los cambios
                self.conexion.commit()

        except mysql.connector.Error as err:
            fallidos +=1
            print(f'Error al manejar la transacción: {err}')

            # Si ocurre un error, realizar un rollback
            self.conexion.rollback()
            print("Rollback realizado")
        self.informe(bloques,exitoso,fallidos)

