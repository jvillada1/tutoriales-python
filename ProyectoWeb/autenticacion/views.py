from django.shortcuts import render,redirect
from django.views.generic import View 
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login 
from django.contrib import messages

# Create your views here.
#se va a crear una clase que maneje tanto el post como el get del formulario 
class VRegistro(View): 
    def get(self,request): #será lo que renderice el formulario, vamos a usar el user creation form 
        form=UserCreationForm() #aqui se almacena el formulario 
        return render(request,"registro/registro.html",{"form":form})
    
    def post(self,request): #se encargará de enviar la info a la base de datos
        form=UserCreationForm(request.POST) #el request con todos los datos que vienen en el post 
        if form.is_valid():#primero se pregunta que el formulario sea valido
            usuario=form.save()#asi se guarda la info en el usuario 
            login(request,usuario) #se mete la peticion y el usuario para que ya esté logeado con esa informacion 
            return redirect('/home/')
        else: 
            for msg in form.error_messages: #se deben recorrer todos los errores que se prersenten y por cada uno que haya lo debe de mostrar 
                messages.error(request,form.error_messages[msg]) #se llama al messages.error para que mire los que hay en la peticion y en el formulario 
            return render(request,"registro/registro.html",{"form":form}) #que devuelva al formulario
                