import pymysql.cursors 
from logger_base import log
import sys

class Conexion:
    _HOST = 'localhost'
    _USER = 'root'
    _PASSWORD = ''
    _DB = 'python'
    _conexion = None
    _cursor = None
    _cerrar = None
    _commit = None

    @classmethod
    def obtenerConexion(cls):
        try: 
            cls._conexion = pymysql.connect(host= cls._HOST,
                                        user= cls._USER,
                                        password= cls._PASSWORD,
                                        db= cls._DB,
                                        autocommit=True)

            log.info(f'Conexión exitosa: {cls._conexion}')
            return cls._conexion
        except Exception as e:
                log.error(f'Ocurrió una excepción {e}')
                sys.exit()
    
    @classmethod
    def obtenerCursor(cls):
        try:
            cls._cursor = cls.obtenerConexion().cursor()
            log.info(f'Se abrió correctamente el cursor: {cls._cursor}')
            return cls._cursor
        except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor {e}')
                sys.exit()  
    
    @classmethod
    def cerrarConexion(cls):
        cls._cerrar = Conexion.obtenerConexion().close()
        return cls._cerrar

    
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()