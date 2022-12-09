from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model): 
    nombre=models.CharField(max_length=50) 
    created=models.DateTimeField(auto_now_add=True) #pone la fecha de creado automaticamente
    updated=models.DateTimeField(auto_now_add=True) 
    
    class Meta: 
        verbose_name='categoria' #especificar el nombre que aparecerá en la base de datos
        verbose_name_plural='categorias' 
    def __str__(self): 
        return self.nombre

class Post(models.Model): #clase post que tendra todo el contenido de cada entrada
    titulo=models.CharField(max_length=50) 
    contenido=models.CharField(max_length=50) 
    imagen=models.ImageField(upload_to='blog',null=True,blank=True)  #el imagefield se usa para poder procesar imagenes, para usar imagenes se debe de tener pillow, el upload es para que se suba a la carptea servicios dentro de media 
    autor=models.ForeignKey(User,on_delete=models.CASCADE) #esto se aplica para que si hay contribuciones externas y se elimnia el usuario, que todo su contenido se vaya con el
    categorias=models.ManyToManyField(Categoria)           #como un post puede pertenecer a varias categorias, hay una relacion muchos a muchos entonces se debe hacer la relación
    created=models.DateTimeField(auto_now_add=True)        #pone la fecha de creado automaticamente
    updated=models.DateTimeField(auto_now_add=True) 
    
    class Meta: 
        verbose_name='post' #especificar el nombre que aparecerá en la base de datos
        verbose_name_plural='posts' 
    def __str__(self): 
        return self.titulo 

