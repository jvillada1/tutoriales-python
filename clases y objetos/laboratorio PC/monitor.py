class Monitor: 
    contador_monitores=0 
    def __init__(self,marca,tamaño): 
        Monitor.contador_monitores+=1 
        self._marca=marca 
        self._id_monitor=Monitor.contador_monitores 
        self._tamaño=tamaño 
    
    @property 
    def marca(self): 
        return self._marca 
    @marca.setter 
    def marca (self,marca): 
        self._marca=marca 
    
    @property 
    def tamaño(self): 
        return self._tamaño 
        
    @tamaño.setter 
    def tamaño(self,value): 
        
        self._tamaño=value 
    
    def __str__(self):
        return f'Id monitor: {self._id_monitor} marca:{self.marca} tamaño:{self.tamaño}' 

if __name__=='__main__': 
    monitor1=Monitor('Lenovo',24) 
    print(monitor1)
    monitor2=Monitor('Hp',32) 
    print(monitor2) 
