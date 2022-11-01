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
            sentencia='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona =%s' #sentencia para actualizar un registro
            valores=(('Andres','Velazques','avelzques@gmail.com','17'), #actualizar varios registros
                    ('Juan','Canales','jcanales@gmail.com','18')) 
            cursor.executemany(sentencia,valores) 
            registros_actualizados=cursor.rowcount 
            print(f'registros actualizados: {registros_actualizados} ')
except Exception as e: 
    print(f'Ocurrió un error {e}')