from django.contrib import admin
from tiendas.models import CategoriaProductos,producto
# Register your models here.

class catProdAdmin(admin.ModelAdmin): 
    list_display=('nombre','created','updated') #lo que se ve en la base de datos 
    search_fields=('nombre',) #filtros para busqueda   
    

class productoAdmin(admin.ModelAdmin): 
    list_display=('nombre_producto','precio','imagen','disponibilidad') 

admin.site.register(CategoriaProductos,catProdAdmin)  
admin.site.register(producto,productoAdmin) 
