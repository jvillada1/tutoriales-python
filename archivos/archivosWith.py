#with open('pruebaA.txt','r',encoding='utf8') as archivo: # se abre y se cierra al rchivo de manera automatica 
#   print(archivo.read())  

from ManejoArchivos import ManejoArchivos


with ManejoArchivos('pruebaA.txt') as archivo: 
    print(archivo.read())

