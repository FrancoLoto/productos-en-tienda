
libros = []

class Libro:

    def __init__(self, nombre="", paginas=0, stock=0):
        
        self.nombre = nombre
        self.paginas = paginas
        self.stock = stock

    def Agregar_Libro(self, nombre, paginas, stock):

        self.nombre = nombre
        self.paginas = paginas
        self.stock = stock
        libros.append({"Libro": nombre,
                       "Páginas": paginas,
                       "Stock": stock})

    def Listar_Libros(self):
        return libros


l = Libro()
l.Agregar_Libro("Viajero Solitario", 344, 40)
l.Agregar_Libro("Los hermanos Karamazov", 267, 29)
print(l.Listar_Libros())
