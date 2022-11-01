#Un pool de conexiones perminte tener varios objetos para realizar conexiones, haciendo el proceso mas rapido 

from logger_base import *
from psycopg2 import pool as pool 
import sys 

class Conexion: 
    _DATABASE='test_db' 
    _USERNAME='postgres' 
    _PASSWORD='admin' 
    _DB_PORT='5432'
    _HOST ='127.0.0.1' 
    _conexion =None 
    _cursor=None  
    _MIN_CON=1 #Todo pool tiene un minimo y un maximo de conexiones 
    _MAX_CON=5
    _pool=None 
    
    @classmethod 
    def obtenerPool(cls): 
        if cls._pool is None: # se pregunta para saber si la variable pool ha sido inicializada 
            try: 
                cls._pool=pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON, 
                                                    host=cls._HOST, 
                                                    user=cls._USERNAME, 
                                                    password=cls._PASSWORD, 
                                                    port=cls._DB_PORT, 
                                                    database=cls._DATABASE)  
            #forma mas sencilla de obtener un pool de conexiones
            #en simpleConnectionPool se pasan los argumentos minimos y maximos a parte de las variables que ya teniamos
                log.debug(f'creación del pool exitosa: {cls._pool}')  
                return cls._pool
            except Exception as e: 
                log.error(f'Ocurrió un error al obtener el pool {e}') 
                sys.exit() 
        else: 
            return cls._pool 
    
    @classmethod
    def obtenerConexion(cls): 
        conexion= cls.obtenerPool().getconn() # se encarga de regresar un objeto de conexion hacia la base de datos 
        log.debug(f'conexion obtenida del pool: {conexion}') 
        return conexion 
    
    #liberar una conexion
    @classmethod  
    def liberarConexiones(cls,conexion1): 
        cls.obtenerPool().putconn(conexion1) #coloca el objeto conexion de nuevo en el pool 
        print(f'Regresamos la conexion al pool: {conexion1}') 
    
    #cerrar conexiones 
    @classmethod 
    def cerrarConexiones(cls): 
        cls.obtenerPool().closeall() 
        log.debug('Conexiones cerradas')

if __name__=='__main__': 
    conexion1=Conexion.obtenerConexion() #se comprueba si es estan haciendo los dos objetos de conexion
    conexion2=Conexion.obtenerConexion()
    Conexion.liberarConexiones(conexion1) #se libera la conexion 1 

    







