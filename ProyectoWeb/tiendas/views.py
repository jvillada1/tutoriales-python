from django.shortcuts import render

# Create your views here.
def tienda_vista(request):  
    return render(request,"tienda/Tienda.html")
