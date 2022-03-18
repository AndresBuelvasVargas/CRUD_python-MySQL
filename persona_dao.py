from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create - Read - Update - Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuarios'
    _INSERTAR = 'INSERT INTO usuarios(nombre, email, pass) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET nombre=%s, email=%s, pass=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        cursor.execute(cls._SELECCIONAR)
        registros = cursor.fetchall()
        conexion.close()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)
        return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.email, persona.passe)
                cursor.execute(cls._INSERTAR, valores)
                conexion.commit()
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount
    
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.email, persona.passe, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona)
                cursor.execute(cls._ELIMINAR, valores)
                conexion.commit()
                log.debug(f'Persona eliminada: {persona}')
                return cursor.rowcount


    
if __name__ == '__main__':
    #Insertar un registro
    persona1 = Persona(nombre='Nieve', email='nieve@gmail.com', passe=555)
    personas_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    #Seleccionar objetos
    '''personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)'''

    #Actualizar un registro
    '''persona2 = Persona(1, 'Aura', 'aura@mail.com', 789)
    personas_actualizadas = PersonaDAO.actualizar(persona2)
    log.debug(f'Personas actualizadas: {personas_actualizadas}')'''

    #Eliminar registro

    '''persona3 =Persona(id_persona=18)
    personas_eliminadas = PersonaDAO.eliminar(persona3)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')'''