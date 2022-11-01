#ciclo while 
"""import math 

numero=(int(input("digite un umero: "))) 

while numero <0 : 
    print("error, digite un numero positivo")
    numero=(int(input("digite un umero: "))) 

print(f"su raiz cuadrada es:{math.sqrt(numero):.2f} ")

#variables iteradoras 
i=1
while i <= 10: 
    print(i)  
    i +=1 #aumentar de 1 en uno para no estar en infinito 


#ciclo for 

#for i in [2,10,3,4] : #recorre elemento por elemento
#    print(f"elemento : {i}") 

coleccion= {"Juan":18, "andres": 20, "Julian":30} 
for i in coleccion: 
    print(i) # muestra solo las claves del diccionario 
    print(coleccion[i]) #muestra los valores 
    print(f"{i} -> {coleccion[i]} ") #mostrarlos a ambos 
    

#mas profesional... 
for clave,valor in coleccion.items(): 
    print(f"{clave} -> {valor}") 
    

cadena= "Juan" 
for j in cadena: 
    #print(f"elementos {j}") #repite por numero de letras en la cadena 
    print(j, end = " ") #para que no sea con salto de linea 
"""
#ciclos curso 
#ciclo while
condicion = True 
while condicion: 
    print("ejecutando ciclo") 
else: 
    print("ciclo terminado") 

contador = 0 
while contador<3: 
    print(contador)  
    contador += 1 #contador = contador +1
else: 
    print("fin del ciclo") 
    


numero= int(input("digite un numero: ")) 
contador3=1 
while contador3 <=numero: 
    print(contador3)  
    contador3+=1
else: 
    print("ciclo terminado")   
    

#ciclo for 
cadena = "hola" 
for letra in cadena: #itera todos los elementos de cadena
    print(letra)    
else: 
    print("fin ciclo for")

#palabra break 
for letra1 in 'Holanda':  
    if letra1 =='a': 
        print(f"letra enocntrada {letra1}") 
        break #cuando encuentra 'a' rompe todo el ciclo
else: 
    print("fin ciclo for") 
    

#palabra continue 
for i in range(6): #6 veces (digitos) 
    if i %2==0:  
        print(f'valor: {i}') 

for i in range (12): 
    if i % 2 != 0: #pregunta si es impar
        continue #ejecutar la siguiente iteracion
    print(f"valor: {i}")