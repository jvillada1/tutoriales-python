class orden: 
    contador_ordenes=0 
    def __init__(self,computadoras): 
        orden.contador_ordenes+=1 
        self._id_orden=orden.contador_ordenes 
        self._computadoras=computadoras 
        
    
    def agregarComputadoras(self,computadora): 
        self._computadoras.append(computadora) 
        
    
    def __str__(self): 
        computadoras_str=''
        for computadora in self._computadoras: 
            computadoras_str+=computadora.__str__() 
        
        return f''' 
    Orden: {self._id_orden}
    Computadoras: {computadoras_str}
    '''