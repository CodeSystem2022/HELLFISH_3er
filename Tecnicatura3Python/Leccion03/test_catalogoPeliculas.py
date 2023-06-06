from dominio.Pelicula import Pelicula
from servicio.catalogoPelicula import CatalogoPeliculas
opcion = None
while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar pelicula")
        print("2. Listar las peliculas")
        print("3. Eliminar catalogo de peliculas")
        print("4. Salir")
        opcion=int(input("Digite una opcion de menu (1-4): "))
        if opcion == 1:
            nombrePelicula = input("Digite el nombre de la pelicula: ")
            pelicula = Pelicula(nombrePelicula)
            CatalogoPeliculas.agregar_peliculas(pelicula)
        elif opcion ==2:
            CatalogoPeliculas.listar_peliculas()

        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f"Ha ocurrido un error de tipo: {e}")
        opcion=None
    else:
        print("Salimos del programa")


