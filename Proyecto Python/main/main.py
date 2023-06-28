from calculadora.Calculadora import sumar, restar, multiplicar, dividir
from calculadora.Calculadora import potencia, raiz, logaritmo
from calculadora.FunCuad import funCuad
from inventario.Inventario import Inventario
import sys


def menuPrincipal():
    print("\n********************")
    print("***** HELLFISH *****")
    print("********************\n")
    print("1- Calculadora")
    print("2- Inventario")
    print("3- Salir")

    opcion = 0
    while (opcion < 1 or opcion > 3):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-3)")

    match opcion:
        case 1:
            menuCalculadora()
        case 2:
            menuInventario()
        case 3:
            sys.exit()


def menuCalculadora():
    print("\n*** Calculadora ***\n")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación")
    print("4- División")
    print("5- Calculadora Científica")
    print("6- Volver")
    print("7- Salir")

    opcion = 0
    while (opcion < 1 or opcion > 7):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-7)")

    match opcion:

        case 1:  # Suma

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            while True:
                try:
                    n2 = float(input("Ingrese segundo número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            input(sumar(n1, n2))
            menuCalculadora()

        case 2:  # Resta

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            while True:
                try:
                    n2 = float(input("Ingrese segundo número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            input(restar(n1, n2))
            menuCalculadora()

        case 3:  # Multiplicación

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            while True:
                try:
                    n2 = float(input("Ingrese segundo número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            input(multiplicar(n1, n2))
            menuCalculadora()

        case 4:  # División

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            while True:
                try:
                    n2 = float(input("Ingrese segundo número: "))
                    if n2 == 0:
                        raise Exception()
                    break
                except Exception:
                    print("Por favor, solo ingrese números (excepto el cero)")

            input(dividir(n1, n2))
            menuCalculadora()

        case 5:
            menuCientifica()

        case 6:
            menuPrincipal()

        case 7:
            sys.exit()


def menuCientifica():
    print("\n*** Calculadora ***")
    print("*** Científica ****\n")
    print("1- Potencia")
    print("2- Raíz Cuadrada")
    print("3- Logaritmo Natural")
    print("4- Función Cuadrática")
    print("5- Volver")
    print("6- Salir")

    opcion = 0
    while (opcion < 1 or opcion > 6):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-6)")

    n1 = n2 = "a"

    match opcion:

        case 1:  # Potencia

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            while True:
                try:
                    n2 = float(input("Ingrese segundo número: "))
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            input(potencia(n1, n2))
            menuCientifica()

        case 2:  # Raíz Cuadrada

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    if n1 <= 0:
                        raise Exception()
                    break
                except Exception:
                    print("Por favor, solo ingrese números positivos")

            input(raiz(n1))
            menuCientifica()

        case 3:  # Logaritmo Natural

            while True:
                try:
                    n1 = float(input("Ingrese primer número: "))
                    if n1 <= 0:
                        raise Exception()
                    break
                except Exception:
                    print("Por favor, solo ingrese números")

            input(logaritmo(n1))
            menuCientifica()

        case 4:  # Función Cuadrática
            cargarFC()

        case 5:  # Volver
            menuCalculadora()

        case 6:  # Salir
            sys.exit()


def cargarFC():
    print("\nPara una funcón del tipo:")
    print("\ta * x^2 + b * x + c")
    print("Ingrese los siguientes valores")

    while True:
        try:
            n1 = float(input("a = "))
            break
        except Exception:
            print("Por favor, solo ingrese números")

    while True:
        try:
            n2 = float(input("b = "))
            break
        except Exception:
            print("Por favor, solo ingrese números")

    while True:
        try:
            n3 = float(input("c = "))
            break
        except Exception:
            print("Por favor, solo ingrese números")

    datosFC = funCuad(n1, n2, n3)
    menuFunCuad(datosFC)


def menuFunCuad(datos=None):
    print("\n***** Función *****")
    print("**** Cuadrática ***\n")
    print("1- Vertice")
    print("2- Raices Reales")
    print("3- Ordenada al origen")
    print("4- Forma de la parábola")
    print("5- Volver")
    print("6- Salir")

    opcion = 0
    while (opcion < 1 or opcion > 6):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-6)")

    match opcion:
        case 1:  # Vertice
            input(datos.vertice())
            menuFunCuad(datos)

        case 2:  # Raices Reales
            input(datos.raices())
            menuFunCuad(datos)

        case 3:  # Ordenada al Origen
            input(datos.ordenada())
            menuFunCuad(datos)

        case 4:  # Forma
            input(datos.forma())
            menuFunCuad(datos)

        case 5:  # Volver
            menuCientifica()

        case 6:  # Salir
            sys.exit()


def menuInventario():
    print("\n*** Inventario ****\n")
    print("1- Cargar Información")
    print("2- Ver Resultados")
    print("3- Volver")
    print("4- Salir")

    opcion = 0
    while (opcion < 1 or opcion > 4):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-4)")

    match opcion:
        case 1:  # Ingreso de datos
            # Verificamos existencia previa de datos
            hay = Inventario.hayDatos()
            if hay:
                print("\n\t¡Se han encontrado datos!")
                while True:
                    try:
                        print("\nPara continuar y sobreescribir los datos, ingrese 1")
                        print("Para cancelar, ingrese 2")
                        eleccion = int(input())
                        if (eleccion != 1 and eleccion != 2):
                            raise Exception
                        elif eleccion == 1:
                            break
                        elif eleccion == 2:
                            menuInventario()
                    except Exception:
                        print("\nIngrese una opción válida (1-2)")
            # Borramos datos anteriores
            Inventario.borrarDatos()
            # Verificación previa al envío de datos
            # cantidad de artículos totales
            while True:
                try:
                    cant = int(input("¿Cuántos artículos hay en su inventario? "))
                    if (cant <= 0 or cant > 15):
                        raise Exception
                    else:
                        break
                except Exception:
                    print("\nIngrese una cantidad válida (1-15)")

            # por cada artículo, pedimos nombre, cantidad y precio
            elementos = range(0, cant, 1)
            for i in elementos:
                nombre = input(f"\nNOMBRE del artículo {i+1}: ")

                # Verificación cantidad válida
                while True:
                    try:
                        cantidad = int(input(f"\n\tCANTIDAD del artículo {i+1}: "))
                        if (cantidad <= 0):
                            raise Exception
                        else:
                            break
                    except Exception:
                        print("\nIngrese una cantidad válida")

                # Verificación precio válido
                while True:
                    try:
                        precio = int(input(f"\n\tPRECIO del artículo {i+1}: "))
                        if (precio <= 0):
                            raise Exception
                        else:
                            break
                    except Exception:
                        print("\nIngrese un precio válido")

                # Cargamos datos
                Inventario.insertarDatos(nombre, cantidad, precio, cantidad*precio)
            Inventario.mostrarDatos()
            input("Presione enter para volver al menú de inventario")
            menuInventario()

        case 2:  # Mostrar resultados
            Inventario.mostrarDatos()
            input("Presione enter para volver al menú de inventario")
            menuInventario()

        case 3:  # Volver al Menú Principal
            menuPrincipal()

        case 4:  # Salir
            sys.exit()


if __name__ == "__main__":
    menuPrincipal()
