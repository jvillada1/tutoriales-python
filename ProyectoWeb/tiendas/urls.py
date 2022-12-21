from django.urls import path  
from . import views  
from carro import views as vp
urlpatterns = [ 
    path('',views.tienda_vista,name="tiendas"), 
    
]