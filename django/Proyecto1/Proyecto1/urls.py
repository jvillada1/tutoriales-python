"""Proycecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
#from Proyecto1.views import saludo
from Proyecto1.views import despedida 
from Proyecto1.views import fecha 
from Proyecto1.views import calcula_edad 
from Proyecto1.views import calcula_suma 
from Proyecto1.views import despedidaHtml
from Proyecto1.views import saludo_variable 
from Proyecto1.views import prueba
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('despedida/',despedida), 
    path('fecha/',fecha) ,
    path('calcula_edad/<int:agno>',calcula_edad),  #asi se indica que se va a pasar un parametro por la url 
    path('calcula_suma/<int:num1>/<int:num2>',calcula_suma) ,
    path('despedidaHtml/',despedidaHtml), 
    path('saludo_variable/',saludo_variable), 
    path('prueba/',prueba)
]
