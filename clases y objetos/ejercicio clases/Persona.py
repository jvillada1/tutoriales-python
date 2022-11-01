class Persona: 
    contador_persona=0  
    
    @classmethod 
    def generar_siguiente_valor(cls): #cada vez que se cree un objeto se aumenta en 1 el id
        cls.contador_persona +=1  
        return cls.contador_persona
    
    def __init__(self, nombre, edad):
        self.id_persona=Persona.generar_siguiente_valor()
        self.nombre = nombre 
        self.edad=edad 
        
    def __str__(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, id: {self.id_persona}' 

persona1=Persona('Juan', 18) 
print(persona1) 
persona2= Persona('Andres',3) 
print(persona2) 
persona3=Persona('Laura', 18) 
print(persona3)