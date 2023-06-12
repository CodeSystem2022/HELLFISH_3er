from calculadora.Calculadora import sumar, restar, multiplicar, dividir
from calculadora.Calculadora import potencia, raiz, logaritmo


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
            return


def menuCalculadora():
    print("\n*** Calculadora ***\n")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicación")
    print("4- División")
    print("5- Calculadora Científica")
    print("6- Volver")

    opcion = 0
    while (opcion < 1 or opcion > 6):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-6)")

    n1 = n2 = "a"

    match opcion:

        case 1:  # Suma

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            while (not isinstance(n2, int)):
                try:
                    n2 = int(input("Ingrese segundo número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(sumar(n1, n2))
            menuCalculadora()

        case 2:  # Resta

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            while (not isinstance(n2, int)):
                try:
                    n2 = int(input("Ingrese segundo número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(restar(n1, n2))
            menuCalculadora()

        case 3:  # Multiplicación

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            while (not isinstance(n2, int)):
                try:
                    n2 = int(input("Ingrese segundo número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(multiplicar(n1, n2))
            menuCalculadora()

        case 4:  # División

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            while (not isinstance(n2, int)):
                try:
                    n2 = int(input("Ingrese segundo número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(dividir(n1, n2))
            menuCalculadora()

        case 5:
            menuCientifica()

        case 6:
            menuPrincipal()


def menuCientifica():
    print("\n*** Calculadora ***")
    print("*** Científica ****\n")
    print("1- Potencia")
    print("2- Raíz Cuadrada")
    print("3- Logaritmo Natural")
    print("4- Función Cuadrática")
    print("5- Volver")

    opcion = 0
    while (opcion < 1 or opcion > 5):
        try:
            opcion = int(input("\nIngrese una opción: "))
        except Exception:
            print("\nIngrese una opción válida (1-5)")

    n1 = n2 = "a"

    match opcion:

        case 1:  # Potencia

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            while (not isinstance(n2, int)):
                try:
                    n2 = int(input("Ingrese segundo número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(potencia(n1, n2))
            menuCientifica()

        case 2:  # Raíz Cuadrada

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(raiz(n1))
            menuCientifica()

        case 3:  # Logaritmo Natural

            while (not isinstance(n1, int)):
                try:
                    n1 = int(input("Ingrese primer número: "))
                except Exception:
                    print("Por favor, solo ingrese números")

            print(logaritmo(n1))
            menuCientifica()

        case 4:  # Función Cuadrática
            menuFunCuad()

        case 5:  # Volver
            menuCalculadora()


def menuFunCuad():
    pass


def menuInventario():
    n2 = int(input("Presione alt + f4 para continuar"))
    return n2


if __name__ == "__main__":
    menuPrincipal()
