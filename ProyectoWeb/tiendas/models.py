from django.db import models

# Create your models here. 

#modelo para las cateforias de los productos
class CategoriaProductos(models.Model): 
    nombre=models.CharField(max_length=50) 
    created=models.DateTimeField(auto_now_add=True) #pone la fecha de creado automaticamente
    updated=models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name='categoria producto' #especificar el nombre que aparecerá en la base de datos
        verbose_name_plural='categorias productos' 
    def __str__(self): 
        return self.nombre



class producto(models.Model): #vamos a crear los modelos para productos y categorias
    nombre_producto=models.CharField(max_length=50) 
    precio=models.FloatField() 
    imagen=models.ImageField(upload_to='tienda',null=True,blank=True) #el imagefield se usa para poder procesar imagenes, para usar imagenes se debe de tener pillow, el upload es para que se suba a la carptea servicios dentro de media 
    disponibilidad=models.BooleanField(default=True)
    categorias=models.ForeignKey(CategoriaProductos,on_delete=models.CASCADE)#relacionamos las dos tablas
    created=models.DateTimeField(auto_now_add=True) #pone la fecha de creado automaticamente
    updated=models.DateTimeField(auto_now_add=True)  

    class Meta: 
            verbose_name='producto' #especificar el nombre que aparecerá en la base de datos
            verbose_name_plural='productos' 
    def __str__(self): 
        return self.nombre_producto