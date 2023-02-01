from django.contrib import admin
from django.urls import path ,include 
from .views import VRegistro,cerrar_sesion,logearse

#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('',VRegistro.as_view(),name="autenticacion"), 
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"), 
    path('login',logearse,name="login"),
]
