#definicion de funciones y parametros()
def mi_funcion(nombre,apellido):  #crear la funcion
    print('saludos desde mi funcion')  
    print(f'Nombre: {nombre}, Apellido: {apellido}')

def recorrer(lista1): 
    for i in lista1: 
        print(i) 


#palabra return
def sumar(numero1,numero2): 
    return numero1 +numero2 

#parametros por default 
def sumarDefault(a=0,b=0) : 
    return a+b

                            # para que se ejecute deben estar los parametros 
                            #nombre y apellido son parametros, Juan y Villada son argumentos 
mi_funcion('Juan','Villada')    #llamar la funcion (no se puede llamara antes de definir)
mi_funcion('Karla','Lara')    #llamar la funcion (no se puede llamara antes de definir)
recorrer([2,3,4,5,6])
resultado=sumar(5,3) 
print(resultado)  
resultado2=sumarDefault()  #hacer la suma con valores default 
print(resultado2) 
resultado3=sumarDefault(2,8) #sobreescribe los valores default
print(resultado3) 


######################################################################################################################## 

######################################################################################################################## 

######################################################################################################################## 

#Argumentos variables en una funcion 
def listarNombres(*nombres): #se pone * cuando no se sabe cuantos parametros se van a pasar
    for nombre in nombres: 
        print(nombre) 

listarNombres('Juan','Karla','Maria','Ernesto') 

#argumentos variables llave-valor
def listarterminos(**terminos):  #para pasar diccionarios
    for llave,valor in terminos.items(): 
        print(f'{llave}: {valor}')   

listarterminos(IDE='Integrated development environment',OOP='object oriented programing') 

#distintos tipos de datos como argumentos 
def desplegarNombres(nombres): 
    for nombre in nombres: 
        print(nombre) 

nombres=['Juan','Karla','Guillermo'] 
desplegarNombres(nombres) 
desplegarNombres('Carlos')  #va a interar una cadena 
desplegarNombres((10,11)) 
desplegarNombres([10,11])

######################################################################################################################## 

######################################################################################################################## 

######################################################################################################################## 

######################################################################################################################## 

######################################################################################################################## 

######################################################################################################################## 

#funciones recursivas 
#funciones que se llaman asi mismas 

def factorial(numero): 
    if numero== 1: 
        return 1 
    else: 
        return numero*factorial(numero-1) 

factorial(5)

