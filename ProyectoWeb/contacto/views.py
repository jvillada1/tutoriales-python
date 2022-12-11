from django.shortcuts import render,redirect
from .forms import FormularioContacto
# Create your views here.

def Contacto_vista(request):   
    formulario_contacto=FormularioContacto()
    if request.method=="POST":  #primero saber si ha hecho POST para poder rescatar la info del formulario
        formulario_contacto=FormularioContacto(request.POST) #ahora si carga en el formulario la info 
        if formulario_contacto.is_valid(): #preguntar si el formulario es valido para poder guardar info 
            nombre=request.POST.get("nombre")  
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            return redirect("/contacto/?valido") #este return se hace para que devuelva a la pgina conacto, diciendo que la info es valida
        
    return render(request,'contacto/Contacto.html',{'miformulario':formulario_contacto})