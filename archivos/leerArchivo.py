archivo=open('pruebaA.txt','r',encoding='utf8') 
#print(archivo.read()) #metodo read lee todo el archivo 

#leer algunos caracteres 
print(archivo.read(5)) 

#leer lineas completas 
print(archivo.readline()) 

#iterar el archivo 
for linea in archivo: 
    print(linea) 
    

#leer lineas 
print(archivo.readlines()) 

#acceder a una linea de la lista 
print(archivo.readlines()[2]) 

#abrimos un nuevo archivo 
#a - anexar informacionv
archivo2=open('copia.txt','a') 
archivo2.write(archivo.read())
