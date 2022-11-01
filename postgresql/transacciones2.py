import psycopg2  
conexion=psycopg2.connect(
    user='postgres',     ## se deben pasar todos los valores de la base de datos creada
    password='admin',
    host='127.0.0.1', 
    port='5432', 
    database='test_db') 

#ya que se van a usar transacciones, no se va a usar with 
try:  
    conexion.autocommit=False #Hace que los cmabio no se giarden automaticamente
    #comienzo transacción
    cursor=conexion.cursor() 
    sentencia='INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'  
    valores= ('Carlos','Lara','clara@gmail.com') 
    cursor.execute(sentencia,valores)  
    
    sentencia='UPDATE persona set nombre=%s,apellido=%s,email=%s WHERE id_persona=%s ' 
    valores= ('Juan Carlos','Perez','jcperez@gmail.com',1) 
    cursor.execute(sentencia,valores)
    
    #fin transacción
    conexion.commit()
    print('Termina la transacción, se hizo commit')
except Exception as e:  
    conexion.rollback() # si hay una excepcion que haga un rollback
    print(f'Ocurrió un error, se hizo un rollback {e}') 
finally: 
    conexion.close()
