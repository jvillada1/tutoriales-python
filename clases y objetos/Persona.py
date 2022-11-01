#creacion clase
class Persona: 
    def __init__(self,nombre,apellido,edad,*valores,**terminos): #crear metodo constructor,  robustecer el metodo init 
        
        self.nombre=nombre #atributos de la clase  
        self.apellido=apellido 
        self.edad=edad 
        self.valores=valores 
        self.terminos=terminos
        #metodos de la clase 
    def mostrar_detalle(self): #se agrega el parametro self a todo los metodos de instancia 
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
        




#se deben pasar los argumentos del constructor
persona1=Persona('Juan','Villada',18,'44455322',2,3,4, m='manzana', p= 'pera') # crear una instancia de persona 
persona1.mostrar_detalle()
#persona1.telefono ='55441122' #automaticamente se crea el telefono pero solo para la persona 1 

persona2=Persona('Karla','Gomez',30) 
persona2.mostrar_detalle()
#print(f"Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}") 

#modificar atributos de un objeto 
persona1.nombre= 'Juan Carlos' 
persona1.apellido= 'Juarez' 
persona1.edad='25'

persona1.mostrar_detalle()  #no se pone ningun parametro pq el self se pone automaticamente
persona2.mostrar_detalle()
Persona.mostrar_detalle(persona1) #si se hace con la clase, se debe pasar un objeto persona como argumento
#print(f"Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}") 

#print(f"Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}") 


