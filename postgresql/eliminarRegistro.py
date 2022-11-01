import psycopg2  
conexion=psycopg2.connect(
    user='postgres',     ## se deben pasar todos los valores de la base de datos creada
    password='admin',
    host='127.0.0.1', 
    port='5432', 
    database='test_db')  

try: 
    with conexion: 
        with conexion.cursor() as cursor:
            sentencia='DELETE from persona WHERE id_persona =%s' #sentencia para actualizar un registro
            valores=(('4',),('3',),('2',)) #siempre se debe poner la coma para saber que es una tupla
            cursor.executemany(sentencia,valores) 
            registros_eliminados=cursor.rowcount 
            print(f'registros actualizados: {registros_eliminados} ')
except Exception as e: 
    print(f'Ocurrió un error {e}') 

finally:  
    conexion.close()