import psycopg2  
conexion=psycopg2.connect(
    user='postgres',     ## se deben pasar todos los valores de la base de datos creada
    password='admin',
    host='127.0.0.1', 
    port='5432', 
    database='test_db') 

#se crea un cursor para poder realizar las ocnsultas
try:
    with conexion:
        with conexion.cursor() as cursor: 
            sentencia1= 'SELECT * FROM persona WHERE id_persona IN %s' #variable que almacena la sentencia  
            #llaves_primarias=((1,2,3),)    
            entrada= input('Proporcione los valores separados por , : ') 
            llaves_primarias=(tuple(entrada.split(',')),) #tupla de tuplas y quita las comas para convertirla
            cursor.execute(sentencia1,llaves_primarias)  #se debe pasar una tupla de tuplas
            registros=cursor.fetchall()  #se recuperan todos los registros de la consulta hecha 
            for registro in registros:  #procesar registros independientemente
                print(registro)
except Exception as e: 
    print(f'ocurrio un error {e}') 
finally:
    cursor.close() 
    conexion.close() #se usa para cerrar la conexion 
    