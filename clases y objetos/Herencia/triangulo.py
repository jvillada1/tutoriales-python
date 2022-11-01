from FiguraGeometrica import FiguraGeometrica 
from Color import Color   

class triangulo(FiguraGeometrica,Color): 
    def __init__(self, ancho, alto,color):
        FiguraGeometrica.__init__(self,ancho,alto) 
        Color.__init__(self,color) 
    
    def __str__(self): 
        return f'{super().__str__()} triangulo' 
    
    def calcular_area(self): 
        return (self._ancho * self._alto)/2