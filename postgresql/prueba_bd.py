### conexion a postgresql ###

import psycopg2  
try:
    conexion=psycopg2.connect(
        user='postgres',     ## se deben pasar todos los valores de la base de datos creada
        password='admin',
        host='127.0.0.1', 
        port='5432', 
        database='test_db')  
except Exception as e: 
    print('no se pudo conectar')

#se crea un cursor para poder realizar las ocnsultas
try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia1= 'SELECT * FROM persona' #variable que almacena la sentencia 
            sentencia2= 'SELECT * FROM persona WHERE id_persona=%s ' #%s es un place holder
            cursor.execute(sentencia1)  
            registros=cursor.fetchall()  #se recuperan todos los registros de la consulta hecha 
            id_persona=input('Proporcione el valor de id_persona: ') 
            cursor.execute(sentencia2,(id_persona,))  #se pone la tupla para pasarla como parametro
            traer1=cursor.fetchone()    #se recupera solo un registro de la consulta hecha
            print(registros)  
            print(traer1)
except Exception as e: 
    print(f'ocurrio un error {e}')  
    print('No se pudo conectar')
finally:
    cursor.close() 
    conexion.close() #se usa para cerrar la conexion