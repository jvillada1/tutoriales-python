
from logger_base import *
class Usuario: 
    def __init__ (self,id_usuario=None,username=None,password=None): #se pone el none pq deben de tener un valor por default
        self._id_usuario=id_usuario
        self._username=username 
        self._password=password
    
    @property 
    def id_usuario(self): 
        return self._id_usuario 
    @id_usuario.setter 
    def id_usuario (self,id_usuario): 
        self._id_persona=id_usuario
    
    @property 
    def username(self): 
        return self._username
    @username.setter 
    def username (self,username): 
        self._nombre=username 
    
    @property 
    def password(self): 
        return self._password
    @password.setter 
    def password (self,password): 
        self._password=password 
    
    
    def __str__ (self): 
        return f"""Id usuario: {self.id_usuario} 
                   username: {self.username} 
                   password: {self.password} 
                   """ 

if __name__=='__main__': 
    usuario1=Usuario(1,'jperez','123')  
    log.debug(usuario1) 





