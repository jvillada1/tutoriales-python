from django.shortcuts import render
import datetime 
import datetime
from django.http import HttpResponse  
from django.template import Template, Context # se importa para podr hacer el conexto y la template
#crear primera vista  
from django.template import loader #se importa loader para poder indicarle a django donde van a estar todas las plantillas 
from django.shortcuts import render #es para hacer simplificaciones de codigo

# Create your views here.

def primera(request,num1): 
    fecha=datetime.datetime.now() 
    suma=num1+1 
    return render(request,'plantillah.html',{'fecha':fecha,'suma':suma}) 

#vamos a crear un formulario capaz de mandar info al servidor y revisar si le llega 
#de forma manual 
def busqueda_productos(request): 
    return render(request,"busqueda_productos.html") #asi se crea la vista que se va a encargar del formulario, solo es el render pq el resto lo tiene el html 

#vista buscar para ver si la información llega o no
def buscar(request): 
    mensaje="Articulo buscado: %r " %request.GET["prd"] #asi se le pide la informacion prd, que es el nombre del input tn el html }
    return HttpResponse(mensaje) 

def compras(request): 
    return render(request,"buesuqeda_productos.html") 

def comprar(request): 
    mensaje="%r"%request.GET["datos"] 
    fecha=datetime.datetime.now()  
    return render(request,"compras.html",{"fecha":fecha,"mensaje":mensaje})
    