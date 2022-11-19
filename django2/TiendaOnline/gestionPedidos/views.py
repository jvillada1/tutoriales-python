from django.shortcuts import render
import datetime 
import datetime
from django.http import HttpResponse  
from django.template import Template, Context # se importa para podr hacer el conexto y la template
#crear primera vista  
from django.template import loader #se importa loader para poder indicarle a django donde van a estar todas las plantillas 
from django.shortcuts import render #es para hacer simplificaciones de codigo

# Create your views here.

def primera(request,num1): 
    fecha=datetime.datetime.now() 
    suma=num1+1 
    return render(request,'plantillah.html',{'fecha':fecha,'suma':suma})