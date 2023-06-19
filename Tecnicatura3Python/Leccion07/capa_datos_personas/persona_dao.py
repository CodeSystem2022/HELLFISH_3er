
from capa_datos_personas.Persona import Persona
from capa_datos_personas.Persona import Conexion
from logger_base import log


_SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
_INSERTAR = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
_EMILINAR = 'DELETE FROM persona WHERE id_persona=%s '

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion():
            with Conexion.obtenerConexion() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registros[0], registro[1], registro[2], registro [3])
                    personas.append(persona)
                    return personas

if __name__ == '__main__':
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        logging.debug(Persona)