
peliculas = []

class Pelicula:

    def __init__(self, nombre="", duracion="", stock=0):
        
        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock

    def Agregar_Pelicula(self, nombre, duracion, stock):

        self.nombre = nombre
        self.duracion = duracion
        self.stock = stock
        peliculas.append({"Pelicula": nombre,
                          "Duracion": duracion,
                          "Stock": stock})

    def Listar_Peliculas(self):
        return peliculas


"""
p = Pelicula()
p.Agregar_Pelicula("Batman", "1:35:00", 21)
p.Agregar_Pelicula("Avangers", "2:22:57", 15)
print(p.Listar_Pelicula())"""
