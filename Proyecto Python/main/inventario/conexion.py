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
