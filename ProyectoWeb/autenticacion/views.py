from django.shortcuts import render

# Create your views here.
def autenticar(request): 
    return render(request,"registro/registro.html")