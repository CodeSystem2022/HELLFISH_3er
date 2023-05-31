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
            sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = ("Carla", "Carlson", "CC@gmail.com")
            # execute funciona con strings o con tuplas de tuplas
            cursor.execute(sentencia, valores)
            # confirmamos y guardamos datos, se hace automático con with
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")

except Exception as e:
    print(f"Error - {e}")

finally:
    # Cerramos conexión
    conexion.close()
