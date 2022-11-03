from pack_tienda.libro import Libro
from pack_tienda.pelicula import Pelicula
from pack_tienda.stock_lista import Listar_Stock


while True:
    print("")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Agregar libro")
    print("4. Listar libros")
    print("5. Ver productos con poco stock")
    print("6. Salir")
    opcion = input("Que quieres hacer? (1:6) : ").strip()
    print("")
    p = Pelicula()
    l = Libro()
    if int(opcion) == 1:
        print("----- Datos de la película -----")
        nom = input("Nombre: ").strip().capitalize()
        dur = input("Duración: ").strip()
        stock = int(input("Stock: ").strip())
        p.Agregar_Pelicula(nom, dur, stock)
    elif int(opcion) == 2:
        lista = p.Listar_Peliculas()
        print(lista)
    elif int(opcion) == 3:
        print("----- Datos del libro -----")
        nom = input("Nombre: ").strip().capitalize()
        pag = int(input("Páginas: ").strip())
        stock = int(input("Stock: ").strip())
        l.Agregar_Libro(nom, pag, stock)
    elif int(opcion) == 4:
        lista = l.Listar_Libros()
        print(lista)
    elif int(opcion) == 5:
        stock = int(input("Cantidad a evaluar: ").strip())
        lista = Listar_Stock(stock, p, l)
        print("---- Productos con stock menor que "+str(stock)+"----")
        print(lista)
    elif int(opcion) == 6:
        break
    else:
        print("Opcion incorrecta.")
