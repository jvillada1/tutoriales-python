#data access object 
from logger_base import *
from Usuario import *
from conexionPool import * 
from cursor_del_pool import CursorDelPool
import psycopg2 

class UsuarioDAO: 
    """DAO (data acces object) 
       CRUD (cREATE-READ-UPDATE-DELETE)
    """ 

    _SELECCIONAR= 'SELECT * FROM usuario ORDER BY id_usuario' 
    _INSERTAR='INSERT INTO usuario (username,password) VALUES (%s,%s)' 
    _ACTUALIZAR='UPDATE usuario SET username=%s,password=%s WHERE id_usuario=%s' 
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s' 

    @classmethod
    def seleccionar(cls): 
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR) 
            registros=cursor.fetchall() 
            usuarios=[]
            for registro in registros: 
                usuario = Usuario(registro[0],registro[1],registro[2]) # se utliza el registro para crear un objeto de tipo usuario 
                usuarios.append(usuario) #mete todos los registros en una lista
            return usuarios 
        
    @classmethod
    def insertar(cls,usuario): 
        with CursorDelPool() as cursor:
            
            valores=(usuario.username,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
            registros_actualizados=cursor.rowcount  
            log.debug(f'usuario insertado {usuario}')
            
            return registros_actualizados  
    
    @classmethod
    def actualizar(cls,usuario): 
        with CursorDelPool() as cursor: 
            valores=(usuario.username,usuario.password,usuario.id_usuario) 
            cursor.execute(cls._ACTUALIZAR,valores)
            registros_actualizados=cursor.rowcount  
            log.debug(f'usuario actualizado:  {usuario}') 
            return registros_actualizados 
    
    @classmethod
    def eliminar(cls,usuario): 
        with CursorDelPool() as cursor:  
            valores=(usuario.id_usuario,) 
            cursor.execute(cls._ELIMINAR,valores) 
            registros_actualizados=cursor.rowcount  
            log.debug(f'usuario actualizado:  {usuario}') 
            return registros_actualizados 


if __name__=='__main__': 
    """
    #insertar
    usuario1=Usuario(username='alejandra',password='567') 
    usuarios_insertadas=UsuarioDAO.insertar(usuario1)
    """
    
    """
    #eliminar
    usuario2=Usuario(id_usuario=2)
    UsuarioDAO.eliminar(usuario2)
    """
    
    
    
    #actualizar
    usuario1=Usuario(3,'ktorres','456') 
    UsuarioDAO.actualizar(usuario1)
    
    #seleccionar
    usuarios =UsuarioDAO.seleccionar() 
    for usuario in usuarios: 
        log.debug(usuario)
    #usuarios=usuarioDAO.insertar() 






