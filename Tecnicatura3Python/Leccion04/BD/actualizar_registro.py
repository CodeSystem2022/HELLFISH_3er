# Clase 5 - ACTUALIZAR O MODIFICAR REGISTROS

import psycopg2 # Esto es para poder conectarnos a PostgreSQL

# Conectarse a la base de datos creando una conexión
conexion = psycopg2.connect(
    user='postgres',
    password='Administrador',
    host='localhost',
    port='5432',
    database='test_bd'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'

            # Cambiamos el registro:
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@mail.com', 1) # Es una tupla

            cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia

            # También modificamos el registro:
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()