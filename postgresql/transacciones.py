# se deben ejecutar todos los queries o ninguno de ellos 

import psycopg2  
conexion=psycopg2.connect(
    user='postgres',     ## se deben pasar todos los valores de la base de datos creada
    password='admin',
    host='127.0.0.1', 
    port='5432', 
    database='test_db') 

#ya que se van a usar transacciones, no se va a suar with 
try:  
    conexion.autocommit=False #Hace que los cmabio no se giarden automaticamente
    cursor=conexion.cursor() 
    sentencia='INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'  
    valores= ('Maria','Esparza','mesparza@gmail.com') 
    cursor.execute(sentencia,valores)  
    conexion.commit()
    print('Termina la transacción')
except Exception as e:  
    conexion.rollback() # si hay una excepcion que haga un rollback
    print(f'Ocurrió un error, se hizo un rollback {e}') 
finally: 
    conexion.close()
