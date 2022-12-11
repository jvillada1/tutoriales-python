from django.urls import path  
from ProyectoWebApp import views 
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [ 
    path('',views.Home,name="Home"), 
    path('Tienda',views.Tienda,name="Tienda"),
    
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #se agrega la url de las imagenes a las demas