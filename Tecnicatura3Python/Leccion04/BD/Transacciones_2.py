import psycopg2 as bd # Esto es para poder conectarnos a Postgre

conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
        conexion.autocommit = False #esto directamente no deberia estar, se inicia la transaccion
        cursor = conexion.cursor()
        sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
        valores = ('Jorge','Prol', 'Jprol@mail.com')
        cursor.execute(sentencia, valores) #asi ejecutamos la sentencia.

        sentencia= 'UPDATE persona SET nombre=%s, email=%s WHERE id_persona=%s'
        valores= ('Juan Carlos', 'Perez', 'juancaperez@mail', 1)
        cursor.execute(sentencia, valores)

        conexion.commit() # se cierra
        print('Termina la transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()