from numerosIgualesException import NumerosIgualesException

resultado = 8

try:
    a = 10
    b = 0
    if a == b:
        raise NumerosIgualesException("Son números iguales")
    resultado = a / b
except TypeError as e:
    print(f"TypeError - Ocurrió un error: {type(e)}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError - Ocurrió un error: {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrió un error: {type(e)}")
else:
    print("No se detectó ninguna excepción.")
finally:  # Siempre se ejecuta
    print("a")

print(f"El resultado es: {resultado}")
print("seguimos")
