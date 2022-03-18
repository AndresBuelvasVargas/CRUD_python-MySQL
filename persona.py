from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, email=None, passe =None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._email = email
        self._passe = passe

    def __str__(self) -> str:
        return f'''
            Id Persona: {self._id_persona}, Nombre: {self._nombre},
            Email: {self._email}, Password: {self._passe}
        '''

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def passe(self):
        return self._passe

    @passe.setter
    def passe(self, passe):
        self._passe = passe

if __name__ == '__main__':
    persona1 = Persona(1, 'Andres', 'Buelvas', 'andy@gmail.com')
    log.debug(persona1)

    #Simular un INSERT
    persona1 = Persona(nombre='Andres', email='Buelvas', passe='andy@gmail.com')
    log.debug(persona1)

    #Simular DELETE
    persona1 = Persona(id_persona=1)
    log.debug(persona1)



