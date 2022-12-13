from django.shortcuts import render,redirect
from .forms import FormularioContacto 
from django.core.mail import send_mail  
from django.conf import settings 
# Create your views here.

def Contacto_vista(request):   
    formulario_contacto=FormularioContacto()
    if request.method=="POST":  #primero saber si ha hecho POST para poder rescatar la info del formulario
        formulario_contacto=FormularioContacto(request.POST) #ahora si carga en el formulario la info 
        if formulario_contacto.is_valid(): #preguntar si el formulario es valido para poder guardar info 
            nombre=request.POST.get("nombre")  #estas variables se van a usar en el metodo send_mail para enviar correos
            emails=request.POST.get("emails")
            contenido=request.POST.get("contenido")  
            subject=(f'mensaje de {nombre} con el email:{emails}') 
            email_from=settings.EMAIL_HOST_USER  
            recipient_list=["encallejone47@gmail.com"] 
            try:
                send_mail(subject,contenido,email_from,recipient_list)
                return redirect("/contacto/?valido") #este return se hace para que devuelva a la pgina conacto, diciendo que la info es valida 
            except: 
                return redirect ("/contacto/?novalido") #el bloque try excpet es para que por si se pasa mal la info que redirija a otra pagina
        
    return render(request,'contacto/Contacto.html',{'miformulario':formulario_contacto})