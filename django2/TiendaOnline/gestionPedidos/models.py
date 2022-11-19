from django.db import models

# Create your models here. 
#cada clase es una tabla de la base de datos
class Clientes(models.Model): 
    nombre=models.CharField(max_length=30) 
    direccion=models.CharField(max_length=50) 
    email=models.EmailField(blank=True,null=True) #se ponen esos dos parametros para permitir que sean opcionales
    telefono=models.CharField(max_length=7) 

class Articulo(models.Model): 
    nombre=models.CharField(max_length=30) 
    seccion=models.CharField(max_length=20) 
    precio=models.IntegerField()  
    def __str__(self): 
        return f"nombre: {self.nombre}, seccion: {self.seccion}, precio: {self.precio}" #se agrega para que no devuelva los objetos sino los strings

class Pedidos(models.Model): 
    numero=models.IntegerField() 
    fecha=models.DateField() 
    entregado=models.BooleanField() 
    

#siempre que se haga un cambio a un modelo, se debe migrar