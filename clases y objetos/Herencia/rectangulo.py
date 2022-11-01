from FiguraGeometrica import FiguraGeometrica 
from Color import Color  


class rectangulo(FiguraGeometrica,Color): 
    def __init__(self,ancho,alto,color): 
            FiguraGeometrica.__init__(self,ancho,alto)  
            Color.__init__(self,color)
    def __str__(self):
        return f'{super().__str__()} rectangulo' 
    def calcular_area(self): 
        return self._ancho*self._alto 
