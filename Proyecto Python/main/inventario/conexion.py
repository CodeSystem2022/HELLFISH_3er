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

