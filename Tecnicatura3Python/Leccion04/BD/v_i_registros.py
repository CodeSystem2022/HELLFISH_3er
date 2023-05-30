# Clase 5 - INSERTAR VARIOS REGISTROS

import psycopg2 # Esto es para poder conectarnos a PostgreSQL

# Conectarse a la base de datos creando una conexión
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
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            # Insertamos varios registros:
            valores = (
                ('Carlas', 'Lara', 'claro@mail.com'),
                ('Marcas', 'Canto', 'mcanto@mail.com'),
                ('Marcela', 'Cuenca', 'cuencaM@mail.com')
            ) # Esto es una tupla de tuplas

            cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
            # conexion.commit() # Guardamos los cambios en la base de datos
            registros_insertados = cursor.rowcount # Obtenemos el número de registros insertados
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()
