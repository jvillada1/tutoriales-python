from django.shortcuts import render
import datetime 
import datetime
from django.http import HttpResponse  
from django.template import Template, Context # se importa para podr hacer el conexto y la template
#crear primera vista  
from django.template import loader #se importa loader para poder indicarle a django donde van a estar todas las plantillas 
from django.shortcuts import render #es para hacer simplificaciones de codigo
from gestionPedidos.models import Articulo, Clientes,Pedidos 
from django.core.mail import send_mail 
from django.conf import settings
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
        if len(producto)>20: #se hace para limitar el numero de caracteres que se pueden ingresar
            mensaje="Texto de busqueda demasiado largo" 
        else:
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
        if len(clt)>20: 
            mensaje="Texto demasiado largo" 
        else: 
            clientes=Clientes.objects.filter(nombre__icontains=clt)
            fecha=datetime.datetime.now()  
            return render(request,"resultados_clientes.html",{"clientes":clientes,"query":clt,"fecha":fecha,})  
    else: 
        mensaje="No has introducido nada" 
    return HttpResponse(mensaje)

def pedidos(request): 
    if request.GET["datos2"]: 
        ped=request.GET["datos2"]  
        if len(ped)>20: 
            mensaje="Texto demasiado largo" 
        else:
            pedidos=Pedidos.objects.filter(numero__icontains=ped) 
            fecha=datetime.datetime.now()  
            return render(request,"resultados_pedidos.html",{"pedidos":pedidos,"query":ped,"fecha":fecha}) 
    else: 
        mensaje="no se ha introducido nada" 
    return HttpResponse(mensaje) 

#vamos a crear un formulario de contacto 
def contacto(request):  
    if request.method=="POST": #comprobacion de que al pulsar el boton enviar se detecte que se está usando el post
        subject=request.POST["asunto"] #capturar la informacion del asunto 
        message=request.POST["mensaje"]+ " " + request.POST["email"]#capturar la inforacion del mensaje y la direccion del email que o envió
        email_from=settings.EMAIL_HOST_USER #la direccion que se le ha indicado en settings 
        recipient_list=["encallejone47@gmail.com"] #la direccion a la que queremos que lleguen los mensajes 
        send_mail(subject,message,email_from,recipient_list) #metodo send_mail con todos sus parametros
        
        
        
        
        return render(request,"gracias.html")
    return render(request,"contacto.html") 

def comprados(request): 
    if request.method=="POST": 
        producto=request.POST["producto"] 
        mail_compra=request.POST["email"] 
        mensaje_compra=request.POST["mensaje"]   
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["encallejone47@gmail.com"]
        send_mail("compra 1",f"se ha realizado a compra 1, el producto es: {producto}, y el mensaje compra es {mensaje_compra} desde la dirección {mail_compra}",email_from,recipient_list) 
        return render(request,"gracias.html") 
    return render(request,"comprados.html")