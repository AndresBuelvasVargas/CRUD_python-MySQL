from persona import Persona
from persona_dao import PersonaDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opción (1-5): '))
    if opcion == 1:
        usuarios = PersonaDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el nombre: ')
        email_var = input('Escribe el email: ')
        password_var = input('Escribe la contraseña: ')
        usuario = Persona(nombre=username_var, email=email_var, passe=password_var)
        usuarios_insertados = PersonaDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id a modificar: '))
        username_var = input('Escribe el nuevo nombre: ')
        email_var = input('Escribe el nuevo email: ')
        password_var = input('Escribe la nueva contraseña: ')
        usuario = Persona(id_usuario_var,username_var,email_var,password_var)
        usuarios_modificados = PersonaDAO.actualizar(usuario)
        log.info(f'Usuarios modificados: {usuarios_modificados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id a eliminar: '))
        usuario = Persona(id_persona=id_usuario_var)
        usuarios_eliminados = PersonaDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')
else: 
    log.info('Salimos de la aplicacion!')