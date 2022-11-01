try: 
    archivo = open('pruebaA.txt','w',encoding='utf8')  #se usa para crear un archivo si no existe o para usar uno ya existente   
    archivo.write('Agregamos informacion al archivo') #escribir en el archivo
    archivo.write('Adios')
except Exception as e:  #por lo general con n bloque try except
    print(e) 
finally: 
    archivo.close()   #cerrar el archivo