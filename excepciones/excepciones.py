resultado=None 
##a=10 
#b=0


try: 
    a=int(input('Primer numero: ')) 
    b=int(input('Segundo Número: '))
    resultado = a/b 
except ZeroDivisionError as e: 
    print(f'ZeroDivisionError - ocuriio un error {e}')    ##sintaxis parecida a try catch, para el manejo de errores 
except TypeError as t : 
    print(f'TypeError - ocurrio un error {t}') 
except Exception as ex:  #la clase exception se debe poner de ultima por qeus sino los demas no se procesan 
    print(f'Exception - Ocurrio un error {ex}')

print(f'Resultado: {resultado}')
print('Continuamos...')

##se captura el error con una clase generica llamada exception, dependiendo del caso puede ser mas especifica 
##la clase exception la de mas jerarquia 