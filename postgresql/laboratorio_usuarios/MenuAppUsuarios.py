from UsuarioDAO import UsuarioDAO
from Usuario import Usuario 
from logger_base import *
opcion=None
while opcion !=5: 
    try:  
        print('Opciones: ') 
        print('1. Listar Usuarios') 
        print('2. Agregar Usuario') 
        print('3. Actualizar Usuario') 
        print('4. Eliminar Usuario') 
        print('5. Salir')
        opcion=int(input('Ingrese una opcion (1-5): '))   
        
        if opcion == 1: 
            usuarios =UsuarioDAO.seleccionar() 
            for usuario in usuarios: 
                print(usuario) 
        
        elif opcion==2:   
            id_usuario=None
            username=input('Digite el username: ') 
            password=int(input('Digite el password: '))   
            usuario1=Usuario(id_usuario,username,password) 
            usuarios_insertados=UsuarioDAO.insertar(usuario1) 
            print(f'se ingreso el usuario: {usuarios_insertados}')  
        
        elif opcion == 3: 
            id_usuario=int(input('ingrese el id a actualizar: ')) 
            username=input('Digite el username: ')
            password=int(input('Digite el password: ')) 
            usuario1=Usuario(id_usuario,username,password)  
            usuarios_actualizados=UsuarioDAO.actualizar(usuario1)  
            print(usuarios_actualizados)
            
        
        elif opcion == 4: 
            id_usuario=int(input('ingrese el id a actualizar: ')) 
            usuario1=Usuario(id_usuario) 
            usarios_eliminados=UsuarioDAO.eliminar(usuario1) 
            print(usarios_eliminados)
    
    except Exception as e: 
        print(f'ocurrio un error {e}') 
        opcion=None
else: 
        print('Salimos del programa') 

