import psycopg2 as bd
import sys


def crear_base_datos():
    conn = bd.connect(
            host="127.0.0.1",
            port="5432",
            user="postgres",
            password="admin"
            )

    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE hellfish3")
    print("base de datos creada correctamente")

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

    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS hellfish3 (id_art VARCHAR(255), nombre VARCHAR(255), cantidad VARCHAR(255), precio VARCHAR(255));")
    print("tabla creada correctamente")

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
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                        host=cls._HOST,
                        port=cls._DB_PORT,
                        user=cls._USERNAME,
                        password=cls._PASSWORD,
                        database=cls._DATABASE,
                        )
                print(f"Conexión exitosa: {cls._conexion}")
                return cls._conexion

            except Exception as e:
                print(f"Conexión Error: {e}")
            try:
                print("Intentando otra cosa...")

                crear_base_datos()

                cls._conexion = bd.connect(
                        host=cls._HOST,
                        port=cls._DB_PORT,
                        user=cls._USERNAME,
                        password=cls._PASSWORD,
                        database=cls._DATABASE,
                        )

                print(f"Conexión exitosa: {cls._conexion}")
                return cls._conexion
            except Exception as e:
                print(f"Conexión Error: {e}")
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
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


if (__name__ == "__main__"):

    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
    crear_tabla()
