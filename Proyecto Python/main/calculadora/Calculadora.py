from math import log, sqrt
# Creamos funciones para realizar operaciones aritméticas
# y devolvemos mensajes listos para imprimir


def sumar(n1, n2):
    return f"{n1} + {n2} = {n1 + n2}"


# Función para restar:
def restar(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


# Función para multiplicar
def multiplicar(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"


def division(n1, n2):
    return f"{n1} / {n2} = {n1 / n2}"


def potencia(n1, n2):
    return f"{n1} ^ {n2} = {n1 ** n2}"


def raiz(n1):
    return f"Raiz cuadrada de {n1} = {sqrt(n1)}"


def logaritmo(n1):
    return f"Logaritmo natural de {n1} = {log(n1)}"
