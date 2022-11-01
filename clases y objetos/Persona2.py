
#encapsulamiento en python
class Persona2: 
    def __init__(self,nombre,apellido,edad): #crear metodo constructor,  robustecer el metodo init 
        self._nombre=nombre #para hacer un atributo privado, se le coloca _  
        self._apellido=apellido 
        self._edad=edad 
    
    @property  #hace que solo pueda acceder al atributo a traves del metodo 
    def nombre(self): 
        print('llamando metodo get')
        return self._nombre 
    
    @nombre.setter #para hacer un set
    def nombre(self,nombre): #asi se puede modificar el metodo nombre para que reciba un nombre 
        print('llamando metodo set nombre')
        self._nombre = nombre 
    
    @property 
    def apellido(self): 
        return self._apellido 
    @apellido.setter 
    def apellido(self,apellido): 
        self._apellido=apellido 
    
    @property 
    def edad (self): 
        return self._edad 
    @edad.setter 
    def edad (self,edad): 
        self._edad=edad 
    
    def mostrar_detalle(self): 
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')
    
    #metodo destructor, elimina objetos
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__': #se hace para que en otros arvhivos no se ejecute otra vez
    persona1=Persona2('Juan','Perez','28') 
    print(persona1.nombre) #llama de manera indirecta al metodo nombre, por eso no se ponen() 
    persona1.nombre='Juan Carlos' 
    print(persona1.nombre) # se modifico el valor por el metodo set 
    persona1.apellido = 'villada' 
    persona1.edad = '10' 
    persona1.mostrar_detalle()
    #para hacer una varaible de solo lectura, se hace el get pero no el set