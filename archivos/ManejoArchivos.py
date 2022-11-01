class ManejoArchivos:    #creando niuestro propio manje de recursos
    def __init__(self,nombre): 
        self.nombre=nombre 

    def __enter__(self): 
        print('entrando al recurso'. center(50,'-')) 
        self.nombre=open(self.nombre,'r',encoding='utf8')  
        return self.nombre 
    
    def __exit__(self,tipo_excepcion,valor_excepcion,traza_error):  
        print('Cerramos el recurso'.center(50,'-'))
        if self.nombre : #si esta apunatndo a un objeto está abierto, eentonces se llama el metodo close
            self.nombre.close()