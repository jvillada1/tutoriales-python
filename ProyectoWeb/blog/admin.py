from django.contrib import admin

# Register your models here.
from blog.models import Categoria,Post

class categoriaAdmin(admin.ModelAdmin): 
    list_display=('nombre','created','updated') #lo que se ve en la base de datos 
    search_fields=('nombre',) #filtros para busqueda  

class PostAdmin(admin.ModelAdmin): 
    list_display=('titulo','imagen','contenido','autor',)

admin.site.register(Categoria,categoriaAdmin)  
admin.site.register(Post,PostAdmin) 


