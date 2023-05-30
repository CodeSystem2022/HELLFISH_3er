import psycopg2  # Conexión a postgres

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_bd"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            # sentencia = "SELECT * FROM persona"
            # sentencia = "SELECT \"idPersona\", nombre FROM persona"
            # sentencia = "SELECT * FROM persona WHERE \"idPersona\" = 1"
            sentencia = "SELECT * FROM persona WHERE \"idPersona\" IN (1, 2)"
            cursor.execute(sentencia)
            # Registramos datos
            registros = cursor.fetchall()  # devuelve una tupla con los datos
            for registro in registros:
                print(registro)

except Exception as e:
    print(f"Error - {e}")

finally:
    # Cerramos conexión
    conexion.close()
