from teclado import* 
from Computadora import* 
from Raton import* 
from monitor import * 
from Orden import * 


teclado1=teclado('HP','USB') 
raton1= Raton('HP', 'USB') 
monitor1=Monitor('HP',15)
computadora1=Computadora('HP',monitor1,teclado1,raton1)


teclado2=teclado('Acer', 'Bluetooth') 
raton2=Raton('Acer', 'Bluetooth') 
monitor2=Monitor('Acer', 27 ) 
computadora2=Computadora('Acer',monitor2,teclado2,raton2)   


teclado3=teclado('Razer','USB') 
raton3=Raton('Razer','USB') 
monitor3=Monitor('Razer', 32) 
computadora3=Computadora('Razer',monitor3,teclado3,raton3)
computadoras1=[computadora1,computadora2] 

orden1=orden(computadoras1)  
orden1.agregarComputadoras(computadora3)
print(orden1) 

teclado4=teclado('Asus','Bluetooth') 
raton4=Raton('Asus','USB') 
monitor4=Monitor('Asus',45) 
computadora4=Computadora('Asus',monitor4,teclado4,raton4) 
computadoras2=[computadora4] 
orden2=orden(computadoras2) 
print(orden2) 
