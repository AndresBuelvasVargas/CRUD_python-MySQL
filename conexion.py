import pymysql as bd
from logger_base import log
import sys

class Conexion:
    _HOST = 'localhost'
    _USER = 'root'
    _PASSWORD = ''
    _DB = 'python'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try: 
                cls._conexion = bd.connect(host= cls._HOST,
                                        user= cls._USER,
                                        password= cls._PASSWORD,
                                        db= cls._DB
        )
                log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción {e}')
                sys.exit()
        else:
            return cls._conexion
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor {e}')
                sys.exit()
        else:   
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()