from Cuadrado import Cuadrado 
from rectangulo import rectangulo 
from triangulo import* 

cuadrado1= Cuadrado(5, 'rojo')  
rectangulo1=rectangulo(5,3,'azul') 
triangulo1=triangulo(20,30,'verde')
"""print(cuadrado1.ancho) 
print(cuadrado1.alto) 
print(cuadrado1.color) 
print(rectangulo1)
""" 

print(cuadrado1) 
print(rectangulo1)  
print(triangulo1)
print(f"calculo de area de cuadrado: {cuadrado1.calcular_area()}") 
print(f"calculo de area de rectangulo: {rectangulo1.calcular_area()}") 
print(f"calculo de area de triangulo: {triangulo1.calcular_area()}")



#print(rectangulo1.calcular_area)
#metodo MRO: ayuda a saber la jerarquia de clases y metodos 
print(cuadrado1)
print(Cuadrado.mro())