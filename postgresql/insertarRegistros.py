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
            sentencia= 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'  
            sentencia2= 'SELECT * FROM persona'
            valores=(('Marcos', 'Cantu','mcantu@gmail.com'), 
                    ('Angel ', 'Quintana','aquintana@gmail.com'), 
                    ('Maria', 'Gonzales','mgonzales@gmail.com')) 
            cursor.executemany(sentencia,valores)  # se hace para poder ingresar varios registros
            
            #conexion.commit() se usa para guardar los cambios realizados 
            registros_insertados=cursor.rowcount  #saber cantidad de registros 
            
            print(f'Registros insertados: {registros_insertados}') 
            cursor.execute(sentencia2) 
            registros=cursor.fetchall()  
            print(registros)
            
except Exception as e: 
    print(f'ocurrio un error {e}') 
finally:
    cursor.close() 
    conexion.close() #se usa para cerrar la conexion 
    