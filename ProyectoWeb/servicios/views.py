from django.shortcuts import render
from servicios.models import Servicios
# Create your views here.
def Servicios_vista(request):  
    #vamos a hacer que se muestren en la pagina los servicios  
    servicios=Servicios.objects.all() #importa todos los servicios que se hayan construido
    return render(request,"servicios/Servicios.html",{'servicios':servicios})