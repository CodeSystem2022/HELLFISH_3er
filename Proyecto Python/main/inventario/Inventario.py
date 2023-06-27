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
        
