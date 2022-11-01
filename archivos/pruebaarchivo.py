try:
    with open('lol.txt','w')as archivo: 
        archivo.write('hola') 
        
        
except Exception as e: 
    print(f'Ocurrió un error {e}')