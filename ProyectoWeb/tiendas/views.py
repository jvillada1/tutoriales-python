from django.shortcuts import render
from .models import producto,CategoriaProductos
# Create your views here. 

#vamos a hacer el mismo proceso que con blog, vamos a mortrar los productos con sus categorias
def tienda_vista(request):   
    productos=producto.objects.all()
    return render(request,"tienda/Tienda.html",{'productos':productos}) 


def categoriaProductos(request,categoria_id): 
    categoria=CategoriaProductos.objects.get(id=categoria_id) #se pone para que traiga todos los ids de las categorias
    productos=producto.objects.filter(categorias=categoria_id) #y asi trae todos los posts con ese id
    return render(request,"tienda/categorias.html",{'categorias':categoria,'productos':productos})
