import psycopg2  
conexion=psycopg2.connect(
    user='postgres',     ## se deben pasar todos los valores de la base de datos creada
    password='admin',
    host='127.0.0.1', 
    port='5432', 
    database='test_db') 

#ya que se van a usar transacciones, no se va a usar with 
try:  
    with conexion: 
        with conexion.cursor() as cursor:
            #comienzo transacción
            sentencia='INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'  
            valores= ('Alex','Rojas','arojas@gmail.com') 
            cursor.execute(sentencia,valores)  
    
            sentencia='UPDATE persona set nombre=%s,apellido=%s,email=%s WHERE id_persona=%s ' 
            valores= ('Juan','Perez','jperez@gmail.com',1) 
            cursor.execute(sentencia,valores)
    
            #fin transacción
except Exception as e:   #no se agrega un conexion.rollback() porque el with lo hace automaticamente
    print(f'Ocurrió un error, se hizo un rollback {e}') 
finally: 
    conexion.close()

print('Termina la transacción, se hizo commit')
