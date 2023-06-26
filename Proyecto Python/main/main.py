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

