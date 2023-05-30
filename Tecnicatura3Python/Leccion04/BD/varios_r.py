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
            sentencia = "SELECT * FROM persona WHERE \"idPersona\" IN %s"
            # entrada = input("Ingrese id_persona a buscar (separados por coma): ")
            # llaves_primarias = (tuple(entrada.split(", ")),)
            llaves_primarias = ((1, 2, 3),)
            cursor.execute(sentencia, llaves_primarias)
            # Registramos datos
            registros = cursor.fetchall()  # devuelve una tupla con los datos
            for registro in registros:
                print(registro)

except Exception as e:
    print(f"Error - {e}")

finally:
    # Cerramos conexión
    conexion.close()
