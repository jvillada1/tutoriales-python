class miClase:  
    variables_clase = 'Valor variable clase' #se asocia con la aclse en si misma  
    #s epuede compartir con todos los objetos que se creen de esa clase
    
    
    def __init__ ( self, variable_instancia): 
        self.variable_instancia =variable_instancia 
        
    
    #metodos estaticos de la clase 
    @staticmethod 
    def metodo_estatico(): #se asocia con la clase en si misma
        #no puede acceder a las variables de instancia 
        print(miClase.variables_clase) 
        
    #metodos de clase 
    @classmethod 
    def metodo_clase(cls): #recibe cls que es una referencia de la clase
        print(cls.variables_clase) 
        
    def metodo_instancia(self): 
        self.metodo_clase() 
        self.metodo_estatico() 
        print(self.variables_clase)  
        print(self.variable_instancia)
        

print(miClase.variables_clase)  
miclase1= miClase('valor variable instancia') 
print(miclase1.variable_instancia) 
print(miclase1.variables_clase)#desde el objeto tambien se puede acceder a la variable 
miclase2=miClase('Otro valor de variable instancia') 
print(miclase2.variable_instancia) 
print(miclase2.variables_clase) 

miClase.metodo_estatico() 
miClase.metodo_clase() 
miObjeto1=miClase('Variable instancia') 
miObjeto1.metodo_clase()  
miObjeto1.metodo_instancia()
#desde el contexto dinamico se puede acceder al estatico 
