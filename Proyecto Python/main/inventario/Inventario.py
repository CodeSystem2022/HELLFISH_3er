from inventario.conexion import Conexion


class Inventario:
    # Data access object
    # desde acá, realizamos las operaciones necesarias para la base de datos

    # Sentencias que se podrán ejecutar en este programa
    _INSERTAR = """INSERT INTO carrito (nombre, cantidad, precio, cantpre)
    VALUES (%s, %s, %s, %s)"""

    _SELECCIONAR = "SELECT * FROM carrito ORDER BY id_art;"
    _ELIMINAR = "DELETE FROM carrito"
    _REINICIAR = "SELECT setval(pg_get_serial_sequence('carrito', 'id_art'), coalesce(MIN(id_art), 1)) FROM carrito;"  # reinicia contador de id

    # Conexión
    _conexion = Conexion.obtenerConexion()

# Marcamos la existencia de datos
    @classmethod
    def hayDatos(cls):
        # Devuelve True si existen datos
        cursor = cls._conexion.cursor()
        cursor.execute(cls._SELECCIONAR)
        rows = cursor.fetchall()
        cursor.close()
        return True if rows else False

     @classmethod
    def insertarDatos(cls, nombre, cantidad, precio, cantpre):
        # Creamos cursor con el que insertaremos datos en la tabla de la bd
        # Los datos que llegan deben estar previamente verificados
        # cantpre = cantidad * precio
        try:
            cursor = cls._conexion.cursor()

            cursor.execute(cls._INSERTAR, (nombre, cantidad, precio, cantpre))

            cls._conexion.commit()
            cursor.close()

        except Exception as e:
            print(f"Error al ingresar datos: {e}")

    @classmethod
    def borrarDatos(cls):
        # Borramos datos en la tabla de la bd
        try:
            if cls.hayDatos():
                cursor = cls._conexion.cursor()

                cursor.execute(cls._ELIMINAR)
                cursor.execute(cls._REINICIAR)
                cls._conexion.commit()

                cursor.close()
                # print("Datos borrados")

            # else:
                # print("No hay datos para borrar")

        except Exception as e:
            print(f"Error al borrar datos: {e}")

    @classmethod
    def mostrarDatos(cls):
        # Imprime en pantalla los datos que se encuentren, con un tab al inicio
        try:
            # Verificamos que existan datos
            hay = cls.hayDatos()
            if hay:
                cursor = cls._conexion.cursor()

                cursor.execute(cls._SELECCIONAR)
                rows = cursor.fetchall()

                total = 0
                print("\nArtículos en inventario:")
                for row in rows:
                    total += row[4]
                    print(f"\t - Producto: {row[1]}, Cantidad: {row[2]}, Precio: {row[3]}, SubTotal: {row[4]}")

                print(f"\n\t\t - Total: {total}\n")
                cursor.close()

            else:
                print("No hay datos para mostrar")

        except Exception as e:
            print(f"Error al mostrar datos: {e}")

    @classmethod
    def cerrarConn(cls):
        print("Cerrando conexión con base de datos")
        try:
            cls._conexion.close()
        except Exception as e:
            print(f"Error al cerrar la base de datos: {e}")


if __name__ == "__main__":
    Inventario.insertarDatos("algo", 4, 4.20, 2344)
    Inventario.mostrarDatos()
    Inventario.borrarDatos()
    Inventario.borrarDatos()  # Debería no poder
    Inventario.mostrarDatos()
    Inventario.cerrarConn()
