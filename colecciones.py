#listas 
nombres=['Juan','Karla','Ricardo','Maria',] 

#imprimir la lista 
print(nombres) 

#acceder a los elementos de una lista 
print(nombres[0]) 
print(nombres[1]) 

#acceder a los elemento de manera inversa 
print(nombres[-1]) 
print(nombres[-2]) 

#imprimir un rango 
print(nombres[0:2])# sin incluir el indice 2 

#ir del inicio de la lista al indice(sin incluirlo) 
print(nombres[ :3]) 

#desde unindice hasta el final 
print(nombres[1:]) 

#cambiar un valor de la lista 
nombres[3]= 'Ivone' 
print(nombres) 

#iterar una lista 
for nombre in nombres: 
    print(nombre)
else: 
    print("fin del ciclo") 

#preguntar el largo de una lista 
print(len(nombres)) 

#agregar un nuevo elemento a la lista 
nombres.append('Lorenzo')
print(nombres) 

#insertar un elemento en un indice especifico 
nombres.insert(1,'Octavio') 
print(nombres)

#remover un elemento 
nombres.remove('Octavio') 
print(nombres) 

#remover el ultimo valor agregado 
nombres.pop() 
print(nombres) 

#eliminar en un indicie 
del nombres[0] 
print(nombres) 

#limpiar la lista 
nombres.clear() 
print(nombres) 

#borrar la lista por completo 
del nombres 
print(nombres) 
################################################################################ 

################################################################################

################################################################################ 

################################################################################ 

#tuplas  (no se pueden modificar)
#definir una tupla 

frutas = ('Naranja', 'Platano','Guayaba') 
print(frutas)
#saber el largo de una tupla 
print(len(frutas)) 

#acceder a un elemento 
print(frutas[0]) 

#navegacion inversa 
print(frutas[-1]) 

#acceder a un rango de valores 
print(frutas[0:1]) 

#recorrer los elementos de una tupla 
for fruta in frutas: 
    print(fruta,end=' ') 
    

#cambiar valor tupla 
#frutas[0] ='Pera' #error, una tupla no se puede modificar 

frutaLista= list(frutas) #pasar de una tupla a una lista 
frutaLista[0] = 'Pera'  #modificar lista 
frutas=tuple(frutaLista) 
print(frutas) 

#eliminar la tupla 
del frutas 

################################################################################ 

################################################################################

################################################################################ 

################################################################################  

#conjuntos set 
planetas = {'Marte','Jupiter','Venus'} 
print(planetas) 

#largo 
print(len(planetas)) 

#revisar si un elemetno está presente 
print('Marte'in planetas) 

#agregar un elemento 
planetas.add('Tierra') 
print(planetas) 

#no se pueden duplicar elementos 

#eliminar elemento 
planetas.remove('Tierra') 
print(planetas)  

#eliminar elemento sin arrojar error
planetas.discrad('Jupiter') 
print(planetas) 

#limpiar set 
planetas.clear() 
print(planetas) 

#eliminar el set 
del planetas 

################################################################################ 

################################################################################

################################################################################ 

################################################################################ 

#diccionarios 
#dict(key,value) 

diccionario = { 
'IDE': "Integrated Development Environment",
'OOP': "Object Oriented Programming", 
'DBMS': "Database Management System"} 
print(diccionario) 

#largo 
print(len(diccionario)) 

#acceder a un elemento (key) 
print(diccionario['IDE']) 

#otra forma de recuperar un elemento 
print(diccionario.get('OOP'))

#modificando elementos 
diccionario['IDE']='integrated development environment' 
print(diccionario) 

#recorrer los elementos clave y valor
for termino,valor in diccionario.items(): 
    print(termino,valor) 
    

#sacar solo las claves
for termino in diccionario.keys(): 
    print(termino) 
    

#sacar solo los terminos 
for valor in diccionario.values(): 
    print(valor) 
    

#comprobar existencia de algun elemento 
print('IDE' in diccionario) 

#agregar elemento 
diccionario['PK']= 'Primary Key' 
print(diccionario) 

#no es posible agregar llaves duplicadas 

#remover un elemento 
diccionario.pop('DBMS') 
print(diccionario) 

#limpiar 
diccionario.clear() 
print(diccionario) 

#eliminar el diccionario 
del diccionario