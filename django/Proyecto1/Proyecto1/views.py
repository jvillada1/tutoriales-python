##primero se debe importar el modulo httpresponse
import datetime
from django.http import HttpResponse  
from django.template import Template, Context # se importa para podr hacer el conexto y la template
#crear primera vista 
def saludo(request):  #tiene que recibir un request como parametro , es la primera vista 
    doc_externo=open("C:/Users/encal/OneDrive/Escritorio/Tutoriales python/curso/django/Proyecto1/Proyecto1/plantillas/plantilla1.html") #asi se abren las plantillas, como archivos 
    plt=Template(doc_externo.read()) 
    doc_externo.close()  #se abre y se cierra la comunicación
    
    #cuando el contexto es estatico, se crea vacio 
    ctx=Context() 
    
    documento=plt.render(ctx) #y para finalizar, se debe renderizar pasandole el contexto
    return HttpResponse(documento) #HACIENDOLO CON HTML 





#cada funcion que se crea es una vista nueva 

def despedida(request):  
    documento="""<html> 
    <h1> 
    me despido de mi primera pagina 
    </h1> 
    </body>  
    </html> 
    """
    return HttpResponse(documento)   

def despedidaHtml(request):  
    doc_externo=open("C:/Users/encal/OneDrive/Escritorio/Tutoriales python/curso/django/Proyecto1/Proyecto1/plantillas/plantilla2.html") 
    plt=Template(doc_externo.read())  
    doc_externo.close()
    cxt=Context() 
    documento=plt.render(cxt) 
    return HttpResponse(documento)

#los anteriores son ejemplos estaticos

#ejemplo de conetnido dinamico

def fecha(request): 
    fecha_actual=datetime.datetime.now() #programa para mostrar fecha y hora actuales 
    documento="""<html> 
    <h1> 
    Fecha y hora actuales %s              
    </h1> 
    </body>  
    </html> """ % fecha_actual 
    # en %s se guarda la variable que queremos mostrar
    return HttpResponse(documento)

#crear una vista que calcule la edad en un año futuro 

def calcula_edad(rerquest,agno):  #pasar otros parametros a una vista 
    edadActual= 19
    periodo=agno-2022 
    edadfutura=edadActual + periodo 
    documento="<html><body><h2>en el año %s tendras %s años" %(agno,edadfutura)  
    #en el %(agno,edadfutura) va en las variables que quiero que se muestren en su respectivo orden 
    return HttpResponse(documento) 

#varios parametros
def calcula_suma(request,num1,num2): 
    
    suma = num1+num2  
    documento="<html><body><h2>la suma es %s" %(suma) 
    return HttpResponse(documento)

