import psycopg2 as bd
import sys


def crear_base_datos():
    # Creamos base de datos para trabajar
    conn = bd.connect(
            host="127.0.0.1",
            port="5432",
            user="postgres",
            password="admin"
            )

    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE hellfish3")

    conn.commit()

    cursor.close()
    conn.close()


def crear_tabla():
    # Creamos tabla en caso de que esta no exista
    conn = bd.connect(
            host="127.0.0.1",
            port="5432",
            user="postgres",
            password="admin",
            database="hellfish3"
            )

    cursor = conn.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS carrito (
            id_art SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            cantidad INTEGER NOT NULL,
            precio NUMERIC(10, 2) NOT NULL,
            cantpre NUMERIC(10, 2) NOT NULL
        );
    '''
    cursor.execute(create_table_query)

    conn.commit()
    cursor.close()
    conn.close()


class Conexion:
    _DATABASE = "hellfish3"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _HOST = "127.0.0.1"
    _DB_PORT = "5432"
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        # Devuelve una conexión con la base de datos hellfish3
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                        host=cls._HOST,
                        port=cls._DB_PORT,
                        user=cls._USERNAME,
                        password=cls._PASSWORD,
                        database=cls._DATABASE,
                        )

                # verificamos que la tabla de esa base esté creada
                crear_tabla()

                return cls._conexion

            except Exception as e:
                print(f"Error de Conexión: {e}")
                # La primera ejecución, es probable que la base de datos hellfish3
                # no exista, entonces la creamos
                # lo hacemos en este orden para evitar el error
                # de crear la misma base dos veces
            try:
                print("Creando base de datos")
                crear_base_datos()

                # verificamos que la tabla de esa base esté creada
                crear_tabla()

                # Intentamos conectar con la base de datos ya creada
                cls._conexion = bd.connect(
                        host=cls._HOST,
                        port=cls._DB_PORT,
                        user=cls._USERNAME,
                        password=cls._PASSWORD,
                        database=cls._DATABASE,
                        )

                return cls._conexion

            except Exception as e:
                print(f"Error de Conexión: {e}")
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        # Solo para pruebas
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                print(f"Se abrió cursor {cls._cursor}")
                return cls._cursor
            except Exception as e:
                print(f"Cursor Error: {e}")
                sys.exit()
        else:
            return cls._cursor


# Pruebas
if (__name__ == "__main__"):

    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
