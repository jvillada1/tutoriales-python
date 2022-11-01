from teclado import* 
from Raton import* 
from dispositivoEntrada import * 
from monitor import Monitor
class Computadora: 
    contador_computadoras=0
    def __init__ (self,nombre,monitor,teclado, raton): 
        Computadora.contador_computadoras+=1 
        self._id_computadora=Computadora.contador_computadoras 
        self._nombre=nombre 
        self._monitor=monitor 
        self._raton=raton 
        self._teclado=teclado 
        
    def __str__(self): 
        return f''' 
    {self._nombre}: {self._id_computadora}
    Monitor: {self._monitor} 
    Teclado: {self._teclado} 
    Raton: {self._raton}
    ''' 

if __name__=='__main__': 
    teclado1=teclado('HP','USB') 
    raton1= Raton('HP', 'USB') 
    monitor1=Monitor('HP',15)
    computadora1=Computadora('HP',monitor1,teclado1,raton1) 
    print(computadora1) 
    teclado2=teclado('Acer', 'Bluetooth') 
    raton2=Raton('Acer', 'Bluetooth') 
    monitor2=Monitor('Acer', 27 ) 
    computadora2=Computadora('Acer',monitor2,teclado2,raton2)  
    print(computadora2)