from django.urls import path  
from ProyectoWebApp import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    path('Servicios',views.Servicios,name="Servicios"),
    path('Tienda',views.Tienda,name="Tienda"),
    path('Blog',views.Blog,name="Blog"),
    path('Contacto',views.Contacto,name="Contacto"), 
    
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #se agrega la url de las imagenes a las demas