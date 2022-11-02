#profundizando tipo float 

a =3.0 
print(f'{a:.2f}')  # para mostrar solo 2 decimales


#Constructor float puede recibir int y str 
a=float(10); # lo convierte en tipo flotante 
a= float('10')# tambien se puede pasar string
print(f'{a:.2f}')  # para mostrar solo 2 decimales

#notacion exponencial (valores positivos o negativos) 
a=3e5 # 3 exponente 5
print(f'a: {a:.2f}') 

#Cualquier calculo que involucre, se promueve a float 
a=4.0+5 
print(a) 
