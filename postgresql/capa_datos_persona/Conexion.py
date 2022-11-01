from logger_base import *
import psycopg2 as bd 
import sys
class Conexion: 
    _DATABASE='test_db' 
    _USERNAME='postgres' 
    _PASSWORD='admin' 
    _DB_PORT='5432'
    _HOST ='127.0.0.1' 
    _conexion =None 
    _cursor=None 

#obtener conexion a la base de datos a travaes de un metodo
    @classmethod 
    def obtener_conexion(cls): 
        if cls._conexion is None: #si conexion es None se crea uno nuevo
            try:  
                cls._conexion =bd.connect(host=cls._HOST, 
                                          user=cls._USERNAME, 
                                          password=cls._PASSWORD, 
                                          port=cls._DB_PORT, 
                                          database=cls._DATABASE) 
                log.debug(f'Conexión exitosa: {cls._conexion} ') 
                return cls._conexion
            except Exception as e: 
                log.error(f'Ocurrió una excepcion al obtener la conexion {e}')
                sys.exit() 
        else: 
            return cls._conexion 
    @classmethod
    def obtener_cursor(cls): 
        if cls._cursor is None: #si el cursor es none se define uno nuevo
            try: 
                cls._cursor=cls.obtener_conexion().cursor() #se usa el metodo de conexion anterior
                log.debug(f'Se abrio correctamente el cursor {cls._cursor}') 
                return cls._cursor
            except Exception as e: 
                log.error(f'Ocurrió una excepcion al obtener el cursor: {e}') 
                sys.exit() #cierra por completo el programa
        else: 
            return cls._cursor 

if __name__=='__main__': 
    Conexion.obtener_conexion() 
    Conexion.obtener_cursor() 

