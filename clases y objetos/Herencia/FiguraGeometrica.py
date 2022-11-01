
#herencia multiple 

#clase abstracta 
from abc import ABC, abstractmethod
class FiguraGeometrica(ABC): 
    def __init__(self,alto,ancho):
        if self._validarValor(ancho): 
            self._ancho=ancho 
        else: 
            self._ancho=0 
        if self._validarValor(alto): 
            self._alto=alto 
        else: 
            self._alto=0
    def __str__(self):
        return f'su figura tiene {self._ancho} de ancho y {self._alto} de alto' 
    
    @property 
    def alto(self): 
        return self._alto 
    
    @alto.setter 
    def alto(self,alto): 
        if self._validarValor(alto): 
            self._alto=alto 
        else: 
            print("valor erroneo")

    @property
    def ancho(self): 
        return self._ancho 
    @ancho.setter 
    def ancho (self,ancho): 
        if self._validarValor(ancho): 
            self._ancho=ancho 
        else: 
            print("valor erroneo")
    def _validarValor(self,valor ):
        return True if 0< valor<10 else False 
    @abstractmethod #obliga a que las demas hijas tengan ese metodo 
    def calcular_area(self): 
        pass
