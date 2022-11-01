
try:  
    with open('prueba5.txt','w') as archivo: 
        archivo.write('hola')
except Exception as e: 
    print(f'ocurrio un error {e}') 
    
    

