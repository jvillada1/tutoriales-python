#manejo de vlores infinitos

import math  
from decimal import Decimal
infinito_positivo=float('inf') #asi se llama infinito positivo 
print(f'inf positivo: {infinito_positivo}') 

#metodo isinf 
print(f'Es infinito: {math.isinf(infinito_positivo)}') 
#devuelve true si es infinito 
infinito_positivo=2.0 
print(f'Es infinito: {math.isinf(infinito_positivo)}') 


#infinito negativo 
infinito_negativo=float('-inf') 
print(f'inf negativo: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)}') 


#otra manera Modulo math
infinito_positivo=math.inf 
print(f'infinito positivo: {infinito_positivo}') 
print(f'Es infinito: {math.isinf(infinito_positivo)}') 

#otra manera Modulo Decimal  
infinito_positivo=Decimal('Infinity') 
print(infinito_positivo) 
print(f'Es infinito: {math.isinf(infinito_positivo)}') 




