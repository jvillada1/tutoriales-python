from django.urls import path  
from . import views 

app_name="carro"
urlpatterns = [  
    path("agregar/<int:producto_id>/",views.agregar_producto, name="agregar"), # se llama a la vista de agregar productos
    path("eliminar/<int:producto_id>/",views.eliminar_producto, name="eliminar"), # se llama a la vista de eliminar productos
    path("restar/<int:producto_id>/",views.restar_producto, name="restar"), # se llama a la vista de restarproductos
    path("limpiar/<int:producto_id>/",views.limpiar_carro, name="limpiar"), # se llama a la vista de limpiar carro 
    
]