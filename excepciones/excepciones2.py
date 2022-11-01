from numerosIdenticosException import numerosIdenticosException
from numerosNegativosEx import numerosNegativosEx
resultado=None 
##a=10 
#b=0


try: 
    a=int(input('Primer numero: ')) 
    b=int(input('Segundo Número: '))
    if a==b: 
        raise numerosIdenticosException ('numeros identicos') #Lanzar una excepcion 
    if a<0 or b<0:  
        raise numerosNegativosEx('numeros negativos')
    resultado=a/b
except ZeroDivisionError as e: 
    print(f'ZeroDivisionError - ocuriio un error {e}')    ##sintaxis parecida a try catch, para el manejo de errores 
except TypeError as t : 
    print(f'TypeError - ocurrio un error {t}') 
except Exception as ex:  #la clase exception se debe poner de ultima por qeus sino los demas no se procesan 
    print(f'Exception - Ocurrio un error {ex}')
else: #se ejecuta cuando no se lanza ninguna excepcion
    print('no se arrojó ninguna excepcion') 
finally :#se ejecuta independientemente de que haya una excepcion o no
    print('ejecución bloque finally')
print(f'Resultado: {resultado}')
print('Continuamos...')
