class Persona: 
    def __init__(self,nombre,edad):
        self.nombre = nombre  
        self.edad=edad
    
    def __add__(self,otro): #se tiene que sobreescribir el metodo __add__
        return self.nombre + otro.nombre  
    
    def __sub__(self,otro): 
        return self.edad - otro.edad

persona1=Persona('juan',19) 
persona2=Persona('David',10) 
print(persona1+persona2) 
print(persona1-persona2)