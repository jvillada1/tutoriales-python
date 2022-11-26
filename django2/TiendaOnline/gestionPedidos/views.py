from django.shortcuts import render
import datetime 
import datetime
from django.http import HttpResponse  
from django.template import Template, Context # se importa para podr hacer el conexto y la template
#crear primera vista  
from django.template import loader #se importa loader para poder indicarle a django donde van a estar todas las plantillas 
from django.shortcuts import render #es para hacer simplificaciones de codigo
from gestionPedidos.models import Articulo, Clientes,Pedidos
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
    if request.GET["prd"]: #si pone el if y el else para que el usuario no mande info vacia
        
        #mensaje="Articulo buscado: %r " %request.GET["prd"] #asi se le pide la informacion prd, que es el nombre del input tn el html }  
        
        #hacerlo para que busque en la base de datos
        producto=request.GET["prd"] #almacenar el request.get en una variable 
        articulos=Articulo.objects.filter(nombre__icontains=producto) #se usa el metodo icontain para hacer la busqueda por filtro en la base de datos, es como la funcion like en sql 
        return render(request,"resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else: 
        mensaje="No has introducido nada"
    return HttpResponse(mensaje) 

def compras(request): 
    return render(request,"buesuqeda_productos.html")  

def cliente(request): 
    return render(request,"busqueda_clientes.html")

def clientes(request): 
    #mensaje="%r"%request.GET["datos"]  
    if request.GET["datos"]:
        clt=request.GET["datos"] 
        clientes=Clientes.objects.filter(nombre__icontains=clt)
        fecha=datetime.datetime.now()  
        return render(request,"resultados_clientes.html",{"clientes":clientes,"query":clt,"fecha":fecha,})  
    else: 
        mensaje="No has introducido nada" 
    return HttpResponse(mensaje)

def pedidos(request): 
    if request.GET["datos2"]: 
        ped=request.GET["datos2"] 
        pedidos=Pedidos.objects.filter(numero__icontains=ped) 
        fecha=datetime.datetime.now()  
        return render(request,"resultados_pedidos.html",{"pedidos":pedidos,"query":ped,"fecha":fecha}) 
    else: 
        mensaje="no se ha introducido nada" 
    return HttpResponse(mensaje)