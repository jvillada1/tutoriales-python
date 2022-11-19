from django.contrib import admin
from gestionPedidos.models import Clientes 
from gestionPedidos.models import Articulo
from gestionPedidos.models import Pedidos

# Register your models here.
#se va ingresar el codigo para el panel de administracion 
#se deben importar los modelos que vamos a manipular desde este panel 

admin.site.register(Clientes) # se hace para ingresar el modelo clientes al sitio admin 
#dese aqui se pueden agregar y eliminar clientes 

admin.site.register(Articulo) 
admin.site.register(Pedidos)