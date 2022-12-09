from django.shortcuts import render,HttpResponse

# Create your views here.

def Home(request): 
    return render(request,"home.html")




def Tienda(request):  
    return render(request,"Tienda.html")



    

def Contacto(request): 
    return render(request,"Contacto.html")

