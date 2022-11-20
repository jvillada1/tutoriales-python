from django.contrib import admin
from gestionPedidos.models import Clientes 
from gestionPedidos.models import Articulo
from gestionPedidos.models import Pedidos

# Register your models here.
#se va ingresar el codigo para el panel de administracion 
#se deben importar los modelos que vamos a manipular desde este panel 

class ClientesAdmin(admin.ModelAdmin):# se hace para saber cuantos campos queremos ver en el panel admin del modelo clientes 
    list_display=("nombre","direccion","telefono")#los campos que se van a mostrar
    search_fields=("nombre","telefono") #agrega una barra de busqueda para filtrar por nombre o por telefono


class ArticulosAdmin(admin.ModelAdmin): 
    list_filter=("seccion",) #agrega una tabla para filtrar por un campo

class PedidosAdmin(admin.ModelAdmin): 
    list_display=("numero","fecha","entregado")
    list_filter=("fecha",) 
    date_hierarchy="fecha" #añade una barra horizontal con todas las fechas posibles
#dese aqui se pueden agregar y eliminar clientes 

admin.site.register(Clientes,ClientesAdmin) # se hace para ingresar el modelo clientes al sitio admin, y tambien se usa clientesAdmin
admin.site.register(Articulo,ArticulosAdmin) 
admin.site.register(Pedidos,PedidosAdmin)