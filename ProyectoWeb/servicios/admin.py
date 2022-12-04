from django.contrib import admin

# Register your models here.
from servicios.models import Servicios 

class serviciosAdmin(admin.ModelAdmin): 
    list_display=('titulo','contenido','imagen','created','updated') #lo que se ve en la base de datos 
    search_fields=('titulo','contenido') #filtros para busqueda 

admin.site.register(Servicios,serviciosAdmin)