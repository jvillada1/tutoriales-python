#data access object 
from logger_base import *
from Persona import *
from conexionPool import * 
from cursor_del_pool import CursorDelPool
import psycopg2 

class PersonaDAO: 
    """DAO (data acces object) 
       CRUD (cREATE-READ-UPDATE-DELETE)
    """ 

    _SELECCIONAR= 'SELECT * FROM persona ORDER BY id_persona' 
    _INSERTAR='INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)' 
    _ACTUALIZAR='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s' 
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s' 

    @classmethod
    def seleccionar(cls): 
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR) 
            registros=cursor.fetchall() 
            personas=[]
            for registro in registros: 
                persona = Persona(registro[0],registro[1],registro[2],registro[3]) # se utliza el registro para crear un objeto de tipo persona 
                personas.append(persona) #mete todos los registros en una lista
            return personas 
        
    @classmethod
    def insertar(cls,persona): 
        with CursorDelPool() as cursor:
            
            valores=(persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            registros_actualizados=cursor.rowcount  
            log.debug(f'Persona insertada {persona}')
            
            return registros_actualizados  
    
    @classmethod
    def actualizar(cls,persona): 
        with CursorDelPool() as cursor: 
            valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona) 
            cursor.execute(cls._ACTUALIZAR,valores)
            registros_actualizados=cursor.rowcount  
            log.debug(f'Persona actualizada:  {persona}') 
            return registros_actualizados 
    
    @classmethod
    def eliminar(cls,persona): 
        with CursorDelPool() as cursor:  
            valores=(persona.id_persona,) 
            cursor.execute(cls._ELIMINAR,valores) 
            registros_actualizados=cursor.rowcount  
            log.debug(f'Persona actualizada:  {persona}') 
            return registros_actualizados 


if __name__=='__main__': 
    """
    #insertar
    persona1=Persona(nombre= 'alejandra',apellido='Tellez',email='atellez@gmail.com') 
    personas_insertadas=PersonaDAO.insertar(persona1)
    """
    
    
    #eliminar
    persona2=Persona(id_persona=24)
    PersonaDAO.eliminar(persona2)
    
    """
    #actualizar
    persona1=Persona(29,'Mauricio','loaiza','mloaiza@gmail.com') 
    PersonaDAO.actualizar(persona1)
    """
    #seleccionar
    personas =PersonaDAO.seleccionar() 
    for persona in personas: 
        log.debug(persona)
    #personas=PersonaDAO.insertar() 






