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

