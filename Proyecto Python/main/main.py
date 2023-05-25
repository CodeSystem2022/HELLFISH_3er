from calculadora import Calculadora
from calculadora import FunCuad
from inventario import Inventario
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def menuPrincipal(msgGuardado):
    opciones = [
        "Inventario",
        "Calculadora",
        "Salir"
    ]

    opcion = tk.messagebox.askquestion(
        "MENU PRINCIPAL",
        "Seleccione una opción",
        icon="question",
        type="yesno",
        default="yes",
        options=opciones
    )

    if opcion == "Inventario":
        menuInventario(msgGuardado)
    elif opcion == "Calculadora":
        menuCalculadora()
    else:
        # Salir
        pass

def menuInventario(msgGuardado):
    opciones = [
        "Cargar Información",
        "Ver Resultados",
        "Menu Principal"
    ]

    opcion = tk.messagebox.askquestion(
        "MENU INVENTARIO",
        "Seleccione una opción",
        icon="question",
        type="yesno",
        default="yes",
        options=opciones
    )

    # Inicialización de variables a usar
    cant = 0
    nombre = ""
    cantidad = 0.0
    precio = 0.0

    if opcion == "Cargar Información":
        cant = int(tk.simpledialog.askstring("Cargar Información", "¿Cuántos artículos hay en su inventario?", initialvalue="1"))

        if cant <= 0 or cant > 15:
            tk.messagebox.showerror("Error", "Por favor, ingrese una cantidad válida\n(números enteros entre 1-15)")
            menuInventario("")
            return

        almacen = Inventario(cant)

        for i in range(cant):
            cantidad = 0.0
            precio = 0.0

            nombre = tk.simpledialog.askstring(f"Ingrese NOMBRE del artículo {i + 1}", f"Sin Nombre {i + 1}")
            almacen.ingresarNombre(i, nombre)

            while cantidad < 1:
                cantidad = float(tk.simpledialog.askstring(f"Ingrese CANTIDAD del artículo {i + 1}", "1"))
                almacen.ingresarCantidad(i, cantidad)

            while precio <= 0:
                precio = float(tk.simpledialog.askstring(f"Ingrese PRECIO del artículo {i + 1}", "1"))
                almacen.ingresarPrecio(i, precio)

            almacen.precioSubTotal(i)

        msgGuardado = almacen.informacion(cant)
        tk.messagebox.showinfo("Información", "¡Ingreso de datos finalizado!")
        # No hay return para mostrar los resultados sin pasar por el menú

    elif opcion == "Ver Resultados":
        if msgGuardado == "":
            tk.messagebox.showerror("Error", "No se han encontrado datos")
        else:
            tk.messagebox.showinfo("Resultados", msgGuardado)
        menuInventario(msgGuardado)

    else:
        menuPrincipal(msgGuardado)

def menuCalculadora():
    opciones = [
        "Suma",
        "Resta",
        "Multiplicación",
        "División",
        "Científica",
        "Menu Principal"
    ]

    opcion = tk.messagebox.askquestion(
        "MENU CALCULADORA",
        "Seleccione una opción",
        icon="question",
        type="yesno",
        default="yes",
        options=opciones
    )

    operacion = Calculadora()
    num1 = 0
    num2 = 0
