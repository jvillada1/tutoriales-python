#vamos a hacer api forms, cada clase va a ser un formulario que vamos a usar 

from django import forms 

class FormularioContacto(forms.Form): # a la clase se le debe pasar el parametro forms.Forms 
    asunto=forms.CharField()   #primero decimos los campos, este es asunto 
    email=forms.EmailField()  
    mensaje=forms.CharField()  

class FormularioCompras(forms.Form): 
    producto=forms.CharField()  
    mail_compra=forms.EmailField() 
    mensaje_compra=forms.CharField()


########################comandos en shell para los formularios############################################ 

#from gestionPedidos.forms import FormularioContacto 
#miformulario=FormularioContacto() 
#print(miformulario) 
#print(miformulario.as_p()) 
#miformulario=FormularioContacto({'asunto':'prueba','email':'prueba@pildoors.es','mensaje':'mensaje de prueba'}) aparte de crear los campos, de una le damos info a estos 
#miformulario.is_valid() determinar que el formulario es valido 
#miformulario.cleaned_data devuelvce un diccionario con los datos que le hemos ingresado