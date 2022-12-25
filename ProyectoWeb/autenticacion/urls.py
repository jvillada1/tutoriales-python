from django.contrib import admin
from django.urls import path ,include 
from .views import VRegistro

#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('',VRegistro.as_view(),name="autenticar"),
]
