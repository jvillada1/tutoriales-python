from django import forms 

class FormularioContacto(forms.Form):  #vamos a hacer formularios a traves de django
    nombre=forms.CharField(label="Nombre",required=True,) 
    emails=forms.CharField(label="Email",required=True,)
    contenido=forms.CharField(label="Contenido",widget=forms.Textarea ) #el text area es para tener un texto mas largo para ingresar  en contenido
    #el formulario se debe de llevar a la vista