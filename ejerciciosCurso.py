#ejercicio convertir numero a texto
numero = (int(input("digite un numero entre 1 y 3: "))) 

if 0<numero<=3:   
    if numero== 1: 
        numeroTexto= "Numero uno"  
        print(f" numero proporcionado: {numero} Texto: {numeroTexto}")
    elif numero == 2: 
        numeroTexto= "Numero dos" 
        print(f" numero proporcionado: {numero} Texto: {numeroTexto}")
        
        
    elif numero == 3: 
        numeroTexto= "Numero tres"
        print(f" numero proporcionado: {numero} Texto: {numeroTexto}")
        

else: 
    print("error, debe ser un numero del 1 al 3")

#ejercicio meses 
mes= int(input("digite el numero de mes (1-12): ")) 
estacion= None 
if 0<mes<13:
    if mes == 12 or mes == 1 or mes == 2: 
        estacion = 'invierno' 
        print(f"Para el mes {mes} la estacion es {estacion}") 
    elif mes == 3 or mes == 4 or mes == 5: 
        estacion = 'primavera' 
        print(f"Para el mes {mes} la estacion es {estacion}") 
    elif mes == 6 or mes == 7 or mes == 8: 
        estacion = 'verano' 
        print(f"Para el mes {mes} la estacion es {estacion}") 
    elif mes == 9 or mes == 10 or mes == 11: 
        estacion = 'otoño' 
        print(f"Para el mes {mes} la estacion es {estacion}") 
else: 
    print("mes incorrecto")


#ejercicio edades 
edad = int(input("ingrese su edad: ")) 
if 0<=edad<30: 
    if 0<=edad<=10:   
        mensaje="la infancia es increible"
        print(f"Tu edad es {edad} {mensaje}") 
    elif 10<edad<=20:  
        mensaje="muchos cambios y mucho estudio"
        print(f"Tu edad es {edad} {mensaje}") 
    elif 20<edad<30:  
        mensaje= "Amor y comienza el trabajo"
        print(f"Tu edad es {edad} {mensaje}") 

else: 
    print("valor incorrecto") 

#ejercicio calificaciones 
numCalificacion = int(input("digite su numero de calificación (0-10): ")) 

if numCalificacion>=0 and numCalificacion<=10: 
    if 0<=numCalificacion<6: 
        calificacion = 'F' 
        print(f"su calificacion es {calificacion}") 
    elif 6<=numCalificacion<7:  
        calificacion= 'D' 
        print(f"su calificacion es {calificacion}") 
    elif 7<=numCalificacion<8: 
        calificacion= 'C' 
        print(f"su calificacion es {calificacion}") 
    elif 8<=numCalificacion <9: 
        calificacion = 'B' 
        print(f"su calificacion es: {calificacion}") 
    elif 9<=numCalificacion<=10: 
        calificacion='A' 
        print(f"su calificacion es {calificacion}")
else: 
    print("numero incorrecto")


#ejercicio numeros del 0 al 5
contador1= 0 
while contador1<=5: 
    print(contador1) 
    contador1+=1
else: 
    print("fin del ciclo") 
    

#ejercicico while descendente
contador4= 5 
minimo=1 
while contador4>=minimo: 
    print(contador4) 
    contador4-=1 #-=1 para hacer en decremento
else: 
    print("fin del ciclo") 
    

#ejercicios uso de rangos 
#1 iterar un rango de 0 a 10 e imprimir los numeros divisibles por 3
for valor in range(11): 
    if valor %3!=0: 
        continue 
    print(valor) 

#2 crear un rango de 2 a 6 e imprimirlos
rango= range(2,7) 
for j in rango: 
    print(j) 

#3  crear un rango desde 3 a 10 con incremento de 2 y recorrerlo
rango1=range(3,10,2)
for valor in rango1: 
    print(valor) 

#ejercicio tuplas y listas 
tupla=(13,1,8,3,2,5,8)  
lista =[]
for valor in tupla: 
    if valor <5:  
        lista.append(valor)
print(lista) 

#ejemplo 
tupla= (10,20,30,40,50,60) 
lista=[30,40] 
for numero in tupla: 
    if numero>40: 
        lista.append(numero) 
print(lista) 

#ejercicio sumar con funciones *args 
def sumar(*args): 
    resultado=0 
    for valor in args: 
        resultado+=valor #suma en asignacion  
        #resultado = resultado +valor
    return resultado

#ejercicio multiplicar con funcionaes *args
def multiplicar(*args): 
    resultado=1
    for valor in args: 
        resultado*= valor 
    return resultado

(sumar(1,3,4,5,6)) 
multiplicar(3,5,15) 

#ejercicio funciones recursivas 

def imprimirNumeros(numero): 
    if numero >=1: 
        print(numero) 
        imprimirNumeros(numero-1)
    elif numero==0: 
        return
    elif numero<=0: 
        print("digite un numero mayor a 0")
    

imprimirNumeros(5) 
imprimirNumeros(-2)
 
#ejercicio calculadora de impuestos 


def calculadoraImpuesto(SinImpuesto,MontoImpuesto): 
    return SinImpuesto + SinImpuesto *(MontoImpuesto/100) 

SinImpuesto = (float(input("digite el pago sin impuesto: "))) 
MontoImpuesto = (float(input("digite el monto del impuesto: ")))
resultado= calculadoraImpuesto(SinImpuesto,MontoImpuesto) 
print(resultado) 


#ejercicio convertidor de temperatura 
#pasar de celsius a fahrenheit
def CelsiusFahrenheit(celsius): 
    return celsius*9/5 +32 
    
#pasar de fahrenheit a celsius
def FahrenheitCelsius(Fahrenheit): 
    return (Fahrenheit-32)/(9/5) 


celsius= float(input("digite grados celsius: ")) 
Fahrenheit=float(input("digite grados fahrenheit: ")) 

gCelsius= CelsiusFahrenheit(celsius) 
gFahrenheit= FahrenheitCelsius(Fahrenheit) 
print(f"{celsius} celsius son {gCelsius} fahrenheit") 
print(f"{Fahrenheit} fahrenheit  son {gFahrenheit} celsius")
