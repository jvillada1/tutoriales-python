from django.db import models

# Create your models here.
class Servicios(models.Model): 
    titulo=models.CharField(max_length=50) 
    contenido=models.CharField(max_length=50) 
    imagen=models.ImageField(upload_to='servicios') #el imagefield se usa para poder procesar imagenes, para usar imagenes se debe de tener pillow, el upload es para que se suba a la carptea servicios dentro de media
    created=models.DateTimeField(auto_now_add=True) #pone la fecha de creado automaticamente
    updated=models.DateTimeField(auto_now_add=True) 
    
    class Meta: 
        verbose_name='servicio' #especificar el nombre que aparecerá en la base de datos
        verbose_name_plural='servicios' 
    def __str__(self): 
        return self.titulo