"""ProyectoWeb URL Configuration

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
from django.urls import path ,include

#estas urs son de todo el proyecto en general, asi que vamos a haver un archivo urls.py para cada aplicacion y asi que cada una tenga sus urls
urlpatterns = [
    path('admin/', admin.site.urls),  
    #asi se enlazan las urls del pryecto con las de la app
    path('',include('ProyectoWebApp.urls')), 
    #ya a la url se le debe agregar ProyectoWebApp/ 
    path('servicios/',include('servicios.urls')), #se agrega la url de la app servicios 
    path('blog/',include('blog.urls')),
    path('contacto/',include('contacto.urls'))
]
