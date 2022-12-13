from django.urls import path  
from . import views 
urlpatterns = [ 
    path('',views.tienda_vista,name="tiendas"),
]