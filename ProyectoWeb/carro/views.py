from django.shortcuts import render
from .carro import Carro 
from tiendas.models import producto as p 
from django.shortcuts import redirect
# Create your views here.
def agregar_producto(request,producto_id): #vamos a hacer la vista agregar productos
    carro=Carro(request) #se llama a la clase carro y se crea un objeto 
    producto=p.objects.get(id=producto_id) #almacenar los id de los productos 
    carro.agregar(producto=producto) #se llama a la funcion agreagr de la clase carro con el producto que definimos antes 
    return redirect("tiendas") #que redireccione a la tienda  

def eliminar_producto(request,producto_id): #vamos a hacer la vista eliminar productos
    carro=Carro(request) #se llama a la clase carro y se crea un objeto 
    producto=p.objects.get(id=producto_id) #almacenar los id de los productos 
    carro.eliminar(producto=producto) #se llama a la funcion eliminar de la clase carro con el producto que definimos antes 
    return redirect("tiendas") #que redireccione a la tienda  

def restar_producto(request,producto_id): #vamos a hacer la vista restar productos
    carro=Carro(request) #se llama a la clase carro y se crea un objeto 
    producto=p.objects.get(id=producto_id) #almacenar los id de los productos 
    carro.restar_producto(producto=producto) #se llama a la funcion restar productos de la clase carro con el producto que definimos antes 
    return redirect("tiendas") #que redireccione a la tienda  

def limpiar_carro(request,producto_id): #y aqui la funcion para vaciar el carro 
    carro=Carro(request) 
    carro.limipar_carro() 
    return redirect("tiendas")


