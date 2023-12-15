
class Global:

    def __init__(self, date_reported, country, new_deaths, cumulative_deaths):
        self.date_reported = date_reported
        self.country = country
        self.new_deaths = new_deaths
        self.cumulative_deaths = cumulative_deaths

    # def mostrar_informacion(self):
    #     print(f"Fecha Reportada: {self.date_reported} "
    #           f"País: {self.country} "
    #           f"Nuevas Muertes: {self.new_deaths} "
    #           f"Muertes Acumuladas: {self.cumulative_deaths} "
    #           "\n")