class vehiculo: 
    def __init__(self,color,ruedas):
        self._color=color 
        self._ruedas = ruedas 
    
    @property 
    def color(self):  
        return self._color 
    @color.setter 
    def color(self,color): 
        self._color=color
    
    @property 
    def ruedas(self): 
        return self._ruedas  
    @ruedas.setter 
    def ruedas(self,ruedas): 
        self._ruedas=ruedas
    
    
    def __str__(self): 
        return f'Vehiculo   color:{self._color} ruedas {self._ruedas}' 

class coche(vehiculo): 
    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self._velocidad=velocidad 
    
    def __str__(self):
        return f'{super().__str__()} velocidad: {self._velocidad}'
    @property 
    def velocidad(self): 
        return self._velocidad 
    @velocidad.setter 
    def velocidad (self,velocidad): 
        self._velocidad =velocidad 

class Bicicleta(vehiculo): 
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas) 
        self._tipo=tipo 
    def __str__(self):
        return f'{super().__str__()} tipo: {self._tipo}' 
    
    @property 
    def tipo(self): 
        return self._tipo 
    @tipo.setter 
    def tipo(self,tipo):
        self._tipo=tipo 
