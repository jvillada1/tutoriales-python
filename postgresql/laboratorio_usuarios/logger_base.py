import logging as log

log.basicConfig(level=log.INFO,  
                format='%(asctime)s:  %(levelname)s [%(filename)s: %(lineno)s] %(message)s', #se define el formato de la consola
                datefmt='%I:%M:%S %p', 
                handlers=[
                    log.FileHandler('capa_datos.log'), #cuando se agregue info a la consola tambien se envia a ese archivo 
                    log.StreamHandler() #manda info a la consola que estamos usando
                ]) 


#asctime == agrega el tiempo al mensaje de log
#levelname== nivel del mensaje que se manda a consola 
#filename == archivo en el que se lanzó el error o mensaje 
#lineno == agrega el numero de line al mensaje de log 
#message == mensaje que se ha agregado al log

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')  





