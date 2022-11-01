class PersonaH: 
    def __init__(self, nombre,edad):
        self.nombre = nombre 
        self.edad = edad
    
    def __str__(self):#sobreescribir el init
            return f'Persona:  {self.nombre} {self.edad}'
class Empleado(PersonaH): #se pone la clase de la cual se va a heredar 
    def __init__(self, nombre,edad, sueldo):
        super().__init__(nombre,edad)  #se hace el metodo super para poder usar los metodos de la clase padre
        self.sueldo=sueldo
    def __str__(self):#sobreescribir el init
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1= Empleado('Juan',18,5000) 
print(empleado1.nombre) 
print(empleado1.edad)
print(empleado1.sueldo)
