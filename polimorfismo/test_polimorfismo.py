from Empleado import Empleado 
from Gerente import Gerente 

def imprimir_detalles(objeto): 
    print(objeto)  
    print(type(objeto))  
    if isinstance(objeto,Gerente): #metodo isinstance para imprimir solo los que tengan departamento
        print(objeto.departamento) 
    else: 
        print('objeto sin departamento')
    

empleado=Empleado('Juan',300)  
imprimir_detalles(empleado) # se accede con un metodo a las 2 clases, actua dependiendo al objeto que se le pase
gerente=Gerente('Andres',300,'labor') 
imprimir_detalles(gerente)

