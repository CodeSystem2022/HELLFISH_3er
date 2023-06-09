from logger_base import log

'''
Lo que vamos a hacer es una clase Persona, una clase Conection, una conexion con nuestra
base de datos de PostgreSQL y una clase PersonaDao (data access object) con los metodos
CRUD para trabjar con la clase Persona.

'''

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None): # para evitar que asignar sea obligatorio
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return f'''
            id persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}
        '''
    # Metodos getters and setters
    @property # decorador que permite convertir metodos en atributos
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email=email

# Comprobacion si ejecutamos dentro de la clase
if __name__ == '__main__':
    persona1 = Persona(1, "Juan", "Perez", "jperez@mail.com")
    log.debug(persona1)
    persona2 = Persona(nombre="Jose", apellido="Lepez", email='jlezpez@mail.com')
    log.debug(persona2)

# todo se va a cargando a nuestro archivo capa_datos log


