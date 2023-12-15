from datetime import datetime


class MergeData:

    def __init__(self, lista_local,lista_global):
        self.lista_local = lista_local
        self.lista_global = lista_global

    def analizar(self):
        print("Iniciando Merge Data")
        print("Cantidad Local",len(self.lista_local))
        print("Cantidad Global", len(self.lista_global))
        lst_merge=[]
        cant=0
        print("TODA LA LISTA DE MERGE INICIANDO")
        print("Cantidad Local", len(self.lista_local))
        print("Cantidad Global", len(self.lista_global))
        print("Cantidad MERGE", len(lst_merge))
        for item_local in self.lista_local:

            bool=False
            for item_global in self.lista_global:
                fecha_original_local = item_global.fecha
                mes, dia, anio = map(int, fecha_original_local.split('/'))
                fecha_formateada = f"{mes}/{dia}/{anio}"

                fecha_original_global = item_local.fecha
                mes1, dia1, anio1 = map(int, fecha_original_global.split('/'))
                fecha_formateada2 = f"{mes1}/{dia1}/{anio1}"


                if fecha_formateada2 == fecha_formateada:
                    cant+=1
                    #print("Merge Count",cant)
                    #print(item_local.fecha, " == ", fecha_formateada)
                    tempL=item_local
                    tempG = item_global

                    #self.lista_local.remove(item_local)
                    self.lista_global.remove(item_global)

                    #tempL.cantidad_global=tempG.cantidad_global
                    item_local.cantidad_global=tempG.cantidad_global
                    #lst_merge.append(tempL)






        print("TODA LA LISTA DE MERGE FINALIZANDO")
        print("Cantidad Local", len(self.lista_local))
        print("Cantidad Global", len(self.lista_global))
        print("Cantidad MERGE", len(lst_merge))
        lst_merge += self.lista_local
        lst_merge += self.lista_global

        print("TODA LA LISTA DE MERGE RESULTADOS")
        print("Cantidad Local", len(self.lista_local))
        print("Cantidad Global", len(self.lista_global))
        print("Cantidad MERGE", len(lst_merge))

        for item in lst_merge:
            item.convert_fecha_db()
        return lst_merge

                #print(item.mostrar_informacion())