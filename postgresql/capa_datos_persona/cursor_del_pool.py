
#se crea el cursor manualmente y se maneja con with
from logger_base import log
from conexionPool import *
class CursorDelPool: 
    def __init__(self): 
        self._conexion=None 
        self._cursor=None 
    
    def __enter__(self): #se encarga de obtener una conexion, cuando inicia el bloque with, se manda a llamar este metodo
        log.debug('Inicio del metodo with __enter__') 
        self._conexion=Conexion.obtenerConexion() 
        self._cursor=self._conexion.cursor() 
        return self._cursor 
    
    
    
    def __exit__(self,tipo_excepcion,valor_excepcion,detalle_excepcion):   
        #se ejecuta al terminar de ejecutar una sentencia sql, dependiendo del resultado se hace commit o rollback 
        log.debug('Se ejecuta metodo __exit__') 
        if valor_excepcion != None: 
            self._conexion.rollback() 
            log.error(f'Ocurrio una excepcion {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')  
            #hace un rollback si encuentra una excepcion
        else: 
            self._conexion.commit() 
            log.debug('commit de la transación') 
        self._cursor.close() 
        Conexion.liberarConexiones(self._conexion) 
        #se realiza el commit, el close de la conexion y se libera el objeto conexion 
        

if __name__=='__main__': 
    with CursorDelPool() as cursor: 
        log.debug('Dentro del bloque with') 
        cursor.execute('SELECT * FROM persona ORDER BY id_persona') 
        log.debug(cursor.fetchall()) 

