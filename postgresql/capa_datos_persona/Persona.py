
from logger_base import *
class Persona: 
    def __init__ (self,id_persona=None,nombre=None,apellido=None,email=None): #se pone el none pq deben de tener un valor por default
        self._id_persona=id_persona
        self._nombre=nombre   
        self._apellido=apellido 
        self._email=email
    
    @property 
    def id_persona(self): 
        return self._id_persona 
    @id_persona.setter 
    def id_persona (self,id_persona): 
        self._id_persona=id_persona
    
    @property 
    def nombre(self): 
        return self._nombre 
    @nombre.setter 
    def nombre (self,nombre): 
        self._nombre=nombre 
    
    @property 
    def apellido(self): 
        return self._apellido 
    @apellido.setter 
    def apellido (self,apellido): 
        self._apellido=apellido 
    
    @property 
    def email(self): 
        return self._email 
    @email.setter 
    def email (self,email): 
        self._email=email 
    
    def __str__ (self): 
        return f"""Id persona: {self.id_persona} 
                   Nombre: {self.nombre} 
                   Apellido: {self.apellido} 
                   Email: {self.email}""" 

if __name__=='__main__': 
    persona1=Persona(1,'Juan','Perez','jperez@mail.com') 
    log.debug(persona1) 
    #simular un insert 
    persona1=Persona(nombre='Juan',apellido='Perez',email='jperez@mail.com') #se debe poner el = pq arriba se puso none
    log.debug(persona1) 
    #simular un delete 
    persona1=Persona(id_persona=1) 
    log.debug(persona1)


