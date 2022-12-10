from django.shortcuts import render
from blog.models import Post,Categoria
# Create your views here.
def blog_vista(request):  
    #vamos a hacer que se muestren en la pagina los servicios   
    posts=Post.objects.all()
    return render(request,"blog/Blog.html",{'posts':posts}) 

def categoria(request,categoria_id): 
    categoria=Categoria.objects.get(id=categoria_id) #se pone para que traiga todos los ids de las categorias
    posts=Post.objects.filter(categorias=categoria_id) #y asi trae todos los posts con ese id
    return render(request,"blog/categorias.html",{'categoria':categoria,'posts':posts})