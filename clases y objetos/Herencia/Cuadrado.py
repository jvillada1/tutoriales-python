from FiguraGeometrica import FiguraGeometrica 
from Color import Color
class Cuadrado(FiguraGeometrica,Color): #influye el orden en el que se pngan las clases
    def __init__(self, lado, color):
        self._lado= lado 
        FiguraGeometrica.__init__(self,lado,lado) #se inicializan los atributos de FiguraGeometrica 
        Color.__init__(self,color) #y tambien los de color
    
    def calcular_area(self): 
        return self._alto*self._ancho 
    
    def __str__ (self): 
        return f'Figura Geometrica de {self._alto} de alto y de {self._ancho} de ancho y de color {self._color}'