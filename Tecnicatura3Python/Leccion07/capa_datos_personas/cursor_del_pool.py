from logger_base import log
from conexion import Conexion

# 11.3 Creamos la Clase CursorDelPool -> Parte 1 (yo):
class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

'''

# 11.4 Pruebas del CursorDelPool -> Parte 1:
if _name_ == '_main_':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
'''
