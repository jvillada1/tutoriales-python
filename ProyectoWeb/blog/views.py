from django.shortcuts import render
from blog.models import Post,Categoria
# Create your views here.
def blog_vista(request):  
    #vamos a hacer que se muestren en la pagina los servicios   
    posts=Post.objects.all()
    return render(request,"blog/Blog.html",{'posts':posts})