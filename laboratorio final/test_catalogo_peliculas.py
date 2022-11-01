from catalogo_peliculas import catalogoPeliculas 
from Pelicula import Pelicula 

opcion=None 
while opcion !=4:  
    try: 
        print('Opciones: ') 
        print('1. Agregar Peliculas') 
        print('2. Listar Peliculas') 
        print('3. Eliminar catalogo') 
        print('4. Salir')  
        opcion=int(input('Ingrese una opcion (1-4): '))   
        
        
        if opcion==1: 
            nombre_pelicula=input('Nombre pelicula: ')
            pelicula1=Pelicula(nombre_pelicula) 
            catalogoPeliculas.agregar_pelicula(pelicula1)   
            print(f' {pelicula1} agregada ')
        elif opcion ==2: 
            catalogoPeliculas.listar_peliculas()  
        elif opcion ==3: 
            catalogoPeliculas.eliminar_peliculas()
    except Exception as e: 
        print(f'ocurrio un error {e}') 
        opcion=None
else: 
    print('Salimos del programa')