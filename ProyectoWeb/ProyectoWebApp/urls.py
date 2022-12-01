from django.urls import path  
from ProyectoWebApp import views 

urlpatterns = [ 
    path('',views.Home,name="Home"), 
    path('Servicios',views.Servicios,name="Servicios"),
    path('Tienda',views.Tienda,name="Tienda"),
    path('Blog',views.Blog,name="Blog"),
    path('Contacto',views.Contacto,name="Contacto"),
    
]
