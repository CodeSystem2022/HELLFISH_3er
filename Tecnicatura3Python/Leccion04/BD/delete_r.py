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

            sentencia = "DELETE FROM persona WHERE \"idPersona\"=%s"

            # entrada = input("Ingrese número de registro a eliminar: ")
            # valores = (entrada,)

            # valores = (7,)
            valores = "7"

            cursor.execute(sentencia, valores)

            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")

except Exception as e:
    print(f"Error - {e}")

finally:
    # Cerramos conexión
    conexion.close()
